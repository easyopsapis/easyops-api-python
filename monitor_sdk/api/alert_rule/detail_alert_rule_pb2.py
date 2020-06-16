# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: detail_alert_rule.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from monitor_sdk.model.monitor import alert_rule_pb2 as monitor__sdk_dot_model_dot_monitor_dot_alert__rule__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='detail_alert_rule.proto',
  package='alert_rule',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x17\x64\x65tail_alert_rule.proto\x12\nalert_rule\x1a*monitor_sdk/model/monitor/alert_rule.proto\"$\n\x16\x44\x65tailAlertRuleRequest\x12\n\n\x02id\x18\x01 \x01(\t\"V\n\x17\x44\x65tailAlertRuleResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12 \n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x12.monitor.AlertRule\"\x85\x01\n\x1e\x44\x65tailAlertRuleResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x31\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32#.alert_rule.DetailAlertRuleResponseb\x06proto3')
  ,
  dependencies=[monitor__sdk_dot_model_dot_monitor_dot_alert__rule__pb2.DESCRIPTOR,])




_DETAILALERTRULEREQUEST = _descriptor.Descriptor(
  name='DetailAlertRuleRequest',
  full_name='alert_rule.DetailAlertRuleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='alert_rule.DetailAlertRuleRequest.id', index=0,
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
  serialized_start=83,
  serialized_end=119,
)


_DETAILALERTRULERESPONSE = _descriptor.Descriptor(
  name='DetailAlertRuleResponse',
  full_name='alert_rule.DetailAlertRuleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='alert_rule.DetailAlertRuleResponse.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='alert_rule.DetailAlertRuleResponse.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='alert_rule.DetailAlertRuleResponse.data', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=121,
  serialized_end=207,
)


_DETAILALERTRULERESPONSEWRAPPER = _descriptor.Descriptor(
  name='DetailAlertRuleResponseWrapper',
  full_name='alert_rule.DetailAlertRuleResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='alert_rule.DetailAlertRuleResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='alert_rule.DetailAlertRuleResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='alert_rule.DetailAlertRuleResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='alert_rule.DetailAlertRuleResponseWrapper.data', index=3,
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
  serialized_start=210,
  serialized_end=343,
)

_DETAILALERTRULERESPONSE.fields_by_name['data'].message_type = monitor__sdk_dot_model_dot_monitor_dot_alert__rule__pb2._ALERTRULE
_DETAILALERTRULERESPONSEWRAPPER.fields_by_name['data'].message_type = _DETAILALERTRULERESPONSE
DESCRIPTOR.message_types_by_name['DetailAlertRuleRequest'] = _DETAILALERTRULEREQUEST
DESCRIPTOR.message_types_by_name['DetailAlertRuleResponse'] = _DETAILALERTRULERESPONSE
DESCRIPTOR.message_types_by_name['DetailAlertRuleResponseWrapper'] = _DETAILALERTRULERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DetailAlertRuleRequest = _reflection.GeneratedProtocolMessageType('DetailAlertRuleRequest', (_message.Message,), {
  'DESCRIPTOR' : _DETAILALERTRULEREQUEST,
  '__module__' : 'detail_alert_rule_pb2'
  # @@protoc_insertion_point(class_scope:alert_rule.DetailAlertRuleRequest)
  })
_sym_db.RegisterMessage(DetailAlertRuleRequest)

DetailAlertRuleResponse = _reflection.GeneratedProtocolMessageType('DetailAlertRuleResponse', (_message.Message,), {
  'DESCRIPTOR' : _DETAILALERTRULERESPONSE,
  '__module__' : 'detail_alert_rule_pb2'
  # @@protoc_insertion_point(class_scope:alert_rule.DetailAlertRuleResponse)
  })
_sym_db.RegisterMessage(DetailAlertRuleResponse)

DetailAlertRuleResponseWrapper = _reflection.GeneratedProtocolMessageType('DetailAlertRuleResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _DETAILALERTRULERESPONSEWRAPPER,
  '__module__' : 'detail_alert_rule_pb2'
  # @@protoc_insertion_point(class_scope:alert_rule.DetailAlertRuleResponseWrapper)
  })
_sym_db.RegisterMessage(DetailAlertRuleResponseWrapper)


# @@protoc_insertion_point(module_scope)
