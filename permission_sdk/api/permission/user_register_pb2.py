# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user_register.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='user_register.proto',
  package='permission',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13user_register.proto\x12\npermission\"5\n\x13UserRegisterRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08is_admin\x18\x02 \x01(\x08\"1\n\x14UserRegisterResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\"\x7f\n\x1bUserRegisterResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12.\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32 .permission.UserRegisterResponseb\x06proto3')
)




_USERREGISTERREQUEST = _descriptor.Descriptor(
  name='UserRegisterRequest',
  full_name='permission.UserRegisterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='permission.UserRegisterRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_admin', full_name='permission.UserRegisterRequest.is_admin', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_end=88,
)


_USERREGISTERRESPONSE = _descriptor.Descriptor(
  name='UserRegisterResponse',
  full_name='permission.UserRegisterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='permission.UserRegisterResponse.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='permission.UserRegisterResponse.msg', index=1,
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
  serialized_start=90,
  serialized_end=139,
)


_USERREGISTERRESPONSEWRAPPER = _descriptor.Descriptor(
  name='UserRegisterResponseWrapper',
  full_name='permission.UserRegisterResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='permission.UserRegisterResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='permission.UserRegisterResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='permission.UserRegisterResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='permission.UserRegisterResponseWrapper.data', index=3,
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
  serialized_start=141,
  serialized_end=268,
)

_USERREGISTERRESPONSEWRAPPER.fields_by_name['data'].message_type = _USERREGISTERRESPONSE
DESCRIPTOR.message_types_by_name['UserRegisterRequest'] = _USERREGISTERREQUEST
DESCRIPTOR.message_types_by_name['UserRegisterResponse'] = _USERREGISTERRESPONSE
DESCRIPTOR.message_types_by_name['UserRegisterResponseWrapper'] = _USERREGISTERRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserRegisterRequest = _reflection.GeneratedProtocolMessageType('UserRegisterRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERREGISTERREQUEST,
  '__module__' : 'user_register_pb2'
  # @@protoc_insertion_point(class_scope:permission.UserRegisterRequest)
  })
_sym_db.RegisterMessage(UserRegisterRequest)

UserRegisterResponse = _reflection.GeneratedProtocolMessageType('UserRegisterResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERREGISTERRESPONSE,
  '__module__' : 'user_register_pb2'
  # @@protoc_insertion_point(class_scope:permission.UserRegisterResponse)
  })
_sym_db.RegisterMessage(UserRegisterResponse)

UserRegisterResponseWrapper = _reflection.GeneratedProtocolMessageType('UserRegisterResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _USERREGISTERRESPONSEWRAPPER,
  '__module__' : 'user_register_pb2'
  # @@protoc_insertion_point(class_scope:permission.UserRegisterResponseWrapper)
  })
_sym_db.RegisterMessage(UserRegisterResponseWrapper)


# @@protoc_insertion_point(module_scope)