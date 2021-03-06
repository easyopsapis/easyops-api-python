# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sync_user_dingtalk_to_ldap.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sync_user_dingtalk_to_ldap.proto',
  package='users',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n sync_user_dingtalk_to_ldap.proto\x12\x05users\"^\n\x1eSyncUserDingTalkToLdapResponse\x12\x13\n\x0binsertCount\x18\x01 \x01(\x05\x12\x13\n\x0bupdateCount\x18\x02 \x01(\x05\x12\x12\n\nfailedList\x18\x03 \x03(\t\"\x8e\x01\n%SyncUserDingTalkToLdapResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x33\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32%.users.SyncUserDingTalkToLdapResponseb\x06proto3')
)




_SYNCUSERDINGTALKTOLDAPRESPONSE = _descriptor.Descriptor(
  name='SyncUserDingTalkToLdapResponse',
  full_name='users.SyncUserDingTalkToLdapResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='insertCount', full_name='users.SyncUserDingTalkToLdapResponse.insertCount', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updateCount', full_name='users.SyncUserDingTalkToLdapResponse.updateCount', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='failedList', full_name='users.SyncUserDingTalkToLdapResponse.failedList', index=2,
      number=3, type=9, cpp_type=9, label=3,
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
  serialized_start=43,
  serialized_end=137,
)


_SYNCUSERDINGTALKTOLDAPRESPONSEWRAPPER = _descriptor.Descriptor(
  name='SyncUserDingTalkToLdapResponseWrapper',
  full_name='users.SyncUserDingTalkToLdapResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='users.SyncUserDingTalkToLdapResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='users.SyncUserDingTalkToLdapResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='users.SyncUserDingTalkToLdapResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='users.SyncUserDingTalkToLdapResponseWrapper.data', index=3,
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
  serialized_start=140,
  serialized_end=282,
)

_SYNCUSERDINGTALKTOLDAPRESPONSEWRAPPER.fields_by_name['data'].message_type = _SYNCUSERDINGTALKTOLDAPRESPONSE
DESCRIPTOR.message_types_by_name['SyncUserDingTalkToLdapResponse'] = _SYNCUSERDINGTALKTOLDAPRESPONSE
DESCRIPTOR.message_types_by_name['SyncUserDingTalkToLdapResponseWrapper'] = _SYNCUSERDINGTALKTOLDAPRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SyncUserDingTalkToLdapResponse = _reflection.GeneratedProtocolMessageType('SyncUserDingTalkToLdapResponse', (_message.Message,), {
  'DESCRIPTOR' : _SYNCUSERDINGTALKTOLDAPRESPONSE,
  '__module__' : 'sync_user_dingtalk_to_ldap_pb2'
  # @@protoc_insertion_point(class_scope:users.SyncUserDingTalkToLdapResponse)
  })
_sym_db.RegisterMessage(SyncUserDingTalkToLdapResponse)

SyncUserDingTalkToLdapResponseWrapper = _reflection.GeneratedProtocolMessageType('SyncUserDingTalkToLdapResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _SYNCUSERDINGTALKTOLDAPRESPONSEWRAPPER,
  '__module__' : 'sync_user_dingtalk_to_ldap_pb2'
  # @@protoc_insertion_point(class_scope:users.SyncUserDingTalkToLdapResponseWrapper)
  })
_sym_db.RegisterMessage(SyncUserDingTalkToLdapResponseWrapper)


# @@protoc_insertion_point(module_scope)
