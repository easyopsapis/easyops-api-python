# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_password_conf.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_password_conf.proto',
  package='user_admin',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x17get_password_conf.proto\x12\nuser_admin\"?\n\x19GetPasswordConfigResponse\x12\r\n\x05regex\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"\x89\x01\n GetPasswordConfigResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x33\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32%.user_admin.GetPasswordConfigResponseb\x06proto3')
)




_GETPASSWORDCONFIGRESPONSE = _descriptor.Descriptor(
  name='GetPasswordConfigResponse',
  full_name='user_admin.GetPasswordConfigResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='regex', full_name='user_admin.GetPasswordConfigResponse.regex', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='user_admin.GetPasswordConfigResponse.description', index=1,
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
  serialized_start=39,
  serialized_end=102,
)


_GETPASSWORDCONFIGRESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetPasswordConfigResponseWrapper',
  full_name='user_admin.GetPasswordConfigResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='user_admin.GetPasswordConfigResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='user_admin.GetPasswordConfigResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='user_admin.GetPasswordConfigResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='user_admin.GetPasswordConfigResponseWrapper.data', index=3,
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
  serialized_end=242,
)

_GETPASSWORDCONFIGRESPONSEWRAPPER.fields_by_name['data'].message_type = _GETPASSWORDCONFIGRESPONSE
DESCRIPTOR.message_types_by_name['GetPasswordConfigResponse'] = _GETPASSWORDCONFIGRESPONSE
DESCRIPTOR.message_types_by_name['GetPasswordConfigResponseWrapper'] = _GETPASSWORDCONFIGRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetPasswordConfigResponse = _reflection.GeneratedProtocolMessageType('GetPasswordConfigResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPASSWORDCONFIGRESPONSE,
  '__module__' : 'get_password_conf_pb2'
  # @@protoc_insertion_point(class_scope:user_admin.GetPasswordConfigResponse)
  })
_sym_db.RegisterMessage(GetPasswordConfigResponse)

GetPasswordConfigResponseWrapper = _reflection.GeneratedProtocolMessageType('GetPasswordConfigResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _GETPASSWORDCONFIGRESPONSEWRAPPER,
  '__module__' : 'get_password_conf_pb2'
  # @@protoc_insertion_point(class_scope:user_admin.GetPasswordConfigResponseWrapper)
  })
_sym_db.RegisterMessage(GetPasswordConfigResponseWrapper)


# @@protoc_insertion_point(module_scope)
