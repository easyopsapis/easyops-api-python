# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: action_param_custom.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='action_param_custom.proto',
  package='easy_command',
  syntax='proto3',
  serialized_options=_b('ZFgo.easyops.local/contracts/protorepo-models/easyops/model/easy_command'),
  serialized_pb=_b('\n\x19\x61\x63tion_param_custom.proto\x12\x0c\x65\x61sy_command\"\"\n\x11\x41\x63tionParamCustom\x12\r\n\x05param\x18\x01 \x01(\tBHZFgo.easyops.local/contracts/protorepo-models/easyops/model/easy_commandb\x06proto3')
)




_ACTIONPARAMCUSTOM = _descriptor.Descriptor(
  name='ActionParamCustom',
  full_name='easy_command.ActionParamCustom',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='param', full_name='easy_command.ActionParamCustom.param', index=0,
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
  serialized_start=43,
  serialized_end=77,
)

DESCRIPTOR.message_types_by_name['ActionParamCustom'] = _ACTIONPARAMCUSTOM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ActionParamCustom = _reflection.GeneratedProtocolMessageType('ActionParamCustom', (_message.Message,), {
  'DESCRIPTOR' : _ACTIONPARAMCUSTOM,
  '__module__' : 'action_param_custom_pb2'
  # @@protoc_insertion_point(class_scope:easy_command.ActionParamCustom)
  })
_sym_db.RegisterMessage(ActionParamCustom)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
