# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: health_assessment_rule_version.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from idcmanager_sdk.model.health_assessment import health_assessment_event_score_config_item_pb2 as idcmanager__sdk_dot_model_dot_health__assessment_dot_health__assessment__event__score__config__item__pb2
from idcmanager_sdk.model.health_assessment import health_assessment_related_resource_score_config_item_pb2 as idcmanager__sdk_dot_model_dot_health__assessment_dot_health__assessment__related__resource__score__config__item__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='health_assessment_rule_version.proto',
  package='health_assessment',
  syntax='proto3',
  serialized_options=_b('ZKgo.easyops.local/contracts/protorepo-models/easyops/model/health_assessment'),
  serialized_pb=_b('\n$health_assessment_rule_version.proto\x12\x11health_assessment\x1aVidcmanager_sdk/model/health_assessment/health_assessment_event_score_config_item.proto\x1a\x61idcmanager_sdk/model/health_assessment/health_assessment_related_resource_score_config_item.proto\"\xc6\x02\n\x1bHealthAssessmentRuleVersion\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0e\n\x06ruleId\x18\x02 \x01(\t\x12\x10\n\x08objectId\x18\x03 \x01(\t\x12Q\n\x10\x65ventScoreConfig\x18\x04 \x03(\x0b\x32\x37.health_assessment.HealthAssessmentEventScoreConfigItem\x12\x65\n\x1arelatedResourceScoreConfig\x18\x05 \x03(\x0b\x32\x41.health_assessment.HealthAssessmentRelatedResourceScoreConfigItem\x12\x18\n\x10\x65ventScoreWeight\x18\x06 \x01(\x05\x12\x1d\n\x15relatedResourceWeight\x18\x07 \x01(\x05\x42MZKgo.easyops.local/contracts/protorepo-models/easyops/model/health_assessmentb\x06proto3')
  ,
  dependencies=[idcmanager__sdk_dot_model_dot_health__assessment_dot_health__assessment__event__score__config__item__pb2.DESCRIPTOR,idcmanager__sdk_dot_model_dot_health__assessment_dot_health__assessment__related__resource__score__config__item__pb2.DESCRIPTOR,])




_HEALTHASSESSMENTRULEVERSION = _descriptor.Descriptor(
  name='HealthAssessmentRuleVersion',
  full_name='health_assessment.HealthAssessmentRuleVersion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='health_assessment.HealthAssessmentRuleVersion.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ruleId', full_name='health_assessment.HealthAssessmentRuleVersion.ruleId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectId', full_name='health_assessment.HealthAssessmentRuleVersion.objectId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eventScoreConfig', full_name='health_assessment.HealthAssessmentRuleVersion.eventScoreConfig', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relatedResourceScoreConfig', full_name='health_assessment.HealthAssessmentRuleVersion.relatedResourceScoreConfig', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eventScoreWeight', full_name='health_assessment.HealthAssessmentRuleVersion.eventScoreWeight', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relatedResourceWeight', full_name='health_assessment.HealthAssessmentRuleVersion.relatedResourceWeight', index=6,
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
  serialized_start=247,
  serialized_end=573,
)

_HEALTHASSESSMENTRULEVERSION.fields_by_name['eventScoreConfig'].message_type = idcmanager__sdk_dot_model_dot_health__assessment_dot_health__assessment__event__score__config__item__pb2._HEALTHASSESSMENTEVENTSCORECONFIGITEM
_HEALTHASSESSMENTRULEVERSION.fields_by_name['relatedResourceScoreConfig'].message_type = idcmanager__sdk_dot_model_dot_health__assessment_dot_health__assessment__related__resource__score__config__item__pb2._HEALTHASSESSMENTRELATEDRESOURCESCORECONFIGITEM
DESCRIPTOR.message_types_by_name['HealthAssessmentRuleVersion'] = _HEALTHASSESSMENTRULEVERSION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HealthAssessmentRuleVersion = _reflection.GeneratedProtocolMessageType('HealthAssessmentRuleVersion', (_message.Message,), {
  'DESCRIPTOR' : _HEALTHASSESSMENTRULEVERSION,
  '__module__' : 'health_assessment_rule_version_pb2'
  # @@protoc_insertion_point(class_scope:health_assessment.HealthAssessmentRuleVersion)
  })
_sym_db.RegisterMessage(HealthAssessmentRuleVersion)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
