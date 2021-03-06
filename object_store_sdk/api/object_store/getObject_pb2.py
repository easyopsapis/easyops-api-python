# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: getObject.proto

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
  name='getObject.proto',
  package='object_store',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0fgetObject.proto\x12\x0cobject_store\x1a\x1bgoogle/protobuf/empty.proto\":\n\x10GetObjectRequest\x12\x12\n\nbucketName\x18\x01 \x01(\t\x12\x12\n\nobjectName\x18\x02 \x01(\tb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_GETOBJECTREQUEST = _descriptor.Descriptor(
  name='GetObjectRequest',
  full_name='object_store.GetObjectRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bucketName', full_name='object_store.GetObjectRequest.bucketName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectName', full_name='object_store.GetObjectRequest.objectName', index=1,
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
  serialized_start=62,
  serialized_end=120,
)

DESCRIPTOR.message_types_by_name['GetObjectRequest'] = _GETOBJECTREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetObjectRequest = _reflection.GeneratedProtocolMessageType('GetObjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETOBJECTREQUEST,
  '__module__' : 'getObject_pb2'
  # @@protoc_insertion_point(class_scope:object_store.GetObjectRequest)
  })
_sym_db.RegisterMessage(GetObjectRequest)


# @@protoc_insertion_point(module_scope)
