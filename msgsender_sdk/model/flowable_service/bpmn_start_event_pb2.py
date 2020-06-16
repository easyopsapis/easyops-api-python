# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bpmn_start_event.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from msgsender_sdk.model.flowable_service import bpmn_links_pb2 as msgsender__sdk_dot_model_dot_flowable__service_dot_bpmn__links__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bpmn_start_event.proto',
  package='flowable_service',
  syntax='proto3',
  serialized_options=_b('ZJgo.easyops.local/contracts/protorepo-models/easyops/model/flowable_service'),
  serialized_pb=_b('\n\x16\x62pmn_start_event.proto\x12\x10\x66lowable_service\x1a\x35msgsender_sdk/model/flowable_service/bpmn_links.proto\"H\n\x0e\x42PMNStartEvent\x12\n\n\x02id\x18\x01 \x01(\t\x12*\n\x05links\x18\x02 \x01(\x0b\x32\x1b.flowable_service.BPMNLinksBLZJgo.easyops.local/contracts/protorepo-models/easyops/model/flowable_serviceb\x06proto3')
  ,
  dependencies=[msgsender__sdk_dot_model_dot_flowable__service_dot_bpmn__links__pb2.DESCRIPTOR,])




_BPMNSTARTEVENT = _descriptor.Descriptor(
  name='BPMNStartEvent',
  full_name='flowable_service.BPMNStartEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='flowable_service.BPMNStartEvent.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='links', full_name='flowable_service.BPMNStartEvent.links', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=99,
  serialized_end=171,
)

_BPMNSTARTEVENT.fields_by_name['links'].message_type = msgsender__sdk_dot_model_dot_flowable__service_dot_bpmn__links__pb2._BPMNLINKS
DESCRIPTOR.message_types_by_name['BPMNStartEvent'] = _BPMNSTARTEVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BPMNStartEvent = _reflection.GeneratedProtocolMessageType('BPMNStartEvent', (_message.Message,), {
  'DESCRIPTOR' : _BPMNSTARTEVENT,
  '__module__' : 'bpmn_start_event_pb2'
  # @@protoc_insertion_point(class_scope:flowable_service.BPMNStartEvent)
  })
_sym_db.RegisterMessage(BPMNStartEvent)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
