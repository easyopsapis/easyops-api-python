# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: filter_condition_group.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from staff_manage_sdk.model.resource_manage import filter_condition_pb2 as staff__manage__sdk_dot_model_dot_resource__manage_dot_filter__condition__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='filter_condition_group.proto',
  package='resource_manage',
  syntax='proto3',
  serialized_options=_b('ZIgo.easyops.local/contracts/protorepo-models/easyops/model/resource_manage'),
  serialized_pb=_b('\n\x1c\x66ilter_condition_group.proto\x12\x0fresource_manage\x1a=staff_manage_sdk/model/resource_manage/filter_condition.proto\"]\n\x14\x46ilterConditionGroup\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x37\n\rconditionList\x18\x02 \x03(\x0b\x32 .resource_manage.FilterConditionBKZIgo.easyops.local/contracts/protorepo-models/easyops/model/resource_manageb\x06proto3')
  ,
  dependencies=[staff__manage__sdk_dot_model_dot_resource__manage_dot_filter__condition__pb2.DESCRIPTOR,])




_FILTERCONDITIONGROUP = _descriptor.Descriptor(
  name='FilterConditionGroup',
  full_name='resource_manage.FilterConditionGroup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='resource_manage.FilterConditionGroup.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conditionList', full_name='resource_manage.FilterConditionGroup.conditionList', index=1,
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
  serialized_start=112,
  serialized_end=205,
)

_FILTERCONDITIONGROUP.fields_by_name['conditionList'].message_type = staff__manage__sdk_dot_model_dot_resource__manage_dot_filter__condition__pb2._FILTERCONDITION
DESCRIPTOR.message_types_by_name['FilterConditionGroup'] = _FILTERCONDITIONGROUP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FilterConditionGroup = _reflection.GeneratedProtocolMessageType('FilterConditionGroup', (_message.Message,), {
  'DESCRIPTOR' : _FILTERCONDITIONGROUP,
  '__module__' : 'filter_condition_group_pb2'
  # @@protoc_insertion_point(class_scope:resource_manage.FilterConditionGroup)
  })
_sym_db.RegisterMessage(FilterConditionGroup)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
