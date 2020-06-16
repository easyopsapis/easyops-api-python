# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: job_tasks_tool_callback.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='job_tasks_tool_callback.proto',
  package='job_task',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1djob_tasks_tool_callback.proto\x12\x08job_task\x1a\x1cgoogle/protobuf/struct.proto\"k\n\x1bJobTasksToolCallbackRequest\x12\x0e\n\x06\x65xecId\x18\x01 \x01(\t\x12\'\n\x06status\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x13\n\x0btotalStatus\x18\x03 \x01(\t\"2\n\x1cJobTasksToolCallbackResponse\x12\x12\n\njobTasksId\x18\x01 \x01(\t\"\x8d\x01\n#JobTasksToolCallbackResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x34\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32&.job_task.JobTasksToolCallbackResponseb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_JOBTASKSTOOLCALLBACKREQUEST = _descriptor.Descriptor(
  name='JobTasksToolCallbackRequest',
  full_name='job_task.JobTasksToolCallbackRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='execId', full_name='job_task.JobTasksToolCallbackRequest.execId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='job_task.JobTasksToolCallbackRequest.status', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='totalStatus', full_name='job_task.JobTasksToolCallbackRequest.totalStatus', index=2,
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
  serialized_start=73,
  serialized_end=180,
)


_JOBTASKSTOOLCALLBACKRESPONSE = _descriptor.Descriptor(
  name='JobTasksToolCallbackResponse',
  full_name='job_task.JobTasksToolCallbackResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='jobTasksId', full_name='job_task.JobTasksToolCallbackResponse.jobTasksId', index=0,
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
  serialized_start=182,
  serialized_end=232,
)


_JOBTASKSTOOLCALLBACKRESPONSEWRAPPER = _descriptor.Descriptor(
  name='JobTasksToolCallbackResponseWrapper',
  full_name='job_task.JobTasksToolCallbackResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='job_task.JobTasksToolCallbackResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='job_task.JobTasksToolCallbackResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='job_task.JobTasksToolCallbackResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='job_task.JobTasksToolCallbackResponseWrapper.data', index=3,
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
  serialized_start=235,
  serialized_end=376,
)

_JOBTASKSTOOLCALLBACKREQUEST.fields_by_name['status'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_JOBTASKSTOOLCALLBACKRESPONSEWRAPPER.fields_by_name['data'].message_type = _JOBTASKSTOOLCALLBACKRESPONSE
DESCRIPTOR.message_types_by_name['JobTasksToolCallbackRequest'] = _JOBTASKSTOOLCALLBACKREQUEST
DESCRIPTOR.message_types_by_name['JobTasksToolCallbackResponse'] = _JOBTASKSTOOLCALLBACKRESPONSE
DESCRIPTOR.message_types_by_name['JobTasksToolCallbackResponseWrapper'] = _JOBTASKSTOOLCALLBACKRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

JobTasksToolCallbackRequest = _reflection.GeneratedProtocolMessageType('JobTasksToolCallbackRequest', (_message.Message,), {
  'DESCRIPTOR' : _JOBTASKSTOOLCALLBACKREQUEST,
  '__module__' : 'job_tasks_tool_callback_pb2'
  # @@protoc_insertion_point(class_scope:job_task.JobTasksToolCallbackRequest)
  })
_sym_db.RegisterMessage(JobTasksToolCallbackRequest)

JobTasksToolCallbackResponse = _reflection.GeneratedProtocolMessageType('JobTasksToolCallbackResponse', (_message.Message,), {
  'DESCRIPTOR' : _JOBTASKSTOOLCALLBACKRESPONSE,
  '__module__' : 'job_tasks_tool_callback_pb2'
  # @@protoc_insertion_point(class_scope:job_task.JobTasksToolCallbackResponse)
  })
_sym_db.RegisterMessage(JobTasksToolCallbackResponse)

JobTasksToolCallbackResponseWrapper = _reflection.GeneratedProtocolMessageType('JobTasksToolCallbackResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _JOBTASKSTOOLCALLBACKRESPONSEWRAPPER,
  '__module__' : 'job_tasks_tool_callback_pb2'
  # @@protoc_insertion_point(class_scope:job_task.JobTasksToolCallbackResponseWrapper)
  })
_sym_db.RegisterMessage(JobTasksToolCallbackResponseWrapper)


# @@protoc_insertion_point(module_scope)
