# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: build.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from model.pipeline import build_status_pb2 as model_dot_pipeline_dot_build__status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='build.proto',
  package='pipeline',
  syntax='proto3',
  serialized_options=_b('ZBgo.easyops.local/contracts/protorepo-models/easyops/model/pipeline'),
  serialized_pb=_b('\n\x0b\x62uild.proto\x12\x08pipeline\x1a!model/pipeline/build_status.proto\"\xe5\x02\n\x05\x42uild\x12\n\n\x02id\x18\x01 \x01(\t\x12)\n\x08git_meta\x18\x02 \x01(\x0b\x32\x17.pipeline.Build.GitMeta\x12\x0e\n\x06sender\x18\x03 \x01(\t\x12\x0f\n\x07\x63reated\x18\x04 \x01(\x05\x12\x13\n\x0byaml_string\x18\x05 \x01(\t\x12%\n\x06status\x18\x06 \x01(\x0b\x32\x15.pipeline.BuildStatus\x12\x0e\n\x06number\x18\x07 \x01(\t\x1a\xb7\x01\n\x07GitMeta\x12\r\n\x05\x65vent\x18\x01 \x01(\t\x12\x0e\n\x06\x62\x65\x66ore\x18\x02 \x01(\t\x12\r\n\x05\x61\x66ter\x18\x03 \x01(\t\x12\x15\n\rauthor_avatar\x18\x04 \x01(\t\x12\x14\n\x0c\x61uthor_email\x18\x05 \x01(\t\x12\x13\n\x0b\x61uthor_name\x18\x06 \x01(\t\x12\x0f\n\x07message\x18\x07 \x01(\t\x12\x0b\n\x03ref\x18\x08 \x01(\t\x12\x0e\n\x06source\x18\t \x01(\t\x12\x0e\n\x06target\x18\n \x01(\tBDZBgo.easyops.local/contracts/protorepo-models/easyops/model/pipelineb\x06proto3')
  ,
  dependencies=[model_dot_pipeline_dot_build__status__pb2.DESCRIPTOR,])




_BUILD_GITMETA = _descriptor.Descriptor(
  name='GitMeta',
  full_name='pipeline.Build.GitMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event', full_name='pipeline.Build.GitMeta.event', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='before', full_name='pipeline.Build.GitMeta.before', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='after', full_name='pipeline.Build.GitMeta.after', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='author_avatar', full_name='pipeline.Build.GitMeta.author_avatar', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='author_email', full_name='pipeline.Build.GitMeta.author_email', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='author_name', full_name='pipeline.Build.GitMeta.author_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='pipeline.Build.GitMeta.message', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ref', full_name='pipeline.Build.GitMeta.ref', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='pipeline.Build.GitMeta.source', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target', full_name='pipeline.Build.GitMeta.target', index=9,
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
  serialized_start=235,
  serialized_end=418,
)

_BUILD = _descriptor.Descriptor(
  name='Build',
  full_name='pipeline.Build',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='pipeline.Build.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='git_meta', full_name='pipeline.Build.git_meta', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sender', full_name='pipeline.Build.sender', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created', full_name='pipeline.Build.created', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='yaml_string', full_name='pipeline.Build.yaml_string', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='pipeline.Build.status', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='number', full_name='pipeline.Build.number', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_BUILD_GITMETA, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=418,
)

_BUILD_GITMETA.containing_type = _BUILD
_BUILD.fields_by_name['git_meta'].message_type = _BUILD_GITMETA
_BUILD.fields_by_name['status'].message_type = model_dot_pipeline_dot_build__status__pb2._BUILDSTATUS
DESCRIPTOR.message_types_by_name['Build'] = _BUILD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Build = _reflection.GeneratedProtocolMessageType('Build', (_message.Message,), dict(

  GitMeta = _reflection.GeneratedProtocolMessageType('GitMeta', (_message.Message,), dict(
    DESCRIPTOR = _BUILD_GITMETA,
    __module__ = 'build_pb2'
    # @@protoc_insertion_point(class_scope:pipeline.Build.GitMeta)
    ))
  ,
  DESCRIPTOR = _BUILD,
  __module__ = 'build_pb2'
  # @@protoc_insertion_point(class_scope:pipeline.Build)
  ))
_sym_db.RegisterMessage(Build)
_sym_db.RegisterMessage(Build.GitMeta)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)