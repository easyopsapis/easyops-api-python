# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_metric_name_detail.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_metric_name_detail.proto',
  package='metric',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1cget_metric_name_detail.proto\x12\x06metric\"H\n DetailCollectorMetricNameRequest\x12\x10\n\x08objectId\x18\x01 \x01(\t\x12\x12\n\nmetricName\x18\x02 \x01(\t\"\xaa\x01\n!DetailCollectorMetricNameResponse\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x12\n\nmetricName\x18\x02 \x01(\t\x12\x11\n\tmetricKey\x18\x03 \x01(\t\x12\x15\n\rmetricKeyName\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x10\n\x08objectId\x18\x06 \x01(\t\x12\x0c\n\x04unit\x18\x07 \x01(\t\"\x95\x01\n(DetailCollectorMetricNameResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x37\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32).metric.DetailCollectorMetricNameResponseb\x06proto3')
)




_DETAILCOLLECTORMETRICNAMEREQUEST = _descriptor.Descriptor(
  name='DetailCollectorMetricNameRequest',
  full_name='metric.DetailCollectorMetricNameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='objectId', full_name='metric.DetailCollectorMetricNameRequest.objectId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metricName', full_name='metric.DetailCollectorMetricNameRequest.metricName', index=1,
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
  serialized_start=40,
  serialized_end=112,
)


_DETAILCOLLECTORMETRICNAMERESPONSE = _descriptor.Descriptor(
  name='DetailCollectorMetricNameResponse',
  full_name='metric.DetailCollectorMetricNameResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='metric.DetailCollectorMetricNameResponse.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metricName', full_name='metric.DetailCollectorMetricNameResponse.metricName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metricKey', full_name='metric.DetailCollectorMetricNameResponse.metricKey', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metricKeyName', full_name='metric.DetailCollectorMetricNameResponse.metricKeyName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='metric.DetailCollectorMetricNameResponse.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectId', full_name='metric.DetailCollectorMetricNameResponse.objectId', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unit', full_name='metric.DetailCollectorMetricNameResponse.unit', index=6,
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
  serialized_start=115,
  serialized_end=285,
)


_DETAILCOLLECTORMETRICNAMERESPONSEWRAPPER = _descriptor.Descriptor(
  name='DetailCollectorMetricNameResponseWrapper',
  full_name='metric.DetailCollectorMetricNameResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='metric.DetailCollectorMetricNameResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='metric.DetailCollectorMetricNameResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='metric.DetailCollectorMetricNameResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='metric.DetailCollectorMetricNameResponseWrapper.data', index=3,
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
  serialized_start=288,
  serialized_end=437,
)

_DETAILCOLLECTORMETRICNAMERESPONSEWRAPPER.fields_by_name['data'].message_type = _DETAILCOLLECTORMETRICNAMERESPONSE
DESCRIPTOR.message_types_by_name['DetailCollectorMetricNameRequest'] = _DETAILCOLLECTORMETRICNAMEREQUEST
DESCRIPTOR.message_types_by_name['DetailCollectorMetricNameResponse'] = _DETAILCOLLECTORMETRICNAMERESPONSE
DESCRIPTOR.message_types_by_name['DetailCollectorMetricNameResponseWrapper'] = _DETAILCOLLECTORMETRICNAMERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DetailCollectorMetricNameRequest = _reflection.GeneratedProtocolMessageType('DetailCollectorMetricNameRequest', (_message.Message,), {
  'DESCRIPTOR' : _DETAILCOLLECTORMETRICNAMEREQUEST,
  '__module__' : 'get_metric_name_detail_pb2'
  # @@protoc_insertion_point(class_scope:metric.DetailCollectorMetricNameRequest)
  })
_sym_db.RegisterMessage(DetailCollectorMetricNameRequest)

DetailCollectorMetricNameResponse = _reflection.GeneratedProtocolMessageType('DetailCollectorMetricNameResponse', (_message.Message,), {
  'DESCRIPTOR' : _DETAILCOLLECTORMETRICNAMERESPONSE,
  '__module__' : 'get_metric_name_detail_pb2'
  # @@protoc_insertion_point(class_scope:metric.DetailCollectorMetricNameResponse)
  })
_sym_db.RegisterMessage(DetailCollectorMetricNameResponse)

DetailCollectorMetricNameResponseWrapper = _reflection.GeneratedProtocolMessageType('DetailCollectorMetricNameResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _DETAILCOLLECTORMETRICNAMERESPONSEWRAPPER,
  '__module__' : 'get_metric_name_detail_pb2'
  # @@protoc_insertion_point(class_scope:metric.DetailCollectorMetricNameResponseWrapper)
  })
_sym_db.RegisterMessage(DetailCollectorMetricNameResponseWrapper)


# @@protoc_insertion_point(module_scope)