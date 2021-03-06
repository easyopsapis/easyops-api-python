# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: storyboard_node.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from metadata_center_sdk.model.next_builder import storyboard_brick_pb2 as metadata__center__sdk_dot_model_dot_next__builder_dot_storyboard__brick__pb2
from metadata_center_sdk.model.next_builder import storyboard_route_pb2 as metadata__center__sdk_dot_model_dot_next__builder_dot_storyboard__route__pb2
from metadata_center_sdk.model.next_builder import micro_app_project_pb2 as metadata__center__sdk_dot_model_dot_next__builder_dot_micro__app__project__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='storyboard_node.proto',
  package='next_builder',
  syntax='proto3',
  serialized_options=_b('ZFgo.easyops.local/contracts/protorepo-models/easyops/model/next_builder'),
  serialized_pb=_b('\n\x15storyboard_node.proto\x12\x0cnext_builder\x1a=metadata_center_sdk/model/next_builder/storyboard_brick.proto\x1a=metadata_center_sdk/model/next_builder/storyboard_route.proto\x1a>metadata_center_sdk/model/next_builder/micro_app_project.proto\"\xe8\x02\n\x0eStoryboardNode\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\r\n\x05\x61lias\x18\x02 \x01(\t\x12\r\n\x05\x61ppId\x18\x03 \x01(\t\x12\n\n\x02id\x18\x04 \x01(\t\x12\x12\n\nmountPoint\x18\x05 \x01(\t\x12\x0c\n\x04sort\x18\x06 \x01(\x05\x12\x0c\n\x04type\x18\x07 \x01(\t\x12,\n\x05\x62rick\x18\x08 \x01(\x0b\x32\x1d.next_builder.StoryboardBrick\x12,\n\x05route\x18\t \x01(\x0b\x32\x1d.next_builder.StoryboardRoute\x12.\n\x07project\x18\n \x01(\x0b\x32\x1d.next_builder.MicroAppProject\x12,\n\x06parent\x18\x0b \x01(\x0b\x32\x1c.next_builder.StoryboardNode\x12.\n\x08\x63hildren\x18\x0c \x03(\x0b\x32\x1c.next_builder.StoryboardNodeBHZFgo.easyops.local/contracts/protorepo-models/easyops/model/next_builderb\x06proto3')
  ,
  dependencies=[metadata__center__sdk_dot_model_dot_next__builder_dot_storyboard__brick__pb2.DESCRIPTOR,metadata__center__sdk_dot_model_dot_next__builder_dot_storyboard__route__pb2.DESCRIPTOR,metadata__center__sdk_dot_model_dot_next__builder_dot_micro__app__project__pb2.DESCRIPTOR,])




_STORYBOARDNODE = _descriptor.Descriptor(
  name='StoryboardNode',
  full_name='next_builder.StoryboardNode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='next_builder.StoryboardNode.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alias', full_name='next_builder.StoryboardNode.alias', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='appId', full_name='next_builder.StoryboardNode.appId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='next_builder.StoryboardNode.id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mountPoint', full_name='next_builder.StoryboardNode.mountPoint', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sort', full_name='next_builder.StoryboardNode.sort', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='next_builder.StoryboardNode.type', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='brick', full_name='next_builder.StoryboardNode.brick', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='route', full_name='next_builder.StoryboardNode.route', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='project', full_name='next_builder.StoryboardNode.project', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent', full_name='next_builder.StoryboardNode.parent', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='children', full_name='next_builder.StoryboardNode.children', index=11,
      number=12, type=11, cpp_type=10, label=3,
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
  serialized_start=230,
  serialized_end=590,
)

_STORYBOARDNODE.fields_by_name['brick'].message_type = metadata__center__sdk_dot_model_dot_next__builder_dot_storyboard__brick__pb2._STORYBOARDBRICK
_STORYBOARDNODE.fields_by_name['route'].message_type = metadata__center__sdk_dot_model_dot_next__builder_dot_storyboard__route__pb2._STORYBOARDROUTE
_STORYBOARDNODE.fields_by_name['project'].message_type = metadata__center__sdk_dot_model_dot_next__builder_dot_micro__app__project__pb2._MICROAPPPROJECT
_STORYBOARDNODE.fields_by_name['parent'].message_type = _STORYBOARDNODE
_STORYBOARDNODE.fields_by_name['children'].message_type = _STORYBOARDNODE
DESCRIPTOR.message_types_by_name['StoryboardNode'] = _STORYBOARDNODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StoryboardNode = _reflection.GeneratedProtocolMessageType('StoryboardNode', (_message.Message,), {
  'DESCRIPTOR' : _STORYBOARDNODE,
  '__module__' : 'storyboard_node_pb2'
  # @@protoc_insertion_point(class_scope:next_builder.StoryboardNode)
  })
_sym_db.RegisterMessage(StoryboardNode)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
