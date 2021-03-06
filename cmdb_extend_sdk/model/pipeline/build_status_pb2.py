# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: build_status.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='build_status.proto',
  package='pipeline',
  syntax='proto3',
  serialized_options=_b('ZBgo.easyops.local/contracts/protorepo-models/easyops/model/pipeline'),
  serialized_pb=_b('\n\x12\x62uild_status.proto\x12\x08pipeline\"b\n\x0b\x42uildStatus\x12\r\n\x05state\x18\x01 \x01(\t\x12\x10\n\x08nodeName\x18\x02 \x01(\t\x12\x0f\n\x07started\x18\x03 \x01(\x05\x12\x0f\n\x07updated\x18\x04 \x01(\x05\x12\x10\n\x08\x66inished\x18\x05 \x01(\x05\x42\x44ZBgo.easyops.local/contracts/protorepo-models/easyops/model/pipelineb\x06proto3')
)




_BUILDSTATUS = _descriptor.Descriptor(
  name='BuildStatus',
  full_name='pipeline.BuildStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='pipeline.BuildStatus.state', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nodeName', full_name='pipeline.BuildStatus.nodeName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='started', full_name='pipeline.BuildStatus.started', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated', full_name='pipeline.BuildStatus.updated', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='finished', full_name='pipeline.BuildStatus.finished', index=4,
      number=5, type=5, cpp_type=1, label=1,
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
  serialized_start=32,
  serialized_end=130,
)

DESCRIPTOR.message_types_by_name['BuildStatus'] = _BUILDSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BuildStatus = _reflection.GeneratedProtocolMessageType('BuildStatus', (_message.Message,), {
  'DESCRIPTOR' : _BUILDSTATUS,
  '__module__' : 'build_status_pb2'
  # @@protoc_insertion_point(class_scope:pipeline.BuildStatus)
  })
_sym_db.RegisterMessage(BuildStatus)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
