# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: create.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from container_sdk.model.container import service_pb2 as container__sdk_dot_model_dot_container_dot_service__pb2
from container_sdk.model.container import service_spec_pb2 as container__sdk_dot_model_dot_container_dot_service__spec__pb2
from container_sdk.model.container import loadbalancer_status_pb2 as container__sdk_dot_model_dot_container_dot_loadbalancer__status__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='create.proto',
  package='service',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0c\x63reate.proto\x12\x07service\x1a+container_sdk/model/container/service.proto\x1a\x30\x63ontainer_sdk/model/container/service_spec.proto\x1a\x37\x63ontainer_sdk/model/container/loadbalancer_status.proto\x1a\x1cgoogle/protobuf/struct.proto\"k\n\rCreateRequest\x12\x0c\n\x04rgId\x18\x01 \x01(\t\x12\x13\n\x0bnamespaceId\x18\x02 \x01(\t\x12\x12\n\nworkloadId\x18\x03 \x01(\t\x12#\n\x07service\x18\x04 \x01(\x0b\x32\x12.container.Service\"k\n\x15\x43reateResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12 \n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x12.container.Serviceb\x06proto3')
  ,
  dependencies=[container__sdk_dot_model_dot_container_dot_service__pb2.DESCRIPTOR,container__sdk_dot_model_dot_container_dot_service__spec__pb2.DESCRIPTOR,container__sdk_dot_model_dot_container_dot_loadbalancer__status__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_CREATEREQUEST = _descriptor.Descriptor(
  name='CreateRequest',
  full_name='service.CreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rgId', full_name='service.CreateRequest.rgId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='namespaceId', full_name='service.CreateRequest.namespaceId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workloadId', full_name='service.CreateRequest.workloadId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service', full_name='service.CreateRequest.service', index=3,
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
  serialized_start=207,
  serialized_end=314,
)


_CREATERESPONSEWRAPPER = _descriptor.Descriptor(
  name='CreateResponseWrapper',
  full_name='service.CreateResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='service.CreateResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='service.CreateResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='service.CreateResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='service.CreateResponseWrapper.data', index=3,
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
  serialized_start=316,
  serialized_end=423,
)

_CREATEREQUEST.fields_by_name['service'].message_type = container__sdk_dot_model_dot_container_dot_service__pb2._SERVICE
_CREATERESPONSEWRAPPER.fields_by_name['data'].message_type = container__sdk_dot_model_dot_container_dot_service__pb2._SERVICE
DESCRIPTOR.message_types_by_name['CreateRequest'] = _CREATEREQUEST
DESCRIPTOR.message_types_by_name['CreateResponseWrapper'] = _CREATERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateRequest = _reflection.GeneratedProtocolMessageType('CreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEREQUEST,
  '__module__' : 'create_pb2'
  # @@protoc_insertion_point(class_scope:service.CreateRequest)
  })
_sym_db.RegisterMessage(CreateRequest)

CreateResponseWrapper = _reflection.GeneratedProtocolMessageType('CreateResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _CREATERESPONSEWRAPPER,
  '__module__' : 'create_pb2'
  # @@protoc_insertion_point(class_scope:service.CreateResponseWrapper)
  })
_sym_db.RegisterMessage(CreateResponseWrapper)


# @@protoc_insertion_point(module_scope)
