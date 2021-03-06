# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: win_patch.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='win_patch.proto',
  package='patch_manager',
  syntax='proto3',
  serialized_options=_b('ZGgo.easyops.local/contracts/protorepo-models/easyops/model/patch_manager'),
  serialized_pb=_b('\n\x0fwin_patch.proto\x12\rpatch_manager\"\xdf\x01\n\x08WinPatch\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tarticleId\x18\x03 \x01(\t\x12\x13\n\x0breleaseTime\x18\x04 \x01(\t\x12\x10\n\x08osSystem\x18\x05 \x01(\t\x12\x11\n\tosVersion\x18\x06 \x03(\t\x12\x16\n\x0eosArchitecture\x18\x07 \x03(\t\x12\x15\n\rrequireReboot\x18\x08 \x01(\x08\x12\x0c\n\x04msrc\x18\t \x01(\t\x12\x0c\n\x04size\x18\n \x01(\x05\x12\x0c\n\x04memo\x18\x0b \x01(\t\x12\x0b\n\x03url\x18\x0c \x01(\tBIZGgo.easyops.local/contracts/protorepo-models/easyops/model/patch_managerb\x06proto3')
)




_WINPATCH = _descriptor.Descriptor(
  name='WinPatch',
  full_name='patch_manager.WinPatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='patch_manager.WinPatch.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='patch_manager.WinPatch.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='articleId', full_name='patch_manager.WinPatch.articleId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='releaseTime', full_name='patch_manager.WinPatch.releaseTime', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='osSystem', full_name='patch_manager.WinPatch.osSystem', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='osVersion', full_name='patch_manager.WinPatch.osVersion', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='osArchitecture', full_name='patch_manager.WinPatch.osArchitecture', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requireReboot', full_name='patch_manager.WinPatch.requireReboot', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msrc', full_name='patch_manager.WinPatch.msrc', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='patch_manager.WinPatch.size', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='patch_manager.WinPatch.memo', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='patch_manager.WinPatch.url', index=11,
      number=12, type=9, cpp_type=9, label=1,
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
  serialized_start=35,
  serialized_end=258,
)

DESCRIPTOR.message_types_by_name['WinPatch'] = _WINPATCH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WinPatch = _reflection.GeneratedProtocolMessageType('WinPatch', (_message.Message,), {
  'DESCRIPTOR' : _WINPATCH,
  '__module__' : 'win_patch_pb2'
  # @@protoc_insertion_point(class_scope:patch_manager.WinPatch)
  })
_sym_db.RegisterMessage(WinPatch)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
