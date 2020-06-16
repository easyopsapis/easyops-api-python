# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: forgot_password.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='forgot_password.proto',
  package='user_admin',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x15\x66orgot_password.proto\x12\nuser_admin\x1a\x1bgoogle/protobuf/empty.proto\"3\n\x15\x46orgotPasswordRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\"w\n\x1d\x46orgotPasswordResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12$\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x16.google.protobuf.Emptyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_FORGOTPASSWORDREQUEST = _descriptor.Descriptor(
  name='ForgotPasswordRequest',
  full_name='user_admin.ForgotPasswordRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='user_admin.ForgotPasswordRequest.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='user_admin.ForgotPasswordRequest.url', index=1,
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
  serialized_start=66,
  serialized_end=117,
)


_FORGOTPASSWORDRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ForgotPasswordResponseWrapper',
  full_name='user_admin.ForgotPasswordResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='user_admin.ForgotPasswordResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='user_admin.ForgotPasswordResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='user_admin.ForgotPasswordResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='user_admin.ForgotPasswordResponseWrapper.data', index=3,
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
  serialized_start=119,
  serialized_end=238,
)

_FORGOTPASSWORDRESPONSEWRAPPER.fields_by_name['data'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
DESCRIPTOR.message_types_by_name['ForgotPasswordRequest'] = _FORGOTPASSWORDREQUEST
DESCRIPTOR.message_types_by_name['ForgotPasswordResponseWrapper'] = _FORGOTPASSWORDRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ForgotPasswordRequest = _reflection.GeneratedProtocolMessageType('ForgotPasswordRequest', (_message.Message,), {
  'DESCRIPTOR' : _FORGOTPASSWORDREQUEST,
  '__module__' : 'forgot_password_pb2'
  # @@protoc_insertion_point(class_scope:user_admin.ForgotPasswordRequest)
  })
_sym_db.RegisterMessage(ForgotPasswordRequest)

ForgotPasswordResponseWrapper = _reflection.GeneratedProtocolMessageType('ForgotPasswordResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _FORGOTPASSWORDRESPONSEWRAPPER,
  '__module__' : 'forgot_password_pb2'
  # @@protoc_insertion_point(class_scope:user_admin.ForgotPasswordResponseWrapper)
  })
_sym_db.RegisterMessage(ForgotPasswordResponseWrapper)


# @@protoc_insertion_point(module_scope)
