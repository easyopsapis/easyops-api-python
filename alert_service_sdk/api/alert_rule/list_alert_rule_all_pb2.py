# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list_alert_rule_all.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from alert_service_sdk.model.monitor import alert_rule_pb2 as alert__service__sdk_dot_model_dot_monitor_dot_alert__rule__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='list_alert_rule_all.proto',
  package='alert_rule',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x19list_alert_rule_all.proto\x12\nalert_rule\x1a\x30\x61lert_service_sdk/model/monitor/alert_rule.proto\"y\n\x17ListAlertRuleAllRequest\x12\x10\n\x08objectId\x18\x01 \x01(\t\x12\x12\n\ninstanceId\x18\x02 \x01(\t\x12\x11\n\trule_name\x18\x03 \x01(\t\x12\x13\n\x0bmetric_name\x18\x04 \x01(\t\x12\x10\n\x08\x64isabled\x18\x05 \x01(\t\"<\n\x18ListAlertRuleAllResponse\x12 \n\x04list\x18\x01 \x03(\x0b\x32\x12.monitor.AlertRule\"\x87\x01\n\x1fListAlertRuleAllResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x32\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32$.alert_rule.ListAlertRuleAllResponseb\x06proto3')
  ,
  dependencies=[alert__service__sdk_dot_model_dot_monitor_dot_alert__rule__pb2.DESCRIPTOR,])




_LISTALERTRULEALLREQUEST = _descriptor.Descriptor(
  name='ListAlertRuleAllRequest',
  full_name='alert_rule.ListAlertRuleAllRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='objectId', full_name='alert_rule.ListAlertRuleAllRequest.objectId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='alert_rule.ListAlertRuleAllRequest.instanceId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rule_name', full_name='alert_rule.ListAlertRuleAllRequest.rule_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metric_name', full_name='alert_rule.ListAlertRuleAllRequest.metric_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disabled', full_name='alert_rule.ListAlertRuleAllRequest.disabled', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=91,
  serialized_end=212,
)


_LISTALERTRULEALLRESPONSE = _descriptor.Descriptor(
  name='ListAlertRuleAllResponse',
  full_name='alert_rule.ListAlertRuleAllResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='list', full_name='alert_rule.ListAlertRuleAllResponse.list', index=0,
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
  serialized_start=214,
  serialized_end=274,
)


_LISTALERTRULEALLRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListAlertRuleAllResponseWrapper',
  full_name='alert_rule.ListAlertRuleAllResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='alert_rule.ListAlertRuleAllResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='alert_rule.ListAlertRuleAllResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='alert_rule.ListAlertRuleAllResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='alert_rule.ListAlertRuleAllResponseWrapper.data', index=3,
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
  serialized_start=277,
  serialized_end=412,
)

_LISTALERTRULEALLRESPONSE.fields_by_name['list'].message_type = alert__service__sdk_dot_model_dot_monitor_dot_alert__rule__pb2._ALERTRULE
_LISTALERTRULEALLRESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTALERTRULEALLRESPONSE
DESCRIPTOR.message_types_by_name['ListAlertRuleAllRequest'] = _LISTALERTRULEALLREQUEST
DESCRIPTOR.message_types_by_name['ListAlertRuleAllResponse'] = _LISTALERTRULEALLRESPONSE
DESCRIPTOR.message_types_by_name['ListAlertRuleAllResponseWrapper'] = _LISTALERTRULEALLRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListAlertRuleAllRequest = _reflection.GeneratedProtocolMessageType('ListAlertRuleAllRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTALERTRULEALLREQUEST,
  '__module__' : 'list_alert_rule_all_pb2'
  # @@protoc_insertion_point(class_scope:alert_rule.ListAlertRuleAllRequest)
  })
_sym_db.RegisterMessage(ListAlertRuleAllRequest)

ListAlertRuleAllResponse = _reflection.GeneratedProtocolMessageType('ListAlertRuleAllResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTALERTRULEALLRESPONSE,
  '__module__' : 'list_alert_rule_all_pb2'
  # @@protoc_insertion_point(class_scope:alert_rule.ListAlertRuleAllResponse)
  })
_sym_db.RegisterMessage(ListAlertRuleAllResponse)

ListAlertRuleAllResponseWrapper = _reflection.GeneratedProtocolMessageType('ListAlertRuleAllResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _LISTALERTRULEALLRESPONSEWRAPPER,
  '__module__' : 'list_alert_rule_all_pb2'
  # @@protoc_insertion_point(class_scope:alert_rule.ListAlertRuleAllResponseWrapper)
  })
_sym_db.RegisterMessage(ListAlertRuleAllResponseWrapper)


# @@protoc_insertion_point(module_scope)
