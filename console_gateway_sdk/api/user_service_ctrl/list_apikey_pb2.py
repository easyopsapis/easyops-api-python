# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list_apikey.proto

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
  name='list_apikey.proto',
  package='user_service_ctrl',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11list_apikey.proto\x12\x11user_service_ctrl\x1a\x1cgoogle/protobuf/struct.proto\"i\n\x12ListApiKeyResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\r\n\x05\x65rror\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\x12%\n\x04\x64\x61ta\x18\x04 \x03(\x0b\x32\x17.google.protobuf.Struct\"\x82\x01\n\x19ListApiKeyResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x33\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32%.user_service_ctrl.ListApiKeyResponseb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_LISTAPIKEYRESPONSE = _descriptor.Descriptor(
  name='ListApiKeyResponse',
  full_name='user_service_ctrl.ListApiKeyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='user_service_ctrl.ListApiKeyResponse.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='user_service_ctrl.ListApiKeyResponse.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='user_service_ctrl.ListApiKeyResponse.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='user_service_ctrl.ListApiKeyResponse.data', index=3,
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
  serialized_start=70,
  serialized_end=175,
)


_LISTAPIKEYRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListApiKeyResponseWrapper',
  full_name='user_service_ctrl.ListApiKeyResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='user_service_ctrl.ListApiKeyResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='user_service_ctrl.ListApiKeyResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='user_service_ctrl.ListApiKeyResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='user_service_ctrl.ListApiKeyResponseWrapper.data', index=3,
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
  serialized_start=178,
  serialized_end=308,
)

_LISTAPIKEYRESPONSE.fields_by_name['data'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_LISTAPIKEYRESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTAPIKEYRESPONSE
DESCRIPTOR.message_types_by_name['ListApiKeyResponse'] = _LISTAPIKEYRESPONSE
DESCRIPTOR.message_types_by_name['ListApiKeyResponseWrapper'] = _LISTAPIKEYRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListApiKeyResponse = _reflection.GeneratedProtocolMessageType('ListApiKeyResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTAPIKEYRESPONSE,
  '__module__' : 'list_apikey_pb2'
  # @@protoc_insertion_point(class_scope:user_service_ctrl.ListApiKeyResponse)
  })
_sym_db.RegisterMessage(ListApiKeyResponse)

ListApiKeyResponseWrapper = _reflection.GeneratedProtocolMessageType('ListApiKeyResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _LISTAPIKEYRESPONSEWRAPPER,
  '__module__' : 'list_apikey_pb2'
  # @@protoc_insertion_point(class_scope:user_service_ctrl.ListApiKeyResponseWrapper)
  })
_sym_db.RegisterMessage(ListApiKeyResponseWrapper)


# @@protoc_insertion_point(module_scope)
