# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: link.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from easy_command_sdk.model.topology import linkStyle_pb2 as easy__command__sdk_dot_model_dot_topology_dot_linkStyle__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='link.proto',
  package='topology',
  syntax='proto3',
  serialized_options=_b('ZBgo.easyops.local/contracts/protorepo-models/easyops/model/topology'),
  serialized_pb=_b('\n\nlink.proto\x12\x08topology\x1a/easy_command_sdk/model/topology/linkStyle.proto\"J\n\x04Link\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x0e\n\x06target\x18\x02 \x01(\t\x12\"\n\x05style\x18\x03 \x01(\x0b\x32\x13.topology.LinkStyleBDZBgo.easyops.local/contracts/protorepo-models/easyops/model/topologyb\x06proto3')
  ,
  dependencies=[easy__command__sdk_dot_model_dot_topology_dot_linkStyle__pb2.DESCRIPTOR,])




_LINK = _descriptor.Descriptor(
  name='Link',
  full_name='topology.Link',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='topology.Link.source', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target', full_name='topology.Link.target', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='style', full_name='topology.Link.style', index=2,
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
  serialized_start=73,
  serialized_end=147,
)

_LINK.fields_by_name['style'].message_type = easy__command__sdk_dot_model_dot_topology_dot_linkStyle__pb2._LINKSTYLE
DESCRIPTOR.message_types_by_name['Link'] = _LINK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Link = _reflection.GeneratedProtocolMessageType('Link', (_message.Message,), {
  'DESCRIPTOR' : _LINK,
  '__module__' : 'link_pb2'
  # @@protoc_insertion_point(class_scope:topology.Link)
  })
_sym_db.RegisterMessage(Link)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
