# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: search_all_user_group.proto

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
  name='search_all_user_group.proto',
  package='user_admin',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1bsearch_all_user_group.proto\x12\nuser_admin\x1a\x1cgoogle/protobuf/struct.proto\"\x93\x01\n\x19SearchAllUserGroupRequest\x12&\n\x05query\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\'\n\x06\x66ields\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12%\n\x04sort\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\"C\n\x1aSearchAllUserGroupResponse\x12%\n\x04list\x18\x01 \x03(\x0b\x32\x17.google.protobuf.Struct\"\x8b\x01\n!SearchAllUserGroupResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x34\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32&.user_admin.SearchAllUserGroupResponseb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_SEARCHALLUSERGROUPREQUEST = _descriptor.Descriptor(
  name='SearchAllUserGroupRequest',
  full_name='user_admin.SearchAllUserGroupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='user_admin.SearchAllUserGroupRequest.query', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fields', full_name='user_admin.SearchAllUserGroupRequest.fields', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sort', full_name='user_admin.SearchAllUserGroupRequest.sort', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=74,
  serialized_end=221,
)


_SEARCHALLUSERGROUPRESPONSE = _descriptor.Descriptor(
  name='SearchAllUserGroupResponse',
  full_name='user_admin.SearchAllUserGroupResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='list', full_name='user_admin.SearchAllUserGroupResponse.list', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=223,
  serialized_end=290,
)


_SEARCHALLUSERGROUPRESPONSEWRAPPER = _descriptor.Descriptor(
  name='SearchAllUserGroupResponseWrapper',
  full_name='user_admin.SearchAllUserGroupResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='user_admin.SearchAllUserGroupResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='user_admin.SearchAllUserGroupResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='user_admin.SearchAllUserGroupResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='user_admin.SearchAllUserGroupResponseWrapper.data', index=3,
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
  serialized_start=293,
  serialized_end=432,
)

_SEARCHALLUSERGROUPREQUEST.fields_by_name['query'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SEARCHALLUSERGROUPREQUEST.fields_by_name['fields'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SEARCHALLUSERGROUPREQUEST.fields_by_name['sort'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SEARCHALLUSERGROUPRESPONSE.fields_by_name['list'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SEARCHALLUSERGROUPRESPONSEWRAPPER.fields_by_name['data'].message_type = _SEARCHALLUSERGROUPRESPONSE
DESCRIPTOR.message_types_by_name['SearchAllUserGroupRequest'] = _SEARCHALLUSERGROUPREQUEST
DESCRIPTOR.message_types_by_name['SearchAllUserGroupResponse'] = _SEARCHALLUSERGROUPRESPONSE
DESCRIPTOR.message_types_by_name['SearchAllUserGroupResponseWrapper'] = _SEARCHALLUSERGROUPRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SearchAllUserGroupRequest = _reflection.GeneratedProtocolMessageType('SearchAllUserGroupRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHALLUSERGROUPREQUEST,
  '__module__' : 'search_all_user_group_pb2'
  # @@protoc_insertion_point(class_scope:user_admin.SearchAllUserGroupRequest)
  })
_sym_db.RegisterMessage(SearchAllUserGroupRequest)

SearchAllUserGroupResponse = _reflection.GeneratedProtocolMessageType('SearchAllUserGroupResponse', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHALLUSERGROUPRESPONSE,
  '__module__' : 'search_all_user_group_pb2'
  # @@protoc_insertion_point(class_scope:user_admin.SearchAllUserGroupResponse)
  })
_sym_db.RegisterMessage(SearchAllUserGroupResponse)

SearchAllUserGroupResponseWrapper = _reflection.GeneratedProtocolMessageType('SearchAllUserGroupResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHALLUSERGROUPRESPONSEWRAPPER,
  '__module__' : 'search_all_user_group_pb2'
  # @@protoc_insertion_point(class_scope:user_admin.SearchAllUserGroupResponseWrapper)
  })
_sym_db.RegisterMessage(SearchAllUserGroupResponseWrapper)


# @@protoc_insertion_point(module_scope)