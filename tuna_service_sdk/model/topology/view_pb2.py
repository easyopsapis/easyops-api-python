# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: view.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tuna_service_sdk.model.topology import node_pb2 as tuna__service__sdk_dot_model_dot_topology_dot_node__pb2
from tuna_service_sdk.model.topology import link_pb2 as tuna__service__sdk_dot_model_dot_topology_dot_link__pb2
from tuna_service_sdk.model.topology import area_pb2 as tuna__service__sdk_dot_model_dot_topology_dot_area__pb2
from tuna_service_sdk.model.topology import note_pb2 as tuna__service__sdk_dot_model_dot_topology_dot_note__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='view.proto',
  package='topology',
  syntax='proto3',
  serialized_options=_b('ZBgo.easyops.local/contracts/protorepo-models/easyops/model/topology'),
  serialized_pb=_b('\n\nview.proto\x12\x08topology\x1a*tuna_service_sdk/model/topology/node.proto\x1a*tuna_service_sdk/model/topology/link.proto\x1a*tuna_service_sdk/model/topology/area.proto\x1a*tuna_service_sdk/model/topology/note.proto\"\xfd\x03\n\x04View\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07\x63reator\x18\x03 \x01(\t\x12\x10\n\x08modifier\x18\x04 \x01(\t\x12\x17\n\x0freadAuthorizers\x18\x05 \x03(\t\x12\x18\n\x10writeAuthorizers\x18\x06 \x03(\t\x12\x0f\n\x07version\x18\x07 \x01(\t\x12\r\n\x05\x63time\x18\x08 \x01(\x05\x12\r\n\x05mtime\x18\t \x01(\x05\x12 \n\x08rootNode\x18\n \x01(\x0b\x32\x0e.topology.Node\x12\x1d\n\x05nodes\x18\x0b \x03(\x0b\x32\x0e.topology.Node\x12\x1d\n\x05links\x18\x0c \x03(\x0b\x32\x0e.topology.Link\x12\x1d\n\x05\x61reas\x18\r \x03(\x0b\x32\x0e.topology.Area\x12\x1d\n\x05notes\x18\x0e \x03(\x0b\x32\x0e.topology.Note\x12!\n\x04\x64iff\x18\x0f \x01(\x0b\x32\x13.topology.View.Diff\x1a\x94\x01\n\x04\x44iff\x12 \n\x08\x61\x64\x64Nodes\x18\x01 \x03(\x0b\x32\x0e.topology.Node\x12#\n\x0bremoveNodes\x18\x02 \x03(\x0b\x32\x0e.topology.Node\x12 \n\x08\x61\x64\x64Links\x18\x03 \x03(\x0b\x32\x0e.topology.Link\x12#\n\x0bremoveLinks\x18\x04 \x03(\x0b\x32\x0e.topology.LinkBDZBgo.easyops.local/contracts/protorepo-models/easyops/model/topologyb\x06proto3')
  ,
  dependencies=[tuna__service__sdk_dot_model_dot_topology_dot_node__pb2.DESCRIPTOR,tuna__service__sdk_dot_model_dot_topology_dot_link__pb2.DESCRIPTOR,tuna__service__sdk_dot_model_dot_topology_dot_area__pb2.DESCRIPTOR,tuna__service__sdk_dot_model_dot_topology_dot_note__pb2.DESCRIPTOR,])




_VIEW_DIFF = _descriptor.Descriptor(
  name='Diff',
  full_name='topology.View.Diff',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='addNodes', full_name='topology.View.Diff.addNodes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='removeNodes', full_name='topology.View.Diff.removeNodes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='addLinks', full_name='topology.View.Diff.addLinks', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='removeLinks', full_name='topology.View.Diff.removeLinks', index=3,
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
  serialized_start=562,
  serialized_end=710,
)

_VIEW = _descriptor.Descriptor(
  name='View',
  full_name='topology.View',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='topology.View.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='topology.View.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='topology.View.creator', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='modifier', full_name='topology.View.modifier', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readAuthorizers', full_name='topology.View.readAuthorizers', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='writeAuthorizers', full_name='topology.View.writeAuthorizers', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='topology.View.version', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='topology.View.ctime', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='topology.View.mtime', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rootNode', full_name='topology.View.rootNode', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nodes', full_name='topology.View.nodes', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='links', full_name='topology.View.links', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='areas', full_name='topology.View.areas', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='notes', full_name='topology.View.notes', index=13,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='diff', full_name='topology.View.diff', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_VIEW_DIFF, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=201,
  serialized_end=710,
)

_VIEW_DIFF.fields_by_name['addNodes'].message_type = tuna__service__sdk_dot_model_dot_topology_dot_node__pb2._NODE
_VIEW_DIFF.fields_by_name['removeNodes'].message_type = tuna__service__sdk_dot_model_dot_topology_dot_node__pb2._NODE
_VIEW_DIFF.fields_by_name['addLinks'].message_type = tuna__service__sdk_dot_model_dot_topology_dot_link__pb2._LINK
_VIEW_DIFF.fields_by_name['removeLinks'].message_type = tuna__service__sdk_dot_model_dot_topology_dot_link__pb2._LINK
_VIEW_DIFF.containing_type = _VIEW
_VIEW.fields_by_name['rootNode'].message_type = tuna__service__sdk_dot_model_dot_topology_dot_node__pb2._NODE
_VIEW.fields_by_name['nodes'].message_type = tuna__service__sdk_dot_model_dot_topology_dot_node__pb2._NODE
_VIEW.fields_by_name['links'].message_type = tuna__service__sdk_dot_model_dot_topology_dot_link__pb2._LINK
_VIEW.fields_by_name['areas'].message_type = tuna__service__sdk_dot_model_dot_topology_dot_area__pb2._AREA
_VIEW.fields_by_name['notes'].message_type = tuna__service__sdk_dot_model_dot_topology_dot_note__pb2._NOTE
_VIEW.fields_by_name['diff'].message_type = _VIEW_DIFF
DESCRIPTOR.message_types_by_name['View'] = _VIEW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

View = _reflection.GeneratedProtocolMessageType('View', (_message.Message,), {

  'Diff' : _reflection.GeneratedProtocolMessageType('Diff', (_message.Message,), {
    'DESCRIPTOR' : _VIEW_DIFF,
    '__module__' : 'view_pb2'
    # @@protoc_insertion_point(class_scope:topology.View.Diff)
    })
  ,
  'DESCRIPTOR' : _VIEW,
  '__module__' : 'view_pb2'
  # @@protoc_insertion_point(class_scope:topology.View)
  })
_sym_db.RegisterMessage(View)
_sym_db.RegisterMessage(View.Diff)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
