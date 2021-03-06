# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: search_issue.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from topboard_sdk.model.topboard import issue_pb2 as topboard__sdk_dot_model_dot_topboard_dot_issue__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='search_issue.proto',
  package='topboard',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x12search_issue.proto\x12\x08topboard\x1a\'topboard_sdk/model/topboard/issue.proto\x1a\x1cgoogle/protobuf/struct.proto\"\x86\x01\n\x12SearchIssueRequest\x12&\n\x05query\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\'\n\x06\x66ields\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0c\n\x04page\x18\x03 \x01(\x05\x12\x11\n\tpage_size\x18\x04 \x01(\x05\"d\n\x13SearchIssueResponse\x12\x1d\n\x04list\x18\x01 \x03(\x0b\x32\x0f.topboard.Issue\x12\r\n\x05total\x18\x02 \x01(\x05\x12\x0c\n\x04page\x18\x03 \x01(\x05\x12\x11\n\tpage_size\x18\x04 \x01(\x05\"{\n\x1aSearchIssueResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12+\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1d.topboard.SearchIssueResponseb\x06proto3')
  ,
  dependencies=[topboard__sdk_dot_model_dot_topboard_dot_issue__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_SEARCHISSUEREQUEST = _descriptor.Descriptor(
  name='SearchIssueRequest',
  full_name='topboard.SearchIssueRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='topboard.SearchIssueRequest.query', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fields', full_name='topboard.SearchIssueRequest.fields', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page', full_name='topboard.SearchIssueRequest.page', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='topboard.SearchIssueRequest.page_size', index=3,
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
  serialized_start=104,
  serialized_end=238,
)


_SEARCHISSUERESPONSE = _descriptor.Descriptor(
  name='SearchIssueResponse',
  full_name='topboard.SearchIssueResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='list', full_name='topboard.SearchIssueResponse.list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='topboard.SearchIssueResponse.total', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page', full_name='topboard.SearchIssueResponse.page', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='topboard.SearchIssueResponse.page_size', index=3,
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
  serialized_start=240,
  serialized_end=340,
)


_SEARCHISSUERESPONSEWRAPPER = _descriptor.Descriptor(
  name='SearchIssueResponseWrapper',
  full_name='topboard.SearchIssueResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='topboard.SearchIssueResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='topboard.SearchIssueResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='topboard.SearchIssueResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='topboard.SearchIssueResponseWrapper.data', index=3,
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
  serialized_start=342,
  serialized_end=465,
)

_SEARCHISSUEREQUEST.fields_by_name['query'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SEARCHISSUEREQUEST.fields_by_name['fields'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SEARCHISSUERESPONSE.fields_by_name['list'].message_type = topboard__sdk_dot_model_dot_topboard_dot_issue__pb2._ISSUE
_SEARCHISSUERESPONSEWRAPPER.fields_by_name['data'].message_type = _SEARCHISSUERESPONSE
DESCRIPTOR.message_types_by_name['SearchIssueRequest'] = _SEARCHISSUEREQUEST
DESCRIPTOR.message_types_by_name['SearchIssueResponse'] = _SEARCHISSUERESPONSE
DESCRIPTOR.message_types_by_name['SearchIssueResponseWrapper'] = _SEARCHISSUERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SearchIssueRequest = _reflection.GeneratedProtocolMessageType('SearchIssueRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHISSUEREQUEST,
  '__module__' : 'search_issue_pb2'
  # @@protoc_insertion_point(class_scope:topboard.SearchIssueRequest)
  })
_sym_db.RegisterMessage(SearchIssueRequest)

SearchIssueResponse = _reflection.GeneratedProtocolMessageType('SearchIssueResponse', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHISSUERESPONSE,
  '__module__' : 'search_issue_pb2'
  # @@protoc_insertion_point(class_scope:topboard.SearchIssueResponse)
  })
_sym_db.RegisterMessage(SearchIssueResponse)

SearchIssueResponseWrapper = _reflection.GeneratedProtocolMessageType('SearchIssueResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHISSUERESPONSEWRAPPER,
  '__module__' : 'search_issue_pb2'
  # @@protoc_insertion_point(class_scope:topboard.SearchIssueResponseWrapper)
  })
_sym_db.RegisterMessage(SearchIssueResponseWrapper)


# @@protoc_insertion_point(module_scope)
