# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: task_ret.proto

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
  name='task_ret.proto',
  package='easy_flow',
  syntax='proto3',
  serialized_options=_b('ZCgo.easyops.local/contracts/protorepo-models/easyops/model/easy_flow'),
  serialized_pb=_b('\n\x0etask_ret.proto\x12\teasy_flow\x1a\x1cgoogle/protobuf/struct.proto\"\xd7\x06\n\x07TaskRet\x12\x0e\n\x06taskId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07groupId\x18\x03 \x01(\t\x12\r\n\x05\x61ppId\x18\x04 \x01(\t\x12\x10\n\x08\x62\x61tchNum\x18\x05 \x01(\x05\x12\x15\n\rbatchInterval\x18\x06 \x01(\x05\x12\x12\n\nfailedStop\x18\x07 \x01(\t\x12\x11\n\tpackageId\x18\x08 \x01(\t\x12\x0c\n\x04type\x18\t \x01(\t\x12\x11\n\toperation\x18\n \x01(\t\x12\x0b\n\x03org\x18\x0b \x01(\x05\x12\x10\n\x08operator\x18\x0c \x01(\t\x12\x0e\n\x06status\x18\r \x01(\t\x12\x0c\n\x04\x63ode\x18\x0e \x01(\x05\x12\x10\n\x08usedTime\x18\x0f \x01(\x05\x12\x11\n\tstartTime\x18\x10 \x01(\t\x12\x0f\n\x07\x65ndTime\x18\x11 \x01(\t\x12*\n\textraInfo\x18\x12 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x31\n\ntargetsLog\x18\x13 \x03(\x0b\x32\x1d.easy_flow.TaskRet.TargetsLog\x1a\xca\x03\n\nTargetsLog\x12\x10\n\x08targetId\x18\x01 \x01(\t\x12\x12\n\ntargetName\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\x12\x11\n\tsysStatus\x18\x04 \x01(\t\x12\x0c\n\x04\x63ode\x18\x05 \x01(\x05\x12\x0b\n\x03msg\x18\x06 \x01(\t\x12)\n\x08progress\x18\x07 \x01(\x0b\x32\x17.google.protobuf.Struct\x12<\n\nactionsLog\x18\x08 \x03(\x0b\x32(.easy_flow.TaskRet.TargetsLog.ActionsLog\x1a\xee\x01\n\nActionsLog\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x03 \x01(\t\x12\x0e\n\x06status\x18\x04 \x01(\t\x12\x0c\n\x04\x63ode\x18\x05 \x01(\x05\x12(\n\x07\x65xtInfo\x18\x06 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0b\n\x03msg\x18\x07 \x01(\t\x12)\n\x08progress\x18\x08 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x10\n\x08usedTime\x18\t \x01(\x05\x12\x11\n\tstartTime\x18\n \x01(\t\x12\x0f\n\x07\x65ndTime\x18\x0b \x01(\tBEZCgo.easyops.local/contracts/protorepo-models/easyops/model/easy_flowb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_TASKRET_TARGETSLOG_ACTIONSLOG = _descriptor.Descriptor(
  name='ActionsLog',
  full_name='easy_flow.TaskRet.TargetsLog.ActionsLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='easy_flow.TaskRet.TargetsLog.ActionsLog.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='easy_flow.TaskRet.TargetsLog.ActionsLog.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='easy_flow.TaskRet.TargetsLog.ActionsLog.action', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='easy_flow.TaskRet.TargetsLog.ActionsLog.status', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='easy_flow.TaskRet.TargetsLog.ActionsLog.code', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extInfo', full_name='easy_flow.TaskRet.TargetsLog.ActionsLog.extInfo', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='easy_flow.TaskRet.TargetsLog.ActionsLog.msg', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='progress', full_name='easy_flow.TaskRet.TargetsLog.ActionsLog.progress', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='usedTime', full_name='easy_flow.TaskRet.TargetsLog.ActionsLog.usedTime', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='easy_flow.TaskRet.TargetsLog.ActionsLog.startTime', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endTime', full_name='easy_flow.TaskRet.TargetsLog.ActionsLog.endTime', index=10,
      number=11, type=9, cpp_type=9, label=1,
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
  serialized_start=677,
  serialized_end=915,
)

_TASKRET_TARGETSLOG = _descriptor.Descriptor(
  name='TargetsLog',
  full_name='easy_flow.TaskRet.TargetsLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='targetId', full_name='easy_flow.TaskRet.TargetsLog.targetId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targetName', full_name='easy_flow.TaskRet.TargetsLog.targetName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='easy_flow.TaskRet.TargetsLog.status', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sysStatus', full_name='easy_flow.TaskRet.TargetsLog.sysStatus', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='easy_flow.TaskRet.TargetsLog.code', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='easy_flow.TaskRet.TargetsLog.msg', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='progress', full_name='easy_flow.TaskRet.TargetsLog.progress', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actionsLog', full_name='easy_flow.TaskRet.TargetsLog.actionsLog', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TASKRET_TARGETSLOG_ACTIONSLOG, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=457,
  serialized_end=915,
)

_TASKRET = _descriptor.Descriptor(
  name='TaskRet',
  full_name='easy_flow.TaskRet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='taskId', full_name='easy_flow.TaskRet.taskId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='easy_flow.TaskRet.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='groupId', full_name='easy_flow.TaskRet.groupId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='appId', full_name='easy_flow.TaskRet.appId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batchNum', full_name='easy_flow.TaskRet.batchNum', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batchInterval', full_name='easy_flow.TaskRet.batchInterval', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='failedStop', full_name='easy_flow.TaskRet.failedStop', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageId', full_name='easy_flow.TaskRet.packageId', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='easy_flow.TaskRet.type', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operation', full_name='easy_flow.TaskRet.operation', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org', full_name='easy_flow.TaskRet.org', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operator', full_name='easy_flow.TaskRet.operator', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='easy_flow.TaskRet.status', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='easy_flow.TaskRet.code', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='usedTime', full_name='easy_flow.TaskRet.usedTime', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='easy_flow.TaskRet.startTime', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endTime', full_name='easy_flow.TaskRet.endTime', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extraInfo', full_name='easy_flow.TaskRet.extraInfo', index=17,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targetsLog', full_name='easy_flow.TaskRet.targetsLog', index=18,
      number=19, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TASKRET_TARGETSLOG, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=915,
)

_TASKRET_TARGETSLOG_ACTIONSLOG.fields_by_name['extInfo'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_TASKRET_TARGETSLOG_ACTIONSLOG.fields_by_name['progress'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_TASKRET_TARGETSLOG_ACTIONSLOG.containing_type = _TASKRET_TARGETSLOG
_TASKRET_TARGETSLOG.fields_by_name['progress'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_TASKRET_TARGETSLOG.fields_by_name['actionsLog'].message_type = _TASKRET_TARGETSLOG_ACTIONSLOG
_TASKRET_TARGETSLOG.containing_type = _TASKRET
_TASKRET.fields_by_name['extraInfo'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_TASKRET.fields_by_name['targetsLog'].message_type = _TASKRET_TARGETSLOG
DESCRIPTOR.message_types_by_name['TaskRet'] = _TASKRET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TaskRet = _reflection.GeneratedProtocolMessageType('TaskRet', (_message.Message,), dict(

  TargetsLog = _reflection.GeneratedProtocolMessageType('TargetsLog', (_message.Message,), dict(

    ActionsLog = _reflection.GeneratedProtocolMessageType('ActionsLog', (_message.Message,), dict(
      DESCRIPTOR = _TASKRET_TARGETSLOG_ACTIONSLOG,
      __module__ = 'task_ret_pb2'
      # @@protoc_insertion_point(class_scope:easy_flow.TaskRet.TargetsLog.ActionsLog)
      ))
    ,
    DESCRIPTOR = _TASKRET_TARGETSLOG,
    __module__ = 'task_ret_pb2'
    # @@protoc_insertion_point(class_scope:easy_flow.TaskRet.TargetsLog)
    ))
  ,
  DESCRIPTOR = _TASKRET,
  __module__ = 'task_ret_pb2'
  # @@protoc_insertion_point(class_scope:easy_flow.TaskRet)
  ))
_sym_db.RegisterMessage(TaskRet)
_sym_db.RegisterMessage(TaskRet.TargetsLog)
_sym_db.RegisterMessage(TaskRet.TargetsLog.ActionsLog)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)