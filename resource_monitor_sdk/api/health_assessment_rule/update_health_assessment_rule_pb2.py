# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: update_health_assessment_rule.proto

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
  name='update_health_assessment_rule.proto',
  package='health_assessment_rule',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n#update_health_assessment_rule.proto\x12\x16health_assessment_rule\x1a\\resource_monitor_sdk/model/health_assessment/health_assessment_event_score_config_item.proto\x1agresource_monitor_sdk/model/health_assessment/health_assessment_related_resource_score_config_item.proto\"\xc2\x02\n!UpdateHealthAssessmentRuleRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08objectId\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12Q\n\x10\x65ventScoreConfig\x18\x04 \x03(\x0b\x32\x37.health_assessment.HealthAssessmentEventScoreConfigItem\x12\x65\n\x1arelatedResourceScoreConfig\x18\x05 \x03(\x0b\x32\x41.health_assessment.HealthAssessmentRelatedResourceScoreConfigItem\x12\x18\n\x10\x65ventScoreWeight\x18\x06 \x01(\x05\x12\x1d\n\x15relatedResourceWeight\x18\x07 \x01(\x05\"0\n\"UpdateHealthAssessmentRuleResponse\x12\n\n\x02id\x18\x01 \x01(\t\"\xa7\x01\n)UpdateHealthAssessmentRuleResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12H\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32:.health_assessment_rule.UpdateHealthAssessmentRuleResponseb\x06proto3')
  ,
  dependencies=[resource__monitor__sdk_dot_model_dot_health__assessment_dot_health__assessment__event__score__config__item__pb2.DESCRIPTOR,resource__monitor__sdk_dot_model_dot_health__assessment_dot_health__assessment__related__resource__score__config__item__pb2.DESCRIPTOR,])




_UPDATEHEALTHASSESSMENTRULEREQUEST = _descriptor.Descriptor(
  name='UpdateHealthAssessmentRuleRequest',
  full_name='health_assessment_rule.UpdateHealthAssessmentRuleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='health_assessment_rule.UpdateHealthAssessmentRuleRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectId', full_name='health_assessment_rule.UpdateHealthAssessmentRuleRequest.objectId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='health_assessment_rule.UpdateHealthAssessmentRuleRequest.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eventScoreConfig', full_name='health_assessment_rule.UpdateHealthAssessmentRuleRequest.eventScoreConfig', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relatedResourceScoreConfig', full_name='health_assessment_rule.UpdateHealthAssessmentRuleRequest.relatedResourceScoreConfig', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eventScoreWeight', full_name='health_assessment_rule.UpdateHealthAssessmentRuleRequest.eventScoreWeight', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relatedResourceWeight', full_name='health_assessment_rule.UpdateHealthAssessmentRuleRequest.relatedResourceWeight', index=6,
      number=7, type=5, cpp_type=1, label=1,
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
  serialized_end=585,
)


_UPDATEHEALTHASSESSMENTRULERESPONSE = _descriptor.Descriptor(
  name='UpdateHealthAssessmentRuleResponse',
  full_name='health_assessment_rule.UpdateHealthAssessmentRuleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='health_assessment_rule.UpdateHealthAssessmentRuleResponse.id', index=0,
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
  serialized_start=587,
  serialized_end=635,
)


_UPDATEHEALTHASSESSMENTRULERESPONSEWRAPPER = _descriptor.Descriptor(
  name='UpdateHealthAssessmentRuleResponseWrapper',
  full_name='health_assessment_rule.UpdateHealthAssessmentRuleResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='health_assessment_rule.UpdateHealthAssessmentRuleResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='health_assessment_rule.UpdateHealthAssessmentRuleResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='health_assessment_rule.UpdateHealthAssessmentRuleResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='health_assessment_rule.UpdateHealthAssessmentRuleResponseWrapper.data', index=3,
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
  serialized_start=638,
  serialized_end=805,
)

_UPDATEHEALTHASSESSMENTRULEREQUEST.fields_by_name['eventScoreConfig'].message_type = resource__monitor__sdk_dot_model_dot_health__assessment_dot_health__assessment__event__score__config__item__pb2._HEALTHASSESSMENTEVENTSCORECONFIGITEM
_UPDATEHEALTHASSESSMENTRULEREQUEST.fields_by_name['relatedResourceScoreConfig'].message_type = resource__monitor__sdk_dot_model_dot_health__assessment_dot_health__assessment__related__resource__score__config__item__pb2._HEALTHASSESSMENTRELATEDRESOURCESCORECONFIGITEM
_UPDATEHEALTHASSESSMENTRULERESPONSEWRAPPER.fields_by_name['data'].message_type = _UPDATEHEALTHASSESSMENTRULERESPONSE
DESCRIPTOR.message_types_by_name['UpdateHealthAssessmentRuleRequest'] = _UPDATEHEALTHASSESSMENTRULEREQUEST
DESCRIPTOR.message_types_by_name['UpdateHealthAssessmentRuleResponse'] = _UPDATEHEALTHASSESSMENTRULERESPONSE
DESCRIPTOR.message_types_by_name['UpdateHealthAssessmentRuleResponseWrapper'] = _UPDATEHEALTHASSESSMENTRULERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateHealthAssessmentRuleRequest = _reflection.GeneratedProtocolMessageType('UpdateHealthAssessmentRuleRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEHEALTHASSESSMENTRULEREQUEST,
  '__module__' : 'update_health_assessment_rule_pb2'
  # @@protoc_insertion_point(class_scope:health_assessment_rule.UpdateHealthAssessmentRuleRequest)
  })
_sym_db.RegisterMessage(UpdateHealthAssessmentRuleRequest)

UpdateHealthAssessmentRuleResponse = _reflection.GeneratedProtocolMessageType('UpdateHealthAssessmentRuleResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEHEALTHASSESSMENTRULERESPONSE,
  '__module__' : 'update_health_assessment_rule_pb2'
  # @@protoc_insertion_point(class_scope:health_assessment_rule.UpdateHealthAssessmentRuleResponse)
  })
_sym_db.RegisterMessage(UpdateHealthAssessmentRuleResponse)

UpdateHealthAssessmentRuleResponseWrapper = _reflection.GeneratedProtocolMessageType('UpdateHealthAssessmentRuleResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEHEALTHASSESSMENTRULERESPONSEWRAPPER,
  '__module__' : 'update_health_assessment_rule_pb2'
  # @@protoc_insertion_point(class_scope:health_assessment_rule.UpdateHealthAssessmentRuleResponseWrapper)
  })
_sym_db.RegisterMessage(UpdateHealthAssessmentRuleResponseWrapper)


# @@protoc_insertion_point(module_scope)