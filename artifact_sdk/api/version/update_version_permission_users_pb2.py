# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: update_version_permission_users.proto

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
  name='update_version_permission_users.proto',
  package='version',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n%update_version_permission_users.proto\x12\x07version\x1a\x1bgoogle/protobuf/empty.proto\"\x81\x01\n#UpdateVersionPermissionUsersRequest\x12\x11\n\tpackageId\x18\x01 \x01(\t\x12\x11\n\tversionId\x18\x02 \x01(\t\x12\x19\n\x11updateAuthorizers\x18\x03 \x03(\t\x12\x19\n\x11\x64\x65leteAuthorizers\x18\x04 \x03(\t\"\x85\x01\n+UpdateVersionPermissionUsersResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12$\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x16.google.protobuf.Emptyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_UPDATEVERSIONPERMISSIONUSERSREQUEST = _descriptor.Descriptor(
  name='UpdateVersionPermissionUsersRequest',
  full_name='version.UpdateVersionPermissionUsersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='packageId', full_name='version.UpdateVersionPermissionUsersRequest.packageId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionId', full_name='version.UpdateVersionPermissionUsersRequest.versionId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updateAuthorizers', full_name='version.UpdateVersionPermissionUsersRequest.updateAuthorizers', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deleteAuthorizers', full_name='version.UpdateVersionPermissionUsersRequest.deleteAuthorizers', index=3,
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
  serialized_start=80,
  serialized_end=209,
)


_UPDATEVERSIONPERMISSIONUSERSRESPONSEWRAPPER = _descriptor.Descriptor(
  name='UpdateVersionPermissionUsersResponseWrapper',
  full_name='version.UpdateVersionPermissionUsersResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='version.UpdateVersionPermissionUsersResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='version.UpdateVersionPermissionUsersResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='version.UpdateVersionPermissionUsersResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='version.UpdateVersionPermissionUsersResponseWrapper.data', index=3,
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
  serialized_start=212,
  serialized_end=345,
)

_UPDATEVERSIONPERMISSIONUSERSRESPONSEWRAPPER.fields_by_name['data'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
DESCRIPTOR.message_types_by_name['UpdateVersionPermissionUsersRequest'] = _UPDATEVERSIONPERMISSIONUSERSREQUEST
DESCRIPTOR.message_types_by_name['UpdateVersionPermissionUsersResponseWrapper'] = _UPDATEVERSIONPERMISSIONUSERSRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateVersionPermissionUsersRequest = _reflection.GeneratedProtocolMessageType('UpdateVersionPermissionUsersRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEVERSIONPERMISSIONUSERSREQUEST,
  '__module__' : 'update_version_permission_users_pb2'
  # @@protoc_insertion_point(class_scope:version.UpdateVersionPermissionUsersRequest)
  })
_sym_db.RegisterMessage(UpdateVersionPermissionUsersRequest)

UpdateVersionPermissionUsersResponseWrapper = _reflection.GeneratedProtocolMessageType('UpdateVersionPermissionUsersResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEVERSIONPERMISSIONUSERSRESPONSEWRAPPER,
  '__module__' : 'update_version_permission_users_pb2'
  # @@protoc_insertion_point(class_scope:version.UpdateVersionPermissionUsersResponseWrapper)
  })
_sym_db.RegisterMessage(UpdateVersionPermissionUsersResponseWrapper)


# @@protoc_insertion_point(module_scope)
