# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_permission_detail.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from permission_sdk.model.permission import permission_pb2 as permission__sdk_dot_model_dot_permission_dot_permission__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_permission_detail.proto',
  package='permission',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1bget_permission_detail.proto\x12\npermission\x1a\x30permission_sdk/model/permission/permission.proto\"(\n\x1aGetPermissionDetailRequest\x12\n\n\x02id\x18\x01 \x01(\t\"C\n\x1bGetPermissionDetailResponse\x12$\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x16.permission.Permission\"\x8d\x01\n\"GetPermissionDetailResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x35\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\'.permission.GetPermissionDetailResponseb\x06proto3')
  ,
  dependencies=[permission__sdk_dot_model_dot_permission_dot_permission__pb2.DESCRIPTOR,])




_GETPERMISSIONDETAILREQUEST = _descriptor.Descriptor(
  name='GetPermissionDetailRequest',
  full_name='permission.GetPermissionDetailRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='permission.GetPermissionDetailRequest.id', index=0,
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
  serialized_start=93,
  serialized_end=133,
)


_GETPERMISSIONDETAILRESPONSE = _descriptor.Descriptor(
  name='GetPermissionDetailResponse',
  full_name='permission.GetPermissionDetailResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='permission.GetPermissionDetailResponse.data', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=135,
  serialized_end=202,
)


_GETPERMISSIONDETAILRESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetPermissionDetailResponseWrapper',
  full_name='permission.GetPermissionDetailResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='permission.GetPermissionDetailResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='permission.GetPermissionDetailResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='permission.GetPermissionDetailResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='permission.GetPermissionDetailResponseWrapper.data', index=3,
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
  serialized_start=205,
  serialized_end=346,
)

_GETPERMISSIONDETAILRESPONSE.fields_by_name['data'].message_type = permission__sdk_dot_model_dot_permission_dot_permission__pb2._PERMISSION
_GETPERMISSIONDETAILRESPONSEWRAPPER.fields_by_name['data'].message_type = _GETPERMISSIONDETAILRESPONSE
DESCRIPTOR.message_types_by_name['GetPermissionDetailRequest'] = _GETPERMISSIONDETAILREQUEST
DESCRIPTOR.message_types_by_name['GetPermissionDetailResponse'] = _GETPERMISSIONDETAILRESPONSE
DESCRIPTOR.message_types_by_name['GetPermissionDetailResponseWrapper'] = _GETPERMISSIONDETAILRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetPermissionDetailRequest = _reflection.GeneratedProtocolMessageType('GetPermissionDetailRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPERMISSIONDETAILREQUEST,
  '__module__' : 'get_permission_detail_pb2'
  # @@protoc_insertion_point(class_scope:permission.GetPermissionDetailRequest)
  })
_sym_db.RegisterMessage(GetPermissionDetailRequest)

GetPermissionDetailResponse = _reflection.GeneratedProtocolMessageType('GetPermissionDetailResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPERMISSIONDETAILRESPONSE,
  '__module__' : 'get_permission_detail_pb2'
  # @@protoc_insertion_point(class_scope:permission.GetPermissionDetailResponse)
  })
_sym_db.RegisterMessage(GetPermissionDetailResponse)

GetPermissionDetailResponseWrapper = _reflection.GeneratedProtocolMessageType('GetPermissionDetailResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _GETPERMISSIONDETAILRESPONSEWRAPPER,
  '__module__' : 'get_permission_detail_pb2'
  # @@protoc_insertion_point(class_scope:permission.GetPermissionDetailResponseWrapper)
  })
_sym_db.RegisterMessage(GetPermissionDetailResponseWrapper)


# @@protoc_insertion_point(module_scope)
