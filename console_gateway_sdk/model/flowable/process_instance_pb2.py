# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: process_instance.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from console_gateway_sdk.model.flowable import process_variable_pb2 as console__gateway__sdk_dot_model_dot_flowable_dot_process__variable__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='process_instance.proto',
  package='flowable',
  syntax='proto3',
  serialized_options=_b('ZBgo.easyops.local/contracts/protorepo-models/easyops/model/flowable'),
  serialized_pb=_b('\n\x16process_instance.proto\x12\x08\x66lowable\x1a\x39\x63onsole_gateway_sdk/model/flowable/process_variable.proto\"\xb9\x03\n\x17\x46lowableProcessInstance\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x62usinessKey\x18\x03 \x01(\t\x12\x11\n\tsuspended\x18\x04 \x01(\x08\x12\r\n\x05\x65nded\x18\x05 \x01(\x08\x12\x1b\n\x13processDefinitionId\x18\x06 \x01(\t\x12\x1d\n\x15processDefinitionName\x18\x07 \x01(\t\x12$\n\x1cprocessDefinitionDescription\x18\x08 \x01(\t\x12\x12\n\nactivityId\x18\t \x01(\t\x12\x13\n\x0bstartUserId\x18\n \x01(\t\x12\x12\n\ncallbackId\x18\x0b \x01(\t\x12\x14\n\x0c\x63\x61llbackType\x18\x0c \x01(\t\x12\x13\n\x0breferenceId\x18\r \x01(\t\x12\x15\n\rreferenceType\x18\x0e \x01(\t\x12\x10\n\x08tenantId\x18\x0f \x01(\t\x12\x11\n\tcompleted\x18\x10 \x01(\x08\x12\x11\n\tstartTime\x18\x11 \x01(\t\x12\x34\n\tvariables\x18\x12 \x03(\x0b\x32!.flowable.FlowableProcessVariableBDZBgo.easyops.local/contracts/protorepo-models/easyops/model/flowableb\x06proto3')
  ,
  dependencies=[console__gateway__sdk_dot_model_dot_flowable_dot_process__variable__pb2.DESCRIPTOR,])




_FLOWABLEPROCESSINSTANCE = _descriptor.Descriptor(
  name='FlowableProcessInstance',
  full_name='flowable.FlowableProcessInstance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='flowable.FlowableProcessInstance.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='flowable.FlowableProcessInstance.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='businessKey', full_name='flowable.FlowableProcessInstance.businessKey', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='suspended', full_name='flowable.FlowableProcessInstance.suspended', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ended', full_name='flowable.FlowableProcessInstance.ended', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processDefinitionId', full_name='flowable.FlowableProcessInstance.processDefinitionId', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processDefinitionName', full_name='flowable.FlowableProcessInstance.processDefinitionName', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processDefinitionDescription', full_name='flowable.FlowableProcessInstance.processDefinitionDescription', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='activityId', full_name='flowable.FlowableProcessInstance.activityId', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startUserId', full_name='flowable.FlowableProcessInstance.startUserId', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='callbackId', full_name='flowable.FlowableProcessInstance.callbackId', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='callbackType', full_name='flowable.FlowableProcessInstance.callbackType', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='referenceId', full_name='flowable.FlowableProcessInstance.referenceId', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='referenceType', full_name='flowable.FlowableProcessInstance.referenceType', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tenantId', full_name='flowable.FlowableProcessInstance.tenantId', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='completed', full_name='flowable.FlowableProcessInstance.completed', index=15,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='flowable.FlowableProcessInstance.startTime', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='variables', full_name='flowable.FlowableProcessInstance.variables', index=17,
      number=18, type=11, cpp_type=10, label=3,
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
  serialized_start=96,
  serialized_end=537,
)

_FLOWABLEPROCESSINSTANCE.fields_by_name['variables'].message_type = console__gateway__sdk_dot_model_dot_flowable_dot_process__variable__pb2._FLOWABLEPROCESSVARIABLE
DESCRIPTOR.message_types_by_name['FlowableProcessInstance'] = _FLOWABLEPROCESSINSTANCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FlowableProcessInstance = _reflection.GeneratedProtocolMessageType('FlowableProcessInstance', (_message.Message,), {
  'DESCRIPTOR' : _FLOWABLEPROCESSINSTANCE,
  '__module__' : 'process_instance_pb2'
  # @@protoc_insertion_point(class_scope:flowable.FlowableProcessInstance)
  })
_sym_db.RegisterMessage(FlowableProcessInstance)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
