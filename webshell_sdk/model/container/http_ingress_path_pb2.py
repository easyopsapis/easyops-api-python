# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: http_ingress_path.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from webshell_sdk.model.container import ingress_backend_pb2 as webshell__sdk_dot_model_dot_container_dot_ingress__backend__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='http_ingress_path.proto',
  package='container',
  syntax='proto3',
  serialized_options=_b('ZCgo.easyops.local/contracts/protorepo-models/easyops/model/container'),
  serialized_pb=_b('\n\x17http_ingress_path.proto\x12\tcontainer\x1a\x32webshell_sdk/model/container/ingress_backend.proto\"K\n\x0fHTTPIngressPath\x12\x0c\n\x04path\x18\x01 \x01(\t\x12*\n\x07\x62\x61\x63kend\x18\x02 \x01(\x0b\x32\x19.container.IngressBackendBEZCgo.easyops.local/contracts/protorepo-models/easyops/model/containerb\x06proto3')
  ,
  dependencies=[webshell__sdk_dot_model_dot_container_dot_ingress__backend__pb2.DESCRIPTOR,])




_HTTPINGRESSPATH = _descriptor.Descriptor(
  name='HTTPIngressPath',
  full_name='container.HTTPIngressPath',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='container.HTTPIngressPath.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='backend', full_name='container.HTTPIngressPath.backend', index=1,
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
  serialized_start=90,
  serialized_end=165,
)

_HTTPINGRESSPATH.fields_by_name['backend'].message_type = webshell__sdk_dot_model_dot_container_dot_ingress__backend__pb2._INGRESSBACKEND
DESCRIPTOR.message_types_by_name['HTTPIngressPath'] = _HTTPINGRESSPATH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HTTPIngressPath = _reflection.GeneratedProtocolMessageType('HTTPIngressPath', (_message.Message,), {
  'DESCRIPTOR' : _HTTPINGRESSPATH,
  '__module__' : 'http_ingress_path_pb2'
  # @@protoc_insertion_point(class_scope:container.HTTPIngressPath)
  })
_sym_db.RegisterMessage(HTTPIngressPath)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
