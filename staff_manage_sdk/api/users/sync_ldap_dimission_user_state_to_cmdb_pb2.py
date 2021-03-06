# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sync_ldap_dimission_user_state_to_cmdb.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sync_ldap_dimission_user_state_to_cmdb.proto',
  package='users',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n,sync_ldap_dimission_user_state_to_cmdb.proto\x12\x05users\"`\n\'SyncLdapDimissionUserStateToCmdbRequest\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\x12\x0c\n\x04user\x18\x03 \x01(\t\x12\x0b\n\x03org\x18\x04 \x01(\x05\"S\n(SyncLdapDimissionUserStateToCmdbResponse\x12\x13\n\x0bupdateCount\x18\x01 \x01(\x05\x12\x12\n\nfailedList\x18\x02 \x03(\t\"\xa2\x01\n/SyncLdapDimissionUserStateToCmdbResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12=\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32/.users.SyncLdapDimissionUserStateToCmdbResponseb\x06proto3')
)




_SYNCLDAPDIMISSIONUSERSTATETOCMDBREQUEST = _descriptor.Descriptor(
  name='SyncLdapDimissionUserStateToCmdbRequest',
  full_name='users.SyncLdapDimissionUserStateToCmdbRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='host', full_name='users.SyncLdapDimissionUserStateToCmdbRequest.host', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='users.SyncLdapDimissionUserStateToCmdbRequest.port', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='users.SyncLdapDimissionUserStateToCmdbRequest.user', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org', full_name='users.SyncLdapDimissionUserStateToCmdbRequest.org', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=55,
  serialized_end=151,
)


_SYNCLDAPDIMISSIONUSERSTATETOCMDBRESPONSE = _descriptor.Descriptor(
  name='SyncLdapDimissionUserStateToCmdbResponse',
  full_name='users.SyncLdapDimissionUserStateToCmdbResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='updateCount', full_name='users.SyncLdapDimissionUserStateToCmdbResponse.updateCount', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='failedList', full_name='users.SyncLdapDimissionUserStateToCmdbResponse.failedList', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_end=236,
)


_SYNCLDAPDIMISSIONUSERSTATETOCMDBRESPONSEWRAPPER = _descriptor.Descriptor(
  name='SyncLdapDimissionUserStateToCmdbResponseWrapper',
  full_name='users.SyncLdapDimissionUserStateToCmdbResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='users.SyncLdapDimissionUserStateToCmdbResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='users.SyncLdapDimissionUserStateToCmdbResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='users.SyncLdapDimissionUserStateToCmdbResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='users.SyncLdapDimissionUserStateToCmdbResponseWrapper.data', index=3,
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
  serialized_start=239,
  serialized_end=401,
)

_SYNCLDAPDIMISSIONUSERSTATETOCMDBRESPONSEWRAPPER.fields_by_name['data'].message_type = _SYNCLDAPDIMISSIONUSERSTATETOCMDBRESPONSE
DESCRIPTOR.message_types_by_name['SyncLdapDimissionUserStateToCmdbRequest'] = _SYNCLDAPDIMISSIONUSERSTATETOCMDBREQUEST
DESCRIPTOR.message_types_by_name['SyncLdapDimissionUserStateToCmdbResponse'] = _SYNCLDAPDIMISSIONUSERSTATETOCMDBRESPONSE
DESCRIPTOR.message_types_by_name['SyncLdapDimissionUserStateToCmdbResponseWrapper'] = _SYNCLDAPDIMISSIONUSERSTATETOCMDBRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SyncLdapDimissionUserStateToCmdbRequest = _reflection.GeneratedProtocolMessageType('SyncLdapDimissionUserStateToCmdbRequest', (_message.Message,), {
  'DESCRIPTOR' : _SYNCLDAPDIMISSIONUSERSTATETOCMDBREQUEST,
  '__module__' : 'sync_ldap_dimission_user_state_to_cmdb_pb2'
  # @@protoc_insertion_point(class_scope:users.SyncLdapDimissionUserStateToCmdbRequest)
  })
_sym_db.RegisterMessage(SyncLdapDimissionUserStateToCmdbRequest)

SyncLdapDimissionUserStateToCmdbResponse = _reflection.GeneratedProtocolMessageType('SyncLdapDimissionUserStateToCmdbResponse', (_message.Message,), {
  'DESCRIPTOR' : _SYNCLDAPDIMISSIONUSERSTATETOCMDBRESPONSE,
  '__module__' : 'sync_ldap_dimission_user_state_to_cmdb_pb2'
  # @@protoc_insertion_point(class_scope:users.SyncLdapDimissionUserStateToCmdbResponse)
  })
_sym_db.RegisterMessage(SyncLdapDimissionUserStateToCmdbResponse)

SyncLdapDimissionUserStateToCmdbResponseWrapper = _reflection.GeneratedProtocolMessageType('SyncLdapDimissionUserStateToCmdbResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _SYNCLDAPDIMISSIONUSERSTATETOCMDBRESPONSEWRAPPER,
  '__module__' : 'sync_ldap_dimission_user_state_to_cmdb_pb2'
  # @@protoc_insertion_point(class_scope:users.SyncLdapDimissionUserStateToCmdbResponseWrapper)
  })
_sym_db.RegisterMessage(SyncLdapDimissionUserStateToCmdbResponseWrapper)


# @@protoc_insertion_point(module_scope)
