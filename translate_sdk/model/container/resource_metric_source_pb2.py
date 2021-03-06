# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: resource_metric_source.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from translate_sdk.model.container import metric_target_pb2 as translate__sdk_dot_model_dot_container_dot_metric__target__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='resource_metric_source.proto',
  package='container',
  syntax='proto3',
  serialized_options=_b('ZCgo.easyops.local/contracts/protorepo-models/easyops/model/container'),
  serialized_pb=_b('\n\x1cresource_metric_source.proto\x12\tcontainer\x1a\x31translate_sdk/model/container/metric_target.proto\"M\n\x14ResourceMetricSource\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\'\n\x06target\x18\x02 \x01(\x0b\x32\x17.container.MetricTargetBEZCgo.easyops.local/contracts/protorepo-models/easyops/model/containerb\x06proto3')
  ,
  dependencies=[translate__sdk_dot_model_dot_container_dot_metric__target__pb2.DESCRIPTOR,])




_RESOURCEMETRICSOURCE = _descriptor.Descriptor(
  name='ResourceMetricSource',
  full_name='container.ResourceMetricSource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='container.ResourceMetricSource.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target', full_name='container.ResourceMetricSource.target', index=1,
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
  serialized_start=94,
  serialized_end=171,
)

_RESOURCEMETRICSOURCE.fields_by_name['target'].message_type = translate__sdk_dot_model_dot_container_dot_metric__target__pb2._METRICTARGET
DESCRIPTOR.message_types_by_name['ResourceMetricSource'] = _RESOURCEMETRICSOURCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResourceMetricSource = _reflection.GeneratedProtocolMessageType('ResourceMetricSource', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCEMETRICSOURCE,
  '__module__' : 'resource_metric_source_pb2'
  # @@protoc_insertion_point(class_scope:container.ResourceMetricSource)
  })
_sym_db.RegisterMessage(ResourceMetricSource)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
