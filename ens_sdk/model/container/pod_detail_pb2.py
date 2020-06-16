# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pod_detail.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ens_sdk.model.container import metadata_pb2 as ens__sdk_dot_model_dot_container_dot_metadata__pb2
from ens_sdk.model.container import pod_status_pb2 as ens__sdk_dot_model_dot_container_dot_pod__status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pod_detail.proto',
  package='container',
  syntax='proto3',
  serialized_options=_b('ZCgo.easyops.local/contracts/protorepo-models/easyops/model/container'),
  serialized_pb=_b('\n\x10pod_detail.proto\x12\tcontainer\x1a&ens_sdk/model/container/metadata.proto\x1a(ens_sdk/model/container/pod_status.proto\"X\n\tPodDetail\x12%\n\x08metadata\x18\x01 \x01(\x0b\x32\x13.container.Metadata\x12$\n\x06status\x18\x02 \x01(\x0b\x32\x14.container.PodStatusBEZCgo.easyops.local/contracts/protorepo-models/easyops/model/containerb\x06proto3')
  ,
  dependencies=[ens__sdk_dot_model_dot_container_dot_metadata__pb2.DESCRIPTOR,ens__sdk_dot_model_dot_container_dot_pod__status__pb2.DESCRIPTOR,])




_PODDETAIL = _descriptor.Descriptor(
  name='PodDetail',
  full_name='container.PodDetail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadata', full_name='container.PodDetail.metadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='container.PodDetail.status', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=113,
  serialized_end=201,
)

_PODDETAIL.fields_by_name['metadata'].message_type = ens__sdk_dot_model_dot_container_dot_metadata__pb2._METADATA
_PODDETAIL.fields_by_name['status'].message_type = ens__sdk_dot_model_dot_container_dot_pod__status__pb2._PODSTATUS
DESCRIPTOR.message_types_by_name['PodDetail'] = _PODDETAIL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PodDetail = _reflection.GeneratedProtocolMessageType('PodDetail', (_message.Message,), {
  'DESCRIPTOR' : _PODDETAIL,
  '__module__' : 'pod_detail_pb2'
  # @@protoc_insertion_point(class_scope:container.PodDetail)
  })
_sym_db.RegisterMessage(PodDetail)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
