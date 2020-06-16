# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: task_spec.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from user_service_sdk.model.easy_command import action_pb2 as user__service__sdk_dot_model_dot_easy__command_dot_action__pb2
from user_service_sdk.model.easy_command import target_pb2 as user__service__sdk_dot_model_dot_easy__command_dot_target__pb2
from user_service_sdk.model.easy_command import task_callback_pb2 as user__service__sdk_dot_model_dot_easy__command_dot_task__callback__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='task_spec.proto',
  package='easy_command',
  syntax='proto3',
  serialized_options=_b('ZFgo.easyops.local/contracts/protorepo-models/easyops/model/easy_command'),
  serialized_pb=_b('\n\x0ftask_spec.proto\x12\x0c\x65\x61sy_command\x1a\x30user_service_sdk/model/easy_command/action.proto\x1a\x30user_service_sdk/model/easy_command/target.proto\x1a\x37user_service_sdk/model/easy_command/task_callback.proto\"\xef\x02\n\x08TaskSpec\x12\x0e\n\x06taskId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x11\n\toperation\x18\x04 \x01(\t\x12\x0f\n\x07groupId\x18\x05 \x01(\t\x12%\n\x07\x61\x63tions\x18\x06 \x03(\x0b\x32\x14.easy_command.Action\x12%\n\x07targets\x18\x07 \x03(\x0b\x32\x14.easy_command.Target\x12\r\n\x05\x61ppId\x18\x08 \x01(\t\x12\x11\n\tclusterId\x18\t \x01(\t\x12\x11\n\tpackageId\x18\n \x01(\t\x12\x11\n\tversionId\x18\x0b \x01(\t\x12\x12\n\nneedNotify\x18\x0c \x01(\x08\x12,\n\x08\x63\x61llback\x18\r \x01(\x0b\x32\x1a.easy_command.TaskCallback\x12\x10\n\x08\x62\x61tchNum\x18\x0e \x01(\x05\x12\x15\n\rbatchInterval\x18\x0f \x01(\x05\x12\x12\n\nfailedStop\x18\x10 \x01(\x08\x42HZFgo.easyops.local/contracts/protorepo-models/easyops/model/easy_commandb\x06proto3')
  ,
  dependencies=[user__service__sdk_dot_model_dot_easy__command_dot_action__pb2.DESCRIPTOR,user__service__sdk_dot_model_dot_easy__command_dot_target__pb2.DESCRIPTOR,user__service__sdk_dot_model_dot_easy__command_dot_task__callback__pb2.DESCRIPTOR,])




_TASKSPEC = _descriptor.Descriptor(
  name='TaskSpec',
  full_name='easy_command.TaskSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='taskId', full_name='easy_command.TaskSpec.taskId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='easy_command.TaskSpec.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='easy_command.TaskSpec.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operation', full_name='easy_command.TaskSpec.operation', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='groupId', full_name='easy_command.TaskSpec.groupId', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actions', full_name='easy_command.TaskSpec.actions', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targets', full_name='easy_command.TaskSpec.targets', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='appId', full_name='easy_command.TaskSpec.appId', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clusterId', full_name='easy_command.TaskSpec.clusterId', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageId', full_name='easy_command.TaskSpec.packageId', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionId', full_name='easy_command.TaskSpec.versionId', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='needNotify', full_name='easy_command.TaskSpec.needNotify', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='callback', full_name='easy_command.TaskSpec.callback', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batchNum', full_name='easy_command.TaskSpec.batchNum', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batchInterval', full_name='easy_command.TaskSpec.batchInterval', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='failedStop', full_name='easy_command.TaskSpec.failedStop', index=15,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=191,
  serialized_end=558,
)

_TASKSPEC.fields_by_name['actions'].message_type = user__service__sdk_dot_model_dot_easy__command_dot_action__pb2._ACTION
_TASKSPEC.fields_by_name['targets'].message_type = user__service__sdk_dot_model_dot_easy__command_dot_target__pb2._TARGET
_TASKSPEC.fields_by_name['callback'].message_type = user__service__sdk_dot_model_dot_easy__command_dot_task__callback__pb2._TASKCALLBACK
DESCRIPTOR.message_types_by_name['TaskSpec'] = _TASKSPEC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TaskSpec = _reflection.GeneratedProtocolMessageType('TaskSpec', (_message.Message,), {
  'DESCRIPTOR' : _TASKSPEC,
  '__module__' : 'task_spec_pb2'
  # @@protoc_insertion_point(class_scope:easy_command.TaskSpec)
  })
_sym_db.RegisterMessage(TaskSpec)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
