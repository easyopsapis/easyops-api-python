# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: update_resource_spec.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from container_sdk.model.container import container_pb2 as container__sdk_dot_model_dot_container_dot_container__pb2
from container_sdk.model.container import volume_pb2 as container__sdk_dot_model_dot_container_dot_volume__pb2
from container_sdk.model.container import deployment_strategy_pb2 as container__sdk_dot_model_dot_container_dot_deployment__strategy__pb2
from container_sdk.model.container import local_object_reference_pb2 as container__sdk_dot_model_dot_container_dot_local__object__reference__pb2
from container_sdk.model.container import deployment_status_pb2 as container__sdk_dot_model_dot_container_dot_deployment__status__pb2
from container_sdk.model.container import workload_pb2 as container__sdk_dot_model_dot_container_dot_workload__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='update_resource_spec.proto',
  package='workload',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1aupdate_resource_spec.proto\x12\x08workload\x1a-container_sdk/model/container/container.proto\x1a*container_sdk/model/container/volume.proto\x1a\x37\x63ontainer_sdk/model/container/deployment_strategy.proto\x1a:container_sdk/model/container/local_object_reference.proto\x1a\x35\x63ontainer_sdk/model/container/deployment_status.proto\x1a,container_sdk/model/container/workload.proto\x1a\x1cgoogle/protobuf/struct.proto\"E\n\x19UpdateResourceSpecRequest\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x14\n\x0cresourceSpec\x18\x02 \x01(\t\"x\n!UpdateResourceSpecResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12!\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x13.container.Workloadb\x06proto3')
  ,
  dependencies=[container__sdk_dot_model_dot_container_dot_container__pb2.DESCRIPTOR,container__sdk_dot_model_dot_container_dot_volume__pb2.DESCRIPTOR,container__sdk_dot_model_dot_container_dot_deployment__strategy__pb2.DESCRIPTOR,container__sdk_dot_model_dot_container_dot_local__object__reference__pb2.DESCRIPTOR,container__sdk_dot_model_dot_container_dot_deployment__status__pb2.DESCRIPTOR,container__sdk_dot_model_dot_container_dot_workload__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_UPDATERESOURCESPECREQUEST = _descriptor.Descriptor(
  name='UpdateResourceSpecRequest',
  full_name='workload.UpdateResourceSpecRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='workload.UpdateResourceSpecRequest.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resourceSpec', full_name='workload.UpdateResourceSpecRequest.resourceSpec', index=1,
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
  serialized_start=379,
  serialized_end=448,
)


_UPDATERESOURCESPECRESPONSEWRAPPER = _descriptor.Descriptor(
  name='UpdateResourceSpecResponseWrapper',
  full_name='workload.UpdateResourceSpecResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='workload.UpdateResourceSpecResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='workload.UpdateResourceSpecResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='workload.UpdateResourceSpecResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='workload.UpdateResourceSpecResponseWrapper.data', index=3,
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
  serialized_start=450,
  serialized_end=570,
)

_UPDATERESOURCESPECRESPONSEWRAPPER.fields_by_name['data'].message_type = container__sdk_dot_model_dot_container_dot_workload__pb2._WORKLOAD
DESCRIPTOR.message_types_by_name['UpdateResourceSpecRequest'] = _UPDATERESOURCESPECREQUEST
DESCRIPTOR.message_types_by_name['UpdateResourceSpecResponseWrapper'] = _UPDATERESOURCESPECRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateResourceSpecRequest = _reflection.GeneratedProtocolMessageType('UpdateResourceSpecRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATERESOURCESPECREQUEST,
  '__module__' : 'update_resource_spec_pb2'
  # @@protoc_insertion_point(class_scope:workload.UpdateResourceSpecRequest)
  })
_sym_db.RegisterMessage(UpdateResourceSpecRequest)

UpdateResourceSpecResponseWrapper = _reflection.GeneratedProtocolMessageType('UpdateResourceSpecResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _UPDATERESOURCESPECRESPONSEWRAPPER,
  '__module__' : 'update_resource_spec_pb2'
  # @@protoc_insertion_point(class_scope:workload.UpdateResourceSpecResponseWrapper)
  })
_sym_db.RegisterMessage(UpdateResourceSpecResponseWrapper)


# @@protoc_insertion_point(module_scope)
