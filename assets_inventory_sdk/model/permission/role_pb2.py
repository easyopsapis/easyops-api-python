# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: role.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='role.proto',
  package='permission',
  syntax='proto3',
  serialized_options=_b('ZDgo.easyops.local/contracts/protorepo-models/easyops/model/permission'),
  serialized_pb=_b('\n\nrole.proto\x12\npermission\"c\n\x04Role\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03org\x18\x02 \x01(\x05\x12\x0c\n\x04role\x18\x03 \x01(\t\x12\x0c\n\x04user\x18\x04 \x03(\t\x12\x12\n\npermission\x18\x05 \x03(\t\x12\x12\n\nuser_group\x18\x06 \x03(\tBFZDgo.easyops.local/contracts/protorepo-models/easyops/model/permissionb\x06proto3')
)




_ROLE = _descriptor.Descriptor(
  name='Role',
  full_name='permission.Role',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='permission.Role.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org', full_name='permission.Role.org', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='role', full_name='permission.Role.role', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='permission.Role.user', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='permission', full_name='permission.Role.permission', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_group', full_name='permission.Role.user_group', index=5,
      number=6, type=9, cpp_type=9, label=3,
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
  serialized_start=26,
  serialized_end=125,
)

DESCRIPTOR.message_types_by_name['Role'] = _ROLE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Role = _reflection.GeneratedProtocolMessageType('Role', (_message.Message,), {
  'DESCRIPTOR' : _ROLE,
  '__module__' : 'role_pb2'
  # @@protoc_insertion_point(class_scope:permission.Role)
  })
_sym_db.RegisterMessage(Role)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)