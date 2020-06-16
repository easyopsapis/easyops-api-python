# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: task_detail.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flow_sdk.model.easy_command import task_callback_pb2 as flow__sdk_dot_model_dot_easy__command_dot_task__callback__pb2
from flow_sdk.model.easy_command import target_log_pb2 as flow__sdk_dot_model_dot_easy__command_dot_target__log__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='task_detail.proto',
  package='easy_command',
  syntax='proto3',
  serialized_options=_b('ZFgo.easyops.local/contracts/protorepo-models/easyops/model/easy_command'),
  serialized_pb=_b('\n\x11task_detail.proto\x12\x0c\x65\x61sy_command\x1a/flow_sdk/model/easy_command/task_callback.proto\x1a,flow_sdk/model/easy_command/target_log.proto\"\xd7\x03\n\nTaskDetail\x12\x0e\n\x06taskId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x11\n\toperation\x18\x04 \x01(\t\x12\x0f\n\x07groupId\x18\x05 \x01(\t\x12\r\n\x05\x61ppId\x18\x06 \x01(\t\x12\x11\n\tclusterId\x18\x07 \x01(\t\x12\x11\n\tpackageId\x18\x08 \x01(\t\x12\x11\n\tversionId\x18\t \x01(\t\x12\x12\n\nneedNotify\x18\n \x01(\x08\x12,\n\x08\x63\x61llback\x18\x0b \x01(\x0b\x32\x1a.easy_command.TaskCallback\x12\x10\n\x08\x62\x61tchNum\x18\x0c \x01(\x05\x12\x15\n\rbatchInterval\x18\r \x01(\x05\x12\x12\n\nfailedStop\x18\x0e \x01(\x08\x12\x0b\n\x03org\x18\x0f \x01(\x05\x12\x10\n\x08operator\x18\x10 \x01(\t\x12\x0e\n\x06status\x18\x11 \x01(\t\x12\x0c\n\x04\x63ode\x18\x12 \x01(\x05\x12\x10\n\x08usedTime\x18\x13 \x01(\x05\x12\x11\n\tstartTime\x18\x14 \x01(\t\x12\x12\n\nupdateTime\x18\x15 \x01(\t\x12\x0f\n\x07\x65ndTime\x18\x16 \x01(\t\x12+\n\ntargetsLog\x18\x17 \x03(\x0b\x32\x17.easy_command.TargetLogBHZFgo.easyops.local/contracts/protorepo-models/easyops/model/easy_commandb\x06proto3')
  ,
  dependencies=[flow__sdk_dot_model_dot_easy__command_dot_task__callback__pb2.DESCRIPTOR,flow__sdk_dot_model_dot_easy__command_dot_target__log__pb2.DESCRIPTOR,])




_TASKDETAIL = _descriptor.Descriptor(
  name='TaskDetail',
  full_name='easy_command.TaskDetail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='taskId', full_name='easy_command.TaskDetail.taskId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='easy_command.TaskDetail.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='easy_command.TaskDetail.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operation', full_name='easy_command.TaskDetail.operation', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='groupId', full_name='easy_command.TaskDetail.groupId', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='appId', full_name='easy_command.TaskDetail.appId', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clusterId', full_name='easy_command.TaskDetail.clusterId', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageId', full_name='easy_command.TaskDetail.packageId', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionId', full_name='easy_command.TaskDetail.versionId', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='needNotify', full_name='easy_command.TaskDetail.needNotify', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='callback', full_name='easy_command.TaskDetail.callback', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batchNum', full_name='easy_command.TaskDetail.batchNum', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batchInterval', full_name='easy_command.TaskDetail.batchInterval', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='failedStop', full_name='easy_command.TaskDetail.failedStop', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org', full_name='easy_command.TaskDetail.org', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operator', full_name='easy_command.TaskDetail.operator', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='easy_command.TaskDetail.status', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='easy_command.TaskDetail.code', index=17,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='usedTime', full_name='easy_command.TaskDetail.usedTime', index=18,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='easy_command.TaskDetail.startTime', index=19,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updateTime', full_name='easy_command.TaskDetail.updateTime', index=20,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endTime', full_name='easy_command.TaskDetail.endTime', index=21,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targetsLog', full_name='easy_command.TaskDetail.targetsLog', index=22,
      number=23, type=11, cpp_type=10, label=3,
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
  serialized_start=131,
  serialized_end=602,
)

_TASKDETAIL.fields_by_name['callback'].message_type = flow__sdk_dot_model_dot_easy__command_dot_task__callback__pb2._TASKCALLBACK
_TASKDETAIL.fields_by_name['targetsLog'].message_type = flow__sdk_dot_model_dot_easy__command_dot_target__log__pb2._TARGETLOG
DESCRIPTOR.message_types_by_name['TaskDetail'] = _TASKDETAIL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TaskDetail = _reflection.GeneratedProtocolMessageType('TaskDetail', (_message.Message,), {
  'DESCRIPTOR' : _TASKDETAIL,
  '__module__' : 'task_detail_pb2'
  # @@protoc_insertion_point(class_scope:easy_command.TaskDetail)
  })
_sym_db.RegisterMessage(TaskDetail)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
