# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bpmn_process.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from easy_command_sdk.model.flowable_service import bpmn_sequence_flow_pb2 as easy__command__sdk_dot_model_dot_flowable__service_dot_bpmn__sequence__flow__pb2
from easy_command_sdk.model.flowable_service import bpmn_exclusive_gateway_pb2 as easy__command__sdk_dot_model_dot_flowable__service_dot_bpmn__exclusive__gateway__pb2
from easy_command_sdk.model.flowable_service import bpmn_start_event_pb2 as easy__command__sdk_dot_model_dot_flowable__service_dot_bpmn__start__event__pb2
from easy_command_sdk.model.flowable_service import bpmn_end_event_pb2 as easy__command__sdk_dot_model_dot_flowable__service_dot_bpmn__end__event__pb2
from easy_command_sdk.model.flowable_service import bpmn_user_task_pb2 as easy__command__sdk_dot_model_dot_flowable__service_dot_bpmn__user__task__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bpmn_process.proto',
  package='flowable_service',
  syntax='proto3',
  serialized_options=_b('ZJgo.easyops.local/contracts/protorepo-models/easyops/model/flowable_service'),
  serialized_pb=_b('\n\x12\x62pmn_process.proto\x12\x10\x66lowable_service\x1a@easy_command_sdk/model/flowable_service/bpmn_sequence_flow.proto\x1a\x44\x65\x61sy_command_sdk/model/flowable_service/bpmn_exclusive_gateway.proto\x1a>easy_command_sdk/model/flowable_service/bpmn_start_event.proto\x1a<easy_command_sdk/model/flowable_service/bpmn_end_event.proto\x1a<easy_command_sdk/model/flowable_service/bpmn_user_task.proto\"\xd4\x02\n\x0b\x42PMNProcess\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x15\n\risExecuteable\x18\x03 \x01(\t\x12\x38\n\x0csequenceFlow\x18\x04 \x03(\x0b\x32\".flowable_service.BPMNSequenceFlow\x12@\n\x10\x65xclusiveGateway\x18\x05 \x03(\x0b\x32&.flowable_service.BPMNExclusiveGateway\x12\x34\n\nstartEvent\x18\x06 \x03(\x0b\x32 .flowable_service.BPMNStartEvent\x12\x30\n\x08\x65ndEvent\x18\x07 \x03(\x0b\x32\x1e.flowable_service.BPMNEndEvent\x12\x30\n\x08userTask\x18\x08 \x03(\x0b\x32\x1e.flowable_service.BPMNUserTaskBLZJgo.easyops.local/contracts/protorepo-models/easyops/model/flowable_serviceb\x06proto3')
  ,
  dependencies=[easy__command__sdk_dot_model_dot_flowable__service_dot_bpmn__sequence__flow__pb2.DESCRIPTOR,easy__command__sdk_dot_model_dot_flowable__service_dot_bpmn__exclusive__gateway__pb2.DESCRIPTOR,easy__command__sdk_dot_model_dot_flowable__service_dot_bpmn__start__event__pb2.DESCRIPTOR,easy__command__sdk_dot_model_dot_flowable__service_dot_bpmn__end__event__pb2.DESCRIPTOR,easy__command__sdk_dot_model_dot_flowable__service_dot_bpmn__user__task__pb2.DESCRIPTOR,])




_BPMNPROCESS = _descriptor.Descriptor(
  name='BPMNProcess',
  full_name='flowable_service.BPMNProcess',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='flowable_service.BPMNProcess.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='flowable_service.BPMNProcess.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isExecuteable', full_name='flowable_service.BPMNProcess.isExecuteable', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sequenceFlow', full_name='flowable_service.BPMNProcess.sequenceFlow', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exclusiveGateway', full_name='flowable_service.BPMNProcess.exclusiveGateway', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startEvent', full_name='flowable_service.BPMNProcess.startEvent', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endEvent', full_name='flowable_service.BPMNProcess.endEvent', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userTask', full_name='flowable_service.BPMNProcess.userTask', index=7,
      number=8, type=11, cpp_type=10, label=3,
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
  serialized_start=365,
  serialized_end=705,
)

_BPMNPROCESS.fields_by_name['sequenceFlow'].message_type = easy__command__sdk_dot_model_dot_flowable__service_dot_bpmn__sequence__flow__pb2._BPMNSEQUENCEFLOW
_BPMNPROCESS.fields_by_name['exclusiveGateway'].message_type = easy__command__sdk_dot_model_dot_flowable__service_dot_bpmn__exclusive__gateway__pb2._BPMNEXCLUSIVEGATEWAY
_BPMNPROCESS.fields_by_name['startEvent'].message_type = easy__command__sdk_dot_model_dot_flowable__service_dot_bpmn__start__event__pb2._BPMNSTARTEVENT
_BPMNPROCESS.fields_by_name['endEvent'].message_type = easy__command__sdk_dot_model_dot_flowable__service_dot_bpmn__end__event__pb2._BPMNENDEVENT
_BPMNPROCESS.fields_by_name['userTask'].message_type = easy__command__sdk_dot_model_dot_flowable__service_dot_bpmn__user__task__pb2._BPMNUSERTASK
DESCRIPTOR.message_types_by_name['BPMNProcess'] = _BPMNPROCESS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BPMNProcess = _reflection.GeneratedProtocolMessageType('BPMNProcess', (_message.Message,), {
  'DESCRIPTOR' : _BPMNPROCESS,
  '__module__' : 'bpmn_process_pb2'
  # @@protoc_insertion_point(class_scope:flowable_service.BPMNProcess)
  })
_sym_db.RegisterMessage(BPMNProcess)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
