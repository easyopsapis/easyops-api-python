# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: search_sprint.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from topboard_sdk.model.topboard import sprint_pb2 as topboard__sdk_dot_model_dot_topboard_dot_sprint__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='search_sprint.proto',
  package='topboard',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13search_sprint.proto\x12\x08topboard\x1a(topboard_sdk/model/topboard/sprint.proto\x1a\x1cgoogle/protobuf/struct.proto\"\x87\x01\n\x13SearchSprintRequest\x12&\n\x05query\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\'\n\x06\x66ields\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0c\n\x04page\x18\x03 \x01(\x05\x12\x11\n\tpage_size\x18\x04 \x01(\x05\"f\n\x14SearchSprintResponse\x12\x1e\n\x04list\x18\x01 \x03(\x0b\x32\x10.topboard.Sprint\x12\r\n\x05total\x18\x02 \x01(\x05\x12\x0c\n\x04page\x18\x03 \x01(\x05\x12\x11\n\tpage_size\x18\x04 \x01(\x05\"}\n\x1bSearchSprintResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12,\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1e.topboard.SearchSprintResponseb\x06proto3')
  ,
  dependencies=[topboard__sdk_dot_model_dot_topboard_dot_sprint__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_SEARCHSPRINTREQUEST = _descriptor.Descriptor(
  name='SearchSprintRequest',
  full_name='topboard.SearchSprintRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='topboard.SearchSprintRequest.query', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fields', full_name='topboard.SearchSprintRequest.fields', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page', full_name='topboard.SearchSprintRequest.page', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='topboard.SearchSprintRequest.page_size', index=3,
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
  serialized_start=106,
  serialized_end=241,
)


_SEARCHSPRINTRESPONSE = _descriptor.Descriptor(
  name='SearchSprintResponse',
  full_name='topboard.SearchSprintResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='list', full_name='topboard.SearchSprintResponse.list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='topboard.SearchSprintResponse.total', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page', full_name='topboard.SearchSprintResponse.page', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='topboard.SearchSprintResponse.page_size', index=3,
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
  serialized_start=243,
  serialized_end=345,
)


_SEARCHSPRINTRESPONSEWRAPPER = _descriptor.Descriptor(
  name='SearchSprintResponseWrapper',
  full_name='topboard.SearchSprintResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='topboard.SearchSprintResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='topboard.SearchSprintResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='topboard.SearchSprintResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='topboard.SearchSprintResponseWrapper.data', index=3,
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
  serialized_start=347,
  serialized_end=472,
)

_SEARCHSPRINTREQUEST.fields_by_name['query'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SEARCHSPRINTREQUEST.fields_by_name['fields'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SEARCHSPRINTRESPONSE.fields_by_name['list'].message_type = topboard__sdk_dot_model_dot_topboard_dot_sprint__pb2._SPRINT
_SEARCHSPRINTRESPONSEWRAPPER.fields_by_name['data'].message_type = _SEARCHSPRINTRESPONSE
DESCRIPTOR.message_types_by_name['SearchSprintRequest'] = _SEARCHSPRINTREQUEST
DESCRIPTOR.message_types_by_name['SearchSprintResponse'] = _SEARCHSPRINTRESPONSE
DESCRIPTOR.message_types_by_name['SearchSprintResponseWrapper'] = _SEARCHSPRINTRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SearchSprintRequest = _reflection.GeneratedProtocolMessageType('SearchSprintRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHSPRINTREQUEST,
  '__module__' : 'search_sprint_pb2'
  # @@protoc_insertion_point(class_scope:topboard.SearchSprintRequest)
  })
_sym_db.RegisterMessage(SearchSprintRequest)

SearchSprintResponse = _reflection.GeneratedProtocolMessageType('SearchSprintResponse', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHSPRINTRESPONSE,
  '__module__' : 'search_sprint_pb2'
  # @@protoc_insertion_point(class_scope:topboard.SearchSprintResponse)
  })
_sym_db.RegisterMessage(SearchSprintResponse)

SearchSprintResponseWrapper = _reflection.GeneratedProtocolMessageType('SearchSprintResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHSPRINTRESPONSEWRAPPER,
  '__module__' : 'search_sprint_pb2'
  # @@protoc_insertion_point(class_scope:topboard.SearchSprintResponseWrapper)
  })
_sym_db.RegisterMessage(SearchSprintResponseWrapper)


# @@protoc_insertion_point(module_scope)
