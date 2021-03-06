# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: diff.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='diff.proto',
  package='file_repository',
  syntax='proto3',
  serialized_options=_b('ZIgo.easyops.local/contracts/protorepo-models/easyops/model/file_repository'),
  serialized_pb=_b('\n\ndiff.proto\x12\x0f\x66ile_repository\"\x90\x01\n\x04\x44iff\x12\n\n\x02op\x18\x01 \x01(\t\x12\x0c\n\x04\x66ile\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x0c\n\x04perm\x18\x04 \x01(\t\x12\x0e\n\x06newMd5\x18\x05 \x01(\t\x12\x0e\n\x06oldMd5\x18\x06 \x01(\t\x12\x0f\n\x07oldSize\x18\x07 \x01(\x03\x12\x0f\n\x07newSize\x18\x08 \x01(\x03\x12\x10\n\x08\x65ncoding\x18\t \x01(\tBKZIgo.easyops.local/contracts/protorepo-models/easyops/model/file_repositoryb\x06proto3')
)




_DIFF = _descriptor.Descriptor(
  name='Diff',
  full_name='file_repository.Diff',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='op', full_name='file_repository.Diff.op', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file', full_name='file_repository.Diff.file', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='file_repository.Diff.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='perm', full_name='file_repository.Diff.perm', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='newMd5', full_name='file_repository.Diff.newMd5', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='oldMd5', full_name='file_repository.Diff.oldMd5', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='oldSize', full_name='file_repository.Diff.oldSize', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='newSize', full_name='file_repository.Diff.newSize', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encoding', full_name='file_repository.Diff.encoding', index=8,
      number=9, type=9, cpp_type=9, label=1,
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
  serialized_start=32,
  serialized_end=176,
)

DESCRIPTOR.message_types_by_name['Diff'] = _DIFF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Diff = _reflection.GeneratedProtocolMessageType('Diff', (_message.Message,), {
  'DESCRIPTOR' : _DIFF,
  '__module__' : 'diff_pb2'
  # @@protoc_insertion_point(class_scope:file_repository.Diff)
  })
_sym_db.RegisterMessage(Diff)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
