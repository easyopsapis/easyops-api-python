# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: issue.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from scheduler_sdk.model.topboard import product_pb2 as scheduler__sdk_dot_model_dot_topboard_dot_product__pb2
from scheduler_sdk.model.topboard import sprint_pb2 as scheduler__sdk_dot_model_dot_topboard_dot_sprint__pb2
from scheduler_sdk.model.cmdb import user_pb2 as scheduler__sdk_dot_model_dot_cmdb_dot_user__pb2
from scheduler_sdk.model.topboard import attachment_pb2 as scheduler__sdk_dot_model_dot_topboard_dot_attachment__pb2
from scheduler_sdk.model.topboard import comment_pb2 as scheduler__sdk_dot_model_dot_topboard_dot_comment__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='issue.proto',
  package='topboard',
  syntax='proto3',
  serialized_options=_b('ZBgo.easyops.local/contracts/protorepo-models/easyops/model/topboard'),
  serialized_pb=_b('\n\x0bissue.proto\x12\x08topboard\x1a*scheduler_sdk/model/topboard/product.proto\x1a)scheduler_sdk/model/topboard/sprint.proto\x1a#scheduler_sdk/model/cmdb/user.proto\x1a-scheduler_sdk/model/topboard/attachment.proto\x1a*scheduler_sdk/model/topboard/comment.proto\"\xc4\x06\n\x05Issue\x12\x1f\n\x06parent\x18\x01 \x03(\x0b\x32\x0f.topboard.Issue\x12!\n\x08subtasks\x18\x02 \x03(\x0b\x32\x0f.topboard.Issue\x12\"\n\x07product\x18\x03 \x03(\x0b\x32\x11.topboard.Product\x12 \n\x06sprint\x18\x04 \x03(\x0b\x32\x10.topboard.Sprint\x12\x1f\n\x0bsubscribers\x18\x05 \x03(\x0b\x32\n.cmdb.User\x12\x1c\n\x08\x61ssignee\x18\x06 \x03(\x0b\x32\n.cmdb.User\x12\x1c\n\x08reporter\x18\x07 \x03(\x0b\x32\n.cmdb.User\x12)\n\x0b\x61ttachments\x18\x08 \x03(\x0b\x32\x14.topboard.Attachment\x12#\n\x08\x63omments\x18\t \x03(\x0b\x32\x11.topboard.Comment\x12,\n\tissueFrom\x18\n \x03(\x0b\x32\x19.topboard.Issue.IssueFrom\x12\x1a\n\x06tester\x18\x0b \x03(\x0b\x32\n.cmdb.User\x12\x0c\n\x04name\x18\x0c \x01(\t\x12\x12\n\ninstanceId\x18\r \x01(\t\x12\x0f\n\x07\x63reator\x18\x0e \x01(\t\x12\r\n\x05\x63time\x18\x0f \x01(\t\x12\r\n\x05title\x18\x10 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x11 \x01(\t\x12\x10\n\x08priority\x18\x12 \x01(\t\x12\x0c\n\x04type\x18\x13 \x01(\t\x12\x0c\n\x04step\x18\x14 \x01(\t\x12$\n\x05links\x18\x15 \x03(\x0b\x32\x15.topboard.Issue.Links\x12\x12\n\nstoryPoint\x18\x16 \x01(\t\x12\x12\n\nresolution\x18\x17 \x01(\t\x12\x0e\n\x06status\x18\x18 \x01(\t\x12&\n\x06images\x18\x19 \x03(\x0b\x32\x16.topboard.Issue.Images\x12\x0f\n\x07\x62ugType\x18\x1a \x01(\t\x12\x16\n\x0eresponsibility\x18\x1b \x01(\t\x1a-\n\tIssueFrom\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ninstanceId\x18\x02 \x01(\t\x1a#\n\x05Links\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x1a#\n\x06Images\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\tBDZBgo.easyops.local/contracts/protorepo-models/easyops/model/topboardb\x06proto3')
  ,
  dependencies=[scheduler__sdk_dot_model_dot_topboard_dot_product__pb2.DESCRIPTOR,scheduler__sdk_dot_model_dot_topboard_dot_sprint__pb2.DESCRIPTOR,scheduler__sdk_dot_model_dot_cmdb_dot_user__pb2.DESCRIPTOR,scheduler__sdk_dot_model_dot_topboard_dot_attachment__pb2.DESCRIPTOR,scheduler__sdk_dot_model_dot_topboard_dot_comment__pb2.DESCRIPTOR,])




_ISSUE_ISSUEFROM = _descriptor.Descriptor(
  name='IssueFrom',
  full_name='topboard.Issue.IssueFrom',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='topboard.Issue.IssueFrom.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='topboard.Issue.IssueFrom.instanceId', index=1,
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
  serialized_start=958,
  serialized_end=1003,
)

_ISSUE_LINKS = _descriptor.Descriptor(
  name='Links',
  full_name='topboard.Issue.Links',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='topboard.Issue.Links.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='topboard.Issue.Links.url', index=1,
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
  serialized_start=1005,
  serialized_end=1040,
)

_ISSUE_IMAGES = _descriptor.Descriptor(
  name='Images',
  full_name='topboard.Issue.Images',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='topboard.Issue.Images.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='topboard.Issue.Images.url', index=1,
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
  serialized_start=1042,
  serialized_end=1077,
)

_ISSUE = _descriptor.Descriptor(
  name='Issue',
  full_name='topboard.Issue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='topboard.Issue.parent', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subtasks', full_name='topboard.Issue.subtasks', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='product', full_name='topboard.Issue.product', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sprint', full_name='topboard.Issue.sprint', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subscribers', full_name='topboard.Issue.subscribers', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='assignee', full_name='topboard.Issue.assignee', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reporter', full_name='topboard.Issue.reporter', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attachments', full_name='topboard.Issue.attachments', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comments', full_name='topboard.Issue.comments', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='issueFrom', full_name='topboard.Issue.issueFrom', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tester', full_name='topboard.Issue.tester', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='topboard.Issue.name', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='topboard.Issue.instanceId', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='topboard.Issue.creator', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='topboard.Issue.ctime', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='topboard.Issue.title', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='topboard.Issue.description', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='priority', full_name='topboard.Issue.priority', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='topboard.Issue.type', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='step', full_name='topboard.Issue.step', index=19,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='links', full_name='topboard.Issue.links', index=20,
      number=21, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='storyPoint', full_name='topboard.Issue.storyPoint', index=21,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resolution', full_name='topboard.Issue.resolution', index=22,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='topboard.Issue.status', index=23,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='images', full_name='topboard.Issue.images', index=24,
      number=25, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bugType', full_name='topboard.Issue.bugType', index=25,
      number=26, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='responsibility', full_name='topboard.Issue.responsibility', index=26,
      number=27, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ISSUE_ISSUEFROM, _ISSUE_LINKS, _ISSUE_IMAGES, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=241,
  serialized_end=1077,
)

_ISSUE_ISSUEFROM.containing_type = _ISSUE
_ISSUE_LINKS.containing_type = _ISSUE
_ISSUE_IMAGES.containing_type = _ISSUE
_ISSUE.fields_by_name['parent'].message_type = _ISSUE
_ISSUE.fields_by_name['subtasks'].message_type = _ISSUE
_ISSUE.fields_by_name['product'].message_type = scheduler__sdk_dot_model_dot_topboard_dot_product__pb2._PRODUCT
_ISSUE.fields_by_name['sprint'].message_type = scheduler__sdk_dot_model_dot_topboard_dot_sprint__pb2._SPRINT
_ISSUE.fields_by_name['subscribers'].message_type = scheduler__sdk_dot_model_dot_cmdb_dot_user__pb2._USER
_ISSUE.fields_by_name['assignee'].message_type = scheduler__sdk_dot_model_dot_cmdb_dot_user__pb2._USER
_ISSUE.fields_by_name['reporter'].message_type = scheduler__sdk_dot_model_dot_cmdb_dot_user__pb2._USER
_ISSUE.fields_by_name['attachments'].message_type = scheduler__sdk_dot_model_dot_topboard_dot_attachment__pb2._ATTACHMENT
_ISSUE.fields_by_name['comments'].message_type = scheduler__sdk_dot_model_dot_topboard_dot_comment__pb2._COMMENT
_ISSUE.fields_by_name['issueFrom'].message_type = _ISSUE_ISSUEFROM
_ISSUE.fields_by_name['tester'].message_type = scheduler__sdk_dot_model_dot_cmdb_dot_user__pb2._USER
_ISSUE.fields_by_name['links'].message_type = _ISSUE_LINKS
_ISSUE.fields_by_name['images'].message_type = _ISSUE_IMAGES
DESCRIPTOR.message_types_by_name['Issue'] = _ISSUE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Issue = _reflection.GeneratedProtocolMessageType('Issue', (_message.Message,), {

  'IssueFrom' : _reflection.GeneratedProtocolMessageType('IssueFrom', (_message.Message,), {
    'DESCRIPTOR' : _ISSUE_ISSUEFROM,
    '__module__' : 'issue_pb2'
    # @@protoc_insertion_point(class_scope:topboard.Issue.IssueFrom)
    })
  ,

  'Links' : _reflection.GeneratedProtocolMessageType('Links', (_message.Message,), {
    'DESCRIPTOR' : _ISSUE_LINKS,
    '__module__' : 'issue_pb2'
    # @@protoc_insertion_point(class_scope:topboard.Issue.Links)
    })
  ,

  'Images' : _reflection.GeneratedProtocolMessageType('Images', (_message.Message,), {
    'DESCRIPTOR' : _ISSUE_IMAGES,
    '__module__' : 'issue_pb2'
    # @@protoc_insertion_point(class_scope:topboard.Issue.Images)
    })
  ,
  'DESCRIPTOR' : _ISSUE,
  '__module__' : 'issue_pb2'
  # @@protoc_insertion_point(class_scope:topboard.Issue)
  })
_sym_db.RegisterMessage(Issue)
_sym_db.RegisterMessage(Issue.IssueFrom)
_sym_db.RegisterMessage(Issue.Links)
_sym_db.RegisterMessage(Issue.Images)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
