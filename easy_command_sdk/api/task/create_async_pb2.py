# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: create_async.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from easy_command_sdk.model.easy_command import action_pb2 as easy__command__sdk_dot_model_dot_easy__command_dot_action__pb2
from easy_command_sdk.model.easy_command import target_pb2 as easy__command__sdk_dot_model_dot_easy__command_dot_target__pb2
from easy_command_sdk.model.easy_command import task_callback_pb2 as easy__command__sdk_dot_model_dot_easy__command_dot_task__callback__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='create_async.proto',
  package='task',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x12\x63reate_async.proto\x12\x04task\x1a\x30\x65\x61sy_command_sdk/model/easy_command/action.proto\x1a\x30\x65\x61sy_command_sdk/model/easy_command/target.proto\x1a\x37\x65\x61sy_command_sdk/model/easy_command/task_callback.proto\")\n\x17\x43reateAsyncTaskResponse\x12\x0e\n\x06taskId\x18\x01 \x01(\t\"\x7f\n\x1e\x43reateAsyncTaskResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12+\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1d.task.CreateAsyncTaskResponseb\x06proto3')
  ,
  dependencies=[easy__command__sdk_dot_model_dot_easy__command_dot_action__pb2.DESCRIPTOR,easy__command__sdk_dot_model_dot_easy__command_dot_target__pb2.DESCRIPTOR,easy__command__sdk_dot_model_dot_easy__command_dot_task__callback__pb2.DESCRIPTOR,])




_CREATEASYNCTASKRESPONSE = _descriptor.Descriptor(
  name='CreateAsyncTaskResponse',
  full_name='task.CreateAsyncTaskResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='taskId', full_name='task.CreateAsyncTaskResponse.taskId', index=0,
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
  serialized_start=185,
  serialized_end=226,
)


_CREATEASYNCTASKRESPONSEWRAPPER = _descriptor.Descriptor(
  name='CreateAsyncTaskResponseWrapper',
  full_name='task.CreateAsyncTaskResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='task.CreateAsyncTaskResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='task.CreateAsyncTaskResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='task.CreateAsyncTaskResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='task.CreateAsyncTaskResponseWrapper.data', index=3,
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
  serialized_start=228,
  serialized_end=355,
)

_CREATEASYNCTASKRESPONSEWRAPPER.fields_by_name['data'].message_type = _CREATEASYNCTASKRESPONSE
DESCRIPTOR.message_types_by_name['CreateAsyncTaskResponse'] = _CREATEASYNCTASKRESPONSE
DESCRIPTOR.message_types_by_name['CreateAsyncTaskResponseWrapper'] = _CREATEASYNCTASKRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateAsyncTaskResponse = _reflection.GeneratedProtocolMessageType('CreateAsyncTaskResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEASYNCTASKRESPONSE,
  '__module__' : 'create_async_pb2'
  # @@protoc_insertion_point(class_scope:task.CreateAsyncTaskResponse)
  })
_sym_db.RegisterMessage(CreateAsyncTaskResponse)

CreateAsyncTaskResponseWrapper = _reflection.GeneratedProtocolMessageType('CreateAsyncTaskResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _CREATEASYNCTASKRESPONSEWRAPPER,
  '__module__' : 'create_async_pb2'
  # @@protoc_insertion_point(class_scope:task.CreateAsyncTaskResponseWrapper)
  })
_sym_db.RegisterMessage(CreateAsyncTaskResponseWrapper)


# @@protoc_insertion_point(module_scope)