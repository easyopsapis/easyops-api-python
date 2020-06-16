# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: target_log.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from webshell_sdk.model.easy_command import action_log_pb2 as webshell__sdk_dot_model_dot_easy__command_dot_action__log__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='target_log.proto',
  package='easy_command',
  syntax='proto3',
  serialized_options=_b('ZFgo.easyops.local/contracts/protorepo-models/easyops/model/easy_command'),
  serialized_pb=_b('\n\x10target_log.proto\x12\x0c\x65\x61sy_command\x1a\x30webshell_sdk/model/easy_command/action_log.proto\"\xe6\x01\n\tTargetLog\x12\x10\n\x08targetId\x18\x01 \x01(\t\x12\x12\n\ntargetName\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\x12\x11\n\tsysStatus\x18\x04 \x01(\t\x12\x0c\n\x04\x63ode\x18\x05 \x01(\x05\x12\x0b\n\x03msg\x18\x06 \x01(\t\x12+\n\nactionsLog\x18\x07 \x03(\x0b\x32\x17.easy_command.ActionLog\x12\x10\n\x08usedTime\x18\x08 \x01(\x05\x12\x11\n\tstartTime\x18\t \x01(\t\x12\x12\n\nupdateTime\x18\n \x01(\t\x12\x0f\n\x07\x65ndTime\x18\x0b \x01(\tBHZFgo.easyops.local/contracts/protorepo-models/easyops/model/easy_commandb\x06proto3')
  ,
  dependencies=[webshell__sdk_dot_model_dot_easy__command_dot_action__log__pb2.DESCRIPTOR,])




_TARGETLOG = _descriptor.Descriptor(
  name='TargetLog',
  full_name='easy_command.TargetLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='targetId', full_name='easy_command.TargetLog.targetId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targetName', full_name='easy_command.TargetLog.targetName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='easy_command.TargetLog.status', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sysStatus', full_name='easy_command.TargetLog.sysStatus', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='easy_command.TargetLog.code', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='easy_command.TargetLog.msg', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actionsLog', full_name='easy_command.TargetLog.actionsLog', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='usedTime', full_name='easy_command.TargetLog.usedTime', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='easy_command.TargetLog.startTime', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updateTime', full_name='easy_command.TargetLog.updateTime', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endTime', full_name='easy_command.TargetLog.endTime', index=10,
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
  serialized_start=85,
  serialized_end=315,
)

_TARGETLOG.fields_by_name['actionsLog'].message_type = webshell__sdk_dot_model_dot_easy__command_dot_action__log__pb2._ACTIONLOG
DESCRIPTOR.message_types_by_name['TargetLog'] = _TARGETLOG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TargetLog = _reflection.GeneratedProtocolMessageType('TargetLog', (_message.Message,), {
  'DESCRIPTOR' : _TARGETLOG,
  '__module__' : 'target_log_pb2'
  # @@protoc_insertion_point(class_scope:easy_command.TargetLog)
  })
_sym_db.RegisterMessage(TargetLog)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
