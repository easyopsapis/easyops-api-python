# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sort_storyboard.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from next_builder_sdk.model.next_builder import storyboard_node_pb2 as next__builder__sdk_dot_model_dot_next__builder_dot_storyboard__node__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sort_storyboard.proto',
  package='storyboard',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x15sort_storyboard.proto\x12\nstoryboard\x1a\x39next_builder_sdk/model/next_builder/storyboard_node.proto\"\x92\x01\n\x1aSortStoryboardNodesRequest\x12;\n\x05nodes\x18\x01 \x03(\x0b\x32,.storyboard.SortStoryboardNodesRequest.Nodes\x1a\x37\n\x05Nodes\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0c\n\x04sort\x18\x03 \x01(\x05\"J\n\x1bSortStoryboardNodesResponse\x12+\n\x05nodes\x18\x01 \x03(\x0b\x32\x1c.next_builder.StoryboardNode\"\x8d\x01\n\"SortStoryboardNodesResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x35\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\'.storyboard.SortStoryboardNodesResponseb\x06proto3')
  ,
  dependencies=[next__builder__sdk_dot_model_dot_next__builder_dot_storyboard__node__pb2.DESCRIPTOR,])




_SORTSTORYBOARDNODESREQUEST_NODES = _descriptor.Descriptor(
  name='Nodes',
  full_name='storyboard.SortStoryboardNodesRequest.Nodes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='storyboard.SortStoryboardNodesRequest.Nodes.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='storyboard.SortStoryboardNodesRequest.Nodes.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sort', full_name='storyboard.SortStoryboardNodesRequest.Nodes.sort', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=188,
  serialized_end=243,
)

_SORTSTORYBOARDNODESREQUEST = _descriptor.Descriptor(
  name='SortStoryboardNodesRequest',
  full_name='storyboard.SortStoryboardNodesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodes', full_name='storyboard.SortStoryboardNodesRequest.nodes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SORTSTORYBOARDNODESREQUEST_NODES, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=97,
  serialized_end=243,
)


_SORTSTORYBOARDNODESRESPONSE = _descriptor.Descriptor(
  name='SortStoryboardNodesResponse',
  full_name='storyboard.SortStoryboardNodesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodes', full_name='storyboard.SortStoryboardNodesResponse.nodes', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=245,
  serialized_end=319,
)


_SORTSTORYBOARDNODESRESPONSEWRAPPER = _descriptor.Descriptor(
  name='SortStoryboardNodesResponseWrapper',
  full_name='storyboard.SortStoryboardNodesResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='storyboard.SortStoryboardNodesResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='storyboard.SortStoryboardNodesResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='storyboard.SortStoryboardNodesResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='storyboard.SortStoryboardNodesResponseWrapper.data', index=3,
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
  serialized_start=322,
  serialized_end=463,
)

_SORTSTORYBOARDNODESREQUEST_NODES.containing_type = _SORTSTORYBOARDNODESREQUEST
_SORTSTORYBOARDNODESREQUEST.fields_by_name['nodes'].message_type = _SORTSTORYBOARDNODESREQUEST_NODES
_SORTSTORYBOARDNODESRESPONSE.fields_by_name['nodes'].message_type = next__builder__sdk_dot_model_dot_next__builder_dot_storyboard__node__pb2._STORYBOARDNODE
_SORTSTORYBOARDNODESRESPONSEWRAPPER.fields_by_name['data'].message_type = _SORTSTORYBOARDNODESRESPONSE
DESCRIPTOR.message_types_by_name['SortStoryboardNodesRequest'] = _SORTSTORYBOARDNODESREQUEST
DESCRIPTOR.message_types_by_name['SortStoryboardNodesResponse'] = _SORTSTORYBOARDNODESRESPONSE
DESCRIPTOR.message_types_by_name['SortStoryboardNodesResponseWrapper'] = _SORTSTORYBOARDNODESRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SortStoryboardNodesRequest = _reflection.GeneratedProtocolMessageType('SortStoryboardNodesRequest', (_message.Message,), {

  'Nodes' : _reflection.GeneratedProtocolMessageType('Nodes', (_message.Message,), {
    'DESCRIPTOR' : _SORTSTORYBOARDNODESREQUEST_NODES,
    '__module__' : 'sort_storyboard_pb2'
    # @@protoc_insertion_point(class_scope:storyboard.SortStoryboardNodesRequest.Nodes)
    })
  ,
  'DESCRIPTOR' : _SORTSTORYBOARDNODESREQUEST,
  '__module__' : 'sort_storyboard_pb2'
  # @@protoc_insertion_point(class_scope:storyboard.SortStoryboardNodesRequest)
  })
_sym_db.RegisterMessage(SortStoryboardNodesRequest)
_sym_db.RegisterMessage(SortStoryboardNodesRequest.Nodes)

SortStoryboardNodesResponse = _reflection.GeneratedProtocolMessageType('SortStoryboardNodesResponse', (_message.Message,), {
  'DESCRIPTOR' : _SORTSTORYBOARDNODESRESPONSE,
  '__module__' : 'sort_storyboard_pb2'
  # @@protoc_insertion_point(class_scope:storyboard.SortStoryboardNodesResponse)
  })
_sym_db.RegisterMessage(SortStoryboardNodesResponse)

SortStoryboardNodesResponseWrapper = _reflection.GeneratedProtocolMessageType('SortStoryboardNodesResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _SORTSTORYBOARDNODESRESPONSEWRAPPER,
  '__module__' : 'sort_storyboard_pb2'
  # @@protoc_insertion_point(class_scope:storyboard.SortStoryboardNodesResponseWrapper)
  })
_sym_db.RegisterMessage(SortStoryboardNodesResponseWrapper)


# @@protoc_insertion_point(module_scope)
