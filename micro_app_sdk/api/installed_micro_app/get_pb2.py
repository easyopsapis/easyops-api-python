# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from micro_app_sdk.model.micro_app import micro_app_container_pb2 as micro__app__sdk_dot_model_dot_micro__app_dot_micro__app__container__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='get.proto',
  package='installed_micro_app',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\tget.proto\x12\x13installed_micro_app\x1a\x37micro_app_sdk/model/micro_app/micro_app_container.proto\x1a\x1cgoogle/protobuf/struct.proto\"-\n\x1bGetInstalledMicroAppRequest\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\t\"\x93\x07\n\x1cGetInstalledMicroAppResponse\x12/\n\tcontainer\x18\x01 \x01(\x0b\x32\x1c.micro_app.MicroAppContainer\x12\x12\n\ninstanceId\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\r\n\x05\x61ppId\x18\x04 \x01(\t\x12\x46\n\x05icons\x18\x05 \x01(\x0b\x32\x37.installed_micro_app.GetInstalledMicroAppResponse.Icons\x12\x16\n\x0estoryboardJson\x18\x06 \x01(\t\x12\x0c\n\x04tags\x18\x07 \x03(\t\x12\x16\n\x0e\x63urrentVersion\x18\x08 \x01(\t\x12\x12\n\nappVersion\x18\t \x01(\t\x12\x15\n\rinstallStatus\x18\n \x01(\t\x12\x10\n\x08homepage\x18\x0b \x01(\t\x12\x10\n\x08internal\x18\x0c \x01(\t\x12\x0f\n\x07private\x18\r \x01(\t\x12P\n\nclonedFrom\x18\x0e \x01(\x0b\x32<.installed_micro_app.GetInstalledMicroAppResponse.ClonedFrom\x12\r\n\x05owner\x18\x0f \x01(\t\x12\x0e\n\x06readme\x18\x10 \x01(\t\x12\x0e\n\x06status\x18\x11 \x01(\t\x12\r\n\x05\x63time\x18\x12 \x01(\t\x12\r\n\x05mtime\x18\x13 \x01(\t\x12\x0f\n\x07pkgName\x18\x14 \x01(\t\x12\x16\n\x0eiconBackground\x18\x15 \x01(\t\x12L\n\x08menuIcon\x18\x16 \x01(\x0b\x32:.installed_micro_app.GetInstalledMicroAppResponse.MenuIcon\x12.\n\rdefaultConfig\x18\x17 \x01(\x0b\x32\x17.google.protobuf.Struct\x12+\n\nuserConfig\x18\x18 \x01(\x0b\x32\x17.google.protobuf.Struct\x1a\x16\n\x05Icons\x12\r\n\x05large\x18\x01 \x01(\t\x1a:\n\nClonedFrom\x12\r\n\x05\x61ppId\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x1a\x64\n\x08MenuIcon\x12\x0b\n\x03lib\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\r\n\x05theme\x18\x03 \x01(\t\x12\x0c\n\x04icon\x18\x04 \x01(\t\x12\x0e\n\x06prefix\x18\x05 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x06 \x01(\t\"\x98\x01\n#GetInstalledMicroAppResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12?\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x31.installed_micro_app.GetInstalledMicroAppResponseb\x06proto3')
  ,
  dependencies=[micro__app__sdk_dot_model_dot_micro__app_dot_micro__app__container__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_GETINSTALLEDMICROAPPREQUEST = _descriptor.Descriptor(
  name='GetInstalledMicroAppRequest',
  full_name='installed_micro_app.GetInstalledMicroAppRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='app_id', full_name='installed_micro_app.GetInstalledMicroAppRequest.app_id', index=0,
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
  serialized_start=121,
  serialized_end=166,
)


_GETINSTALLEDMICROAPPRESPONSE_ICONS = _descriptor.Descriptor(
  name='Icons',
  full_name='installed_micro_app.GetInstalledMicroAppResponse.Icons',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='large', full_name='installed_micro_app.GetInstalledMicroAppResponse.Icons.large', index=0,
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
  serialized_start=900,
  serialized_end=922,
)

_GETINSTALLEDMICROAPPRESPONSE_CLONEDFROM = _descriptor.Descriptor(
  name='ClonedFrom',
  full_name='installed_micro_app.GetInstalledMicroAppResponse.ClonedFrom',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appId', full_name='installed_micro_app.GetInstalledMicroAppResponse.ClonedFrom.appId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='installed_micro_app.GetInstalledMicroAppResponse.ClonedFrom.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='installed_micro_app.GetInstalledMicroAppResponse.ClonedFrom.name', index=2,
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
  serialized_start=924,
  serialized_end=982,
)

_GETINSTALLEDMICROAPPRESPONSE_MENUICON = _descriptor.Descriptor(
  name='MenuIcon',
  full_name='installed_micro_app.GetInstalledMicroAppResponse.MenuIcon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lib', full_name='installed_micro_app.GetInstalledMicroAppResponse.MenuIcon.lib', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='installed_micro_app.GetInstalledMicroAppResponse.MenuIcon.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='theme', full_name='installed_micro_app.GetInstalledMicroAppResponse.MenuIcon.theme', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon', full_name='installed_micro_app.GetInstalledMicroAppResponse.MenuIcon.icon', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prefix', full_name='installed_micro_app.GetInstalledMicroAppResponse.MenuIcon.prefix', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='installed_micro_app.GetInstalledMicroAppResponse.MenuIcon.category', index=5,
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
  serialized_start=984,
  serialized_end=1084,
)

_GETINSTALLEDMICROAPPRESPONSE = _descriptor.Descriptor(
  name='GetInstalledMicroAppResponse',
  full_name='installed_micro_app.GetInstalledMicroAppResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='container', full_name='installed_micro_app.GetInstalledMicroAppResponse.container', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='installed_micro_app.GetInstalledMicroAppResponse.instanceId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='installed_micro_app.GetInstalledMicroAppResponse.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='appId', full_name='installed_micro_app.GetInstalledMicroAppResponse.appId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icons', full_name='installed_micro_app.GetInstalledMicroAppResponse.icons', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='storyboardJson', full_name='installed_micro_app.GetInstalledMicroAppResponse.storyboardJson', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='installed_micro_app.GetInstalledMicroAppResponse.tags', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currentVersion', full_name='installed_micro_app.GetInstalledMicroAppResponse.currentVersion', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='appVersion', full_name='installed_micro_app.GetInstalledMicroAppResponse.appVersion', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='installStatus', full_name='installed_micro_app.GetInstalledMicroAppResponse.installStatus', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='homepage', full_name='installed_micro_app.GetInstalledMicroAppResponse.homepage', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='internal', full_name='installed_micro_app.GetInstalledMicroAppResponse.internal', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='private', full_name='installed_micro_app.GetInstalledMicroAppResponse.private', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clonedFrom', full_name='installed_micro_app.GetInstalledMicroAppResponse.clonedFrom', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='owner', full_name='installed_micro_app.GetInstalledMicroAppResponse.owner', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readme', full_name='installed_micro_app.GetInstalledMicroAppResponse.readme', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='installed_micro_app.GetInstalledMicroAppResponse.status', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='installed_micro_app.GetInstalledMicroAppResponse.ctime', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='installed_micro_app.GetInstalledMicroAppResponse.mtime', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pkgName', full_name='installed_micro_app.GetInstalledMicroAppResponse.pkgName', index=19,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iconBackground', full_name='installed_micro_app.GetInstalledMicroAppResponse.iconBackground', index=20,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='menuIcon', full_name='installed_micro_app.GetInstalledMicroAppResponse.menuIcon', index=21,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='defaultConfig', full_name='installed_micro_app.GetInstalledMicroAppResponse.defaultConfig', index=22,
      number=23, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userConfig', full_name='installed_micro_app.GetInstalledMicroAppResponse.userConfig', index=23,
      number=24, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETINSTALLEDMICROAPPRESPONSE_ICONS, _GETINSTALLEDMICROAPPRESPONSE_CLONEDFROM, _GETINSTALLEDMICROAPPRESPONSE_MENUICON, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=169,
  serialized_end=1084,
)


_GETINSTALLEDMICROAPPRESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetInstalledMicroAppResponseWrapper',
  full_name='installed_micro_app.GetInstalledMicroAppResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='installed_micro_app.GetInstalledMicroAppResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='installed_micro_app.GetInstalledMicroAppResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='installed_micro_app.GetInstalledMicroAppResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='installed_micro_app.GetInstalledMicroAppResponseWrapper.data', index=3,
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
  serialized_start=1087,
  serialized_end=1239,
)

_GETINSTALLEDMICROAPPRESPONSE_ICONS.containing_type = _GETINSTALLEDMICROAPPRESPONSE
_GETINSTALLEDMICROAPPRESPONSE_CLONEDFROM.containing_type = _GETINSTALLEDMICROAPPRESPONSE
_GETINSTALLEDMICROAPPRESPONSE_MENUICON.containing_type = _GETINSTALLEDMICROAPPRESPONSE
_GETINSTALLEDMICROAPPRESPONSE.fields_by_name['container'].message_type = micro__app__sdk_dot_model_dot_micro__app_dot_micro__app__container__pb2._MICROAPPCONTAINER
_GETINSTALLEDMICROAPPRESPONSE.fields_by_name['icons'].message_type = _GETINSTALLEDMICROAPPRESPONSE_ICONS
_GETINSTALLEDMICROAPPRESPONSE.fields_by_name['clonedFrom'].message_type = _GETINSTALLEDMICROAPPRESPONSE_CLONEDFROM
_GETINSTALLEDMICROAPPRESPONSE.fields_by_name['menuIcon'].message_type = _GETINSTALLEDMICROAPPRESPONSE_MENUICON
_GETINSTALLEDMICROAPPRESPONSE.fields_by_name['defaultConfig'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_GETINSTALLEDMICROAPPRESPONSE.fields_by_name['userConfig'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_GETINSTALLEDMICROAPPRESPONSEWRAPPER.fields_by_name['data'].message_type = _GETINSTALLEDMICROAPPRESPONSE
DESCRIPTOR.message_types_by_name['GetInstalledMicroAppRequest'] = _GETINSTALLEDMICROAPPREQUEST
DESCRIPTOR.message_types_by_name['GetInstalledMicroAppResponse'] = _GETINSTALLEDMICROAPPRESPONSE
DESCRIPTOR.message_types_by_name['GetInstalledMicroAppResponseWrapper'] = _GETINSTALLEDMICROAPPRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetInstalledMicroAppRequest = _reflection.GeneratedProtocolMessageType('GetInstalledMicroAppRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETINSTALLEDMICROAPPREQUEST,
  '__module__' : 'get_pb2'
  # @@protoc_insertion_point(class_scope:installed_micro_app.GetInstalledMicroAppRequest)
  })
_sym_db.RegisterMessage(GetInstalledMicroAppRequest)

GetInstalledMicroAppResponse = _reflection.GeneratedProtocolMessageType('GetInstalledMicroAppResponse', (_message.Message,), {

  'Icons' : _reflection.GeneratedProtocolMessageType('Icons', (_message.Message,), {
    'DESCRIPTOR' : _GETINSTALLEDMICROAPPRESPONSE_ICONS,
    '__module__' : 'get_pb2'
    # @@protoc_insertion_point(class_scope:installed_micro_app.GetInstalledMicroAppResponse.Icons)
    })
  ,

  'ClonedFrom' : _reflection.GeneratedProtocolMessageType('ClonedFrom', (_message.Message,), {
    'DESCRIPTOR' : _GETINSTALLEDMICROAPPRESPONSE_CLONEDFROM,
    '__module__' : 'get_pb2'
    # @@protoc_insertion_point(class_scope:installed_micro_app.GetInstalledMicroAppResponse.ClonedFrom)
    })
  ,

  'MenuIcon' : _reflection.GeneratedProtocolMessageType('MenuIcon', (_message.Message,), {
    'DESCRIPTOR' : _GETINSTALLEDMICROAPPRESPONSE_MENUICON,
    '__module__' : 'get_pb2'
    # @@protoc_insertion_point(class_scope:installed_micro_app.GetInstalledMicroAppResponse.MenuIcon)
    })
  ,
  'DESCRIPTOR' : _GETINSTALLEDMICROAPPRESPONSE,
  '__module__' : 'get_pb2'
  # @@protoc_insertion_point(class_scope:installed_micro_app.GetInstalledMicroAppResponse)
  })
_sym_db.RegisterMessage(GetInstalledMicroAppResponse)
_sym_db.RegisterMessage(GetInstalledMicroAppResponse.Icons)
_sym_db.RegisterMessage(GetInstalledMicroAppResponse.ClonedFrom)
_sym_db.RegisterMessage(GetInstalledMicroAppResponse.MenuIcon)

GetInstalledMicroAppResponseWrapper = _reflection.GeneratedProtocolMessageType('GetInstalledMicroAppResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _GETINSTALLEDMICROAPPRESPONSEWRAPPER,
  '__module__' : 'get_pb2'
  # @@protoc_insertion_point(class_scope:installed_micro_app.GetInstalledMicroAppResponseWrapper)
  })
_sym_db.RegisterMessage(GetInstalledMicroAppResponseWrapper)


# @@protoc_insertion_point(module_scope)
