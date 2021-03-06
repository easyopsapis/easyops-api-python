# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: listBuckets.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='listBuckets.proto',
  package='object_store',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11listBuckets.proto\x12\x0cobject_store\"\x86\x01\n\x13ListBucketsResponse\x12:\n\x07\x62uckets\x18\x01 \x03(\x0b\x32).object_store.ListBucketsResponse.Buckets\x1a\x33\n\x07\x42uckets\x12\x12\n\nbucketName\x18\x01 \x01(\t\x12\x14\n\x0c\x63reationDate\x18\x02 \x01(\t\"\x7f\n\x1aListBucketsResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12/\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32!.object_store.ListBucketsResponseb\x06proto3')
)




_LISTBUCKETSRESPONSE_BUCKETS = _descriptor.Descriptor(
  name='Buckets',
  full_name='object_store.ListBucketsResponse.Buckets',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bucketName', full_name='object_store.ListBucketsResponse.Buckets.bucketName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creationDate', full_name='object_store.ListBucketsResponse.Buckets.creationDate', index=1,
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
  serialized_start=119,
  serialized_end=170,
)

_LISTBUCKETSRESPONSE = _descriptor.Descriptor(
  name='ListBucketsResponse',
  full_name='object_store.ListBucketsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='buckets', full_name='object_store.ListBucketsResponse.buckets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTBUCKETSRESPONSE_BUCKETS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=170,
)


_LISTBUCKETSRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListBucketsResponseWrapper',
  full_name='object_store.ListBucketsResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='object_store.ListBucketsResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='object_store.ListBucketsResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='object_store.ListBucketsResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='object_store.ListBucketsResponseWrapper.data', index=3,
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
  serialized_start=172,
  serialized_end=299,
)

_LISTBUCKETSRESPONSE_BUCKETS.containing_type = _LISTBUCKETSRESPONSE
_LISTBUCKETSRESPONSE.fields_by_name['buckets'].message_type = _LISTBUCKETSRESPONSE_BUCKETS
_LISTBUCKETSRESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTBUCKETSRESPONSE
DESCRIPTOR.message_types_by_name['ListBucketsResponse'] = _LISTBUCKETSRESPONSE
DESCRIPTOR.message_types_by_name['ListBucketsResponseWrapper'] = _LISTBUCKETSRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListBucketsResponse = _reflection.GeneratedProtocolMessageType('ListBucketsResponse', (_message.Message,), {

  'Buckets' : _reflection.GeneratedProtocolMessageType('Buckets', (_message.Message,), {
    'DESCRIPTOR' : _LISTBUCKETSRESPONSE_BUCKETS,
    '__module__' : 'listBuckets_pb2'
    # @@protoc_insertion_point(class_scope:object_store.ListBucketsResponse.Buckets)
    })
  ,
  'DESCRIPTOR' : _LISTBUCKETSRESPONSE,
  '__module__' : 'listBuckets_pb2'
  # @@protoc_insertion_point(class_scope:object_store.ListBucketsResponse)
  })
_sym_db.RegisterMessage(ListBucketsResponse)
_sym_db.RegisterMessage(ListBucketsResponse.Buckets)

ListBucketsResponseWrapper = _reflection.GeneratedProtocolMessageType('ListBucketsResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _LISTBUCKETSRESPONSEWRAPPER,
  '__module__' : 'listBuckets_pb2'
  # @@protoc_insertion_point(class_scope:object_store.ListBucketsResponseWrapper)
  })
_sym_db.RegisterMessage(ListBucketsResponseWrapper)


# @@protoc_insertion_point(module_scope)
