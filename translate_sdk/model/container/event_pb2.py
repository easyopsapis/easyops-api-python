# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: event.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from translate_sdk.model.container import metadata_pb2 as translate__sdk_dot_model_dot_container_dot_metadata__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='event.proto',
  package='container',
  syntax='proto3',
  serialized_options=_b('ZCgo.easyops.local/contracts/protorepo-models/easyops/model/container'),
  serialized_pb=_b('\n\x0b\x65vent.proto\x12\tcontainer\x1a,translate_sdk/model/container/metadata.proto\"\xed\x04\n\x05\x45vent\x12%\n\x08metadata\x18\x01 \x01(\x0b\x32\x13.container.Metadata\x12\x37\n\x0einvolvedObject\x18\x02 \x01(\x0b\x32\x1f.container.Event.InvolvedObject\x12\x0e\n\x06reason\x18\x03 \x01(\t\x12\x0f\n\x07message\x18\x04 \x01(\t\x12\'\n\x06source\x18\x05 \x01(\x0b\x32\x17.container.Event.Source\x12\x16\n\x0e\x66irstTimestamp\x18\x06 \x01(\t\x12\x15\n\rlastTimestamp\x18\x07 \x01(\t\x12\r\n\x05\x63ount\x18\x08 \x01(\x05\x12\x0c\n\x04type\x18\t \x01(\t\x12\x11\n\teventTime\x18\n \x01(\t\x12\'\n\x06series\x18\x0b \x01(\x0b\x32\x17.container.Event.Series\x12\x0e\n\x06\x61\x63tion\x18\x0c \x01(\t\x12\x1a\n\x12reportingComponent\x18\r \x01(\t\x12\x19\n\x11reportingInstance\x18\x0e \x01(\t\x1a\x8c\x01\n\x0eInvolvedObject\x12\x0c\n\x04kind\x18\x01 \x01(\t\x12\x11\n\tnamespace\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0b\n\x03uid\x18\x04 \x01(\t\x12\x12\n\napiVersion\x18\x05 \x01(\t\x12\x17\n\x0fresourceVersion\x18\x06 \x01(\t\x12\x11\n\tfieldPath\x18\x07 \x01(\t\x1a)\n\x06Source\x12\x11\n\tcomponent\x18\x01 \x01(\t\x12\x0c\n\x04host\x18\x02 \x01(\t\x1a\x31\n\x06Series\x12\r\n\x05\x63ount\x18\x01 \x01(\x05\x12\x18\n\x10lastObservedTime\x18\x02 \x01(\tBEZCgo.easyops.local/contracts/protorepo-models/easyops/model/containerb\x06proto3')
  ,
  dependencies=[translate__sdk_dot_model_dot_container_dot_metadata__pb2.DESCRIPTOR,])




_EVENT_INVOLVEDOBJECT = _descriptor.Descriptor(
  name='InvolvedObject',
  full_name='container.Event.InvolvedObject',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='kind', full_name='container.Event.InvolvedObject.kind', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='namespace', full_name='container.Event.InvolvedObject.namespace', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='container.Event.InvolvedObject.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uid', full_name='container.Event.InvolvedObject.uid', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='apiVersion', full_name='container.Event.InvolvedObject.apiVersion', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resourceVersion', full_name='container.Event.InvolvedObject.resourceVersion', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fieldPath', full_name='container.Event.InvolvedObject.fieldPath', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=460,
  serialized_end=600,
)

_EVENT_SOURCE = _descriptor.Descriptor(
  name='Source',
  full_name='container.Event.Source',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='component', full_name='container.Event.Source.component', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host', full_name='container.Event.Source.host', index=1,
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
  serialized_start=602,
  serialized_end=643,
)

_EVENT_SERIES = _descriptor.Descriptor(
  name='Series',
  full_name='container.Event.Series',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='container.Event.Series.count', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastObservedTime', full_name='container.Event.Series.lastObservedTime', index=1,
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
  serialized_start=645,
  serialized_end=694,
)

_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='container.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadata', full_name='container.Event.metadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='involvedObject', full_name='container.Event.involvedObject', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reason', full_name='container.Event.reason', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='container.Event.message', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='container.Event.source', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='firstTimestamp', full_name='container.Event.firstTimestamp', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastTimestamp', full_name='container.Event.lastTimestamp', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='container.Event.count', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='container.Event.type', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eventTime', full_name='container.Event.eventTime', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='series', full_name='container.Event.series', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='container.Event.action', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reportingComponent', full_name='container.Event.reportingComponent', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reportingInstance', full_name='container.Event.reportingInstance', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_EVENT_INVOLVEDOBJECT, _EVENT_SOURCE, _EVENT_SERIES, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=73,
  serialized_end=694,
)

_EVENT_INVOLVEDOBJECT.containing_type = _EVENT
_EVENT_SOURCE.containing_type = _EVENT
_EVENT_SERIES.containing_type = _EVENT
_EVENT.fields_by_name['metadata'].message_type = translate__sdk_dot_model_dot_container_dot_metadata__pb2._METADATA
_EVENT.fields_by_name['involvedObject'].message_type = _EVENT_INVOLVEDOBJECT
_EVENT.fields_by_name['source'].message_type = _EVENT_SOURCE
_EVENT.fields_by_name['series'].message_type = _EVENT_SERIES
DESCRIPTOR.message_types_by_name['Event'] = _EVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), {

  'InvolvedObject' : _reflection.GeneratedProtocolMessageType('InvolvedObject', (_message.Message,), {
    'DESCRIPTOR' : _EVENT_INVOLVEDOBJECT,
    '__module__' : 'event_pb2'
    # @@protoc_insertion_point(class_scope:container.Event.InvolvedObject)
    })
  ,

  'Source' : _reflection.GeneratedProtocolMessageType('Source', (_message.Message,), {
    'DESCRIPTOR' : _EVENT_SOURCE,
    '__module__' : 'event_pb2'
    # @@protoc_insertion_point(class_scope:container.Event.Source)
    })
  ,

  'Series' : _reflection.GeneratedProtocolMessageType('Series', (_message.Message,), {
    'DESCRIPTOR' : _EVENT_SERIES,
    '__module__' : 'event_pb2'
    # @@protoc_insertion_point(class_scope:container.Event.Series)
    })
  ,
  'DESCRIPTOR' : _EVENT,
  '__module__' : 'event_pb2'
  # @@protoc_insertion_point(class_scope:container.Event)
  })
_sym_db.RegisterMessage(Event)
_sym_db.RegisterMessage(Event.InvolvedObject)
_sym_db.RegisterMessage(Event.Source)
_sym_db.RegisterMessage(Event.Series)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
