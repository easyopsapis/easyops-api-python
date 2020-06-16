# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: target_info.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from object_store_sdk.model.cmdb import cluster_info_pb2 as object__store__sdk_dot_model_dot_cmdb_dot_cluster__info__pb2
from object_store_sdk.model.easy_flow import version_info_pb2 as object__store__sdk_dot_model_dot_easy__flow_dot_version__info__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='target_info.proto',
  package='easy_flow',
  syntax='proto3',
  serialized_options=_b('ZCgo.easyops.local/contracts/protorepo-models/easyops/model/easy_flow'),
  serialized_pb=_b('\n\x11target_info.proto\x12\teasy_flow\x1a.object_store_sdk/model/cmdb/cluster_info.proto\x1a\x33object_store_sdk/model/easy_flow/version_info.proto\"\x9b\x04\n\nTargetInfo\x12\x10\n\x08targetId\x18\x01 \x01(\t\x12\x12\n\ntargetName\x18\x02 \x01(\t\x12\x12\n\ninstanceId\x18\x03 \x01(\t\x12\"\n\x07\x63luster\x18\x04 \x01(\x0b\x32\x11.cmdb.ClusterInfo\x12\x38\n\x0cinstanceInfo\x18\x05 \x03(\x0b\x32\".easy_flow.TargetInfo.InstanceInfo\x12:\n\roperationInfo\x18\x06 \x03(\x0b\x32#.easy_flow.TargetInfo.OperationInfo\x1a\x8b\x01\n\x0cInstanceInfo\x12\x13\n\x0bversionName\x18\x01 \x01(\t\x12+\n\x0bversionInfo\x18\x02 \x01(\x0b\x32\x16.easy_flow.VersionInfo\x12\x11\n\tpackageId\x18\x03 \x01(\t\x12\x13\n\x0binstallPath\x18\x04 \x01(\t\x12\x11\n\tversionId\x18\x05 \x01(\t\x1a\xaa\x01\n\rOperationInfo\x12\x11\n\toperation\x18\x01 \x01(\t\x12-\n\rversionToInfo\x18\x02 \x01(\x0b\x32\x16.easy_flow.VersionInfo\x12/\n\x0fversionFromInfo\x18\x03 \x01(\x0b\x32\x16.easy_flow.VersionInfo\x12\x13\n\x0binstallPath\x18\x04 \x01(\t\x12\x11\n\tpackageId\x18\x05 \x01(\tBEZCgo.easyops.local/contracts/protorepo-models/easyops/model/easy_flowb\x06proto3')
  ,
  dependencies=[object__store__sdk_dot_model_dot_cmdb_dot_cluster__info__pb2.DESCRIPTOR,object__store__sdk_dot_model_dot_easy__flow_dot_version__info__pb2.DESCRIPTOR,])




_TARGETINFO_INSTANCEINFO = _descriptor.Descriptor(
  name='InstanceInfo',
  full_name='easy_flow.TargetInfo.InstanceInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='versionName', full_name='easy_flow.TargetInfo.InstanceInfo.versionName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionInfo', full_name='easy_flow.TargetInfo.InstanceInfo.versionInfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageId', full_name='easy_flow.TargetInfo.InstanceInfo.packageId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='installPath', full_name='easy_flow.TargetInfo.InstanceInfo.installPath', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionId', full_name='easy_flow.TargetInfo.InstanceInfo.versionId', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=361,
  serialized_end=500,
)

_TARGETINFO_OPERATIONINFO = _descriptor.Descriptor(
  name='OperationInfo',
  full_name='easy_flow.TargetInfo.OperationInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation', full_name='easy_flow.TargetInfo.OperationInfo.operation', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionToInfo', full_name='easy_flow.TargetInfo.OperationInfo.versionToInfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionFromInfo', full_name='easy_flow.TargetInfo.OperationInfo.versionFromInfo', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='installPath', full_name='easy_flow.TargetInfo.OperationInfo.installPath', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageId', full_name='easy_flow.TargetInfo.OperationInfo.packageId', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=503,
  serialized_end=673,
)

_TARGETINFO = _descriptor.Descriptor(
  name='TargetInfo',
  full_name='easy_flow.TargetInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='targetId', full_name='easy_flow.TargetInfo.targetId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targetName', full_name='easy_flow.TargetInfo.targetName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='easy_flow.TargetInfo.instanceId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cluster', full_name='easy_flow.TargetInfo.cluster', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceInfo', full_name='easy_flow.TargetInfo.instanceInfo', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operationInfo', full_name='easy_flow.TargetInfo.operationInfo', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TARGETINFO_INSTANCEINFO, _TARGETINFO_OPERATIONINFO, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=134,
  serialized_end=673,
)

_TARGETINFO_INSTANCEINFO.fields_by_name['versionInfo'].message_type = object__store__sdk_dot_model_dot_easy__flow_dot_version__info__pb2._VERSIONINFO
_TARGETINFO_INSTANCEINFO.containing_type = _TARGETINFO
_TARGETINFO_OPERATIONINFO.fields_by_name['versionToInfo'].message_type = object__store__sdk_dot_model_dot_easy__flow_dot_version__info__pb2._VERSIONINFO
_TARGETINFO_OPERATIONINFO.fields_by_name['versionFromInfo'].message_type = object__store__sdk_dot_model_dot_easy__flow_dot_version__info__pb2._VERSIONINFO
_TARGETINFO_OPERATIONINFO.containing_type = _TARGETINFO
_TARGETINFO.fields_by_name['cluster'].message_type = object__store__sdk_dot_model_dot_cmdb_dot_cluster__info__pb2._CLUSTERINFO
_TARGETINFO.fields_by_name['instanceInfo'].message_type = _TARGETINFO_INSTANCEINFO
_TARGETINFO.fields_by_name['operationInfo'].message_type = _TARGETINFO_OPERATIONINFO
DESCRIPTOR.message_types_by_name['TargetInfo'] = _TARGETINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TargetInfo = _reflection.GeneratedProtocolMessageType('TargetInfo', (_message.Message,), {

  'InstanceInfo' : _reflection.GeneratedProtocolMessageType('InstanceInfo', (_message.Message,), {
    'DESCRIPTOR' : _TARGETINFO_INSTANCEINFO,
    '__module__' : 'target_info_pb2'
    # @@protoc_insertion_point(class_scope:easy_flow.TargetInfo.InstanceInfo)
    })
  ,

  'OperationInfo' : _reflection.GeneratedProtocolMessageType('OperationInfo', (_message.Message,), {
    'DESCRIPTOR' : _TARGETINFO_OPERATIONINFO,
    '__module__' : 'target_info_pb2'
    # @@protoc_insertion_point(class_scope:easy_flow.TargetInfo.OperationInfo)
    })
  ,
  'DESCRIPTOR' : _TARGETINFO,
  '__module__' : 'target_info_pb2'
  # @@protoc_insertion_point(class_scope:easy_flow.TargetInfo)
  })
_sym_db.RegisterMessage(TargetInfo)
_sym_db.RegisterMessage(TargetInfo.InstanceInfo)
_sym_db.RegisterMessage(TargetInfo.OperationInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
