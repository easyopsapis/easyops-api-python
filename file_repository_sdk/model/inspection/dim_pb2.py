# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dim.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dim.proto',
  package='inspection',
  syntax='proto3',
  serialized_options=_b('ZDgo.easyops.local/contracts/protorepo-models/easyops/model/inspection'),
  serialized_pb=_b('\n\tdim.proto\x12\ninspection\")\n\rInspectionDim\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\tBFZDgo.easyops.local/contracts/protorepo-models/easyops/model/inspectionb\x06proto3')
)




_INSPECTIONDIM = _descriptor.Descriptor(
  name='InspectionDim',
  full_name='inspection.InspectionDim',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='inspection.InspectionDim.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='inspection.InspectionDim.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=25,
  serialized_end=66,
)

DESCRIPTOR.message_types_by_name['InspectionDim'] = _INSPECTIONDIM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InspectionDim = _reflection.GeneratedProtocolMessageType('InspectionDim', (_message.Message,), {
  'DESCRIPTOR' : _INSPECTIONDIM,
  '__module__' : 'dim_pb2'
  # @@protoc_insertion_point(class_scope:inspection.InspectionDim)
  })
_sym_db.RegisterMessage(InspectionDim)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
