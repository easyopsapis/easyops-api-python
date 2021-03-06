# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list_plugin_agent_v1.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='list_plugin_agent_v1.proto',
  package='plugin',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1alist_plugin_agent_v1.proto\x12\x06plugin\"G\n\x19ListPluginAgentsV1Request\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x10\n\x08pageSize\x18\x02 \x01(\x05\x12\n\n\x02id\x18\x03 \x01(\t\"\xe1\x01\n\x1aListPluginAgentsV1Response\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12\x35\n\x04list\x18\x04 \x03(\x0b\x32\'.plugin.ListPluginAgentsV1Response.List\x1a\\\n\x04List\x12\x0f\n\x07\x61gentId\x18\x01 \x01(\t\x12\n\n\x02ip\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\x12\x12\n\ndeployPath\x18\x04 \x03(\t\x12\x13\n\x0bversionName\x18\x05 \x01(\t\"\x87\x01\n!ListPluginAgentsV1ResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x30\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\".plugin.ListPluginAgentsV1Responseb\x06proto3')
)




_LISTPLUGINAGENTSV1REQUEST = _descriptor.Descriptor(
  name='ListPluginAgentsV1Request',
  full_name='plugin.ListPluginAgentsV1Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='plugin.ListPluginAgentsV1Request.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='plugin.ListPluginAgentsV1Request.pageSize', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='plugin.ListPluginAgentsV1Request.id', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=38,
  serialized_end=109,
)


_LISTPLUGINAGENTSV1RESPONSE_LIST = _descriptor.Descriptor(
  name='List',
  full_name='plugin.ListPluginAgentsV1Response.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agentId', full_name='plugin.ListPluginAgentsV1Response.List.agentId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip', full_name='plugin.ListPluginAgentsV1Response.List.ip', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='plugin.ListPluginAgentsV1Response.List.status', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deployPath', full_name='plugin.ListPluginAgentsV1Response.List.deployPath', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionName', full_name='plugin.ListPluginAgentsV1Response.List.versionName', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=245,
  serialized_end=337,
)

_LISTPLUGINAGENTSV1RESPONSE = _descriptor.Descriptor(
  name='ListPluginAgentsV1Response',
  full_name='plugin.ListPluginAgentsV1Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='plugin.ListPluginAgentsV1Response.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='plugin.ListPluginAgentsV1Response.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='plugin.ListPluginAgentsV1Response.total', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='plugin.ListPluginAgentsV1Response.list', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTPLUGINAGENTSV1RESPONSE_LIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=337,
)


_LISTPLUGINAGENTSV1RESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListPluginAgentsV1ResponseWrapper',
  full_name='plugin.ListPluginAgentsV1ResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='plugin.ListPluginAgentsV1ResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='plugin.ListPluginAgentsV1ResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='plugin.ListPluginAgentsV1ResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='plugin.ListPluginAgentsV1ResponseWrapper.data', index=3,
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
  serialized_start=340,
  serialized_end=475,
)

_LISTPLUGINAGENTSV1RESPONSE_LIST.containing_type = _LISTPLUGINAGENTSV1RESPONSE
_LISTPLUGINAGENTSV1RESPONSE.fields_by_name['list'].message_type = _LISTPLUGINAGENTSV1RESPONSE_LIST
_LISTPLUGINAGENTSV1RESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTPLUGINAGENTSV1RESPONSE
DESCRIPTOR.message_types_by_name['ListPluginAgentsV1Request'] = _LISTPLUGINAGENTSV1REQUEST
DESCRIPTOR.message_types_by_name['ListPluginAgentsV1Response'] = _LISTPLUGINAGENTSV1RESPONSE
DESCRIPTOR.message_types_by_name['ListPluginAgentsV1ResponseWrapper'] = _LISTPLUGINAGENTSV1RESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListPluginAgentsV1Request = _reflection.GeneratedProtocolMessageType('ListPluginAgentsV1Request', (_message.Message,), {
  'DESCRIPTOR' : _LISTPLUGINAGENTSV1REQUEST,
  '__module__' : 'list_plugin_agent_v1_pb2'
  # @@protoc_insertion_point(class_scope:plugin.ListPluginAgentsV1Request)
  })
_sym_db.RegisterMessage(ListPluginAgentsV1Request)

ListPluginAgentsV1Response = _reflection.GeneratedProtocolMessageType('ListPluginAgentsV1Response', (_message.Message,), {

  'List' : _reflection.GeneratedProtocolMessageType('List', (_message.Message,), {
    'DESCRIPTOR' : _LISTPLUGINAGENTSV1RESPONSE_LIST,
    '__module__' : 'list_plugin_agent_v1_pb2'
    # @@protoc_insertion_point(class_scope:plugin.ListPluginAgentsV1Response.List)
    })
  ,
  'DESCRIPTOR' : _LISTPLUGINAGENTSV1RESPONSE,
  '__module__' : 'list_plugin_agent_v1_pb2'
  # @@protoc_insertion_point(class_scope:plugin.ListPluginAgentsV1Response)
  })
_sym_db.RegisterMessage(ListPluginAgentsV1Response)
_sym_db.RegisterMessage(ListPluginAgentsV1Response.List)

ListPluginAgentsV1ResponseWrapper = _reflection.GeneratedProtocolMessageType('ListPluginAgentsV1ResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _LISTPLUGINAGENTSV1RESPONSEWRAPPER,
  '__module__' : 'list_plugin_agent_v1_pb2'
  # @@protoc_insertion_point(class_scope:plugin.ListPluginAgentsV1ResponseWrapper)
  })
_sym_db.RegisterMessage(ListPluginAgentsV1ResponseWrapper)


# @@protoc_insertion_point(module_scope)
