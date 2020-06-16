# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: permission_resource.proto

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
  name='permission_resource.proto',
  package='permission',
  syntax='proto3',
  serialized_options=_b('ZDgo.easyops.local/contracts/protorepo-models/easyops/model/permission'),
  serialized_pb=_b('\n\x19permission_resource.proto\x12\npermission\x1a\x1cgoogle/protobuf/struct.proto\"^\n\x12PermissionResource\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06system\x18\x02 \x01(\t\x12*\n\tcondition\x18\x03 \x01(\x0b\x32\x17.google.protobuf.StructBFZDgo.easyops.local/contracts/protorepo-models/easyops/model/permissionb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_PERMISSIONRESOURCE = _descriptor.Descriptor(
  name='PermissionResource',
  full_name='permission.PermissionResource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='permission.PermissionResource.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='system', full_name='permission.PermissionResource.system', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='condition', full_name='permission.PermissionResource.condition', index=2,
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
  serialized_start=71,
  serialized_end=165,
)

_PERMISSIONRESOURCE.fields_by_name['condition'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['PermissionResource'] = _PERMISSIONRESOURCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PermissionResource = _reflection.GeneratedProtocolMessageType('PermissionResource', (_message.Message,), {
  'DESCRIPTOR' : _PERMISSIONRESOURCE,
  '__module__' : 'permission_resource_pb2'
  # @@protoc_insertion_point(class_scope:permission.PermissionResource)
  })
_sym_db.RegisterMessage(PermissionResource)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
