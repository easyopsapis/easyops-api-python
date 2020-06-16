# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pod_status.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from container_sdk.model.container import container_status_pb2 as container__sdk_dot_model_dot_container_dot_container__status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pod_status.proto',
  package='container',
  syntax='proto3',
  serialized_options=_b('ZCgo.easyops.local/contracts/protorepo-models/easyops/model/container'),
  serialized_pb=_b('\n\x10pod_status.proto\x12\tcontainer\x1a\x34\x63ontainer_sdk/model/container/container_status.proto\"\xbc\x01\n\tPodStatus\x12\r\n\x05phase\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x39\n\x15initContainerStatuses\x18\x03 \x03(\x0b\x32\x1a.container.ContainerStatus\x12\x35\n\x11\x63ontainerStatuses\x18\x04 \x03(\x0b\x32\x1a.container.ContainerStatus\x12\x0e\n\x06hostIP\x18\x05 \x01(\t\x12\r\n\x05podIP\x18\x06 \x01(\tBEZCgo.easyops.local/contracts/protorepo-models/easyops/model/containerb\x06proto3')
  ,
  dependencies=[container__sdk_dot_model_dot_container_dot_container__status__pb2.DESCRIPTOR,])




_PODSTATUS = _descriptor.Descriptor(
  name='PodStatus',
  full_name='container.PodStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='phase', full_name='container.PodStatus.phase', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='container.PodStatus.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='initContainerStatuses', full_name='container.PodStatus.initContainerStatuses', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='containerStatuses', full_name='container.PodStatus.containerStatuses', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hostIP', full_name='container.PodStatus.hostIP', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='podIP', full_name='container.PodStatus.podIP', index=5,
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
  serialized_start=86,
  serialized_end=274,
)

_PODSTATUS.fields_by_name['initContainerStatuses'].message_type = container__sdk_dot_model_dot_container_dot_container__status__pb2._CONTAINERSTATUS
_PODSTATUS.fields_by_name['containerStatuses'].message_type = container__sdk_dot_model_dot_container_dot_container__status__pb2._CONTAINERSTATUS
DESCRIPTOR.message_types_by_name['PodStatus'] = _PODSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PodStatus = _reflection.GeneratedProtocolMessageType('PodStatus', (_message.Message,), {
  'DESCRIPTOR' : _PODSTATUS,
  '__module__' : 'pod_status_pb2'
  # @@protoc_insertion_point(class_scope:container.PodStatus)
  })
_sym_db.RegisterMessage(PodStatus)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
