# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: package_info.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from capacity_admin_sdk.model.cmdb import cluster_info_pb2 as capacity__admin__sdk_dot_model_dot_cmdb_dot_cluster__info__pb2
from capacity_admin_sdk.model.easy_flow import version_info_pb2 as capacity__admin__sdk_dot_model_dot_easy__flow_dot_version__info__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='package_info.proto',
  package='easy_flow',
  syntax='proto3',
  serialized_options=_b('ZCgo.easyops.local/contracts/protorepo-models/easyops/model/easy_flow'),
  serialized_pb=_b('\n\x12package_info.proto\x12\teasy_flow\x1a\x30\x63\x61pacity_admin_sdk/model/cmdb/cluster_info.proto\x1a\x35\x63\x61pacity_admin_sdk/model/easy_flow/version_info.proto\"\xc2\x04\n\x0bPackageInfo\x12\x13\n\x0bpackageName\x18\x01 \x01(\t\x12\x13\n\x0bversionName\x18\x02 \x01(\t\x12\"\n\x07\x63luster\x18\x03 \x01(\x0b\x32\x11.cmdb.ClusterInfo\x12\x14\n\x0cpreVersionId\x18\x04 \x01(\t\x12\x16\n\x0epreVersionName\x18\x05 \x01(\t\x12\x19\n\x11preVersionEnvType\x18\x06 \x01(\x05\x12\x15\n\rtargetVersion\x18\x07 \x01(\t\x12\x0f\n\x07preStop\x18\x08 \x01(\x08\x12\x11\n\tpostStart\x18\t \x01(\x08\x12\x13\n\x0bpostRestart\x18\n \x01(\x08\x12\x11\n\tautoStart\x18\x0b \x01(\x08\x12\x11\n\tuserCheck\x18\x0c \x01(\x08\x12\x12\n\nfullUpdate\x18\r \x01(\x08\x12\x13\n\x0b\x66orceUpdate\x18\x0e \x01(\x08\x12\r\n\x05\x66orce\x18\x0f \x01(\x08\x12\x14\n\x0c\x66orceInstall\x18\x10 \x01(\x08\x12\x17\n\x0fsimulateInstall\x18\x11 \x01(\x08\x12+\n\x0bversionInfo\x18\x12 \x01(\x0b\x32\x16.easy_flow.VersionInfo\x12\x11\n\tspecialOp\x18\x13 \x01(\t\x12\x10\n\x08\x66ileOnly\x18\x14 \x01(\x08\x12\x12\n\nscriptOnly\x18\x15 \x01(\x08\x12\x11\n\tversionId\x18\x16 \x01(\t\x12\x11\n\tpackageId\x18\x17 \x01(\t\x12\x13\n\x0binstallPath\x18\x18 \x01(\t\x12\x0c\n\x04type\x18\x19 \x01(\x05\x12\x10\n\x08platform\x18\x1a \x01(\tBEZCgo.easyops.local/contracts/protorepo-models/easyops/model/easy_flowb\x06proto3')
  ,
  dependencies=[capacity__admin__sdk_dot_model_dot_cmdb_dot_cluster__info__pb2.DESCRIPTOR,capacity__admin__sdk_dot_model_dot_easy__flow_dot_version__info__pb2.DESCRIPTOR,])




_PACKAGEINFO = _descriptor.Descriptor(
  name='PackageInfo',
  full_name='easy_flow.PackageInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='packageName', full_name='easy_flow.PackageInfo.packageName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionName', full_name='easy_flow.PackageInfo.versionName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cluster', full_name='easy_flow.PackageInfo.cluster', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preVersionId', full_name='easy_flow.PackageInfo.preVersionId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preVersionName', full_name='easy_flow.PackageInfo.preVersionName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preVersionEnvType', full_name='easy_flow.PackageInfo.preVersionEnvType', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targetVersion', full_name='easy_flow.PackageInfo.targetVersion', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preStop', full_name='easy_flow.PackageInfo.preStop', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='postStart', full_name='easy_flow.PackageInfo.postStart', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='postRestart', full_name='easy_flow.PackageInfo.postRestart', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='autoStart', full_name='easy_flow.PackageInfo.autoStart', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userCheck', full_name='easy_flow.PackageInfo.userCheck', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fullUpdate', full_name='easy_flow.PackageInfo.fullUpdate', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='forceUpdate', full_name='easy_flow.PackageInfo.forceUpdate', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='force', full_name='easy_flow.PackageInfo.force', index=14,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='forceInstall', full_name='easy_flow.PackageInfo.forceInstall', index=15,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='simulateInstall', full_name='easy_flow.PackageInfo.simulateInstall', index=16,
      number=17, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionInfo', full_name='easy_flow.PackageInfo.versionInfo', index=17,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='specialOp', full_name='easy_flow.PackageInfo.specialOp', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fileOnly', full_name='easy_flow.PackageInfo.fileOnly', index=19,
      number=20, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scriptOnly', full_name='easy_flow.PackageInfo.scriptOnly', index=20,
      number=21, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionId', full_name='easy_flow.PackageInfo.versionId', index=21,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageId', full_name='easy_flow.PackageInfo.packageId', index=22,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='installPath', full_name='easy_flow.PackageInfo.installPath', index=23,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='easy_flow.PackageInfo.type', index=24,
      number=25, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='platform', full_name='easy_flow.PackageInfo.platform', index=25,
      number=26, type=9, cpp_type=9, label=1,
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
  serialized_start=139,
  serialized_end=717,
)

_PACKAGEINFO.fields_by_name['cluster'].message_type = capacity__admin__sdk_dot_model_dot_cmdb_dot_cluster__info__pb2._CLUSTERINFO
_PACKAGEINFO.fields_by_name['versionInfo'].message_type = capacity__admin__sdk_dot_model_dot_easy__flow_dot_version__info__pb2._VERSIONINFO
DESCRIPTOR.message_types_by_name['PackageInfo'] = _PACKAGEINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PackageInfo = _reflection.GeneratedProtocolMessageType('PackageInfo', (_message.Message,), {
  'DESCRIPTOR' : _PACKAGEINFO,
  '__module__' : 'package_info_pb2'
  # @@protoc_insertion_point(class_scope:easy_flow.PackageInfo)
  })
_sym_db.RegisterMessage(PackageInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
