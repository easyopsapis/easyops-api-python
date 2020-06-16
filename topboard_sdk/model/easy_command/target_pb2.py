# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: target.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from topboard_sdk.model.easy_command import action_param_custom_pb2 as topboard__sdk_dot_model_dot_easy__command_dot_action__param__custom__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='target.proto',
  package='easy_command',
  syntax='proto3',
  serialized_options=_b('ZFgo.easyops.local/contracts/protorepo-models/easyops/model/easy_command'),
  serialized_pb=_b('\n\x0ctarget.proto\x12\x0c\x65\x61sy_command\x1a\x39topboard_sdk/model/easy_command/action_param_custom.proto\"e\n\x06Target\x12\x10\n\x08targetId\x18\x01 \x01(\t\x12\x12\n\ntargetName\x18\x02 \x01(\t\x12\x35\n\x0c\x61\x63tionParams\x18\x03 \x03(\x0b\x32\x1f.easy_command.ActionParamCustomBHZFgo.easyops.local/contracts/protorepo-models/easyops/model/easy_commandb\x06proto3')
  ,
  dependencies=[topboard__sdk_dot_model_dot_easy__command_dot_action__param__custom__pb2.DESCRIPTOR,])




_TARGET = _descriptor.Descriptor(
  name='Target',
  full_name='easy_command.Target',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='targetId', full_name='easy_command.Target.targetId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targetName', full_name='easy_command.Target.targetName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actionParams', full_name='easy_command.Target.actionParams', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=89,
  serialized_end=190,
)

_TARGET.fields_by_name['actionParams'].message_type = topboard__sdk_dot_model_dot_easy__command_dot_action__param__custom__pb2._ACTIONPARAMCUSTOM
DESCRIPTOR.message_types_by_name['Target'] = _TARGET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Target = _reflection.GeneratedProtocolMessageType('Target', (_message.Message,), {
  'DESCRIPTOR' : _TARGET,
  '__module__' : 'target_pb2'
  # @@protoc_insertion_point(class_scope:easy_command.Target)
  })
_sym_db.RegisterMessage(Target)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
