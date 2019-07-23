# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from model.inspection import user_or_user_group_pb2 as model_dot_inspection_dot_user__or__user__group__pb2
from model.easy_command import action_param_custom_pb2 as model_dot_easy__command_dot_action__param__custom__pb2
from model.inspection import task_pb2 as model_dot_inspection_dot_task__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='get.proto',
  package='task',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\tget.proto\x12\x04task\x1a)model/inspection/user_or_user_group.proto\x1a,model/easy_command/action_param_custom.proto\x1a\x1bmodel/inspection/task.proto\"6\n\x0eGetTaskRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x18\n\x10inspectionTaskId\x18\x02 \x01(\t\"t\n\x16GetTaskResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12(\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1a.inspection.InspectionTaskb\x06proto3')
  ,
  dependencies=[model_dot_inspection_dot_user__or__user__group__pb2.DESCRIPTOR,model_dot_easy__command_dot_action__param__custom__pb2.DESCRIPTOR,model_dot_inspection_dot_task__pb2.DESCRIPTOR,])




_GETTASKREQUEST = _descriptor.Descriptor(
  name='GetTaskRequest',
  full_name='task.GetTaskRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='task.GetTaskRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inspectionTaskId', full_name='task.GetTaskRequest.inspectionTaskId', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=137,
  serialized_end=191,
)


_GETTASKRESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetTaskResponseWrapper',
  full_name='task.GetTaskResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='task.GetTaskResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='task.GetTaskResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='task.GetTaskResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='task.GetTaskResponseWrapper.data', index=3,
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
  serialized_start=193,
  serialized_end=309,
)

_GETTASKRESPONSEWRAPPER.fields_by_name['data'].message_type = model_dot_inspection_dot_task__pb2._INSPECTIONTASK
DESCRIPTOR.message_types_by_name['GetTaskRequest'] = _GETTASKREQUEST
DESCRIPTOR.message_types_by_name['GetTaskResponseWrapper'] = _GETTASKRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetTaskRequest = _reflection.GeneratedProtocolMessageType('GetTaskRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETTASKREQUEST,
  __module__ = 'get_pb2'
  # @@protoc_insertion_point(class_scope:task.GetTaskRequest)
  ))
_sym_db.RegisterMessage(GetTaskRequest)

GetTaskResponseWrapper = _reflection.GeneratedProtocolMessageType('GetTaskResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _GETTASKRESPONSEWRAPPER,
  __module__ = 'get_pb2'
  # @@protoc_insertion_point(class_scope:task.GetTaskResponseWrapper)
  ))
_sym_db.RegisterMessage(GetTaskResponseWrapper)


# @@protoc_insertion_point(module_scope)
