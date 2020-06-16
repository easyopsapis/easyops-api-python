# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: batch_search.proto

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
  name='batch_search.proto',
  package='instance',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x12\x62\x61tch_search.proto\x12\x08instance\x1a\x1cgoogle/protobuf/struct.proto\"\x89\x03\n\x12\x42\x61tchSearchRequest\x12/\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32!.instance.BatchSearchRequest.Data\x1a\xc1\x02\n\x04\x44\x61ta\x12\x11\n\tobject_id\x18\x01 \x01(\t\x12\x38\n\x06search\x18\x02 \x01(\x0b\x32(.instance.BatchSearchRequest.Data.Search\x1a\xeb\x01\n\x06Search\x12&\n\x05query\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\'\n\x06\x66ields\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x18\n\x10only_my_instance\x18\x03 \x01(\x08\x12\x1a\n\x12only_relation_view\x18\x04 \x01(\x08\x12\x0c\n\x04page\x18\x05 \x01(\x05\x12\x11\n\tpage_size\x18\x06 \x01(\x05\x12%\n\x04sort\x18\x07 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x12\n\npermission\x18\x08 \x03(\t\"\xd4\x01\n\x13\x42\x61tchSearchResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\r\n\x05\x65rror\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\x12\x30\n\x04\x64\x61ta\x18\x04 \x03(\x0b\x32\".instance.BatchSearchResponse.Data\x1a]\n\x04\x44\x61ta\x12%\n\x04list\x18\x01 \x03(\x0b\x32\x17.google.protobuf.Struct\x12\r\n\x05total\x18\x02 \x01(\x05\x12\x0c\n\x04page\x18\x03 \x01(\x05\x12\x11\n\tpage_size\x18\x04 \x01(\x05\"{\n\x1a\x42\x61tchSearchResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12+\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1d.instance.BatchSearchResponseb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_BATCHSEARCHREQUEST_DATA_SEARCH = _descriptor.Descriptor(
  name='Search',
  full_name='instance.BatchSearchRequest.Data.Search',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='instance.BatchSearchRequest.Data.Search.query', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fields', full_name='instance.BatchSearchRequest.Data.Search.fields', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='only_my_instance', full_name='instance.BatchSearchRequest.Data.Search.only_my_instance', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='only_relation_view', full_name='instance.BatchSearchRequest.Data.Search.only_relation_view', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page', full_name='instance.BatchSearchRequest.Data.Search.page', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='instance.BatchSearchRequest.Data.Search.page_size', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sort', full_name='instance.BatchSearchRequest.Data.Search.sort', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='permission', full_name='instance.BatchSearchRequest.Data.Search.permission', index=7,
      number=8, type=9, cpp_type=9, label=3,
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
  serialized_start=221,
  serialized_end=456,
)

_BATCHSEARCHREQUEST_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='instance.BatchSearchRequest.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_id', full_name='instance.BatchSearchRequest.Data.object_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='search', full_name='instance.BatchSearchRequest.Data.search', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_BATCHSEARCHREQUEST_DATA_SEARCH, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=456,
)

_BATCHSEARCHREQUEST = _descriptor.Descriptor(
  name='BatchSearchRequest',
  full_name='instance.BatchSearchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='instance.BatchSearchRequest.data', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_BATCHSEARCHREQUEST_DATA, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=63,
  serialized_end=456,
)


_BATCHSEARCHRESPONSE_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='instance.BatchSearchResponse.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='list', full_name='instance.BatchSearchResponse.Data.list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='instance.BatchSearchResponse.Data.total', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page', full_name='instance.BatchSearchResponse.Data.page', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='instance.BatchSearchResponse.Data.page_size', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=578,
  serialized_end=671,
)

_BATCHSEARCHRESPONSE = _descriptor.Descriptor(
  name='BatchSearchResponse',
  full_name='instance.BatchSearchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='instance.BatchSearchResponse.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='instance.BatchSearchResponse.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='instance.BatchSearchResponse.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='instance.BatchSearchResponse.data', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_BATCHSEARCHRESPONSE_DATA, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=459,
  serialized_end=671,
)


_BATCHSEARCHRESPONSEWRAPPER = _descriptor.Descriptor(
  name='BatchSearchResponseWrapper',
  full_name='instance.BatchSearchResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='instance.BatchSearchResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='instance.BatchSearchResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='instance.BatchSearchResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='instance.BatchSearchResponseWrapper.data', index=3,
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
  serialized_start=673,
  serialized_end=796,
)

_BATCHSEARCHREQUEST_DATA_SEARCH.fields_by_name['query'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_BATCHSEARCHREQUEST_DATA_SEARCH.fields_by_name['fields'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_BATCHSEARCHREQUEST_DATA_SEARCH.fields_by_name['sort'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_BATCHSEARCHREQUEST_DATA_SEARCH.containing_type = _BATCHSEARCHREQUEST_DATA
_BATCHSEARCHREQUEST_DATA.fields_by_name['search'].message_type = _BATCHSEARCHREQUEST_DATA_SEARCH
_BATCHSEARCHREQUEST_DATA.containing_type = _BATCHSEARCHREQUEST
_BATCHSEARCHREQUEST.fields_by_name['data'].message_type = _BATCHSEARCHREQUEST_DATA
_BATCHSEARCHRESPONSE_DATA.fields_by_name['list'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_BATCHSEARCHRESPONSE_DATA.containing_type = _BATCHSEARCHRESPONSE
_BATCHSEARCHRESPONSE.fields_by_name['data'].message_type = _BATCHSEARCHRESPONSE_DATA
_BATCHSEARCHRESPONSEWRAPPER.fields_by_name['data'].message_type = _BATCHSEARCHRESPONSE
DESCRIPTOR.message_types_by_name['BatchSearchRequest'] = _BATCHSEARCHREQUEST
DESCRIPTOR.message_types_by_name['BatchSearchResponse'] = _BATCHSEARCHRESPONSE
DESCRIPTOR.message_types_by_name['BatchSearchResponseWrapper'] = _BATCHSEARCHRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BatchSearchRequest = _reflection.GeneratedProtocolMessageType('BatchSearchRequest', (_message.Message,), {

  'Data' : _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), {

    'Search' : _reflection.GeneratedProtocolMessageType('Search', (_message.Message,), {
      'DESCRIPTOR' : _BATCHSEARCHREQUEST_DATA_SEARCH,
      '__module__' : 'batch_search_pb2'
      # @@protoc_insertion_point(class_scope:instance.BatchSearchRequest.Data.Search)
      })
    ,
    'DESCRIPTOR' : _BATCHSEARCHREQUEST_DATA,
    '__module__' : 'batch_search_pb2'
    # @@protoc_insertion_point(class_scope:instance.BatchSearchRequest.Data)
    })
  ,
  'DESCRIPTOR' : _BATCHSEARCHREQUEST,
  '__module__' : 'batch_search_pb2'
  # @@protoc_insertion_point(class_scope:instance.BatchSearchRequest)
  })
_sym_db.RegisterMessage(BatchSearchRequest)
_sym_db.RegisterMessage(BatchSearchRequest.Data)
_sym_db.RegisterMessage(BatchSearchRequest.Data.Search)

BatchSearchResponse = _reflection.GeneratedProtocolMessageType('BatchSearchResponse', (_message.Message,), {

  'Data' : _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), {
    'DESCRIPTOR' : _BATCHSEARCHRESPONSE_DATA,
    '__module__' : 'batch_search_pb2'
    # @@protoc_insertion_point(class_scope:instance.BatchSearchResponse.Data)
    })
  ,
  'DESCRIPTOR' : _BATCHSEARCHRESPONSE,
  '__module__' : 'batch_search_pb2'
  # @@protoc_insertion_point(class_scope:instance.BatchSearchResponse)
  })
_sym_db.RegisterMessage(BatchSearchResponse)
_sym_db.RegisterMessage(BatchSearchResponse.Data)

BatchSearchResponseWrapper = _reflection.GeneratedProtocolMessageType('BatchSearchResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _BATCHSEARCHRESPONSEWRAPPER,
  '__module__' : 'batch_search_pb2'
  # @@protoc_insertion_point(class_scope:instance.BatchSearchResponseWrapper)
  })
_sym_db.RegisterMessage(BatchSearchResponseWrapper)


# @@protoc_insertion_point(module_scope)