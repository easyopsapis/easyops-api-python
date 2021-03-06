# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: batch_list_relation_query_strategy_v2.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cmdb_sdk.model.cmdb import relation_query_strategy_v2_pb2 as cmdb__sdk_dot_model_dot_cmdb_dot_relation__query__strategy__v2__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='batch_list_relation_query_strategy_v2.proto',
  package='cmdb_object',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n+batch_list_relation_query_strategy_v2.proto\x12\x0b\x63mdb_object\x1a\x34\x63mdb_sdk/model/cmdb/relation_query_strategy_v2.proto\"`\n.BatchListRelationQueryStrategyV2RequestRequest\x12\x12\n\nobject_ids\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\"\xec\x01\n/BatchListRelationQueryStrategyV2RequestResponse\x12`\n\rstrategy_data\x18\x01 \x03(\x0b\x32I.cmdb_object.BatchListRelationQueryStrategyV2RequestResponse.StrategyData\x1aW\n\x0cStrategyData\x12\x11\n\tobject_id\x18\x01 \x01(\t\x12\x34\n\rstrategy_list\x18\x02 \x03(\x0b\x32\x1d.cmdb.RelationQueryStrategyV2\"\xb6\x01\n6BatchListRelationQueryStrategyV2RequestResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12J\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32<.cmdb_object.BatchListRelationQueryStrategyV2RequestResponseb\x06proto3')
  ,
  dependencies=[cmdb__sdk_dot_model_dot_cmdb_dot_relation__query__strategy__v2__pb2.DESCRIPTOR,])




_BATCHLISTRELATIONQUERYSTRATEGYV2REQUESTREQUEST = _descriptor.Descriptor(
  name='BatchListRelationQueryStrategyV2RequestRequest',
  full_name='cmdb_object.BatchListRelationQueryStrategyV2RequestRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_ids', full_name='cmdb_object.BatchListRelationQueryStrategyV2RequestRequest.object_ids', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='cmdb_object.BatchListRelationQueryStrategyV2RequestRequest.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='cmdb_object.BatchListRelationQueryStrategyV2RequestRequest.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=114,
  serialized_end=210,
)


_BATCHLISTRELATIONQUERYSTRATEGYV2REQUESTRESPONSE_STRATEGYDATA = _descriptor.Descriptor(
  name='StrategyData',
  full_name='cmdb_object.BatchListRelationQueryStrategyV2RequestResponse.StrategyData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_id', full_name='cmdb_object.BatchListRelationQueryStrategyV2RequestResponse.StrategyData.object_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strategy_list', full_name='cmdb_object.BatchListRelationQueryStrategyV2RequestResponse.StrategyData.strategy_list', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=362,
  serialized_end=449,
)

_BATCHLISTRELATIONQUERYSTRATEGYV2REQUESTRESPONSE = _descriptor.Descriptor(
  name='BatchListRelationQueryStrategyV2RequestResponse',
  full_name='cmdb_object.BatchListRelationQueryStrategyV2RequestResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='strategy_data', full_name='cmdb_object.BatchListRelationQueryStrategyV2RequestResponse.strategy_data', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_BATCHLISTRELATIONQUERYSTRATEGYV2REQUESTRESPONSE_STRATEGYDATA, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=213,
  serialized_end=449,
)


_BATCHLISTRELATIONQUERYSTRATEGYV2REQUESTRESPONSEWRAPPER = _descriptor.Descriptor(
  name='BatchListRelationQueryStrategyV2RequestResponseWrapper',
  full_name='cmdb_object.BatchListRelationQueryStrategyV2RequestResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='cmdb_object.BatchListRelationQueryStrategyV2RequestResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='cmdb_object.BatchListRelationQueryStrategyV2RequestResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='cmdb_object.BatchListRelationQueryStrategyV2RequestResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='cmdb_object.BatchListRelationQueryStrategyV2RequestResponseWrapper.data', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=452,
  serialized_end=634,
)

_BATCHLISTRELATIONQUERYSTRATEGYV2REQUESTRESPONSE_STRATEGYDATA.fields_by_name['strategy_list'].message_type = cmdb__sdk_dot_model_dot_cmdb_dot_relation__query__strategy__v2__pb2._RELATIONQUERYSTRATEGYV2
_BATCHLISTRELATIONQUERYSTRATEGYV2REQUESTRESPONSE_STRATEGYDATA.containing_type = _BATCHLISTRELATIONQUERYSTRATEGYV2REQUESTRESPONSE
_BATCHLISTRELATIONQUERYSTRATEGYV2REQUESTRESPONSE.fields_by_name['strategy_data'].message_type = _BATCHLISTRELATIONQUERYSTRATEGYV2REQUESTRESPONSE_STRATEGYDATA
_BATCHLISTRELATIONQUERYSTRATEGYV2REQUESTRESPONSEWRAPPER.fields_by_name['data'].message_type = _BATCHLISTRELATIONQUERYSTRATEGYV2REQUESTRESPONSE
DESCRIPTOR.message_types_by_name['BatchListRelationQueryStrategyV2RequestRequest'] = _BATCHLISTRELATIONQUERYSTRATEGYV2REQUESTREQUEST
DESCRIPTOR.message_types_by_name['BatchListRelationQueryStrategyV2RequestResponse'] = _BATCHLISTRELATIONQUERYSTRATEGYV2REQUESTRESPONSE
DESCRIPTOR.message_types_by_name['BatchListRelationQueryStrategyV2RequestResponseWrapper'] = _BATCHLISTRELATIONQUERYSTRATEGYV2REQUESTRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BatchListRelationQueryStrategyV2RequestRequest = _reflection.GeneratedProtocolMessageType('BatchListRelationQueryStrategyV2RequestRequest', (_message.Message,), {
  'DESCRIPTOR' : _BATCHLISTRELATIONQUERYSTRATEGYV2REQUESTREQUEST,
  '__module__' : 'batch_list_relation_query_strategy_v2_pb2'
  # @@protoc_insertion_point(class_scope:cmdb_object.BatchListRelationQueryStrategyV2RequestRequest)
  })
_sym_db.RegisterMessage(BatchListRelationQueryStrategyV2RequestRequest)

BatchListRelationQueryStrategyV2RequestResponse = _reflection.GeneratedProtocolMessageType('BatchListRelationQueryStrategyV2RequestResponse', (_message.Message,), {

  'StrategyData' : _reflection.GeneratedProtocolMessageType('StrategyData', (_message.Message,), {
    'DESCRIPTOR' : _BATCHLISTRELATIONQUERYSTRATEGYV2REQUESTRESPONSE_STRATEGYDATA,
    '__module__' : 'batch_list_relation_query_strategy_v2_pb2'
    # @@protoc_insertion_point(class_scope:cmdb_object.BatchListRelationQueryStrategyV2RequestResponse.StrategyData)
    })
  ,
  'DESCRIPTOR' : _BATCHLISTRELATIONQUERYSTRATEGYV2REQUESTRESPONSE,
  '__module__' : 'batch_list_relation_query_strategy_v2_pb2'
  # @@protoc_insertion_point(class_scope:cmdb_object.BatchListRelationQueryStrategyV2RequestResponse)
  })
_sym_db.RegisterMessage(BatchListRelationQueryStrategyV2RequestResponse)
_sym_db.RegisterMessage(BatchListRelationQueryStrategyV2RequestResponse.StrategyData)

BatchListRelationQueryStrategyV2RequestResponseWrapper = _reflection.GeneratedProtocolMessageType('BatchListRelationQueryStrategyV2RequestResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _BATCHLISTRELATIONQUERYSTRATEGYV2REQUESTRESPONSEWRAPPER,
  '__module__' : 'batch_list_relation_query_strategy_v2_pb2'
  # @@protoc_insertion_point(class_scope:cmdb_object.BatchListRelationQueryStrategyV2RequestResponseWrapper)
  })
_sym_db.RegisterMessage(BatchListRelationQueryStrategyV2RequestResponseWrapper)


# @@protoc_insertion_point(module_scope)
