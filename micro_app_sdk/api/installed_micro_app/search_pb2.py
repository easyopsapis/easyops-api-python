# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: search.proto

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
  name='search.proto',
  package='installed_micro_app',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0csearch.proto\x12\x13installed_micro_app\x1a\x1cgoogle/protobuf/struct.proto\"\xb9\x01\n\x1eSearchInstalledMicroAppRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12H\n\x05query\x18\x03 \x01(\x0b\x32\x39.installed_micro_app.SearchInstalledMicroAppRequest.Query\x1a,\n\x05Query\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x16\n\x0e\x66ilterInternal\x18\x02 \x01(\x08\"\xff\x07\n\x1fSearchInstalledMicroAppResponse\x12\r\n\x05total\x18\x01 \x01(\x05\x12\x0c\n\x04page\x18\x02 \x01(\x05\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12G\n\x04list\x18\x04 \x03(\x0b\x32\x39.installed_micro_app.SearchInstalledMicroAppResponse.List\x1a\xe2\x06\n\x04List\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x61ppId\x18\x03 \x01(\t\x12N\n\x05icons\x18\x04 \x01(\x0b\x32?.installed_micro_app.SearchInstalledMicroAppResponse.List.Icons\x12\x16\n\x0estoryboardJson\x18\x05 \x01(\t\x12\x0c\n\x04tags\x18\x06 \x03(\t\x12\x16\n\x0e\x63urrentVersion\x18\x07 \x01(\t\x12\x12\n\nappVersion\x18\x08 \x01(\t\x12\x15\n\rinstallStatus\x18\t \x01(\t\x12\x10\n\x08homepage\x18\n \x01(\t\x12\x10\n\x08internal\x18\x0b \x01(\t\x12\x0f\n\x07private\x18\x0c \x01(\t\x12X\n\nclonedFrom\x18\r \x01(\x0b\x32\x44.installed_micro_app.SearchInstalledMicroAppResponse.List.ClonedFrom\x12\r\n\x05owner\x18\x0e \x01(\t\x12\x0e\n\x06readme\x18\x0f \x01(\t\x12\x0e\n\x06status\x18\x10 \x01(\t\x12\r\n\x05\x63time\x18\x11 \x01(\t\x12\r\n\x05mtime\x18\x12 \x01(\t\x12\x0f\n\x07pkgName\x18\x13 \x01(\t\x12\x16\n\x0eiconBackground\x18\x14 \x01(\t\x12T\n\x08menuIcon\x18\x15 \x01(\x0b\x32\x42.installed_micro_app.SearchInstalledMicroAppResponse.List.MenuIcon\x12.\n\rdefaultConfig\x18\x16 \x01(\x0b\x32\x17.google.protobuf.Struct\x12+\n\nuserConfig\x18\x17 \x01(\x0b\x32\x17.google.protobuf.Struct\x1a\x16\n\x05Icons\x12\r\n\x05large\x18\x01 \x01(\t\x1a:\n\nClonedFrom\x12\r\n\x05\x61ppId\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x1a\x64\n\x08MenuIcon\x12\x0b\n\x03lib\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\r\n\x05theme\x18\x03 \x01(\t\x12\x0c\n\x04icon\x18\x04 \x01(\t\x12\x0e\n\x06prefix\x18\x05 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x06 \x01(\t\"\x9e\x01\n&SearchInstalledMicroAppResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x42\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x34.installed_micro_app.SearchInstalledMicroAppResponseb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_SEARCHINSTALLEDMICROAPPREQUEST_QUERY = _descriptor.Descriptor(
  name='Query',
  full_name='installed_micro_app.SearchInstalledMicroAppRequest.Query',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='installed_micro_app.SearchInstalledMicroAppRequest.Query.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filterInternal', full_name='installed_micro_app.SearchInstalledMicroAppRequest.Query.filterInternal', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=209,
  serialized_end=253,
)

_SEARCHINSTALLEDMICROAPPREQUEST = _descriptor.Descriptor(
  name='SearchInstalledMicroAppRequest',
  full_name='installed_micro_app.SearchInstalledMicroAppRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='installed_micro_app.SearchInstalledMicroAppRequest.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='installed_micro_app.SearchInstalledMicroAppRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='query', full_name='installed_micro_app.SearchInstalledMicroAppRequest.query', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SEARCHINSTALLEDMICROAPPREQUEST_QUERY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=68,
  serialized_end=253,
)


_SEARCHINSTALLEDMICROAPPRESPONSE_LIST_ICONS = _descriptor.Descriptor(
  name='Icons',
  full_name='installed_micro_app.SearchInstalledMicroAppResponse.List.Icons',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='large', full_name='installed_micro_app.SearchInstalledMicroAppResponse.List.Icons.large', index=0,
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
  serialized_start=1095,
  serialized_end=1117,
)

_SEARCHINSTALLEDMICROAPPRESPONSE_LIST_CLONEDFROM = _descriptor.Descriptor(
  name='ClonedFrom',
  full_name='installed_micro_app.SearchInstalledMicroAppResponse.List.ClonedFrom',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appId', full_name='installed_micro_app.SearchInstalledMicroAppResponse.List.ClonedFrom.appId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='installed_micro_app.SearchInstalledMicroAppResponse.List.ClonedFrom.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='installed_micro_app.SearchInstalledMicroAppResponse.List.ClonedFrom.name', index=2,
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
  serialized_start=1119,
  serialized_end=1177,
)

_SEARCHINSTALLEDMICROAPPRESPONSE_LIST_MENUICON = _descriptor.Descriptor(
  name='MenuIcon',
  full_name='installed_micro_app.SearchInstalledMicroAppResponse.List.MenuIcon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lib', full_name='installed_micro_app.SearchInstalledMicroAppResponse.List.MenuIcon.lib', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='installed_micro_app.SearchInstalledMicroAppResponse.List.MenuIcon.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='theme', full_name='installed_micro_app.SearchInstalledMicroAppResponse.List.MenuIcon.theme', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon', full_name='installed_micro_app.SearchInstalledMicroAppResponse.List.MenuIcon.icon', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prefix', full_name='installed_micro_app.SearchInstalledMicroAppResponse.List.MenuIcon.prefix', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='installed_micro_app.SearchInstalledMicroAppResponse.List.MenuIcon.category', index=5,
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
  serialized_start=1179,
  serialized_end=1279,
)

_SEARCHINSTALLEDMICROAPPRESPONSE_LIST = _descriptor.Descriptor(
  name='List',
  full_name='installed_micro_app.SearchInstalledMicroAppResponse.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='installed_micro_app.SearchInstalledMicroAppResponse.List.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='installed_micro_app.SearchInstalledMicroAppResponse.List.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='appId', full_name='installed_micro_app.SearchInstalledMicroAppResponse.List.appId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icons', full_name='installed_micro_app.SearchInstalledMicroAppResponse.List.icons', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='storyboardJson', full_name='installed_micro_app.SearchInstalledMicroAppResponse.List.storyboardJson', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='installed_micro_app.SearchInstalledMicroAppResponse.List.tags', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currentVersion', full_name='installed_micro_app.SearchInstalledMicroAppResponse.List.currentVersion', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='appVersion', full_name='installed_micro_app.SearchInstalledMicroAppResponse.List.appVersion', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='installStatus', full_name='installed_micro_app.SearchInstalledMicroAppResponse.List.installStatus', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='homepage', full_name='installed_micro_app.SearchInstalledMicroAppResponse.List.homepage', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='internal', full_name='installed_micro_app.SearchInstalledMicroAppResponse.List.internal', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='private', full_name='installed_micro_app.SearchInstalledMicroAppResponse.List.private', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clonedFrom', full_name='installed_micro_app.SearchInstalledMicroAppResponse.List.clonedFrom', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='owner', full_name='installed_micro_app.SearchInstalledMicroAppResponse.List.owner', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readme', full_name='installed_micro_app.SearchInstalledMicroAppResponse.List.readme', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='installed_micro_app.SearchInstalledMicroAppResponse.List.status', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='installed_micro_app.SearchInstalledMicroAppResponse.List.ctime', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='installed_micro_app.SearchInstalledMicroAppResponse.List.mtime', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pkgName', full_name='installed_micro_app.SearchInstalledMicroAppResponse.List.pkgName', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iconBackground', full_name='installed_micro_app.SearchInstalledMicroAppResponse.List.iconBackground', index=19,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='menuIcon', full_name='installed_micro_app.SearchInstalledMicroAppResponse.List.menuIcon', index=20,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='defaultConfig', full_name='installed_micro_app.SearchInstalledMicroAppResponse.List.defaultConfig', index=21,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userConfig', full_name='installed_micro_app.SearchInstalledMicroAppResponse.List.userConfig', index=22,
      number=23, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SEARCHINSTALLEDMICROAPPRESPONSE_LIST_ICONS, _SEARCHINSTALLEDMICROAPPRESPONSE_LIST_CLONEDFROM, _SEARCHINSTALLEDMICROAPPRESPONSE_LIST_MENUICON, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=413,
  serialized_end=1279,
)

_SEARCHINSTALLEDMICROAPPRESPONSE = _descriptor.Descriptor(
  name='SearchInstalledMicroAppResponse',
  full_name='installed_micro_app.SearchInstalledMicroAppResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='total', full_name='installed_micro_app.SearchInstalledMicroAppResponse.total', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page', full_name='installed_micro_app.SearchInstalledMicroAppResponse.page', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='installed_micro_app.SearchInstalledMicroAppResponse.page_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='installed_micro_app.SearchInstalledMicroAppResponse.list', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SEARCHINSTALLEDMICROAPPRESPONSE_LIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=256,
  serialized_end=1279,
)


_SEARCHINSTALLEDMICROAPPRESPONSEWRAPPER = _descriptor.Descriptor(
  name='SearchInstalledMicroAppResponseWrapper',
  full_name='installed_micro_app.SearchInstalledMicroAppResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='installed_micro_app.SearchInstalledMicroAppResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='installed_micro_app.SearchInstalledMicroAppResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='installed_micro_app.SearchInstalledMicroAppResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='installed_micro_app.SearchInstalledMicroAppResponseWrapper.data', index=3,
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
  serialized_start=1282,
  serialized_end=1440,
)

_SEARCHINSTALLEDMICROAPPREQUEST_QUERY.containing_type = _SEARCHINSTALLEDMICROAPPREQUEST
_SEARCHINSTALLEDMICROAPPREQUEST.fields_by_name['query'].message_type = _SEARCHINSTALLEDMICROAPPREQUEST_QUERY
_SEARCHINSTALLEDMICROAPPRESPONSE_LIST_ICONS.containing_type = _SEARCHINSTALLEDMICROAPPRESPONSE_LIST
_SEARCHINSTALLEDMICROAPPRESPONSE_LIST_CLONEDFROM.containing_type = _SEARCHINSTALLEDMICROAPPRESPONSE_LIST
_SEARCHINSTALLEDMICROAPPRESPONSE_LIST_MENUICON.containing_type = _SEARCHINSTALLEDMICROAPPRESPONSE_LIST
_SEARCHINSTALLEDMICROAPPRESPONSE_LIST.fields_by_name['icons'].message_type = _SEARCHINSTALLEDMICROAPPRESPONSE_LIST_ICONS
_SEARCHINSTALLEDMICROAPPRESPONSE_LIST.fields_by_name['clonedFrom'].message_type = _SEARCHINSTALLEDMICROAPPRESPONSE_LIST_CLONEDFROM
_SEARCHINSTALLEDMICROAPPRESPONSE_LIST.fields_by_name['menuIcon'].message_type = _SEARCHINSTALLEDMICROAPPRESPONSE_LIST_MENUICON
_SEARCHINSTALLEDMICROAPPRESPONSE_LIST.fields_by_name['defaultConfig'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SEARCHINSTALLEDMICROAPPRESPONSE_LIST.fields_by_name['userConfig'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SEARCHINSTALLEDMICROAPPRESPONSE_LIST.containing_type = _SEARCHINSTALLEDMICROAPPRESPONSE
_SEARCHINSTALLEDMICROAPPRESPONSE.fields_by_name['list'].message_type = _SEARCHINSTALLEDMICROAPPRESPONSE_LIST
_SEARCHINSTALLEDMICROAPPRESPONSEWRAPPER.fields_by_name['data'].message_type = _SEARCHINSTALLEDMICROAPPRESPONSE
DESCRIPTOR.message_types_by_name['SearchInstalledMicroAppRequest'] = _SEARCHINSTALLEDMICROAPPREQUEST
DESCRIPTOR.message_types_by_name['SearchInstalledMicroAppResponse'] = _SEARCHINSTALLEDMICROAPPRESPONSE
DESCRIPTOR.message_types_by_name['SearchInstalledMicroAppResponseWrapper'] = _SEARCHINSTALLEDMICROAPPRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SearchInstalledMicroAppRequest = _reflection.GeneratedProtocolMessageType('SearchInstalledMicroAppRequest', (_message.Message,), {

  'Query' : _reflection.GeneratedProtocolMessageType('Query', (_message.Message,), {
    'DESCRIPTOR' : _SEARCHINSTALLEDMICROAPPREQUEST_QUERY,
    '__module__' : 'search_pb2'
    # @@protoc_insertion_point(class_scope:installed_micro_app.SearchInstalledMicroAppRequest.Query)
    })
  ,
  'DESCRIPTOR' : _SEARCHINSTALLEDMICROAPPREQUEST,
  '__module__' : 'search_pb2'
  # @@protoc_insertion_point(class_scope:installed_micro_app.SearchInstalledMicroAppRequest)
  })
_sym_db.RegisterMessage(SearchInstalledMicroAppRequest)
_sym_db.RegisterMessage(SearchInstalledMicroAppRequest.Query)

SearchInstalledMicroAppResponse = _reflection.GeneratedProtocolMessageType('SearchInstalledMicroAppResponse', (_message.Message,), {

  'List' : _reflection.GeneratedProtocolMessageType('List', (_message.Message,), {

    'Icons' : _reflection.GeneratedProtocolMessageType('Icons', (_message.Message,), {
      'DESCRIPTOR' : _SEARCHINSTALLEDMICROAPPRESPONSE_LIST_ICONS,
      '__module__' : 'search_pb2'
      # @@protoc_insertion_point(class_scope:installed_micro_app.SearchInstalledMicroAppResponse.List.Icons)
      })
    ,

    'ClonedFrom' : _reflection.GeneratedProtocolMessageType('ClonedFrom', (_message.Message,), {
      'DESCRIPTOR' : _SEARCHINSTALLEDMICROAPPRESPONSE_LIST_CLONEDFROM,
      '__module__' : 'search_pb2'
      # @@protoc_insertion_point(class_scope:installed_micro_app.SearchInstalledMicroAppResponse.List.ClonedFrom)
      })
    ,

    'MenuIcon' : _reflection.GeneratedProtocolMessageType('MenuIcon', (_message.Message,), {
      'DESCRIPTOR' : _SEARCHINSTALLEDMICROAPPRESPONSE_LIST_MENUICON,
      '__module__' : 'search_pb2'
      # @@protoc_insertion_point(class_scope:installed_micro_app.SearchInstalledMicroAppResponse.List.MenuIcon)
      })
    ,
    'DESCRIPTOR' : _SEARCHINSTALLEDMICROAPPRESPONSE_LIST,
    '__module__' : 'search_pb2'
    # @@protoc_insertion_point(class_scope:installed_micro_app.SearchInstalledMicroAppResponse.List)
    })
  ,
  'DESCRIPTOR' : _SEARCHINSTALLEDMICROAPPRESPONSE,
  '__module__' : 'search_pb2'
  # @@protoc_insertion_point(class_scope:installed_micro_app.SearchInstalledMicroAppResponse)
  })
_sym_db.RegisterMessage(SearchInstalledMicroAppResponse)
_sym_db.RegisterMessage(SearchInstalledMicroAppResponse.List)
_sym_db.RegisterMessage(SearchInstalledMicroAppResponse.List.Icons)
_sym_db.RegisterMessage(SearchInstalledMicroAppResponse.List.ClonedFrom)
_sym_db.RegisterMessage(SearchInstalledMicroAppResponse.List.MenuIcon)

SearchInstalledMicroAppResponseWrapper = _reflection.GeneratedProtocolMessageType('SearchInstalledMicroAppResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHINSTALLEDMICROAPPRESPONSEWRAPPER,
  '__module__' : 'search_pb2'
  # @@protoc_insertion_point(class_scope:installed_micro_app.SearchInstalledMicroAppResponseWrapper)
  })
_sym_db.RegisterMessage(SearchInstalledMicroAppResponseWrapper)


# @@protoc_insertion_point(module_scope)
