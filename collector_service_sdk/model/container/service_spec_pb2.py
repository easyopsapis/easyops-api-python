# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service_spec.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from collector_service_sdk.model.container import service_port_pb2 as collector__service__sdk_dot_model_dot_container_dot_service__port__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='service_spec.proto',
  package='container',
  syntax='proto3',
  serialized_options=_b('ZCgo.easyops.local/contracts/protorepo-models/easyops/model/container'),
  serialized_pb=_b('\n\x12service_spec.proto\x12\tcontainer\x1a\x38\x63ollector_service_sdk/model/container/service_port.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xdc\x01\n\x0bServiceSpec\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x11\n\tclusterIP\x18\x02 \x01(\t\x12\x16\n\x0eloadBalancerIP\x18\x03 \x01(\t\x12\x13\n\x0b\x65xternalIPs\x18\x04 \x03(\t\x12\x14\n\x0c\x65xternalName\x18\x05 \x01(\t\x12\x17\n\x0fsessionAffinity\x18\x06 \x01(\t\x12)\n\x08selector\x18\x07 \x01(\x0b\x32\x17.google.protobuf.Struct\x12%\n\x05ports\x18\x08 \x03(\x0b\x32\x16.container.ServicePortBEZCgo.easyops.local/contracts/protorepo-models/easyops/model/containerb\x06proto3')
  ,
  dependencies=[collector__service__sdk_dot_model_dot_container_dot_service__port__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_SERVICESPEC = _descriptor.Descriptor(
  name='ServiceSpec',
  full_name='container.ServiceSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='container.ServiceSpec.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clusterIP', full_name='container.ServiceSpec.clusterIP', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='loadBalancerIP', full_name='container.ServiceSpec.loadBalancerIP', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='externalIPs', full_name='container.ServiceSpec.externalIPs', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='externalName', full_name='container.ServiceSpec.externalName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sessionAffinity', full_name='container.ServiceSpec.sessionAffinity', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='selector', full_name='container.ServiceSpec.selector', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ports', full_name='container.ServiceSpec.ports', index=7,
      number=8, type=11, cpp_type=10, label=3,
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
  serialized_start=122,
  serialized_end=342,
)

_SERVICESPEC.fields_by_name['selector'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SERVICESPEC.fields_by_name['ports'].message_type = collector__service__sdk_dot_model_dot_container_dot_service__port__pb2._SERVICEPORT
DESCRIPTOR.message_types_by_name['ServiceSpec'] = _SERVICESPEC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ServiceSpec = _reflection.GeneratedProtocolMessageType('ServiceSpec', (_message.Message,), {
  'DESCRIPTOR' : _SERVICESPEC,
  '__module__' : 'service_spec_pb2'
  # @@protoc_insertion_point(class_scope:container.ServiceSpec)
  })
_sym_db.RegisterMessage(ServiceSpec)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
