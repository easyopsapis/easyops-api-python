# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fulltext_search.proto

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
  name='fulltext_search.proto',
  package='instance',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x15\x66ulltext_search.proto\x12\x08instance\x1a\x1cgoogle/protobuf/struct.proto\"r\n\x15\x46ulltextSearchRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x0f\n\x07keyword\x18\x03 \x01(\t\x12\x11\n\tobject_id\x18\x04 \x01(\t\x12\x14\n\x0cprefixSearch\x18\x05 \x01(\t\"\x97\x01\n\x16\x46ulltextSearchResponse\x12%\n\x04list\x18\x01 \x03(\x0b\x32\x17.google.protobuf.Struct\x12\r\n\x05total\x18\x02 \x01(\x05\x12\x0c\n\x04page\x18\x03 \x01(\x05\x12\x11\n\tpage_size\x18\x04 \x01(\x05\x12&\n\x05\x63ount\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\"\x81\x01\n\x1d\x46ulltextSearchResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12.\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32 .instance.FulltextSearchResponseb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_FULLTEXTSEARCHREQUEST = _descriptor.Descriptor(
  name='FulltextSearchRequest',
  full_name='instance.FulltextSearchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='instance.FulltextSearchRequest.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='instance.FulltextSearchRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keyword', full_name='instance.FulltextSearchRequest.keyword', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object_id', full_name='instance.FulltextSearchRequest.object_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prefixSearch', full_name='instance.FulltextSearchRequest.prefixSearch', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=65,
  serialized_end=179,
)


_FULLTEXTSEARCHRESPONSE = _descriptor.Descriptor(
  name='FulltextSearchResponse',
  full_name='instance.FulltextSearchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='list', full_name='instance.FulltextSearchResponse.list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='instance.FulltextSearchResponse.total', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page', full_name='instance.FulltextSearchResponse.page', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='instance.FulltextSearchResponse.page_size', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='instance.FulltextSearchResponse.count', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=182,
  serialized_end=333,
)


_FULLTEXTSEARCHRESPONSEWRAPPER = _descriptor.Descriptor(
  name='FulltextSearchResponseWrapper',
  full_name='instance.FulltextSearchResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='instance.FulltextSearchResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='instance.FulltextSearchResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='instance.FulltextSearchResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='instance.FulltextSearchResponseWrapper.data', index=3,
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
  serialized_start=336,
  serialized_end=465,
)

_FULLTEXTSEARCHRESPONSE.fields_by_name['list'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_FULLTEXTSEARCHRESPONSE.fields_by_name['count'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_FULLTEXTSEARCHRESPONSEWRAPPER.fields_by_name['data'].message_type = _FULLTEXTSEARCHRESPONSE
DESCRIPTOR.message_types_by_name['FulltextSearchRequest'] = _FULLTEXTSEARCHREQUEST
DESCRIPTOR.message_types_by_name['FulltextSearchResponse'] = _FULLTEXTSEARCHRESPONSE
DESCRIPTOR.message_types_by_name['FulltextSearchResponseWrapper'] = _FULLTEXTSEARCHRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FulltextSearchRequest = _reflection.GeneratedProtocolMessageType('FulltextSearchRequest', (_message.Message,), {
  'DESCRIPTOR' : _FULLTEXTSEARCHREQUEST,
  '__module__' : 'fulltext_search_pb2'
  # @@protoc_insertion_point(class_scope:instance.FulltextSearchRequest)
  })
_sym_db.RegisterMessage(FulltextSearchRequest)

FulltextSearchResponse = _reflection.GeneratedProtocolMessageType('FulltextSearchResponse', (_message.Message,), {
  'DESCRIPTOR' : _FULLTEXTSEARCHRESPONSE,
  '__module__' : 'fulltext_search_pb2'
  # @@protoc_insertion_point(class_scope:instance.FulltextSearchResponse)
  })
_sym_db.RegisterMessage(FulltextSearchResponse)

FulltextSearchResponseWrapper = _reflection.GeneratedProtocolMessageType('FulltextSearchResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _FULLTEXTSEARCHRESPONSEWRAPPER,
  '__module__' : 'fulltext_search_pb2'
  # @@protoc_insertion_point(class_scope:instance.FulltextSearchResponseWrapper)
  })
_sym_db.RegisterMessage(FulltextSearchResponseWrapper)


# @@protoc_insertion_point(module_scope)
