# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sql_package_version.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sql_package_version.proto',
  package='database_delivery',
  syntax='proto3',
  serialized_options=_b('ZKgo.easyops.local/contracts/protorepo-models/easyops/model/database_delivery'),
  serialized_pb=_b('\n\x19sql_package_version.proto\x12\x11\x64\x61tabase_delivery\"\xab\x01\n\x11SQLPackageVersion\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x15\n\rrepoVersionId\x18\x03 \x01(\t\x12\x13\n\x0bversionName\x18\x04 \x01(\t\x12\x0c\n\x04memo\x18\x05 \x01(\t\x12\x0f\n\x07\x63reator\x18\x06 \x01(\t\x12\r\n\x05\x63time\x18\x07 \x01(\x03\x12\r\n\x05mtime\x18\x08 \x01(\x03\x12\x13\n\x0bversionType\x18\t \x01(\tBMZKgo.easyops.local/contracts/protorepo-models/easyops/model/database_deliveryb\x06proto3')
)




_SQLPACKAGEVERSION = _descriptor.Descriptor(
  name='SQLPackageVersion',
  full_name='database_delivery.SQLPackageVersion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='database_delivery.SQLPackageVersion.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='database_delivery.SQLPackageVersion.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repoVersionId', full_name='database_delivery.SQLPackageVersion.repoVersionId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionName', full_name='database_delivery.SQLPackageVersion.versionName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='database_delivery.SQLPackageVersion.memo', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='database_delivery.SQLPackageVersion.creator', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='database_delivery.SQLPackageVersion.ctime', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='database_delivery.SQLPackageVersion.mtime', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionType', full_name='database_delivery.SQLPackageVersion.versionType', index=8,
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
  serialized_start=49,
  serialized_end=220,
)

DESCRIPTOR.message_types_by_name['SQLPackageVersion'] = _SQLPACKAGEVERSION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SQLPackageVersion = _reflection.GeneratedProtocolMessageType('SQLPackageVersion', (_message.Message,), {
  'DESCRIPTOR' : _SQLPACKAGEVERSION,
  '__module__' : 'sql_package_version_pb2'
  # @@protoc_insertion_point(class_scope:database_delivery.SQLPackageVersion)
  })
_sym_db.RegisterMessage(SQLPackageVersion)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
