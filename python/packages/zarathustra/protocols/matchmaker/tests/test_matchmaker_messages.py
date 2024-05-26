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

"""Test messages module for matchmaker protocol."""

# pylint: disable=too-many-statements,too-many-locals,no-member,too-few-public-methods,redefined-builtin
from typing import List

from aea.test_tools.test_protocol import BaseProtocolMessagesTestCase

from packages.zarathustra.protocols.matchmaker.custom_types import (
    ErrorCode,
    Preferences,
    UserInfo,
)
from packages.zarathustra.protocols.matchmaker.message import MatchmakerMessage


class TestMessageMatchmaker(BaseProtocolMessagesTestCase):
    """Test for the 'matchmaker' protocol message."""

    MESSAGE_CLASS = MatchmakerMessage

    def build_messages(self) -> List[MatchmakerMessage]:  # type: ignore[override]
        """Build the messages to be used for testing."""
        return [
            MatchmakerMessage(
                performative=MatchmakerMessage.Performative.MATCHMAKING_REQUEST,
                user_info=UserInfo(),  # check it please!
                preferences=Preferences(),  # check it please!
            ),
            MatchmakerMessage(
                performative=MatchmakerMessage.Performative.MATCHMAKING_RESPONSE,
                peer_ids=("some str",),
            ),
            MatchmakerMessage(
                performative=MatchmakerMessage.Performative.RESULT,
                success=True,
                block=True,
            ),
            MatchmakerMessage(
                performative=MatchmakerMessage.Performative.ERROR,
                error_code=ErrorCode(),  # check it please!
                error_msg="some str",
            ),
        ]

    def build_inconsistent(self) -> List[MatchmakerMessage]:  # type: ignore[override]
        """Build inconsistent messages to be used for testing."""
        return [
            MatchmakerMessage(
                performative=MatchmakerMessage.Performative.MATCHMAKING_REQUEST,
                # skip content: user_info
                preferences=Preferences(),  # check it please!
            ),
            MatchmakerMessage(
                performative=MatchmakerMessage.Performative.MATCHMAKING_RESPONSE,
                # skip content: peer_ids
            ),
            MatchmakerMessage(
                performative=MatchmakerMessage.Performative.RESULT,
                # skip content: success
                block=True,
            ),
            MatchmakerMessage(
                performative=MatchmakerMessage.Performative.ERROR,
                # skip content: error_code
                error_msg="some str",
            ),
        ]
