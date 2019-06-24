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
  package='user_admin',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13user_register.proto\x12\nuser_admin\"T\n\x13UserRegisterRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x0e\n\x06invite\x18\x04 \x01(\t\"@\n\x14UserRegisterResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x0b\n\x03org\x18\x03 \x01(\x05\"\x7f\n\x1bUserRegisterResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12.\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32 .user_admin.UserRegisterResponseb\x06proto3')
)




_USERREGISTERREQUEST = _descriptor.Descriptor(
  name='UserRegisterRequest',
  full_name='user_admin.UserRegisterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='user_admin.UserRegisterRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='user_admin.UserRegisterRequest.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='user_admin.UserRegisterRequest.email', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='invite', full_name='user_admin.UserRegisterRequest.invite', index=3,
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
  serialized_start=35,
  serialized_end=119,
)


_USERREGISTERRESPONSE = _descriptor.Descriptor(
  name='UserRegisterResponse',
  full_name='user_admin.UserRegisterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='user_admin.UserRegisterResponse.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='user_admin.UserRegisterResponse.email', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org', full_name='user_admin.UserRegisterResponse.org', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=121,
  serialized_end=185,
)


_USERREGISTERRESPONSEWRAPPER = _descriptor.Descriptor(
  name='UserRegisterResponseWrapper',
  full_name='user_admin.UserRegisterResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='user_admin.UserRegisterResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='user_admin.UserRegisterResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='user_admin.UserRegisterResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='user_admin.UserRegisterResponseWrapper.data', index=3,
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
  serialized_start=187,
  serialized_end=314,
)

_USERREGISTERRESPONSEWRAPPER.fields_by_name['data'].message_type = _USERREGISTERRESPONSE
DESCRIPTOR.message_types_by_name['UserRegisterRequest'] = _USERREGISTERREQUEST
DESCRIPTOR.message_types_by_name['UserRegisterResponse'] = _USERREGISTERRESPONSE
DESCRIPTOR.message_types_by_name['UserRegisterResponseWrapper'] = _USERREGISTERRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserRegisterRequest = _reflection.GeneratedProtocolMessageType('UserRegisterRequest', (_message.Message,), dict(
  DESCRIPTOR = _USERREGISTERREQUEST,
  __module__ = 'user_register_pb2'
  # @@protoc_insertion_point(class_scope:user_admin.UserRegisterRequest)
  ))
_sym_db.RegisterMessage(UserRegisterRequest)

UserRegisterResponse = _reflection.GeneratedProtocolMessageType('UserRegisterResponse', (_message.Message,), dict(
  DESCRIPTOR = _USERREGISTERRESPONSE,
  __module__ = 'user_register_pb2'
  # @@protoc_insertion_point(class_scope:user_admin.UserRegisterResponse)
  ))
_sym_db.RegisterMessage(UserRegisterResponse)

UserRegisterResponseWrapper = _reflection.GeneratedProtocolMessageType('UserRegisterResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _USERREGISTERRESPONSEWRAPPER,
  __module__ = 'user_register_pb2'
  # @@protoc_insertion_point(class_scope:user_admin.UserRegisterResponseWrapper)
  ))
_sym_db.RegisterMessage(UserRegisterResponseWrapper)


# @@protoc_insertion_point(module_scope)