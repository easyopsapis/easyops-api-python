# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: instance_tree_search.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from model.cmdb import instance_tree_root_node_pb2 as model_dot_cmdb_dot_instance__tree__root__node__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='instance_tree_search.proto',
  package='instance_tree',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1ainstance_tree_search.proto\x12\rinstance_tree\x1a(model/cmdb/instance_tree_root_node.proto\x1a\x1cgoogle/protobuf/struct.proto\"\x84\x01\n\x19InstanceTreeSearchRequest\x12(\n\x04tree\x18\x01 \x01(\x0b\x32\x1a.cmdb.InstanceTreeRootNode\x12\x15\n\rignore_single\x18\x02 \x01(\x08\x12&\n\x05query\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\"|\n!InstanceTreeSearchResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12%\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Structb\x06proto3')
  ,
  dependencies=[model_dot_cmdb_dot_instance__tree__root__node__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_INSTANCETREESEARCHREQUEST = _descriptor.Descriptor(
  name='InstanceTreeSearchRequest',
  full_name='instance_tree.InstanceTreeSearchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tree', full_name='instance_tree.InstanceTreeSearchRequest.tree', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ignore_single', full_name='instance_tree.InstanceTreeSearchRequest.ignore_single', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='query', full_name='instance_tree.InstanceTreeSearchRequest.query', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=118,
  serialized_end=250,
)


_INSTANCETREESEARCHRESPONSEWRAPPER = _descriptor.Descriptor(
  name='InstanceTreeSearchResponseWrapper',
  full_name='instance_tree.InstanceTreeSearchResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='instance_tree.InstanceTreeSearchResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='instance_tree.InstanceTreeSearchResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='instance_tree.InstanceTreeSearchResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='instance_tree.InstanceTreeSearchResponseWrapper.data', index=3,
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
  serialized_start=252,
  serialized_end=376,
)

_INSTANCETREESEARCHREQUEST.fields_by_name['tree'].message_type = model_dot_cmdb_dot_instance__tree__root__node__pb2._INSTANCETREEROOTNODE
_INSTANCETREESEARCHREQUEST.fields_by_name['query'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_INSTANCETREESEARCHRESPONSEWRAPPER.fields_by_name['data'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['InstanceTreeSearchRequest'] = _INSTANCETREESEARCHREQUEST
DESCRIPTOR.message_types_by_name['InstanceTreeSearchResponseWrapper'] = _INSTANCETREESEARCHRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InstanceTreeSearchRequest = _reflection.GeneratedProtocolMessageType('InstanceTreeSearchRequest', (_message.Message,), dict(
  DESCRIPTOR = _INSTANCETREESEARCHREQUEST,
  __module__ = 'instance_tree_search_pb2'
  # @@protoc_insertion_point(class_scope:instance_tree.InstanceTreeSearchRequest)
  ))
_sym_db.RegisterMessage(InstanceTreeSearchRequest)

InstanceTreeSearchResponseWrapper = _reflection.GeneratedProtocolMessageType('InstanceTreeSearchResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _INSTANCETREESEARCHRESPONSEWRAPPER,
  __module__ = 'instance_tree_search_pb2'
  # @@protoc_insertion_point(class_scope:instance_tree.InstanceTreeSearchResponseWrapper)
  ))
_sym_db.RegisterMessage(InstanceTreeSearchResponseWrapper)


# @@protoc_insertion_point(module_scope)
