# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: delete_backlog.proto

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
  name='delete_backlog.proto',
  package='backlog',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14\x64\x65lete_backlog.proto\x12\x07\x62\x61\x63klog\x1a\x1bgoogle/protobuf/empty.proto\"4\n\x14\x44\x65leteBacklogRequest\x12\x10\n\x08\x63\x61tegory\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\"v\n\x1c\x44\x65leteBacklogResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12$\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x16.google.protobuf.Emptyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_DELETEBACKLOGREQUEST = _descriptor.Descriptor(
  name='DeleteBacklogRequest',
  full_name='backlog.DeleteBacklogRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='category', full_name='backlog.DeleteBacklogRequest.category', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='backlog.DeleteBacklogRequest.id', index=1,
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
  serialized_end=114,
)


_DELETEBACKLOGRESPONSEWRAPPER = _descriptor.Descriptor(
  name='DeleteBacklogResponseWrapper',
  full_name='backlog.DeleteBacklogResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='backlog.DeleteBacklogResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='backlog.DeleteBacklogResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='backlog.DeleteBacklogResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='backlog.DeleteBacklogResponseWrapper.data', index=3,
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
  serialized_start=116,
  serialized_end=234,
)

_DELETEBACKLOGRESPONSEWRAPPER.fields_by_name['data'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
DESCRIPTOR.message_types_by_name['DeleteBacklogRequest'] = _DELETEBACKLOGREQUEST
DESCRIPTOR.message_types_by_name['DeleteBacklogResponseWrapper'] = _DELETEBACKLOGRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeleteBacklogRequest = _reflection.GeneratedProtocolMessageType('DeleteBacklogRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEBACKLOGREQUEST,
  '__module__' : 'delete_backlog_pb2'
  # @@protoc_insertion_point(class_scope:backlog.DeleteBacklogRequest)
  })
_sym_db.RegisterMessage(DeleteBacklogRequest)

DeleteBacklogResponseWrapper = _reflection.GeneratedProtocolMessageType('DeleteBacklogResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _DELETEBACKLOGRESPONSEWRAPPER,
  '__module__' : 'delete_backlog_pb2'
  # @@protoc_insertion_point(class_scope:backlog.DeleteBacklogResponseWrapper)
  })
_sym_db.RegisterMessage(DeleteBacklogResponseWrapper)


# @@protoc_insertion_point(module_scope)
