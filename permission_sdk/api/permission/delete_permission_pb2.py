# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: delete_permission.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='delete_permission.proto',
  package='permission',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x17\x64\x65lete_permission.proto\x12\npermission\")\n\x17\x44\x65letePermissionRequest\x12\x0e\n\x06\x61\x63tion\x18\x01 \x01(\t\"\x85\x01\n\x18\x44\x65letePermissionResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x37\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32).permission.DeletePermissionResponse.Data\x1a\x15\n\x04\x44\x61ta\x12\r\n\x05\x63ount\x18\x01 \x01(\x05\"\x87\x01\n\x1f\x44\x65letePermissionResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x32\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32$.permission.DeletePermissionResponseb\x06proto3')
)




_DELETEPERMISSIONREQUEST = _descriptor.Descriptor(
  name='DeletePermissionRequest',
  full_name='permission.DeletePermissionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='permission.DeletePermissionRequest.action', index=0,
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
  serialized_start=39,
  serialized_end=80,
)


_DELETEPERMISSIONRESPONSE_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='permission.DeletePermissionResponse.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='permission.DeletePermissionResponse.Data.count', index=0,
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
  serialized_start=195,
  serialized_end=216,
)

_DELETEPERMISSIONRESPONSE = _descriptor.Descriptor(
  name='DeletePermissionResponse',
  full_name='permission.DeletePermissionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='permission.DeletePermissionResponse.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='permission.DeletePermissionResponse.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='permission.DeletePermissionResponse.data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DELETEPERMISSIONRESPONSE_DATA, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=83,
  serialized_end=216,
)


_DELETEPERMISSIONRESPONSEWRAPPER = _descriptor.Descriptor(
  name='DeletePermissionResponseWrapper',
  full_name='permission.DeletePermissionResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='permission.DeletePermissionResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='permission.DeletePermissionResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='permission.DeletePermissionResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='permission.DeletePermissionResponseWrapper.data', index=3,
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
  serialized_start=219,
  serialized_end=354,
)

_DELETEPERMISSIONRESPONSE_DATA.containing_type = _DELETEPERMISSIONRESPONSE
_DELETEPERMISSIONRESPONSE.fields_by_name['data'].message_type = _DELETEPERMISSIONRESPONSE_DATA
_DELETEPERMISSIONRESPONSEWRAPPER.fields_by_name['data'].message_type = _DELETEPERMISSIONRESPONSE
DESCRIPTOR.message_types_by_name['DeletePermissionRequest'] = _DELETEPERMISSIONREQUEST
DESCRIPTOR.message_types_by_name['DeletePermissionResponse'] = _DELETEPERMISSIONRESPONSE
DESCRIPTOR.message_types_by_name['DeletePermissionResponseWrapper'] = _DELETEPERMISSIONRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeletePermissionRequest = _reflection.GeneratedProtocolMessageType('DeletePermissionRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEPERMISSIONREQUEST,
  '__module__' : 'delete_permission_pb2'
  # @@protoc_insertion_point(class_scope:permission.DeletePermissionRequest)
  })
_sym_db.RegisterMessage(DeletePermissionRequest)

DeletePermissionResponse = _reflection.GeneratedProtocolMessageType('DeletePermissionResponse', (_message.Message,), {

  'Data' : _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), {
    'DESCRIPTOR' : _DELETEPERMISSIONRESPONSE_DATA,
    '__module__' : 'delete_permission_pb2'
    # @@protoc_insertion_point(class_scope:permission.DeletePermissionResponse.Data)
    })
  ,
  'DESCRIPTOR' : _DELETEPERMISSIONRESPONSE,
  '__module__' : 'delete_permission_pb2'
  # @@protoc_insertion_point(class_scope:permission.DeletePermissionResponse)
  })
_sym_db.RegisterMessage(DeletePermissionResponse)
_sym_db.RegisterMessage(DeletePermissionResponse.Data)

DeletePermissionResponseWrapper = _reflection.GeneratedProtocolMessageType('DeletePermissionResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _DELETEPERMISSIONRESPONSEWRAPPER,
  '__module__' : 'delete_permission_pb2'
  # @@protoc_insertion_point(class_scope:permission.DeletePermissionResponseWrapper)
  })
_sym_db.RegisterMessage(DeletePermissionResponseWrapper)


# @@protoc_insertion_point(module_scope)