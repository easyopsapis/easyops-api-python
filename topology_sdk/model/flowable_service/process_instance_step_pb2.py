# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: process_instance_step.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from topology_sdk.model.flowable_service import process_variable_pb2 as topology__sdk_dot_model_dot_flowable__service_dot_process__variable__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='process_instance_step.proto',
  package='flowable_service',
  syntax='proto3',
  serialized_options=_b('ZJgo.easyops.local/contracts/protorepo-models/easyops/model/flowable_service'),
  serialized_pb=_b('\n\x1bprocess_instance_step.proto\x12\x10\x66lowable_service\x1a:topology_sdk/model/flowable_service/process_variable.proto\"\xb7\x02\n\x13ProcessInstanceStep\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x12\n\nuserTaskId\x18\x02 \x01(\t\x12\x16\n\x0e\x66lowableTaskId\x18\x03 \x01(\t\x12\x0f\n\x07\x63reator\x18\x04 \x01(\t\x12\r\n\x05\x63time\x18\x05 \x01(\t\x12\r\n\x05\x65time\x18\x06 \x01(\t\x12\x10\n\x08operator\x18\x07 \x01(\t\x12\x0e\n\x06status\x18\x08 \x01(\t\x12\r\n\x05otime\x18\t \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\n \x01(\t\x12\x0c\n\x04memo\x18\x0b \x01(\t\x12\x34\n\tvariables\x18\x0c \x03(\x0b\x32!.flowable_service.ProcessVariable\x12\x16\n\x0e\x66ormHeaderData\x18\r \x01(\t\x12\x14\n\x0c\x66ormBodyData\x18\x0e \x01(\tBLZJgo.easyops.local/contracts/protorepo-models/easyops/model/flowable_serviceb\x06proto3')
  ,
  dependencies=[topology__sdk_dot_model_dot_flowable__service_dot_process__variable__pb2.DESCRIPTOR,])




_PROCESSINSTANCESTEP = _descriptor.Descriptor(
  name='ProcessInstanceStep',
  full_name='flowable_service.ProcessInstanceStep',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='flowable_service.ProcessInstanceStep.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userTaskId', full_name='flowable_service.ProcessInstanceStep.userTaskId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flowableTaskId', full_name='flowable_service.ProcessInstanceStep.flowableTaskId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='flowable_service.ProcessInstanceStep.creator', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='flowable_service.ProcessInstanceStep.ctime', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='etime', full_name='flowable_service.ProcessInstanceStep.etime', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operator', full_name='flowable_service.ProcessInstanceStep.operator', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='flowable_service.ProcessInstanceStep.status', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='otime', full_name='flowable_service.ProcessInstanceStep.otime', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='flowable_service.ProcessInstanceStep.action', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='flowable_service.ProcessInstanceStep.memo', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='variables', full_name='flowable_service.ProcessInstanceStep.variables', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='formHeaderData', full_name='flowable_service.ProcessInstanceStep.formHeaderData', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='formBodyData', full_name='flowable_service.ProcessInstanceStep.formBodyData', index=13,
      number=14, type=9, cpp_type=9, label=1,
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
  serialized_start=110,
  serialized_end=421,
)

_PROCESSINSTANCESTEP.fields_by_name['variables'].message_type = topology__sdk_dot_model_dot_flowable__service_dot_process__variable__pb2._PROCESSVARIABLE
DESCRIPTOR.message_types_by_name['ProcessInstanceStep'] = _PROCESSINSTANCESTEP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProcessInstanceStep = _reflection.GeneratedProtocolMessageType('ProcessInstanceStep', (_message.Message,), {
  'DESCRIPTOR' : _PROCESSINSTANCESTEP,
  '__module__' : 'process_instance_step_pb2'
  # @@protoc_insertion_point(class_scope:flowable_service.ProcessInstanceStep)
  })
_sym_db.RegisterMessage(ProcessInstanceStep)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
