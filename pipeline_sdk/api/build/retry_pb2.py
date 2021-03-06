# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: retry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='retry.proto',
  package='build',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0bretry.proto\x12\x05\x62uild\" \n\x0cRetryRequest\x12\x10\n\x08\x62uild_id\x18\x01 \x01(\t\"\x1b\n\rRetryResponse\x12\n\n\x02id\x18\x01 \x01(\t\"l\n\x14RetryResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\"\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x14.build.RetryResponseb\x06proto3')
)




_RETRYREQUEST = _descriptor.Descriptor(
  name='RetryRequest',
  full_name='build.RetryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='build_id', full_name='build.RetryRequest.build_id', index=0,
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
  serialized_start=22,
  serialized_end=54,
)


_RETRYRESPONSE = _descriptor.Descriptor(
  name='RetryResponse',
  full_name='build.RetryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='build.RetryResponse.id', index=0,
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
  serialized_start=56,
  serialized_end=83,
)


_RETRYRESPONSEWRAPPER = _descriptor.Descriptor(
  name='RetryResponseWrapper',
  full_name='build.RetryResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='build.RetryResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='build.RetryResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='build.RetryResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='build.RetryResponseWrapper.data', index=3,
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
  serialized_start=85,
  serialized_end=193,
)

_RETRYRESPONSEWRAPPER.fields_by_name['data'].message_type = _RETRYRESPONSE
DESCRIPTOR.message_types_by_name['RetryRequest'] = _RETRYREQUEST
DESCRIPTOR.message_types_by_name['RetryResponse'] = _RETRYRESPONSE
DESCRIPTOR.message_types_by_name['RetryResponseWrapper'] = _RETRYRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RetryRequest = _reflection.GeneratedProtocolMessageType('RetryRequest', (_message.Message,), {
  'DESCRIPTOR' : _RETRYREQUEST,
  '__module__' : 'retry_pb2'
  # @@protoc_insertion_point(class_scope:build.RetryRequest)
  })
_sym_db.RegisterMessage(RetryRequest)

RetryResponse = _reflection.GeneratedProtocolMessageType('RetryResponse', (_message.Message,), {
  'DESCRIPTOR' : _RETRYRESPONSE,
  '__module__' : 'retry_pb2'
  # @@protoc_insertion_point(class_scope:build.RetryResponse)
  })
_sym_db.RegisterMessage(RetryResponse)

RetryResponseWrapper = _reflection.GeneratedProtocolMessageType('RetryResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _RETRYRESPONSEWRAPPER,
  '__module__' : 'retry_pb2'
  # @@protoc_insertion_point(class_scope:build.RetryResponseWrapper)
  })
_sym_db.RegisterMessage(RetryResponseWrapper)


# @@protoc_insertion_point(module_scope)
