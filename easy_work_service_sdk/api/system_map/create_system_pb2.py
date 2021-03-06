# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: create_system.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='create_system.proto',
  package='system_map',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13\x63reate_system.proto\x12\nsystem_map\"*\n\x14\x43reateSystemResponse\x12\x12\n\ninstanceId\x18\x01 \x01(\t\"\x7f\n\x1b\x43reateSystemResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12.\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32 .system_map.CreateSystemResponseb\x06proto3')
)




_CREATESYSTEMRESPONSE = _descriptor.Descriptor(
  name='CreateSystemResponse',
  full_name='system_map.CreateSystemResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='system_map.CreateSystemResponse.instanceId', index=0,
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
  serialized_start=35,
  serialized_end=77,
)


_CREATESYSTEMRESPONSEWRAPPER = _descriptor.Descriptor(
  name='CreateSystemResponseWrapper',
  full_name='system_map.CreateSystemResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='system_map.CreateSystemResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='system_map.CreateSystemResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='system_map.CreateSystemResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='system_map.CreateSystemResponseWrapper.data', index=3,
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
  serialized_start=79,
  serialized_end=206,
)

_CREATESYSTEMRESPONSEWRAPPER.fields_by_name['data'].message_type = _CREATESYSTEMRESPONSE
DESCRIPTOR.message_types_by_name['CreateSystemResponse'] = _CREATESYSTEMRESPONSE
DESCRIPTOR.message_types_by_name['CreateSystemResponseWrapper'] = _CREATESYSTEMRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateSystemResponse = _reflection.GeneratedProtocolMessageType('CreateSystemResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATESYSTEMRESPONSE,
  '__module__' : 'create_system_pb2'
  # @@protoc_insertion_point(class_scope:system_map.CreateSystemResponse)
  })
_sym_db.RegisterMessage(CreateSystemResponse)

CreateSystemResponseWrapper = _reflection.GeneratedProtocolMessageType('CreateSystemResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _CREATESYSTEMRESPONSEWRAPPER,
  '__module__' : 'create_system_pb2'
  # @@protoc_insertion_point(class_scope:system_map.CreateSystemResponseWrapper)
  })
_sym_db.RegisterMessage(CreateSystemResponseWrapper)


# @@protoc_insertion_point(module_scope)
