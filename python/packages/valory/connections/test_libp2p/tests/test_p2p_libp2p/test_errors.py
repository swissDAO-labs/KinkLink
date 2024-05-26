# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2022-2023 Valory AG
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""Test errors."""

# pylint: skip-file

import asyncio
import os
import platform
import subprocess  # nosec
import sys
import tempfile
from asyncio.futures import Future
from unittest.mock import Mock, patch

import pytest

from aea.configurations.base import ConnectionConfig
from aea.multiplexer import Multiplexer

from packages.valory.connections.p2p_libp2p.connection import (
    LIBP2P_NODE_MODULE_NAME,
    Libp2pNode,
    P2PLibp2pConnection,
    _golang_module_run,
    _ip_all_private_or_all_public,
)
from packages.valory.connections.p2p_libp2p.tests.base import ports
from packages.valory.connections.test_libp2p.tests.base import (
    BaseP2PLibp2pTest,
    SKIP_WINDOWS,
    _make_libp2p_connection,
    create_identity,
)
from packages.valory.protocols.acn.message import AcnMessage


class TestP2PLibp2pConnectionFailureGolangRun(BaseP2PLibp2pTest):
    """Test that golang run fails if wrong path or timeout"""

    def test_wrong_path(self) -> None:
        """Test the wrong path."""
        log_file_desc = open("log", "a", 1)
        wrong_path = tempfile.mkdtemp()
        with pytest.raises(FileNotFoundError):  # match differs based on OS
            _golang_module_run(wrong_path, LIBP2P_NODE_MODULE_NAME, [], log_file_desc)

    def test_timeout(self) -> None:
        """Test the timeout."""

        connection = _make_libp2p_connection()
        connection.node._connection_timeout = 0
        muxer = Multiplexer([connection])
        with pytest.raises(Exception, match="Couldn't connect to libp2p process"):
            muxer.connect()
        muxer.disconnect()


class TestP2PLibp2pConnectionFailureSetupNewConnection(BaseP2PLibp2pTest):
    """Test that connection constructor ensures proper configuration"""

    key_file: str

    @classmethod
    def setup_class(cls) -> None:
        """Set the test up"""

        super().setup_class()
        crypto = cls.default_crypto
        cls.identity = create_identity(crypto)
        cls.host = "localhost"
        cls.port = next(ports)
        cls.key_file = os.path.join(cls.tmp, "keyfile")
        crypto.dump(cls.key_file)

    def test_entry_peers_when_no_public_uri_provided(self) -> None:
        """Test entry peers when no public uri provided."""

        configuration = ConnectionConfig(
            libp2p_key_file=None,
            local_uri=f"{self.host}:{self.port}",
            delegate_uri=f"{self.host}:{self.port}",
            entry_peers=None,
            log_file=None,
            connection_id=P2PLibp2pConnection.connection_id,
            build_directory=self.tmp,
        )
        with pytest.raises(ValueError, match="Couldn't find connection key"):
            P2PLibp2pConnection(
                configuration=configuration, data_dir=self.tmp, identity=self.identity
            )

    def test_local_uri_provided_when_public_uri_provided(self) -> None:
        """Test local uri provided when public uri provided."""

        configuration = ConnectionConfig(
            node_key_file=self.key_file,
            public_uri=f"{self.host}:{self.port}",
            entry_peers=None,
            log_file=None,
            connection_id=P2PLibp2pConnection.connection_id,
            build_directory=self.tmp,
        )
        with pytest.raises(ValueError, match="Couldn't find connection key"):
            P2PLibp2pConnection(
                configuration=configuration, data_dir=self.tmp, identity=self.identity
            )


@SKIP_WINDOWS
def test_libp2p_connection_mixed_ip_address() -> None:
    """Test correct public uri ip and entry peers ips configuration."""
    assert _ip_all_private_or_all_public([]) is True
    assert _ip_all_private_or_all_public(["127.0.0.1", "127.0.0.1"]) is True
    assert _ip_all_private_or_all_public(["localhost", "127.0.0.1"]) is True
    assert _ip_all_private_or_all_public(["10.0.0.1", "127.0.0.1"]) is False
    assert _ip_all_private_or_all_public(["fetch.ai", "127.0.0.1"]) is False
    assert _ip_all_private_or_all_public(["104.26.2.97", "127.0.0.1"]) is False
    assert _ip_all_private_or_all_public(["fetch.ai", "acn.fetch.ai"]) is True


@pytest.mark.skipif(
    condition=(platform.system() == "Windows"),
    reason="https://github.com/golang/go/issues/51007",
)
@SKIP_WINDOWS
def test_libp2p_connection_node_config_registration_delay() -> None:
    """Test node registration delay configuration"""

    with pytest.raises(ValueError, match="must be a float number in seconds"):
        _make_libp2p_connection(peer_registration_delay="must_be_float")


@SKIP_WINDOWS
def test_build_dir_not_set() -> None:
    """Test build dir not set."""

    with tempfile.TemporaryDirectory() as data_dir:
        con = _make_libp2p_connection(data_dir=data_dir)
        con.configuration.build_directory = None
        with pytest.raises(
            ValueError, match="Connection Configuration build directory is not set!"
        ):
            P2PLibp2pConnection(
                configuration=con.configuration,
                data_dir=data_dir,
                identity=con._identity,
                crypto_store=con.crypto_store,
            )


@pytest.mark.asyncio
@SKIP_WINDOWS
async def test_reconnect_on_write_failed() -> None:
    """Test node restart on write fail."""

    con = _make_libp2p_connection()
    node = Libp2pNode(Mock(), Mock(), "tmp", "tmp")
    con.node = node
    node.pipe = Mock()
    node.pipe.write = Mock(side_effect=Exception("expected"))
    con._node_client = node.get_client()
    f = Future()
    f.set_result(None)
    with patch.object(
        con, "_restart_node", return_value=f
    ) as restart_mock, patch.object(
        con, "_ensure_valid_envelope_for_external_comms"
    ), patch.object(
        con._node_client, "make_acn_envelope_message", return_value=b"some_data"
    ), pytest.raises(
        Exception, match="expected"
    ):
        await con._send_envelope_with_node_client(Mock())

    assert node.pipe.write.call_count == 2
    restart_mock.assert_called_once()


@pytest.mark.asyncio
@SKIP_WINDOWS
async def test_reconnect_on_write_failed_reconnect_pipe() -> None:
    """Test node restart on write fail."""

    con = _make_libp2p_connection()

    node = Libp2pNode(Mock(), Mock(), "tmp", "tmp")
    f = Future()
    f.set_result(None)
    con.node = node
    node.pipe = Mock()
    node.pipe.connect = Mock(return_value=f)
    node.pipe.write = Mock(side_effect=[Exception("expected"), f])
    node.pipe.close = Mock(return_value=f)

    con._node_client = node.get_client()
    status_ok = Mock()
    status_ok.code = int(AcnMessage.StatusBody.StatusCode.SUCCESS)
    status_ok_future = Future()
    status_ok_future.set_result(status_ok)
    with patch.object(con, "_ensure_valid_envelope_for_external_comms"), patch.object(
        node, "is_proccess_running", return_value=True
    ), patch.object(
        con._node_client, "make_acn_envelope_message", return_value=b"some_data"
    ), patch.object(
        con._node_client, "wait_for_status", lambda: status_ok_future
    ):
        await con._send_envelope_with_node_client(Mock())

    assert node.pipe.write.call_count == 2
    assert node.pipe.connect.call_count == 1


@pytest.mark.asyncio
@SKIP_WINDOWS
async def test_reconnect_on_read_failed() -> None:
    """Test node restart on read fail."""

    con = _make_libp2p_connection()
    node = Libp2pNode(Mock(), Mock(), "tmp", "tmp")
    con.node = node
    node.pipe = Mock()
    node.pipe.read = Mock(side_effect=Exception("expected"))
    con._node_client = node.get_client()
    f = Future()
    f.set_result(None)
    with patch.object(
        con, "_restart_node", return_value=f
    ) as restart_mock, pytest.raises(Exception, match="expected"):
        await con._read_envelope_from_node()

    assert node.pipe.read.call_count == 2
    restart_mock.assert_called_once()

    assert node.pipe.read.call_count == 2
    restart_mock.assert_called_once()


@pytest.mark.asyncio
@SKIP_WINDOWS
async def test_node_stopped_callback() -> None:
    """Test node stopped callback called."""

    if not (
        platform.system() != "Windows"
        and sys.version_info.major == 3
        and sys.version_info.minor >= 8
    ):
        pytest.skip(
            "Not supported on this platform. Unix and python >= 3.8 supported only"
        )

    con = _make_libp2p_connection()
    con.node.logger.error = Mock()
    await con.node.start()
    subprocess.Popen.terminate(con.node.proc)
    await asyncio.sleep(2)
    con.node.logger.error.assert_called_once()
    await con.node.stop()

    con = _make_libp2p_connection()
    con.node.logger.error = Mock()
    await con.node.start()
    await con.node.stop()
    await asyncio.sleep(2)
    con.node.logger.error.assert_not_called()
