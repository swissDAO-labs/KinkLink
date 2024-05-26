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

"""Serialization module for matchmaker protocol."""

# pylint: disable=too-many-statements,too-many-locals,no-member,too-few-public-methods,redefined-builtin
from typing import Any, Dict, cast

from aea.mail.base_pb2 import DialogueMessage  # type: ignore
from aea.mail.base_pb2 import Message as ProtobufMessage  # type: ignore
from aea.protocols.base import Message  # type: ignore
from aea.protocols.base import Serializer  # type: ignore

from packages.zarathustra.protocols.matchmaker import matchmaker_pb2  # type: ignore
from packages.zarathustra.protocols.matchmaker.custom_types import (  # type: ignore
    ErrorCode,
    Preferences,
    UserInfo,
)
from packages.zarathustra.protocols.matchmaker.message import (  # type: ignore
    MatchmakerMessage,
)


class MatchmakerSerializer(Serializer):
    """Serialization for the 'matchmaker' protocol."""

    @staticmethod
    def encode(msg: Message) -> bytes:
        """
        Encode a 'Matchmaker' message into bytes.

        :param msg: the message object.
        :return: the bytes.
        """
        msg = cast(MatchmakerMessage, msg)
        message_pb = ProtobufMessage()
        dialogue_message_pb = DialogueMessage()
        matchmaker_msg = matchmaker_pb2.MatchmakerMessage()  # type: ignore

        dialogue_message_pb.message_id = msg.message_id
        dialogue_reference = msg.dialogue_reference
        dialogue_message_pb.dialogue_starter_reference = dialogue_reference[0]
        dialogue_message_pb.dialogue_responder_reference = dialogue_reference[1]
        dialogue_message_pb.target = msg.target

        performative_id = msg.performative
        if performative_id == MatchmakerMessage.Performative.MATCHMAKING_REQUEST:
            performative = matchmaker_pb2.MatchmakerMessage.Matchmaking_Request_Performative()  # type: ignore
            user_info = msg.user_info
            UserInfo.encode(performative.user_info, user_info)
            preferences = msg.preferences
            Preferences.encode(performative.preferences, preferences)
            matchmaker_msg.matchmaking_request.CopyFrom(performative)
        elif performative_id == MatchmakerMessage.Performative.MATCHMAKING_RESPONSE:
            performative = matchmaker_pb2.MatchmakerMessage.Matchmaking_Response_Performative()  # type: ignore
            peer_ids = msg.peer_ids
            performative.peer_ids.extend(peer_ids)
            matchmaker_msg.matchmaking_response.CopyFrom(performative)
        elif performative_id == MatchmakerMessage.Performative.RESULT:
            performative = matchmaker_pb2.MatchmakerMessage.Result_Performative()  # type: ignore
            success = msg.success
            performative.success = success
            block = msg.block
            performative.block = block
            matchmaker_msg.result.CopyFrom(performative)
        elif performative_id == MatchmakerMessage.Performative.ERROR:
            performative = matchmaker_pb2.MatchmakerMessage.Error_Performative()  # type: ignore
            error_code = msg.error_code
            ErrorCode.encode(performative.error_code, error_code)
            error_msg = msg.error_msg
            performative.error_msg = error_msg
            matchmaker_msg.error.CopyFrom(performative)
        else:
            raise ValueError("Performative not valid: {}".format(performative_id))

        dialogue_message_pb.content = matchmaker_msg.SerializeToString()

        message_pb.dialogue_message.CopyFrom(dialogue_message_pb)
        message_bytes = message_pb.SerializeToString()
        return message_bytes

    @staticmethod
    def decode(obj: bytes) -> Message:
        """
        Decode bytes into a 'Matchmaker' message.

        :param obj: the bytes object.
        :return: the 'Matchmaker' message.
        """
        message_pb = ProtobufMessage()
        matchmaker_pb = matchmaker_pb2.MatchmakerMessage()  # type: ignore
        message_pb.ParseFromString(obj)
        message_id = message_pb.dialogue_message.message_id
        dialogue_reference = (
            message_pb.dialogue_message.dialogue_starter_reference,
            message_pb.dialogue_message.dialogue_responder_reference,
        )
        target = message_pb.dialogue_message.target

        matchmaker_pb.ParseFromString(message_pb.dialogue_message.content)
        performative = matchmaker_pb.WhichOneof("performative")
        performative_id = MatchmakerMessage.Performative(str(performative))
        performative_content = dict()  # type: Dict[str, Any]
        if performative_id == MatchmakerMessage.Performative.MATCHMAKING_REQUEST:
            pb2_user_info = matchmaker_pb.matchmaking_request.user_info
            user_info = UserInfo.decode(pb2_user_info)
            performative_content["user_info"] = user_info
            pb2_preferences = matchmaker_pb.matchmaking_request.preferences
            preferences = Preferences.decode(pb2_preferences)
            performative_content["preferences"] = preferences
        elif performative_id == MatchmakerMessage.Performative.MATCHMAKING_RESPONSE:
            peer_ids = matchmaker_pb.matchmaking_response.peer_ids
            peer_ids_tuple = tuple(peer_ids)
            performative_content["peer_ids"] = peer_ids_tuple
        elif performative_id == MatchmakerMessage.Performative.RESULT:
            success = matchmaker_pb.result.success
            performative_content["success"] = success
            block = matchmaker_pb.result.block
            performative_content["block"] = block
        elif performative_id == MatchmakerMessage.Performative.ERROR:
            pb2_error_code = matchmaker_pb.error.error_code
            error_code = ErrorCode.decode(pb2_error_code)
            performative_content["error_code"] = error_code
            error_msg = matchmaker_pb.error.error_msg
            performative_content["error_msg"] = error_msg
        else:
            raise ValueError("Performative not valid: {}.".format(performative_id))

        return MatchmakerMessage(
            message_id=message_id,
            dialogue_reference=dialogue_reference,
            target=target,
            performative=performative,
            **performative_content
        )
