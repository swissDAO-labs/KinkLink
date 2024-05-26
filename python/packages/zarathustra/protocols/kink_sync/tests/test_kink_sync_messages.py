# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2024 zarathustra
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

"""Test messages module for kink_sync protocol."""

# pylint: disable=too-many-statements,too-many-locals,no-member,too-few-public-methods,redefined-builtin
from typing import List

from aea.test_tools.test_protocol import BaseProtocolMessagesTestCase

from packages.zarathustra.protocols.kink_sync.custom_types import ErrorCode
from packages.zarathustra.protocols.kink_sync.message import KinkSyncMessage


class TestMessageKinkSync(BaseProtocolMessagesTestCase):
    """Test for the 'kink_sync' protocol message."""

    MESSAGE_CLASS = KinkSyncMessage

    def build_messages(self) -> List[KinkSyncMessage]:  # type: ignore[override]
        """Build the messages to be used for testing."""
        return [
            KinkSyncMessage(
                performative=KinkSyncMessage.Performative.INITIATE_CONVERSATION,
                message="some str",
            ),
            KinkSyncMessage(
                performative=KinkSyncMessage.Performative.ENGAGE,
                message="some str",
            ),
            KinkSyncMessage(
                performative=KinkSyncMessage.Performative.END_CONVERSATION,
                score=12,
            ),
            KinkSyncMessage(
                performative=KinkSyncMessage.Performative.ERROR,
                error_code=ErrorCode(),  # check it please!
                error_msg="some str",
            ),
        ]

    def build_inconsistent(self) -> List[KinkSyncMessage]:  # type: ignore[override]
        """Build inconsistent messages to be used for testing."""
        return [
            KinkSyncMessage(
                performative=KinkSyncMessage.Performative.INITIATE_CONVERSATION,
                # skip content: message
            ),
            KinkSyncMessage(
                performative=KinkSyncMessage.Performative.ENGAGE,
                # skip content: message
            ),
            KinkSyncMessage(
                performative=KinkSyncMessage.Performative.END_CONVERSATION,
                # skip content: score
            ),
            KinkSyncMessage(
                performative=KinkSyncMessage.Performative.ERROR,
                # skip content: error_code
                error_msg="some str",
            ),
        ]
