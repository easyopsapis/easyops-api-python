# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: search_comment.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from topboard_sdk.model.topboard import comment_pb2 as topboard__sdk_dot_model_dot_topboard_dot_comment__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='search_comment.proto',
  package='topboard',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14search_comment.proto\x12\x08topboard\x1a)topboard_sdk/model/topboard/comment.proto\x1a\x1cgoogle/protobuf/struct.proto\"\x88\x01\n\x14SearchCommentRequest\x12&\n\x05query\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\'\n\x06\x66ields\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0c\n\x04page\x18\x03 \x01(\x05\x12\x11\n\tpage_size\x18\x04 \x01(\x05\"h\n\x15SearchCommentResponse\x12\x1f\n\x04list\x18\x01 \x03(\x0b\x32\x11.topboard.Comment\x12\r\n\x05total\x18\x02 \x01(\x05\x12\x0c\n\x04page\x18\x03 \x01(\x05\x12\x11\n\tpage_size\x18\x04 \x01(\x05\"\x7f\n\x1cSearchCommentResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12-\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1f.topboard.SearchCommentResponseb\x06proto3')
  ,
  dependencies=[topboard__sdk_dot_model_dot_topboard_dot_comment__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_SEARCHCOMMENTREQUEST = _descriptor.Descriptor(
  name='SearchCommentRequest',
  full_name='topboard.SearchCommentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='topboard.SearchCommentRequest.query', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fields', full_name='topboard.SearchCommentRequest.fields', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page', full_name='topboard.SearchCommentRequest.page', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='topboard.SearchCommentRequest.page_size', index=3,
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
  serialized_start=108,
  serialized_end=244,
)


_SEARCHCOMMENTRESPONSE = _descriptor.Descriptor(
  name='SearchCommentResponse',
  full_name='topboard.SearchCommentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='list', full_name='topboard.SearchCommentResponse.list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='topboard.SearchCommentResponse.total', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page', full_name='topboard.SearchCommentResponse.page', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='topboard.SearchCommentResponse.page_size', index=3,
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
  serialized_start=246,
  serialized_end=350,
)


_SEARCHCOMMENTRESPONSEWRAPPER = _descriptor.Descriptor(
  name='SearchCommentResponseWrapper',
  full_name='topboard.SearchCommentResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='topboard.SearchCommentResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='topboard.SearchCommentResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='topboard.SearchCommentResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='topboard.SearchCommentResponseWrapper.data', index=3,
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
  serialized_start=352,
  serialized_end=479,
)

_SEARCHCOMMENTREQUEST.fields_by_name['query'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SEARCHCOMMENTREQUEST.fields_by_name['fields'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SEARCHCOMMENTRESPONSE.fields_by_name['list'].message_type = topboard__sdk_dot_model_dot_topboard_dot_comment__pb2._COMMENT
_SEARCHCOMMENTRESPONSEWRAPPER.fields_by_name['data'].message_type = _SEARCHCOMMENTRESPONSE
DESCRIPTOR.message_types_by_name['SearchCommentRequest'] = _SEARCHCOMMENTREQUEST
DESCRIPTOR.message_types_by_name['SearchCommentResponse'] = _SEARCHCOMMENTRESPONSE
DESCRIPTOR.message_types_by_name['SearchCommentResponseWrapper'] = _SEARCHCOMMENTRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SearchCommentRequest = _reflection.GeneratedProtocolMessageType('SearchCommentRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHCOMMENTREQUEST,
  '__module__' : 'search_comment_pb2'
  # @@protoc_insertion_point(class_scope:topboard.SearchCommentRequest)
  })
_sym_db.RegisterMessage(SearchCommentRequest)

SearchCommentResponse = _reflection.GeneratedProtocolMessageType('SearchCommentResponse', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHCOMMENTRESPONSE,
  '__module__' : 'search_comment_pb2'
  # @@protoc_insertion_point(class_scope:topboard.SearchCommentResponse)
  })
_sym_db.RegisterMessage(SearchCommentResponse)

SearchCommentResponseWrapper = _reflection.GeneratedProtocolMessageType('SearchCommentResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHCOMMENTRESPONSEWRAPPER,
  '__module__' : 'search_comment_pb2'
  # @@protoc_insertion_point(class_scope:topboard.SearchCommentResponseWrapper)
  })
_sym_db.RegisterMessage(SearchCommentResponseWrapper)


# @@protoc_insertion_point(module_scope)
