# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stateWorkflow.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cmdb_extend_sdk.model.state_workflow import state_pb2 as cmdb__extend__sdk_dot_model_dot_state__workflow_dot_state__pb2
from cmdb_extend_sdk.model.state_workflow import transition_pb2 as cmdb__extend__sdk_dot_model_dot_state__workflow_dot_transition__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='stateWorkflow.proto',
  package='state_workflow',
  syntax='proto3',
  serialized_options=_b('ZHgo.easyops.local/contracts/protorepo-models/easyops/model/state_workflow'),
  serialized_pb=_b('\n\x13stateWorkflow.proto\x12\x0estate_workflow\x1a\x30\x63mdb_extend_sdk/model/state_workflow/state.proto\x1a\x35\x63mdb_extend_sdk/model/state_workflow/transition.proto\"\xeb\x04\n\rStateWorkflow\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12<\n\nobjectInfo\x18\x03 \x01(\x0b\x32(.state_workflow.StateWorkflow.ObjectInfo\x12%\n\x06states\x18\x04 \x03(\x0b\x32\x15.state_workflow.State\x12\x42\n\rstateTriggers\x18\x05 \x03(\x0b\x32+.state_workflow.StateWorkflow.StateTriggers\x12/\n\x0btransitions\x18\x06 \x03(\x0b\x32\x1a.state_workflow.Transition\x12L\n\x12transitionTriggers\x18\x07 \x03(\x0b\x32\x30.state_workflow.StateWorkflow.TransitionTriggers\x12\x0c\n\x04memo\x18\x08 \x01(\t\x1a\x41\n\nObjectInfo\x12\x10\n\x08objectId\x18\x01 \x01(\t\x12\x11\n\tattribute\x18\x02 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x03 \x01(\t\x1a\\\n\rStateTriggers\x12\r\n\x05\x65vent\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x13\n\x0b\x63\x61llbackUri\x18\x03 \x01(\t\x12\x1b\n\x13\x63\x61llbackServiceName\x18\x04 \x01(\t\x1a\x61\n\x12TransitionTriggers\x12\r\n\x05\x65vent\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x13\n\x0b\x63\x61llbackUri\x18\x03 \x01(\t\x12\x1b\n\x13\x63\x61llbackServiceName\x18\x04 \x01(\tBJZHgo.easyops.local/contracts/protorepo-models/easyops/model/state_workflowb\x06proto3')
  ,
  dependencies=[cmdb__extend__sdk_dot_model_dot_state__workflow_dot_state__pb2.DESCRIPTOR,cmdb__extend__sdk_dot_model_dot_state__workflow_dot_transition__pb2.DESCRIPTOR,])




_STATEWORKFLOW_OBJECTINFO = _descriptor.Descriptor(
  name='ObjectInfo',
  full_name='state_workflow.StateWorkflow.ObjectInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='objectId', full_name='state_workflow.StateWorkflow.ObjectInfo.objectId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attribute', full_name='state_workflow.StateWorkflow.ObjectInfo.attribute', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter', full_name='state_workflow.StateWorkflow.ObjectInfo.filter', index=2,
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
  serialized_start=506,
  serialized_end=571,
)

_STATEWORKFLOW_STATETRIGGERS = _descriptor.Descriptor(
  name='StateTriggers',
  full_name='state_workflow.StateWorkflow.StateTriggers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event', full_name='state_workflow.StateWorkflow.StateTriggers.event', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='state_workflow.StateWorkflow.StateTriggers.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='callbackUri', full_name='state_workflow.StateWorkflow.StateTriggers.callbackUri', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='callbackServiceName', full_name='state_workflow.StateWorkflow.StateTriggers.callbackServiceName', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=573,
  serialized_end=665,
)

_STATEWORKFLOW_TRANSITIONTRIGGERS = _descriptor.Descriptor(
  name='TransitionTriggers',
  full_name='state_workflow.StateWorkflow.TransitionTriggers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event', full_name='state_workflow.StateWorkflow.TransitionTriggers.event', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='state_workflow.StateWorkflow.TransitionTriggers.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='callbackUri', full_name='state_workflow.StateWorkflow.TransitionTriggers.callbackUri', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='callbackServiceName', full_name='state_workflow.StateWorkflow.TransitionTriggers.callbackServiceName', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=667,
  serialized_end=764,
)

_STATEWORKFLOW = _descriptor.Descriptor(
  name='StateWorkflow',
  full_name='state_workflow.StateWorkflow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='state_workflow.StateWorkflow.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='state_workflow.StateWorkflow.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectInfo', full_name='state_workflow.StateWorkflow.objectInfo', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='states', full_name='state_workflow.StateWorkflow.states', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stateTriggers', full_name='state_workflow.StateWorkflow.stateTriggers', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transitions', full_name='state_workflow.StateWorkflow.transitions', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transitionTriggers', full_name='state_workflow.StateWorkflow.transitionTriggers', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='state_workflow.StateWorkflow.memo', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_STATEWORKFLOW_OBJECTINFO, _STATEWORKFLOW_STATETRIGGERS, _STATEWORKFLOW_TRANSITIONTRIGGERS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=145,
  serialized_end=764,
)

_STATEWORKFLOW_OBJECTINFO.containing_type = _STATEWORKFLOW
_STATEWORKFLOW_STATETRIGGERS.containing_type = _STATEWORKFLOW
_STATEWORKFLOW_TRANSITIONTRIGGERS.containing_type = _STATEWORKFLOW
_STATEWORKFLOW.fields_by_name['objectInfo'].message_type = _STATEWORKFLOW_OBJECTINFO
_STATEWORKFLOW.fields_by_name['states'].message_type = cmdb__extend__sdk_dot_model_dot_state__workflow_dot_state__pb2._STATE
_STATEWORKFLOW.fields_by_name['stateTriggers'].message_type = _STATEWORKFLOW_STATETRIGGERS
_STATEWORKFLOW.fields_by_name['transitions'].message_type = cmdb__extend__sdk_dot_model_dot_state__workflow_dot_transition__pb2._TRANSITION
_STATEWORKFLOW.fields_by_name['transitionTriggers'].message_type = _STATEWORKFLOW_TRANSITIONTRIGGERS
DESCRIPTOR.message_types_by_name['StateWorkflow'] = _STATEWORKFLOW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StateWorkflow = _reflection.GeneratedProtocolMessageType('StateWorkflow', (_message.Message,), {

  'ObjectInfo' : _reflection.GeneratedProtocolMessageType('ObjectInfo', (_message.Message,), {
    'DESCRIPTOR' : _STATEWORKFLOW_OBJECTINFO,
    '__module__' : 'stateWorkflow_pb2'
    # @@protoc_insertion_point(class_scope:state_workflow.StateWorkflow.ObjectInfo)
    })
  ,

  'StateTriggers' : _reflection.GeneratedProtocolMessageType('StateTriggers', (_message.Message,), {
    'DESCRIPTOR' : _STATEWORKFLOW_STATETRIGGERS,
    '__module__' : 'stateWorkflow_pb2'
    # @@protoc_insertion_point(class_scope:state_workflow.StateWorkflow.StateTriggers)
    })
  ,

  'TransitionTriggers' : _reflection.GeneratedProtocolMessageType('TransitionTriggers', (_message.Message,), {
    'DESCRIPTOR' : _STATEWORKFLOW_TRANSITIONTRIGGERS,
    '__module__' : 'stateWorkflow_pb2'
    # @@protoc_insertion_point(class_scope:state_workflow.StateWorkflow.TransitionTriggers)
    })
  ,
  'DESCRIPTOR' : _STATEWORKFLOW,
  '__module__' : 'stateWorkflow_pb2'
  # @@protoc_insertion_point(class_scope:state_workflow.StateWorkflow)
  })
_sym_db.RegisterMessage(StateWorkflow)
_sym_db.RegisterMessage(StateWorkflow.ObjectInfo)
_sym_db.RegisterMessage(StateWorkflow.StateTriggers)
_sym_db.RegisterMessage(StateWorkflow.TransitionTriggers)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
