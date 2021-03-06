# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: filter_strategy_instance_data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from alert_service_sdk.model.resource_manage import filter_condition_group_pb2 as alert__service__sdk_dot_model_dot_resource__manage_dot_filter__condition__group__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='filter_strategy_instance_data.proto',
  package='resource_manage',
  syntax='proto3',
  serialized_options=_b('ZIgo.easyops.local/contracts/protorepo-models/easyops/model/resource_manage'),
  serialized_pb=_b('\n#filter_strategy_instance_data.proto\x12\x0fresource_manage\x1a\x44\x61lert_service_sdk/model/resource_manage/filter_condition_group.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xa2\x01\n\x1a\x46ilterStrategyInstanceData\x12\n\n\x02id\x18\x01 \x01(\t\x12\x1a\n\x12strategyInstanceId\x18\x02 \x01(\t\x12%\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x35\n\x06\x66ilter\x18\x04 \x03(\x0b\x32%.resource_manage.FilterConditionGroupBKZIgo.easyops.local/contracts/protorepo-models/easyops/model/resource_manageb\x06proto3')
  ,
  dependencies=[alert__service__sdk_dot_model_dot_resource__manage_dot_filter__condition__group__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_FILTERSTRATEGYINSTANCEDATA = _descriptor.Descriptor(
  name='FilterStrategyInstanceData',
  full_name='resource_manage.FilterStrategyInstanceData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='resource_manage.FilterStrategyInstanceData.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strategyInstanceId', full_name='resource_manage.FilterStrategyInstanceData.strategyInstanceId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='resource_manage.FilterStrategyInstanceData.data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter', full_name='resource_manage.FilterStrategyInstanceData.filter', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=157,
  serialized_end=319,
)

_FILTERSTRATEGYINSTANCEDATA.fields_by_name['data'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_FILTERSTRATEGYINSTANCEDATA.fields_by_name['filter'].message_type = alert__service__sdk_dot_model_dot_resource__manage_dot_filter__condition__group__pb2._FILTERCONDITIONGROUP
DESCRIPTOR.message_types_by_name['FilterStrategyInstanceData'] = _FILTERSTRATEGYINSTANCEDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FilterStrategyInstanceData = _reflection.GeneratedProtocolMessageType('FilterStrategyInstanceData', (_message.Message,), {
  'DESCRIPTOR' : _FILTERSTRATEGYINSTANCEDATA,
  '__module__' : 'filter_strategy_instance_data_pb2'
  # @@protoc_insertion_point(class_scope:resource_manage.FilterStrategyInstanceData)
  })
_sym_db.RegisterMessage(FilterStrategyInstanceData)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
