# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: task.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cmdb_sdk.model.easy_flow import target_info_pb2 as cmdb__sdk_dot_model_dot_easy__flow_dot_target__info__pb2
from cmdb_sdk.model.easy_flow import package_info_pb2 as cmdb__sdk_dot_model_dot_easy__flow_dot_package__info__pb2
from cmdb_sdk.model.easy_flow import deploy_target_pb2 as cmdb__sdk_dot_model_dot_easy__flow_dot_deploy__target__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='task.proto',
  package='easy_flow',
  syntax='proto3',
  serialized_options=_b('ZCgo.easyops.local/contracts/protorepo-models/easyops/model/easy_flow'),
  serialized_pb=_b('\n\ntask.proto\x12\teasy_flow\x1a*cmdb_sdk/model/easy_flow/target_info.proto\x1a+cmdb_sdk/model/easy_flow/package_info.proto\x1a,cmdb_sdk/model/easy_flow/deploy_target.proto\x1a\x1cgoogle/protobuf/struct.proto\"\x9f\x08\n\x04Task\x12\r\n\x05\x61ppId\x18\x01 \x01(\t\x12\x0f\n\x07\x61ppName\x18\x02 \x01(\t\x12\x11\n\tclusterId\x18\x03 \x01(\t\x12\x13\n\x0b\x63lusterType\x18\x04 \x01(\t\x12\x10\n\x08operator\x18\x05 \x01(\t\x12\x0b\n\x03org\x18\x06 \x01(\x05\x12)\n\ntargetList\x18\x07 \x03(\x0b\x32\x15.easy_flow.TargetInfo\x12+\n\x0bpackageList\x18\x08 \x03(\x0b\x32\x16.easy_flow.PackageInfo\x12.\n\nconfigList\x18\t \x03(\x0b\x32\x1a.easy_flow.Task.ConfigList\x12\x15\n\rtaskTimeStamp\x18\n \x01(\t\x12\x15\n\rconfigVersion\x18\x0b \x01(\t\x12\x17\n\x0f\x63onfigPackageId\x18\x0c \x01(\t\x12\'\n\x06labels\x18\r \x01(\x0b\x32\x17.google.protobuf.Struct\x12.\n\nconfigDiff\x18\x0e \x03(\x0b\x32\x1a.easy_flow.Task.ConfigDiff\x12\x12\n\nneedNotify\x18\x0f \x01(\x08\x12\x10\n\x08\x62\x61tchNum\x18\x10 \x01(\x05\x12\x15\n\rbatchInterval\x18\x11 \x01(\x05\x12(\n\x07\x62\x61tches\x18\x12 \x03(\x0b\x32\x17.easy_flow.Task.Batches\x12\x12\n\nfailedStop\x18\x13 \x01(\x08\x1a\xe2\x01\n\nConfigList\x12\r\n\x05hosts\x18\x01 \x03(\t\x12\x33\n\x07\x63onfigs\x18\x02 \x03(\x0b\x32\".easy_flow.Task.ConfigList.Configs\x1a\x8f\x01\n\x07\x43onfigs\x12\x11\n\tpackageId\x18\x01 \x01(\t\x12\x37\n\x05items\x18\x02 \x03(\x0b\x32(.easy_flow.Task.ConfigList.Configs.Items\x12\x13\n\x0binstallPath\x18\x03 \x01(\t\x1a#\n\x05Items\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\x1a\xf2\x01\n\nConfigDiff\x12\r\n\x05hosts\x18\x01 \x03(\t\x12\x31\n\x06\x64\x65tail\x18\x02 \x03(\x0b\x32!.easy_flow.Task.ConfigDiff.Detail\x1a\xa1\x01\n\x06\x44\x65tail\x12\x36\n\x05items\x18\x01 \x03(\x0b\x32\'.easy_flow.Task.ConfigDiff.Detail.Items\x12\x11\n\tpackageId\x18\x02 \x01(\t\x12\x13\n\x0binstallPath\x18\x03 \x01(\t\x1a\x37\n\x05Items\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0f\n\x07newName\x18\x02 \x01(\t\x12\x0f\n\x07oldName\x18\x03 \x01(\t\x1a\x33\n\x07\x42\x61tches\x12(\n\x07targets\x18\x01 \x03(\x0b\x32\x17.easy_flow.DeployTargetBEZCgo.easyops.local/contracts/protorepo-models/easyops/model/easy_flowb\x06proto3')
  ,
  dependencies=[cmdb__sdk_dot_model_dot_easy__flow_dot_target__info__pb2.DESCRIPTOR,cmdb__sdk_dot_model_dot_easy__flow_dot_package__info__pb2.DESCRIPTOR,cmdb__sdk_dot_model_dot_easy__flow_dot_deploy__target__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_TASK_CONFIGLIST_CONFIGS_ITEMS = _descriptor.Descriptor(
  name='Items',
  full_name='easy_flow.Task.ConfigList.Configs.Items',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='easy_flow.Task.ConfigList.Configs.Items.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='easy_flow.Task.ConfigList.Configs.Items.path', index=1,
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
  serialized_start=913,
  serialized_end=948,
)

_TASK_CONFIGLIST_CONFIGS = _descriptor.Descriptor(
  name='Configs',
  full_name='easy_flow.Task.ConfigList.Configs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='packageId', full_name='easy_flow.Task.ConfigList.Configs.packageId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='items', full_name='easy_flow.Task.ConfigList.Configs.items', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='installPath', full_name='easy_flow.Task.ConfigList.Configs.installPath', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TASK_CONFIGLIST_CONFIGS_ITEMS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=805,
  serialized_end=948,
)

_TASK_CONFIGLIST = _descriptor.Descriptor(
  name='ConfigList',
  full_name='easy_flow.Task.ConfigList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hosts', full_name='easy_flow.Task.ConfigList.hosts', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='configs', full_name='easy_flow.Task.ConfigList.configs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TASK_CONFIGLIST_CONFIGS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=722,
  serialized_end=948,
)

_TASK_CONFIGDIFF_DETAIL_ITEMS = _descriptor.Descriptor(
  name='Items',
  full_name='easy_flow.Task.ConfigDiff.Detail.Items',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='easy_flow.Task.ConfigDiff.Detail.Items.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='newName', full_name='easy_flow.Task.ConfigDiff.Detail.Items.newName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='oldName', full_name='easy_flow.Task.ConfigDiff.Detail.Items.oldName', index=2,
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
  serialized_start=1138,
  serialized_end=1193,
)

_TASK_CONFIGDIFF_DETAIL = _descriptor.Descriptor(
  name='Detail',
  full_name='easy_flow.Task.ConfigDiff.Detail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='easy_flow.Task.ConfigDiff.Detail.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageId', full_name='easy_flow.Task.ConfigDiff.Detail.packageId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='installPath', full_name='easy_flow.Task.ConfigDiff.Detail.installPath', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TASK_CONFIGDIFF_DETAIL_ITEMS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1032,
  serialized_end=1193,
)

_TASK_CONFIGDIFF = _descriptor.Descriptor(
  name='ConfigDiff',
  full_name='easy_flow.Task.ConfigDiff',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hosts', full_name='easy_flow.Task.ConfigDiff.hosts', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='detail', full_name='easy_flow.Task.ConfigDiff.detail', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TASK_CONFIGDIFF_DETAIL, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=951,
  serialized_end=1193,
)

_TASK_BATCHES = _descriptor.Descriptor(
  name='Batches',
  full_name='easy_flow.Task.Batches',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='targets', full_name='easy_flow.Task.Batches.targets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1195,
  serialized_end=1246,
)

_TASK = _descriptor.Descriptor(
  name='Task',
  full_name='easy_flow.Task',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appId', full_name='easy_flow.Task.appId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='appName', full_name='easy_flow.Task.appName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clusterId', full_name='easy_flow.Task.clusterId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clusterType', full_name='easy_flow.Task.clusterType', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operator', full_name='easy_flow.Task.operator', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org', full_name='easy_flow.Task.org', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targetList', full_name='easy_flow.Task.targetList', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageList', full_name='easy_flow.Task.packageList', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='configList', full_name='easy_flow.Task.configList', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='taskTimeStamp', full_name='easy_flow.Task.taskTimeStamp', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='configVersion', full_name='easy_flow.Task.configVersion', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='configPackageId', full_name='easy_flow.Task.configPackageId', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='easy_flow.Task.labels', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='configDiff', full_name='easy_flow.Task.configDiff', index=13,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='needNotify', full_name='easy_flow.Task.needNotify', index=14,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batchNum', full_name='easy_flow.Task.batchNum', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batchInterval', full_name='easy_flow.Task.batchInterval', index=16,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batches', full_name='easy_flow.Task.batches', index=17,
      number=18, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='failedStop', full_name='easy_flow.Task.failedStop', index=18,
      number=19, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TASK_CONFIGLIST, _TASK_CONFIGDIFF, _TASK_BATCHES, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=191,
  serialized_end=1246,
)

_TASK_CONFIGLIST_CONFIGS_ITEMS.containing_type = _TASK_CONFIGLIST_CONFIGS
_TASK_CONFIGLIST_CONFIGS.fields_by_name['items'].message_type = _TASK_CONFIGLIST_CONFIGS_ITEMS
_TASK_CONFIGLIST_CONFIGS.containing_type = _TASK_CONFIGLIST
_TASK_CONFIGLIST.fields_by_name['configs'].message_type = _TASK_CONFIGLIST_CONFIGS
_TASK_CONFIGLIST.containing_type = _TASK
_TASK_CONFIGDIFF_DETAIL_ITEMS.containing_type = _TASK_CONFIGDIFF_DETAIL
_TASK_CONFIGDIFF_DETAIL.fields_by_name['items'].message_type = _TASK_CONFIGDIFF_DETAIL_ITEMS
_TASK_CONFIGDIFF_DETAIL.containing_type = _TASK_CONFIGDIFF
_TASK_CONFIGDIFF.fields_by_name['detail'].message_type = _TASK_CONFIGDIFF_DETAIL
_TASK_CONFIGDIFF.containing_type = _TASK
_TASK_BATCHES.fields_by_name['targets'].message_type = cmdb__sdk_dot_model_dot_easy__flow_dot_deploy__target__pb2._DEPLOYTARGET
_TASK_BATCHES.containing_type = _TASK
_TASK.fields_by_name['targetList'].message_type = cmdb__sdk_dot_model_dot_easy__flow_dot_target__info__pb2._TARGETINFO
_TASK.fields_by_name['packageList'].message_type = cmdb__sdk_dot_model_dot_easy__flow_dot_package__info__pb2._PACKAGEINFO
_TASK.fields_by_name['configList'].message_type = _TASK_CONFIGLIST
_TASK.fields_by_name['labels'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_TASK.fields_by_name['configDiff'].message_type = _TASK_CONFIGDIFF
_TASK.fields_by_name['batches'].message_type = _TASK_BATCHES
DESCRIPTOR.message_types_by_name['Task'] = _TASK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Task = _reflection.GeneratedProtocolMessageType('Task', (_message.Message,), {

  'ConfigList' : _reflection.GeneratedProtocolMessageType('ConfigList', (_message.Message,), {

    'Configs' : _reflection.GeneratedProtocolMessageType('Configs', (_message.Message,), {

      'Items' : _reflection.GeneratedProtocolMessageType('Items', (_message.Message,), {
        'DESCRIPTOR' : _TASK_CONFIGLIST_CONFIGS_ITEMS,
        '__module__' : 'task_pb2'
        # @@protoc_insertion_point(class_scope:easy_flow.Task.ConfigList.Configs.Items)
        })
      ,
      'DESCRIPTOR' : _TASK_CONFIGLIST_CONFIGS,
      '__module__' : 'task_pb2'
      # @@protoc_insertion_point(class_scope:easy_flow.Task.ConfigList.Configs)
      })
    ,
    'DESCRIPTOR' : _TASK_CONFIGLIST,
    '__module__' : 'task_pb2'
    # @@protoc_insertion_point(class_scope:easy_flow.Task.ConfigList)
    })
  ,

  'ConfigDiff' : _reflection.GeneratedProtocolMessageType('ConfigDiff', (_message.Message,), {

    'Detail' : _reflection.GeneratedProtocolMessageType('Detail', (_message.Message,), {

      'Items' : _reflection.GeneratedProtocolMessageType('Items', (_message.Message,), {
        'DESCRIPTOR' : _TASK_CONFIGDIFF_DETAIL_ITEMS,
        '__module__' : 'task_pb2'
        # @@protoc_insertion_point(class_scope:easy_flow.Task.ConfigDiff.Detail.Items)
        })
      ,
      'DESCRIPTOR' : _TASK_CONFIGDIFF_DETAIL,
      '__module__' : 'task_pb2'
      # @@protoc_insertion_point(class_scope:easy_flow.Task.ConfigDiff.Detail)
      })
    ,
    'DESCRIPTOR' : _TASK_CONFIGDIFF,
    '__module__' : 'task_pb2'
    # @@protoc_insertion_point(class_scope:easy_flow.Task.ConfigDiff)
    })
  ,

  'Batches' : _reflection.GeneratedProtocolMessageType('Batches', (_message.Message,), {
    'DESCRIPTOR' : _TASK_BATCHES,
    '__module__' : 'task_pb2'
    # @@protoc_insertion_point(class_scope:easy_flow.Task.Batches)
    })
  ,
  'DESCRIPTOR' : _TASK,
  '__module__' : 'task_pb2'
  # @@protoc_insertion_point(class_scope:easy_flow.Task)
  })
_sym_db.RegisterMessage(Task)
_sym_db.RegisterMessage(Task.ConfigList)
_sym_db.RegisterMessage(Task.ConfigList.Configs)
_sym_db.RegisterMessage(Task.ConfigList.Configs.Items)
_sym_db.RegisterMessage(Task.ConfigDiff)
_sym_db.RegisterMessage(Task.ConfigDiff.Detail)
_sym_db.RegisterMessage(Task.ConfigDiff.Detail.Items)
_sym_db.RegisterMessage(Task.Batches)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
