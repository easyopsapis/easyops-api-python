# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from collector_center_sdk.model.container import service_spec_pb2 as collector__center__sdk_dot_model_dot_container_dot_service__spec__pb2
from collector_center_sdk.model.container import loadbalancer_status_pb2 as collector__center__sdk_dot_model_dot_container_dot_loadbalancer__status__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='service.proto',
  package='container',
  syntax='proto3',
  serialized_options=_b('ZCgo.easyops.local/contracts/protorepo-models/easyops/model/container'),
  serialized_pb=_b('\n\rservice.proto\x12\tcontainer\x1a\x37\x63ollector_center_sdk/model/container/service_spec.proto\x1a>collector_center_sdk/model/container/loadbalancer_status.proto\x1a\x1cgoogle/protobuf/struct.proto\"\x8b\x03\n\x07Service\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0c\n\x04kind\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x11\n\tnamespace\x18\x04 \x01(\t\x12\x14\n\x0cresourceName\x18\x05 \x01(\t\x12,\n\x0b\x61nnotations\x18\x06 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\'\n\x06labels\x18\x07 \x01(\x0b\x32\x17.google.protobuf.Struct\x12$\n\x04spec\x18\x08 \x01(\x0b\x32\x16.container.ServiceSpec\x12\x14\n\x0cresourceSpec\x18\t \x01(\t\x12)\n\x06status\x18\n \x01(\x0b\x32\x19.container.Service.Status\x12\x19\n\x11\x63reationTimestamp\x18\x0b \x01(\t\x12\x0f\n\x07\x63reator\x18\x0c \x01(\t\x1a=\n\x06Status\x12\x33\n\x0cloadBalancer\x18\x01 \x01(\x0b\x32\x1d.container.LoadBalancerStatusBEZCgo.easyops.local/contracts/protorepo-models/easyops/model/containerb\x06proto3')
  ,
  dependencies=[collector__center__sdk_dot_model_dot_container_dot_service__spec__pb2.DESCRIPTOR,collector__center__sdk_dot_model_dot_container_dot_loadbalancer__status__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_SERVICE_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='container.Service.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='loadBalancer', full_name='container.Service.Status.loadBalancer', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=514,
  serialized_end=575,
)

_SERVICE = _descriptor.Descriptor(
  name='Service',
  full_name='container.Service',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='container.Service.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kind', full_name='container.Service.kind', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='container.Service.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='namespace', full_name='container.Service.namespace', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resourceName', full_name='container.Service.resourceName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='annotations', full_name='container.Service.annotations', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='container.Service.labels', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spec', full_name='container.Service.spec', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resourceSpec', full_name='container.Service.resourceSpec', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='container.Service.status', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creationTimestamp', full_name='container.Service.creationTimestamp', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='container.Service.creator', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SERVICE_STATUS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=180,
  serialized_end=575,
)

_SERVICE_STATUS.fields_by_name['loadBalancer'].message_type = collector__center__sdk_dot_model_dot_container_dot_loadbalancer__status__pb2._LOADBALANCERSTATUS
_SERVICE_STATUS.containing_type = _SERVICE
_SERVICE.fields_by_name['annotations'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SERVICE.fields_by_name['labels'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SERVICE.fields_by_name['spec'].message_type = collector__center__sdk_dot_model_dot_container_dot_service__spec__pb2._SERVICESPEC
_SERVICE.fields_by_name['status'].message_type = _SERVICE_STATUS
DESCRIPTOR.message_types_by_name['Service'] = _SERVICE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Service = _reflection.GeneratedProtocolMessageType('Service', (_message.Message,), {

  'Status' : _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
    'DESCRIPTOR' : _SERVICE_STATUS,
    '__module__' : 'service_pb2'
    # @@protoc_insertion_point(class_scope:container.Service.Status)
    })
  ,
  'DESCRIPTOR' : _SERVICE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:container.Service)
  })
_sym_db.RegisterMessage(Service)
_sym_db.RegisterMessage(Service.Status)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
