# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: create_org.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='create_org.proto',
  package='organization',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10\x63reate_org.proto\x12\x0corganization\"a\n\x10\x43reateOrgRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x14\n\x0c\x65xpired_days\x18\x02 \x01(\x05\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0c\n\x04memo\x18\x04 \x01(\t\x12\x0f\n\x07\x65\x64ition\x18\x05 \x01(\t\"y\n\x11\x43reateOrgResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07\x65xpires\x18\x02 \x01(\x05\x12\x10\n\x08\x63reateAt\x18\x03 \x01(\t\x12\r\n\x05valid\x18\x04 \x01(\x08\x12\n\n\x02ts\x18\x05 \x01(\x05\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x0c\n\x04memo\x18\x07 \x01(\t\"{\n\x18\x43reateOrgResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12-\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1f.organization.CreateOrgResponseb\x06proto3')
)




_CREATEORGREQUEST = _descriptor.Descriptor(
  name='CreateOrgRequest',
  full_name='organization.CreateOrgRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='organization.CreateOrgRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expired_days', full_name='organization.CreateOrgRequest.expired_days', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='organization.CreateOrgRequest.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='organization.CreateOrgRequest.memo', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='edition', full_name='organization.CreateOrgRequest.edition', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_end=131,
)


_CREATEORGRESPONSE = _descriptor.Descriptor(
  name='CreateOrgResponse',
  full_name='organization.CreateOrgResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='organization.CreateOrgResponse.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expires', full_name='organization.CreateOrgResponse.expires', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='createAt', full_name='organization.CreateOrgResponse.createAt', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='valid', full_name='organization.CreateOrgResponse.valid', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ts', full_name='organization.CreateOrgResponse.ts', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='organization.CreateOrgResponse.name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='organization.CreateOrgResponse.memo', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=133,
  serialized_end=254,
)


_CREATEORGRESPONSEWRAPPER = _descriptor.Descriptor(
  name='CreateOrgResponseWrapper',
  full_name='organization.CreateOrgResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='organization.CreateOrgResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='organization.CreateOrgResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='organization.CreateOrgResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='organization.CreateOrgResponseWrapper.data', index=3,
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
  serialized_start=256,
  serialized_end=379,
)

_CREATEORGRESPONSEWRAPPER.fields_by_name['data'].message_type = _CREATEORGRESPONSE
DESCRIPTOR.message_types_by_name['CreateOrgRequest'] = _CREATEORGREQUEST
DESCRIPTOR.message_types_by_name['CreateOrgResponse'] = _CREATEORGRESPONSE
DESCRIPTOR.message_types_by_name['CreateOrgResponseWrapper'] = _CREATEORGRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateOrgRequest = _reflection.GeneratedProtocolMessageType('CreateOrgRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEORGREQUEST,
  '__module__' : 'create_org_pb2'
  # @@protoc_insertion_point(class_scope:organization.CreateOrgRequest)
  })
_sym_db.RegisterMessage(CreateOrgRequest)

CreateOrgResponse = _reflection.GeneratedProtocolMessageType('CreateOrgResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEORGRESPONSE,
  '__module__' : 'create_org_pb2'
  # @@protoc_insertion_point(class_scope:organization.CreateOrgResponse)
  })
_sym_db.RegisterMessage(CreateOrgResponse)

CreateOrgResponseWrapper = _reflection.GeneratedProtocolMessageType('CreateOrgResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _CREATEORGRESPONSEWRAPPER,
  '__module__' : 'create_org_pb2'
  # @@protoc_insertion_point(class_scope:organization.CreateOrgResponseWrapper)
  })
_sym_db.RegisterMessage(CreateOrgResponseWrapper)


# @@protoc_insertion_point(module_scope)
