# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: update_issue_step.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from topboard_sdk.model.topboard import product_pb2 as topboard__sdk_dot_model_dot_topboard_dot_product__pb2
from topboard_sdk.model.topboard import sprint_pb2 as topboard__sdk_dot_model_dot_topboard_dot_sprint__pb2
from topboard_sdk.model.cmdb import user_pb2 as topboard__sdk_dot_model_dot_cmdb_dot_user__pb2
from topboard_sdk.model.topboard import attachment_pb2 as topboard__sdk_dot_model_dot_topboard_dot_attachment__pb2
from topboard_sdk.model.topboard import comment_pb2 as topboard__sdk_dot_model_dot_topboard_dot_comment__pb2
from topboard_sdk.model.topboard import issue_pb2 as topboard__sdk_dot_model_dot_topboard_dot_issue__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='update_issue_step.proto',
  package='topboard',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x17update_issue_step.proto\x12\x08topboard\x1a)topboard_sdk/model/topboard/product.proto\x1a(topboard_sdk/model/topboard/sprint.proto\x1a\"topboard_sdk/model/cmdb/user.proto\x1a,topboard_sdk/model/topboard/attachment.proto\x1a)topboard_sdk/model/topboard/comment.proto\x1a\'topboard_sdk/model/topboard/issue.proto\"\x88\x01\n\x16UpdateIssueStepRequest\x12\x0f\n\x07issueID\x18\x01 \x01(\t\x12\x33\n\x04step\x18\x02 \x01(\x0b\x32%.topboard.UpdateIssueStepRequest.Step\x1a(\n\x04Step\x12\x0c\n\x04step\x18\x01 \x01(\t\x12\x12\n\ninstanceId\x18\x02 \x01(\t\"q\n\x1eUpdateIssueStepResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x1d\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x0f.topboard.Issueb\x06proto3')
  ,
  dependencies=[topboard__sdk_dot_model_dot_topboard_dot_product__pb2.DESCRIPTOR,topboard__sdk_dot_model_dot_topboard_dot_sprint__pb2.DESCRIPTOR,topboard__sdk_dot_model_dot_cmdb_dot_user__pb2.DESCRIPTOR,topboard__sdk_dot_model_dot_topboard_dot_attachment__pb2.DESCRIPTOR,topboard__sdk_dot_model_dot_topboard_dot_comment__pb2.DESCRIPTOR,topboard__sdk_dot_model_dot_topboard_dot_issue__pb2.DESCRIPTOR,])




_UPDATEISSUESTEPREQUEST_STEP = _descriptor.Descriptor(
  name='Step',
  full_name='topboard.UpdateIssueStepRequest.Step',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='step', full_name='topboard.UpdateIssueStepRequest.Step.step', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='topboard.UpdateIssueStepRequest.Step.instanceId', index=1,
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
  serialized_start=385,
  serialized_end=425,
)

_UPDATEISSUESTEPREQUEST = _descriptor.Descriptor(
  name='UpdateIssueStepRequest',
  full_name='topboard.UpdateIssueStepRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='issueID', full_name='topboard.UpdateIssueStepRequest.issueID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='step', full_name='topboard.UpdateIssueStepRequest.step', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_UPDATEISSUESTEPREQUEST_STEP, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=289,
  serialized_end=425,
)


_UPDATEISSUESTEPRESPONSEWRAPPER = _descriptor.Descriptor(
  name='UpdateIssueStepResponseWrapper',
  full_name='topboard.UpdateIssueStepResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='topboard.UpdateIssueStepResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='topboard.UpdateIssueStepResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='topboard.UpdateIssueStepResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='topboard.UpdateIssueStepResponseWrapper.data', index=3,
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
  serialized_start=427,
  serialized_end=540,
)

_UPDATEISSUESTEPREQUEST_STEP.containing_type = _UPDATEISSUESTEPREQUEST
_UPDATEISSUESTEPREQUEST.fields_by_name['step'].message_type = _UPDATEISSUESTEPREQUEST_STEP
_UPDATEISSUESTEPRESPONSEWRAPPER.fields_by_name['data'].message_type = topboard__sdk_dot_model_dot_topboard_dot_issue__pb2._ISSUE
DESCRIPTOR.message_types_by_name['UpdateIssueStepRequest'] = _UPDATEISSUESTEPREQUEST
DESCRIPTOR.message_types_by_name['UpdateIssueStepResponseWrapper'] = _UPDATEISSUESTEPRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateIssueStepRequest = _reflection.GeneratedProtocolMessageType('UpdateIssueStepRequest', (_message.Message,), {

  'Step' : _reflection.GeneratedProtocolMessageType('Step', (_message.Message,), {
    'DESCRIPTOR' : _UPDATEISSUESTEPREQUEST_STEP,
    '__module__' : 'update_issue_step_pb2'
    # @@protoc_insertion_point(class_scope:topboard.UpdateIssueStepRequest.Step)
    })
  ,
  'DESCRIPTOR' : _UPDATEISSUESTEPREQUEST,
  '__module__' : 'update_issue_step_pb2'
  # @@protoc_insertion_point(class_scope:topboard.UpdateIssueStepRequest)
  })
_sym_db.RegisterMessage(UpdateIssueStepRequest)
_sym_db.RegisterMessage(UpdateIssueStepRequest.Step)

UpdateIssueStepResponseWrapper = _reflection.GeneratedProtocolMessageType('UpdateIssueStepResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEISSUESTEPRESPONSEWRAPPER,
  '__module__' : 'update_issue_step_pb2'
  # @@protoc_insertion_point(class_scope:topboard.UpdateIssueStepResponseWrapper)
  })
_sym_db.RegisterMessage(UpdateIssueStepResponseWrapper)


# @@protoc_insertion_point(module_scope)