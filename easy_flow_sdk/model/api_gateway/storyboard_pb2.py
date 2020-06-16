# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: storyboard.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from easy_flow_sdk.model.micro_app import installed_micro_app_bootstrap_pb2 as easy__flow__sdk_dot_model_dot_micro__app_dot_installed__micro__app__bootstrap__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='storyboard.proto',
  package='api_gateway',
  syntax='proto3',
  serialized_options=_b('ZEgo.easyops.local/contracts/protorepo-models/easyops/model/api_gateway'),
  serialized_pb=_b('\n\x10storyboard.proto\x12\x0b\x61pi_gateway\x1a\x41\x65\x61sy_flow_sdk/model/micro_app/installed_micro_app_bootstrap.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xa4\x01\n\nStoryBoard\x12\x32\n\x03\x61pp\x18\x01 \x01(\x0b\x32%.micro_app.InstalledMicroAppBootstrap\x12\x12\n\ndependsAll\x18\x02 \x01(\x08\x12\'\n\x06routes\x18\x03 \x03(\x0b\x32\x17.google.protobuf.Struct\x12%\n\x04meta\x18\x04 \x01(\x0b\x32\x17.google.protobuf.StructBGZEgo.easyops.local/contracts/protorepo-models/easyops/model/api_gatewayb\x06proto3')
  ,
  dependencies=[easy__flow__sdk_dot_model_dot_micro__app_dot_installed__micro__app__bootstrap__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_STORYBOARD = _descriptor.Descriptor(
  name='StoryBoard',
  full_name='api_gateway.StoryBoard',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='app', full_name='api_gateway.StoryBoard.app', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dependsAll', full_name='api_gateway.StoryBoard.dependsAll', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='routes', full_name='api_gateway.StoryBoard.routes', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='meta', full_name='api_gateway.StoryBoard.meta', index=3,
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
  serialized_start=131,
  serialized_end=295,
)

_STORYBOARD.fields_by_name['app'].message_type = easy__flow__sdk_dot_model_dot_micro__app_dot_installed__micro__app__bootstrap__pb2._INSTALLEDMICROAPPBOOTSTRAP
_STORYBOARD.fields_by_name['routes'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_STORYBOARD.fields_by_name['meta'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['StoryBoard'] = _STORYBOARD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StoryBoard = _reflection.GeneratedProtocolMessageType('StoryBoard', (_message.Message,), {
  'DESCRIPTOR' : _STORYBOARD,
  '__module__' : 'storyboard_pb2'
  # @@protoc_insertion_point(class_scope:api_gateway.StoryBoard)
  })
_sym_db.RegisterMessage(StoryBoard)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
