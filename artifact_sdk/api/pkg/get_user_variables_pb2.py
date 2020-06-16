# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_user_variables.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_user_variables.proto',
  package='pkg',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x18get_user_variables.proto\x12\x03pkg\"6\n\x18GetUserVariablesResponse\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x80\x01\n\x1fGetUserVariablesResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12+\n\x04\x64\x61ta\x18\x04 \x03(\x0b\x32\x1d.pkg.GetUserVariablesResponseb\x06proto3')
)




_GETUSERVARIABLESRESPONSE = _descriptor.Descriptor(
  name='GetUserVariablesResponse',
  full_name='pkg.GetUserVariablesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='pkg.GetUserVariablesResponse.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='pkg.GetUserVariablesResponse.value', index=1,
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
  serialized_start=33,
  serialized_end=87,
)


_GETUSERVARIABLESRESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetUserVariablesResponseWrapper',
  full_name='pkg.GetUserVariablesResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='pkg.GetUserVariablesResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='pkg.GetUserVariablesResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='pkg.GetUserVariablesResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='pkg.GetUserVariablesResponseWrapper.data', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=90,
  serialized_end=218,
)

_GETUSERVARIABLESRESPONSEWRAPPER.fields_by_name['data'].message_type = _GETUSERVARIABLESRESPONSE
DESCRIPTOR.message_types_by_name['GetUserVariablesResponse'] = _GETUSERVARIABLESRESPONSE
DESCRIPTOR.message_types_by_name['GetUserVariablesResponseWrapper'] = _GETUSERVARIABLESRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetUserVariablesResponse = _reflection.GeneratedProtocolMessageType('GetUserVariablesResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERVARIABLESRESPONSE,
  '__module__' : 'get_user_variables_pb2'
  # @@protoc_insertion_point(class_scope:pkg.GetUserVariablesResponse)
  })
_sym_db.RegisterMessage(GetUserVariablesResponse)

GetUserVariablesResponseWrapper = _reflection.GeneratedProtocolMessageType('GetUserVariablesResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERVARIABLESRESPONSEWRAPPER,
  '__module__' : 'get_user_variables_pb2'
  # @@protoc_insertion_point(class_scope:pkg.GetUserVariablesResponseWrapper)
  })
_sym_db.RegisterMessage(GetUserVariablesResponseWrapper)


# @@protoc_insertion_point(module_scope)
