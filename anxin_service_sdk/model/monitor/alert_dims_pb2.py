# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: alert_dims.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='alert_dims.proto',
  package='monitor',
  syntax='proto3',
  serialized_options=_b('ZAgo.easyops.local/contracts/protorepo-models/easyops/model/monitor'),
  serialized_pb=_b('\n\x10\x61lert_dims.proto\x12\x07monitor\"\x98\x01\n\tAlertDims\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12)\n\x06values\x18\x03 \x03(\x0b\x32\x19.monitor.AlertDims.Values\x12\x0c\n\x04type\x18\x04 \x01(\t\x1a.\n\x06Values\x12\r\n\x05value\x18\x01 \x01(\t\x12\x15\n\rdisplay_value\x18\x02 \x01(\tBCZAgo.easyops.local/contracts/protorepo-models/easyops/model/monitorb\x06proto3')
)




_ALERTDIMS_VALUES = _descriptor.Descriptor(
  name='Values',
  full_name='monitor.AlertDims.Values',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='monitor.AlertDims.Values.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='display_value', full_name='monitor.AlertDims.Values.display_value', index=1,
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
  serialized_start=136,
  serialized_end=182,
)

_ALERTDIMS = _descriptor.Descriptor(
  name='AlertDims',
  full_name='monitor.AlertDims',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='monitor.AlertDims.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='monitor.AlertDims.display_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='values', full_name='monitor.AlertDims.values', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='monitor.AlertDims.type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ALERTDIMS_VALUES, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=182,
)

_ALERTDIMS_VALUES.containing_type = _ALERTDIMS
_ALERTDIMS.fields_by_name['values'].message_type = _ALERTDIMS_VALUES
DESCRIPTOR.message_types_by_name['AlertDims'] = _ALERTDIMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AlertDims = _reflection.GeneratedProtocolMessageType('AlertDims', (_message.Message,), {

  'Values' : _reflection.GeneratedProtocolMessageType('Values', (_message.Message,), {
    'DESCRIPTOR' : _ALERTDIMS_VALUES,
    '__module__' : 'alert_dims_pb2'
    # @@protoc_insertion_point(class_scope:monitor.AlertDims.Values)
    })
  ,
  'DESCRIPTOR' : _ALERTDIMS,
  '__module__' : 'alert_dims_pb2'
  # @@protoc_insertion_point(class_scope:monitor.AlertDims)
  })
_sym_db.RegisterMessage(AlertDims)
_sym_db.RegisterMessage(AlertDims.Values)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)