# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: task.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from influxdb_service_sdk.model.inspection import user_or_user_group_pb2 as influxdb__service__sdk_dot_model_dot_inspection_dot_user__or__user__group__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='task.proto',
  package='inspection',
  syntax='proto3',
  serialized_options=_b('ZDgo.easyops.local/contracts/protorepo-models/easyops/model/inspection'),
  serialized_pb=_b('\n\ntask.proto\x12\ninspection\x1a>influxdb_service_sdk/model/inspection/user_or_user_group.proto\"\xc8\x04\n\x0eInspectionTask\x12\x18\n\x10inspectionTaskId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0bisAllNotify\x18\x03 \x01(\x08\x12\x1c\n\x14notifyPassComparator\x18\x04 \x01(\t\x12\x13\n\x0bnotifyScore\x18\x05 \x01(\x02\x12-\n\x04\x61rgs\x18\x06 \x03(\x0b\x32\x1f.inspection.InspectionTask.Args\x12\x39\n\nnotifyUser\x18\x07 \x01(\x0b\x32%.inspection.InspectionUserOrUserGroup\x12>\n\x0fnotifyUserGroup\x18\x08 \x01(\x0b\x32%.inspection.InspectionUserOrUserGroup\x12\x10\n\x08taskType\x18\t \x01(\t\x12\x1a\n\x12performanceTargets\x18\n \x01(\t\x12\x17\n\x0fqueryStrategyId\x18\x0b \x01(\t\x12\x15\n\rtaskScheduler\x18\x0c \x01(\t\x12\x33\n\x07targets\x18\r \x03(\x0b\x32\".inspection.InspectionTask.Targets\x12\x0c\n\x04memo\x18\x0e \x01(\t\x12\x12\n\ntemplateId\x18\x0f \x01(\t\x12\x14\n\x0ctemplateName\x18\x10 \x01(\t\x1a\x32\n\x04\x41rgs\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x0e\n\x06source\x18\x03 \x01(\t\x1a\x1d\n\x07Targets\x12\x12\n\ninstanceId\x18\x01 \x01(\tBFZDgo.easyops.local/contracts/protorepo-models/easyops/model/inspectionb\x06proto3')
  ,
  dependencies=[influxdb__service__sdk_dot_model_dot_inspection_dot_user__or__user__group__pb2.DESCRIPTOR,])




_INSPECTIONTASK_ARGS = _descriptor.Descriptor(
  name='Args',
  full_name='inspection.InspectionTask.Args',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='inspection.InspectionTask.Args.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='inspection.InspectionTask.Args.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='inspection.InspectionTask.Args.source', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=594,
  serialized_end=644,
)

_INSPECTIONTASK_TARGETS = _descriptor.Descriptor(
  name='Targets',
  full_name='inspection.InspectionTask.Targets',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='inspection.InspectionTask.Targets.instanceId', index=0,
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
  serialized_start=646,
  serialized_end=675,
)

_INSPECTIONTASK = _descriptor.Descriptor(
  name='InspectionTask',
  full_name='inspection.InspectionTask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inspectionTaskId', full_name='inspection.InspectionTask.inspectionTaskId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='inspection.InspectionTask.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isAllNotify', full_name='inspection.InspectionTask.isAllNotify', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='notifyPassComparator', full_name='inspection.InspectionTask.notifyPassComparator', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='notifyScore', full_name='inspection.InspectionTask.notifyScore', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='args', full_name='inspection.InspectionTask.args', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='notifyUser', full_name='inspection.InspectionTask.notifyUser', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='notifyUserGroup', full_name='inspection.InspectionTask.notifyUserGroup', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='taskType', full_name='inspection.InspectionTask.taskType', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='performanceTargets', full_name='inspection.InspectionTask.performanceTargets', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='queryStrategyId', full_name='inspection.InspectionTask.queryStrategyId', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='taskScheduler', full_name='inspection.InspectionTask.taskScheduler', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targets', full_name='inspection.InspectionTask.targets', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='inspection.InspectionTask.memo', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='templateId', full_name='inspection.InspectionTask.templateId', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='templateName', full_name='inspection.InspectionTask.templateName', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_INSPECTIONTASK_ARGS, _INSPECTIONTASK_TARGETS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=91,
  serialized_end=675,
)

_INSPECTIONTASK_ARGS.containing_type = _INSPECTIONTASK
_INSPECTIONTASK_TARGETS.containing_type = _INSPECTIONTASK
_INSPECTIONTASK.fields_by_name['args'].message_type = _INSPECTIONTASK_ARGS
_INSPECTIONTASK.fields_by_name['notifyUser'].message_type = influxdb__service__sdk_dot_model_dot_inspection_dot_user__or__user__group__pb2._INSPECTIONUSERORUSERGROUP
_INSPECTIONTASK.fields_by_name['notifyUserGroup'].message_type = influxdb__service__sdk_dot_model_dot_inspection_dot_user__or__user__group__pb2._INSPECTIONUSERORUSERGROUP
_INSPECTIONTASK.fields_by_name['targets'].message_type = _INSPECTIONTASK_TARGETS
DESCRIPTOR.message_types_by_name['InspectionTask'] = _INSPECTIONTASK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InspectionTask = _reflection.GeneratedProtocolMessageType('InspectionTask', (_message.Message,), {

  'Args' : _reflection.GeneratedProtocolMessageType('Args', (_message.Message,), {
    'DESCRIPTOR' : _INSPECTIONTASK_ARGS,
    '__module__' : 'task_pb2'
    # @@protoc_insertion_point(class_scope:inspection.InspectionTask.Args)
    })
  ,

  'Targets' : _reflection.GeneratedProtocolMessageType('Targets', (_message.Message,), {
    'DESCRIPTOR' : _INSPECTIONTASK_TARGETS,
    '__module__' : 'task_pb2'
    # @@protoc_insertion_point(class_scope:inspection.InspectionTask.Targets)
    })
  ,
  'DESCRIPTOR' : _INSPECTIONTASK,
  '__module__' : 'task_pb2'
  # @@protoc_insertion_point(class_scope:inspection.InspectionTask)
  })
_sym_db.RegisterMessage(InspectionTask)
_sym_db.RegisterMessage(InspectionTask.Args)
_sym_db.RegisterMessage(InspectionTask.Targets)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
