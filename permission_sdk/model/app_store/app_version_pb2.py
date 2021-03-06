# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app_version.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='app_version.proto',
  package='app_store',
  syntax='proto3',
  serialized_options=_b('ZCgo.easyops.local/contracts/protorepo-models/easyops/model/app_store'),
  serialized_pb=_b('\n\x11\x61pp_version.proto\x12\tapp_store\"\xdd\x01\n\nAppVersion\x12\x11\n\tversionId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0bversionName\x18\x03 \x01(\t\x12\x11\n\tchangeLog\x18\x04 \x01(\t\x12\x13\n\x0breleaseTime\x18\x05 \x01(\t\x12\x38\n\x0c\x64\x65pendencies\x18\x06 \x03(\x0b\x32\".app_store.AppVersion.Dependencies\x1a\x37\n\x0c\x44\x65pendencies\x12\x13\n\x0bpackageName\x18\x01 \x01(\t\x12\x12\n\nconstraint\x18\x02 \x01(\tBEZCgo.easyops.local/contracts/protorepo-models/easyops/model/app_storeb\x06proto3')
)




_APPVERSION_DEPENDENCIES = _descriptor.Descriptor(
  name='Dependencies',
  full_name='app_store.AppVersion.Dependencies',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='packageName', full_name='app_store.AppVersion.Dependencies.packageName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='constraint', full_name='app_store.AppVersion.Dependencies.constraint', index=1,
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
  serialized_start=199,
  serialized_end=254,
)

_APPVERSION = _descriptor.Descriptor(
  name='AppVersion',
  full_name='app_store.AppVersion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='versionId', full_name='app_store.AppVersion.versionId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='app_store.AppVersion.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionName', full_name='app_store.AppVersion.versionName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='changeLog', full_name='app_store.AppVersion.changeLog', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='releaseTime', full_name='app_store.AppVersion.releaseTime', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dependencies', full_name='app_store.AppVersion.dependencies', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_APPVERSION_DEPENDENCIES, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=254,
)

_APPVERSION_DEPENDENCIES.containing_type = _APPVERSION
_APPVERSION.fields_by_name['dependencies'].message_type = _APPVERSION_DEPENDENCIES
DESCRIPTOR.message_types_by_name['AppVersion'] = _APPVERSION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AppVersion = _reflection.GeneratedProtocolMessageType('AppVersion', (_message.Message,), {

  'Dependencies' : _reflection.GeneratedProtocolMessageType('Dependencies', (_message.Message,), {
    'DESCRIPTOR' : _APPVERSION_DEPENDENCIES,
    '__module__' : 'app_version_pb2'
    # @@protoc_insertion_point(class_scope:app_store.AppVersion.Dependencies)
    })
  ,
  'DESCRIPTOR' : _APPVERSION,
  '__module__' : 'app_version_pb2'
  # @@protoc_insertion_point(class_scope:app_store.AppVersion)
  })
_sym_db.RegisterMessage(AppVersion)
_sym_db.RegisterMessage(AppVersion.Dependencies)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
