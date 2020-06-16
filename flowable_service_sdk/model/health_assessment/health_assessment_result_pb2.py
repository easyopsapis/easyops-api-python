# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: health_assessment_result.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flowable_service_sdk.model.health_assessment import health_assessment_related_resource_event_score_pb2 as flowable__service__sdk_dot_model_dot_health__assessment_dot_health__assessment__related__resource__event__score__pb2
from flowable_service_sdk.model.health_assessment import health_assessment_event_score_config_item_pb2 as flowable__service__sdk_dot_model_dot_health__assessment_dot_health__assessment__event__score__config__item__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='health_assessment_result.proto',
  package='health_assessment',
  syntax='proto3',
  serialized_options=_b('ZKgo.easyops.local/contracts/protorepo-models/easyops/model/health_assessment'),
  serialized_pb=_b('\n\x1ehealth_assessment_result.proto\x12\x11health_assessment\x1a\x61\x66lowable_service_sdk/model/health_assessment/health_assessment_related_resource_event_score.proto\x1a\\flowable_service_sdk/model/health_assessment/health_assessment_event_score_config_item.proto\"\xa6\x03\n\x16HealthAssessmentResult\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0e\n\x06ruleId\x18\x02 \x01(\t\x12\x15\n\rruleVersionId\x18\x03 \x01(\t\x12\x10\n\x08objectId\x18\x04 \x01(\t\x12\x12\n\neventScore\x18\x05 \x01(\x05\x12\x15\n\rrelationScore\x18\x06 \x01(\x05\x12\x13\n\x0bhealthScore\x18\x07 \x01(\x05\x12`\n\x1arelatedResourceEventScores\x18\x08 \x03(\x0b\x32<.health_assessment.HealthAssessmentRelatedResourceEventScore\x12\x18\n\x10\x65ventScoreWeight\x18\t \x01(\x05\x12\x1d\n\x15relatedResourceWeight\x18\n \x01(\x05\x12\x11\n\ttimestamp\x18\x0b \x01(\x05\x12Q\n\x10\x65ventScoreConfig\x18\x0c \x03(\x0b\x32\x37.health_assessment.HealthAssessmentEventScoreConfigItemBMZKgo.easyops.local/contracts/protorepo-models/easyops/model/health_assessmentb\x06proto3')
  ,
  dependencies=[flowable__service__sdk_dot_model_dot_health__assessment_dot_health__assessment__related__resource__event__score__pb2.DESCRIPTOR,flowable__service__sdk_dot_model_dot_health__assessment_dot_health__assessment__event__score__config__item__pb2.DESCRIPTOR,])




_HEALTHASSESSMENTRESULT = _descriptor.Descriptor(
  name='HealthAssessmentResult',
  full_name='health_assessment.HealthAssessmentResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='health_assessment.HealthAssessmentResult.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ruleId', full_name='health_assessment.HealthAssessmentResult.ruleId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ruleVersionId', full_name='health_assessment.HealthAssessmentResult.ruleVersionId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectId', full_name='health_assessment.HealthAssessmentResult.objectId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eventScore', full_name='health_assessment.HealthAssessmentResult.eventScore', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relationScore', full_name='health_assessment.HealthAssessmentResult.relationScore', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='healthScore', full_name='health_assessment.HealthAssessmentResult.healthScore', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relatedResourceEventScores', full_name='health_assessment.HealthAssessmentResult.relatedResourceEventScores', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eventScoreWeight', full_name='health_assessment.HealthAssessmentResult.eventScoreWeight', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relatedResourceWeight', full_name='health_assessment.HealthAssessmentResult.relatedResourceWeight', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='health_assessment.HealthAssessmentResult.timestamp', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eventScoreConfig', full_name='health_assessment.HealthAssessmentResult.eventScoreConfig', index=11,
      number=12, type=11, cpp_type=10, label=3,
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
  serialized_start=247,
  serialized_end=669,
)

_HEALTHASSESSMENTRESULT.fields_by_name['relatedResourceEventScores'].message_type = flowable__service__sdk_dot_model_dot_health__assessment_dot_health__assessment__related__resource__event__score__pb2._HEALTHASSESSMENTRELATEDRESOURCEEVENTSCORE
_HEALTHASSESSMENTRESULT.fields_by_name['eventScoreConfig'].message_type = flowable__service__sdk_dot_model_dot_health__assessment_dot_health__assessment__event__score__config__item__pb2._HEALTHASSESSMENTEVENTSCORECONFIGITEM
DESCRIPTOR.message_types_by_name['HealthAssessmentResult'] = _HEALTHASSESSMENTRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HealthAssessmentResult = _reflection.GeneratedProtocolMessageType('HealthAssessmentResult', (_message.Message,), {
  'DESCRIPTOR' : _HEALTHASSESSMENTRESULT,
  '__module__' : 'health_assessment_result_pb2'
  # @@protoc_insertion_point(class_scope:health_assessment.HealthAssessmentResult)
  })
_sym_db.RegisterMessage(HealthAssessmentResult)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
