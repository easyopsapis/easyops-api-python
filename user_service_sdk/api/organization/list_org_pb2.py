# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list_org.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='list_org.proto',
  package='organization',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0elist_org.proto\x12\x0corganization\"w\n\x0fListOrgResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07\x65xpires\x18\x02 \x01(\x05\x12\x10\n\x08\x63reateAt\x18\x03 \x01(\t\x12\r\n\x05valid\x18\x04 \x01(\x08\x12\n\n\x02ts\x18\x05 \x01(\x05\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x0c\n\x04memo\x18\x07 \x01(\t\"w\n\x16ListOrgResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12+\n\x04\x64\x61ta\x18\x04 \x03(\x0b\x32\x1d.organization.ListOrgResponseb\x06proto3')
)




_LISTORGRESPONSE = _descriptor.Descriptor(
  name='ListOrgResponse',
  full_name='organization.ListOrgResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='organization.ListOrgResponse.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expires', full_name='organization.ListOrgResponse.expires', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='createAt', full_name='organization.ListOrgResponse.createAt', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='valid', full_name='organization.ListOrgResponse.valid', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ts', full_name='organization.ListOrgResponse.ts', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='organization.ListOrgResponse.name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='organization.ListOrgResponse.memo', index=6,
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
  serialized_start=32,
  serialized_end=151,
)


_LISTORGRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListOrgResponseWrapper',
  full_name='organization.ListOrgResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='organization.ListOrgResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='organization.ListOrgResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='organization.ListOrgResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='organization.ListOrgResponseWrapper.data', index=3,
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
  serialized_start=153,
  serialized_end=272,
)

_LISTORGRESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTORGRESPONSE
DESCRIPTOR.message_types_by_name['ListOrgResponse'] = _LISTORGRESPONSE
DESCRIPTOR.message_types_by_name['ListOrgResponseWrapper'] = _LISTORGRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListOrgResponse = _reflection.GeneratedProtocolMessageType('ListOrgResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTORGRESPONSE,
  __module__ = 'list_org_pb2'
  # @@protoc_insertion_point(class_scope:organization.ListOrgResponse)
  ))
_sym_db.RegisterMessage(ListOrgResponse)

ListOrgResponseWrapper = _reflection.GeneratedProtocolMessageType('ListOrgResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _LISTORGRESPONSEWRAPPER,
  __module__ = 'list_org_pb2'
  # @@protoc_insertion_point(class_scope:organization.ListOrgResponseWrapper)
  ))
_sym_db.RegisterMessage(ListOrgResponseWrapper)


# @@protoc_insertion_point(module_scope)
