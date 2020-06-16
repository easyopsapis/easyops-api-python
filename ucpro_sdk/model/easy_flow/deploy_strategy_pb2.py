# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: deploy_strategy.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ucpro_sdk.model.easy_flow import deploy_target_pb2 as ucpro__sdk_dot_model_dot_easy__flow_dot_deploy__target__pb2
from ucpro_sdk.model.cmdb import cluster_info_pb2 as ucpro__sdk_dot_model_dot_cmdb_dot_cluster__info__pb2
from ucpro_sdk.model.easy_flow import target_info_pb2 as ucpro__sdk_dot_model_dot_easy__flow_dot_target__info__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='deploy_strategy.proto',
  package='easy_flow',
  syntax='proto3',
  serialized_options=_b('ZCgo.easyops.local/contracts/protorepo-models/easyops/model/easy_flow'),
  serialized_pb=_b('\n\x15\x64\x65ploy_strategy.proto\x12\teasy_flow\x1a-ucpro_sdk/model/easy_flow/deploy_target.proto\x1a\'ucpro_sdk/model/cmdb/cluster_info.proto\x1a+ucpro_sdk/model/easy_flow/target_info.proto\"\xd6\t\n\x0e\x44\x65ployStrategy\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\napiVersion\x18\x03 \x01(\t\x12\x0b\n\x03org\x18\x04 \x01(\x05\x12*\n\x03\x61pp\x18\x05 \x01(\x0b\x32\x1d.easy_flow.DeployStrategy.App\x12\x0c\n\x04type\x18\x06 \x01(\t\x12>\n\rbatchStrategy\x18\x07 \x01(\x0b\x32\'.easy_flow.DeployStrategy.BatchStrategy\x12\r\n\x05scope\x18\x08 \x01(\t\x12#\n\x08\x63lusters\x18\t \x03(\x0b\x32\x11.cmdb.ClusterInfo\x12)\n\ntargetList\x18\n \x03(\x0b\x32\x15.easy_flow.TargetInfo\x12\x1a\n\x12\x63lusterEnvironment\x18\x0b \x01(\t\x12\x13\n\x0b\x63lusterType\x18\x0c \x01(\t\x12:\n\x0bpackageList\x18\r \x03(\x0b\x32%.easy_flow.DeployStrategy.PackageList\x12\x30\n\x06status\x18\x0e \x01(\x0b\x32 .easy_flow.DeployStrategy.Status\x1a\"\n\x03\x41pp\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x61ppId\x18\x02 \x01(\t\x1a\xc7\x03\n\rBatchStrategy\x12\x44\n\tautoBatch\x18\x01 \x01(\x0b\x32\x31.easy_flow.DeployStrategy.BatchStrategy.AutoBatch\x12H\n\x0bmanualBatch\x18\x02 \x01(\x0b\x32\x33.easy_flow.DeployStrategy.BatchStrategy.ManualBatch\x12\x0c\n\x04type\x18\x03 \x01(\t\x1aH\n\tAutoBatch\x12\x10\n\x08\x62\x61tchNum\x18\x01 \x01(\x05\x12\x15\n\rbatchInterval\x18\x02 \x01(\x05\x12\x12\n\nfailedStop\x18\x03 \x01(\x08\x1a\xcd\x01\n\x0bManualBatch\x12L\n\x07\x62\x61tches\x18\x01 \x03(\x0b\x32;.easy_flow.DeployStrategy.BatchStrategy.ManualBatch.Batches\x12\x10\n\x08\x62\x61tchNum\x18\x02 \x01(\x05\x12\x15\n\rbatchInterval\x18\x03 \x01(\x05\x12\x12\n\nfailedStop\x18\x04 \x01(\x08\x1a\x33\n\x07\x42\x61tches\x12(\n\x07targets\x18\x01 \x03(\x0b\x32\x17.easy_flow.DeployTarget\x1a\x85\x02\n\x0bPackageList\x12\x13\n\x0bpackageName\x18\x01 \x01(\t\x12\"\n\x07\x63luster\x18\x02 \x01(\x0b\x32\x11.cmdb.ClusterInfo\x12\x15\n\rtargetVersion\x18\x03 \x01(\t\x12\x0f\n\x07preStop\x18\x04 \x01(\x08\x12\x13\n\x0bpostRestart\x18\x05 \x01(\x08\x12\x11\n\tautoStart\x18\x06 \x01(\x08\x12\x11\n\tuserCheck\x18\x07 \x01(\x08\x12\x12\n\nfullUpdate\x18\x08 \x01(\x08\x12\x11\n\tpackageId\x18\t \x01(\t\x12\x13\n\x0binstallPath\x18\n \x01(\t\x12\x0c\n\x04type\x18\x0b \x01(\x05\x12\x10\n\x08platform\x18\x0c \x01(\t\x1a\x1b\n\x06Status\x12\x11\n\toutOfDate\x18\x01 \x01(\x08\x42\x45ZCgo.easyops.local/contracts/protorepo-models/easyops/model/easy_flowb\x06proto3')
  ,
  dependencies=[ucpro__sdk_dot_model_dot_easy__flow_dot_deploy__target__pb2.DESCRIPTOR,ucpro__sdk_dot_model_dot_cmdb_dot_cluster__info__pb2.DESCRIPTOR,ucpro__sdk_dot_model_dot_easy__flow_dot_target__info__pb2.DESCRIPTOR,])




_DEPLOYSTRATEGY_APP = _descriptor.Descriptor(
  name='App',
  full_name='easy_flow.DeployStrategy.App',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='easy_flow.DeployStrategy.App.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='appId', full_name='easy_flow.DeployStrategy.App.appId', index=1,
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
  serialized_start=623,
  serialized_end=657,
)

_DEPLOYSTRATEGY_BATCHSTRATEGY_AUTOBATCH = _descriptor.Descriptor(
  name='AutoBatch',
  full_name='easy_flow.DeployStrategy.BatchStrategy.AutoBatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='batchNum', full_name='easy_flow.DeployStrategy.BatchStrategy.AutoBatch.batchNum', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batchInterval', full_name='easy_flow.DeployStrategy.BatchStrategy.AutoBatch.batchInterval', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='failedStop', full_name='easy_flow.DeployStrategy.BatchStrategy.AutoBatch.failedStop', index=2,
      number=3, type=8, cpp_type=7, label=1,
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
  serialized_start=835,
  serialized_end=907,
)

_DEPLOYSTRATEGY_BATCHSTRATEGY_MANUALBATCH_BATCHES = _descriptor.Descriptor(
  name='Batches',
  full_name='easy_flow.DeployStrategy.BatchStrategy.ManualBatch.Batches',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='targets', full_name='easy_flow.DeployStrategy.BatchStrategy.ManualBatch.Batches.targets', index=0,
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
  serialized_start=1064,
  serialized_end=1115,
)

_DEPLOYSTRATEGY_BATCHSTRATEGY_MANUALBATCH = _descriptor.Descriptor(
  name='ManualBatch',
  full_name='easy_flow.DeployStrategy.BatchStrategy.ManualBatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='batches', full_name='easy_flow.DeployStrategy.BatchStrategy.ManualBatch.batches', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batchNum', full_name='easy_flow.DeployStrategy.BatchStrategy.ManualBatch.batchNum', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batchInterval', full_name='easy_flow.DeployStrategy.BatchStrategy.ManualBatch.batchInterval', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='failedStop', full_name='easy_flow.DeployStrategy.BatchStrategy.ManualBatch.failedStop', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DEPLOYSTRATEGY_BATCHSTRATEGY_MANUALBATCH_BATCHES, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=910,
  serialized_end=1115,
)

_DEPLOYSTRATEGY_BATCHSTRATEGY = _descriptor.Descriptor(
  name='BatchStrategy',
  full_name='easy_flow.DeployStrategy.BatchStrategy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='autoBatch', full_name='easy_flow.DeployStrategy.BatchStrategy.autoBatch', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='manualBatch', full_name='easy_flow.DeployStrategy.BatchStrategy.manualBatch', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='easy_flow.DeployStrategy.BatchStrategy.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DEPLOYSTRATEGY_BATCHSTRATEGY_AUTOBATCH, _DEPLOYSTRATEGY_BATCHSTRATEGY_MANUALBATCH, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=660,
  serialized_end=1115,
)

_DEPLOYSTRATEGY_PACKAGELIST = _descriptor.Descriptor(
  name='PackageList',
  full_name='easy_flow.DeployStrategy.PackageList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='packageName', full_name='easy_flow.DeployStrategy.PackageList.packageName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cluster', full_name='easy_flow.DeployStrategy.PackageList.cluster', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targetVersion', full_name='easy_flow.DeployStrategy.PackageList.targetVersion', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preStop', full_name='easy_flow.DeployStrategy.PackageList.preStop', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='postRestart', full_name='easy_flow.DeployStrategy.PackageList.postRestart', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='autoStart', full_name='easy_flow.DeployStrategy.PackageList.autoStart', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userCheck', full_name='easy_flow.DeployStrategy.PackageList.userCheck', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fullUpdate', full_name='easy_flow.DeployStrategy.PackageList.fullUpdate', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageId', full_name='easy_flow.DeployStrategy.PackageList.packageId', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='installPath', full_name='easy_flow.DeployStrategy.PackageList.installPath', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='easy_flow.DeployStrategy.PackageList.type', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='platform', full_name='easy_flow.DeployStrategy.PackageList.platform', index=11,
      number=12, type=9, cpp_type=9, label=1,
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
  serialized_end=1379,
)

_DEPLOYSTRATEGY_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='easy_flow.DeployStrategy.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='outOfDate', full_name='easy_flow.DeployStrategy.Status.outOfDate', index=0,
      number=1, type=8, cpp_type=7, label=1,
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
  serialized_start=1381,
  serialized_end=1408,
)

_DEPLOYSTRATEGY = _descriptor.Descriptor(
  name='DeployStrategy',
  full_name='easy_flow.DeployStrategy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='easy_flow.DeployStrategy.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='easy_flow.DeployStrategy.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='apiVersion', full_name='easy_flow.DeployStrategy.apiVersion', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org', full_name='easy_flow.DeployStrategy.org', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='app', full_name='easy_flow.DeployStrategy.app', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='easy_flow.DeployStrategy.type', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batchStrategy', full_name='easy_flow.DeployStrategy.batchStrategy', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scope', full_name='easy_flow.DeployStrategy.scope', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clusters', full_name='easy_flow.DeployStrategy.clusters', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targetList', full_name='easy_flow.DeployStrategy.targetList', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clusterEnvironment', full_name='easy_flow.DeployStrategy.clusterEnvironment', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clusterType', full_name='easy_flow.DeployStrategy.clusterType', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageList', full_name='easy_flow.DeployStrategy.packageList', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='easy_flow.DeployStrategy.status', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DEPLOYSTRATEGY_APP, _DEPLOYSTRATEGY_BATCHSTRATEGY, _DEPLOYSTRATEGY_PACKAGELIST, _DEPLOYSTRATEGY_STATUS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=170,
  serialized_end=1408,
)

_DEPLOYSTRATEGY_APP.containing_type = _DEPLOYSTRATEGY
_DEPLOYSTRATEGY_BATCHSTRATEGY_AUTOBATCH.containing_type = _DEPLOYSTRATEGY_BATCHSTRATEGY
_DEPLOYSTRATEGY_BATCHSTRATEGY_MANUALBATCH_BATCHES.fields_by_name['targets'].message_type = ucpro__sdk_dot_model_dot_easy__flow_dot_deploy__target__pb2._DEPLOYTARGET
_DEPLOYSTRATEGY_BATCHSTRATEGY_MANUALBATCH_BATCHES.containing_type = _DEPLOYSTRATEGY_BATCHSTRATEGY_MANUALBATCH
_DEPLOYSTRATEGY_BATCHSTRATEGY_MANUALBATCH.fields_by_name['batches'].message_type = _DEPLOYSTRATEGY_BATCHSTRATEGY_MANUALBATCH_BATCHES
_DEPLOYSTRATEGY_BATCHSTRATEGY_MANUALBATCH.containing_type = _DEPLOYSTRATEGY_BATCHSTRATEGY
_DEPLOYSTRATEGY_BATCHSTRATEGY.fields_by_name['autoBatch'].message_type = _DEPLOYSTRATEGY_BATCHSTRATEGY_AUTOBATCH
_DEPLOYSTRATEGY_BATCHSTRATEGY.fields_by_name['manualBatch'].message_type = _DEPLOYSTRATEGY_BATCHSTRATEGY_MANUALBATCH
_DEPLOYSTRATEGY_BATCHSTRATEGY.containing_type = _DEPLOYSTRATEGY
_DEPLOYSTRATEGY_PACKAGELIST.fields_by_name['cluster'].message_type = ucpro__sdk_dot_model_dot_cmdb_dot_cluster__info__pb2._CLUSTERINFO
_DEPLOYSTRATEGY_PACKAGELIST.containing_type = _DEPLOYSTRATEGY
_DEPLOYSTRATEGY_STATUS.containing_type = _DEPLOYSTRATEGY
_DEPLOYSTRATEGY.fields_by_name['app'].message_type = _DEPLOYSTRATEGY_APP
_DEPLOYSTRATEGY.fields_by_name['batchStrategy'].message_type = _DEPLOYSTRATEGY_BATCHSTRATEGY
_DEPLOYSTRATEGY.fields_by_name['clusters'].message_type = ucpro__sdk_dot_model_dot_cmdb_dot_cluster__info__pb2._CLUSTERINFO
_DEPLOYSTRATEGY.fields_by_name['targetList'].message_type = ucpro__sdk_dot_model_dot_easy__flow_dot_target__info__pb2._TARGETINFO
_DEPLOYSTRATEGY.fields_by_name['packageList'].message_type = _DEPLOYSTRATEGY_PACKAGELIST
_DEPLOYSTRATEGY.fields_by_name['status'].message_type = _DEPLOYSTRATEGY_STATUS
DESCRIPTOR.message_types_by_name['DeployStrategy'] = _DEPLOYSTRATEGY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeployStrategy = _reflection.GeneratedProtocolMessageType('DeployStrategy', (_message.Message,), {

  'App' : _reflection.GeneratedProtocolMessageType('App', (_message.Message,), {
    'DESCRIPTOR' : _DEPLOYSTRATEGY_APP,
    '__module__' : 'deploy_strategy_pb2'
    # @@protoc_insertion_point(class_scope:easy_flow.DeployStrategy.App)
    })
  ,

  'BatchStrategy' : _reflection.GeneratedProtocolMessageType('BatchStrategy', (_message.Message,), {

    'AutoBatch' : _reflection.GeneratedProtocolMessageType('AutoBatch', (_message.Message,), {
      'DESCRIPTOR' : _DEPLOYSTRATEGY_BATCHSTRATEGY_AUTOBATCH,
      '__module__' : 'deploy_strategy_pb2'
      # @@protoc_insertion_point(class_scope:easy_flow.DeployStrategy.BatchStrategy.AutoBatch)
      })
    ,

    'ManualBatch' : _reflection.GeneratedProtocolMessageType('ManualBatch', (_message.Message,), {

      'Batches' : _reflection.GeneratedProtocolMessageType('Batches', (_message.Message,), {
        'DESCRIPTOR' : _DEPLOYSTRATEGY_BATCHSTRATEGY_MANUALBATCH_BATCHES,
        '__module__' : 'deploy_strategy_pb2'
        # @@protoc_insertion_point(class_scope:easy_flow.DeployStrategy.BatchStrategy.ManualBatch.Batches)
        })
      ,
      'DESCRIPTOR' : _DEPLOYSTRATEGY_BATCHSTRATEGY_MANUALBATCH,
      '__module__' : 'deploy_strategy_pb2'
      # @@protoc_insertion_point(class_scope:easy_flow.DeployStrategy.BatchStrategy.ManualBatch)
      })
    ,
    'DESCRIPTOR' : _DEPLOYSTRATEGY_BATCHSTRATEGY,
    '__module__' : 'deploy_strategy_pb2'
    # @@protoc_insertion_point(class_scope:easy_flow.DeployStrategy.BatchStrategy)
    })
  ,

  'PackageList' : _reflection.GeneratedProtocolMessageType('PackageList', (_message.Message,), {
    'DESCRIPTOR' : _DEPLOYSTRATEGY_PACKAGELIST,
    '__module__' : 'deploy_strategy_pb2'
    # @@protoc_insertion_point(class_scope:easy_flow.DeployStrategy.PackageList)
    })
  ,

  'Status' : _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
    'DESCRIPTOR' : _DEPLOYSTRATEGY_STATUS,
    '__module__' : 'deploy_strategy_pb2'
    # @@protoc_insertion_point(class_scope:easy_flow.DeployStrategy.Status)
    })
  ,
  'DESCRIPTOR' : _DEPLOYSTRATEGY,
  '__module__' : 'deploy_strategy_pb2'
  # @@protoc_insertion_point(class_scope:easy_flow.DeployStrategy)
  })
_sym_db.RegisterMessage(DeployStrategy)
_sym_db.RegisterMessage(DeployStrategy.App)
_sym_db.RegisterMessage(DeployStrategy.BatchStrategy)
_sym_db.RegisterMessage(DeployStrategy.BatchStrategy.AutoBatch)
_sym_db.RegisterMessage(DeployStrategy.BatchStrategy.ManualBatch)
_sym_db.RegisterMessage(DeployStrategy.BatchStrategy.ManualBatch.Batches)
_sym_db.RegisterMessage(DeployStrategy.PackageList)
_sym_db.RegisterMessage(DeployStrategy.Status)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
