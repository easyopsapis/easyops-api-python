# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: update.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from container_sdk.model.container import ingress_pb2 as container__sdk_dot_model_dot_container_dot_ingress__pb2
from container_sdk.model.container import ingress_backend_pb2 as container__sdk_dot_model_dot_container_dot_ingress__backend__pb2
from container_sdk.model.container import ingress_rule_pb2 as container__sdk_dot_model_dot_container_dot_ingress__rule__pb2
from container_sdk.model.container import ingress_tls_pb2 as container__sdk_dot_model_dot_container_dot_ingress__tls__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='update.proto',
  package='ingress',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0cupdate.proto\x12\x07ingress\x1a+container_sdk/model/container/ingress.proto\x1a\x33\x63ontainer_sdk/model/container/ingress_backend.proto\x1a\x30\x63ontainer_sdk/model/container/ingress_rule.proto\x1a/container_sdk/model/container/ingress_tls.proto\x1a\x1cgoogle/protobuf/struct.proto\"H\n\rUpdateRequest\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12#\n\x07ingress\x18\x02 \x01(\x0b\x32\x12.container.Ingress\"k\n\x15UpdateResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12 \n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x12.container.Ingressb\x06proto3')
  ,
  dependencies=[container__sdk_dot_model_dot_container_dot_ingress__pb2.DESCRIPTOR,container__sdk_dot_model_dot_container_dot_ingress__backend__pb2.DESCRIPTOR,container__sdk_dot_model_dot_container_dot_ingress__rule__pb2.DESCRIPTOR,container__sdk_dot_model_dot_container_dot_ingress__tls__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_UPDATEREQUEST = _descriptor.Descriptor(
  name='UpdateRequest',
  full_name='ingress.UpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='ingress.UpdateRequest.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ingress', full_name='ingress.UpdateRequest.ingress', index=1,
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
  serialized_start=252,
  serialized_end=324,
)


_UPDATERESPONSEWRAPPER = _descriptor.Descriptor(
  name='UpdateResponseWrapper',
  full_name='ingress.UpdateResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='ingress.UpdateResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='ingress.UpdateResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='ingress.UpdateResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='ingress.UpdateResponseWrapper.data', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=326,
  serialized_end=433,
)

_UPDATEREQUEST.fields_by_name['ingress'].message_type = container__sdk_dot_model_dot_container_dot_ingress__pb2._INGRESS
_UPDATERESPONSEWRAPPER.fields_by_name['data'].message_type = container__sdk_dot_model_dot_container_dot_ingress__pb2._INGRESS
DESCRIPTOR.message_types_by_name['UpdateRequest'] = _UPDATEREQUEST
DESCRIPTOR.message_types_by_name['UpdateResponseWrapper'] = _UPDATERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateRequest = _reflection.GeneratedProtocolMessageType('UpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEREQUEST,
  '__module__' : 'update_pb2'
  # @@protoc_insertion_point(class_scope:ingress.UpdateRequest)
  })
_sym_db.RegisterMessage(UpdateRequest)

UpdateResponseWrapper = _reflection.GeneratedProtocolMessageType('UpdateResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _UPDATERESPONSEWRAPPER,
  '__module__' : 'update_pb2'
  # @@protoc_insertion_point(class_scope:ingress.UpdateResponseWrapper)
  })
_sym_db.RegisterMessage(UpdateResponseWrapper)


# @@protoc_insertion_point(module_scope)