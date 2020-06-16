# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list_deployment.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flowable_sdk.model.flowable import deployment_pb2 as flowable__sdk_dot_model_dot_flowable_dot_deployment__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='list_deployment.proto',
  package='deployment',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x15list_deployment.proto\x12\ndeployment\x1a,flowable_sdk/model/flowable/deployment.proto\"\xb6\x02\n\x15ListDeploymentRequest\x12\r\n\x05start\x18\x01 \x01(\x05\x12\x0c\n\x04size\x18\x02 \x01(\x05\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x10\n\x08nameLike\x18\x04 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x05 \x01(\t\x12\x19\n\x11\x63\x61tegoryNotEquals\x18\x06 \x01(\t\x12\x1a\n\x12parentDeploymentId\x18\x07 \x01(\t\x12\x1e\n\x16parentDeploymentIdLike\x18\x08 \x01(\t\x12\x10\n\x08tenantId\x18\t \x01(\t\x12\x14\n\x0ctenantIdLike\x18\n \x01(\t\x12\x17\n\x0fwithoutTenantId\x18\x0b \x01(\x08\x12\x0c\n\x04sort\x18\x0c \x01(\t\x12\r\n\x05order\x18\r \x01(\t\x12\x19\n\x11XXX_RestFieldMask\x18\x0e \x03(\t\"\x8d\x01\n\x16ListDeploymentResponse\x12*\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x1c.flowable.FlowableDeployment\x12\r\n\x05total\x18\x02 \x01(\x05\x12\r\n\x05start\x18\x03 \x01(\x05\x12\x0c\n\x04sort\x18\x04 \x01(\t\x12\r\n\x05order\x18\x05 \x01(\t\x12\x0c\n\x04size\x18\x06 \x01(\x05\"\x83\x01\n\x1dListDeploymentResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x30\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\".deployment.ListDeploymentResponseb\x06proto3')
  ,
  dependencies=[flowable__sdk_dot_model_dot_flowable_dot_deployment__pb2.DESCRIPTOR,])




_LISTDEPLOYMENTREQUEST = _descriptor.Descriptor(
  name='ListDeploymentRequest',
  full_name='deployment.ListDeploymentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='deployment.ListDeploymentRequest.start', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='deployment.ListDeploymentRequest.size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='deployment.ListDeploymentRequest.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nameLike', full_name='deployment.ListDeploymentRequest.nameLike', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='deployment.ListDeploymentRequest.category', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='categoryNotEquals', full_name='deployment.ListDeploymentRequest.categoryNotEquals', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parentDeploymentId', full_name='deployment.ListDeploymentRequest.parentDeploymentId', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parentDeploymentIdLike', full_name='deployment.ListDeploymentRequest.parentDeploymentIdLike', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tenantId', full_name='deployment.ListDeploymentRequest.tenantId', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tenantIdLike', full_name='deployment.ListDeploymentRequest.tenantIdLike', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='withoutTenantId', full_name='deployment.ListDeploymentRequest.withoutTenantId', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sort', full_name='deployment.ListDeploymentRequest.sort', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order', full_name='deployment.ListDeploymentRequest.order', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='XXX_RestFieldMask', full_name='deployment.ListDeploymentRequest.XXX_RestFieldMask', index=13,
      number=14, type=9, cpp_type=9, label=3,
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
  serialized_start=84,
  serialized_end=394,
)


_LISTDEPLOYMENTRESPONSE = _descriptor.Descriptor(
  name='ListDeploymentResponse',
  full_name='deployment.ListDeploymentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='deployment.ListDeploymentResponse.data', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='deployment.ListDeploymentResponse.total', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start', full_name='deployment.ListDeploymentResponse.start', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sort', full_name='deployment.ListDeploymentResponse.sort', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order', full_name='deployment.ListDeploymentResponse.order', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='deployment.ListDeploymentResponse.size', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=397,
  serialized_end=538,
)


_LISTDEPLOYMENTRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListDeploymentResponseWrapper',
  full_name='deployment.ListDeploymentResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='deployment.ListDeploymentResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='deployment.ListDeploymentResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='deployment.ListDeploymentResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='deployment.ListDeploymentResponseWrapper.data', index=3,
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
  serialized_start=541,
  serialized_end=672,
)

_LISTDEPLOYMENTRESPONSE.fields_by_name['data'].message_type = flowable__sdk_dot_model_dot_flowable_dot_deployment__pb2._FLOWABLEDEPLOYMENT
_LISTDEPLOYMENTRESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTDEPLOYMENTRESPONSE
DESCRIPTOR.message_types_by_name['ListDeploymentRequest'] = _LISTDEPLOYMENTREQUEST
DESCRIPTOR.message_types_by_name['ListDeploymentResponse'] = _LISTDEPLOYMENTRESPONSE
DESCRIPTOR.message_types_by_name['ListDeploymentResponseWrapper'] = _LISTDEPLOYMENTRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListDeploymentRequest = _reflection.GeneratedProtocolMessageType('ListDeploymentRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTDEPLOYMENTREQUEST,
  '__module__' : 'list_deployment_pb2'
  # @@protoc_insertion_point(class_scope:deployment.ListDeploymentRequest)
  })
_sym_db.RegisterMessage(ListDeploymentRequest)

ListDeploymentResponse = _reflection.GeneratedProtocolMessageType('ListDeploymentResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTDEPLOYMENTRESPONSE,
  '__module__' : 'list_deployment_pb2'
  # @@protoc_insertion_point(class_scope:deployment.ListDeploymentResponse)
  })
_sym_db.RegisterMessage(ListDeploymentResponse)

ListDeploymentResponseWrapper = _reflection.GeneratedProtocolMessageType('ListDeploymentResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _LISTDEPLOYMENTRESPONSEWRAPPER,
  '__module__' : 'list_deployment_pb2'
  # @@protoc_insertion_point(class_scope:deployment.ListDeploymentResponseWrapper)
  })
_sym_db.RegisterMessage(ListDeploymentResponseWrapper)


# @@protoc_insertion_point(module_scope)