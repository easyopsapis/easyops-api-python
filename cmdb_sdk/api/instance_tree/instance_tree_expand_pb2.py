# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: instance_tree_expand.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cmdb_sdk.model.cmdb import instance_tree_root_node_pb2 as cmdb__sdk_dot_model_dot_cmdb_dot_instance__tree__root__node__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='instance_tree_expand.proto',
  package='instance_tree',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1ainstance_tree_expand.proto\x12\rinstance_tree\x1a\x31\x63mdb_sdk/model/cmdb/instance_tree_root_node.proto\x1a\x1cgoogle/protobuf/struct.proto\"\x83\x01\n\x19InstanceTreeExpandRequest\x12(\n\x04tree\x18\x01 \x01(\x0b\x32\x1a.cmdb.InstanceTreeRootNode\x12\x15\n\rignore_single\x18\x02 \x01(\x08\x12\x11\n\tobject_id\x18\x03 \x01(\t\x12\x12\n\ninstanceId\x18\x04 \x01(\t\"|\n!InstanceTreeExpandResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12%\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Structb\x06proto3')
  ,
  dependencies=[cmdb__sdk_dot_model_dot_cmdb_dot_instance__tree__root__node__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_INSTANCETREEEXPANDREQUEST = _descriptor.Descriptor(
  name='InstanceTreeExpandRequest',
  full_name='instance_tree.InstanceTreeExpandRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tree', full_name='instance_tree.InstanceTreeExpandRequest.tree', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ignore_single', full_name='instance_tree.InstanceTreeExpandRequest.ignore_single', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object_id', full_name='instance_tree.InstanceTreeExpandRequest.object_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='instance_tree.InstanceTreeExpandRequest.instanceId', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=127,
  serialized_end=258,
)


_INSTANCETREEEXPANDRESPONSEWRAPPER = _descriptor.Descriptor(
  name='InstanceTreeExpandResponseWrapper',
  full_name='instance_tree.InstanceTreeExpandResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='instance_tree.InstanceTreeExpandResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='instance_tree.InstanceTreeExpandResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='instance_tree.InstanceTreeExpandResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='instance_tree.InstanceTreeExpandResponseWrapper.data', index=3,
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
  serialized_start=260,
  serialized_end=384,
)

_INSTANCETREEEXPANDREQUEST.fields_by_name['tree'].message_type = cmdb__sdk_dot_model_dot_cmdb_dot_instance__tree__root__node__pb2._INSTANCETREEROOTNODE
_INSTANCETREEEXPANDRESPONSEWRAPPER.fields_by_name['data'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['InstanceTreeExpandRequest'] = _INSTANCETREEEXPANDREQUEST
DESCRIPTOR.message_types_by_name['InstanceTreeExpandResponseWrapper'] = _INSTANCETREEEXPANDRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InstanceTreeExpandRequest = _reflection.GeneratedProtocolMessageType('InstanceTreeExpandRequest', (_message.Message,), {
  'DESCRIPTOR' : _INSTANCETREEEXPANDREQUEST,
  '__module__' : 'instance_tree_expand_pb2'
  # @@protoc_insertion_point(class_scope:instance_tree.InstanceTreeExpandRequest)
  })
_sym_db.RegisterMessage(InstanceTreeExpandRequest)

InstanceTreeExpandResponseWrapper = _reflection.GeneratedProtocolMessageType('InstanceTreeExpandResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _INSTANCETREEEXPANDRESPONSEWRAPPER,
  '__module__' : 'instance_tree_expand_pb2'
  # @@protoc_insertion_point(class_scope:instance_tree.InstanceTreeExpandResponseWrapper)
  })
_sym_db.RegisterMessage(InstanceTreeExpandResponseWrapper)


# @@protoc_insertion_point(module_scope)
