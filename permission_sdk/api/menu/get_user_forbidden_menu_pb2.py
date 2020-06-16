# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_user_forbidden_menu.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_user_forbidden_menu.proto',
  package='menu',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1dget_user_forbidden_menu.proto\x12\x04menu\"/\n\x1bGetUserForbiddenMenuRequest\x12\x10\n\x08username\x18\x01 \x01(\t\"6\n\x1cGetUserForbiddenMenuResponse\x12\x16\n\x0e\x66orbidden_menu\x18\x01 \x03(\t\"\x89\x01\n#GetUserForbiddenMenuResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x30\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\".menu.GetUserForbiddenMenuResponseb\x06proto3')
)




_GETUSERFORBIDDENMENUREQUEST = _descriptor.Descriptor(
  name='GetUserForbiddenMenuRequest',
  full_name='menu.GetUserForbiddenMenuRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='menu.GetUserForbiddenMenuRequest.username', index=0,
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
  serialized_start=39,
  serialized_end=86,
)


_GETUSERFORBIDDENMENURESPONSE = _descriptor.Descriptor(
  name='GetUserForbiddenMenuResponse',
  full_name='menu.GetUserForbiddenMenuResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='forbidden_menu', full_name='menu.GetUserForbiddenMenuResponse.forbidden_menu', index=0,
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
  serialized_start=88,
  serialized_end=142,
)


_GETUSERFORBIDDENMENURESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetUserForbiddenMenuResponseWrapper',
  full_name='menu.GetUserForbiddenMenuResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='menu.GetUserForbiddenMenuResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='menu.GetUserForbiddenMenuResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='menu.GetUserForbiddenMenuResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='menu.GetUserForbiddenMenuResponseWrapper.data', index=3,
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
  serialized_start=145,
  serialized_end=282,
)

_GETUSERFORBIDDENMENURESPONSEWRAPPER.fields_by_name['data'].message_type = _GETUSERFORBIDDENMENURESPONSE
DESCRIPTOR.message_types_by_name['GetUserForbiddenMenuRequest'] = _GETUSERFORBIDDENMENUREQUEST
DESCRIPTOR.message_types_by_name['GetUserForbiddenMenuResponse'] = _GETUSERFORBIDDENMENURESPONSE
DESCRIPTOR.message_types_by_name['GetUserForbiddenMenuResponseWrapper'] = _GETUSERFORBIDDENMENURESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetUserForbiddenMenuRequest = _reflection.GeneratedProtocolMessageType('GetUserForbiddenMenuRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERFORBIDDENMENUREQUEST,
  '__module__' : 'get_user_forbidden_menu_pb2'
  # @@protoc_insertion_point(class_scope:menu.GetUserForbiddenMenuRequest)
  })
_sym_db.RegisterMessage(GetUserForbiddenMenuRequest)

GetUserForbiddenMenuResponse = _reflection.GeneratedProtocolMessageType('GetUserForbiddenMenuResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERFORBIDDENMENURESPONSE,
  '__module__' : 'get_user_forbidden_menu_pb2'
  # @@protoc_insertion_point(class_scope:menu.GetUserForbiddenMenuResponse)
  })
_sym_db.RegisterMessage(GetUserForbiddenMenuResponse)

GetUserForbiddenMenuResponseWrapper = _reflection.GeneratedProtocolMessageType('GetUserForbiddenMenuResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERFORBIDDENMENURESPONSEWRAPPER,
  '__module__' : 'get_user_forbidden_menu_pb2'
  # @@protoc_insertion_point(class_scope:menu.GetUserForbiddenMenuResponseWrapper)
  })
_sym_db.RegisterMessage(GetUserForbiddenMenuResponseWrapper)


# @@protoc_insertion_point(module_scope)