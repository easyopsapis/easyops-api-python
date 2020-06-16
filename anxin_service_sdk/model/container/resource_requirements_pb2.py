# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: resource_requirements.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from anxin_service_sdk.model.container import resource_list_pb2 as anxin__service__sdk_dot_model_dot_container_dot_resource__list__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='resource_requirements.proto',
  package='container',
  syntax='proto3',
  serialized_options=_b('ZCgo.easyops.local/contracts/protorepo-models/easyops/model/container'),
  serialized_pb=_b('\n\x1bresource_requirements.proto\x12\tcontainer\x1a\x35\x61nxin_service_sdk/model/container/resource_list.proto\"j\n\x14ResourceRequirements\x12\'\n\x06limits\x18\x01 \x01(\x0b\x32\x17.container.ResourceList\x12)\n\x08requests\x18\x02 \x01(\x0b\x32\x17.container.ResourceListBEZCgo.easyops.local/contracts/protorepo-models/easyops/model/containerb\x06proto3')
  ,
  dependencies=[anxin__service__sdk_dot_model_dot_container_dot_resource__list__pb2.DESCRIPTOR,])




_RESOURCEREQUIREMENTS = _descriptor.Descriptor(
  name='ResourceRequirements',
  full_name='container.ResourceRequirements',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='limits', full_name='container.ResourceRequirements.limits', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requests', full_name='container.ResourceRequirements.requests', index=1,
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
  serialized_start=97,
  serialized_end=203,
)

_RESOURCEREQUIREMENTS.fields_by_name['limits'].message_type = anxin__service__sdk_dot_model_dot_container_dot_resource__list__pb2._RESOURCELIST
_RESOURCEREQUIREMENTS.fields_by_name['requests'].message_type = anxin__service__sdk_dot_model_dot_container_dot_resource__list__pb2._RESOURCELIST
DESCRIPTOR.message_types_by_name['ResourceRequirements'] = _RESOURCEREQUIREMENTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResourceRequirements = _reflection.GeneratedProtocolMessageType('ResourceRequirements', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCEREQUIREMENTS,
  '__module__' : 'resource_requirements_pb2'
  # @@protoc_insertion_point(class_scope:container.ResourceRequirements)
  })
_sym_db.RegisterMessage(ResourceRequirements)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
