# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: attachment.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from easy_work_service_sdk.model.topboard import issue_basic_pb2 as easy__work__service__sdk_dot_model_dot_topboard_dot_issue__basic__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='attachment.proto',
  package='topboard',
  syntax='proto3',
  serialized_options=_b('ZBgo.easyops.local/contracts/protorepo-models/easyops/model/topboard'),
  serialized_pb=_b('\n\x10\x61ttachment.proto\x12\x08topboard\x1a\x36\x65\x61sy_work_service_sdk/model/topboard/issue_basic.proto\"\x98\x01\n\nAttachment\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ninstanceId\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x10\n\x08\x66ilename\x18\x04 \x01(\t\x12\x0c\n\x04size\x18\x05 \x01(\t\x12\x15\n\rfileToConvert\x18\x06 \x01(\t\x12#\n\x05issue\x18\x07 \x03(\x0b\x32\x14.topboard.IssueBasicBDZBgo.easyops.local/contracts/protorepo-models/easyops/model/topboardb\x06proto3')
  ,
  dependencies=[easy__work__service__sdk_dot_model_dot_topboard_dot_issue__basic__pb2.DESCRIPTOR,])




_ATTACHMENT = _descriptor.Descriptor(
  name='Attachment',
  full_name='topboard.Attachment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='topboard.Attachment.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='topboard.Attachment.instanceId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='topboard.Attachment.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filename', full_name='topboard.Attachment.filename', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='topboard.Attachment.size', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fileToConvert', full_name='topboard.Attachment.fileToConvert', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='issue', full_name='topboard.Attachment.issue', index=6,
      number=7, type=11, cpp_type=10, label=3,
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
  serialized_start=87,
  serialized_end=239,
)

_ATTACHMENT.fields_by_name['issue'].message_type = easy__work__service__sdk_dot_model_dot_topboard_dot_issue__basic__pb2._ISSUEBASIC
DESCRIPTOR.message_types_by_name['Attachment'] = _ATTACHMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Attachment = _reflection.GeneratedProtocolMessageType('Attachment', (_message.Message,), {
  'DESCRIPTOR' : _ATTACHMENT,
  '__module__' : 'attachment_pb2'
  # @@protoc_insertion_point(class_scope:topboard.Attachment)
  })
_sym_db.RegisterMessage(Attachment)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
