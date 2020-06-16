# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: create_toolkit.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cmdb_extend_sdk.model.cmdb_extend import toolkit_pb2 as cmdb__extend__sdk_dot_model_dot_cmdb__extend_dot_toolkit__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='create_toolkit.proto',
  package='toolkit',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14\x63reate_toolkit.proto\x12\x07toolkit\x1a/cmdb_extend_sdk/model/cmdb_extend/toolkit.proto\x1a\x1cgoogle/protobuf/struct.proto\"O\n\x14\x43reateToolkitRequest\x12\x10\n\x08objectId\x18\x01 \x01(\t\x12%\n\x07toolkit\x18\x02 \x01(\x0b\x32\x14.cmdb_extend.Toolkit\"t\n\x1c\x43reateToolkitResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\"\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x14.cmdb_extend.Toolkitb\x06proto3')
  ,
  dependencies=[cmdb__extend__sdk_dot_model_dot_cmdb__extend_dot_toolkit__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_CREATETOOLKITREQUEST = _descriptor.Descriptor(
  name='CreateToolkitRequest',
  full_name='toolkit.CreateToolkitRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='objectId', full_name='toolkit.CreateToolkitRequest.objectId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='toolkit', full_name='toolkit.CreateToolkitRequest.toolkit', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=112,
  serialized_end=191,
)


_CREATETOOLKITRESPONSEWRAPPER = _descriptor.Descriptor(
  name='CreateToolkitResponseWrapper',
  full_name='toolkit.CreateToolkitResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='toolkit.CreateToolkitResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='toolkit.CreateToolkitResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='toolkit.CreateToolkitResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='toolkit.CreateToolkitResponseWrapper.data', index=3,
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
  serialized_start=193,
  serialized_end=309,
)

_CREATETOOLKITREQUEST.fields_by_name['toolkit'].message_type = cmdb__extend__sdk_dot_model_dot_cmdb__extend_dot_toolkit__pb2._TOOLKIT
_CREATETOOLKITRESPONSEWRAPPER.fields_by_name['data'].message_type = cmdb__extend__sdk_dot_model_dot_cmdb__extend_dot_toolkit__pb2._TOOLKIT
DESCRIPTOR.message_types_by_name['CreateToolkitRequest'] = _CREATETOOLKITREQUEST
DESCRIPTOR.message_types_by_name['CreateToolkitResponseWrapper'] = _CREATETOOLKITRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateToolkitRequest = _reflection.GeneratedProtocolMessageType('CreateToolkitRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATETOOLKITREQUEST,
  '__module__' : 'create_toolkit_pb2'
  # @@protoc_insertion_point(class_scope:toolkit.CreateToolkitRequest)
  })
_sym_db.RegisterMessage(CreateToolkitRequest)

CreateToolkitResponseWrapper = _reflection.GeneratedProtocolMessageType('CreateToolkitResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _CREATETOOLKITRESPONSEWRAPPER,
  '__module__' : 'create_toolkit_pb2'
  # @@protoc_insertion_point(class_scope:toolkit.CreateToolkitResponseWrapper)
  })
_sym_db.RegisterMessage(CreateToolkitResponseWrapper)


# @@protoc_insertion_point(module_scope)
