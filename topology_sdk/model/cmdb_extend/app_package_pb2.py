# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app_package.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='app_package.proto',
  package='cmdb_extend',
  syntax='proto3',
  serialized_options=_b('ZEgo.easyops.local/contracts/protorepo-models/easyops/model/cmdb_extend'),
  serialized_pb=_b('\n\x11\x61pp_package.proto\x12\x0b\x63mdb_extend\"\xf2\x01\n\nAppPackage\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tpackageId\x18\x02 \x01(\t\x12\x13\n\x0binstallPath\x18\x03 \x01(\t\x12\x10\n\x08isMaster\x18\x04 \x01(\t\x12\x10\n\x08platform\x18\x05 \x01(\t\x12\x0f\n\x07preStop\x18\x06 \x01(\x05\x12\x13\n\x0b\x66orceUpdate\x18\x07 \x01(\x05\x12\x13\n\x0bpostRestart\x18\x08 \x01(\x05\x12\x11\n\tautoStart\x18\t \x01(\x05\x12\x15\n\rtargetVersion\x18\n \x01(\t\x12\x11\n\tuserCheck\x18\x0b \x01(\x05\x12\x12\n\nfullUpdate\x18\x0c \x01(\x05\x42GZEgo.easyops.local/contracts/protorepo-models/easyops/model/cmdb_extendb\x06proto3')
)




_APPPACKAGE = _descriptor.Descriptor(
  name='AppPackage',
  full_name='cmdb_extend.AppPackage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cmdb_extend.AppPackage.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageId', full_name='cmdb_extend.AppPackage.packageId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='installPath', full_name='cmdb_extend.AppPackage.installPath', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isMaster', full_name='cmdb_extend.AppPackage.isMaster', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='platform', full_name='cmdb_extend.AppPackage.platform', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preStop', full_name='cmdb_extend.AppPackage.preStop', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='forceUpdate', full_name='cmdb_extend.AppPackage.forceUpdate', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='postRestart', full_name='cmdb_extend.AppPackage.postRestart', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='autoStart', full_name='cmdb_extend.AppPackage.autoStart', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targetVersion', full_name='cmdb_extend.AppPackage.targetVersion', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userCheck', full_name='cmdb_extend.AppPackage.userCheck', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fullUpdate', full_name='cmdb_extend.AppPackage.fullUpdate', index=11,
      number=12, type=5, cpp_type=1, label=1,
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
  serialized_start=35,
  serialized_end=277,
)

DESCRIPTOR.message_types_by_name['AppPackage'] = _APPPACKAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AppPackage = _reflection.GeneratedProtocolMessageType('AppPackage', (_message.Message,), {
  'DESCRIPTOR' : _APPPACKAGE,
  '__module__' : 'app_package_pb2'
  # @@protoc_insertion_point(class_scope:cmdb_extend.AppPackage)
  })
_sym_db.RegisterMessage(AppPackage)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
