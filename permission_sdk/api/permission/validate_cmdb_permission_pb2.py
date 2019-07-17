# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: validate_cmdb_permission.proto

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
  name='validate_cmdb_permission.proto',
  package='permission',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1evalidate_cmdb_permission.proto\x12\npermission\x1a\x1bgoogle/protobuf/empty.proto\"\x83\x01\n\x1dValidateCmdbPermissionRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x02 \x01(\t\x12\x11\n\tobject_id\x18\x03 \x01(\t\x12\x13\n\x0binstance_id\x18\x04 \x01(\t\x12\x1c\n\x14validate_action_only\x18\x05 \x01(\x08\"\x7f\n%ValidateCmdbPermissionResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12$\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x16.google.protobuf.Emptyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_VALIDATECMDBPERMISSIONREQUEST = _descriptor.Descriptor(
  name='ValidateCmdbPermissionRequest',
  full_name='permission.ValidateCmdbPermissionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='permission.ValidateCmdbPermissionRequest.user', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='permission.ValidateCmdbPermissionRequest.action', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object_id', full_name='permission.ValidateCmdbPermissionRequest.object_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instance_id', full_name='permission.ValidateCmdbPermissionRequest.instance_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validate_action_only', full_name='permission.ValidateCmdbPermissionRequest.validate_action_only', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=76,
  serialized_end=207,
)


_VALIDATECMDBPERMISSIONRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ValidateCmdbPermissionResponseWrapper',
  full_name='permission.ValidateCmdbPermissionResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='permission.ValidateCmdbPermissionResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='permission.ValidateCmdbPermissionResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='permission.ValidateCmdbPermissionResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='permission.ValidateCmdbPermissionResponseWrapper.data', index=3,
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
  serialized_start=209,
  serialized_end=336,
)

_VALIDATECMDBPERMISSIONRESPONSEWRAPPER.fields_by_name['data'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
DESCRIPTOR.message_types_by_name['ValidateCmdbPermissionRequest'] = _VALIDATECMDBPERMISSIONREQUEST
DESCRIPTOR.message_types_by_name['ValidateCmdbPermissionResponseWrapper'] = _VALIDATECMDBPERMISSIONRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ValidateCmdbPermissionRequest = _reflection.GeneratedProtocolMessageType('ValidateCmdbPermissionRequest', (_message.Message,), dict(
  DESCRIPTOR = _VALIDATECMDBPERMISSIONREQUEST,
  __module__ = 'validate_cmdb_permission_pb2'
  # @@protoc_insertion_point(class_scope:permission.ValidateCmdbPermissionRequest)
  ))
_sym_db.RegisterMessage(ValidateCmdbPermissionRequest)

ValidateCmdbPermissionResponseWrapper = _reflection.GeneratedProtocolMessageType('ValidateCmdbPermissionResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _VALIDATECMDBPERMISSIONRESPONSEWRAPPER,
  __module__ = 'validate_cmdb_permission_pb2'
  # @@protoc_insertion_point(class_scope:permission.ValidateCmdbPermissionResponseWrapper)
  ))
_sym_db.RegisterMessage(ValidateCmdbPermissionResponseWrapper)


# @@protoc_insertion_point(module_scope)