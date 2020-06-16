# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: val.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from easy_work_service_sdk.model.inspection import condition_pb2 as easy__work__service__sdk_dot_model_dot_inspection_dot_condition__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='val.proto',
  package='inspection',
  syntax='proto3',
  serialized_options=_b('ZDgo.easyops.local/contracts/protorepo-models/easyops/model/inspection'),
  serialized_pb=_b('\n\tval.proto\x12\ninspection\x1a\x36\x65\x61sy_work_service_sdk/model/inspection/condition.proto\"\x98\x01\n\rInspectionVal\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04memo\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x0c\n\x04unit\x18\x05 \x01(\t\x12\x0e\n\x06weight\x18\x06 \x01(\x05\x12\x33\n\nconditions\x18\x07 \x03(\x0b\x32\x1f.inspection.InspectionConditionBFZDgo.easyops.local/contracts/protorepo-models/easyops/model/inspectionb\x06proto3')
  ,
  dependencies=[easy__work__service__sdk_dot_model_dot_inspection_dot_condition__pb2.DESCRIPTOR,])




_INSPECTIONVAL = _descriptor.Descriptor(
  name='InspectionVal',
  full_name='inspection.InspectionVal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='inspection.InspectionVal.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='inspection.InspectionVal.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='inspection.InspectionVal.memo', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='inspection.InspectionVal.type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unit', full_name='inspection.InspectionVal.unit', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight', full_name='inspection.InspectionVal.weight', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conditions', full_name='inspection.InspectionVal.conditions', index=6,
      number=7, type=11, cpp_type=10, label=3,
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
  serialized_start=82,
  serialized_end=234,
)

_INSPECTIONVAL.fields_by_name['conditions'].message_type = easy__work__service__sdk_dot_model_dot_inspection_dot_condition__pb2._INSPECTIONCONDITION
DESCRIPTOR.message_types_by_name['InspectionVal'] = _INSPECTIONVAL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InspectionVal = _reflection.GeneratedProtocolMessageType('InspectionVal', (_message.Message,), {
  'DESCRIPTOR' : _INSPECTIONVAL,
  '__module__' : 'val_pb2'
  # @@protoc_insertion_point(class_scope:inspection.InspectionVal)
  })
_sym_db.RegisterMessage(InspectionVal)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)