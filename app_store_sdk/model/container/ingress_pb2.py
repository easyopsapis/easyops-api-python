# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ingress.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from app_store_sdk.model.container import ingress_backend_pb2 as app__store__sdk_dot_model_dot_container_dot_ingress__backend__pb2
from app_store_sdk.model.container import ingress_rule_pb2 as app__store__sdk_dot_model_dot_container_dot_ingress__rule__pb2
from app_store_sdk.model.container import ingress_tls_pb2 as app__store__sdk_dot_model_dot_container_dot_ingress__tls__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ingress.proto',
  package='container',
  syntax='proto3',
  serialized_options=_b('ZCgo.easyops.local/contracts/protorepo-models/easyops/model/container'),
  serialized_pb=_b('\n\ringress.proto\x12\tcontainer\x1a\x33\x61pp_store_sdk/model/container/ingress_backend.proto\x1a\x30\x61pp_store_sdk/model/container/ingress_rule.proto\x1a/app_store_sdk/model/container/ingress_tls.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xd4\x02\n\x07Ingress\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0c\n\x04kind\x18\x02 \x01(\t\x12\x11\n\tnamespace\x18\x03 \x01(\t\x12\x14\n\x0cresourceName\x18\x04 \x01(\t\x12\x13\n\x0b\x64isplayName\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12,\n\x0b\x61nnotations\x18\x07 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0f\n\x07\x61\x64\x64ress\x18\x08 \x03(\t\x12*\n\x07\x62\x61\x63kend\x18\t \x01(\x0b\x32\x19.container.IngressBackend\x12%\n\x05rules\x18\n \x03(\x0b\x32\x16.container.IngressRule\x12\"\n\x03tls\x18\x0b \x03(\x0b\x32\x15.container.IngressTLS\x12\r\n\x05\x63time\x18\x0c \x01(\t\x12\x0f\n\x07\x63reator\x18\r \x01(\tBEZCgo.easyops.local/contracts/protorepo-models/easyops/model/containerb\x06proto3')
  ,
  dependencies=[app__store__sdk_dot_model_dot_container_dot_ingress__backend__pb2.DESCRIPTOR,app__store__sdk_dot_model_dot_container_dot_ingress__rule__pb2.DESCRIPTOR,app__store__sdk_dot_model_dot_container_dot_ingress__tls__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_INGRESS = _descriptor.Descriptor(
  name='Ingress',
  full_name='container.Ingress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='container.Ingress.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kind', full_name='container.Ingress.kind', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='namespace', full_name='container.Ingress.namespace', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resourceName', full_name='container.Ingress.resourceName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='displayName', full_name='container.Ingress.displayName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='container.Ingress.description', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='annotations', full_name='container.Ingress.annotations', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='container.Ingress.address', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='backend', full_name='container.Ingress.backend', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rules', full_name='container.Ingress.rules', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tls', full_name='container.Ingress.tls', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='container.Ingress.ctime', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='container.Ingress.creator', index=12,
      number=13, type=9, cpp_type=9, label=1,
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
  serialized_start=211,
  serialized_end=551,
)

_INGRESS.fields_by_name['annotations'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_INGRESS.fields_by_name['backend'].message_type = app__store__sdk_dot_model_dot_container_dot_ingress__backend__pb2._INGRESSBACKEND
_INGRESS.fields_by_name['rules'].message_type = app__store__sdk_dot_model_dot_container_dot_ingress__rule__pb2._INGRESSRULE
_INGRESS.fields_by_name['tls'].message_type = app__store__sdk_dot_model_dot_container_dot_ingress__tls__pb2._INGRESSTLS
DESCRIPTOR.message_types_by_name['Ingress'] = _INGRESS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Ingress = _reflection.GeneratedProtocolMessageType('Ingress', (_message.Message,), {
  'DESCRIPTOR' : _INGRESS,
  '__module__' : 'ingress_pb2'
  # @@protoc_insertion_point(class_scope:container.Ingress)
  })
_sym_db.RegisterMessage(Ingress)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
