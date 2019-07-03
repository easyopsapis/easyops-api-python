# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list_job_tasks.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from model.ops_automation import job_tasks_pb2 as model_dot_ops__automation_dot_job__tasks__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='list_job_tasks.proto',
  package='job_task',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14list_job_tasks.proto\x12\x08job_task\x1a$model/ops_automation/job_tasks.proto\"\x99\x01\n\x13ListJobTasksRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x10\n\x08pageSize\x18\x02 \x01(\x05\x12\r\n\x05jobId\x18\x03 \x01(\t\x12\x0f\n\x07trigger\x18\x04 \x01(\t\x12\x0e\n\x06taskId\x18\x05 \x01(\t\x12\x10\n\x08taskType\x18\x06 \x01(\t\x12\x10\n\x08\x65xecUser\x18\x07 \x01(\t\x12\x0e\n\x06status\x18\x08 \x01(\t\"n\n\x14ListJobTasksResponse\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12&\n\x04list\x18\x04 \x03(\x0b\x32\x18.ops_automation.JobTasks\"}\n\x1bListJobTasksResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12,\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1e.job_task.ListJobTasksResponseb\x06proto3')
  ,
  dependencies=[model_dot_ops__automation_dot_job__tasks__pb2.DESCRIPTOR,])




_LISTJOBTASKSREQUEST = _descriptor.Descriptor(
  name='ListJobTasksRequest',
  full_name='job_task.ListJobTasksRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='job_task.ListJobTasksRequest.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='job_task.ListJobTasksRequest.pageSize', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='jobId', full_name='job_task.ListJobTasksRequest.jobId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trigger', full_name='job_task.ListJobTasksRequest.trigger', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='taskId', full_name='job_task.ListJobTasksRequest.taskId', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='taskType', full_name='job_task.ListJobTasksRequest.taskType', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='execUser', full_name='job_task.ListJobTasksRequest.execUser', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='job_task.ListJobTasksRequest.status', index=7,
      number=8, type=9, cpp_type=9, label=1,
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
  serialized_end=226,
)


_LISTJOBTASKSRESPONSE = _descriptor.Descriptor(
  name='ListJobTasksResponse',
  full_name='job_task.ListJobTasksResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='job_task.ListJobTasksResponse.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='job_task.ListJobTasksResponse.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='job_task.ListJobTasksResponse.total', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='job_task.ListJobTasksResponse.list', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=228,
  serialized_end=338,
)


_LISTJOBTASKSRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListJobTasksResponseWrapper',
  full_name='job_task.ListJobTasksResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='job_task.ListJobTasksResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='job_task.ListJobTasksResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='job_task.ListJobTasksResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='job_task.ListJobTasksResponseWrapper.data', index=3,
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
  serialized_end=465,
)

_LISTJOBTASKSRESPONSE.fields_by_name['list'].message_type = model_dot_ops__automation_dot_job__tasks__pb2._JOBTASKS
_LISTJOBTASKSRESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTJOBTASKSRESPONSE
DESCRIPTOR.message_types_by_name['ListJobTasksRequest'] = _LISTJOBTASKSREQUEST
DESCRIPTOR.message_types_by_name['ListJobTasksResponse'] = _LISTJOBTASKSRESPONSE
DESCRIPTOR.message_types_by_name['ListJobTasksResponseWrapper'] = _LISTJOBTASKSRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListJobTasksRequest = _reflection.GeneratedProtocolMessageType('ListJobTasksRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTJOBTASKSREQUEST,
  __module__ = 'list_job_tasks_pb2'
  # @@protoc_insertion_point(class_scope:job_task.ListJobTasksRequest)
  ))
_sym_db.RegisterMessage(ListJobTasksRequest)

ListJobTasksResponse = _reflection.GeneratedProtocolMessageType('ListJobTasksResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTJOBTASKSRESPONSE,
  __module__ = 'list_job_tasks_pb2'
  # @@protoc_insertion_point(class_scope:job_task.ListJobTasksResponse)
  ))
_sym_db.RegisterMessage(ListJobTasksResponse)

ListJobTasksResponseWrapper = _reflection.GeneratedProtocolMessageType('ListJobTasksResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _LISTJOBTASKSRESPONSEWRAPPER,
  __module__ = 'list_job_tasks_pb2'
  # @@protoc_insertion_point(class_scope:job_task.ListJobTasksResponseWrapper)
  ))
_sym_db.RegisterMessage(ListJobTasksResponseWrapper)


# @@protoc_insertion_point(module_scope)
