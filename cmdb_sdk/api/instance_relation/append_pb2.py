# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: append.proto

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
  name='append.proto',
  package='instance_relation',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0c\x61ppend.proto\x12\x11instance_relation\x1a\x1bgoogle/protobuf/empty.proto\"m\n\rAppendRequest\x12\x10\n\x08objectId\x18\x01 \x01(\t\x12\x16\n\x0erelationSideId\x18\x02 \x01(\t\x12\x14\n\x0cinstance_ids\x18\x03 \x03(\t\x12\x1c\n\x14related_instance_ids\x18\x04 \x03(\t\"o\n\x15\x41ppendResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12$\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x16.google.protobuf.Emptyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_APPENDREQUEST = _descriptor.Descriptor(
  name='AppendRequest',
  full_name='instance_relation.AppendRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='objectId', full_name='instance_relation.AppendRequest.objectId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relationSideId', full_name='instance_relation.AppendRequest.relationSideId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instance_ids', full_name='instance_relation.AppendRequest.instance_ids', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='related_instance_ids', full_name='instance_relation.AppendRequest.related_instance_ids', index=3,
      number=4, type=9, cpp_type=9, label=3,
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
  serialized_start=64,
  serialized_end=173,
)


_APPENDRESPONSEWRAPPER = _descriptor.Descriptor(
  name='AppendResponseWrapper',
  full_name='instance_relation.AppendResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='instance_relation.AppendResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='instance_relation.AppendResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='instance_relation.AppendResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='instance_relation.AppendResponseWrapper.data', index=3,
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
  serialized_start=175,
  serialized_end=286,
)

_APPENDRESPONSEWRAPPER.fields_by_name['data'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
DESCRIPTOR.message_types_by_name['AppendRequest'] = _APPENDREQUEST
DESCRIPTOR.message_types_by_name['AppendResponseWrapper'] = _APPENDRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AppendRequest = _reflection.GeneratedProtocolMessageType('AppendRequest', (_message.Message,), {
  'DESCRIPTOR' : _APPENDREQUEST,
  '__module__' : 'append_pb2'
  # @@protoc_insertion_point(class_scope:instance_relation.AppendRequest)
  })
_sym_db.RegisterMessage(AppendRequest)

AppendResponseWrapper = _reflection.GeneratedProtocolMessageType('AppendResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _APPENDRESPONSEWRAPPER,
  '__module__' : 'append_pb2'
  # @@protoc_insertion_point(class_scope:instance_relation.AppendResponseWrapper)
  })
_sym_db.RegisterMessage(AppendResponseWrapper)


# @@protoc_insertion_point(module_scope)
