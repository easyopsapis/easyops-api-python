# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_plan.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from monitor_sdk.model.tuna_service import requirement_instance_pb2 as monitor__sdk_dot_model_dot_tuna__service_dot_requirement__instance__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='test_plan.proto',
  package='tuna_service',
  syntax='proto3',
  serialized_options=_b('ZFgo.easyops.local/contracts/protorepo-models/easyops/model/tuna_service'),
  serialized_pb=_b('\n\x0ftest_plan.proto\x12\x0ctuna_service\x1a\x39monitor_sdk/model/tuna_service/requirement_instance.proto\"\xf9\x04\n\x08TestPlan\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\nreviewDate\x18\x03 \x01(\t\x12\x1b\n\x13startExcutePlanDate\x18\x04 \x01(\t\x12\x18\n\x10projectStartDate\x18\x05 \x01(\t\x12\x1f\n\x17projectPlanCompleteDate\x18\x06 \x01(\t\x12!\n\x19projectActualCompleteDate\x18\x07 \x01(\t\x12\x19\n\x11\x66unctionMissCount\x18\x08 \x01(\x05\x12\x17\n\x0f\x62\x61\x63kendBugCount\x18\t \x01(\x05\x12\x12\n\nbugPercent\x18\n \x01(\t\x12\x10\n\x08\x62ugTotal\x18\x0b \x01(\x05\x12\x17\n\x0f\x63\x61pabilityCount\x18\x0c \x01(\x05\x12\x16\n\x0e\x63odingErrCount\x18\r \x01(\x05\x12\x14\n\x0c\x64\x65layPercent\x18\x0e \x01(\t\x12\x18\n\x10\x65nvironmentCount\x18\x0f \x01(\x05\x12\x15\n\rfrontBugCount\x18\x10 \x01(\x05\x12\x14\n\x0cprojectScore\x18\x11 \x01(\t\x12\x1e\n\x16requirementBlurryCount\x18\x12 \x01(\x05\x12\x18\n\x10scenarioBugCount\x18\x13 \x01(\x05\x12\x15\n\rscenarioCount\x18\x14 \x01(\x05\x12\x0e\n\x06status\x18\x15 \x01(\t\x12\x17\n\x0fsuggestionCount\x18\x16 \x01(\x05\x12\x19\n\x11unableAppearCount\x18\x17 \x01(\x05\x12?\n\x14requirement_instance\x18\x18 \x03(\x0b\x32!.tuna_service.RequirementInstanceBHZFgo.easyops.local/contracts/protorepo-models/easyops/model/tuna_serviceb\x06proto3')
  ,
  dependencies=[monitor__sdk_dot_model_dot_tuna__service_dot_requirement__instance__pb2.DESCRIPTOR,])




_TESTPLAN = _descriptor.Descriptor(
  name='TestPlan',
  full_name='tuna_service.TestPlan',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='tuna_service.TestPlan.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='tuna_service.TestPlan.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reviewDate', full_name='tuna_service.TestPlan.reviewDate', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startExcutePlanDate', full_name='tuna_service.TestPlan.startExcutePlanDate', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='projectStartDate', full_name='tuna_service.TestPlan.projectStartDate', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='projectPlanCompleteDate', full_name='tuna_service.TestPlan.projectPlanCompleteDate', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='projectActualCompleteDate', full_name='tuna_service.TestPlan.projectActualCompleteDate', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='functionMissCount', full_name='tuna_service.TestPlan.functionMissCount', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='backendBugCount', full_name='tuna_service.TestPlan.backendBugCount', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bugPercent', full_name='tuna_service.TestPlan.bugPercent', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bugTotal', full_name='tuna_service.TestPlan.bugTotal', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='capabilityCount', full_name='tuna_service.TestPlan.capabilityCount', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codingErrCount', full_name='tuna_service.TestPlan.codingErrCount', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delayPercent', full_name='tuna_service.TestPlan.delayPercent', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='environmentCount', full_name='tuna_service.TestPlan.environmentCount', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frontBugCount', full_name='tuna_service.TestPlan.frontBugCount', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='projectScore', full_name='tuna_service.TestPlan.projectScore', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requirementBlurryCount', full_name='tuna_service.TestPlan.requirementBlurryCount', index=17,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scenarioBugCount', full_name='tuna_service.TestPlan.scenarioBugCount', index=18,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scenarioCount', full_name='tuna_service.TestPlan.scenarioCount', index=19,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='tuna_service.TestPlan.status', index=20,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='suggestionCount', full_name='tuna_service.TestPlan.suggestionCount', index=21,
      number=22, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unableAppearCount', full_name='tuna_service.TestPlan.unableAppearCount', index=22,
      number=23, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requirement_instance', full_name='tuna_service.TestPlan.requirement_instance', index=23,
      number=24, type=11, cpp_type=10, label=3,
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
  serialized_start=93,
  serialized_end=726,
)

_TESTPLAN.fields_by_name['requirement_instance'].message_type = monitor__sdk_dot_model_dot_tuna__service_dot_requirement__instance__pb2._REQUIREMENTINSTANCE
DESCRIPTOR.message_types_by_name['TestPlan'] = _TESTPLAN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TestPlan = _reflection.GeneratedProtocolMessageType('TestPlan', (_message.Message,), {
  'DESCRIPTOR' : _TESTPLAN,
  '__module__' : 'test_plan_pb2'
  # @@protoc_insertion_point(class_scope:tuna_service.TestPlan)
  })
_sym_db.RegisterMessage(TestPlan)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
