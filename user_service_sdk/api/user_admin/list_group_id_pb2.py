# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list_group_id.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='list_group_id.proto',
  package='user_admin',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13list_group_id.proto\x12\nuser_admin\x1a\x1bgoogle/protobuf/empty.proto\"&\n\x13ListGroupsIdRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"]\n\x1bListGroupsIdResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x04 \x03(\tb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_LISTGROUPSIDREQUEST = _descriptor.Descriptor(
  name='ListGroupsIdRequest',
  full_name='user_admin.ListGroupsIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='user_admin.ListGroupsIdRequest.user_id', index=0,
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
  serialized_start=64,
  serialized_end=102,
)


_LISTGROUPSIDRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListGroupsIdResponseWrapper',
  full_name='user_admin.ListGroupsIdResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='user_admin.ListGroupsIdResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='user_admin.ListGroupsIdResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='user_admin.ListGroupsIdResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='user_admin.ListGroupsIdResponseWrapper.data', index=3,
      number=4, type=9, cpp_type=9, label=3,
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
  serialized_start=104,
  serialized_end=197,
)

DESCRIPTOR.message_types_by_name['ListGroupsIdRequest'] = _LISTGROUPSIDREQUEST
DESCRIPTOR.message_types_by_name['ListGroupsIdResponseWrapper'] = _LISTGROUPSIDRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListGroupsIdRequest = _reflection.GeneratedProtocolMessageType('ListGroupsIdRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTGROUPSIDREQUEST,
  __module__ = 'list_group_id_pb2'
  # @@protoc_insertion_point(class_scope:user_admin.ListGroupsIdRequest)
  ))
_sym_db.RegisterMessage(ListGroupsIdRequest)

ListGroupsIdResponseWrapper = _reflection.GeneratedProtocolMessageType('ListGroupsIdResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _LISTGROUPSIDRESPONSEWRAPPER,
  __module__ = 'list_group_id_pb2'
  # @@protoc_insertion_point(class_scope:user_admin.ListGroupsIdResponseWrapper)
  ))
_sym_db.RegisterMessage(ListGroupsIdResponseWrapper)


# @@protoc_insertion_point(module_scope)
