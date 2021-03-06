# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: target_result.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from topboard_sdk.model.cmdb import cluster_info_pb2 as topboard__sdk_dot_model_dot_cmdb_dot_cluster__info__pb2
from topboard_sdk.model.easy_flow import deploy_package_result_pb2 as topboard__sdk_dot_model_dot_easy__flow_dot_deploy__package__result__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='target_result.proto',
  package='easy_flow',
  syntax='proto3',
  serialized_options=_b('ZCgo.easyops.local/contracts/protorepo-models/easyops/model/easy_flow'),
  serialized_pb=_b('\n\x13target_result.proto\x12\teasy_flow\x1a*topboard_sdk/model/cmdb/cluster_info.proto\x1a\x38topboard_sdk/model/easy_flow/deploy_package_result.proto\"\xba\x01\n\x0cTargetResult\x12\x10\n\x08targetId\x18\x01 \x01(\t\x12\x12\n\ntargetName\x18\x02 \x01(\t\x12\"\n\x07\x63luster\x18\x03 \x01(\x0b\x32\x11.cmdb.ClusterInfo\x12\x0c\n\x04\x63ode\x18\x04 \x01(\x05\x12\x0b\n\x03msg\x18\x05 \x01(\t\x12\x0e\n\x06status\x18\x06 \x01(\t\x12\x35\n\rpackageStatus\x18\x07 \x03(\x0b\x32\x1e.easy_flow.DeployPackageResultBEZCgo.easyops.local/contracts/protorepo-models/easyops/model/easy_flowb\x06proto3')
  ,
  dependencies=[topboard__sdk_dot_model_dot_cmdb_dot_cluster__info__pb2.DESCRIPTOR,topboard__sdk_dot_model_dot_easy__flow_dot_deploy__package__result__pb2.DESCRIPTOR,])




_TARGETRESULT = _descriptor.Descriptor(
  name='TargetResult',
  full_name='easy_flow.TargetResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='targetId', full_name='easy_flow.TargetResult.targetId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targetName', full_name='easy_flow.TargetResult.targetName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cluster', full_name='easy_flow.TargetResult.cluster', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='easy_flow.TargetResult.code', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='easy_flow.TargetResult.msg', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='easy_flow.TargetResult.status', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageStatus', full_name='easy_flow.TargetResult.packageStatus', index=6,
      number=7, type=11, cpp_type=10, label=3,
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
  serialized_start=137,
  serialized_end=323,
)

_TARGETRESULT.fields_by_name['cluster'].message_type = topboard__sdk_dot_model_dot_cmdb_dot_cluster__info__pb2._CLUSTERINFO
_TARGETRESULT.fields_by_name['packageStatus'].message_type = topboard__sdk_dot_model_dot_easy__flow_dot_deploy__package__result__pb2._DEPLOYPACKAGERESULT
DESCRIPTOR.message_types_by_name['TargetResult'] = _TARGETRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TargetResult = _reflection.GeneratedProtocolMessageType('TargetResult', (_message.Message,), {
  'DESCRIPTOR' : _TARGETRESULT,
  '__module__' : 'target_result_pb2'
  # @@protoc_insertion_point(class_scope:easy_flow.TargetResult)
  })
_sym_db.RegisterMessage(TargetResult)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
