# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kink_sync.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0fkink_sync.proto\x12 aea.zarathustra.kink_sync.v0_1_0"\xf4\x06\n\x0fKinkSyncMessage\x12k\n\x10\x65nd_conversation\x18\x05 \x01(\x0b\x32O.aea.zarathustra.kink_sync.v0_1_0.KinkSyncMessage.End_Conversation_PerformativeH\x00\x12W\n\x06\x65ngage\x18\x06 \x01(\x0b\x32\x45.aea.zarathustra.kink_sync.v0_1_0.KinkSyncMessage.Engage_PerformativeH\x00\x12U\n\x05\x65rror\x18\x07 \x01(\x0b\x32\x44.aea.zarathustra.kink_sync.v0_1_0.KinkSyncMessage.Error_PerformativeH\x00\x12u\n\x15initiate_conversation\x18\x08 \x01(\x0b\x32T.aea.zarathustra.kink_sync.v0_1_0.KinkSyncMessage.Initiate_Conversation_PerformativeH\x00\x1a\xb3\x01\n\tErrorCode\x12]\n\nerror_code\x18\x01 \x01(\x0e\x32I.aea.zarathustra.kink_sync.v0_1_0.KinkSyncMessage.ErrorCode.ErrorCodeEnum"G\n\rErrorCodeEnum\x12\x14\n\x10\x43ONNECTION_ERROR\x10\x00\x12\x13\n\x0fINVALID_MESSAGE\x10\x01\x12\x0b\n\x07TIMEOUT\x10\x02\x1a\x35\n"Initiate_Conversation_Performative\x12\x0f\n\x07message\x18\x01 \x01(\t\x1a&\n\x13\x45ngage_Performative\x12\x0f\n\x07message\x18\x01 \x01(\t\x1a.\n\x1d\x45nd_Conversation_Performative\x12\r\n\x05score\x18\x01 \x01(\x05\x1ax\n\x12\x45rror_Performative\x12O\n\nerror_code\x18\x01 \x01(\x0b\x32;.aea.zarathustra.kink_sync.v0_1_0.KinkSyncMessage.ErrorCode\x12\x11\n\terror_msg\x18\x02 \x01(\tB\x0e\n\x0cperformativeb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "kink_sync_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals["_KINKSYNCMESSAGE"]._serialized_start = 54
    _globals["_KINKSYNCMESSAGE"]._serialized_end = 938
    _globals["_KINKSYNCMESSAGE_ERRORCODE"]._serialized_start = 478
    _globals["_KINKSYNCMESSAGE_ERRORCODE"]._serialized_end = 657
    _globals["_KINKSYNCMESSAGE_ERRORCODE_ERRORCODEENUM"]._serialized_start = 586
    _globals["_KINKSYNCMESSAGE_ERRORCODE_ERRORCODEENUM"]._serialized_end = 657
    _globals[
        "_KINKSYNCMESSAGE_INITIATE_CONVERSATION_PERFORMATIVE"
    ]._serialized_start = 659
    _globals["_KINKSYNCMESSAGE_INITIATE_CONVERSATION_PERFORMATIVE"]._serialized_end = (
        712
    )
    _globals["_KINKSYNCMESSAGE_ENGAGE_PERFORMATIVE"]._serialized_start = 714
    _globals["_KINKSYNCMESSAGE_ENGAGE_PERFORMATIVE"]._serialized_end = 752
    _globals["_KINKSYNCMESSAGE_END_CONVERSATION_PERFORMATIVE"]._serialized_start = 754
    _globals["_KINKSYNCMESSAGE_END_CONVERSATION_PERFORMATIVE"]._serialized_end = 800
    _globals["_KINKSYNCMESSAGE_ERROR_PERFORMATIVE"]._serialized_start = 802
    _globals["_KINKSYNCMESSAGE_ERROR_PERFORMATIVE"]._serialized_end = 922
# @@protoc_insertion_point(module_scope)