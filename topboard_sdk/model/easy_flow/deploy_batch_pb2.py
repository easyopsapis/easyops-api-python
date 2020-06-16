# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: deploy_batch.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from topboard_sdk.model.easy_flow import deploy_target_pb2 as topboard__sdk_dot_model_dot_easy__flow_dot_deploy__target__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='deploy_batch.proto',
  package='easy_flow',
  syntax='proto3',
  serialized_options=_b('ZCgo.easyops.local/contracts/protorepo-models/easyops/model/easy_flow'),
  serialized_pb=_b('\n\x12\x64\x65ploy_batch.proto\x12\teasy_flow\x1a\x30topboard_sdk/model/easy_flow/deploy_target.proto\"\xbe\x01\n\x0b\x44\x65ployBatch\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x10\n\x08\x62\x61tchNum\x18\x02 \x01(\x05\x12\x15\n\rbatchInterval\x18\x03 \x01(\x05\x12/\n\x07\x62\x61tches\x18\x04 \x03(\x0b\x32\x1e.easy_flow.DeployBatch.Batches\x12\x12\n\nfailedStop\x18\x05 \x01(\x08\x1a\x33\n\x07\x42\x61tches\x12(\n\x07targets\x18\x01 \x03(\x0b\x32\x17.easy_flow.DeployTargetBEZCgo.easyops.local/contracts/protorepo-models/easyops/model/easy_flowb\x06proto3')
  ,
  dependencies=[topboard__sdk_dot_model_dot_easy__flow_dot_deploy__target__pb2.DESCRIPTOR,])




_DEPLOYBATCH_BATCHES = _descriptor.Descriptor(
  name='Batches',
  full_name='easy_flow.DeployBatch.Batches',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='targets', full_name='easy_flow.DeployBatch.Batches.targets', index=0,
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
  serialized_start=223,
  serialized_end=274,
)

_DEPLOYBATCH = _descriptor.Descriptor(
  name='DeployBatch',
  full_name='easy_flow.DeployBatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='easy_flow.DeployBatch.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batchNum', full_name='easy_flow.DeployBatch.batchNum', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batchInterval', full_name='easy_flow.DeployBatch.batchInterval', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batches', full_name='easy_flow.DeployBatch.batches', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='failedStop', full_name='easy_flow.DeployBatch.failedStop', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DEPLOYBATCH_BATCHES, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=84,
  serialized_end=274,
)

_DEPLOYBATCH_BATCHES.fields_by_name['targets'].message_type = topboard__sdk_dot_model_dot_easy__flow_dot_deploy__target__pb2._DEPLOYTARGET
_DEPLOYBATCH_BATCHES.containing_type = _DEPLOYBATCH
_DEPLOYBATCH.fields_by_name['batches'].message_type = _DEPLOYBATCH_BATCHES
DESCRIPTOR.message_types_by_name['DeployBatch'] = _DEPLOYBATCH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeployBatch = _reflection.GeneratedProtocolMessageType('DeployBatch', (_message.Message,), {

  'Batches' : _reflection.GeneratedProtocolMessageType('Batches', (_message.Message,), {
    'DESCRIPTOR' : _DEPLOYBATCH_BATCHES,
    '__module__' : 'deploy_batch_pb2'
    # @@protoc_insertion_point(class_scope:easy_flow.DeployBatch.Batches)
    })
  ,
  'DESCRIPTOR' : _DEPLOYBATCH,
  '__module__' : 'deploy_batch_pb2'
  # @@protoc_insertion_point(class_scope:easy_flow.DeployBatch)
  })
_sym_db.RegisterMessage(DeployBatch)
_sym_db.RegisterMessage(DeployBatch.Batches)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
