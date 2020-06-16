# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: action_param_cmd.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='action_param_cmd.proto',
  package='easy_command',
  syntax='proto3',
  serialized_options=_b('ZFgo.easyops.local/contracts/protorepo-models/easyops/model/easy_command'),
  serialized_pb=_b('\n\x16\x61\x63tion_param_cmd.proto\x12\x0c\x65\x61sy_command\"d\n\x0e\x43mdActionParam\x12\x0b\n\x03\x63md\x18\x01 \x01(\t\x12\x10\n\x08\x65xecUser\x18\x02 \x01(\t\x12\x12\n\nscriptType\x18\x03 \x01(\t\x12\x0e\n\x06parser\x18\x04 \x01(\t\x12\x0f\n\x07timeout\x18\x05 \x01(\x05\x42HZFgo.easyops.local/contracts/protorepo-models/easyops/model/easy_commandb\x06proto3')
)




_CMDACTIONPARAM = _descriptor.Descriptor(
  name='CmdActionParam',
  full_name='easy_command.CmdActionParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='easy_command.CmdActionParam.cmd', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='execUser', full_name='easy_command.CmdActionParam.execUser', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scriptType', full_name='easy_command.CmdActionParam.scriptType', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parser', full_name='easy_command.CmdActionParam.parser', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='easy_command.CmdActionParam.timeout', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=40,
  serialized_end=140,
)

DESCRIPTOR.message_types_by_name['CmdActionParam'] = _CMDACTIONPARAM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CmdActionParam = _reflection.GeneratedProtocolMessageType('CmdActionParam', (_message.Message,), {
  'DESCRIPTOR' : _CMDACTIONPARAM,
  '__module__' : 'action_param_cmd_pb2'
  # @@protoc_insertion_point(class_scope:easy_command.CmdActionParam)
  })
_sym_db.RegisterMessage(CmdActionParam)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
