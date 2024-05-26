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

"""Test dialogues module for matchmaker protocol."""

# pylint: disable=too-many-statements,too-many-locals,no-member,too-few-public-methods,redefined-builtin
from aea.test_tools.test_protocol import BaseProtocolDialoguesTestCase

from packages.zarathustra.protocols.matchmaker.custom_types import Preferences, UserInfo
from packages.zarathustra.protocols.matchmaker.dialogues import (
    MatchmakerDialogue,
    MatchmakerDialogues,
)
from packages.zarathustra.protocols.matchmaker.message import MatchmakerMessage


class TestDialoguesMatchmaker(BaseProtocolDialoguesTestCase):
    """Test for the 'matchmaker' protocol dialogues."""

    MESSAGE_CLASS = MatchmakerMessage

    DIALOGUE_CLASS = MatchmakerDialogue

    DIALOGUES_CLASS = MatchmakerDialogues

    ROLE_FOR_THE_FIRST_MESSAGE = MatchmakerDialogue.Role.MATCHMAKER  # CHECK

    def make_message_content(self) -> dict:
        """Make a dict with message contruction content for dialogues.create."""
        return dict(
            performative=MatchmakerMessage.Performative.MATCHMAKING_REQUEST,
            user_info=UserInfo(),  # check it please!
            preferences=Preferences(),  # check it please!
        )
