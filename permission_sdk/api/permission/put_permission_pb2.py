# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: put_permission.proto

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
  name='put_permission.proto',
  package='permission',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14put_permission.proto\x12\npermission\x1a\x1cgoogle/protobuf/struct.proto\"\x8b\x01\n\x14PutPermissionRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06system\x18\x02 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x03 \x01(\t\x12\x0e\n\x06remark\x18\x04 \x01(\t\x12\r\n\x05roles\x18\x05 \x03(\t\x12(\n\x08resource\x18\x06 \x01(\x0b\x32\x16.google.protobuf.Value\"&\n\x15PutPermissionResponse\x12\r\n\x05\x63ount\x18\x01 \x01(\x05\"\x81\x01\n\x1cPutPermissionResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12/\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32!.permission.PutPermissionResponseb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_PUTPERMISSIONREQUEST = _descriptor.Descriptor(
  name='PutPermissionRequest',
  full_name='permission.PutPermissionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='permission.PutPermissionRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='system', full_name='permission.PutPermissionRequest.system', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='permission.PutPermissionRequest.action', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remark', full_name='permission.PutPermissionRequest.remark', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roles', full_name='permission.PutPermissionRequest.roles', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resource', full_name='permission.PutPermissionRequest.resource', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
  serialized_start=67,
  serialized_end=206,
)


_PUTPERMISSIONRESPONSE = _descriptor.Descriptor(
  name='PutPermissionResponse',
  full_name='permission.PutPermissionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='permission.PutPermissionResponse.count', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=208,
  serialized_end=246,
)


_PUTPERMISSIONRESPONSEWRAPPER = _descriptor.Descriptor(
  name='PutPermissionResponseWrapper',
  full_name='permission.PutPermissionResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='permission.PutPermissionResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='permission.PutPermissionResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='permission.PutPermissionResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='permission.PutPermissionResponseWrapper.data', index=3,
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
  serialized_start=249,
  serialized_end=378,
)

_PUTPERMISSIONREQUEST.fields_by_name['resource'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_PUTPERMISSIONRESPONSEWRAPPER.fields_by_name['data'].message_type = _PUTPERMISSIONRESPONSE
DESCRIPTOR.message_types_by_name['PutPermissionRequest'] = _PUTPERMISSIONREQUEST
DESCRIPTOR.message_types_by_name['PutPermissionResponse'] = _PUTPERMISSIONRESPONSE
DESCRIPTOR.message_types_by_name['PutPermissionResponseWrapper'] = _PUTPERMISSIONRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PutPermissionRequest = _reflection.GeneratedProtocolMessageType('PutPermissionRequest', (_message.Message,), {
  'DESCRIPTOR' : _PUTPERMISSIONREQUEST,
  '__module__' : 'put_permission_pb2'
  # @@protoc_insertion_point(class_scope:permission.PutPermissionRequest)
  })
_sym_db.RegisterMessage(PutPermissionRequest)

PutPermissionResponse = _reflection.GeneratedProtocolMessageType('PutPermissionResponse', (_message.Message,), {
  'DESCRIPTOR' : _PUTPERMISSIONRESPONSE,
  '__module__' : 'put_permission_pb2'
  # @@protoc_insertion_point(class_scope:permission.PutPermissionResponse)
  })
_sym_db.RegisterMessage(PutPermissionResponse)

PutPermissionResponseWrapper = _reflection.GeneratedProtocolMessageType('PutPermissionResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _PUTPERMISSIONRESPONSEWRAPPER,
  '__module__' : 'put_permission_pb2'
  # @@protoc_insertion_point(class_scope:permission.PutPermissionResponseWrapper)
  })
_sym_db.RegisterMessage(PutPermissionResponseWrapper)


# @@protoc_insertion_point(module_scope)
