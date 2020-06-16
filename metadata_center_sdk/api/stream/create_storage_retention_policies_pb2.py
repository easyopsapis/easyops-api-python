# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: create_storage_retention_policies.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='create_storage_retention_policies.proto',
  package='stream',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\'create_storage_retention_policies.proto\x12\x06stream\"\x90\x01\n&CreateStorageRetentionPoliciesResponse\x12\x41\n\x04list\x18\x01 \x03(\x0b\x32\x33.stream.CreateStorageRetentionPoliciesResponse.List\x1a#\n\x04List\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x05\"\x9f\x01\n-CreateStorageRetentionPoliciesResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12<\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32..stream.CreateStorageRetentionPoliciesResponseb\x06proto3')
)




_CREATESTORAGERETENTIONPOLICIESRESPONSE_LIST = _descriptor.Descriptor(
  name='List',
  full_name='stream.CreateStorageRetentionPoliciesResponse.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='stream.CreateStorageRetentionPoliciesResponse.List.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='stream.CreateStorageRetentionPoliciesResponse.List.version', index=1,
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
  serialized_start=161,
  serialized_end=196,
)

_CREATESTORAGERETENTIONPOLICIESRESPONSE = _descriptor.Descriptor(
  name='CreateStorageRetentionPoliciesResponse',
  full_name='stream.CreateStorageRetentionPoliciesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='list', full_name='stream.CreateStorageRetentionPoliciesResponse.list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CREATESTORAGERETENTIONPOLICIESRESPONSE_LIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=52,
  serialized_end=196,
)


_CREATESTORAGERETENTIONPOLICIESRESPONSEWRAPPER = _descriptor.Descriptor(
  name='CreateStorageRetentionPoliciesResponseWrapper',
  full_name='stream.CreateStorageRetentionPoliciesResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='stream.CreateStorageRetentionPoliciesResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='stream.CreateStorageRetentionPoliciesResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='stream.CreateStorageRetentionPoliciesResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='stream.CreateStorageRetentionPoliciesResponseWrapper.data', index=3,
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
  serialized_start=199,
  serialized_end=358,
)

_CREATESTORAGERETENTIONPOLICIESRESPONSE_LIST.containing_type = _CREATESTORAGERETENTIONPOLICIESRESPONSE
_CREATESTORAGERETENTIONPOLICIESRESPONSE.fields_by_name['list'].message_type = _CREATESTORAGERETENTIONPOLICIESRESPONSE_LIST
_CREATESTORAGERETENTIONPOLICIESRESPONSEWRAPPER.fields_by_name['data'].message_type = _CREATESTORAGERETENTIONPOLICIESRESPONSE
DESCRIPTOR.message_types_by_name['CreateStorageRetentionPoliciesResponse'] = _CREATESTORAGERETENTIONPOLICIESRESPONSE
DESCRIPTOR.message_types_by_name['CreateStorageRetentionPoliciesResponseWrapper'] = _CREATESTORAGERETENTIONPOLICIESRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateStorageRetentionPoliciesResponse = _reflection.GeneratedProtocolMessageType('CreateStorageRetentionPoliciesResponse', (_message.Message,), {

  'List' : _reflection.GeneratedProtocolMessageType('List', (_message.Message,), {
    'DESCRIPTOR' : _CREATESTORAGERETENTIONPOLICIESRESPONSE_LIST,
    '__module__' : 'create_storage_retention_policies_pb2'
    # @@protoc_insertion_point(class_scope:stream.CreateStorageRetentionPoliciesResponse.List)
    })
  ,
  'DESCRIPTOR' : _CREATESTORAGERETENTIONPOLICIESRESPONSE,
  '__module__' : 'create_storage_retention_policies_pb2'
  # @@protoc_insertion_point(class_scope:stream.CreateStorageRetentionPoliciesResponse)
  })
_sym_db.RegisterMessage(CreateStorageRetentionPoliciesResponse)
_sym_db.RegisterMessage(CreateStorageRetentionPoliciesResponse.List)

CreateStorageRetentionPoliciesResponseWrapper = _reflection.GeneratedProtocolMessageType('CreateStorageRetentionPoliciesResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _CREATESTORAGERETENTIONPOLICIESRESPONSEWRAPPER,
  '__module__' : 'create_storage_retention_policies_pb2'
  # @@protoc_insertion_point(class_scope:stream.CreateStorageRetentionPoliciesResponseWrapper)
  })
_sym_db.RegisterMessage(CreateStorageRetentionPoliciesResponseWrapper)


# @@protoc_insertion_point(module_scope)