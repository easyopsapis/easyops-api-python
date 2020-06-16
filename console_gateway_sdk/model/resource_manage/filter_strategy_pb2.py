# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: filter_strategy.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from console_gateway_sdk.model.console import cmdb_query_strategy_pb2 as console__gateway__sdk_dot_model_dot_console_dot_cmdb__query__strategy__pb2
from console_gateway_sdk.model.resource_manage import filter_condition_group_pb2 as console__gateway__sdk_dot_model_dot_resource__manage_dot_filter__condition__group__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='filter_strategy.proto',
  package='resource_manage',
  syntax='proto3',
  serialized_options=_b('ZIgo.easyops.local/contracts/protorepo-models/easyops/model/resource_manage'),
  serialized_pb=_b('\n\x15\x66ilter_strategy.proto\x12\x0fresource_manage\x1a;console_gateway_sdk/model/console/cmdb_query_strategy.proto\x1a\x46\x63onsole_gateway_sdk/model/resource_manage/filter_condition_group.proto\"\xb6\x03\n\x0e\x46ilterStrategy\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x14\n\x0cstrategyName\x18\x02 \x01(\t\x12\x18\n\x10strategyObjectId\x18\x03 \x01(\t\x12)\n\x05query\x18\x04 \x01(\x0b\x32\x1a.console.CmdbQueryStrategy\x12\x35\n\x06\x66ilter\x18\x05 \x03(\x0b\x32%.resource_manage.FilterConditionGroup\x12\x0f\n\x07\x63rontab\x18\x06 \x01(\t\x12\r\n\x05\x63time\x18\x07 \x01(\t\x12\r\n\x05mtime\x18\x08 \x01(\t\x12\x0f\n\x07\x63reator\x18\t \x01(\t\x12\x10\n\x08modifier\x18\n \x01(\t\x12\x14\n\x0cnextExecTime\x18\x0b \x01(\t\x12\x0e\n\x06\x65nable\x18\x0c \x01(\x08\x12\x19\n\x11updateAuthorizers\x18\r \x03(\t\x12\x17\n\x0freadAuthorizers\x18\x0e \x03(\t\x12\x19\n\x11\x64\x65leteAuthorizers\x18\x0f \x03(\t\x12\x13\n\x0bnotifyUsers\x18\x10 \x03(\t\x12\x15\n\rnotifyMethods\x18\x11 \x03(\t\x12\x0b\n\x03org\x18\x12 \x01(\x05\x42KZIgo.easyops.local/contracts/protorepo-models/easyops/model/resource_manageb\x06proto3')
  ,
  dependencies=[console__gateway__sdk_dot_model_dot_console_dot_cmdb__query__strategy__pb2.DESCRIPTOR,console__gateway__sdk_dot_model_dot_resource__manage_dot_filter__condition__group__pb2.DESCRIPTOR,])




_FILTERSTRATEGY = _descriptor.Descriptor(
  name='FilterStrategy',
  full_name='resource_manage.FilterStrategy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='resource_manage.FilterStrategy.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strategyName', full_name='resource_manage.FilterStrategy.strategyName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strategyObjectId', full_name='resource_manage.FilterStrategy.strategyObjectId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='query', full_name='resource_manage.FilterStrategy.query', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter', full_name='resource_manage.FilterStrategy.filter', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='crontab', full_name='resource_manage.FilterStrategy.crontab', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='resource_manage.FilterStrategy.ctime', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='resource_manage.FilterStrategy.mtime', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='resource_manage.FilterStrategy.creator', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='modifier', full_name='resource_manage.FilterStrategy.modifier', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nextExecTime', full_name='resource_manage.FilterStrategy.nextExecTime', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable', full_name='resource_manage.FilterStrategy.enable', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updateAuthorizers', full_name='resource_manage.FilterStrategy.updateAuthorizers', index=12,
      number=13, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readAuthorizers', full_name='resource_manage.FilterStrategy.readAuthorizers', index=13,
      number=14, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deleteAuthorizers', full_name='resource_manage.FilterStrategy.deleteAuthorizers', index=14,
      number=15, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='notifyUsers', full_name='resource_manage.FilterStrategy.notifyUsers', index=15,
      number=16, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='notifyMethods', full_name='resource_manage.FilterStrategy.notifyMethods', index=16,
      number=17, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org', full_name='resource_manage.FilterStrategy.org', index=17,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=176,
  serialized_end=614,
)

_FILTERSTRATEGY.fields_by_name['query'].message_type = console__gateway__sdk_dot_model_dot_console_dot_cmdb__query__strategy__pb2._CMDBQUERYSTRATEGY
_FILTERSTRATEGY.fields_by_name['filter'].message_type = console__gateway__sdk_dot_model_dot_resource__manage_dot_filter__condition__group__pb2._FILTERCONDITIONGROUP
DESCRIPTOR.message_types_by_name['FilterStrategy'] = _FILTERSTRATEGY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FilterStrategy = _reflection.GeneratedProtocolMessageType('FilterStrategy', (_message.Message,), {
  'DESCRIPTOR' : _FILTERSTRATEGY,
  '__module__' : 'filter_strategy_pb2'
  # @@protoc_insertion_point(class_scope:resource_manage.FilterStrategy)
  })
_sym_db.RegisterMessage(FilterStrategy)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
