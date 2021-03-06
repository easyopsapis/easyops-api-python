# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_process_instance.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flowable_service_sdk.model.flowable_service import process_variable_pb2 as flowable__service__sdk_dot_model_dot_flowable__service_dot_process__variable__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_process_instance.proto',
  package='process_instance',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1aget_process_instance.proto\x12\x10process_instance\x1a\x42\x66lowable_service_sdk/model/flowable_service/process_variable.proto\"/\n\x19GetProcessInstanceRequest\x12\x12\n\ninstanceId\x18\x01 \x01(\t\"\xc1\t\n\x1aGetProcessInstanceResponse\x12S\n\x0eprocessVersion\x18\x01 \x01(\x0b\x32;.process_instance.GetProcessInstanceResponse.ProcessVersion\x12\x45\n\x07process\x18\x02 \x01(\x0b\x32\x34.process_instance.GetProcessInstanceResponse.Process\x12O\n\x0cuserTaskList\x18\x03 \x03(\x0b\x32\x39.process_instance.GetProcessInstanceResponse.UserTaskList\x12G\n\x08stepList\x18\x04 \x03(\x0b\x32\x35.process_instance.GetProcessInstanceResponse.StepList\x12\x18\n\x10\x66inishedStepList\x18\x05 \x03(\t\x12\x12\n\ninstanceId\x18\x06 \x01(\t\x12\x1a\n\x12\x66lowableInstanceId\x18\x07 \x01(\t\x12\x0c\n\x04name\x18\x08 \x01(\t\x12\x0f\n\x07\x63reator\x18\t \x01(\t\x12\r\n\x05\x63time\x18\n \x01(\t\x12\r\n\x05\x65time\x18\x0b \x01(\t\x12\x0e\n\x06status\x18\x0c \x01(\t\x12\x12\n\nstepIdList\x18\r \x03(\t\x12\x0e\n\x06stopAt\x18\x0e \x01(\t\x12\x13\n\x0bisSuspended\x18\x0f \x01(\x08\x12\x13\n\x0bisCancelled\x18\x10 \x01(\x08\x1a\x39\n\x0eProcessVersion\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x13\n\x0bversionName\x18\x02 \x01(\t\x1a=\n\x07Process\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x03 \x01(\t\x1a\xa1\x02\n\x0cUserTaskList\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x16\n\x0e\x66ormDefinition\x18\x03 \x01(\t\x12\x16\n\x0eisFormDecision\x18\x04 \x01(\t\x12V\n\tprocessOp\x18\x05 \x03(\x0b\x32\x43.process_instance.GetProcessInstanceResponse.UserTaskList.ProcessOp\x1ao\n\tProcessOp\x12\x0c\n\x04name\x18\x01 \x01(\t\x12>\n\x13\x63onditionExpression\x18\x02 \x01(\x0b\x32!.flowable_service.ProcessVariable\x12\x14\n\x0ctargetTaskId\x18\x03 \x01(\t\x1a\xe9\x01\n\x08StepList\x12\x12\n\nuserTaskId\x18\x01 \x01(\t\x12P\n\x08\x66ormData\x18\x02 \x01(\x0b\x32>.process_instance.GetProcessInstanceResponse.StepList.FormData\x12\x10\n\x08operator\x18\x03 \x01(\t\x12\r\n\x05otime\x18\x04 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x05 \x01(\t\x12\x0c\n\x04memo\x18\x06 \x01(\t\x12\x0e\n\x06status\x18\x07 \x01(\t\x1a(\n\x08\x46ormData\x12\x0e\n\x06header\x18\x01 \x01(\t\x12\x0c\n\x04\x62ody\x18\x02 \x01(\t\"\x91\x01\n!GetProcessInstanceResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12:\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32,.process_instance.GetProcessInstanceResponseb\x06proto3')
  ,
  dependencies=[flowable__service__sdk_dot_model_dot_flowable__service_dot_process__variable__pb2.DESCRIPTOR,])




_GETPROCESSINSTANCEREQUEST = _descriptor.Descriptor(
  name='GetProcessInstanceRequest',
  full_name='process_instance.GetProcessInstanceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='process_instance.GetProcessInstanceRequest.instanceId', index=0,
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
  serialized_start=116,
  serialized_end=163,
)


_GETPROCESSINSTANCERESPONSE_PROCESSVERSION = _descriptor.Descriptor(
  name='ProcessVersion',
  full_name='process_instance.GetProcessInstanceResponse.ProcessVersion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='process_instance.GetProcessInstanceResponse.ProcessVersion.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionName', full_name='process_instance.GetProcessInstanceResponse.ProcessVersion.versionName', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=735,
  serialized_end=792,
)

_GETPROCESSINSTANCERESPONSE_PROCESS = _descriptor.Descriptor(
  name='Process',
  full_name='process_instance.GetProcessInstanceResponse.Process',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='process_instance.GetProcessInstanceResponse.Process.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='process_instance.GetProcessInstanceResponse.Process.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='process_instance.GetProcessInstanceResponse.Process.category', index=2,
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
  serialized_start=794,
  serialized_end=855,
)

_GETPROCESSINSTANCERESPONSE_USERTASKLIST_PROCESSOP = _descriptor.Descriptor(
  name='ProcessOp',
  full_name='process_instance.GetProcessInstanceResponse.UserTaskList.ProcessOp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='process_instance.GetProcessInstanceResponse.UserTaskList.ProcessOp.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conditionExpression', full_name='process_instance.GetProcessInstanceResponse.UserTaskList.ProcessOp.conditionExpression', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targetTaskId', full_name='process_instance.GetProcessInstanceResponse.UserTaskList.ProcessOp.targetTaskId', index=2,
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
  serialized_start=1036,
  serialized_end=1147,
)

_GETPROCESSINSTANCERESPONSE_USERTASKLIST = _descriptor.Descriptor(
  name='UserTaskList',
  full_name='process_instance.GetProcessInstanceResponse.UserTaskList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='process_instance.GetProcessInstanceResponse.UserTaskList.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='process_instance.GetProcessInstanceResponse.UserTaskList.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='formDefinition', full_name='process_instance.GetProcessInstanceResponse.UserTaskList.formDefinition', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isFormDecision', full_name='process_instance.GetProcessInstanceResponse.UserTaskList.isFormDecision', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processOp', full_name='process_instance.GetProcessInstanceResponse.UserTaskList.processOp', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETPROCESSINSTANCERESPONSE_USERTASKLIST_PROCESSOP, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=858,
  serialized_end=1147,
)

_GETPROCESSINSTANCERESPONSE_STEPLIST_FORMDATA = _descriptor.Descriptor(
  name='FormData',
  full_name='process_instance.GetProcessInstanceResponse.StepList.FormData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='process_instance.GetProcessInstanceResponse.StepList.FormData.header', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='body', full_name='process_instance.GetProcessInstanceResponse.StepList.FormData.body', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=1343,
  serialized_end=1383,
)

_GETPROCESSINSTANCERESPONSE_STEPLIST = _descriptor.Descriptor(
  name='StepList',
  full_name='process_instance.GetProcessInstanceResponse.StepList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userTaskId', full_name='process_instance.GetProcessInstanceResponse.StepList.userTaskId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='formData', full_name='process_instance.GetProcessInstanceResponse.StepList.formData', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operator', full_name='process_instance.GetProcessInstanceResponse.StepList.operator', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='otime', full_name='process_instance.GetProcessInstanceResponse.StepList.otime', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='process_instance.GetProcessInstanceResponse.StepList.action', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='process_instance.GetProcessInstanceResponse.StepList.memo', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='process_instance.GetProcessInstanceResponse.StepList.status', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETPROCESSINSTANCERESPONSE_STEPLIST_FORMDATA, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1150,
  serialized_end=1383,
)

_GETPROCESSINSTANCERESPONSE = _descriptor.Descriptor(
  name='GetProcessInstanceResponse',
  full_name='process_instance.GetProcessInstanceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='processVersion', full_name='process_instance.GetProcessInstanceResponse.processVersion', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='process', full_name='process_instance.GetProcessInstanceResponse.process', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userTaskList', full_name='process_instance.GetProcessInstanceResponse.userTaskList', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stepList', full_name='process_instance.GetProcessInstanceResponse.stepList', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='finishedStepList', full_name='process_instance.GetProcessInstanceResponse.finishedStepList', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='process_instance.GetProcessInstanceResponse.instanceId', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flowableInstanceId', full_name='process_instance.GetProcessInstanceResponse.flowableInstanceId', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='process_instance.GetProcessInstanceResponse.name', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='process_instance.GetProcessInstanceResponse.creator', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='process_instance.GetProcessInstanceResponse.ctime', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='etime', full_name='process_instance.GetProcessInstanceResponse.etime', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='process_instance.GetProcessInstanceResponse.status', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stepIdList', full_name='process_instance.GetProcessInstanceResponse.stepIdList', index=12,
      number=13, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stopAt', full_name='process_instance.GetProcessInstanceResponse.stopAt', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isSuspended', full_name='process_instance.GetProcessInstanceResponse.isSuspended', index=14,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isCancelled', full_name='process_instance.GetProcessInstanceResponse.isCancelled', index=15,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETPROCESSINSTANCERESPONSE_PROCESSVERSION, _GETPROCESSINSTANCERESPONSE_PROCESS, _GETPROCESSINSTANCERESPONSE_USERTASKLIST, _GETPROCESSINSTANCERESPONSE_STEPLIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=166,
  serialized_end=1383,
)


_GETPROCESSINSTANCERESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetProcessInstanceResponseWrapper',
  full_name='process_instance.GetProcessInstanceResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='process_instance.GetProcessInstanceResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='process_instance.GetProcessInstanceResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='process_instance.GetProcessInstanceResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='process_instance.GetProcessInstanceResponseWrapper.data', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1386,
  serialized_end=1531,
)

_GETPROCESSINSTANCERESPONSE_PROCESSVERSION.containing_type = _GETPROCESSINSTANCERESPONSE
_GETPROCESSINSTANCERESPONSE_PROCESS.containing_type = _GETPROCESSINSTANCERESPONSE
_GETPROCESSINSTANCERESPONSE_USERTASKLIST_PROCESSOP.fields_by_name['conditionExpression'].message_type = flowable__service__sdk_dot_model_dot_flowable__service_dot_process__variable__pb2._PROCESSVARIABLE
_GETPROCESSINSTANCERESPONSE_USERTASKLIST_PROCESSOP.containing_type = _GETPROCESSINSTANCERESPONSE_USERTASKLIST
_GETPROCESSINSTANCERESPONSE_USERTASKLIST.fields_by_name['processOp'].message_type = _GETPROCESSINSTANCERESPONSE_USERTASKLIST_PROCESSOP
_GETPROCESSINSTANCERESPONSE_USERTASKLIST.containing_type = _GETPROCESSINSTANCERESPONSE
_GETPROCESSINSTANCERESPONSE_STEPLIST_FORMDATA.containing_type = _GETPROCESSINSTANCERESPONSE_STEPLIST
_GETPROCESSINSTANCERESPONSE_STEPLIST.fields_by_name['formData'].message_type = _GETPROCESSINSTANCERESPONSE_STEPLIST_FORMDATA
_GETPROCESSINSTANCERESPONSE_STEPLIST.containing_type = _GETPROCESSINSTANCERESPONSE
_GETPROCESSINSTANCERESPONSE.fields_by_name['processVersion'].message_type = _GETPROCESSINSTANCERESPONSE_PROCESSVERSION
_GETPROCESSINSTANCERESPONSE.fields_by_name['process'].message_type = _GETPROCESSINSTANCERESPONSE_PROCESS
_GETPROCESSINSTANCERESPONSE.fields_by_name['userTaskList'].message_type = _GETPROCESSINSTANCERESPONSE_USERTASKLIST
_GETPROCESSINSTANCERESPONSE.fields_by_name['stepList'].message_type = _GETPROCESSINSTANCERESPONSE_STEPLIST
_GETPROCESSINSTANCERESPONSEWRAPPER.fields_by_name['data'].message_type = _GETPROCESSINSTANCERESPONSE
DESCRIPTOR.message_types_by_name['GetProcessInstanceRequest'] = _GETPROCESSINSTANCEREQUEST
DESCRIPTOR.message_types_by_name['GetProcessInstanceResponse'] = _GETPROCESSINSTANCERESPONSE
DESCRIPTOR.message_types_by_name['GetProcessInstanceResponseWrapper'] = _GETPROCESSINSTANCERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetProcessInstanceRequest = _reflection.GeneratedProtocolMessageType('GetProcessInstanceRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPROCESSINSTANCEREQUEST,
  '__module__' : 'get_process_instance_pb2'
  # @@protoc_insertion_point(class_scope:process_instance.GetProcessInstanceRequest)
  })
_sym_db.RegisterMessage(GetProcessInstanceRequest)

GetProcessInstanceResponse = _reflection.GeneratedProtocolMessageType('GetProcessInstanceResponse', (_message.Message,), {

  'ProcessVersion' : _reflection.GeneratedProtocolMessageType('ProcessVersion', (_message.Message,), {
    'DESCRIPTOR' : _GETPROCESSINSTANCERESPONSE_PROCESSVERSION,
    '__module__' : 'get_process_instance_pb2'
    # @@protoc_insertion_point(class_scope:process_instance.GetProcessInstanceResponse.ProcessVersion)
    })
  ,

  'Process' : _reflection.GeneratedProtocolMessageType('Process', (_message.Message,), {
    'DESCRIPTOR' : _GETPROCESSINSTANCERESPONSE_PROCESS,
    '__module__' : 'get_process_instance_pb2'
    # @@protoc_insertion_point(class_scope:process_instance.GetProcessInstanceResponse.Process)
    })
  ,

  'UserTaskList' : _reflection.GeneratedProtocolMessageType('UserTaskList', (_message.Message,), {

    'ProcessOp' : _reflection.GeneratedProtocolMessageType('ProcessOp', (_message.Message,), {
      'DESCRIPTOR' : _GETPROCESSINSTANCERESPONSE_USERTASKLIST_PROCESSOP,
      '__module__' : 'get_process_instance_pb2'
      # @@protoc_insertion_point(class_scope:process_instance.GetProcessInstanceResponse.UserTaskList.ProcessOp)
      })
    ,
    'DESCRIPTOR' : _GETPROCESSINSTANCERESPONSE_USERTASKLIST,
    '__module__' : 'get_process_instance_pb2'
    # @@protoc_insertion_point(class_scope:process_instance.GetProcessInstanceResponse.UserTaskList)
    })
  ,

  'StepList' : _reflection.GeneratedProtocolMessageType('StepList', (_message.Message,), {

    'FormData' : _reflection.GeneratedProtocolMessageType('FormData', (_message.Message,), {
      'DESCRIPTOR' : _GETPROCESSINSTANCERESPONSE_STEPLIST_FORMDATA,
      '__module__' : 'get_process_instance_pb2'
      # @@protoc_insertion_point(class_scope:process_instance.GetProcessInstanceResponse.StepList.FormData)
      })
    ,
    'DESCRIPTOR' : _GETPROCESSINSTANCERESPONSE_STEPLIST,
    '__module__' : 'get_process_instance_pb2'
    # @@protoc_insertion_point(class_scope:process_instance.GetProcessInstanceResponse.StepList)
    })
  ,
  'DESCRIPTOR' : _GETPROCESSINSTANCERESPONSE,
  '__module__' : 'get_process_instance_pb2'
  # @@protoc_insertion_point(class_scope:process_instance.GetProcessInstanceResponse)
  })
_sym_db.RegisterMessage(GetProcessInstanceResponse)
_sym_db.RegisterMessage(GetProcessInstanceResponse.ProcessVersion)
_sym_db.RegisterMessage(GetProcessInstanceResponse.Process)
_sym_db.RegisterMessage(GetProcessInstanceResponse.UserTaskList)
_sym_db.RegisterMessage(GetProcessInstanceResponse.UserTaskList.ProcessOp)
_sym_db.RegisterMessage(GetProcessInstanceResponse.StepList)
_sym_db.RegisterMessage(GetProcessInstanceResponse.StepList.FormData)

GetProcessInstanceResponseWrapper = _reflection.GeneratedProtocolMessageType('GetProcessInstanceResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _GETPROCESSINSTANCERESPONSEWRAPPER,
  '__module__' : 'get_process_instance_pb2'
  # @@protoc_insertion_point(class_scope:process_instance.GetProcessInstanceResponseWrapper)
  })
_sym_db.RegisterMessage(GetProcessInstanceResponseWrapper)


# @@protoc_insertion_point(module_scope)
