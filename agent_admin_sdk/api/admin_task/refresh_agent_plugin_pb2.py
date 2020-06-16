# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: refresh_agent_plugin.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='refresh_agent_plugin.proto',
  package='admin_task',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1arefresh_agent_plugin.proto\x12\nadmin_task\"/\n\x1dRefreshAgentPluginTaskRequest\x12\x0e\n\x06\x61gents\x18\x01 \x03(\t\",\n\x1eRefreshAgentPluginTaskResponse\x12\n\n\x02id\x18\x01 \x01(\t\"\x93\x01\n%RefreshAgentPluginTaskResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x38\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32*.admin_task.RefreshAgentPluginTaskResponseb\x06proto3')
)




_REFRESHAGENTPLUGINTASKREQUEST = _descriptor.Descriptor(
  name='RefreshAgentPluginTaskRequest',
  full_name='admin_task.RefreshAgentPluginTaskRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agents', full_name='admin_task.RefreshAgentPluginTaskRequest.agents', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=42,
  serialized_end=89,
)


_REFRESHAGENTPLUGINTASKRESPONSE = _descriptor.Descriptor(
  name='RefreshAgentPluginTaskResponse',
  full_name='admin_task.RefreshAgentPluginTaskResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='admin_task.RefreshAgentPluginTaskResponse.id', index=0,
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
  serialized_start=91,
  serialized_end=135,
)


_REFRESHAGENTPLUGINTASKRESPONSEWRAPPER = _descriptor.Descriptor(
  name='RefreshAgentPluginTaskResponseWrapper',
  full_name='admin_task.RefreshAgentPluginTaskResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='admin_task.RefreshAgentPluginTaskResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='admin_task.RefreshAgentPluginTaskResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='admin_task.RefreshAgentPluginTaskResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='admin_task.RefreshAgentPluginTaskResponseWrapper.data', index=3,
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
  serialized_start=138,
  serialized_end=285,
)

_REFRESHAGENTPLUGINTASKRESPONSEWRAPPER.fields_by_name['data'].message_type = _REFRESHAGENTPLUGINTASKRESPONSE
DESCRIPTOR.message_types_by_name['RefreshAgentPluginTaskRequest'] = _REFRESHAGENTPLUGINTASKREQUEST
DESCRIPTOR.message_types_by_name['RefreshAgentPluginTaskResponse'] = _REFRESHAGENTPLUGINTASKRESPONSE
DESCRIPTOR.message_types_by_name['RefreshAgentPluginTaskResponseWrapper'] = _REFRESHAGENTPLUGINTASKRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RefreshAgentPluginTaskRequest = _reflection.GeneratedProtocolMessageType('RefreshAgentPluginTaskRequest', (_message.Message,), {
  'DESCRIPTOR' : _REFRESHAGENTPLUGINTASKREQUEST,
  '__module__' : 'refresh_agent_plugin_pb2'
  # @@protoc_insertion_point(class_scope:admin_task.RefreshAgentPluginTaskRequest)
  })
_sym_db.RegisterMessage(RefreshAgentPluginTaskRequest)

RefreshAgentPluginTaskResponse = _reflection.GeneratedProtocolMessageType('RefreshAgentPluginTaskResponse', (_message.Message,), {
  'DESCRIPTOR' : _REFRESHAGENTPLUGINTASKRESPONSE,
  '__module__' : 'refresh_agent_plugin_pb2'
  # @@protoc_insertion_point(class_scope:admin_task.RefreshAgentPluginTaskResponse)
  })
_sym_db.RegisterMessage(RefreshAgentPluginTaskResponse)

RefreshAgentPluginTaskResponseWrapper = _reflection.GeneratedProtocolMessageType('RefreshAgentPluginTaskResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _REFRESHAGENTPLUGINTASKRESPONSEWRAPPER,
  '__module__' : 'refresh_agent_plugin_pb2'
  # @@protoc_insertion_point(class_scope:admin_task.RefreshAgentPluginTaskResponseWrapper)
  })
_sym_db.RegisterMessage(RefreshAgentPluginTaskResponseWrapper)


# @@protoc_insertion_point(module_scope)
