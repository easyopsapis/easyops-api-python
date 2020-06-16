# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sprint_basic.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sprint_basic.proto',
  package='topboard',
  syntax='proto3',
  serialized_options=_b('ZBgo.easyops.local/contracts/protorepo-models/easyops/model/topboard'),
  serialized_pb=_b('\n\x12sprint_basic.proto\x12\x08topboard\"\x80\x01\n\x0bSprintBasic\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ninstanceId\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\x0e\n\x06status\x18\x04 \x01(\t\x12\x0c\n\x04goal\x18\x05 \x01(\t\x12\x11\n\tstartTime\x18\x06 \x01(\t\x12\x0f\n\x07\x65ndTime\x18\x07 \x01(\tBDZBgo.easyops.local/contracts/protorepo-models/easyops/model/topboardb\x06proto3')
)




_SPRINTBASIC = _descriptor.Descriptor(
  name='SprintBasic',
  full_name='topboard.SprintBasic',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='topboard.SprintBasic.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='topboard.SprintBasic.instanceId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='topboard.SprintBasic.title', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='topboard.SprintBasic.status', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='goal', full_name='topboard.SprintBasic.goal', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='topboard.SprintBasic.startTime', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endTime', full_name='topboard.SprintBasic.endTime', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=33,
  serialized_end=161,
)

DESCRIPTOR.message_types_by_name['SprintBasic'] = _SPRINTBASIC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SprintBasic = _reflection.GeneratedProtocolMessageType('SprintBasic', (_message.Message,), {
  'DESCRIPTOR' : _SPRINTBASIC,
  '__module__' : 'sprint_basic_pb2'
  # @@protoc_insertion_point(class_scope:topboard.SprintBasic)
  })
_sym_db.RegisterMessage(SprintBasic)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
