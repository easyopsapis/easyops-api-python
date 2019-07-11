# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: liquibase_task_callback.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from model.easy_command import task_detail_pb2 as model_dot_easy__command_dot_task__detail__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='liquibase_task_callback.proto',
  package='dbtask',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1dliquibase_task_callback.proto\x12\x06\x64\x62task\x1a$model/easy_command/task_detail.proto\"I\n\x1cLiquibaseTaskCallbackRequest\x12)\n\x07\x63ommand\x18\x01 \x01(\x0b\x32\x18.easy_command.TaskDetail\"/\n\x1dLiquibaseTaskCallbackResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"\x8d\x01\n$LiquibaseTaskCallbackResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x33\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32%.dbtask.LiquibaseTaskCallbackResponseb\x06proto3')
  ,
  dependencies=[model_dot_easy__command_dot_task__detail__pb2.DESCRIPTOR,])




_LIQUIBASETASKCALLBACKREQUEST = _descriptor.Descriptor(
  name='LiquibaseTaskCallbackRequest',
  full_name='dbtask.LiquibaseTaskCallbackRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='command', full_name='dbtask.LiquibaseTaskCallbackRequest.command', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=79,
  serialized_end=152,
)


_LIQUIBASETASKCALLBACKRESPONSE = _descriptor.Descriptor(
  name='LiquibaseTaskCallbackResponse',
  full_name='dbtask.LiquibaseTaskCallbackResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='dbtask.LiquibaseTaskCallbackResponse.status', index=0,
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
  serialized_start=154,
  serialized_end=201,
)


_LIQUIBASETASKCALLBACKRESPONSEWRAPPER = _descriptor.Descriptor(
  name='LiquibaseTaskCallbackResponseWrapper',
  full_name='dbtask.LiquibaseTaskCallbackResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='dbtask.LiquibaseTaskCallbackResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='dbtask.LiquibaseTaskCallbackResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dbtask.LiquibaseTaskCallbackResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='dbtask.LiquibaseTaskCallbackResponseWrapper.data', index=3,
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
  serialized_start=204,
  serialized_end=345,
)

_LIQUIBASETASKCALLBACKREQUEST.fields_by_name['command'].message_type = model_dot_easy__command_dot_task__detail__pb2._TASKDETAIL
_LIQUIBASETASKCALLBACKRESPONSEWRAPPER.fields_by_name['data'].message_type = _LIQUIBASETASKCALLBACKRESPONSE
DESCRIPTOR.message_types_by_name['LiquibaseTaskCallbackRequest'] = _LIQUIBASETASKCALLBACKREQUEST
DESCRIPTOR.message_types_by_name['LiquibaseTaskCallbackResponse'] = _LIQUIBASETASKCALLBACKRESPONSE
DESCRIPTOR.message_types_by_name['LiquibaseTaskCallbackResponseWrapper'] = _LIQUIBASETASKCALLBACKRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LiquibaseTaskCallbackRequest = _reflection.GeneratedProtocolMessageType('LiquibaseTaskCallbackRequest', (_message.Message,), dict(
  DESCRIPTOR = _LIQUIBASETASKCALLBACKREQUEST,
  __module__ = 'liquibase_task_callback_pb2'
  # @@protoc_insertion_point(class_scope:dbtask.LiquibaseTaskCallbackRequest)
  ))
_sym_db.RegisterMessage(LiquibaseTaskCallbackRequest)

LiquibaseTaskCallbackResponse = _reflection.GeneratedProtocolMessageType('LiquibaseTaskCallbackResponse', (_message.Message,), dict(
  DESCRIPTOR = _LIQUIBASETASKCALLBACKRESPONSE,
  __module__ = 'liquibase_task_callback_pb2'
  # @@protoc_insertion_point(class_scope:dbtask.LiquibaseTaskCallbackResponse)
  ))
_sym_db.RegisterMessage(LiquibaseTaskCallbackResponse)

LiquibaseTaskCallbackResponseWrapper = _reflection.GeneratedProtocolMessageType('LiquibaseTaskCallbackResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _LIQUIBASETASKCALLBACKRESPONSEWRAPPER,
  __module__ = 'liquibase_task_callback_pb2'
  # @@protoc_insertion_point(class_scope:dbtask.LiquibaseTaskCallbackResponseWrapper)
  ))
_sym_db.RegisterMessage(LiquibaseTaskCallbackResponseWrapper)


# @@protoc_insertion_point(module_scope)