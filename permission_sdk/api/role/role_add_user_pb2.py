# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: role_add_user.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='role_add_user.proto',
  package='role',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13role_add_user.proto\x12\x04role\"6\n\x12RoleAddUserRequest\x12\x14\n\x0coperate_user\x18\x01 \x03(\t\x12\n\n\x02id\x18\x02 \x01(\t\"$\n\x13RoleAddUserResponse\x12\r\n\x05\x63ount\x18\x01 \x01(\x05\"w\n\x1aRoleAddUserResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\'\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x19.role.RoleAddUserResponseb\x06proto3')
)




_ROLEADDUSERREQUEST = _descriptor.Descriptor(
  name='RoleAddUserRequest',
  full_name='role.RoleAddUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operate_user', full_name='role.RoleAddUserRequest.operate_user', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='role.RoleAddUserRequest.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=29,
  serialized_end=83,
)


_ROLEADDUSERRESPONSE = _descriptor.Descriptor(
  name='RoleAddUserResponse',
  full_name='role.RoleAddUserResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='role.RoleAddUserResponse.count', index=0,
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
  serialized_start=85,
  serialized_end=121,
)


_ROLEADDUSERRESPONSEWRAPPER = _descriptor.Descriptor(
  name='RoleAddUserResponseWrapper',
  full_name='role.RoleAddUserResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='role.RoleAddUserResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='role.RoleAddUserResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='role.RoleAddUserResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='role.RoleAddUserResponseWrapper.data', index=3,
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
  serialized_start=123,
  serialized_end=242,
)

_ROLEADDUSERRESPONSEWRAPPER.fields_by_name['data'].message_type = _ROLEADDUSERRESPONSE
DESCRIPTOR.message_types_by_name['RoleAddUserRequest'] = _ROLEADDUSERREQUEST
DESCRIPTOR.message_types_by_name['RoleAddUserResponse'] = _ROLEADDUSERRESPONSE
DESCRIPTOR.message_types_by_name['RoleAddUserResponseWrapper'] = _ROLEADDUSERRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RoleAddUserRequest = _reflection.GeneratedProtocolMessageType('RoleAddUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROLEADDUSERREQUEST,
  '__module__' : 'role_add_user_pb2'
  # @@protoc_insertion_point(class_scope:role.RoleAddUserRequest)
  })
_sym_db.RegisterMessage(RoleAddUserRequest)

RoleAddUserResponse = _reflection.GeneratedProtocolMessageType('RoleAddUserResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROLEADDUSERRESPONSE,
  '__module__' : 'role_add_user_pb2'
  # @@protoc_insertion_point(class_scope:role.RoleAddUserResponse)
  })
_sym_db.RegisterMessage(RoleAddUserResponse)

RoleAddUserResponseWrapper = _reflection.GeneratedProtocolMessageType('RoleAddUserResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _ROLEADDUSERRESPONSEWRAPPER,
  '__module__' : 'role_add_user_pb2'
  # @@protoc_insertion_point(class_scope:role.RoleAddUserResponseWrapper)
  })
_sym_db.RegisterMessage(RoleAddUserResponseWrapper)


# @@protoc_insertion_point(module_scope)