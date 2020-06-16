# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: comment.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from msgsender_sdk.model.topboard import issue_basic_pb2 as msgsender__sdk_dot_model_dot_topboard_dot_issue__basic__pb2
from msgsender_sdk.model.cmdb import user_pb2 as msgsender__sdk_dot_model_dot_cmdb_dot_user__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='comment.proto',
  package='topboard',
  syntax='proto3',
  serialized_options=_b('ZBgo.easyops.local/contracts/protorepo-models/easyops/model/topboard'),
  serialized_pb=_b('\n\rcomment.proto\x12\x08topboard\x1a.msgsender_sdk/model/topboard/issue_basic.proto\x1a#msgsender_sdk/model/cmdb/user.proto\"\x9b\x01\n\x07\x43omment\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ninstanceId\x18\x02 \x01(\t\x12#\n\x05issue\x18\x03 \x03(\x0b\x32\x14.topboard.IssueBasic\x12\r\n\x05\x63time\x18\x04 \x01(\t\x12\x0c\n\x04\x62ody\x18\x05 \x01(\t\x12\x10\n\x08parentId\x18\x06 \x01(\t\x12\x1a\n\x06\x61uthor\x18\x07 \x03(\x0b\x32\n.cmdb.UserBDZBgo.easyops.local/contracts/protorepo-models/easyops/model/topboardb\x06proto3')
  ,
  dependencies=[msgsender__sdk_dot_model_dot_topboard_dot_issue__basic__pb2.DESCRIPTOR,msgsender__sdk_dot_model_dot_cmdb_dot_user__pb2.DESCRIPTOR,])




_COMMENT = _descriptor.Descriptor(
  name='Comment',
  full_name='topboard.Comment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='topboard.Comment.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='topboard.Comment.instanceId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='issue', full_name='topboard.Comment.issue', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='topboard.Comment.ctime', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='body', full_name='topboard.Comment.body', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parentId', full_name='topboard.Comment.parentId', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='author', full_name='topboard.Comment.author', index=6,
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
  serialized_start=113,
  serialized_end=268,
)

_COMMENT.fields_by_name['issue'].message_type = msgsender__sdk_dot_model_dot_topboard_dot_issue__basic__pb2._ISSUEBASIC
_COMMENT.fields_by_name['author'].message_type = msgsender__sdk_dot_model_dot_cmdb_dot_user__pb2._USER
DESCRIPTOR.message_types_by_name['Comment'] = _COMMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Comment = _reflection.GeneratedProtocolMessageType('Comment', (_message.Message,), {
  'DESCRIPTOR' : _COMMENT,
  '__module__' : 'comment_pb2'
  # @@protoc_insertion_point(class_scope:topboard.Comment)
  })
_sym_db.RegisterMessage(Comment)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
