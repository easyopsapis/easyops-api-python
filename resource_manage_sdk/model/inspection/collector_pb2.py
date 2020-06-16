# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: collector.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from resource_manage_sdk.model.inspection import arg_pb2 as resource__manage__sdk_dot_model_dot_inspection_dot_arg__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='collector.proto',
  package='inspection',
  syntax='proto3',
  serialized_options=_b('ZDgo.easyops.local/contracts/protorepo-models/easyops/model/inspection'),
  serialized_pb=_b('\n\x0f\x63ollector.proto\x12\ninspection\x1a.resource_manage_sdk/model/inspection/arg.proto\"y\n\x13InspectionCollector\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12\x0e\n\x06script\x18\x04 \x01(\t\x12\'\n\x04\x61rgs\x18\x05 \x03(\x0b\x32\x19.inspection.InspectionArgBFZDgo.easyops.local/contracts/protorepo-models/easyops/model/inspectionb\x06proto3')
  ,
  dependencies=[resource__manage__sdk_dot_model_dot_inspection_dot_arg__pb2.DESCRIPTOR,])




_INSPECTIONCOLLECTOR = _descriptor.Descriptor(
  name='InspectionCollector',
  full_name='inspection.InspectionCollector',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='inspection.InspectionCollector.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='inspection.InspectionCollector.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='inspection.InspectionCollector.content', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='script', full_name='inspection.InspectionCollector.script', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='args', full_name='inspection.InspectionCollector.args', index=4,
      number=5, type=11, cpp_type=10, label=3,
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
  serialized_start=79,
  serialized_end=200,
)

_INSPECTIONCOLLECTOR.fields_by_name['args'].message_type = resource__manage__sdk_dot_model_dot_inspection_dot_arg__pb2._INSPECTIONARG
DESCRIPTOR.message_types_by_name['InspectionCollector'] = _INSPECTIONCOLLECTOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InspectionCollector = _reflection.GeneratedProtocolMessageType('InspectionCollector', (_message.Message,), {
  'DESCRIPTOR' : _INSPECTIONCOLLECTOR,
  '__module__' : 'collector_pb2'
  # @@protoc_insertion_point(class_scope:inspection.InspectionCollector)
  })
_sym_db.RegisterMessage(InspectionCollector)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
