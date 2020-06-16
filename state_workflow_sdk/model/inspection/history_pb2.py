# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: history.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from state_workflow_sdk.model.inspection import target_pb2 as state__workflow__sdk_dot_model_dot_inspection_dot_target__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='history.proto',
  package='inspection',
  syntax='proto3',
  serialized_options=_b('ZDgo.easyops.local/contracts/protorepo-models/easyops/model/inspection'),
  serialized_pb=_b('\n\rhistory.proto\x12\ninspection\x1a\x30state_workflow_sdk/model/inspection/target.proto\"\xdd\x01\n\x11InspectionHistory\x12\r\n\x05jobId\x18\x01 \x01(\t\x12\x0e\n\x06taskId\x18\x02 \x01(\t\x12\x10\n\x08taskName\x18\x03 \x01(\t\x12\x11\n\tstartTime\x18\x04 \x01(\x05\x12\x0f\n\x07\x65ndTime\x18\x05 \x01(\x05\x12\x10\n\x08usedTime\x18\x06 \x01(\x05\x12\x0e\n\x06status\x18\x07 \x01(\t\x12\x13\n\x0bpassingRate\x18\x08 \x01(\x02\x12\r\n\x05score\x18\t \x01(\x02\x12-\n\x07targets\x18\n \x03(\x0b\x32\x1c.inspection.InspectionTargetBFZDgo.easyops.local/contracts/protorepo-models/easyops/model/inspectionb\x06proto3')
  ,
  dependencies=[state__workflow__sdk_dot_model_dot_inspection_dot_target__pb2.DESCRIPTOR,])




_INSPECTIONHISTORY = _descriptor.Descriptor(
  name='InspectionHistory',
  full_name='inspection.InspectionHistory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='jobId', full_name='inspection.InspectionHistory.jobId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='taskId', full_name='inspection.InspectionHistory.taskId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='taskName', full_name='inspection.InspectionHistory.taskName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='inspection.InspectionHistory.startTime', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endTime', full_name='inspection.InspectionHistory.endTime', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='usedTime', full_name='inspection.InspectionHistory.usedTime', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='inspection.InspectionHistory.status', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='passingRate', full_name='inspection.InspectionHistory.passingRate', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score', full_name='inspection.InspectionHistory.score', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targets', full_name='inspection.InspectionHistory.targets', index=9,
      number=10, type=11, cpp_type=10, label=3,
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
  serialized_start=80,
  serialized_end=301,
)

_INSPECTIONHISTORY.fields_by_name['targets'].message_type = state__workflow__sdk_dot_model_dot_inspection_dot_target__pb2._INSPECTIONTARGET
DESCRIPTOR.message_types_by_name['InspectionHistory'] = _INSPECTIONHISTORY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InspectionHistory = _reflection.GeneratedProtocolMessageType('InspectionHistory', (_message.Message,), {
  'DESCRIPTOR' : _INSPECTIONHISTORY,
  '__module__' : 'history_pb2'
  # @@protoc_insertion_point(class_scope:inspection.InspectionHistory)
  })
_sym_db.RegisterMessage(InspectionHistory)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
