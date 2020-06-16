# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bpmn_user_task.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from metadata_center_sdk.model.flowable_service import bpmn_links_pb2 as metadata__center__sdk_dot_model_dot_flowable__service_dot_bpmn__links__pb2
from metadata_center_sdk.model.flowable_service import process_variable_pb2 as metadata__center__sdk_dot_model_dot_flowable__service_dot_process__variable__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bpmn_user_task.proto',
  package='flowable_service',
  syntax='proto3',
  serialized_options=_b('ZJgo.easyops.local/contracts/protorepo-models/easyops/model/flowable_service'),
  serialized_pb=_b('\n\x14\x62pmn_user_task.proto\x12\x10\x66lowable_service\x1a;metadata_center_sdk/model/flowable_service/bpmn_links.proto\x1a\x41metadata_center_sdk/model/flowable_service/process_variable.proto\"\x8b\x03\n\x0c\x42PMNUserTask\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12*\n\x05links\x18\x03 \x01(\x0b\x32\x1b.flowable_service.BPMNLinks\x12\x16\n\x0eisFormDecision\x18\x04 \x01(\t\x12\x12\n\nassignType\x18\x05 \x01(\t\x12\x16\n\x0e\x61ssignStrategy\x18\x06 \x01(\t\x12\x10\n\x08userType\x18\x07 \x01(\t\x12\x18\n\x10\x61ssigneeListUser\x18\x08 \x03(\t\x12\x17\n\x0ftaskWorkingTime\x18\t \x01(\x02\x12;\n\tprocessOp\x18\n \x03(\x0b\x32(.flowable_service.BPMNUserTask.ProcessOp\x1ao\n\tProcessOp\x12\x0c\n\x04name\x18\x01 \x01(\t\x12>\n\x13\x63onditionExpression\x18\x02 \x01(\x0b\x32!.flowable_service.ProcessVariable\x12\x14\n\x0ctargetTaskId\x18\x03 \x01(\tBLZJgo.easyops.local/contracts/protorepo-models/easyops/model/flowable_serviceb\x06proto3')
  ,
  dependencies=[metadata__center__sdk_dot_model_dot_flowable__service_dot_bpmn__links__pb2.DESCRIPTOR,metadata__center__sdk_dot_model_dot_flowable__service_dot_process__variable__pb2.DESCRIPTOR,])




_BPMNUSERTASK_PROCESSOP = _descriptor.Descriptor(
  name='ProcessOp',
  full_name='flowable_service.BPMNUserTask.ProcessOp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='flowable_service.BPMNUserTask.ProcessOp.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conditionExpression', full_name='flowable_service.BPMNUserTask.ProcessOp.conditionExpression', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targetTaskId', full_name='flowable_service.BPMNUserTask.ProcessOp.targetTaskId', index=2,
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
  serialized_start=455,
  serialized_end=566,
)

_BPMNUSERTASK = _descriptor.Descriptor(
  name='BPMNUserTask',
  full_name='flowable_service.BPMNUserTask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='flowable_service.BPMNUserTask.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='flowable_service.BPMNUserTask.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='links', full_name='flowable_service.BPMNUserTask.links', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isFormDecision', full_name='flowable_service.BPMNUserTask.isFormDecision', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='assignType', full_name='flowable_service.BPMNUserTask.assignType', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='assignStrategy', full_name='flowable_service.BPMNUserTask.assignStrategy', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userType', full_name='flowable_service.BPMNUserTask.userType', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='assigneeListUser', full_name='flowable_service.BPMNUserTask.assigneeListUser', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='taskWorkingTime', full_name='flowable_service.BPMNUserTask.taskWorkingTime', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processOp', full_name='flowable_service.BPMNUserTask.processOp', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_BPMNUSERTASK_PROCESSOP, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=171,
  serialized_end=566,
)

_BPMNUSERTASK_PROCESSOP.fields_by_name['conditionExpression'].message_type = metadata__center__sdk_dot_model_dot_flowable__service_dot_process__variable__pb2._PROCESSVARIABLE
_BPMNUSERTASK_PROCESSOP.containing_type = _BPMNUSERTASK
_BPMNUSERTASK.fields_by_name['links'].message_type = metadata__center__sdk_dot_model_dot_flowable__service_dot_bpmn__links__pb2._BPMNLINKS
_BPMNUSERTASK.fields_by_name['processOp'].message_type = _BPMNUSERTASK_PROCESSOP
DESCRIPTOR.message_types_by_name['BPMNUserTask'] = _BPMNUSERTASK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BPMNUserTask = _reflection.GeneratedProtocolMessageType('BPMNUserTask', (_message.Message,), {

  'ProcessOp' : _reflection.GeneratedProtocolMessageType('ProcessOp', (_message.Message,), {
    'DESCRIPTOR' : _BPMNUSERTASK_PROCESSOP,
    '__module__' : 'bpmn_user_task_pb2'
    # @@protoc_insertion_point(class_scope:flowable_service.BPMNUserTask.ProcessOp)
    })
  ,
  'DESCRIPTOR' : _BPMNUSERTASK,
  '__module__' : 'bpmn_user_task_pb2'
  # @@protoc_insertion_point(class_scope:flowable_service.BPMNUserTask)
  })
_sym_db.RegisterMessage(BPMNUserTask)
_sym_db.RegisterMessage(BPMNUserTask.ProcessOp)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
