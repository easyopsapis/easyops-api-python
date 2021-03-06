# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: terminate_task.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tool_sdk.model.tool import callback_pb2 as tool__sdk_dot_model_dot_tool_dot_callback__pb2
from tool_sdk.model.tool import tool_pb2 as tool__sdk_dot_model_dot_tool_dot_tool__pb2
from tool_sdk.model.tool import tool_task_pb2 as tool__sdk_dot_model_dot_tool_dot_tool__task__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='terminate_task.proto',
  package='execute',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14terminate_task.proto\x12\x07\x65xecute\x1a\"tool_sdk/model/tool/callback.proto\x1a\x1etool_sdk/model/tool/tool.proto\x1a#tool_sdk/model/tool/tool_task.proto\x1a\x1cgoogle/protobuf/struct.proto\"&\n\x14TerminateTaskRequest\x12\x0e\n\x06taskId\x18\x01 \x01(\t\"n\n\x1cTerminateTaskResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x1c\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x0e.tool.ToolTaskb\x06proto3')
  ,
  dependencies=[tool__sdk_dot_model_dot_tool_dot_callback__pb2.DESCRIPTOR,tool__sdk_dot_model_dot_tool_dot_tool__pb2.DESCRIPTOR,tool__sdk_dot_model_dot_tool_dot_tool__task__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_TERMINATETASKREQUEST = _descriptor.Descriptor(
  name='TerminateTaskRequest',
  full_name='execute.TerminateTaskRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='taskId', full_name='execute.TerminateTaskRequest.taskId', index=0,
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
  serialized_start=168,
  serialized_end=206,
)


_TERMINATETASKRESPONSEWRAPPER = _descriptor.Descriptor(
  name='TerminateTaskResponseWrapper',
  full_name='execute.TerminateTaskResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='execute.TerminateTaskResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='execute.TerminateTaskResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='execute.TerminateTaskResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='execute.TerminateTaskResponseWrapper.data', index=3,
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
  serialized_start=208,
  serialized_end=318,
)

_TERMINATETASKRESPONSEWRAPPER.fields_by_name['data'].message_type = tool__sdk_dot_model_dot_tool_dot_tool__task__pb2._TOOLTASK
DESCRIPTOR.message_types_by_name['TerminateTaskRequest'] = _TERMINATETASKREQUEST
DESCRIPTOR.message_types_by_name['TerminateTaskResponseWrapper'] = _TERMINATETASKRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TerminateTaskRequest = _reflection.GeneratedProtocolMessageType('TerminateTaskRequest', (_message.Message,), {
  'DESCRIPTOR' : _TERMINATETASKREQUEST,
  '__module__' : 'terminate_task_pb2'
  # @@protoc_insertion_point(class_scope:execute.TerminateTaskRequest)
  })
_sym_db.RegisterMessage(TerminateTaskRequest)

TerminateTaskResponseWrapper = _reflection.GeneratedProtocolMessageType('TerminateTaskResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _TERMINATETASKRESPONSEWRAPPER,
  '__module__' : 'terminate_task_pb2'
  # @@protoc_insertion_point(class_scope:execute.TerminateTaskResponseWrapper)
  })
_sym_db.RegisterMessage(TerminateTaskResponseWrapper)


# @@protoc_insertion_point(module_scope)
