# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: release_package.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='release_package.proto',
  package='app_store',
  syntax='proto3',
  serialized_options=_b('ZCgo.easyops.local/contracts/protorepo-models/easyops/model/app_store'),
  serialized_pb=_b('\n\x15release_package.proto\x12\tapp_store\"\x92\x01\n\x0eReleasePackage\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bpackageName\x18\x02 \x01(\t\x12\x13\n\x0bversionName\x18\x03 \x01(\t\x12\x11\n\tpackageId\x18\x04 \x01(\t\x12\x11\n\tversionId\x18\x05 \x01(\t\x12\x13\n\x0b\x64ownloadUrl\x18\x06 \x01(\t\x12\r\n\x05group\x18\x07 \x01(\tBEZCgo.easyops.local/contracts/protorepo-models/easyops/model/app_storeb\x06proto3')
)




_RELEASEPACKAGE = _descriptor.Descriptor(
  name='ReleasePackage',
  full_name='app_store.ReleasePackage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='app_store.ReleasePackage.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageName', full_name='app_store.ReleasePackage.packageName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionName', full_name='app_store.ReleasePackage.versionName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageId', full_name='app_store.ReleasePackage.packageId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionId', full_name='app_store.ReleasePackage.versionId', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='downloadUrl', full_name='app_store.ReleasePackage.downloadUrl', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='group', full_name='app_store.ReleasePackage.group', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=37,
  serialized_end=183,
)

DESCRIPTOR.message_types_by_name['ReleasePackage'] = _RELEASEPACKAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReleasePackage = _reflection.GeneratedProtocolMessageType('ReleasePackage', (_message.Message,), dict(
  DESCRIPTOR = _RELEASEPACKAGE,
  __module__ = 'release_package_pb2'
  # @@protoc_insertion_point(class_scope:app_store.ReleasePackage)
  ))
_sym_db.RegisterMessage(ReleasePackage)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
