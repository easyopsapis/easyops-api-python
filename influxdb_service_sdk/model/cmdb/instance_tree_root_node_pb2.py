# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: instance_tree_root_node.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from influxdb_service_sdk.model.cmdb import instance_tree_child_node_pb2 as influxdb__service__sdk_dot_model_dot_cmdb_dot_instance__tree__child__node__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='instance_tree_root_node.proto',
  package='cmdb',
  syntax='proto3',
  serialized_options=_b('Z>go.easyops.local/contracts/protorepo-models/easyops/model/cmdb'),
  serialized_pb=_b('\n\x1dinstance_tree_root_node.proto\x12\x04\x63mdb\x1a>influxdb_service_sdk/model/cmdb/instance_tree_child_node.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xa6\x01\n\x14InstanceTreeRootNode\x12\x11\n\tobject_id\x18\x01 \x01(\t\x12&\n\x05query\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\'\n\x06\x66ields\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12*\n\x05\x63hild\x18\x04 \x03(\x0b\x32\x1b.cmdb.InstanceTreeChildNodeB@Z>go.easyops.local/contracts/protorepo-models/easyops/model/cmdbb\x06proto3')
  ,
  dependencies=[influxdb__service__sdk_dot_model_dot_cmdb_dot_instance__tree__child__node__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_INSTANCETREEROOTNODE = _descriptor.Descriptor(
  name='InstanceTreeRootNode',
  full_name='cmdb.InstanceTreeRootNode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_id', full_name='cmdb.InstanceTreeRootNode.object_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='query', full_name='cmdb.InstanceTreeRootNode.query', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fields', full_name='cmdb.InstanceTreeRootNode.fields', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='child', full_name='cmdb.InstanceTreeRootNode.child', index=3,
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
  serialized_end=300,
)

_INSTANCETREEROOTNODE.fields_by_name['query'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_INSTANCETREEROOTNODE.fields_by_name['fields'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_INSTANCETREEROOTNODE.fields_by_name['child'].message_type = influxdb__service__sdk_dot_model_dot_cmdb_dot_instance__tree__child__node__pb2._INSTANCETREECHILDNODE
DESCRIPTOR.message_types_by_name['InstanceTreeRootNode'] = _INSTANCETREEROOTNODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InstanceTreeRootNode = _reflection.GeneratedProtocolMessageType('InstanceTreeRootNode', (_message.Message,), {
  'DESCRIPTOR' : _INSTANCETREEROOTNODE,
  '__module__' : 'instance_tree_root_node_pb2'
  # @@protoc_insertion_point(class_scope:cmdb.InstanceTreeRootNode)
  })
_sym_db.RegisterMessage(InstanceTreeRootNode)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
