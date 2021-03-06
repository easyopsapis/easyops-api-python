# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: create_health_assessment_rule.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from resource_monitor_sdk.model.health_assessment import health_assessment_event_score_config_item_pb2 as resource__monitor__sdk_dot_model_dot_health__assessment_dot_health__assessment__event__score__config__item__pb2
from resource_monitor_sdk.model.health_assessment import health_assessment_related_resource_score_config_item_pb2 as resource__monitor__sdk_dot_model_dot_health__assessment_dot_health__assessment__related__resource__score__config__item__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='create_health_assessment_rule.proto',
  package='health_assessment_rule',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n#create_health_assessment_rule.proto\x12\x16health_assessment_rule\x1a\\resource_monitor_sdk/model/health_assessment/health_assessment_event_score_config_item.proto\x1agresource_monitor_sdk/model/health_assessment/health_assessment_related_resource_score_config_item.proto\"\xb6\x02\n!CreateHealthAssessmentRuleRequest\x12\x10\n\x08objectId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12Q\n\x10\x65ventScoreConfig\x18\x03 \x03(\x0b\x32\x37.health_assessment.HealthAssessmentEventScoreConfigItem\x12\x65\n\x1arelatedResourceScoreConfig\x18\x04 \x03(\x0b\x32\x41.health_assessment.HealthAssessmentRelatedResourceScoreConfigItem\x12\x18\n\x10\x65ventScoreWeight\x18\x05 \x01(\x05\x12\x1d\n\x15relatedResourceWeight\x18\x06 \x01(\x05\"0\n\"CreateHealthAssessmentRuleResponse\x12\n\n\x02id\x18\x01 \x01(\t\"\xa7\x01\n)CreateHealthAssessmentRuleResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12H\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32:.health_assessment_rule.CreateHealthAssessmentRuleResponseb\x06proto3')
  ,
  dependencies=[resource__monitor__sdk_dot_model_dot_health__assessment_dot_health__assessment__event__score__config__item__pb2.DESCRIPTOR,resource__monitor__sdk_dot_model_dot_health__assessment_dot_health__assessment__related__resource__score__config__item__pb2.DESCRIPTOR,])




_CREATEHEALTHASSESSMENTRULEREQUEST = _descriptor.Descriptor(
  name='CreateHealthAssessmentRuleRequest',
  full_name='health_assessment_rule.CreateHealthAssessmentRuleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='objectId', full_name='health_assessment_rule.CreateHealthAssessmentRuleRequest.objectId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='health_assessment_rule.CreateHealthAssessmentRuleRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eventScoreConfig', full_name='health_assessment_rule.CreateHealthAssessmentRuleRequest.eventScoreConfig', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relatedResourceScoreConfig', full_name='health_assessment_rule.CreateHealthAssessmentRuleRequest.relatedResourceScoreConfig', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eventScoreWeight', full_name='health_assessment_rule.CreateHealthAssessmentRuleRequest.eventScoreWeight', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relatedResourceWeight', full_name='health_assessment_rule.CreateHealthAssessmentRuleRequest.relatedResourceWeight', index=5,
      number=6, type=5, cpp_type=1, label=1,
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
  serialized_start=263,
  serialized_end=573,
)


_CREATEHEALTHASSESSMENTRULERESPONSE = _descriptor.Descriptor(
  name='CreateHealthAssessmentRuleResponse',
  full_name='health_assessment_rule.CreateHealthAssessmentRuleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='health_assessment_rule.CreateHealthAssessmentRuleResponse.id', index=0,
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
  serialized_start=575,
  serialized_end=623,
)


_CREATEHEALTHASSESSMENTRULERESPONSEWRAPPER = _descriptor.Descriptor(
  name='CreateHealthAssessmentRuleResponseWrapper',
  full_name='health_assessment_rule.CreateHealthAssessmentRuleResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='health_assessment_rule.CreateHealthAssessmentRuleResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='health_assessment_rule.CreateHealthAssessmentRuleResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='health_assessment_rule.CreateHealthAssessmentRuleResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='health_assessment_rule.CreateHealthAssessmentRuleResponseWrapper.data', index=3,
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
  serialized_start=626,
  serialized_end=793,
)

_CREATEHEALTHASSESSMENTRULEREQUEST.fields_by_name['eventScoreConfig'].message_type = resource__monitor__sdk_dot_model_dot_health__assessment_dot_health__assessment__event__score__config__item__pb2._HEALTHASSESSMENTEVENTSCORECONFIGITEM
_CREATEHEALTHASSESSMENTRULEREQUEST.fields_by_name['relatedResourceScoreConfig'].message_type = resource__monitor__sdk_dot_model_dot_health__assessment_dot_health__assessment__related__resource__score__config__item__pb2._HEALTHASSESSMENTRELATEDRESOURCESCORECONFIGITEM
_CREATEHEALTHASSESSMENTRULERESPONSEWRAPPER.fields_by_name['data'].message_type = _CREATEHEALTHASSESSMENTRULERESPONSE
DESCRIPTOR.message_types_by_name['CreateHealthAssessmentRuleRequest'] = _CREATEHEALTHASSESSMENTRULEREQUEST
DESCRIPTOR.message_types_by_name['CreateHealthAssessmentRuleResponse'] = _CREATEHEALTHASSESSMENTRULERESPONSE
DESCRIPTOR.message_types_by_name['CreateHealthAssessmentRuleResponseWrapper'] = _CREATEHEALTHASSESSMENTRULERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateHealthAssessmentRuleRequest = _reflection.GeneratedProtocolMessageType('CreateHealthAssessmentRuleRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEHEALTHASSESSMENTRULEREQUEST,
  '__module__' : 'create_health_assessment_rule_pb2'
  # @@protoc_insertion_point(class_scope:health_assessment_rule.CreateHealthAssessmentRuleRequest)
  })
_sym_db.RegisterMessage(CreateHealthAssessmentRuleRequest)

CreateHealthAssessmentRuleResponse = _reflection.GeneratedProtocolMessageType('CreateHealthAssessmentRuleResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEHEALTHASSESSMENTRULERESPONSE,
  '__module__' : 'create_health_assessment_rule_pb2'
  # @@protoc_insertion_point(class_scope:health_assessment_rule.CreateHealthAssessmentRuleResponse)
  })
_sym_db.RegisterMessage(CreateHealthAssessmentRuleResponse)

CreateHealthAssessmentRuleResponseWrapper = _reflection.GeneratedProtocolMessageType('CreateHealthAssessmentRuleResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _CREATEHEALTHASSESSMENTRULERESPONSEWRAPPER,
  '__module__' : 'create_health_assessment_rule_pb2'
  # @@protoc_insertion_point(class_scope:health_assessment_rule.CreateHealthAssessmentRuleResponseWrapper)
  })
_sym_db.RegisterMessage(CreateHealthAssessmentRuleResponseWrapper)


# @@protoc_insertion_point(module_scope)
