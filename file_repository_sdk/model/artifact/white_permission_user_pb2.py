# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: white_permission_user.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='white_permission_user.proto',
  package='artifact',
  syntax='proto3',
  serialized_options=_b('ZBgo.easyops.local/contracts/protorepo-models/easyops/model/artifact'),
  serialized_pb=_b('\n\x1bwhite_permission_user.proto\x12\x08\x61rtifact\"d\n\x13WhitePermissionUser\x12\x19\n\x11updateAuthorizers\x18\x01 \x03(\t\x12\x19\n\x11\x64\x65leteAuthorizers\x18\x02 \x03(\t\x12\x17\n\x0freadAuthorizers\x18\x03 \x03(\tBDZBgo.easyops.local/contracts/protorepo-models/easyops/model/artifactb\x06proto3')
)




_WHITEPERMISSIONUSER = _descriptor.Descriptor(
  name='WhitePermissionUser',
  full_name='artifact.WhitePermissionUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='updateAuthorizers', full_name='artifact.WhitePermissionUser.updateAuthorizers', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deleteAuthorizers', full_name='artifact.WhitePermissionUser.deleteAuthorizers', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readAuthorizers', full_name='artifact.WhitePermissionUser.readAuthorizers', index=2,
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
  serialized_start=41,
  serialized_end=141,
)

DESCRIPTOR.message_types_by_name['WhitePermissionUser'] = _WHITEPERMISSIONUSER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WhitePermissionUser = _reflection.GeneratedProtocolMessageType('WhitePermissionUser', (_message.Message,), dict(
  DESCRIPTOR = _WHITEPERMISSIONUSER,
  __module__ = 'white_permission_user_pb2'
  # @@protoc_insertion_point(class_scope:artifact.WhitePermissionUser)
  ))
_sym_db.RegisterMessage(WhitePermissionUser)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
