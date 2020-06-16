# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: create_win_patch.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='create_win_patch.proto',
  package='patch',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16\x63reate_win_patch.proto\x12\x05patch\"\xb8\x01\n\x15\x43reateWinPatchRequest\x12\x11\n\tarticleId\x18\x01 \x01(\t\x12\x11\n\tosVersion\x18\x02 \x03(\t\x12\x16\n\x0eosArchitecture\x18\x03 \x03(\t\x12\x15\n\rrequireReboot\x18\x04 \x01(\x08\x12\x13\n\x0breleaseTime\x18\x05 \x01(\t\x12\x0c\n\x04msrc\x18\x06 \x01(\t\x12\x0c\n\x04size\x18\x07 \x01(\x05\x12\x0c\n\x04memo\x18\x08 \x01(\t\x12\x0b\n\x03url\x18\t \x01(\t\",\n\x16\x43reateWinPatchResponse\x12\x12\n\ninstanceId\x18\x01 \x01(\t\"~\n\x1d\x43reateWinPatchResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12+\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1d.patch.CreateWinPatchResponseb\x06proto3')
)




_CREATEWINPATCHREQUEST = _descriptor.Descriptor(
  name='CreateWinPatchRequest',
  full_name='patch.CreateWinPatchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='articleId', full_name='patch.CreateWinPatchRequest.articleId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='osVersion', full_name='patch.CreateWinPatchRequest.osVersion', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='osArchitecture', full_name='patch.CreateWinPatchRequest.osArchitecture', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requireReboot', full_name='patch.CreateWinPatchRequest.requireReboot', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='releaseTime', full_name='patch.CreateWinPatchRequest.releaseTime', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msrc', full_name='patch.CreateWinPatchRequest.msrc', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='patch.CreateWinPatchRequest.size', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='patch.CreateWinPatchRequest.memo', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='patch.CreateWinPatchRequest.url', index=8,
      number=9, type=9, cpp_type=9, label=1,
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
  serialized_start=34,
  serialized_end=218,
)


_CREATEWINPATCHRESPONSE = _descriptor.Descriptor(
  name='CreateWinPatchResponse',
  full_name='patch.CreateWinPatchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='patch.CreateWinPatchResponse.instanceId', index=0,
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
  serialized_start=220,
  serialized_end=264,
)


_CREATEWINPATCHRESPONSEWRAPPER = _descriptor.Descriptor(
  name='CreateWinPatchResponseWrapper',
  full_name='patch.CreateWinPatchResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='patch.CreateWinPatchResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='patch.CreateWinPatchResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='patch.CreateWinPatchResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='patch.CreateWinPatchResponseWrapper.data', index=3,
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
  serialized_start=266,
  serialized_end=392,
)

_CREATEWINPATCHRESPONSEWRAPPER.fields_by_name['data'].message_type = _CREATEWINPATCHRESPONSE
DESCRIPTOR.message_types_by_name['CreateWinPatchRequest'] = _CREATEWINPATCHREQUEST
DESCRIPTOR.message_types_by_name['CreateWinPatchResponse'] = _CREATEWINPATCHRESPONSE
DESCRIPTOR.message_types_by_name['CreateWinPatchResponseWrapper'] = _CREATEWINPATCHRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateWinPatchRequest = _reflection.GeneratedProtocolMessageType('CreateWinPatchRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEWINPATCHREQUEST,
  '__module__' : 'create_win_patch_pb2'
  # @@protoc_insertion_point(class_scope:patch.CreateWinPatchRequest)
  })
_sym_db.RegisterMessage(CreateWinPatchRequest)

CreateWinPatchResponse = _reflection.GeneratedProtocolMessageType('CreateWinPatchResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEWINPATCHRESPONSE,
  '__module__' : 'create_win_patch_pb2'
  # @@protoc_insertion_point(class_scope:patch.CreateWinPatchResponse)
  })
_sym_db.RegisterMessage(CreateWinPatchResponse)

CreateWinPatchResponseWrapper = _reflection.GeneratedProtocolMessageType('CreateWinPatchResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _CREATEWINPATCHRESPONSEWRAPPER,
  '__module__' : 'create_win_patch_pb2'
  # @@protoc_insertion_point(class_scope:patch.CreateWinPatchResponseWrapper)
  })
_sym_db.RegisterMessage(CreateWinPatchResponseWrapper)


# @@protoc_insertion_point(module_scope)
