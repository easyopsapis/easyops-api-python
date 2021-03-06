# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list_event.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from container_sdk.model.container import event_pb2 as container__sdk_dot_model_dot_container_dot_event__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='list_event.proto',
  package='workload',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10list_event.proto\x12\x08workload\x1a)container_sdk/model/container/event.proto\"B\n\x10ListEventRequest\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0c\n\x04kind\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\"c\n\x11ListEventResponse\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12\x1e\n\x04list\x18\x04 \x03(\x0b\x32\x10.container.Event\"w\n\x18ListEventResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12)\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1b.workload.ListEventResponseb\x06proto3')
  ,
  dependencies=[container__sdk_dot_model_dot_container_dot_event__pb2.DESCRIPTOR,])




_LISTEVENTREQUEST = _descriptor.Descriptor(
  name='ListEventRequest',
  full_name='workload.ListEventRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='workload.ListEventRequest.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kind', full_name='workload.ListEventRequest.kind', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='workload.ListEventRequest.type', index=2,
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
  serialized_start=73,
  serialized_end=139,
)


_LISTEVENTRESPONSE = _descriptor.Descriptor(
  name='ListEventResponse',
  full_name='workload.ListEventResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='workload.ListEventResponse.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='workload.ListEventResponse.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='workload.ListEventResponse.total', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='workload.ListEventResponse.list', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=141,
  serialized_end=240,
)


_LISTEVENTRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListEventResponseWrapper',
  full_name='workload.ListEventResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='workload.ListEventResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='workload.ListEventResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='workload.ListEventResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='workload.ListEventResponseWrapper.data', index=3,
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
  serialized_start=242,
  serialized_end=361,
)

_LISTEVENTRESPONSE.fields_by_name['list'].message_type = container__sdk_dot_model_dot_container_dot_event__pb2._EVENT
_LISTEVENTRESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTEVENTRESPONSE
DESCRIPTOR.message_types_by_name['ListEventRequest'] = _LISTEVENTREQUEST
DESCRIPTOR.message_types_by_name['ListEventResponse'] = _LISTEVENTRESPONSE
DESCRIPTOR.message_types_by_name['ListEventResponseWrapper'] = _LISTEVENTRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListEventRequest = _reflection.GeneratedProtocolMessageType('ListEventRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTEVENTREQUEST,
  '__module__' : 'list_event_pb2'
  # @@protoc_insertion_point(class_scope:workload.ListEventRequest)
  })
_sym_db.RegisterMessage(ListEventRequest)

ListEventResponse = _reflection.GeneratedProtocolMessageType('ListEventResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTEVENTRESPONSE,
  '__module__' : 'list_event_pb2'
  # @@protoc_insertion_point(class_scope:workload.ListEventResponse)
  })
_sym_db.RegisterMessage(ListEventResponse)

ListEventResponseWrapper = _reflection.GeneratedProtocolMessageType('ListEventResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _LISTEVENTRESPONSEWRAPPER,
  '__module__' : 'list_event_pb2'
  # @@protoc_insertion_point(class_scope:workload.ListEventResponseWrapper)
  })
_sym_db.RegisterMessage(ListEventResponseWrapper)


# @@protoc_insertion_point(module_scope)
