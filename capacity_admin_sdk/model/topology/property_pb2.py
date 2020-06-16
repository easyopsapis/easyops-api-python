# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: property.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from capacity_admin_sdk.model.topology import strategy_pb2 as capacity__admin__sdk_dot_model_dot_topology_dot_strategy__pb2
from capacity_admin_sdk.model.topology import cmdb_instance_pb2 as capacity__admin__sdk_dot_model_dot_topology_dot_cmdb__instance__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='property.proto',
  package='topology',
  syntax='proto3',
  serialized_options=_b('ZBgo.easyops.local/contracts/protorepo-models/easyops/model/topology'),
  serialized_pb=_b('\n\x0eproperty.proto\x12\x08topology\x1a\x30\x63\x61pacity_admin_sdk/model/topology/strategy.proto\x1a\x35\x63\x61pacity_admin_sdk/model/topology/cmdb_instance.proto\"\x87\x01\n\x08Property\x12\x10\n\x08objectId\x18\x01 \x01(\t\x12\x12\n\ninstanceId\x18\x02 \x01(\t\x12$\n\x08strategy\x18\x03 \x01(\x0b\x32\x12.topology.Strategy\x12/\n\x0frelateInstances\x18\x04 \x03(\x0b\x32\x16.topology.CmdbInstanceBDZBgo.easyops.local/contracts/protorepo-models/easyops/model/topologyb\x06proto3')
  ,
  dependencies=[capacity__admin__sdk_dot_model_dot_topology_dot_strategy__pb2.DESCRIPTOR,capacity__admin__sdk_dot_model_dot_topology_dot_cmdb__instance__pb2.DESCRIPTOR,])




_PROPERTY = _descriptor.Descriptor(
  name='Property',
  full_name='topology.Property',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='objectId', full_name='topology.Property.objectId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='topology.Property.instanceId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strategy', full_name='topology.Property.strategy', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relateInstances', full_name='topology.Property.relateInstances', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=134,
  serialized_end=269,
)

_PROPERTY.fields_by_name['strategy'].message_type = capacity__admin__sdk_dot_model_dot_topology_dot_strategy__pb2._STRATEGY
_PROPERTY.fields_by_name['relateInstances'].message_type = capacity__admin__sdk_dot_model_dot_topology_dot_cmdb__instance__pb2._CMDBINSTANCE
DESCRIPTOR.message_types_by_name['Property'] = _PROPERTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Property = _reflection.GeneratedProtocolMessageType('Property', (_message.Message,), {
  'DESCRIPTOR' : _PROPERTY,
  '__module__' : 'property_pb2'
  # @@protoc_insertion_point(class_scope:topology.Property)
  })
_sym_db.RegisterMessage(Property)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
