# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: report_installed_micro_app_result.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from micro_app_sdk.model.micro_app import installed_micro_app_pb2 as micro__app__sdk_dot_model_dot_micro__app_dot_installed__micro__app__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='report_installed_micro_app_result.proto',
  package='report',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\'report_installed_micro_app_result.proto\x12\x06report\x1a\x37micro_app_sdk/model/micro_app/installed_micro_app.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xcf\x01\n$ReportInstalledMicroAppResultRequest\x12Q\n\rinstalledApps\x18\x01 \x03(\x0b\x32:.report.ReportInstalledMicroAppResultRequest.InstalledApps\x1aT\n\rInstalledApps\x12.\n\x08microApp\x18\x01 \x01(\x0b\x32\x1c.micro_app.InstalledMicroApp\x12\x13\n\x0b\x63ontainerId\x18\x02 \x01(\t\"\xb9\x07\n%ReportInstalledMicroAppResultResponse\x12@\n\x04list\x18\x01 \x03(\x0b\x32\x32.report.ReportInstalledMicroAppResultResponse.List\x1a\xcd\x06\n\x04List\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x61ppId\x18\x03 \x01(\t\x12G\n\x05icons\x18\x04 \x01(\x0b\x32\x38.report.ReportInstalledMicroAppResultResponse.List.Icons\x12\x16\n\x0estoryboardJson\x18\x05 \x01(\t\x12\x0c\n\x04tags\x18\x06 \x03(\t\x12\x16\n\x0e\x63urrentVersion\x18\x07 \x01(\t\x12\x12\n\nappVersion\x18\x08 \x01(\t\x12\x15\n\rinstallStatus\x18\t \x01(\t\x12\x10\n\x08homepage\x18\n \x01(\t\x12\x10\n\x08internal\x18\x0b \x01(\t\x12\x0f\n\x07private\x18\x0c \x01(\t\x12Q\n\nclonedFrom\x18\r \x01(\x0b\x32=.report.ReportInstalledMicroAppResultResponse.List.ClonedFrom\x12\r\n\x05owner\x18\x0e \x01(\t\x12\x0e\n\x06readme\x18\x0f \x01(\t\x12\x0e\n\x06status\x18\x10 \x01(\t\x12\r\n\x05\x63time\x18\x11 \x01(\t\x12\r\n\x05mtime\x18\x12 \x01(\t\x12\x0f\n\x07pkgName\x18\x13 \x01(\t\x12\x16\n\x0eiconBackground\x18\x14 \x01(\t\x12M\n\x08menuIcon\x18\x15 \x01(\x0b\x32;.report.ReportInstalledMicroAppResultResponse.List.MenuIcon\x12.\n\rdefaultConfig\x18\x16 \x01(\x0b\x32\x17.google.protobuf.Struct\x12+\n\nuserConfig\x18\x17 \x01(\x0b\x32\x17.google.protobuf.Struct\x1a\x16\n\x05Icons\x12\r\n\x05large\x18\x01 \x01(\t\x1a:\n\nClonedFrom\x12\r\n\x05\x61ppId\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x1a\x64\n\x08MenuIcon\x12\x0b\n\x03lib\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\r\n\x05theme\x18\x03 \x01(\t\x12\x0c\n\x04icon\x18\x04 \x01(\t\x12\x0e\n\x06prefix\x18\x05 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x06 \x01(\t\"\x9d\x01\n,ReportInstalledMicroAppResultResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12;\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32-.report.ReportInstalledMicroAppResultResponseb\x06proto3')
  ,
  dependencies=[micro__app__sdk_dot_model_dot_micro__app_dot_installed__micro__app__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_REPORTINSTALLEDMICROAPPRESULTREQUEST_INSTALLEDAPPS = _descriptor.Descriptor(
  name='InstalledApps',
  full_name='report.ReportInstalledMicroAppResultRequest.InstalledApps',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='microApp', full_name='report.ReportInstalledMicroAppResultRequest.InstalledApps.microApp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='containerId', full_name='report.ReportInstalledMicroAppResultRequest.InstalledApps.containerId', index=1,
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
  serialized_start=262,
  serialized_end=346,
)

_REPORTINSTALLEDMICROAPPRESULTREQUEST = _descriptor.Descriptor(
  name='ReportInstalledMicroAppResultRequest',
  full_name='report.ReportInstalledMicroAppResultRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='installedApps', full_name='report.ReportInstalledMicroAppResultRequest.installedApps', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_REPORTINSTALLEDMICROAPPRESULTREQUEST_INSTALLEDAPPS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=346,
)


_REPORTINSTALLEDMICROAPPRESULTRESPONSE_LIST_ICONS = _descriptor.Descriptor(
  name='Icons',
  full_name='report.ReportInstalledMicroAppResultResponse.List.Icons',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='large', full_name='report.ReportInstalledMicroAppResultResponse.List.Icons.large', index=0,
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
  serialized_start=1118,
  serialized_end=1140,
)

_REPORTINSTALLEDMICROAPPRESULTRESPONSE_LIST_CLONEDFROM = _descriptor.Descriptor(
  name='ClonedFrom',
  full_name='report.ReportInstalledMicroAppResultResponse.List.ClonedFrom',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appId', full_name='report.ReportInstalledMicroAppResultResponse.List.ClonedFrom.appId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='report.ReportInstalledMicroAppResultResponse.List.ClonedFrom.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='report.ReportInstalledMicroAppResultResponse.List.ClonedFrom.name', index=2,
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
  serialized_start=1142,
  serialized_end=1200,
)

_REPORTINSTALLEDMICROAPPRESULTRESPONSE_LIST_MENUICON = _descriptor.Descriptor(
  name='MenuIcon',
  full_name='report.ReportInstalledMicroAppResultResponse.List.MenuIcon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lib', full_name='report.ReportInstalledMicroAppResultResponse.List.MenuIcon.lib', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='report.ReportInstalledMicroAppResultResponse.List.MenuIcon.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='theme', full_name='report.ReportInstalledMicroAppResultResponse.List.MenuIcon.theme', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon', full_name='report.ReportInstalledMicroAppResultResponse.List.MenuIcon.icon', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prefix', full_name='report.ReportInstalledMicroAppResultResponse.List.MenuIcon.prefix', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='report.ReportInstalledMicroAppResultResponse.List.MenuIcon.category', index=5,
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
  serialized_start=1202,
  serialized_end=1302,
)

_REPORTINSTALLEDMICROAPPRESULTRESPONSE_LIST = _descriptor.Descriptor(
  name='List',
  full_name='report.ReportInstalledMicroAppResultResponse.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='report.ReportInstalledMicroAppResultResponse.List.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='report.ReportInstalledMicroAppResultResponse.List.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='appId', full_name='report.ReportInstalledMicroAppResultResponse.List.appId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icons', full_name='report.ReportInstalledMicroAppResultResponse.List.icons', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='storyboardJson', full_name='report.ReportInstalledMicroAppResultResponse.List.storyboardJson', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='report.ReportInstalledMicroAppResultResponse.List.tags', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currentVersion', full_name='report.ReportInstalledMicroAppResultResponse.List.currentVersion', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='appVersion', full_name='report.ReportInstalledMicroAppResultResponse.List.appVersion', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='installStatus', full_name='report.ReportInstalledMicroAppResultResponse.List.installStatus', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='homepage', full_name='report.ReportInstalledMicroAppResultResponse.List.homepage', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='internal', full_name='report.ReportInstalledMicroAppResultResponse.List.internal', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='private', full_name='report.ReportInstalledMicroAppResultResponse.List.private', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clonedFrom', full_name='report.ReportInstalledMicroAppResultResponse.List.clonedFrom', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='owner', full_name='report.ReportInstalledMicroAppResultResponse.List.owner', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readme', full_name='report.ReportInstalledMicroAppResultResponse.List.readme', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='report.ReportInstalledMicroAppResultResponse.List.status', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='report.ReportInstalledMicroAppResultResponse.List.ctime', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='report.ReportInstalledMicroAppResultResponse.List.mtime', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pkgName', full_name='report.ReportInstalledMicroAppResultResponse.List.pkgName', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iconBackground', full_name='report.ReportInstalledMicroAppResultResponse.List.iconBackground', index=19,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='menuIcon', full_name='report.ReportInstalledMicroAppResultResponse.List.menuIcon', index=20,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='defaultConfig', full_name='report.ReportInstalledMicroAppResultResponse.List.defaultConfig', index=21,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userConfig', full_name='report.ReportInstalledMicroAppResultResponse.List.userConfig', index=22,
      number=23, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_REPORTINSTALLEDMICROAPPRESULTRESPONSE_LIST_ICONS, _REPORTINSTALLEDMICROAPPRESULTRESPONSE_LIST_CLONEDFROM, _REPORTINSTALLEDMICROAPPRESULTRESPONSE_LIST_MENUICON, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=457,
  serialized_end=1302,
)

_REPORTINSTALLEDMICROAPPRESULTRESPONSE = _descriptor.Descriptor(
  name='ReportInstalledMicroAppResultResponse',
  full_name='report.ReportInstalledMicroAppResultResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='list', full_name='report.ReportInstalledMicroAppResultResponse.list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_REPORTINSTALLEDMICROAPPRESULTRESPONSE_LIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=349,
  serialized_end=1302,
)


_REPORTINSTALLEDMICROAPPRESULTRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ReportInstalledMicroAppResultResponseWrapper',
  full_name='report.ReportInstalledMicroAppResultResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='report.ReportInstalledMicroAppResultResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='report.ReportInstalledMicroAppResultResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='report.ReportInstalledMicroAppResultResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='report.ReportInstalledMicroAppResultResponseWrapper.data', index=3,
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
  serialized_start=1305,
  serialized_end=1462,
)

_REPORTINSTALLEDMICROAPPRESULTREQUEST_INSTALLEDAPPS.fields_by_name['microApp'].message_type = micro__app__sdk_dot_model_dot_micro__app_dot_installed__micro__app__pb2._INSTALLEDMICROAPP
_REPORTINSTALLEDMICROAPPRESULTREQUEST_INSTALLEDAPPS.containing_type = _REPORTINSTALLEDMICROAPPRESULTREQUEST
_REPORTINSTALLEDMICROAPPRESULTREQUEST.fields_by_name['installedApps'].message_type = _REPORTINSTALLEDMICROAPPRESULTREQUEST_INSTALLEDAPPS
_REPORTINSTALLEDMICROAPPRESULTRESPONSE_LIST_ICONS.containing_type = _REPORTINSTALLEDMICROAPPRESULTRESPONSE_LIST
_REPORTINSTALLEDMICROAPPRESULTRESPONSE_LIST_CLONEDFROM.containing_type = _REPORTINSTALLEDMICROAPPRESULTRESPONSE_LIST
_REPORTINSTALLEDMICROAPPRESULTRESPONSE_LIST_MENUICON.containing_type = _REPORTINSTALLEDMICROAPPRESULTRESPONSE_LIST
_REPORTINSTALLEDMICROAPPRESULTRESPONSE_LIST.fields_by_name['icons'].message_type = _REPORTINSTALLEDMICROAPPRESULTRESPONSE_LIST_ICONS
_REPORTINSTALLEDMICROAPPRESULTRESPONSE_LIST.fields_by_name['clonedFrom'].message_type = _REPORTINSTALLEDMICROAPPRESULTRESPONSE_LIST_CLONEDFROM
_REPORTINSTALLEDMICROAPPRESULTRESPONSE_LIST.fields_by_name['menuIcon'].message_type = _REPORTINSTALLEDMICROAPPRESULTRESPONSE_LIST_MENUICON
_REPORTINSTALLEDMICROAPPRESULTRESPONSE_LIST.fields_by_name['defaultConfig'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_REPORTINSTALLEDMICROAPPRESULTRESPONSE_LIST.fields_by_name['userConfig'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_REPORTINSTALLEDMICROAPPRESULTRESPONSE_LIST.containing_type = _REPORTINSTALLEDMICROAPPRESULTRESPONSE
_REPORTINSTALLEDMICROAPPRESULTRESPONSE.fields_by_name['list'].message_type = _REPORTINSTALLEDMICROAPPRESULTRESPONSE_LIST
_REPORTINSTALLEDMICROAPPRESULTRESPONSEWRAPPER.fields_by_name['data'].message_type = _REPORTINSTALLEDMICROAPPRESULTRESPONSE
DESCRIPTOR.message_types_by_name['ReportInstalledMicroAppResultRequest'] = _REPORTINSTALLEDMICROAPPRESULTREQUEST
DESCRIPTOR.message_types_by_name['ReportInstalledMicroAppResultResponse'] = _REPORTINSTALLEDMICROAPPRESULTRESPONSE
DESCRIPTOR.message_types_by_name['ReportInstalledMicroAppResultResponseWrapper'] = _REPORTINSTALLEDMICROAPPRESULTRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReportInstalledMicroAppResultRequest = _reflection.GeneratedProtocolMessageType('ReportInstalledMicroAppResultRequest', (_message.Message,), {

  'InstalledApps' : _reflection.GeneratedProtocolMessageType('InstalledApps', (_message.Message,), {
    'DESCRIPTOR' : _REPORTINSTALLEDMICROAPPRESULTREQUEST_INSTALLEDAPPS,
    '__module__' : 'report_installed_micro_app_result_pb2'
    # @@protoc_insertion_point(class_scope:report.ReportInstalledMicroAppResultRequest.InstalledApps)
    })
  ,
  'DESCRIPTOR' : _REPORTINSTALLEDMICROAPPRESULTREQUEST,
  '__module__' : 'report_installed_micro_app_result_pb2'
  # @@protoc_insertion_point(class_scope:report.ReportInstalledMicroAppResultRequest)
  })
_sym_db.RegisterMessage(ReportInstalledMicroAppResultRequest)
_sym_db.RegisterMessage(ReportInstalledMicroAppResultRequest.InstalledApps)

ReportInstalledMicroAppResultResponse = _reflection.GeneratedProtocolMessageType('ReportInstalledMicroAppResultResponse', (_message.Message,), {

  'List' : _reflection.GeneratedProtocolMessageType('List', (_message.Message,), {

    'Icons' : _reflection.GeneratedProtocolMessageType('Icons', (_message.Message,), {
      'DESCRIPTOR' : _REPORTINSTALLEDMICROAPPRESULTRESPONSE_LIST_ICONS,
      '__module__' : 'report_installed_micro_app_result_pb2'
      # @@protoc_insertion_point(class_scope:report.ReportInstalledMicroAppResultResponse.List.Icons)
      })
    ,

    'ClonedFrom' : _reflection.GeneratedProtocolMessageType('ClonedFrom', (_message.Message,), {
      'DESCRIPTOR' : _REPORTINSTALLEDMICROAPPRESULTRESPONSE_LIST_CLONEDFROM,
      '__module__' : 'report_installed_micro_app_result_pb2'
      # @@protoc_insertion_point(class_scope:report.ReportInstalledMicroAppResultResponse.List.ClonedFrom)
      })
    ,

    'MenuIcon' : _reflection.GeneratedProtocolMessageType('MenuIcon', (_message.Message,), {
      'DESCRIPTOR' : _REPORTINSTALLEDMICROAPPRESULTRESPONSE_LIST_MENUICON,
      '__module__' : 'report_installed_micro_app_result_pb2'
      # @@protoc_insertion_point(class_scope:report.ReportInstalledMicroAppResultResponse.List.MenuIcon)
      })
    ,
    'DESCRIPTOR' : _REPORTINSTALLEDMICROAPPRESULTRESPONSE_LIST,
    '__module__' : 'report_installed_micro_app_result_pb2'
    # @@protoc_insertion_point(class_scope:report.ReportInstalledMicroAppResultResponse.List)
    })
  ,
  'DESCRIPTOR' : _REPORTINSTALLEDMICROAPPRESULTRESPONSE,
  '__module__' : 'report_installed_micro_app_result_pb2'
  # @@protoc_insertion_point(class_scope:report.ReportInstalledMicroAppResultResponse)
  })
_sym_db.RegisterMessage(ReportInstalledMicroAppResultResponse)
_sym_db.RegisterMessage(ReportInstalledMicroAppResultResponse.List)
_sym_db.RegisterMessage(ReportInstalledMicroAppResultResponse.List.Icons)
_sym_db.RegisterMessage(ReportInstalledMicroAppResultResponse.List.ClonedFrom)
_sym_db.RegisterMessage(ReportInstalledMicroAppResultResponse.List.MenuIcon)

ReportInstalledMicroAppResultResponseWrapper = _reflection.GeneratedProtocolMessageType('ReportInstalledMicroAppResultResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _REPORTINSTALLEDMICROAPPRESULTRESPONSEWRAPPER,
  '__module__' : 'report_installed_micro_app_result_pb2'
  # @@protoc_insertion_point(class_scope:report.ReportInstalledMicroAppResultResponseWrapper)
  })
_sym_db.RegisterMessage(ReportInstalledMicroAppResultResponseWrapper)


# @@protoc_insertion_point(module_scope)
