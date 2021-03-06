# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_user_info.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_user_info.proto',
  package='user_admin',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13get_user_info.proto\x12\nuser_admin\x1a\x1cgoogle/protobuf/struct.proto\"&\n\x12GetUserInfoRequest\x12\x10\n\x08username\x18\x01 \x01(\t\"u\n\x1aGetUserInfoResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12%\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Structb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_GETUSERINFOREQUEST = _descriptor.Descriptor(
  name='GetUserInfoRequest',
  full_name='user_admin.GetUserInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='user_admin.GetUserInfoRequest.username', index=0,
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
  serialized_start=65,
  serialized_end=103,
)


_GETUSERINFORESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetUserInfoResponseWrapper',
  full_name='user_admin.GetUserInfoResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='user_admin.GetUserInfoResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='user_admin.GetUserInfoResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='user_admin.GetUserInfoResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='user_admin.GetUserInfoResponseWrapper.data', index=3,
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
  serialized_start=105,
  serialized_end=222,
)

_GETUSERINFORESPONSEWRAPPER.fields_by_name['data'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['GetUserInfoRequest'] = _GETUSERINFOREQUEST
DESCRIPTOR.message_types_by_name['GetUserInfoResponseWrapper'] = _GETUSERINFORESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetUserInfoRequest = _reflection.GeneratedProtocolMessageType('GetUserInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERINFOREQUEST,
  '__module__' : 'get_user_info_pb2'
  # @@protoc_insertion_point(class_scope:user_admin.GetUserInfoRequest)
  })
_sym_db.RegisterMessage(GetUserInfoRequest)

GetUserInfoResponseWrapper = _reflection.GeneratedProtocolMessageType('GetUserInfoResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERINFORESPONSEWRAPPER,
  '__module__' : 'get_user_info_pb2'
  # @@protoc_insertion_point(class_scope:user_admin.GetUserInfoResponseWrapper)
  })
_sym_db.RegisterMessage(GetUserInfoResponseWrapper)


# @@protoc_insertion_point(module_scope)
