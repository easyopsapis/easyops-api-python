# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: callback.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='callback.proto',
  package='state_workflow',
  syntax='proto3',
  serialized_options=_b('ZHgo.easyops.local/contracts/protorepo-models/easyops/model/state_workflow'),
  serialized_pb=_b('\n\x0e\x63\x61llback.proto\x12\x0estate_workflow\"Q\n\rStateCallback\x12\x13\n\x0b\x63\x61llbackUri\x18\x01 \x01(\t\x12\x1b\n\x13\x63\x61llbackServiceName\x18\x02 \x01(\t\x12\x0e\n\x06result\x18\x03 \x01(\x08\x42JZHgo.easyops.local/contracts/protorepo-models/easyops/model/state_workflowb\x06proto3')
)




_STATECALLBACK = _descriptor.Descriptor(
  name='StateCallback',
  full_name='state_workflow.StateCallback',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='callbackUri', full_name='state_workflow.StateCallback.callbackUri', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='callbackServiceName', full_name='state_workflow.StateCallback.callbackServiceName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result', full_name='state_workflow.StateCallback.result', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=34,
  serialized_end=115,
)

DESCRIPTOR.message_types_by_name['StateCallback'] = _STATECALLBACK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StateCallback = _reflection.GeneratedProtocolMessageType('StateCallback', (_message.Message,), {
  'DESCRIPTOR' : _STATECALLBACK,
  '__module__' : 'callback_pb2'
  # @@protoc_insertion_point(class_scope:state_workflow.StateCallback)
  })
_sym_db.RegisterMessage(StateCallback)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)