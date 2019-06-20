# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: git_meta.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='git_meta.proto',
  package='pipeline',
  syntax='proto3',
  serialized_options=_b('ZBgo.easyops.local/contracts/protorepo-models/easyops/model/pipeline'),
  serialized_pb=_b('\n\x0egit_meta.proto\x12\x08pipeline\"\xb7\x01\n\x07GitMeta\x12\r\n\x05\x65vent\x18\x01 \x01(\t\x12\x0e\n\x06\x62\x65\x66ore\x18\x02 \x01(\t\x12\r\n\x05\x61\x66ter\x18\x03 \x01(\t\x12\x15\n\rauthor_avatar\x18\x04 \x01(\t\x12\x14\n\x0c\x61uthor_email\x18\x05 \x01(\t\x12\x13\n\x0b\x61uthor_name\x18\x06 \x01(\t\x12\x0f\n\x07message\x18\x07 \x01(\t\x12\x0b\n\x03ref\x18\x08 \x01(\t\x12\x0e\n\x06source\x18\t \x01(\t\x12\x0e\n\x06target\x18\n \x01(\tBDZBgo.easyops.local/contracts/protorepo-models/easyops/model/pipelineb\x06proto3')
)




_GITMETA = _descriptor.Descriptor(
  name='GitMeta',
  full_name='pipeline.GitMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event', full_name='pipeline.GitMeta.event', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='before', full_name='pipeline.GitMeta.before', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='after', full_name='pipeline.GitMeta.after', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='author_avatar', full_name='pipeline.GitMeta.author_avatar', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='author_email', full_name='pipeline.GitMeta.author_email', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='author_name', full_name='pipeline.GitMeta.author_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='pipeline.GitMeta.message', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ref', full_name='pipeline.GitMeta.ref', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='pipeline.GitMeta.source', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target', full_name='pipeline.GitMeta.target', index=9,
      number=10, type=9, cpp_type=9, label=1,
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
  serialized_start=29,
  serialized_end=212,
)

DESCRIPTOR.message_types_by_name['GitMeta'] = _GITMETA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GitMeta = _reflection.GeneratedProtocolMessageType('GitMeta', (_message.Message,), dict(
  DESCRIPTOR = _GITMETA,
  __module__ = 'git_meta_pb2'
  # @@protoc_insertion_point(class_scope:pipeline.GitMeta)
  ))
_sym_db.RegisterMessage(GitMeta)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
