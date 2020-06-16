# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: installed_micro_app_bootstrap.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='installed_micro_app_bootstrap.proto',
  package='micro_app',
  syntax='proto3',
  serialized_options=_b('ZCgo.easyops.local/contracts/protorepo-models/easyops/model/micro_app'),
  serialized_pb=_b('\n#installed_micro_app_bootstrap.proto\x12\tmicro_app\x1a\x1cgoogle/protobuf/struct.proto\"\xa1\x06\n\x1aInstalledMicroAppBootstrap\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08internal\x18\x02 \x01(\x08\x12\x0f\n\x07private\x18\x03 \x01(\x08\x12\x0e\n\x06legacy\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12:\n\x05icons\x18\x06 \x01(\x0b\x32+.micro_app.InstalledMicroAppBootstrap.Icons\x12\x16\n\x0estoryboardJson\x18\x07 \x01(\t\x12\x0c\n\x04tags\x18\x08 \x03(\t\x12\x16\n\x0e\x63urrentVersion\x18\t \x01(\t\x12\x15\n\rinstallStatus\x18\n \x01(\t\x12\x10\n\x08homepage\x18\x0b \x01(\t\x12\x44\n\nclonedFrom\x18\x0c \x01(\x0b\x32\x30.micro_app.InstalledMicroAppBootstrap.ClonedFrom\x12\r\n\x05owner\x18\r \x01(\t\x12\x0e\n\x06readme\x18\x0e \x01(\t\x12\x0e\n\x06status\x18\x0f \x01(\t\x12\r\n\x05\x63time\x18\x10 \x01(\t\x12\r\n\x05mtime\x18\x11 \x01(\t\x12\x0f\n\x07pkgName\x18\x12 \x01(\t\x12@\n\x08menuIcon\x18\x13 \x01(\x0b\x32..micro_app.InstalledMicroAppBootstrap.MenuIcon\x12\x16\n\x0eiconBackground\x18\x14 \x01(\t\x12.\n\rdefaultConfig\x18\x15 \x01(\x0b\x32\x17.google.protobuf.Struct\x12+\n\nuserConfig\x18\x16 \x01(\x0b\x32\x17.google.protobuf.Struct\x1a\x16\n\x05Icons\x12\r\n\x05large\x18\x01 \x01(\t\x1a:\n\nClonedFrom\x12\r\n\x05\x61ppId\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x1a\x64\n\x08MenuIcon\x12\x0b\n\x03lib\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\r\n\x05theme\x18\x03 \x01(\t\x12\x0c\n\x04icon\x18\x04 \x01(\t\x12\x0e\n\x06prefix\x18\x05 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x06 \x01(\tBEZCgo.easyops.local/contracts/protorepo-models/easyops/model/micro_appb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_INSTALLEDMICROAPPBOOTSTRAP_ICONS = _descriptor.Descriptor(
  name='Icons',
  full_name='micro_app.InstalledMicroAppBootstrap.Icons',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='large', full_name='micro_app.InstalledMicroAppBootstrap.Icons.large', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=698,
  serialized_end=720,
)

_INSTALLEDMICROAPPBOOTSTRAP_CLONEDFROM = _descriptor.Descriptor(
  name='ClonedFrom',
  full_name='micro_app.InstalledMicroAppBootstrap.ClonedFrom',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appId', full_name='micro_app.InstalledMicroAppBootstrap.ClonedFrom.appId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='micro_app.InstalledMicroAppBootstrap.ClonedFrom.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='micro_app.InstalledMicroAppBootstrap.ClonedFrom.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=722,
  serialized_end=780,
)

_INSTALLEDMICROAPPBOOTSTRAP_MENUICON = _descriptor.Descriptor(
  name='MenuIcon',
  full_name='micro_app.InstalledMicroAppBootstrap.MenuIcon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lib', full_name='micro_app.InstalledMicroAppBootstrap.MenuIcon.lib', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='micro_app.InstalledMicroAppBootstrap.MenuIcon.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='theme', full_name='micro_app.InstalledMicroAppBootstrap.MenuIcon.theme', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon', full_name='micro_app.InstalledMicroAppBootstrap.MenuIcon.icon', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prefix', full_name='micro_app.InstalledMicroAppBootstrap.MenuIcon.prefix', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='micro_app.InstalledMicroAppBootstrap.MenuIcon.category', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=782,
  serialized_end=882,
)

_INSTALLEDMICROAPPBOOTSTRAP = _descriptor.Descriptor(
  name='InstalledMicroAppBootstrap',
  full_name='micro_app.InstalledMicroAppBootstrap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='micro_app.InstalledMicroAppBootstrap.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='internal', full_name='micro_app.InstalledMicroAppBootstrap.internal', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='private', full_name='micro_app.InstalledMicroAppBootstrap.private', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='legacy', full_name='micro_app.InstalledMicroAppBootstrap.legacy', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='micro_app.InstalledMicroAppBootstrap.name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icons', full_name='micro_app.InstalledMicroAppBootstrap.icons', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='storyboardJson', full_name='micro_app.InstalledMicroAppBootstrap.storyboardJson', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='micro_app.InstalledMicroAppBootstrap.tags', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currentVersion', full_name='micro_app.InstalledMicroAppBootstrap.currentVersion', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='installStatus', full_name='micro_app.InstalledMicroAppBootstrap.installStatus', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='homepage', full_name='micro_app.InstalledMicroAppBootstrap.homepage', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clonedFrom', full_name='micro_app.InstalledMicroAppBootstrap.clonedFrom', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='owner', full_name='micro_app.InstalledMicroAppBootstrap.owner', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readme', full_name='micro_app.InstalledMicroAppBootstrap.readme', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='micro_app.InstalledMicroAppBootstrap.status', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='micro_app.InstalledMicroAppBootstrap.ctime', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='micro_app.InstalledMicroAppBootstrap.mtime', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pkgName', full_name='micro_app.InstalledMicroAppBootstrap.pkgName', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='menuIcon', full_name='micro_app.InstalledMicroAppBootstrap.menuIcon', index=18,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iconBackground', full_name='micro_app.InstalledMicroAppBootstrap.iconBackground', index=19,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='defaultConfig', full_name='micro_app.InstalledMicroAppBootstrap.defaultConfig', index=20,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userConfig', full_name='micro_app.InstalledMicroAppBootstrap.userConfig', index=21,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_INSTALLEDMICROAPPBOOTSTRAP_ICONS, _INSTALLEDMICROAPPBOOTSTRAP_CLONEDFROM, _INSTALLEDMICROAPPBOOTSTRAP_MENUICON, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=81,
  serialized_end=882,
)

_INSTALLEDMICROAPPBOOTSTRAP_ICONS.containing_type = _INSTALLEDMICROAPPBOOTSTRAP
_INSTALLEDMICROAPPBOOTSTRAP_CLONEDFROM.containing_type = _INSTALLEDMICROAPPBOOTSTRAP
_INSTALLEDMICROAPPBOOTSTRAP_MENUICON.containing_type = _INSTALLEDMICROAPPBOOTSTRAP
_INSTALLEDMICROAPPBOOTSTRAP.fields_by_name['icons'].message_type = _INSTALLEDMICROAPPBOOTSTRAP_ICONS
_INSTALLEDMICROAPPBOOTSTRAP.fields_by_name['clonedFrom'].message_type = _INSTALLEDMICROAPPBOOTSTRAP_CLONEDFROM
_INSTALLEDMICROAPPBOOTSTRAP.fields_by_name['menuIcon'].message_type = _INSTALLEDMICROAPPBOOTSTRAP_MENUICON
_INSTALLEDMICROAPPBOOTSTRAP.fields_by_name['defaultConfig'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_INSTALLEDMICROAPPBOOTSTRAP.fields_by_name['userConfig'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['InstalledMicroAppBootstrap'] = _INSTALLEDMICROAPPBOOTSTRAP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InstalledMicroAppBootstrap = _reflection.GeneratedProtocolMessageType('InstalledMicroAppBootstrap', (_message.Message,), {

  'Icons' : _reflection.GeneratedProtocolMessageType('Icons', (_message.Message,), {
    'DESCRIPTOR' : _INSTALLEDMICROAPPBOOTSTRAP_ICONS,
    '__module__' : 'installed_micro_app_bootstrap_pb2'
    # @@protoc_insertion_point(class_scope:micro_app.InstalledMicroAppBootstrap.Icons)
    })
  ,

  'ClonedFrom' : _reflection.GeneratedProtocolMessageType('ClonedFrom', (_message.Message,), {
    'DESCRIPTOR' : _INSTALLEDMICROAPPBOOTSTRAP_CLONEDFROM,
    '__module__' : 'installed_micro_app_bootstrap_pb2'
    # @@protoc_insertion_point(class_scope:micro_app.InstalledMicroAppBootstrap.ClonedFrom)
    })
  ,

  'MenuIcon' : _reflection.GeneratedProtocolMessageType('MenuIcon', (_message.Message,), {
    'DESCRIPTOR' : _INSTALLEDMICROAPPBOOTSTRAP_MENUICON,
    '__module__' : 'installed_micro_app_bootstrap_pb2'
    # @@protoc_insertion_point(class_scope:micro_app.InstalledMicroAppBootstrap.MenuIcon)
    })
  ,
  'DESCRIPTOR' : _INSTALLEDMICROAPPBOOTSTRAP,
  '__module__' : 'installed_micro_app_bootstrap_pb2'
  # @@protoc_insertion_point(class_scope:micro_app.InstalledMicroAppBootstrap)
  })
_sym_db.RegisterMessage(InstalledMicroAppBootstrap)
_sym_db.RegisterMessage(InstalledMicroAppBootstrap.Icons)
_sym_db.RegisterMessage(InstalledMicroAppBootstrap.ClonedFrom)
_sym_db.RegisterMessage(InstalledMicroAppBootstrap.MenuIcon)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)