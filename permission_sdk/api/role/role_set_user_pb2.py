# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: role_set_user.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='role_set_user.proto',
  package='role',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13role_set_user.proto\x12\x04role\"1\n\x12RoleSetUserRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\r\n\x05roles\x18\x02 \x03(\t\"$\n\x13RoleSetUserResponse\x12\r\n\x05\x63ount\x18\x01 \x01(\x05\"w\n\x1aRoleSetUserResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\'\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x19.role.RoleSetUserResponseb\x06proto3')
)




_ROLESETUSERREQUEST = _descriptor.Descriptor(
  name='RoleSetUserRequest',
  full_name='role.RoleSetUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='role.RoleSetUserRequest.user', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roles', full_name='role.RoleSetUserRequest.roles', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=29,
  serialized_end=78,
)


_ROLESETUSERRESPONSE = _descriptor.Descriptor(
  name='RoleSetUserResponse',
  full_name='role.RoleSetUserResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='role.RoleSetUserResponse.count', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=80,
  serialized_end=116,
)


_ROLESETUSERRESPONSEWRAPPER = _descriptor.Descriptor(
  name='RoleSetUserResponseWrapper',
  full_name='role.RoleSetUserResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='role.RoleSetUserResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='role.RoleSetUserResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='role.RoleSetUserResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='role.RoleSetUserResponseWrapper.data', index=3,
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
  serialized_start=118,
  serialized_end=237,
)

_ROLESETUSERRESPONSEWRAPPER.fields_by_name['data'].message_type = _ROLESETUSERRESPONSE
DESCRIPTOR.message_types_by_name['RoleSetUserRequest'] = _ROLESETUSERREQUEST
DESCRIPTOR.message_types_by_name['RoleSetUserResponse'] = _ROLESETUSERRESPONSE
DESCRIPTOR.message_types_by_name['RoleSetUserResponseWrapper'] = _ROLESETUSERRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RoleSetUserRequest = _reflection.GeneratedProtocolMessageType('RoleSetUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROLESETUSERREQUEST,
  '__module__' : 'role_set_user_pb2'
  # @@protoc_insertion_point(class_scope:role.RoleSetUserRequest)
  })
_sym_db.RegisterMessage(RoleSetUserRequest)

RoleSetUserResponse = _reflection.GeneratedProtocolMessageType('RoleSetUserResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROLESETUSERRESPONSE,
  '__module__' : 'role_set_user_pb2'
  # @@protoc_insertion_point(class_scope:role.RoleSetUserResponse)
  })
_sym_db.RegisterMessage(RoleSetUserResponse)

RoleSetUserResponseWrapper = _reflection.GeneratedProtocolMessageType('RoleSetUserResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _ROLESETUSERRESPONSEWRAPPER,
  '__module__' : 'role_set_user_pb2'
  # @@protoc_insertion_point(class_scope:role.RoleSetUserResponseWrapper)
  })
_sym_db.RegisterMessage(RoleSetUserResponseWrapper)


# @@protoc_insertion_point(module_scope)
