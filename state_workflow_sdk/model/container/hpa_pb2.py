# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hpa.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from state_workflow_sdk.model.container import resource_metric_source_pb2 as state__workflow__sdk_dot_model_dot_container_dot_resource__metric__source__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='hpa.proto',
  package='container',
  syntax='proto3',
  serialized_options=_b('ZCgo.easyops.local/contracts/protorepo-models/easyops/model/container'),
  serialized_pb=_b('\n\thpa.proto\x12\tcontainer\x1a?state_workflow_sdk/model/container/resource_metric_source.proto\"\x96\x03\n\x17HorizontalPodAutoscaler\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x14\n\x0cresourceName\x18\x02 \x01(\t\x12\x11\n\tnamespace\x18\x03 \x01(\t\x12I\n\x0escaleTargetRef\x18\x04 \x01(\x0b\x32\x31.container.HorizontalPodAutoscaler.ScaleTargetRef\x12\x13\n\x0bminReplicas\x18\x05 \x01(\x05\x12\x13\n\x0bmaxReplicas\x18\x06 \x01(\x05\x12;\n\x07metrics\x18\x07 \x03(\x0b\x32*.container.HorizontalPodAutoscaler.Metrics\x1a@\n\x0eScaleTargetRef\x12\x0c\n\x04kind\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\napiVersion\x18\x03 \x01(\t\x1aJ\n\x07Metrics\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x31\n\x08resource\x18\x02 \x01(\x0b\x32\x1f.container.ResourceMetricSourceBEZCgo.easyops.local/contracts/protorepo-models/easyops/model/containerb\x06proto3')
  ,
  dependencies=[state__workflow__sdk_dot_model_dot_container_dot_resource__metric__source__pb2.DESCRIPTOR,])




_HORIZONTALPODAUTOSCALER_SCALETARGETREF = _descriptor.Descriptor(
  name='ScaleTargetRef',
  full_name='container.HorizontalPodAutoscaler.ScaleTargetRef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='kind', full_name='container.HorizontalPodAutoscaler.ScaleTargetRef.kind', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='container.HorizontalPodAutoscaler.ScaleTargetRef.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='apiVersion', full_name='container.HorizontalPodAutoscaler.ScaleTargetRef.apiVersion', index=2,
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
  serialized_start=356,
  serialized_end=420,
)

_HORIZONTALPODAUTOSCALER_METRICS = _descriptor.Descriptor(
  name='Metrics',
  full_name='container.HorizontalPodAutoscaler.Metrics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='container.HorizontalPodAutoscaler.Metrics.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resource', full_name='container.HorizontalPodAutoscaler.Metrics.resource', index=1,
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
  serialized_start=422,
  serialized_end=496,
)

_HORIZONTALPODAUTOSCALER = _descriptor.Descriptor(
  name='HorizontalPodAutoscaler',
  full_name='container.HorizontalPodAutoscaler',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='container.HorizontalPodAutoscaler.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resourceName', full_name='container.HorizontalPodAutoscaler.resourceName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='namespace', full_name='container.HorizontalPodAutoscaler.namespace', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scaleTargetRef', full_name='container.HorizontalPodAutoscaler.scaleTargetRef', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minReplicas', full_name='container.HorizontalPodAutoscaler.minReplicas', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maxReplicas', full_name='container.HorizontalPodAutoscaler.maxReplicas', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metrics', full_name='container.HorizontalPodAutoscaler.metrics', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_HORIZONTALPODAUTOSCALER_SCALETARGETREF, _HORIZONTALPODAUTOSCALER_METRICS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=496,
)

_HORIZONTALPODAUTOSCALER_SCALETARGETREF.containing_type = _HORIZONTALPODAUTOSCALER
_HORIZONTALPODAUTOSCALER_METRICS.fields_by_name['resource'].message_type = state__workflow__sdk_dot_model_dot_container_dot_resource__metric__source__pb2._RESOURCEMETRICSOURCE
_HORIZONTALPODAUTOSCALER_METRICS.containing_type = _HORIZONTALPODAUTOSCALER
_HORIZONTALPODAUTOSCALER.fields_by_name['scaleTargetRef'].message_type = _HORIZONTALPODAUTOSCALER_SCALETARGETREF
_HORIZONTALPODAUTOSCALER.fields_by_name['metrics'].message_type = _HORIZONTALPODAUTOSCALER_METRICS
DESCRIPTOR.message_types_by_name['HorizontalPodAutoscaler'] = _HORIZONTALPODAUTOSCALER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HorizontalPodAutoscaler = _reflection.GeneratedProtocolMessageType('HorizontalPodAutoscaler', (_message.Message,), {

  'ScaleTargetRef' : _reflection.GeneratedProtocolMessageType('ScaleTargetRef', (_message.Message,), {
    'DESCRIPTOR' : _HORIZONTALPODAUTOSCALER_SCALETARGETREF,
    '__module__' : 'hpa_pb2'
    # @@protoc_insertion_point(class_scope:container.HorizontalPodAutoscaler.ScaleTargetRef)
    })
  ,

  'Metrics' : _reflection.GeneratedProtocolMessageType('Metrics', (_message.Message,), {
    'DESCRIPTOR' : _HORIZONTALPODAUTOSCALER_METRICS,
    '__module__' : 'hpa_pb2'
    # @@protoc_insertion_point(class_scope:container.HorizontalPodAutoscaler.Metrics)
    })
  ,
  'DESCRIPTOR' : _HORIZONTALPODAUTOSCALER,
  '__module__' : 'hpa_pb2'
  # @@protoc_insertion_point(class_scope:container.HorizontalPodAutoscaler)
  })
_sym_db.RegisterMessage(HorizontalPodAutoscaler)
_sym_db.RegisterMessage(HorizontalPodAutoscaler.ScaleTargetRef)
_sym_db.RegisterMessage(HorizontalPodAutoscaler.Metrics)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
