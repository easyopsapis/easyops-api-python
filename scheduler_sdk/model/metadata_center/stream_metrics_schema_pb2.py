# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stream_metrics_schema.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from scheduler_sdk.model.metadata_center import stream_metrics_schema_field_pb2 as scheduler__sdk_dot_model_dot_metadata__center_dot_stream__metrics__schema__field__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='stream_metrics_schema.proto',
  package='metadata_center',
  syntax='proto3',
  serialized_options=_b('ZIgo.easyops.local/contracts/protorepo-models/easyops/model/metadata_center'),
  serialized_pb=_b('\n\x1bstream_metrics_schema.proto\x12\x0fmetadata_center\x1a\x45scheduler_sdk/model/metadata_center/stream_metrics_schema_field.proto\"\xc8\x01\n\x13StreamMetricsSchema\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03org\x18\x02 \x01(\x05\x12\x0f\n\x07version\x18\x03 \x01(\x05\x12\x0c\n\x04name\x18\x04 \x01(\t\x12=\n\ndimensions\x18\x05 \x03(\x0b\x32).metadata_center.StreamMetricsSchemaField\x12:\n\x07metrics\x18\x06 \x03(\x0b\x32).metadata_center.StreamMetricsSchemaFieldBKZIgo.easyops.local/contracts/protorepo-models/easyops/model/metadata_centerb\x06proto3')
  ,
  dependencies=[scheduler__sdk_dot_model_dot_metadata__center_dot_stream__metrics__schema__field__pb2.DESCRIPTOR,])




_STREAMMETRICSSCHEMA = _descriptor.Descriptor(
  name='StreamMetricsSchema',
  full_name='metadata_center.StreamMetricsSchema',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='metadata_center.StreamMetricsSchema.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org', full_name='metadata_center.StreamMetricsSchema.org', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='metadata_center.StreamMetricsSchema.version', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='metadata_center.StreamMetricsSchema.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dimensions', full_name='metadata_center.StreamMetricsSchema.dimensions', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metrics', full_name='metadata_center.StreamMetricsSchema.metrics', index=5,
      number=6, type=11, cpp_type=10, label=3,
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
  serialized_start=120,
  serialized_end=320,
)

_STREAMMETRICSSCHEMA.fields_by_name['dimensions'].message_type = scheduler__sdk_dot_model_dot_metadata__center_dot_stream__metrics__schema__field__pb2._STREAMMETRICSSCHEMAFIELD
_STREAMMETRICSSCHEMA.fields_by_name['metrics'].message_type = scheduler__sdk_dot_model_dot_metadata__center_dot_stream__metrics__schema__field__pb2._STREAMMETRICSSCHEMAFIELD
DESCRIPTOR.message_types_by_name['StreamMetricsSchema'] = _STREAMMETRICSSCHEMA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StreamMetricsSchema = _reflection.GeneratedProtocolMessageType('StreamMetricsSchema', (_message.Message,), {
  'DESCRIPTOR' : _STREAMMETRICSSCHEMA,
  '__module__' : 'stream_metrics_schema_pb2'
  # @@protoc_insertion_point(class_scope:metadata_center.StreamMetricsSchema)
  })
_sym_db.RegisterMessage(StreamMetricsSchema)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
