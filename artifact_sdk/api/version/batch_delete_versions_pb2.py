# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: batch_delete_versions.proto

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
  name='batch_delete_versions.proto',
  package='version',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1b\x62\x61tch_delete_versions.proto\x12\x07version\x1a\x1bgoogle/protobuf/empty.proto\"W\n\x1a\x42\x61tchDeleteVersionsRequest\x12\x12\n\nversionIds\x18\x01 \x01(\t\x12\x12\n\ndeleteFile\x18\x02 \x01(\x08\x12\x11\n\tpackageId\x18\x03 \x01(\t\"|\n\"BatchDeleteVersionsResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12$\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x16.google.protobuf.Emptyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_BATCHDELETEVERSIONSREQUEST = _descriptor.Descriptor(
  name='BatchDeleteVersionsRequest',
  full_name='version.BatchDeleteVersionsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='versionIds', full_name='version.BatchDeleteVersionsRequest.versionIds', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deleteFile', full_name='version.BatchDeleteVersionsRequest.deleteFile', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageId', full_name='version.BatchDeleteVersionsRequest.packageId', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=69,
  serialized_end=156,
)


_BATCHDELETEVERSIONSRESPONSEWRAPPER = _descriptor.Descriptor(
  name='BatchDeleteVersionsResponseWrapper',
  full_name='version.BatchDeleteVersionsResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='version.BatchDeleteVersionsResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='version.BatchDeleteVersionsResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='version.BatchDeleteVersionsResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='version.BatchDeleteVersionsResponseWrapper.data', index=3,
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
  serialized_start=158,
  serialized_end=282,
)

_BATCHDELETEVERSIONSRESPONSEWRAPPER.fields_by_name['data'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
DESCRIPTOR.message_types_by_name['BatchDeleteVersionsRequest'] = _BATCHDELETEVERSIONSREQUEST
DESCRIPTOR.message_types_by_name['BatchDeleteVersionsResponseWrapper'] = _BATCHDELETEVERSIONSRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BatchDeleteVersionsRequest = _reflection.GeneratedProtocolMessageType('BatchDeleteVersionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _BATCHDELETEVERSIONSREQUEST,
  '__module__' : 'batch_delete_versions_pb2'
  # @@protoc_insertion_point(class_scope:version.BatchDeleteVersionsRequest)
  })
_sym_db.RegisterMessage(BatchDeleteVersionsRequest)

BatchDeleteVersionsResponseWrapper = _reflection.GeneratedProtocolMessageType('BatchDeleteVersionsResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _BATCHDELETEVERSIONSRESPONSEWRAPPER,
  '__module__' : 'batch_delete_versions_pb2'
  # @@protoc_insertion_point(class_scope:version.BatchDeleteVersionsResponseWrapper)
  })
_sym_db.RegisterMessage(BatchDeleteVersionsResponseWrapper)


# @@protoc_insertion_point(module_scope)
