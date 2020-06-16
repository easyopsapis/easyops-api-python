# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: process_definition_version.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ops_automation_sdk.model.flowable_service import bpmn_user_task_pb2 as ops__automation__sdk_dot_model_dot_flowable__service_dot_bpmn__user__task__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='process_definition_version.proto',
  package='flowable_service',
  syntax='proto3',
  serialized_options=_b('ZJgo.easyops.local/contracts/protorepo-models/easyops/model/flowable_service'),
  serialized_pb=_b('\n process_definition_version.proto\x12\x10\x66lowable_service\x1a>ops_automation_sdk/model/flowable_service/bpmn_user_task.proto\"\xec\x02\n\x18ProcessDefinitionVersion\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0bversionName\x18\x03 \x01(\t\x12\x14\n\x0c\x64\x65ploymentId\x18\x04 \x01(\t\x12\x1c\n\x14\x66lowableDefinitionId\x18\x05 \x01(\t\x12\x1d\n\x15\x66lowableDefinitionKey\x18\x06 \x01(\t\x12\x0e\n\x06isMain\x18\x07 \x01(\x08\x12\r\n\x05state\x18\x08 \x01(\t\x12\x16\n\x0e\x64\x65ploymentTime\x18\t \x01(\t\x12\x1a\n\x12parentDeploymentId\x18\n \x01(\t\x12\x0f\n\x07\x62pmnXML\x18\x0b \x01(\t\x12\x0f\n\x07\x63reator\x18\x0c \x01(\t\x12\r\n\x05\x63time\x18\r \x01(\t\x12\x0c\n\x04memo\x18\x0e \x01(\t\x12\x34\n\x0cuserTaskList\x18\x0f \x03(\x0b\x32\x1e.flowable_service.BPMNUserTaskBLZJgo.easyops.local/contracts/protorepo-models/easyops/model/flowable_serviceb\x06proto3')
  ,
  dependencies=[ops__automation__sdk_dot_model_dot_flowable__service_dot_bpmn__user__task__pb2.DESCRIPTOR,])




_PROCESSDEFINITIONVERSION = _descriptor.Descriptor(
  name='ProcessDefinitionVersion',
  full_name='flowable_service.ProcessDefinitionVersion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='flowable_service.ProcessDefinitionVersion.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='flowable_service.ProcessDefinitionVersion.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionName', full_name='flowable_service.ProcessDefinitionVersion.versionName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deploymentId', full_name='flowable_service.ProcessDefinitionVersion.deploymentId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flowableDefinitionId', full_name='flowable_service.ProcessDefinitionVersion.flowableDefinitionId', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flowableDefinitionKey', full_name='flowable_service.ProcessDefinitionVersion.flowableDefinitionKey', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isMain', full_name='flowable_service.ProcessDefinitionVersion.isMain', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='flowable_service.ProcessDefinitionVersion.state', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deploymentTime', full_name='flowable_service.ProcessDefinitionVersion.deploymentTime', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parentDeploymentId', full_name='flowable_service.ProcessDefinitionVersion.parentDeploymentId', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bpmnXML', full_name='flowable_service.ProcessDefinitionVersion.bpmnXML', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='flowable_service.ProcessDefinitionVersion.creator', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='flowable_service.ProcessDefinitionVersion.ctime', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='flowable_service.ProcessDefinitionVersion.memo', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userTaskList', full_name='flowable_service.ProcessDefinitionVersion.userTaskList', index=14,
      number=15, type=11, cpp_type=10, label=3,
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
  serialized_start=119,
  serialized_end=483,
)

_PROCESSDEFINITIONVERSION.fields_by_name['userTaskList'].message_type = ops__automation__sdk_dot_model_dot_flowable__service_dot_bpmn__user__task__pb2._BPMNUSERTASK
DESCRIPTOR.message_types_by_name['ProcessDefinitionVersion'] = _PROCESSDEFINITIONVERSION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProcessDefinitionVersion = _reflection.GeneratedProtocolMessageType('ProcessDefinitionVersion', (_message.Message,), {
  'DESCRIPTOR' : _PROCESSDEFINITIONVERSION,
  '__module__' : 'process_definition_version_pb2'
  # @@protoc_insertion_point(class_scope:flowable_service.ProcessDefinitionVersion)
  })
_sym_db.RegisterMessage(ProcessDefinitionVersion)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
