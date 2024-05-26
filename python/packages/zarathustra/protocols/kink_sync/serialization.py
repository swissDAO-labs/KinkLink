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

"""Serialization module for kink_sync protocol."""

# pylint: disable=too-many-statements,too-many-locals,no-member,too-few-public-methods,redefined-builtin
from typing import Any, Dict, cast

from aea.mail.base_pb2 import DialogueMessage  # type: ignore
from aea.mail.base_pb2 import Message as ProtobufMessage  # type: ignore
from aea.protocols.base import Message  # type: ignore
from aea.protocols.base import Serializer  # type: ignore

from packages.zarathustra.protocols.kink_sync import kink_sync_pb2  # type: ignore
from packages.zarathustra.protocols.kink_sync.custom_types import (  # type: ignore
    ErrorCode,
)
from packages.zarathustra.protocols.kink_sync.message import (  # type: ignore
    KinkSyncMessage,
)


class KinkSyncSerializer(Serializer):
    """Serialization for the 'kink_sync' protocol."""

    @staticmethod
    def encode(msg: Message) -> bytes:
        """
        Encode a 'KinkSync' message into bytes.

        :param msg: the message object.
        :return: the bytes.
        """
        msg = cast(KinkSyncMessage, msg)
        message_pb = ProtobufMessage()
        dialogue_message_pb = DialogueMessage()
        kink_sync_msg = kink_sync_pb2.KinkSyncMessage()  # type: ignore

        dialogue_message_pb.message_id = msg.message_id
        dialogue_reference = msg.dialogue_reference
        dialogue_message_pb.dialogue_starter_reference = dialogue_reference[0]
        dialogue_message_pb.dialogue_responder_reference = dialogue_reference[1]
        dialogue_message_pb.target = msg.target

        performative_id = msg.performative
        if performative_id == KinkSyncMessage.Performative.INITIATE_CONVERSATION:
            performative = kink_sync_pb2.KinkSyncMessage.Initiate_Conversation_Performative()  # type: ignore
            message = msg.message
            performative.message = message
            kink_sync_msg.initiate_conversation.CopyFrom(performative)
        elif performative_id == KinkSyncMessage.Performative.ENGAGE:
            performative = kink_sync_pb2.KinkSyncMessage.Engage_Performative()  # type: ignore
            message = msg.message
            performative.message = message
            kink_sync_msg.engage.CopyFrom(performative)
        elif performative_id == KinkSyncMessage.Performative.END_CONVERSATION:
            performative = kink_sync_pb2.KinkSyncMessage.End_Conversation_Performative()  # type: ignore
            score = msg.score
            performative.score = score
            kink_sync_msg.end_conversation.CopyFrom(performative)
        elif performative_id == KinkSyncMessage.Performative.ERROR:
            performative = kink_sync_pb2.KinkSyncMessage.Error_Performative()  # type: ignore
            error_code = msg.error_code
            ErrorCode.encode(performative.error_code, error_code)
            error_msg = msg.error_msg
            performative.error_msg = error_msg
            kink_sync_msg.error.CopyFrom(performative)
        else:
            raise ValueError("Performative not valid: {}".format(performative_id))

        dialogue_message_pb.content = kink_sync_msg.SerializeToString()

        message_pb.dialogue_message.CopyFrom(dialogue_message_pb)
        message_bytes = message_pb.SerializeToString()
        return message_bytes

    @staticmethod
    def decode(obj: bytes) -> Message:
        """
        Decode bytes into a 'KinkSync' message.

        :param obj: the bytes object.
        :return: the 'KinkSync' message.
        """
        message_pb = ProtobufMessage()
        kink_sync_pb = kink_sync_pb2.KinkSyncMessage()  # type: ignore
        message_pb.ParseFromString(obj)
        message_id = message_pb.dialogue_message.message_id
        dialogue_reference = (
            message_pb.dialogue_message.dialogue_starter_reference,
            message_pb.dialogue_message.dialogue_responder_reference,
        )
        target = message_pb.dialogue_message.target

        kink_sync_pb.ParseFromString(message_pb.dialogue_message.content)
        performative = kink_sync_pb.WhichOneof("performative")
        performative_id = KinkSyncMessage.Performative(str(performative))
        performative_content = dict()  # type: Dict[str, Any]
        if performative_id == KinkSyncMessage.Performative.INITIATE_CONVERSATION:
            message = kink_sync_pb.initiate_conversation.message
            performative_content["message"] = message
        elif performative_id == KinkSyncMessage.Performative.ENGAGE:
            message = kink_sync_pb.engage.message
            performative_content["message"] = message
        elif performative_id == KinkSyncMessage.Performative.END_CONVERSATION:
            score = kink_sync_pb.end_conversation.score
            performative_content["score"] = score
        elif performative_id == KinkSyncMessage.Performative.ERROR:
            pb2_error_code = kink_sync_pb.error.error_code
            error_code = ErrorCode.decode(pb2_error_code)
            performative_content["error_code"] = error_code
            error_msg = kink_sync_pb.error.error_msg
            performative_content["error_msg"] = error_msg
        else:
            raise ValueError("Performative not valid: {}.".format(performative_id))

        return KinkSyncMessage(
            message_id=message_id,
            dialogue_reference=dialogue_reference,
            target=target,
            performative=performative,
            **performative_content
        )
