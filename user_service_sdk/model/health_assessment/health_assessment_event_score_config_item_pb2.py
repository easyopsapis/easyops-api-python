# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: health_assessment_event_score_config_item.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='health_assessment_event_score_config_item.proto',
  package='health_assessment',
  syntax='proto3',
  serialized_options=_b('ZKgo.easyops.local/contracts/protorepo-models/easyops/model/health_assessment'),
  serialized_pb=_b('\n/health_assessment_event_score_config_item.proto\x12\x11health_assessment\"R\n$HealthAssessmentEventScoreConfigItem\x12\x12\n\neventLevel\x18\x01 \x01(\t\x12\x16\n\x0e\x64\x65\x64uctionScore\x18\x02 \x01(\x05\x42MZKgo.easyops.local/contracts/protorepo-models/easyops/model/health_assessmentb\x06proto3')
)




_HEALTHASSESSMENTEVENTSCORECONFIGITEM = _descriptor.Descriptor(
  name='HealthAssessmentEventScoreConfigItem',
  full_name='health_assessment.HealthAssessmentEventScoreConfigItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='eventLevel', full_name='health_assessment.HealthAssessmentEventScoreConfigItem.eventLevel', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deductionScore', full_name='health_assessment.HealthAssessmentEventScoreConfigItem.deductionScore', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=70,
  serialized_end=152,
)

DESCRIPTOR.message_types_by_name['HealthAssessmentEventScoreConfigItem'] = _HEALTHASSESSMENTEVENTSCORECONFIGITEM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HealthAssessmentEventScoreConfigItem = _reflection.GeneratedProtocolMessageType('HealthAssessmentEventScoreConfigItem', (_message.Message,), {
  'DESCRIPTOR' : _HEALTHASSESSMENTEVENTSCORECONFIGITEM,
  '__module__' : 'health_assessment_event_score_config_item_pb2'
  # @@protoc_insertion_point(class_scope:health_assessment.HealthAssessmentEventScoreConfigItem)
  })
_sym_db.RegisterMessage(HealthAssessmentEventScoreConfigItem)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)