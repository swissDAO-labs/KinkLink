# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tac.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\ttac.proto\x12\x16\x61\x65\x61.fetchai.tac.v1_0_0"\xf9\x1f\n\nTacMessage\x12N\n\tcancelled\x18\x05 \x01(\x0b\x32\x39.aea.fetchai.tac.v1_0_0.TacMessage.Cancelled_PerformativeH\x00\x12N\n\tgame_data\x18\x06 \x01(\x0b\x32\x39.aea.fetchai.tac.v1_0_0.TacMessage.Game_Data_PerformativeH\x00\x12L\n\x08register\x18\x07 \x01(\x0b\x32\x38.aea.fetchai.tac.v1_0_0.TacMessage.Register_PerformativeH\x00\x12N\n\ttac_error\x18\x08 \x01(\x0b\x32\x39.aea.fetchai.tac.v1_0_0.TacMessage.Tac_Error_PerformativeH\x00\x12R\n\x0btransaction\x18\t \x01(\x0b\x32;.aea.fetchai.tac.v1_0_0.TacMessage.Transaction_PerformativeH\x00\x12l\n\x18transaction_confirmation\x18\n \x01(\x0b\x32H.aea.fetchai.tac.v1_0_0.TacMessage.Transaction_Confirmation_PerformativeH\x00\x12P\n\nunregister\x18\x0b \x01(\x0b\x32:.aea.fetchai.tac.v1_0_0.TacMessage.Unregister_PerformativeH\x00\x1a\x89\x03\n\tErrorCode\x12N\n\nerror_code\x18\x01 \x01(\x0e\x32:.aea.fetchai.tac.v1_0_0.TacMessage.ErrorCode.ErrorCodeEnum"\xab\x02\n\rErrorCodeEnum\x12\x11\n\rGENERIC_ERROR\x10\x00\x12\x15\n\x11REQUEST_NOT_VALID\x10\x01\x12!\n\x1d\x41GENT_ADDR_ALREADY_REGISTERED\x10\x02\x12!\n\x1d\x41GENT_NAME_ALREADY_REGISTERED\x10\x03\x12\x18\n\x14\x41GENT_NOT_REGISTERED\x10\x04\x12\x19\n\x15TRANSACTION_NOT_VALID\x10\x05\x12\x1c\n\x18TRANSACTION_NOT_MATCHING\x10\x06\x12\x1f\n\x1b\x41GENT_NAME_NOT_IN_WHITELIST\x10\x07\x12\x1b\n\x17\x43OMPETITION_NOT_RUNNING\x10\x08\x12\x19\n\x15\x44IALOGUE_INCONSISTENT\x10\t\x1a+\n\x15Register_Performative\x12\x12\n\nagent_name\x18\x01 \x01(\t\x1a\x19\n\x17Unregister_Performative\x1a\xc8\x05\n\x18Transaction_Performative\x12\x16\n\x0etransaction_id\x18\x01 \x01(\t\x12\x11\n\tledger_id\x18\x02 \x01(\t\x12\x16\n\x0esender_address\x18\x03 \x01(\t\x12\x1c\n\x14\x63ounterparty_address\x18\x04 \x01(\t\x12r\n\x15\x61mount_by_currency_id\x18\x05 \x03(\x0b\x32S.aea.fetchai.tac.v1_0_0.TacMessage.Transaction_Performative.AmountByCurrencyIdEntry\x12l\n\x12\x66\x65\x65_by_currency_id\x18\x06 \x03(\x0b\x32P.aea.fetchai.tac.v1_0_0.TacMessage.Transaction_Performative.FeeByCurrencyIdEntry\x12r\n\x15quantities_by_good_id\x18\x07 \x03(\x0b\x32S.aea.fetchai.tac.v1_0_0.TacMessage.Transaction_Performative.QuantitiesByGoodIdEntry\x12\r\n\x05nonce\x18\x08 \x01(\t\x12\x18\n\x10sender_signature\x18\t \x01(\t\x12\x1e\n\x16\x63ounterparty_signature\x18\n \x01(\t\x1a\x39\n\x17\x41mountByCurrencyIdEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x36\n\x14\x46\x65\x65\x42yCurrencyIdEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x39\n\x17QuantitiesByGoodIdEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x18\n\x16\x43\x61ncelled_Performative\x1a\xa3\x0c\n\x16Game_Data_Performative\x12p\n\x15\x61mount_by_currency_id\x18\x01 \x03(\x0b\x32Q.aea.fetchai.tac.v1_0_0.TacMessage.Game_Data_Performative.AmountByCurrencyIdEntry\x12\x81\x01\n\x1e\x65xchange_params_by_currency_id\x18\x02 \x03(\x0b\x32Y.aea.fetchai.tac.v1_0_0.TacMessage.Game_Data_Performative.ExchangeParamsByCurrencyIdEntry\x12p\n\x15quantities_by_good_id\x18\x03 \x03(\x0b\x32Q.aea.fetchai.tac.v1_0_0.TacMessage.Game_Data_Performative.QuantitiesByGoodIdEntry\x12w\n\x19utility_params_by_good_id\x18\x04 \x03(\x0b\x32T.aea.fetchai.tac.v1_0_0.TacMessage.Game_Data_Performative.UtilityParamsByGoodIdEntry\x12j\n\x12\x66\x65\x65_by_currency_id\x18\x05 \x03(\x0b\x32N.aea.fetchai.tac.v1_0_0.TacMessage.Game_Data_Performative.FeeByCurrencyIdEntry\x12j\n\x12\x61gent_addr_to_name\x18\x06 \x03(\x0b\x32N.aea.fetchai.tac.v1_0_0.TacMessage.Game_Data_Performative.AgentAddrToNameEntry\x12l\n\x13\x63urrency_id_to_name\x18\x07 \x03(\x0b\x32O.aea.fetchai.tac.v1_0_0.TacMessage.Game_Data_Performative.CurrencyIdToNameEntry\x12\x64\n\x0fgood_id_to_name\x18\x08 \x03(\x0b\x32K.aea.fetchai.tac.v1_0_0.TacMessage.Game_Data_Performative.GoodIdToNameEntry\x12\x12\n\nversion_id\x18\t \x01(\t\x12Q\n\x04info\x18\n \x03(\x0b\x32\x43.aea.fetchai.tac.v1_0_0.TacMessage.Game_Data_Performative.InfoEntry\x12\x13\n\x0binfo_is_set\x18\x0b \x01(\x08\x1a\x39\n\x17\x41mountByCurrencyIdEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x41\n\x1f\x45xchangeParamsByCurrencyIdEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\x1a\x39\n\x17QuantitiesByGoodIdEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a<\n\x1aUtilityParamsByGoodIdEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\x1a\x36\n\x14\x46\x65\x65\x42yCurrencyIdEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x36\n\x14\x41gentAddrToNameEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x37\n\x15\x43urrencyIdToNameEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x33\n\x11GoodIdToNameEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a+\n\tInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\xb7\x03\n%Transaction_Confirmation_Performative\x12\x16\n\x0etransaction_id\x18\x01 \x01(\t\x12\x7f\n\x15\x61mount_by_currency_id\x18\x02 \x03(\x0b\x32`.aea.fetchai.tac.v1_0_0.TacMessage.Transaction_Confirmation_Performative.AmountByCurrencyIdEntry\x12\x7f\n\x15quantities_by_good_id\x18\x03 \x03(\x0b\x32`.aea.fetchai.tac.v1_0_0.TacMessage.Transaction_Confirmation_Performative.QuantitiesByGoodIdEntry\x1a\x39\n\x17\x41mountByCurrencyIdEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\x39\n\x17QuantitiesByGoodIdEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x1a\xef\x01\n\x16Tac_Error_Performative\x12@\n\nerror_code\x18\x01 \x01(\x0b\x32,.aea.fetchai.tac.v1_0_0.TacMessage.ErrorCode\x12Q\n\x04info\x18\x02 \x03(\x0b\x32\x43.aea.fetchai.tac.v1_0_0.TacMessage.Tac_Error_Performative.InfoEntry\x12\x13\n\x0binfo_is_set\x18\x03 \x01(\x08\x1a+\n\tInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x0e\n\x0cperformativeb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "tac_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _TACMESSAGE_TRANSACTION_PERFORMATIVE_AMOUNTBYCURRENCYIDENTRY._options = None
    _TACMESSAGE_TRANSACTION_PERFORMATIVE_AMOUNTBYCURRENCYIDENTRY._serialized_options = (
        b"8\001"
    )
    _TACMESSAGE_TRANSACTION_PERFORMATIVE_FEEBYCURRENCYIDENTRY._options = None
    _TACMESSAGE_TRANSACTION_PERFORMATIVE_FEEBYCURRENCYIDENTRY._serialized_options = (
        b"8\001"
    )
    _TACMESSAGE_TRANSACTION_PERFORMATIVE_QUANTITIESBYGOODIDENTRY._options = None
    _TACMESSAGE_TRANSACTION_PERFORMATIVE_QUANTITIESBYGOODIDENTRY._serialized_options = (
        b"8\001"
    )
    _TACMESSAGE_GAME_DATA_PERFORMATIVE_AMOUNTBYCURRENCYIDENTRY._options = None
    _TACMESSAGE_GAME_DATA_PERFORMATIVE_AMOUNTBYCURRENCYIDENTRY._serialized_options = (
        b"8\001"
    )
    _TACMESSAGE_GAME_DATA_PERFORMATIVE_EXCHANGEPARAMSBYCURRENCYIDENTRY._options = None
    _TACMESSAGE_GAME_DATA_PERFORMATIVE_EXCHANGEPARAMSBYCURRENCYIDENTRY._serialized_options = (
        b"8\001"
    )
    _TACMESSAGE_GAME_DATA_PERFORMATIVE_QUANTITIESBYGOODIDENTRY._options = None
    _TACMESSAGE_GAME_DATA_PERFORMATIVE_QUANTITIESBYGOODIDENTRY._serialized_options = (
        b"8\001"
    )
    _TACMESSAGE_GAME_DATA_PERFORMATIVE_UTILITYPARAMSBYGOODIDENTRY._options = None
    _TACMESSAGE_GAME_DATA_PERFORMATIVE_UTILITYPARAMSBYGOODIDENTRY._serialized_options = (
        b"8\001"
    )
    _TACMESSAGE_GAME_DATA_PERFORMATIVE_FEEBYCURRENCYIDENTRY._options = None
    _TACMESSAGE_GAME_DATA_PERFORMATIVE_FEEBYCURRENCYIDENTRY._serialized_options = (
        b"8\001"
    )
    _TACMESSAGE_GAME_DATA_PERFORMATIVE_AGENTADDRTONAMEENTRY._options = None
    _TACMESSAGE_GAME_DATA_PERFORMATIVE_AGENTADDRTONAMEENTRY._serialized_options = (
        b"8\001"
    )
    _TACMESSAGE_GAME_DATA_PERFORMATIVE_CURRENCYIDTONAMEENTRY._options = None
    _TACMESSAGE_GAME_DATA_PERFORMATIVE_CURRENCYIDTONAMEENTRY._serialized_options = (
        b"8\001"
    )
    _TACMESSAGE_GAME_DATA_PERFORMATIVE_GOODIDTONAMEENTRY._options = None
    _TACMESSAGE_GAME_DATA_PERFORMATIVE_GOODIDTONAMEENTRY._serialized_options = b"8\001"
    _TACMESSAGE_GAME_DATA_PERFORMATIVE_INFOENTRY._options = None
    _TACMESSAGE_GAME_DATA_PERFORMATIVE_INFOENTRY._serialized_options = b"8\001"
    _TACMESSAGE_TRANSACTION_CONFIRMATION_PERFORMATIVE_AMOUNTBYCURRENCYIDENTRY._options = (
        None
    )
    _TACMESSAGE_TRANSACTION_CONFIRMATION_PERFORMATIVE_AMOUNTBYCURRENCYIDENTRY._serialized_options = (
        b"8\001"
    )
    _TACMESSAGE_TRANSACTION_CONFIRMATION_PERFORMATIVE_QUANTITIESBYGOODIDENTRY._options = (
        None
    )
    _TACMESSAGE_TRANSACTION_CONFIRMATION_PERFORMATIVE_QUANTITIESBYGOODIDENTRY._serialized_options = (
        b"8\001"
    )
    _TACMESSAGE_TAC_ERROR_PERFORMATIVE_INFOENTRY._options = None
    _TACMESSAGE_TAC_ERROR_PERFORMATIVE_INFOENTRY._serialized_options = b"8\001"
    _globals["_TACMESSAGE"]._serialized_start = 38
    _globals["_TACMESSAGE"]._serialized_end = 4127
    _globals["_TACMESSAGE_ERRORCODE"]._serialized_start = 647
    _globals["_TACMESSAGE_ERRORCODE"]._serialized_end = 1040
    _globals["_TACMESSAGE_ERRORCODE_ERRORCODEENUM"]._serialized_start = 741
    _globals["_TACMESSAGE_ERRORCODE_ERRORCODEENUM"]._serialized_end = 1040
    _globals["_TACMESSAGE_REGISTER_PERFORMATIVE"]._serialized_start = 1042
    _globals["_TACMESSAGE_REGISTER_PERFORMATIVE"]._serialized_end = 1085
    _globals["_TACMESSAGE_UNREGISTER_PERFORMATIVE"]._serialized_start = 1087
    _globals["_TACMESSAGE_UNREGISTER_PERFORMATIVE"]._serialized_end = 1112
    _globals["_TACMESSAGE_TRANSACTION_PERFORMATIVE"]._serialized_start = 1115
    _globals["_TACMESSAGE_TRANSACTION_PERFORMATIVE"]._serialized_end = 1827
    _globals[
        "_TACMESSAGE_TRANSACTION_PERFORMATIVE_AMOUNTBYCURRENCYIDENTRY"
    ]._serialized_start = 1655
    _globals[
        "_TACMESSAGE_TRANSACTION_PERFORMATIVE_AMOUNTBYCURRENCYIDENTRY"
    ]._serialized_end = 1712
    _globals[
        "_TACMESSAGE_TRANSACTION_PERFORMATIVE_FEEBYCURRENCYIDENTRY"
    ]._serialized_start = 1714
    _globals[
        "_TACMESSAGE_TRANSACTION_PERFORMATIVE_FEEBYCURRENCYIDENTRY"
    ]._serialized_end = 1768
    _globals[
        "_TACMESSAGE_TRANSACTION_PERFORMATIVE_QUANTITIESBYGOODIDENTRY"
    ]._serialized_start = 1770
    _globals[
        "_TACMESSAGE_TRANSACTION_PERFORMATIVE_QUANTITIESBYGOODIDENTRY"
    ]._serialized_end = 1827
    _globals["_TACMESSAGE_CANCELLED_PERFORMATIVE"]._serialized_start = 1829
    _globals["_TACMESSAGE_CANCELLED_PERFORMATIVE"]._serialized_end = 1853
    _globals["_TACMESSAGE_GAME_DATA_PERFORMATIVE"]._serialized_start = 1856
    _globals["_TACMESSAGE_GAME_DATA_PERFORMATIVE"]._serialized_end = 3427
    _globals[
        "_TACMESSAGE_GAME_DATA_PERFORMATIVE_AMOUNTBYCURRENCYIDENTRY"
    ]._serialized_start = 1655
    _globals[
        "_TACMESSAGE_GAME_DATA_PERFORMATIVE_AMOUNTBYCURRENCYIDENTRY"
    ]._serialized_end = 1712
    _globals[
        "_TACMESSAGE_GAME_DATA_PERFORMATIVE_EXCHANGEPARAMSBYCURRENCYIDENTRY"
    ]._serialized_start = 2974
    _globals[
        "_TACMESSAGE_GAME_DATA_PERFORMATIVE_EXCHANGEPARAMSBYCURRENCYIDENTRY"
    ]._serialized_end = 3039
    _globals[
        "_TACMESSAGE_GAME_DATA_PERFORMATIVE_QUANTITIESBYGOODIDENTRY"
    ]._serialized_start = 1770
    _globals[
        "_TACMESSAGE_GAME_DATA_PERFORMATIVE_QUANTITIESBYGOODIDENTRY"
    ]._serialized_end = 1827
    _globals[
        "_TACMESSAGE_GAME_DATA_PERFORMATIVE_UTILITYPARAMSBYGOODIDENTRY"
    ]._serialized_start = 3100
    _globals[
        "_TACMESSAGE_GAME_DATA_PERFORMATIVE_UTILITYPARAMSBYGOODIDENTRY"
    ]._serialized_end = 3160
    _globals[
        "_TACMESSAGE_GAME_DATA_PERFORMATIVE_FEEBYCURRENCYIDENTRY"
    ]._serialized_start = 1714
    _globals[
        "_TACMESSAGE_GAME_DATA_PERFORMATIVE_FEEBYCURRENCYIDENTRY"
    ]._serialized_end = 1768
    _globals[
        "_TACMESSAGE_GAME_DATA_PERFORMATIVE_AGENTADDRTONAMEENTRY"
    ]._serialized_start = 3218
    _globals[
        "_TACMESSAGE_GAME_DATA_PERFORMATIVE_AGENTADDRTONAMEENTRY"
    ]._serialized_end = 3272
    _globals[
        "_TACMESSAGE_GAME_DATA_PERFORMATIVE_CURRENCYIDTONAMEENTRY"
    ]._serialized_start = 3274
    _globals[
        "_TACMESSAGE_GAME_DATA_PERFORMATIVE_CURRENCYIDTONAMEENTRY"
    ]._serialized_end = 3329
    _globals[
        "_TACMESSAGE_GAME_DATA_PERFORMATIVE_GOODIDTONAMEENTRY"
    ]._serialized_start = 3331
    _globals[
        "_TACMESSAGE_GAME_DATA_PERFORMATIVE_GOODIDTONAMEENTRY"
    ]._serialized_end = 3382
    _globals["_TACMESSAGE_GAME_DATA_PERFORMATIVE_INFOENTRY"]._serialized_start = 3384
    _globals["_TACMESSAGE_GAME_DATA_PERFORMATIVE_INFOENTRY"]._serialized_end = 3427
    _globals[
        "_TACMESSAGE_TRANSACTION_CONFIRMATION_PERFORMATIVE"
    ]._serialized_start = 3430
    _globals["_TACMESSAGE_TRANSACTION_CONFIRMATION_PERFORMATIVE"]._serialized_end = 3869
    _globals[
        "_TACMESSAGE_TRANSACTION_CONFIRMATION_PERFORMATIVE_AMOUNTBYCURRENCYIDENTRY"
    ]._serialized_start = 1655
    _globals[
        "_TACMESSAGE_TRANSACTION_CONFIRMATION_PERFORMATIVE_AMOUNTBYCURRENCYIDENTRY"
    ]._serialized_end = 1712
    _globals[
        "_TACMESSAGE_TRANSACTION_CONFIRMATION_PERFORMATIVE_QUANTITIESBYGOODIDENTRY"
    ]._serialized_start = 1770
    _globals[
        "_TACMESSAGE_TRANSACTION_CONFIRMATION_PERFORMATIVE_QUANTITIESBYGOODIDENTRY"
    ]._serialized_end = 1827
    _globals["_TACMESSAGE_TAC_ERROR_PERFORMATIVE"]._serialized_start = 3872
    _globals["_TACMESSAGE_TAC_ERROR_PERFORMATIVE"]._serialized_end = 4111
    _globals["_TACMESSAGE_TAC_ERROR_PERFORMATIVE_INFOENTRY"]._serialized_start = 3384
    _globals["_TACMESSAGE_TAC_ERROR_PERFORMATIVE_INFOENTRY"]._serialized_end = 3427
# @@protoc_insertion_point(module_scope)