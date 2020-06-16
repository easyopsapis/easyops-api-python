# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: update_version_env_type.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from artifact_sdk.model.artifact import version_pb2 as artifact__sdk_dot_model_dot_artifact_dot_version__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='update_version_env_type.proto',
  package='version',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1dupdate_version_env_type.proto\x12\x07version\x1a)artifact_sdk/model/artifact/version.proto\"U\n\x1bUpdateVersionEnvTypeRequest\x12\x11\n\tpackageId\x18\x01 \x01(\t\x12\x11\n\tversionId\x18\x02 \x01(\t\x12\x10\n\x08\x65nv_type\x18\x03 \x01(\x05\"x\n#UpdateVersionEnvTypeResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x1f\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x11.artifact.Versionb\x06proto3')
  ,
  dependencies=[artifact__sdk_dot_model_dot_artifact_dot_version__pb2.DESCRIPTOR,])




_UPDATEVERSIONENVTYPEREQUEST = _descriptor.Descriptor(
  name='UpdateVersionEnvTypeRequest',
  full_name='version.UpdateVersionEnvTypeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='packageId', full_name='version.UpdateVersionEnvTypeRequest.packageId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionId', full_name='version.UpdateVersionEnvTypeRequest.versionId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='env_type', full_name='version.UpdateVersionEnvTypeRequest.env_type', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=85,
  serialized_end=170,
)


_UPDATEVERSIONENVTYPERESPONSEWRAPPER = _descriptor.Descriptor(
  name='UpdateVersionEnvTypeResponseWrapper',
  full_name='version.UpdateVersionEnvTypeResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='version.UpdateVersionEnvTypeResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='version.UpdateVersionEnvTypeResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='version.UpdateVersionEnvTypeResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='version.UpdateVersionEnvTypeResponseWrapper.data', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=172,
  serialized_end=292,
)

_UPDATEVERSIONENVTYPERESPONSEWRAPPER.fields_by_name['data'].message_type = artifact__sdk_dot_model_dot_artifact_dot_version__pb2._VERSION
DESCRIPTOR.message_types_by_name['UpdateVersionEnvTypeRequest'] = _UPDATEVERSIONENVTYPEREQUEST
DESCRIPTOR.message_types_by_name['UpdateVersionEnvTypeResponseWrapper'] = _UPDATEVERSIONENVTYPERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateVersionEnvTypeRequest = _reflection.GeneratedProtocolMessageType('UpdateVersionEnvTypeRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEVERSIONENVTYPEREQUEST,
  '__module__' : 'update_version_env_type_pb2'
  # @@protoc_insertion_point(class_scope:version.UpdateVersionEnvTypeRequest)
  })
_sym_db.RegisterMessage(UpdateVersionEnvTypeRequest)

UpdateVersionEnvTypeResponseWrapper = _reflection.GeneratedProtocolMessageType('UpdateVersionEnvTypeResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEVERSIONENVTYPERESPONSEWRAPPER,
  '__module__' : 'update_version_env_type_pb2'
  # @@protoc_insertion_point(class_scope:version.UpdateVersionEnvTypeResponseWrapper)
  })
_sym_db.RegisterMessage(UpdateVersionEnvTypeResponseWrapper)


# @@protoc_insertion_point(module_scope)
