# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: alias_metric_with_one_original_metric.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from notify_sdk.model.collector_service import metric_pb2 as notify__sdk_dot_model_dot_collector__service_dot_metric__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='alias_metric_with_one_original_metric.proto',
  package='collector_service',
  syntax='proto3',
  serialized_options=_b('ZKgo.easyops.local/contracts/protorepo-models/easyops/model/collector_service'),
  serialized_pb=_b('\n+alias_metric_with_one_original_metric.proto\x12\x11\x63ollector_service\x1a/notify_sdk/model/collector_service/metric.proto\"\xb5\x03\n*CollectorAliasMetricWithOneOiriginalMetric\x12\x15\n\rcalculateOnly\x18\x01 \x01(\x08\x12;\n\x0f\x63ollectorMetric\x18\x02 \x01(\x0b\x32\".collector_service.CollectorMetric\x12T\n\rdependMetrics\x18\x03 \x03(\x0b\x32=.collector_service.CollectorAliasMetricWithOneOiriginalMetric\x12\x12\n\ninstanceId\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12P\n\x04\x64ims\x18\x06 \x03(\x0b\x32\x42.collector_service.CollectorAliasMetricWithOneOiriginalMetric.Dims\x12\x0f\n\x07version\x18\x07 \x01(\x05\x12\x14\n\x0cisCalculated\x18\x08 \x01(\x08\x12\x12\n\nexpression\x18\t \x01(\t\x1a.\n\x04\x44ims\x12\x0f\n\x07\x64imName\x18\x01 \x01(\t\x12\x15\n\roriginDimName\x18\x02 \x01(\tBMZKgo.easyops.local/contracts/protorepo-models/easyops/model/collector_serviceb\x06proto3')
  ,
  dependencies=[notify__sdk_dot_model_dot_collector__service_dot_metric__pb2.DESCRIPTOR,])




_COLLECTORALIASMETRICWITHONEOIRIGINALMETRIC_DIMS = _descriptor.Descriptor(
  name='Dims',
  full_name='collector_service.CollectorAliasMetricWithOneOiriginalMetric.Dims',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dimName', full_name='collector_service.CollectorAliasMetricWithOneOiriginalMetric.Dims.dimName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='originDimName', full_name='collector_service.CollectorAliasMetricWithOneOiriginalMetric.Dims.originDimName', index=1,
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
  serialized_start=507,
  serialized_end=553,
)

_COLLECTORALIASMETRICWITHONEOIRIGINALMETRIC = _descriptor.Descriptor(
  name='CollectorAliasMetricWithOneOiriginalMetric',
  full_name='collector_service.CollectorAliasMetricWithOneOiriginalMetric',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='calculateOnly', full_name='collector_service.CollectorAliasMetricWithOneOiriginalMetric.calculateOnly', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collectorMetric', full_name='collector_service.CollectorAliasMetricWithOneOiriginalMetric.collectorMetric', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dependMetrics', full_name='collector_service.CollectorAliasMetricWithOneOiriginalMetric.dependMetrics', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='collector_service.CollectorAliasMetricWithOneOiriginalMetric.instanceId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='collector_service.CollectorAliasMetricWithOneOiriginalMetric.name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dims', full_name='collector_service.CollectorAliasMetricWithOneOiriginalMetric.dims', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='collector_service.CollectorAliasMetricWithOneOiriginalMetric.version', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isCalculated', full_name='collector_service.CollectorAliasMetricWithOneOiriginalMetric.isCalculated', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expression', full_name='collector_service.CollectorAliasMetricWithOneOiriginalMetric.expression', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_COLLECTORALIASMETRICWITHONEOIRIGINALMETRIC_DIMS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=116,
  serialized_end=553,
)

_COLLECTORALIASMETRICWITHONEOIRIGINALMETRIC_DIMS.containing_type = _COLLECTORALIASMETRICWITHONEOIRIGINALMETRIC
_COLLECTORALIASMETRICWITHONEOIRIGINALMETRIC.fields_by_name['collectorMetric'].message_type = notify__sdk_dot_model_dot_collector__service_dot_metric__pb2._COLLECTORMETRIC
_COLLECTORALIASMETRICWITHONEOIRIGINALMETRIC.fields_by_name['dependMetrics'].message_type = _COLLECTORALIASMETRICWITHONEOIRIGINALMETRIC
_COLLECTORALIASMETRICWITHONEOIRIGINALMETRIC.fields_by_name['dims'].message_type = _COLLECTORALIASMETRICWITHONEOIRIGINALMETRIC_DIMS
DESCRIPTOR.message_types_by_name['CollectorAliasMetricWithOneOiriginalMetric'] = _COLLECTORALIASMETRICWITHONEOIRIGINALMETRIC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CollectorAliasMetricWithOneOiriginalMetric = _reflection.GeneratedProtocolMessageType('CollectorAliasMetricWithOneOiriginalMetric', (_message.Message,), {

  'Dims' : _reflection.GeneratedProtocolMessageType('Dims', (_message.Message,), {
    'DESCRIPTOR' : _COLLECTORALIASMETRICWITHONEOIRIGINALMETRIC_DIMS,
    '__module__' : 'alias_metric_with_one_original_metric_pb2'
    # @@protoc_insertion_point(class_scope:collector_service.CollectorAliasMetricWithOneOiriginalMetric.Dims)
    })
  ,
  'DESCRIPTOR' : _COLLECTORALIASMETRICWITHONEOIRIGINALMETRIC,
  '__module__' : 'alias_metric_with_one_original_metric_pb2'
  # @@protoc_insertion_point(class_scope:collector_service.CollectorAliasMetricWithOneOiriginalMetric)
  })
_sym_db.RegisterMessage(CollectorAliasMetricWithOneOiriginalMetric)
_sym_db.RegisterMessage(CollectorAliasMetricWithOneOiriginalMetric.Dims)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
