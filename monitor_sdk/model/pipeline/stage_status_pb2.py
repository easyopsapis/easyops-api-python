# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stage_status.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from monitor_sdk.model.pipeline import condition_pb2 as monitor__sdk_dot_model_dot_pipeline_dot_condition__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='stage_status.proto',
  package='pipeline',
  syntax='proto3',
  serialized_options=_b('ZBgo.easyops.local/contracts/protorepo-models/easyops/model/pipeline'),
  serialized_pb=_b('\n\x12stage_status.proto\x12\x08pipeline\x1a*monitor_sdk/model/pipeline/condition.proto\"\xec\x02\n\x0bStageStatus\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nstage_name\x18\x02 \x01(\t\x12\x0e\n\x06number\x18\x03 \x01(\x05\x12\x10\n\x08parallel\x18\x04 \x01(\x08\x12\r\n\x05state\x18\x05 \x01(\t\x12\'\n\nconditions\x18\x06 \x03(\x0b\x32\x13.pipeline.Condition\x12*\n\x05steps\x18\x07 \x03(\x0b\x32\x1b.pipeline.StageStatus.Steps\x12\x0f\n\x07\x63reated\x18\x08 \x01(\x05\x12\x0f\n\x07updated\x18\t \x01(\x05\x1a\x94\x01\n\x05Steps\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06number\x18\x03 \x01(\x05\x12\r\n\x05state\x18\x04 \x01(\t\x12\x11\n\texit_code\x18\x05 \x01(\x05\x12\x0e\n\x06log_id\x18\x06 \x01(\t\x12\x0f\n\x07started\x18\x07 \x01(\x05\x12\x10\n\x08\x66inished\x18\x08 \x01(\x05\x12\x0c\n\x04type\x18\t \x01(\tBDZBgo.easyops.local/contracts/protorepo-models/easyops/model/pipelineb\x06proto3')
  ,
  dependencies=[monitor__sdk_dot_model_dot_pipeline_dot_condition__pb2.DESCRIPTOR,])




_STAGESTATUS_STEPS = _descriptor.Descriptor(
  name='Steps',
  full_name='pipeline.StageStatus.Steps',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='pipeline.StageStatus.Steps.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='pipeline.StageStatus.Steps.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='number', full_name='pipeline.StageStatus.Steps.number', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='pipeline.StageStatus.Steps.state', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exit_code', full_name='pipeline.StageStatus.Steps.exit_code', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log_id', full_name='pipeline.StageStatus.Steps.log_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='started', full_name='pipeline.StageStatus.Steps.started', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='finished', full_name='pipeline.StageStatus.Steps.finished', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='pipeline.StageStatus.Steps.type', index=8,
      number=9, type=9, cpp_type=9, label=1,
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
  serialized_start=293,
  serialized_end=441,
)

_STAGESTATUS = _descriptor.Descriptor(
  name='StageStatus',
  full_name='pipeline.StageStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='pipeline.StageStatus.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stage_name', full_name='pipeline.StageStatus.stage_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='number', full_name='pipeline.StageStatus.number', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parallel', full_name='pipeline.StageStatus.parallel', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='pipeline.StageStatus.state', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conditions', full_name='pipeline.StageStatus.conditions', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='steps', full_name='pipeline.StageStatus.steps', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created', full_name='pipeline.StageStatus.created', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated', full_name='pipeline.StageStatus.updated', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_STAGESTATUS_STEPS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=77,
  serialized_end=441,
)

_STAGESTATUS_STEPS.containing_type = _STAGESTATUS
_STAGESTATUS.fields_by_name['conditions'].message_type = monitor__sdk_dot_model_dot_pipeline_dot_condition__pb2._CONDITION
_STAGESTATUS.fields_by_name['steps'].message_type = _STAGESTATUS_STEPS
DESCRIPTOR.message_types_by_name['StageStatus'] = _STAGESTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StageStatus = _reflection.GeneratedProtocolMessageType('StageStatus', (_message.Message,), {

  'Steps' : _reflection.GeneratedProtocolMessageType('Steps', (_message.Message,), {
    'DESCRIPTOR' : _STAGESTATUS_STEPS,
    '__module__' : 'stage_status_pb2'
    # @@protoc_insertion_point(class_scope:pipeline.StageStatus.Steps)
    })
  ,
  'DESCRIPTOR' : _STAGESTATUS,
  '__module__' : 'stage_status_pb2'
  # @@protoc_insertion_point(class_scope:pipeline.StageStatus)
  })
_sym_db.RegisterMessage(StageStatus)
_sym_db.RegisterMessage(StageStatus.Steps)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
