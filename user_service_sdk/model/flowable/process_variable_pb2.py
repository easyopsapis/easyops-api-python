# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: process_variable.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='process_variable.proto',
  package='flowable',
  syntax='proto3',
  serialized_options=_b('ZBgo.easyops.local/contracts/protorepo-models/easyops/model/flowable'),
  serialized_pb=_b('\n\x16process_variable.proto\x12\x08\x66lowable\"S\n\x17\x46lowableProcessVariable\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\x12\r\n\x05scope\x18\x04 \x01(\tBDZBgo.easyops.local/contracts/protorepo-models/easyops/model/flowableb\x06proto3')
)




_FLOWABLEPROCESSVARIABLE = _descriptor.Descriptor(
  name='FlowableProcessVariable',
  full_name='flowable.FlowableProcessVariable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='flowable.FlowableProcessVariable.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='flowable.FlowableProcessVariable.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='flowable.FlowableProcessVariable.value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scope', full_name='flowable.FlowableProcessVariable.scope', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=36,
  serialized_end=119,
)

DESCRIPTOR.message_types_by_name['FlowableProcessVariable'] = _FLOWABLEPROCESSVARIABLE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FlowableProcessVariable = _reflection.GeneratedProtocolMessageType('FlowableProcessVariable', (_message.Message,), {
  'DESCRIPTOR' : _FLOWABLEPROCESSVARIABLE,
  '__module__' : 'process_variable_pb2'
  # @@protoc_insertion_point(class_scope:flowable.FlowableProcessVariable)
  })
_sym_db.RegisterMessage(FlowableProcessVariable)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)