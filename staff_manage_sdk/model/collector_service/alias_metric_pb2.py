# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: alias_metric.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from staff_manage_sdk.model.collector_service import metric_pb2 as staff__manage__sdk_dot_model_dot_collector__service_dot_metric__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='alias_metric.proto',
  package='collector_service',
  syntax='proto3',
  serialized_options=_b('ZKgo.easyops.local/contracts/protorepo-models/easyops/model/collector_service'),
  serialized_pb=_b('\n\x12\x61lias_metric.proto\x12\x11\x63ollector_service\x1a\x35staff_manage_sdk/model/collector_service/metric.proto\"\x98\x03\n\x14\x43ollectorAliasMetric\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12:\n\x04\x64ims\x18\x03 \x03(\x0b\x32,.collector_service.CollectorAliasMetric.Dims\x12\x0f\n\x07version\x18\x04 \x01(\x05\x12\x13\n\x0bisKeyMetric\x18\x05 \x01(\x08\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\x10\n\x08objectId\x18\x07 \x01(\t\x12;\n\x0foriginalMetrics\x18\x08 \x03(\x0b\x32\".collector_service.CollectorMetric\x12>\n\rdependMetrics\x18\t \x03(\x0b\x32\'.collector_service.CollectorAliasMetric\x12\x14\n\x0cisCalculated\x18\n \x01(\x08\x12\x12\n\nexpression\x18\x0b \x01(\t\x1a.\n\x04\x44ims\x12\x0f\n\x07\x64imName\x18\x01 \x01(\t\x12\x15\n\roriginDimName\x18\x02 \x01(\tBMZKgo.easyops.local/contracts/protorepo-models/easyops/model/collector_serviceb\x06proto3')
  ,
  dependencies=[staff__manage__sdk_dot_model_dot_collector__service_dot_metric__pb2.DESCRIPTOR,])




_COLLECTORALIASMETRIC_DIMS = _descriptor.Descriptor(
  name='Dims',
  full_name='collector_service.CollectorAliasMetric.Dims',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dimName', full_name='collector_service.CollectorAliasMetric.Dims.dimName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='originDimName', full_name='collector_service.CollectorAliasMetric.Dims.originDimName', index=1,
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
  serialized_start=459,
  serialized_end=505,
)

_COLLECTORALIASMETRIC = _descriptor.Descriptor(
  name='CollectorAliasMetric',
  full_name='collector_service.CollectorAliasMetric',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='collector_service.CollectorAliasMetric.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='collector_service.CollectorAliasMetric.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dims', full_name='collector_service.CollectorAliasMetric.dims', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='collector_service.CollectorAliasMetric.version', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isKeyMetric', full_name='collector_service.CollectorAliasMetric.isKeyMetric', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='collector_service.CollectorAliasMetric.description', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectId', full_name='collector_service.CollectorAliasMetric.objectId', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='originalMetrics', full_name='collector_service.CollectorAliasMetric.originalMetrics', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dependMetrics', full_name='collector_service.CollectorAliasMetric.dependMetrics', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isCalculated', full_name='collector_service.CollectorAliasMetric.isCalculated', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expression', full_name='collector_service.CollectorAliasMetric.expression', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_COLLECTORALIASMETRIC_DIMS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=97,
  serialized_end=505,
)

_COLLECTORALIASMETRIC_DIMS.containing_type = _COLLECTORALIASMETRIC
_COLLECTORALIASMETRIC.fields_by_name['dims'].message_type = _COLLECTORALIASMETRIC_DIMS
_COLLECTORALIASMETRIC.fields_by_name['originalMetrics'].message_type = staff__manage__sdk_dot_model_dot_collector__service_dot_metric__pb2._COLLECTORMETRIC
_COLLECTORALIASMETRIC.fields_by_name['dependMetrics'].message_type = _COLLECTORALIASMETRIC
DESCRIPTOR.message_types_by_name['CollectorAliasMetric'] = _COLLECTORALIASMETRIC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CollectorAliasMetric = _reflection.GeneratedProtocolMessageType('CollectorAliasMetric', (_message.Message,), {

  'Dims' : _reflection.GeneratedProtocolMessageType('Dims', (_message.Message,), {
    'DESCRIPTOR' : _COLLECTORALIASMETRIC_DIMS,
    '__module__' : 'alias_metric_pb2'
    # @@protoc_insertion_point(class_scope:collector_service.CollectorAliasMetric.Dims)
    })
  ,
  'DESCRIPTOR' : _COLLECTORALIASMETRIC,
  '__module__' : 'alias_metric_pb2'
  # @@protoc_insertion_point(class_scope:collector_service.CollectorAliasMetric)
  })
_sym_db.RegisterMessage(CollectorAliasMetric)
_sym_db.RegisterMessage(CollectorAliasMetric.Dims)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
