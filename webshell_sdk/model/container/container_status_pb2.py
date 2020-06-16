# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: container_status.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from webshell_sdk.model.container import container_state_pb2 as webshell__sdk_dot_model_dot_container_dot_container__state__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='container_status.proto',
  package='container',
  syntax='proto3',
  serialized_options=_b('ZCgo.easyops.local/contracts/protorepo-models/easyops/model/container'),
  serialized_pb=_b('\n\x16\x63ontainer_status.proto\x12\tcontainer\x1a\x32webshell_sdk/model/container/container_state.proto\"n\n\x0f\x43ontainerStatus\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0crestartCount\x18\x02 \x01(\x05\x12(\n\x05state\x18\x03 \x01(\x0b\x32\x19.container.ContainerState\x12\r\n\x05image\x18\x04 \x01(\tBEZCgo.easyops.local/contracts/protorepo-models/easyops/model/containerb\x06proto3')
  ,
  dependencies=[webshell__sdk_dot_model_dot_container_dot_container__state__pb2.DESCRIPTOR,])




_CONTAINERSTATUS = _descriptor.Descriptor(
  name='ContainerStatus',
  full_name='container.ContainerStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='container.ContainerStatus.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='restartCount', full_name='container.ContainerStatus.restartCount', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='container.ContainerStatus.state', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image', full_name='container.ContainerStatus.image', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=89,
  serialized_end=199,
)

_CONTAINERSTATUS.fields_by_name['state'].message_type = webshell__sdk_dot_model_dot_container_dot_container__state__pb2._CONTAINERSTATE
DESCRIPTOR.message_types_by_name['ContainerStatus'] = _CONTAINERSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ContainerStatus = _reflection.GeneratedProtocolMessageType('ContainerStatus', (_message.Message,), {
  'DESCRIPTOR' : _CONTAINERSTATUS,
  '__module__' : 'container_status_pb2'
  # @@protoc_insertion_point(class_scope:container.ContainerStatus)
  })
_sym_db.RegisterMessage(ContainerStatus)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
