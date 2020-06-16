# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: metric_group.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flow_sdk.model.inspection import dim_pb2 as flow__sdk_dot_model_dot_inspection_dot_dim__pb2
from flow_sdk.model.inspection import val_pb2 as flow__sdk_dot_model_dot_inspection_dot_val__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='metric_group.proto',
  package='inspection',
  syntax='proto3',
  serialized_options=_b('ZDgo.easyops.local/contracts/protorepo-models/easyops/model/inspection'),
  serialized_pb=_b('\n\x12metric_group.proto\x12\ninspection\x1a#flow_sdk/model/inspection/dim.proto\x1a#flow_sdk/model/inspection/val.proto\"\xa3\x01\n\x15InspectionMetricGroup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x03 \x01(\t\x12\'\n\x04\x64ims\x18\x04 \x03(\x0b\x32\x19.inspection.InspectionDim\x12\'\n\x04vals\x18\x05 \x03(\x0b\x32\x19.inspection.InspectionVal\x12\x0c\n\x04memo\x18\x06 \x01(\tBFZDgo.easyops.local/contracts/protorepo-models/easyops/model/inspectionb\x06proto3')
  ,
  dependencies=[flow__sdk_dot_model_dot_inspection_dot_dim__pb2.DESCRIPTOR,flow__sdk_dot_model_dot_inspection_dot_val__pb2.DESCRIPTOR,])




_INSPECTIONMETRICGROUP = _descriptor.Descriptor(
  name='InspectionMetricGroup',
  full_name='inspection.InspectionMetricGroup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='inspection.InspectionMetricGroup.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='inspection.InspectionMetricGroup.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='inspection.InspectionMetricGroup.category', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dims', full_name='inspection.InspectionMetricGroup.dims', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vals', full_name='inspection.InspectionMetricGroup.vals', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='inspection.InspectionMetricGroup.memo', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=109,
  serialized_end=272,
)

_INSPECTIONMETRICGROUP.fields_by_name['dims'].message_type = flow__sdk_dot_model_dot_inspection_dot_dim__pb2._INSPECTIONDIM
_INSPECTIONMETRICGROUP.fields_by_name['vals'].message_type = flow__sdk_dot_model_dot_inspection_dot_val__pb2._INSPECTIONVAL
DESCRIPTOR.message_types_by_name['InspectionMetricGroup'] = _INSPECTIONMETRICGROUP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InspectionMetricGroup = _reflection.GeneratedProtocolMessageType('InspectionMetricGroup', (_message.Message,), {
  'DESCRIPTOR' : _INSPECTIONMETRICGROUP,
  '__module__' : 'metric_group_pb2'
  # @@protoc_insertion_point(class_scope:inspection.InspectionMetricGroup)
  })
_sym_db.RegisterMessage(InspectionMetricGroup)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
