# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: create_strategy.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from resource_manage_sdk.model.console import cmdb_query_strategy_pb2 as resource__manage__sdk_dot_model_dot_console_dot_cmdb__query__strategy__pb2
from resource_manage_sdk.model.resource_manage import filter_condition_group_pb2 as resource__manage__sdk_dot_model_dot_resource__manage_dot_filter__condition__group__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='create_strategy.proto',
  package='datafilter',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x15\x63reate_strategy.proto\x12\ndatafilter\x1a;resource_manage_sdk/model/console/cmdb_query_strategy.proto\x1a\x46resource_manage_sdk/model/resource_manage/filter_condition_group.proto\",\n\x16\x43reateStrategyResponse\x12\x12\n\ninstanceId\x18\x01 \x01(\t\"\x83\x01\n\x1d\x43reateStrategyResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x30\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\".datafilter.CreateStrategyResponseb\x06proto3')
  ,
  dependencies=[resource__manage__sdk_dot_model_dot_console_dot_cmdb__query__strategy__pb2.DESCRIPTOR,resource__manage__sdk_dot_model_dot_resource__manage_dot_filter__condition__group__pb2.DESCRIPTOR,])




_CREATESTRATEGYRESPONSE = _descriptor.Descriptor(
  name='CreateStrategyResponse',
  full_name='datafilter.CreateStrategyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='datafilter.CreateStrategyResponse.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=170,
  serialized_end=214,
)


_CREATESTRATEGYRESPONSEWRAPPER = _descriptor.Descriptor(
  name='CreateStrategyResponseWrapper',
  full_name='datafilter.CreateStrategyResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='datafilter.CreateStrategyResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='datafilter.CreateStrategyResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='datafilter.CreateStrategyResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='datafilter.CreateStrategyResponseWrapper.data', index=3,
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
  serialized_start=217,
  serialized_end=348,
)

_CREATESTRATEGYRESPONSEWRAPPER.fields_by_name['data'].message_type = _CREATESTRATEGYRESPONSE
DESCRIPTOR.message_types_by_name['CreateStrategyResponse'] = _CREATESTRATEGYRESPONSE
DESCRIPTOR.message_types_by_name['CreateStrategyResponseWrapper'] = _CREATESTRATEGYRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateStrategyResponse = _reflection.GeneratedProtocolMessageType('CreateStrategyResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATESTRATEGYRESPONSE,
  '__module__' : 'create_strategy_pb2'
  # @@protoc_insertion_point(class_scope:datafilter.CreateStrategyResponse)
  })
_sym_db.RegisterMessage(CreateStrategyResponse)

CreateStrategyResponseWrapper = _reflection.GeneratedProtocolMessageType('CreateStrategyResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _CREATESTRATEGYRESPONSEWRAPPER,
  '__module__' : 'create_strategy_pb2'
  # @@protoc_insertion_point(class_scope:datafilter.CreateStrategyResponseWrapper)
  })
_sym_db.RegisterMessage(CreateStrategyResponseWrapper)


# @@protoc_insertion_point(module_scope)