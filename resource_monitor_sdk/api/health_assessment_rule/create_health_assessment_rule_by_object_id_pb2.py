# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: create_health_assessment_rule_by_object_id.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='create_health_assessment_rule_by_object_id.proto',
  package='health_assessment_rule',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n0create_health_assessment_rule_by_object_id.proto\x12\x16health_assessment_rule\"?\n+CreateHealthAssessmentRuleByObjectIdRequest\x12\x10\n\x08objectId\x18\x01 \x01(\t\":\n,CreateHealthAssessmentRuleByObjectIdResponse\x12\n\n\x02id\x18\x01 \x01(\t\"\xbb\x01\n3CreateHealthAssessmentRuleByObjectIdResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12R\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x44.health_assessment_rule.CreateHealthAssessmentRuleByObjectIdResponseb\x06proto3')
)




_CREATEHEALTHASSESSMENTRULEBYOBJECTIDREQUEST = _descriptor.Descriptor(
  name='CreateHealthAssessmentRuleByObjectIdRequest',
  full_name='health_assessment_rule.CreateHealthAssessmentRuleByObjectIdRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='objectId', full_name='health_assessment_rule.CreateHealthAssessmentRuleByObjectIdRequest.objectId', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=76,
  serialized_end=139,
)


_CREATEHEALTHASSESSMENTRULEBYOBJECTIDRESPONSE = _descriptor.Descriptor(
  name='CreateHealthAssessmentRuleByObjectIdResponse',
  full_name='health_assessment_rule.CreateHealthAssessmentRuleByObjectIdResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='health_assessment_rule.CreateHealthAssessmentRuleByObjectIdResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=141,
  serialized_end=199,
)


_CREATEHEALTHASSESSMENTRULEBYOBJECTIDRESPONSEWRAPPER = _descriptor.Descriptor(
  name='CreateHealthAssessmentRuleByObjectIdResponseWrapper',
  full_name='health_assessment_rule.CreateHealthAssessmentRuleByObjectIdResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='health_assessment_rule.CreateHealthAssessmentRuleByObjectIdResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='health_assessment_rule.CreateHealthAssessmentRuleByObjectIdResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='health_assessment_rule.CreateHealthAssessmentRuleByObjectIdResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='health_assessment_rule.CreateHealthAssessmentRuleByObjectIdResponseWrapper.data', index=3,
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
  serialized_start=202,
  serialized_end=389,
)

_CREATEHEALTHASSESSMENTRULEBYOBJECTIDRESPONSEWRAPPER.fields_by_name['data'].message_type = _CREATEHEALTHASSESSMENTRULEBYOBJECTIDRESPONSE
DESCRIPTOR.message_types_by_name['CreateHealthAssessmentRuleByObjectIdRequest'] = _CREATEHEALTHASSESSMENTRULEBYOBJECTIDREQUEST
DESCRIPTOR.message_types_by_name['CreateHealthAssessmentRuleByObjectIdResponse'] = _CREATEHEALTHASSESSMENTRULEBYOBJECTIDRESPONSE
DESCRIPTOR.message_types_by_name['CreateHealthAssessmentRuleByObjectIdResponseWrapper'] = _CREATEHEALTHASSESSMENTRULEBYOBJECTIDRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateHealthAssessmentRuleByObjectIdRequest = _reflection.GeneratedProtocolMessageType('CreateHealthAssessmentRuleByObjectIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEHEALTHASSESSMENTRULEBYOBJECTIDREQUEST,
  '__module__' : 'create_health_assessment_rule_by_object_id_pb2'
  # @@protoc_insertion_point(class_scope:health_assessment_rule.CreateHealthAssessmentRuleByObjectIdRequest)
  })
_sym_db.RegisterMessage(CreateHealthAssessmentRuleByObjectIdRequest)

CreateHealthAssessmentRuleByObjectIdResponse = _reflection.GeneratedProtocolMessageType('CreateHealthAssessmentRuleByObjectIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEHEALTHASSESSMENTRULEBYOBJECTIDRESPONSE,
  '__module__' : 'create_health_assessment_rule_by_object_id_pb2'
  # @@protoc_insertion_point(class_scope:health_assessment_rule.CreateHealthAssessmentRuleByObjectIdResponse)
  })
_sym_db.RegisterMessage(CreateHealthAssessmentRuleByObjectIdResponse)

CreateHealthAssessmentRuleByObjectIdResponseWrapper = _reflection.GeneratedProtocolMessageType('CreateHealthAssessmentRuleByObjectIdResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _CREATEHEALTHASSESSMENTRULEBYOBJECTIDRESPONSEWRAPPER,
  '__module__' : 'create_health_assessment_rule_by_object_id_pb2'
  # @@protoc_insertion_point(class_scope:health_assessment_rule.CreateHealthAssessmentRuleByObjectIdResponseWrapper)
  })
_sym_db.RegisterMessage(CreateHealthAssessmentRuleByObjectIdResponseWrapper)


# @@protoc_insertion_point(module_scope)
