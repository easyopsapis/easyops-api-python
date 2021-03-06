# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list_child_object.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cmdb_sdk.model.cmdb import cmdb_object_pb2 as cmdb__sdk_dot_model_dot_cmdb_dot_cmdb__object__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='list_child_object.proto',
  package='cmdb_object',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x17list_child_object.proto\x12\x0b\x63mdb_object\x1a%cmdb_sdk/model/cmdb/cmdb_object.proto\"H\n\x16ListChildObjectRequest\x12\x1c\n\x14ignoreAttrPermission\x18\x01 \x01(\x08\x12\x10\n\x08objectId\x18\x02 \x01(\t\"g\n\x17ListChildObjectResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\r\n\x05\x65rror\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\x12\x1e\n\x04\x64\x61ta\x18\x04 \x03(\x0b\x32\x10.cmdb.CmdbObject\"\x86\x01\n\x1eListChildObjectResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x32\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32$.cmdb_object.ListChildObjectResponseb\x06proto3')
  ,
  dependencies=[cmdb__sdk_dot_model_dot_cmdb_dot_cmdb__object__pb2.DESCRIPTOR,])




_LISTCHILDOBJECTREQUEST = _descriptor.Descriptor(
  name='ListChildObjectRequest',
  full_name='cmdb_object.ListChildObjectRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ignoreAttrPermission', full_name='cmdb_object.ListChildObjectRequest.ignoreAttrPermission', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectId', full_name='cmdb_object.ListChildObjectRequest.objectId', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=79,
  serialized_end=151,
)


_LISTCHILDOBJECTRESPONSE = _descriptor.Descriptor(
  name='ListChildObjectResponse',
  full_name='cmdb_object.ListChildObjectResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='cmdb_object.ListChildObjectResponse.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='cmdb_object.ListChildObjectResponse.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='cmdb_object.ListChildObjectResponse.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='cmdb_object.ListChildObjectResponse.data', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_end=256,
)


_LISTCHILDOBJECTRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListChildObjectResponseWrapper',
  full_name='cmdb_object.ListChildObjectResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='cmdb_object.ListChildObjectResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='cmdb_object.ListChildObjectResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='cmdb_object.ListChildObjectResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='cmdb_object.ListChildObjectResponseWrapper.data', index=3,
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
  serialized_start=259,
  serialized_end=393,
)

_LISTCHILDOBJECTRESPONSE.fields_by_name['data'].message_type = cmdb__sdk_dot_model_dot_cmdb_dot_cmdb__object__pb2._CMDBOBJECT
_LISTCHILDOBJECTRESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTCHILDOBJECTRESPONSE
DESCRIPTOR.message_types_by_name['ListChildObjectRequest'] = _LISTCHILDOBJECTREQUEST
DESCRIPTOR.message_types_by_name['ListChildObjectResponse'] = _LISTCHILDOBJECTRESPONSE
DESCRIPTOR.message_types_by_name['ListChildObjectResponseWrapper'] = _LISTCHILDOBJECTRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListChildObjectRequest = _reflection.GeneratedProtocolMessageType('ListChildObjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTCHILDOBJECTREQUEST,
  '__module__' : 'list_child_object_pb2'
  # @@protoc_insertion_point(class_scope:cmdb_object.ListChildObjectRequest)
  })
_sym_db.RegisterMessage(ListChildObjectRequest)

ListChildObjectResponse = _reflection.GeneratedProtocolMessageType('ListChildObjectResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTCHILDOBJECTRESPONSE,
  '__module__' : 'list_child_object_pb2'
  # @@protoc_insertion_point(class_scope:cmdb_object.ListChildObjectResponse)
  })
_sym_db.RegisterMessage(ListChildObjectResponse)

ListChildObjectResponseWrapper = _reflection.GeneratedProtocolMessageType('ListChildObjectResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _LISTCHILDOBJECTRESPONSEWRAPPER,
  '__module__' : 'list_child_object_pb2'
  # @@protoc_insertion_point(class_scope:cmdb_object.ListChildObjectResponseWrapper)
  })
_sym_db.RegisterMessage(ListChildObjectResponseWrapper)


# @@protoc_insertion_point(module_scope)
