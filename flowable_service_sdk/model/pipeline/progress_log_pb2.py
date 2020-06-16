# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: progress_log.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='progress_log.proto',
  package='pipeline',
  syntax='proto3',
  serialized_options=_b('ZBgo.easyops.local/contracts/protorepo-models/easyops/model/pipeline'),
  serialized_pb=_b('\n\x12progress_log.proto\x12\x08pipeline\"8\n\x0bProgressLog\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07metrics\x18\x02 \x01(\t\x12\x0c\n\x04logs\x18\x03 \x03(\tBDZBgo.easyops.local/contracts/protorepo-models/easyops/model/pipelineb\x06proto3')
)




_PROGRESSLOG = _descriptor.Descriptor(
  name='ProgressLog',
  full_name='pipeline.ProgressLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='pipeline.ProgressLog.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metrics', full_name='pipeline.ProgressLog.metrics', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logs', full_name='pipeline.ProgressLog.logs', index=2,
      number=3, type=9, cpp_type=9, label=3,
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
  serialized_start=32,
  serialized_end=88,
)

DESCRIPTOR.message_types_by_name['ProgressLog'] = _PROGRESSLOG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProgressLog = _reflection.GeneratedProtocolMessageType('ProgressLog', (_message.Message,), {
  'DESCRIPTOR' : _PROGRESSLOG,
  '__module__' : 'progress_log_pb2'
  # @@protoc_insertion_point(class_scope:pipeline.ProgressLog)
  })
_sym_db.RegisterMessage(ProgressLog)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
