# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: container_state.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='container_state.proto',
  package='container',
  syntax='proto3',
  serialized_options=_b('ZCgo.easyops.local/contracts/protorepo-models/easyops/model/container'),
  serialized_pb=_b('\n\x15\x63ontainer_state.proto\x12\tcontainer\"\xab\x02\n\x0e\x43ontainerState\x12\x32\n\x07waiting\x18\x01 \x01(\x0b\x32!.container.ContainerState.Waiting\x12\x32\n\x07running\x18\x02 \x01(\x0b\x32!.container.ContainerState.Running\x12\x38\n\nterminated\x18\x03 \x01(\x0b\x32$.container.ContainerState.Terminated\x1a*\n\x07Waiting\x12\x0e\n\x06reason\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x1a\x1c\n\x07Running\x12\x11\n\tstartedAt\x18\x01 \x01(\t\x1a-\n\nTerminated\x12\x0e\n\x06reason\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\tBEZCgo.easyops.local/contracts/protorepo-models/easyops/model/containerb\x06proto3')
)




_CONTAINERSTATE_WAITING = _descriptor.Descriptor(
  name='Waiting',
  full_name='container.ContainerState.Waiting',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reason', full_name='container.ContainerState.Waiting.reason', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='container.ContainerState.Waiting.message', index=1,
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
  serialized_start=217,
  serialized_end=259,
)

_CONTAINERSTATE_RUNNING = _descriptor.Descriptor(
  name='Running',
  full_name='container.ContainerState.Running',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='startedAt', full_name='container.ContainerState.Running.startedAt', index=0,
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
  serialized_start=261,
  serialized_end=289,
)

_CONTAINERSTATE_TERMINATED = _descriptor.Descriptor(
  name='Terminated',
  full_name='container.ContainerState.Terminated',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reason', full_name='container.ContainerState.Terminated.reason', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='container.ContainerState.Terminated.message', index=1,
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
  serialized_start=291,
  serialized_end=336,
)

_CONTAINERSTATE = _descriptor.Descriptor(
  name='ContainerState',
  full_name='container.ContainerState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='waiting', full_name='container.ContainerState.waiting', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='running', full_name='container.ContainerState.running', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='terminated', full_name='container.ContainerState.terminated', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CONTAINERSTATE_WAITING, _CONTAINERSTATE_RUNNING, _CONTAINERSTATE_TERMINATED, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=336,
)

_CONTAINERSTATE_WAITING.containing_type = _CONTAINERSTATE
_CONTAINERSTATE_RUNNING.containing_type = _CONTAINERSTATE
_CONTAINERSTATE_TERMINATED.containing_type = _CONTAINERSTATE
_CONTAINERSTATE.fields_by_name['waiting'].message_type = _CONTAINERSTATE_WAITING
_CONTAINERSTATE.fields_by_name['running'].message_type = _CONTAINERSTATE_RUNNING
_CONTAINERSTATE.fields_by_name['terminated'].message_type = _CONTAINERSTATE_TERMINATED
DESCRIPTOR.message_types_by_name['ContainerState'] = _CONTAINERSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ContainerState = _reflection.GeneratedProtocolMessageType('ContainerState', (_message.Message,), {

  'Waiting' : _reflection.GeneratedProtocolMessageType('Waiting', (_message.Message,), {
    'DESCRIPTOR' : _CONTAINERSTATE_WAITING,
    '__module__' : 'container_state_pb2'
    # @@protoc_insertion_point(class_scope:container.ContainerState.Waiting)
    })
  ,

  'Running' : _reflection.GeneratedProtocolMessageType('Running', (_message.Message,), {
    'DESCRIPTOR' : _CONTAINERSTATE_RUNNING,
    '__module__' : 'container_state_pb2'
    # @@protoc_insertion_point(class_scope:container.ContainerState.Running)
    })
  ,

  'Terminated' : _reflection.GeneratedProtocolMessageType('Terminated', (_message.Message,), {
    'DESCRIPTOR' : _CONTAINERSTATE_TERMINATED,
    '__module__' : 'container_state_pb2'
    # @@protoc_insertion_point(class_scope:container.ContainerState.Terminated)
    })
  ,
  'DESCRIPTOR' : _CONTAINERSTATE,
  '__module__' : 'container_state_pb2'
  # @@protoc_insertion_point(class_scope:container.ContainerState)
  })
_sym_db.RegisterMessage(ContainerState)
_sym_db.RegisterMessage(ContainerState.Waiting)
_sym_db.RegisterMessage(ContainerState.Running)
_sym_db.RegisterMessage(ContainerState.Terminated)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
