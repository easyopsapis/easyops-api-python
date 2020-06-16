# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: node.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ens_sdk.model.topology import property_pb2 as ens__sdk_dot_model_dot_topology_dot_property__pb2
from ens_sdk.model.topology import nodeStyle_pb2 as ens__sdk_dot_model_dot_topology_dot_nodeStyle__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='node.proto',
  package='topology',
  syntax='proto3',
  serialized_options=_b('ZBgo.easyops.local/contracts/protorepo-models/easyops/model/topology'),
  serialized_pb=_b('\n\nnode.proto\x12\x08topology\x1a%ens_sdk/model/topology/property.proto\x1a&ens_sdk/model/topology/nodeStyle.proto\"\xa6\x01\n\x04Node\x12\r\n\x05label\x18\x01 \x03(\t\x12\x12\n\ndataSource\x18\x02 \x01(\t\x12\x13\n\x0brelateNodes\x18\x03 \x03(\t\x12\n\n\x02id\x18\x04 \x01(\t\x12$\n\x08property\x18\x05 \x01(\x0b\x32\x12.topology.Property\x12\x10\n\x08\x63ollapse\x18\x06 \x01(\x08\x12\"\n\x05style\x18\x07 \x01(\x0b\x32\x13.topology.NodeStyleBDZBgo.easyops.local/contracts/protorepo-models/easyops/model/topologyb\x06proto3')
  ,
  dependencies=[ens__sdk_dot_model_dot_topology_dot_property__pb2.DESCRIPTOR,ens__sdk_dot_model_dot_topology_dot_nodeStyle__pb2.DESCRIPTOR,])




_NODE = _descriptor.Descriptor(
  name='Node',
  full_name='topology.Node',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='topology.Node.label', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataSource', full_name='topology.Node.dataSource', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relateNodes', full_name='topology.Node.relateNodes', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='topology.Node.id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='property', full_name='topology.Node.property', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collapse', full_name='topology.Node.collapse', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='style', full_name='topology.Node.style', index=6,
      number=7, type=11, cpp_type=10, label=1,
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
  serialized_start=104,
  serialized_end=270,
)

_NODE.fields_by_name['property'].message_type = ens__sdk_dot_model_dot_topology_dot_property__pb2._PROPERTY
_NODE.fields_by_name['style'].message_type = ens__sdk_dot_model_dot_topology_dot_nodeStyle__pb2._NODESTYLE
DESCRIPTOR.message_types_by_name['Node'] = _NODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Node = _reflection.GeneratedProtocolMessageType('Node', (_message.Message,), {
  'DESCRIPTOR' : _NODE,
  '__module__' : 'node_pb2'
  # @@protoc_insertion_point(class_scope:topology.Node)
  })
_sym_db.RegisterMessage(Node)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
