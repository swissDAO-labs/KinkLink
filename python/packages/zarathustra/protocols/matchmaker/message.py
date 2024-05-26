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

"""This module contains matchmaker's message definition."""

# pylint: disable=too-many-statements,too-many-locals,no-member,too-few-public-methods,too-many-branches,not-an-iterable,unidiomatic-typecheck,unsubscriptable-object
import logging
from typing import Any, Set, Tuple, cast

from aea.configurations.base import PublicId
from aea.exceptions import AEAEnforceError, enforce
from aea.protocols.base import Message  # type: ignore

from packages.zarathustra.protocols.matchmaker.custom_types import (
    ErrorCode as CustomErrorCode,
)
from packages.zarathustra.protocols.matchmaker.custom_types import (
    Preferences as CustomPreferences,
)
from packages.zarathustra.protocols.matchmaker.custom_types import (
    UserInfo as CustomUserInfo,
)


_default_logger = logging.getLogger(
    "aea.packages.zarathustra.protocols.matchmaker.message"
)

DEFAULT_BODY_SIZE = 4


class MatchmakerMessage(Message):
    """A protocol for agent matchmaking functionality."""

    protocol_id = PublicId.from_str("zarathustra/matchmaker:0.1.0")
    protocol_specification_id = PublicId.from_str("zarathustra/matchmaker:0.1.0")

    ErrorCode = CustomErrorCode

    Preferences = CustomPreferences

    UserInfo = CustomUserInfo

    class Performative(Message.Performative):
        """Performatives for the matchmaker protocol."""

        ERROR = "error"
        MATCHMAKING_REQUEST = "matchmaking_request"
        MATCHMAKING_RESPONSE = "matchmaking_response"
        RESULT = "result"

        def __str__(self) -> str:
            """Get the string representation."""
            return str(self.value)

    _performatives = {"error", "matchmaking_request", "matchmaking_response", "result"}
    __slots__: Tuple[str, ...] = tuple()

    class _SlotsCls:
        __slots__ = (
            "block",
            "dialogue_reference",
            "error_code",
            "error_msg",
            "message_id",
            "peer_ids",
            "performative",
            "preferences",
            "success",
            "target",
            "user_info",
        )

    def __init__(
        self,
        performative: Performative,
        dialogue_reference: Tuple[str, str] = ("", ""),
        message_id: int = 1,
        target: int = 0,
        **kwargs: Any,
    ):
        """
        Initialise an instance of MatchmakerMessage.

        :param message_id: the message id.
        :param dialogue_reference: the dialogue reference.
        :param target: the message target.
        :param performative: the message performative.
        :param **kwargs: extra options.
        """
        super().__init__(
            dialogue_reference=dialogue_reference,
            message_id=message_id,
            target=target,
            performative=MatchmakerMessage.Performative(performative),
            **kwargs,
        )

    @property
    def valid_performatives(self) -> Set[str]:
        """Get valid performatives."""
        return self._performatives

    @property
    def dialogue_reference(self) -> Tuple[str, str]:
        """Get the dialogue_reference of the message."""
        enforce(self.is_set("dialogue_reference"), "dialogue_reference is not set.")
        return cast(Tuple[str, str], self.get("dialogue_reference"))

    @property
    def message_id(self) -> int:
        """Get the message_id of the message."""
        enforce(self.is_set("message_id"), "message_id is not set.")
        return cast(int, self.get("message_id"))

    @property
    def performative(self) -> Performative:  # type: ignore # noqa: F821
        """Get the performative of the message."""
        enforce(self.is_set("performative"), "performative is not set.")
        return cast(MatchmakerMessage.Performative, self.get("performative"))

    @property
    def target(self) -> int:
        """Get the target of the message."""
        enforce(self.is_set("target"), "target is not set.")
        return cast(int, self.get("target"))

    @property
    def block(self) -> bool:
        """Get the 'block' content from the message."""
        enforce(self.is_set("block"), "'block' content is not set.")
        return cast(bool, self.get("block"))

    @property
    def error_code(self) -> CustomErrorCode:
        """Get the 'error_code' content from the message."""
        enforce(self.is_set("error_code"), "'error_code' content is not set.")
        return cast(CustomErrorCode, self.get("error_code"))

    @property
    def error_msg(self) -> str:
        """Get the 'error_msg' content from the message."""
        enforce(self.is_set("error_msg"), "'error_msg' content is not set.")
        return cast(str, self.get("error_msg"))

    @property
    def peer_ids(self) -> Tuple[str, ...]:
        """Get the 'peer_ids' content from the message."""
        enforce(self.is_set("peer_ids"), "'peer_ids' content is not set.")
        return cast(Tuple[str, ...], self.get("peer_ids"))

    @property
    def preferences(self) -> CustomPreferences:
        """Get the 'preferences' content from the message."""
        enforce(self.is_set("preferences"), "'preferences' content is not set.")
        return cast(CustomPreferences, self.get("preferences"))

    @property
    def success(self) -> bool:
        """Get the 'success' content from the message."""
        enforce(self.is_set("success"), "'success' content is not set.")
        return cast(bool, self.get("success"))

    @property
    def user_info(self) -> CustomUserInfo:
        """Get the 'user_info' content from the message."""
        enforce(self.is_set("user_info"), "'user_info' content is not set.")
        return cast(CustomUserInfo, self.get("user_info"))

    def _is_consistent(self) -> bool:
        """Check that the message follows the matchmaker protocol."""
        try:
            enforce(
                isinstance(self.dialogue_reference, tuple),
                "Invalid type for 'dialogue_reference'. Expected 'tuple'. Found '{}'.".format(
                    type(self.dialogue_reference)
                ),
            )
            enforce(
                isinstance(self.dialogue_reference[0], str),
                "Invalid type for 'dialogue_reference[0]'. Expected 'str'. Found '{}'.".format(
                    type(self.dialogue_reference[0])
                ),
            )
            enforce(
                isinstance(self.dialogue_reference[1], str),
                "Invalid type for 'dialogue_reference[1]'. Expected 'str'. Found '{}'.".format(
                    type(self.dialogue_reference[1])
                ),
            )
            enforce(
                type(self.message_id) is int,
                "Invalid type for 'message_id'. Expected 'int'. Found '{}'.".format(
                    type(self.message_id)
                ),
            )
            enforce(
                type(self.target) is int,
                "Invalid type for 'target'. Expected 'int'. Found '{}'.".format(
                    type(self.target)
                ),
            )

            # Light Protocol Rule 2
            # Check correct performative
            enforce(
                isinstance(self.performative, MatchmakerMessage.Performative),
                "Invalid 'performative'. Expected either of '{}'. Found '{}'.".format(
                    self.valid_performatives, self.performative
                ),
            )

            # Check correct contents
            actual_nb_of_contents = len(self._body) - DEFAULT_BODY_SIZE
            expected_nb_of_contents = 0
            if self.performative == MatchmakerMessage.Performative.MATCHMAKING_REQUEST:
                expected_nb_of_contents = 2
                enforce(
                    isinstance(self.user_info, CustomUserInfo),
                    "Invalid type for content 'user_info'. Expected 'UserInfo'. Found '{}'.".format(
                        type(self.user_info)
                    ),
                )
                enforce(
                    isinstance(self.preferences, CustomPreferences),
                    "Invalid type for content 'preferences'. Expected 'Preferences'. Found '{}'.".format(
                        type(self.preferences)
                    ),
                )
            elif (
                self.performative == MatchmakerMessage.Performative.MATCHMAKING_RESPONSE
            ):
                expected_nb_of_contents = 1
                enforce(
                    isinstance(self.peer_ids, tuple),
                    "Invalid type for content 'peer_ids'. Expected 'tuple'. Found '{}'.".format(
                        type(self.peer_ids)
                    ),
                )
                enforce(
                    all(isinstance(element, str) for element in self.peer_ids),
                    "Invalid type for tuple elements in content 'peer_ids'. Expected 'str'.",
                )
            elif self.performative == MatchmakerMessage.Performative.RESULT:
                expected_nb_of_contents = 2
                enforce(
                    isinstance(self.success, bool),
                    "Invalid type for content 'success'. Expected 'bool'. Found '{}'.".format(
                        type(self.success)
                    ),
                )
                enforce(
                    isinstance(self.block, bool),
                    "Invalid type for content 'block'. Expected 'bool'. Found '{}'.".format(
                        type(self.block)
                    ),
                )
            elif self.performative == MatchmakerMessage.Performative.ERROR:
                expected_nb_of_contents = 2
                enforce(
                    isinstance(self.error_code, CustomErrorCode),
                    "Invalid type for content 'error_code'. Expected 'ErrorCode'. Found '{}'.".format(
                        type(self.error_code)
                    ),
                )
                enforce(
                    isinstance(self.error_msg, str),
                    "Invalid type for content 'error_msg'. Expected 'str'. Found '{}'.".format(
                        type(self.error_msg)
                    ),
                )

            # Check correct content count
            enforce(
                expected_nb_of_contents == actual_nb_of_contents,
                "Incorrect number of contents. Expected {}. Found {}".format(
                    expected_nb_of_contents, actual_nb_of_contents
                ),
            )

            # Light Protocol Rule 3
            if self.message_id == 1:
                enforce(
                    self.target == 0,
                    "Invalid 'target'. Expected 0 (because 'message_id' is 1). Found {}.".format(
                        self.target
                    ),
                )
        except (AEAEnforceError, ValueError, KeyError) as e:
            _default_logger.error(str(e))
            return False

        return True
