# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_user_role.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_user_role.proto',
  package='role',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13get_user_role.proto\x12\x04role\"\"\n\x12GetUserRoleRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\"$\n\x13GetUserRoleResponse\x12\r\n\x05roles\x18\x01 \x03(\t\"w\n\x1aGetUserRoleResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\'\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x19.role.GetUserRoleResponseb\x06proto3')
)




_GETUSERROLEREQUEST = _descriptor.Descriptor(
  name='GetUserRoleRequest',
  full_name='role.GetUserRoleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='role.GetUserRoleRequest.user', index=0,
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
  serialized_start=29,
  serialized_end=63,
)


_GETUSERROLERESPONSE = _descriptor.Descriptor(
  name='GetUserRoleResponse',
  full_name='role.GetUserRoleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='roles', full_name='role.GetUserRoleResponse.roles', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=65,
  serialized_end=101,
)


_GETUSERROLERESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetUserRoleResponseWrapper',
  full_name='role.GetUserRoleResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='role.GetUserRoleResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='role.GetUserRoleResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='role.GetUserRoleResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='role.GetUserRoleResponseWrapper.data', index=3,
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
  serialized_start=103,
  serialized_end=222,
)

_GETUSERROLERESPONSEWRAPPER.fields_by_name['data'].message_type = _GETUSERROLERESPONSE
DESCRIPTOR.message_types_by_name['GetUserRoleRequest'] = _GETUSERROLEREQUEST
DESCRIPTOR.message_types_by_name['GetUserRoleResponse'] = _GETUSERROLERESPONSE
DESCRIPTOR.message_types_by_name['GetUserRoleResponseWrapper'] = _GETUSERROLERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetUserRoleRequest = _reflection.GeneratedProtocolMessageType('GetUserRoleRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERROLEREQUEST,
  '__module__' : 'get_user_role_pb2'
  # @@protoc_insertion_point(class_scope:role.GetUserRoleRequest)
  })
_sym_db.RegisterMessage(GetUserRoleRequest)

GetUserRoleResponse = _reflection.GeneratedProtocolMessageType('GetUserRoleResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERROLERESPONSE,
  '__module__' : 'get_user_role_pb2'
  # @@protoc_insertion_point(class_scope:role.GetUserRoleResponse)
  })
_sym_db.RegisterMessage(GetUserRoleResponse)

GetUserRoleResponseWrapper = _reflection.GeneratedProtocolMessageType('GetUserRoleResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERROLERESPONSEWRAPPER,
  '__module__' : 'get_user_role_pb2'
  # @@protoc_insertion_point(class_scope:role.GetUserRoleResponseWrapper)
  })
_sym_db.RegisterMessage(GetUserRoleResponseWrapper)


# @@protoc_insertion_point(module_scope)
