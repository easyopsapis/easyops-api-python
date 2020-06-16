# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: filter_condition.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from artifact_sdk.model.resource_manage import filter_data_source_pb2 as artifact__sdk_dot_model_dot_resource__manage_dot_filter__data__source__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='filter_condition.proto',
  package='resource_manage',
  syntax='proto3',
  serialized_options=_b('ZIgo.easyops.local/contracts/protorepo-models/easyops/model/resource_manage'),
  serialized_pb=_b('\n\x16\x66ilter_condition.proto\x12\x0fresource_manage\x1a;artifact_sdk/model/resource_manage/filter_data_source.proto\"\x93\x01\n\x0f\x46ilterCondition\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x63ompare\x18\x02 \x01(\t\x12/\n\x04left\x18\x03 \x01(\x0b\x32!.resource_manage.FilterDataSource\x12\x30\n\x05right\x18\x04 \x01(\x0b\x32!.resource_manage.FilterDataSourceBKZIgo.easyops.local/contracts/protorepo-models/easyops/model/resource_manageb\x06proto3')
  ,
  dependencies=[artifact__sdk_dot_model_dot_resource__manage_dot_filter__data__source__pb2.DESCRIPTOR,])




_FILTERCONDITION = _descriptor.Descriptor(
  name='FilterCondition',
  full_name='resource_manage.FilterCondition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='resource_manage.FilterCondition.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='compare', full_name='resource_manage.FilterCondition.compare', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='left', full_name='resource_manage.FilterCondition.left', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right', full_name='resource_manage.FilterCondition.right', index=3,
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
  serialized_start=105,
  serialized_end=252,
)

_FILTERCONDITION.fields_by_name['left'].message_type = artifact__sdk_dot_model_dot_resource__manage_dot_filter__data__source__pb2._FILTERDATASOURCE
_FILTERCONDITION.fields_by_name['right'].message_type = artifact__sdk_dot_model_dot_resource__manage_dot_filter__data__source__pb2._FILTERDATASOURCE
DESCRIPTOR.message_types_by_name['FilterCondition'] = _FILTERCONDITION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FilterCondition = _reflection.GeneratedProtocolMessageType('FilterCondition', (_message.Message,), {
  'DESCRIPTOR' : _FILTERCONDITION,
  '__module__' : 'filter_condition_pb2'
  # @@protoc_insertion_point(class_scope:resource_manage.FilterCondition)
  })
_sym_db.RegisterMessage(FilterCondition)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
