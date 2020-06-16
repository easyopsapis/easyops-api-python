# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ingress_rule.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from monitor_sdk.model.container import http_ingress_path_pb2 as monitor__sdk_dot_model_dot_container_dot_http__ingress__path__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ingress_rule.proto',
  package='container',
  syntax='proto3',
  serialized_options=_b('ZCgo.easyops.local/contracts/protorepo-models/easyops/model/container'),
  serialized_pb=_b('\n\x12ingress_rule.proto\x12\tcontainer\x1a\x33monitor_sdk/model/container/http_ingress_path.proto\"y\n\x0bIngressRule\x12\x0c\n\x04host\x18\x01 \x01(\t\x12)\n\x04http\x18\x02 \x01(\x0b\x32\x1b.container.IngressRule.Http\x1a\x31\n\x04Http\x12)\n\x05paths\x18\x01 \x03(\x0b\x32\x1a.container.HTTPIngressPathBEZCgo.easyops.local/contracts/protorepo-models/easyops/model/containerb\x06proto3')
  ,
  dependencies=[monitor__sdk_dot_model_dot_container_dot_http__ingress__path__pb2.DESCRIPTOR,])




_INGRESSRULE_HTTP = _descriptor.Descriptor(
  name='Http',
  full_name='container.IngressRule.Http',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='paths', full_name='container.IngressRule.Http.paths', index=0,
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
  serialized_start=158,
  serialized_end=207,
)

_INGRESSRULE = _descriptor.Descriptor(
  name='IngressRule',
  full_name='container.IngressRule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='host', full_name='container.IngressRule.host', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='http', full_name='container.IngressRule.http', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_INGRESSRULE_HTTP, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=86,
  serialized_end=207,
)

_INGRESSRULE_HTTP.fields_by_name['paths'].message_type = monitor__sdk_dot_model_dot_container_dot_http__ingress__path__pb2._HTTPINGRESSPATH
_INGRESSRULE_HTTP.containing_type = _INGRESSRULE
_INGRESSRULE.fields_by_name['http'].message_type = _INGRESSRULE_HTTP
DESCRIPTOR.message_types_by_name['IngressRule'] = _INGRESSRULE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IngressRule = _reflection.GeneratedProtocolMessageType('IngressRule', (_message.Message,), {

  'Http' : _reflection.GeneratedProtocolMessageType('Http', (_message.Message,), {
    'DESCRIPTOR' : _INGRESSRULE_HTTP,
    '__module__' : 'ingress_rule_pb2'
    # @@protoc_insertion_point(class_scope:container.IngressRule.Http)
    })
  ,
  'DESCRIPTOR' : _INGRESSRULE,
  '__module__' : 'ingress_rule_pb2'
  # @@protoc_insertion_point(class_scope:container.IngressRule)
  })
_sym_db.RegisterMessage(IngressRule)
_sym_db.RegisterMessage(IngressRule.Http)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
