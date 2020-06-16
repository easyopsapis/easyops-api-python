# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: import_storyboard_node.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from influxdb_service_sdk.model.next_builder import storyboard_brick_pb2 as influxdb__service__sdk_dot_model_dot_next__builder_dot_storyboard__brick__pb2
from influxdb_service_sdk.model.next_builder import storyboard_route_pb2 as influxdb__service__sdk_dot_model_dot_next__builder_dot_storyboard__route__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='import_storyboard_node.proto',
  package='next_builder',
  syntax='proto3',
  serialized_options=_b('ZFgo.easyops.local/contracts/protorepo-models/easyops/model/next_builder'),
  serialized_pb=_b('\n\x1cimport_storyboard_node.proto\x12\x0cnext_builder\x1a>influxdb_service_sdk/model/next_builder/storyboard_brick.proto\x1a>influxdb_service_sdk/model/next_builder/storyboard_route.proto\"\xf9\x02\n\x14ImportStoryboardNode\x12;\n\x07project\x18\x01 \x01(\x0b\x32*.next_builder.ImportStoryboardNode.Project\x12\x39\n\x06parent\x18\x02 \x01(\x0b\x32).next_builder.ImportStoryboardNode.Parent\x12\n\n\x02id\x18\x03 \x01(\t\x12\r\n\x05\x61lias\x18\x04 \x01(\t\x12\r\n\x05\x61ppId\x18\x05 \x01(\t\x12\x12\n\nmountPoint\x18\x06 \x01(\t\x12\x0c\n\x04sort\x18\x07 \x01(\x05\x12\x0c\n\x04type\x18\x08 \x01(\t\x12,\n\x05\x62rick\x18\t \x01(\x0b\x32\x1d.next_builder.StoryboardBrick\x12,\n\x05route\x18\n \x01(\x0b\x32\x1d.next_builder.StoryboardRoute\x1a\x1d\n\x07Project\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x1a\x14\n\x06Parent\x12\n\n\x02id\x18\x01 \x01(\tBHZFgo.easyops.local/contracts/protorepo-models/easyops/model/next_builderb\x06proto3')
  ,
  dependencies=[influxdb__service__sdk_dot_model_dot_next__builder_dot_storyboard__brick__pb2.DESCRIPTOR,influxdb__service__sdk_dot_model_dot_next__builder_dot_storyboard__route__pb2.DESCRIPTOR,])




_IMPORTSTORYBOARDNODE_PROJECT = _descriptor.Descriptor(
  name='Project',
  full_name='next_builder.ImportStoryboardNode.Project',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='next_builder.ImportStoryboardNode.Project.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=501,
  serialized_end=530,
)

_IMPORTSTORYBOARDNODE_PARENT = _descriptor.Descriptor(
  name='Parent',
  full_name='next_builder.ImportStoryboardNode.Parent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='next_builder.ImportStoryboardNode.Parent.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=532,
  serialized_end=552,
)

_IMPORTSTORYBOARDNODE = _descriptor.Descriptor(
  name='ImportStoryboardNode',
  full_name='next_builder.ImportStoryboardNode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project', full_name='next_builder.ImportStoryboardNode.project', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent', full_name='next_builder.ImportStoryboardNode.parent', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='next_builder.ImportStoryboardNode.id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alias', full_name='next_builder.ImportStoryboardNode.alias', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='appId', full_name='next_builder.ImportStoryboardNode.appId', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mountPoint', full_name='next_builder.ImportStoryboardNode.mountPoint', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sort', full_name='next_builder.ImportStoryboardNode.sort', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='next_builder.ImportStoryboardNode.type', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='brick', full_name='next_builder.ImportStoryboardNode.brick', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='route', full_name='next_builder.ImportStoryboardNode.route', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_IMPORTSTORYBOARDNODE_PROJECT, _IMPORTSTORYBOARDNODE_PARENT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=175,
  serialized_end=552,
)

_IMPORTSTORYBOARDNODE_PROJECT.containing_type = _IMPORTSTORYBOARDNODE
_IMPORTSTORYBOARDNODE_PARENT.containing_type = _IMPORTSTORYBOARDNODE
_IMPORTSTORYBOARDNODE.fields_by_name['project'].message_type = _IMPORTSTORYBOARDNODE_PROJECT
_IMPORTSTORYBOARDNODE.fields_by_name['parent'].message_type = _IMPORTSTORYBOARDNODE_PARENT
_IMPORTSTORYBOARDNODE.fields_by_name['brick'].message_type = influxdb__service__sdk_dot_model_dot_next__builder_dot_storyboard__brick__pb2._STORYBOARDBRICK
_IMPORTSTORYBOARDNODE.fields_by_name['route'].message_type = influxdb__service__sdk_dot_model_dot_next__builder_dot_storyboard__route__pb2._STORYBOARDROUTE
DESCRIPTOR.message_types_by_name['ImportStoryboardNode'] = _IMPORTSTORYBOARDNODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImportStoryboardNode = _reflection.GeneratedProtocolMessageType('ImportStoryboardNode', (_message.Message,), {

  'Project' : _reflection.GeneratedProtocolMessageType('Project', (_message.Message,), {
    'DESCRIPTOR' : _IMPORTSTORYBOARDNODE_PROJECT,
    '__module__' : 'import_storyboard_node_pb2'
    # @@protoc_insertion_point(class_scope:next_builder.ImportStoryboardNode.Project)
    })
  ,

  'Parent' : _reflection.GeneratedProtocolMessageType('Parent', (_message.Message,), {
    'DESCRIPTOR' : _IMPORTSTORYBOARDNODE_PARENT,
    '__module__' : 'import_storyboard_node_pb2'
    # @@protoc_insertion_point(class_scope:next_builder.ImportStoryboardNode.Parent)
    })
  ,
  'DESCRIPTOR' : _IMPORTSTORYBOARDNODE,
  '__module__' : 'import_storyboard_node_pb2'
  # @@protoc_insertion_point(class_scope:next_builder.ImportStoryboardNode)
  })
_sym_db.RegisterMessage(ImportStoryboardNode)
_sym_db.RegisterMessage(ImportStoryboardNode.Project)
_sym_db.RegisterMessage(ImportStoryboardNode.Parent)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
