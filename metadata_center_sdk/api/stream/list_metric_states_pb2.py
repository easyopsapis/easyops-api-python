# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list_metric_states.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from metadata_center_sdk.model.metadata_center import stream_metric_schema_pb2 as metadata__center__sdk_dot_model_dot_metadata__center_dot_stream__metric__schema__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='list_metric_states.proto',
  package='stream',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x18list_metric_states.proto\x12\x06stream\x1a\x44metadata_center_sdk/model/metadata_center/stream_metric_schema.proto\"O\n\x18ListMetricStatesResponse\x12\x33\n\x06states\x18\x01 \x03(\x0b\x32#.metadata_center.StreamMetricSchema\"\x83\x01\n\x1fListMetricStatesResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12.\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32 .stream.ListMetricStatesResponseb\x06proto3')
  ,
  dependencies=[metadata__center__sdk_dot_model_dot_metadata__center_dot_stream__metric__schema__pb2.DESCRIPTOR,])




_LISTMETRICSTATESRESPONSE = _descriptor.Descriptor(
  name='ListMetricStatesResponse',
  full_name='stream.ListMetricStatesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='states', full_name='stream.ListMetricStatesResponse.states', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=106,
  serialized_end=185,
)


_LISTMETRICSTATESRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListMetricStatesResponseWrapper',
  full_name='stream.ListMetricStatesResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='stream.ListMetricStatesResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='stream.ListMetricStatesResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='stream.ListMetricStatesResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='stream.ListMetricStatesResponseWrapper.data', index=3,
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
  serialized_start=188,
  serialized_end=319,
)

_LISTMETRICSTATESRESPONSE.fields_by_name['states'].message_type = metadata__center__sdk_dot_model_dot_metadata__center_dot_stream__metric__schema__pb2._STREAMMETRICSCHEMA
_LISTMETRICSTATESRESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTMETRICSTATESRESPONSE
DESCRIPTOR.message_types_by_name['ListMetricStatesResponse'] = _LISTMETRICSTATESRESPONSE
DESCRIPTOR.message_types_by_name['ListMetricStatesResponseWrapper'] = _LISTMETRICSTATESRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListMetricStatesResponse = _reflection.GeneratedProtocolMessageType('ListMetricStatesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTMETRICSTATESRESPONSE,
  '__module__' : 'list_metric_states_pb2'
  # @@protoc_insertion_point(class_scope:stream.ListMetricStatesResponse)
  })
_sym_db.RegisterMessage(ListMetricStatesResponse)

ListMetricStatesResponseWrapper = _reflection.GeneratedProtocolMessageType('ListMetricStatesResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _LISTMETRICSTATESRESPONSEWRAPPER,
  '__module__' : 'list_metric_states_pb2'
  # @@protoc_insertion_point(class_scope:stream.ListMetricStatesResponseWrapper)
  })
_sym_db.RegisterMessage(ListMetricStatesResponseWrapper)


# @@protoc_insertion_point(module_scope)
