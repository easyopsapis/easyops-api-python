# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: loadbalancer_status.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='loadbalancer_status.proto',
  package='container',
  syntax='proto3',
  serialized_options=_b('ZCgo.easyops.local/contracts/protorepo-models/easyops/model/container'),
  serialized_pb=_b('\n\x19loadbalancer_status.proto\x12\tcontainer\"u\n\x12LoadBalancerStatus\x12\x36\n\x07ingress\x18\x01 \x03(\x0b\x32%.container.LoadBalancerStatus.Ingress\x1a\'\n\x07Ingress\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x10\n\x08hostname\x18\x02 \x01(\tBEZCgo.easyops.local/contracts/protorepo-models/easyops/model/containerb\x06proto3')
)




_LOADBALANCERSTATUS_INGRESS = _descriptor.Descriptor(
  name='Ingress',
  full_name='container.LoadBalancerStatus.Ingress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='container.LoadBalancerStatus.Ingress.ip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hostname', full_name='container.LoadBalancerStatus.Ingress.hostname', index=1,
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
  serialized_start=118,
  serialized_end=157,
)

_LOADBALANCERSTATUS = _descriptor.Descriptor(
  name='LoadBalancerStatus',
  full_name='container.LoadBalancerStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ingress', full_name='container.LoadBalancerStatus.ingress', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LOADBALANCERSTATUS_INGRESS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=157,
)

_LOADBALANCERSTATUS_INGRESS.containing_type = _LOADBALANCERSTATUS
_LOADBALANCERSTATUS.fields_by_name['ingress'].message_type = _LOADBALANCERSTATUS_INGRESS
DESCRIPTOR.message_types_by_name['LoadBalancerStatus'] = _LOADBALANCERSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LoadBalancerStatus = _reflection.GeneratedProtocolMessageType('LoadBalancerStatus', (_message.Message,), {

  'Ingress' : _reflection.GeneratedProtocolMessageType('Ingress', (_message.Message,), {
    'DESCRIPTOR' : _LOADBALANCERSTATUS_INGRESS,
    '__module__' : 'loadbalancer_status_pb2'
    # @@protoc_insertion_point(class_scope:container.LoadBalancerStatus.Ingress)
    })
  ,
  'DESCRIPTOR' : _LOADBALANCERSTATUS,
  '__module__' : 'loadbalancer_status_pb2'
  # @@protoc_insertion_point(class_scope:container.LoadBalancerStatus)
  })
_sym_db.RegisterMessage(LoadBalancerStatus)
_sym_db.RegisterMessage(LoadBalancerStatus.Ingress)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
