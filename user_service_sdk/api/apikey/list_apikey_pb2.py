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




DESCRIPTOR = _descriptor.FileDescriptor(
  name='list_apikey.proto',
  package='apikey',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11list_apikey.proto\x12\x06\x61pikey\"4\n\x11ListApiKeyRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\"\xe8\x01\n\x12ListApiKeyResponse\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12-\n\x04list\x18\x04 \x03(\x0b\x32\x1f.apikey.ListApiKeyResponse.List\x1as\n\x04List\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x12\n\naccess_key\x18\x02 \x01(\t\x12\x12\n\nsecret_key\x18\x03 \x01(\t\x12\r\n\x05state\x18\x04 \x01(\t\x12\x0b\n\x03org\x18\x05 \x01(\x05\x12\r\n\x05\x63time\x18\x06 \x01(\t\x12\n\n\x02ts\x18\x07 \x01(\x05\"w\n\x19ListApiKeyResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12(\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1a.apikey.ListApiKeyResponseb\x06proto3')
)




_LISTAPIKEYREQUEST = _descriptor.Descriptor(
  name='ListApiKeyRequest',
  full_name='apikey.ListApiKeyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='apikey.ListApiKeyRequest.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='apikey.ListApiKeyRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=29,
  serialized_end=81,
)


_LISTAPIKEYRESPONSE_LIST = _descriptor.Descriptor(
  name='List',
  full_name='apikey.ListApiKeyResponse.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='apikey.ListApiKeyResponse.List.user', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='access_key', full_name='apikey.ListApiKeyResponse.List.access_key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secret_key', full_name='apikey.ListApiKeyResponse.List.secret_key', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='apikey.ListApiKeyResponse.List.state', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org', full_name='apikey.ListApiKeyResponse.List.org', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='apikey.ListApiKeyResponse.List.ctime', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ts', full_name='apikey.ListApiKeyResponse.List.ts', index=6,
      number=7, type=5, cpp_type=1, label=1,
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
  serialized_start=201,
  serialized_end=316,
)

_LISTAPIKEYRESPONSE = _descriptor.Descriptor(
  name='ListApiKeyResponse',
  full_name='apikey.ListApiKeyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='apikey.ListApiKeyResponse.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='apikey.ListApiKeyResponse.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='apikey.ListApiKeyResponse.total', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='apikey.ListApiKeyResponse.list', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTAPIKEYRESPONSE_LIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=84,
  serialized_end=316,
)


_LISTAPIKEYRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListApiKeyResponseWrapper',
  full_name='apikey.ListApiKeyResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='apikey.ListApiKeyResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='apikey.ListApiKeyResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='apikey.ListApiKeyResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='apikey.ListApiKeyResponseWrapper.data', index=3,
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
  serialized_start=318,
  serialized_end=437,
)

_LISTAPIKEYRESPONSE_LIST.containing_type = _LISTAPIKEYRESPONSE
_LISTAPIKEYRESPONSE.fields_by_name['list'].message_type = _LISTAPIKEYRESPONSE_LIST
_LISTAPIKEYRESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTAPIKEYRESPONSE
DESCRIPTOR.message_types_by_name['ListApiKeyRequest'] = _LISTAPIKEYREQUEST
DESCRIPTOR.message_types_by_name['ListApiKeyResponse'] = _LISTAPIKEYRESPONSE
DESCRIPTOR.message_types_by_name['ListApiKeyResponseWrapper'] = _LISTAPIKEYRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListApiKeyRequest = _reflection.GeneratedProtocolMessageType('ListApiKeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTAPIKEYREQUEST,
  '__module__' : 'list_apikey_pb2'
  # @@protoc_insertion_point(class_scope:apikey.ListApiKeyRequest)
  })
_sym_db.RegisterMessage(ListApiKeyRequest)

ListApiKeyResponse = _reflection.GeneratedProtocolMessageType('ListApiKeyResponse', (_message.Message,), {

  'List' : _reflection.GeneratedProtocolMessageType('List', (_message.Message,), {
    'DESCRIPTOR' : _LISTAPIKEYRESPONSE_LIST,
    '__module__' : 'list_apikey_pb2'
    # @@protoc_insertion_point(class_scope:apikey.ListApiKeyResponse.List)
    })
  ,
  'DESCRIPTOR' : _LISTAPIKEYRESPONSE,
  '__module__' : 'list_apikey_pb2'
  # @@protoc_insertion_point(class_scope:apikey.ListApiKeyResponse)
  })
_sym_db.RegisterMessage(ListApiKeyResponse)
_sym_db.RegisterMessage(ListApiKeyResponse.List)

ListApiKeyResponseWrapper = _reflection.GeneratedProtocolMessageType('ListApiKeyResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _LISTAPIKEYRESPONSEWRAPPER,
  '__module__' : 'list_apikey_pb2'
  # @@protoc_insertion_point(class_scope:apikey.ListApiKeyResponseWrapper)
  })
_sym_db.RegisterMessage(ListApiKeyResponseWrapper)


# @@protoc_insertion_point(module_scope)
