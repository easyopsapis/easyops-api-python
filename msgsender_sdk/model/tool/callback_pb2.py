# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: callback.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='callback.proto',
  package='tool',
  syntax='proto3',
  serialized_options=_b('Z>go.easyops.local/contracts/protorepo-models/easyops/model/tool'),
  serialized_pb=_b('\n\x0e\x63\x61llback.proto\x12\x04tool\"F\n\x08\x43\x61llback\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x0c\n\x04host\x18\x02 \x01(\t\x12\x0f\n\x07\x65nsName\x18\x03 \x01(\t\x12\x0e\n\x06method\x18\x04 \x01(\tB@Z>go.easyops.local/contracts/protorepo-models/easyops/model/toolb\x06proto3')
)




_CALLBACK = _descriptor.Descriptor(
  name='Callback',
  full_name='tool.Callback',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='tool.Callback.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host', full_name='tool.Callback.host', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ensName', full_name='tool.Callback.ensName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='method', full_name='tool.Callback.method', index=3,
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
  serialized_start=24,
  serialized_end=94,
)

DESCRIPTOR.message_types_by_name['Callback'] = _CALLBACK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Callback = _reflection.GeneratedProtocolMessageType('Callback', (_message.Message,), {
  'DESCRIPTOR' : _CALLBACK,
  '__module__' : 'callback_pb2'
  # @@protoc_insertion_point(class_scope:tool.Callback)
  })
_sym_db.RegisterMessage(Callback)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
