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


from assets_inventory_sdk.model.flowable import process_variable_pb2 as assets__inventory__sdk_dot_model_dot_flowable_dot_process__variable__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='task.proto',
  package='flowable',
  syntax='proto3',
  serialized_options=_b('ZBgo.easyops.local/contracts/protorepo-models/easyops/model/flowable'),
  serialized_pb=_b('\n\ntask.proto\x12\x08\x66lowable\x1a:assets_inventory_sdk/model/flowable/process_variable.proto\"\xd9\x04\n\x0c\x46lowableTask\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\r\n\x05owner\x18\x03 \x01(\t\x12\x10\n\x08\x61ssignee\x18\x04 \x01(\t\x12\x17\n\x0f\x64\x65legationState\x18\x05 \x01(\t\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x07 \x01(\t\x12\x12\n\ncreateTime\x18\x08 \x01(\t\x12\x0f\n\x07\x64ueDate\x18\t \x01(\t\x12\x10\n\x08priority\x18\n \x01(\x05\x12\x11\n\tsuspended\x18\x0b \x01(\x08\x12\x11\n\tclaimTime\x18\x0c \x01(\t\x12\x19\n\x11taskDefinitionKey\x18\r \x01(\t\x12\x19\n\x11scopeDefinitionId\x18\x0e \x01(\t\x12\x0f\n\x07scopeId\x18\x0f \x01(\t\x12\x11\n\tscopeType\x18\x10 \x01(\t\x12\x10\n\x08tenantId\x18\x11 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x12 \x01(\t\x12\x0f\n\x07\x66ormKey\x18\x13 \x01(\t\x12\x14\n\x0cparentTaskId\x18\x14 \x01(\t\x12\x13\n\x0b\x65xecutionId\x18\x15 \x01(\t\x12\x14\n\x0c\x65xecutionUrl\x18\x16 \x01(\t\x12\x19\n\x11processInstanceId\x18\x17 \x01(\t\x12\x1a\n\x12processInstanceUrl\x18\x18 \x01(\t\x12\x1b\n\x13processDefinitionId\x18\x19 \x01(\t\x12\x1c\n\x14processDefinitionUrl\x18\x1a \x01(\t\x12\x34\n\tvariables\x18\x1b \x03(\x0b\x32!.flowable.FlowableProcessVariableBDZBgo.easyops.local/contracts/protorepo-models/easyops/model/flowableb\x06proto3')
  ,
  dependencies=[assets__inventory__sdk_dot_model_dot_flowable_dot_process__variable__pb2.DESCRIPTOR,])




_FLOWABLETASK = _descriptor.Descriptor(
  name='FlowableTask',
  full_name='flowable.FlowableTask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='flowable.FlowableTask.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='flowable.FlowableTask.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='owner', full_name='flowable.FlowableTask.owner', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='assignee', full_name='flowable.FlowableTask.assignee', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delegationState', full_name='flowable.FlowableTask.delegationState', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='flowable.FlowableTask.name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='flowable.FlowableTask.description', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='createTime', full_name='flowable.FlowableTask.createTime', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dueDate', full_name='flowable.FlowableTask.dueDate', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='priority', full_name='flowable.FlowableTask.priority', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='suspended', full_name='flowable.FlowableTask.suspended', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='claimTime', full_name='flowable.FlowableTask.claimTime', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='taskDefinitionKey', full_name='flowable.FlowableTask.taskDefinitionKey', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scopeDefinitionId', full_name='flowable.FlowableTask.scopeDefinitionId', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scopeId', full_name='flowable.FlowableTask.scopeId', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scopeType', full_name='flowable.FlowableTask.scopeType', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tenantId', full_name='flowable.FlowableTask.tenantId', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='flowable.FlowableTask.category', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='formKey', full_name='flowable.FlowableTask.formKey', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parentTaskId', full_name='flowable.FlowableTask.parentTaskId', index=19,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='executionId', full_name='flowable.FlowableTask.executionId', index=20,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='executionUrl', full_name='flowable.FlowableTask.executionUrl', index=21,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processInstanceId', full_name='flowable.FlowableTask.processInstanceId', index=22,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processInstanceUrl', full_name='flowable.FlowableTask.processInstanceUrl', index=23,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processDefinitionId', full_name='flowable.FlowableTask.processDefinitionId', index=24,
      number=25, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processDefinitionUrl', full_name='flowable.FlowableTask.processDefinitionUrl', index=25,
      number=26, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='variables', full_name='flowable.FlowableTask.variables', index=26,
      number=27, type=11, cpp_type=10, label=3,
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
  serialized_start=85,
  serialized_end=686,
)

_FLOWABLETASK.fields_by_name['variables'].message_type = assets__inventory__sdk_dot_model_dot_flowable_dot_process__variable__pb2._FLOWABLEPROCESSVARIABLE
DESCRIPTOR.message_types_by_name['FlowableTask'] = _FLOWABLETASK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FlowableTask = _reflection.GeneratedProtocolMessageType('FlowableTask', (_message.Message,), {
  'DESCRIPTOR' : _FLOWABLETASK,
  '__module__' : 'task_pb2'
  # @@protoc_insertion_point(class_scope:flowable.FlowableTask)
  })
_sym_db.RegisterMessage(FlowableTask)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
