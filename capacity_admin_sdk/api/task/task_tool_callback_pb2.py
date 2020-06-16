# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: task_tool_callback.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='task_tool_callback.proto',
  package='task',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x18task_tool_callback.proto\x12\x04task\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1bgoogle/protobuf/empty.proto\"\x93\x01\n\x17TaskToolCallbackRequest\x12\x0e\n\x06\x65xecId\x18\x01 \x01(\t\x12\'\n\x06status\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x13\n\x0btotalStatus\x18\x03 \x01(\t\x12*\n\tagentData\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\"y\n\x1fTaskToolCallbackResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12$\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x16.google.protobuf.Emptyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_TASKTOOLCALLBACKREQUEST = _descriptor.Descriptor(
  name='TaskToolCallbackRequest',
  full_name='task.TaskToolCallbackRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='execId', full_name='task.TaskToolCallbackRequest.execId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='task.TaskToolCallbackRequest.status', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='totalStatus', full_name='task.TaskToolCallbackRequest.totalStatus', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agentData', full_name='task.TaskToolCallbackRequest.agentData', index=3,
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
  serialized_start=94,
  serialized_end=241,
)


_TASKTOOLCALLBACKRESPONSEWRAPPER = _descriptor.Descriptor(
  name='TaskToolCallbackResponseWrapper',
  full_name='task.TaskToolCallbackResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='task.TaskToolCallbackResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='task.TaskToolCallbackResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='task.TaskToolCallbackResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='task.TaskToolCallbackResponseWrapper.data', index=3,
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
  serialized_start=243,
  serialized_end=364,
)

_TASKTOOLCALLBACKREQUEST.fields_by_name['status'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_TASKTOOLCALLBACKREQUEST.fields_by_name['agentData'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_TASKTOOLCALLBACKRESPONSEWRAPPER.fields_by_name['data'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
DESCRIPTOR.message_types_by_name['TaskToolCallbackRequest'] = _TASKTOOLCALLBACKREQUEST
DESCRIPTOR.message_types_by_name['TaskToolCallbackResponseWrapper'] = _TASKTOOLCALLBACKRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TaskToolCallbackRequest = _reflection.GeneratedProtocolMessageType('TaskToolCallbackRequest', (_message.Message,), {
  'DESCRIPTOR' : _TASKTOOLCALLBACKREQUEST,
  '__module__' : 'task_tool_callback_pb2'
  # @@protoc_insertion_point(class_scope:task.TaskToolCallbackRequest)
  })
_sym_db.RegisterMessage(TaskToolCallbackRequest)

TaskToolCallbackResponseWrapper = _reflection.GeneratedProtocolMessageType('TaskToolCallbackResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _TASKTOOLCALLBACKRESPONSEWRAPPER,
  '__module__' : 'task_tool_callback_pb2'
  # @@protoc_insertion_point(class_scope:task.TaskToolCallbackResponseWrapper)
  })
_sym_db.RegisterMessage(TaskToolCallbackResponseWrapper)


# @@protoc_insertion_point(module_scope)