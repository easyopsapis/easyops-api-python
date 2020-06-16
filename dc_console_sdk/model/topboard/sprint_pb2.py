# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sprint.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from dc_console_sdk.model.topboard import product_basic_pb2 as dc__console__sdk_dot_model_dot_topboard_dot_product__basic__pb2
from dc_console_sdk.model.topboard import issue_basic_pb2 as dc__console__sdk_dot_model_dot_topboard_dot_issue__basic__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sprint.proto',
  package='topboard',
  syntax='proto3',
  serialized_options=_b('ZBgo.easyops.local/contracts/protorepo-models/easyops/model/topboard'),
  serialized_pb=_b('\n\x0csprint.proto\x12\x08topboard\x1a\x31\x64\x63_console_sdk/model/topboard/product_basic.proto\x1a/dc_console_sdk/model/topboard/issue_basic.proto\"\xca\x01\n\x06Sprint\x12\'\n\x07product\x18\x01 \x03(\x0b\x32\x16.topboard.ProductBasic\x12$\n\x06issues\x18\x02 \x03(\x0b\x32\x14.topboard.IssueBasic\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x12\n\ninstanceId\x18\x04 \x01(\t\x12\r\n\x05title\x18\x05 \x01(\t\x12\x0e\n\x06status\x18\x06 \x01(\t\x12\x0c\n\x04goal\x18\x07 \x01(\t\x12\x11\n\tstartTime\x18\x08 \x01(\t\x12\x0f\n\x07\x65ndTime\x18\t \x01(\tBDZBgo.easyops.local/contracts/protorepo-models/easyops/model/topboardb\x06proto3')
  ,
  dependencies=[dc__console__sdk_dot_model_dot_topboard_dot_product__basic__pb2.DESCRIPTOR,dc__console__sdk_dot_model_dot_topboard_dot_issue__basic__pb2.DESCRIPTOR,])




_SPRINT = _descriptor.Descriptor(
  name='Sprint',
  full_name='topboard.Sprint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='product', full_name='topboard.Sprint.product', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='issues', full_name='topboard.Sprint.issues', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='topboard.Sprint.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='topboard.Sprint.instanceId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='topboard.Sprint.title', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='topboard.Sprint.status', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='goal', full_name='topboard.Sprint.goal', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='topboard.Sprint.startTime', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endTime', full_name='topboard.Sprint.endTime', index=8,
      number=9, type=9, cpp_type=9, label=1,
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
  serialized_start=127,
  serialized_end=329,
)

_SPRINT.fields_by_name['product'].message_type = dc__console__sdk_dot_model_dot_topboard_dot_product__basic__pb2._PRODUCTBASIC
_SPRINT.fields_by_name['issues'].message_type = dc__console__sdk_dot_model_dot_topboard_dot_issue__basic__pb2._ISSUEBASIC
DESCRIPTOR.message_types_by_name['Sprint'] = _SPRINT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Sprint = _reflection.GeneratedProtocolMessageType('Sprint', (_message.Message,), {
  'DESCRIPTOR' : _SPRINT,
  '__module__' : 'sprint_pb2'
  # @@protoc_insertion_point(class_scope:topboard.Sprint)
  })
_sym_db.RegisterMessage(Sprint)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
