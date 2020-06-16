# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: users_register.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='users_register.proto',
  package='gateway',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14users_register.proto\x12\x07gateway\"T\n\x13UserRegisterRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x0e\n\x06invite\x18\x04 \x01(\t\"T\n\x14UserRegisterResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x0b\n\x03org\x18\x03 \x01(\x05\x12\x12\n\ninstanceId\x18\x04 \x01(\t\"|\n\x1bUserRegisterResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12+\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1d.gateway.UserRegisterResponseb\x06proto3')
)




_USERREGISTERREQUEST = _descriptor.Descriptor(
  name='UserRegisterRequest',
  full_name='gateway.UserRegisterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='gateway.UserRegisterRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='gateway.UserRegisterRequest.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='gateway.UserRegisterRequest.email', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='invite', full_name='gateway.UserRegisterRequest.invite', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=33,
  serialized_end=117,
)


_USERREGISTERRESPONSE = _descriptor.Descriptor(
  name='UserRegisterResponse',
  full_name='gateway.UserRegisterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='gateway.UserRegisterResponse.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='gateway.UserRegisterResponse.email', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org', full_name='gateway.UserRegisterResponse.org', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='gateway.UserRegisterResponse.instanceId', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=119,
  serialized_end=203,
)


_USERREGISTERRESPONSEWRAPPER = _descriptor.Descriptor(
  name='UserRegisterResponseWrapper',
  full_name='gateway.UserRegisterResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='gateway.UserRegisterResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='gateway.UserRegisterResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='gateway.UserRegisterResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='gateway.UserRegisterResponseWrapper.data', index=3,
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
  serialized_start=205,
  serialized_end=329,
)

_USERREGISTERRESPONSEWRAPPER.fields_by_name['data'].message_type = _USERREGISTERRESPONSE
DESCRIPTOR.message_types_by_name['UserRegisterRequest'] = _USERREGISTERREQUEST
DESCRIPTOR.message_types_by_name['UserRegisterResponse'] = _USERREGISTERRESPONSE
DESCRIPTOR.message_types_by_name['UserRegisterResponseWrapper'] = _USERREGISTERRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserRegisterRequest = _reflection.GeneratedProtocolMessageType('UserRegisterRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERREGISTERREQUEST,
  '__module__' : 'users_register_pb2'
  # @@protoc_insertion_point(class_scope:gateway.UserRegisterRequest)
  })
_sym_db.RegisterMessage(UserRegisterRequest)

UserRegisterResponse = _reflection.GeneratedProtocolMessageType('UserRegisterResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERREGISTERRESPONSE,
  '__module__' : 'users_register_pb2'
  # @@protoc_insertion_point(class_scope:gateway.UserRegisterResponse)
  })
_sym_db.RegisterMessage(UserRegisterResponse)

UserRegisterResponseWrapper = _reflection.GeneratedProtocolMessageType('UserRegisterResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _USERREGISTERRESPONSEWRAPPER,
  '__module__' : 'users_register_pb2'
  # @@protoc_insertion_point(class_scope:gateway.UserRegisterResponseWrapper)
  })
_sym_db.RegisterMessage(UserRegisterResponseWrapper)


# @@protoc_insertion_point(module_scope)