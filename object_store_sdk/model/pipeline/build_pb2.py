# -*- coding: utf-8 -*-
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


from object_store_sdk.model.pipeline import git_meta_pb2 as object__store__sdk_dot_model_dot_pipeline_dot_git__meta__pb2
from object_store_sdk.model.pipeline import build_status_pb2 as object__store__sdk_dot_model_dot_pipeline_dot_build__status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='build.proto',
  package='pipeline',
  syntax='proto3',
  serialized_options=_b('ZBgo.easyops.local/contracts/protorepo-models/easyops/model/pipeline'),
  serialized_pb=_b('\n\x0b\x62uild.proto\x12\x08pipeline\x1a.object_store_sdk/model/pipeline/git_meta.proto\x1a\x32object_store_sdk/model/pipeline/build_status.proto\"\xcc\x02\n\x05\x42uild\x12\n\n\x02id\x18\x01 \x01(\t\x12#\n\x08git_meta\x18\x02 \x01(\x0b\x32\x11.pipeline.GitMeta\x12\x0e\n\x06sender\x18\x03 \x01(\t\x12*\n\x08\x61rtifact\x18\x04 \x01(\x0b\x32\x18.pipeline.Build.Artifact\x12\x0f\n\x07\x63reated\x18\x05 \x01(\x05\x12\x13\n\x0byaml_string\x18\x06 \x01(\t\x12%\n\x06status\x18\x07 \x01(\x0b\x32\x15.pipeline.BuildStatus\x12\x0e\n\x06number\x18\x08 \x01(\t\x12\x0e\n\x06\x65vents\x18\t \x03(\t\x1ai\n\x08\x41rtifact\x12\x13\n\x0bpackageName\x18\x01 \x01(\t\x12\x13\n\x0bversionName\x18\x02 \x01(\t\x12\r\n\x05\x63time\x18\x03 \x01(\t\x12\x11\n\tpackageId\x18\x04 \x01(\t\x12\x11\n\tversionId\x18\x05 \x01(\tBDZBgo.easyops.local/contracts/protorepo-models/easyops/model/pipelineb\x06proto3')
  ,
  dependencies=[object__store__sdk_dot_model_dot_pipeline_dot_git__meta__pb2.DESCRIPTOR,object__store__sdk_dot_model_dot_pipeline_dot_build__status__pb2.DESCRIPTOR,])




_BUILD_ARTIFACT = _descriptor.Descriptor(
  name='Artifact',
  full_name='pipeline.Build.Artifact',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='packageName', full_name='pipeline.Build.Artifact.packageName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionName', full_name='pipeline.Build.Artifact.versionName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='pipeline.Build.Artifact.ctime', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageId', full_name='pipeline.Build.Artifact.packageId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionId', full_name='pipeline.Build.Artifact.versionId', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=353,
  serialized_end=458,
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
      name='artifact', full_name='pipeline.Build.artifact', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created', full_name='pipeline.Build.created', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='yaml_string', full_name='pipeline.Build.yaml_string', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='pipeline.Build.status', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='number', full_name='pipeline.Build.number', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='events', full_name='pipeline.Build.events', index=8,
      number=9, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_BUILD_ARTIFACT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=458,
)

_BUILD_ARTIFACT.containing_type = _BUILD
_BUILD.fields_by_name['git_meta'].message_type = object__store__sdk_dot_model_dot_pipeline_dot_git__meta__pb2._GITMETA
_BUILD.fields_by_name['artifact'].message_type = _BUILD_ARTIFACT
_BUILD.fields_by_name['status'].message_type = object__store__sdk_dot_model_dot_pipeline_dot_build__status__pb2._BUILDSTATUS
DESCRIPTOR.message_types_by_name['Build'] = _BUILD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Build = _reflection.GeneratedProtocolMessageType('Build', (_message.Message,), {

  'Artifact' : _reflection.GeneratedProtocolMessageType('Artifact', (_message.Message,), {
    'DESCRIPTOR' : _BUILD_ARTIFACT,
    '__module__' : 'build_pb2'
    # @@protoc_insertion_point(class_scope:pipeline.Build.Artifact)
    })
  ,
  'DESCRIPTOR' : _BUILD,
  '__module__' : 'build_pb2'
  # @@protoc_insertion_point(class_scope:pipeline.Build)
  })
_sym_db.RegisterMessage(Build)
_sym_db.RegisterMessage(Build.Artifact)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
