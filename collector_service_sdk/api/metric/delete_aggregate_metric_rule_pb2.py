# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: delete_aggregate_metric_rule.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='delete_aggregate_metric_rule.proto',
  package='metric',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\"delete_aggregate_metric_rule.proto\x12\x06metric\x1a\x1bgoogle/protobuf/empty.proto\"?\n)DeleteCollectorAggregateMetricRuleRequest\x12\x12\n\ninstanceId\x18\x01 \x01(\t\"\x8b\x01\n1DeleteCollectorAggregateMetricRuleResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12$\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x16.google.protobuf.Emptyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_DELETECOLLECTORAGGREGATEMETRICRULEREQUEST = _descriptor.Descriptor(
  name='DeleteCollectorAggregateMetricRuleRequest',
  full_name='metric.DeleteCollectorAggregateMetricRuleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='metric.DeleteCollectorAggregateMetricRuleRequest.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=75,
  serialized_end=138,
)


_DELETECOLLECTORAGGREGATEMETRICRULERESPONSEWRAPPER = _descriptor.Descriptor(
  name='DeleteCollectorAggregateMetricRuleResponseWrapper',
  full_name='metric.DeleteCollectorAggregateMetricRuleResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='metric.DeleteCollectorAggregateMetricRuleResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='metric.DeleteCollectorAggregateMetricRuleResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='metric.DeleteCollectorAggregateMetricRuleResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='metric.DeleteCollectorAggregateMetricRuleResponseWrapper.data', index=3,
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
  serialized_start=141,
  serialized_end=280,
)

_DELETECOLLECTORAGGREGATEMETRICRULERESPONSEWRAPPER.fields_by_name['data'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
DESCRIPTOR.message_types_by_name['DeleteCollectorAggregateMetricRuleRequest'] = _DELETECOLLECTORAGGREGATEMETRICRULEREQUEST
DESCRIPTOR.message_types_by_name['DeleteCollectorAggregateMetricRuleResponseWrapper'] = _DELETECOLLECTORAGGREGATEMETRICRULERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeleteCollectorAggregateMetricRuleRequest = _reflection.GeneratedProtocolMessageType('DeleteCollectorAggregateMetricRuleRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETECOLLECTORAGGREGATEMETRICRULEREQUEST,
  '__module__' : 'delete_aggregate_metric_rule_pb2'
  # @@protoc_insertion_point(class_scope:metric.DeleteCollectorAggregateMetricRuleRequest)
  })
_sym_db.RegisterMessage(DeleteCollectorAggregateMetricRuleRequest)

DeleteCollectorAggregateMetricRuleResponseWrapper = _reflection.GeneratedProtocolMessageType('DeleteCollectorAggregateMetricRuleResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _DELETECOLLECTORAGGREGATEMETRICRULERESPONSEWRAPPER,
  '__module__' : 'delete_aggregate_metric_rule_pb2'
  # @@protoc_insertion_point(class_scope:metric.DeleteCollectorAggregateMetricRuleResponseWrapper)
  })
_sym_db.RegisterMessage(DeleteCollectorAggregateMetricRuleResponseWrapper)


# @@protoc_insertion_point(module_scope)
