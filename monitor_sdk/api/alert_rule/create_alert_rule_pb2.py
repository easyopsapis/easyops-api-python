# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: create_alert_rule.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from monitor_sdk.model.monitor import alert_dims_pb2 as monitor__sdk_dot_model_dot_monitor_dot_alert__dims__pb2
from monitor_sdk.model.monitor import alert_conditions_pb2 as monitor__sdk_dot_model_dot_monitor_dot_alert__conditions__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='create_alert_rule.proto',
  package='alert_rule',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x17\x63reate_alert_rule.proto\x12\nalert_rule\x1a*monitor_sdk/model/monitor/alert_dims.proto\x1a\x30monitor_sdk/model/monitor/alert_conditions.proto\x1a\x1cgoogle/protobuf/struct.proto\"\x80\x01\n\x17\x43reateAlertRuleResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x36\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32(.alert_rule.CreateAlertRuleResponse.Data\x1a\x12\n\x04\x44\x61ta\x12\n\n\x02id\x18\x01 \x01(\t\"\x85\x01\n\x1e\x43reateAlertRuleResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x31\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32#.alert_rule.CreateAlertRuleResponseb\x06proto3')
  ,
  dependencies=[monitor__sdk_dot_model_dot_monitor_dot_alert__dims__pb2.DESCRIPTOR,monitor__sdk_dot_model_dot_monitor_dot_alert__conditions__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_CREATEALERTRULERESPONSE_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='alert_rule.CreateAlertRuleResponse.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='alert_rule.CreateAlertRuleResponse.Data.id', index=0,
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
  serialized_start=274,
  serialized_end=292,
)

_CREATEALERTRULERESPONSE = _descriptor.Descriptor(
  name='CreateAlertRuleResponse',
  full_name='alert_rule.CreateAlertRuleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='alert_rule.CreateAlertRuleResponse.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='alert_rule.CreateAlertRuleResponse.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='alert_rule.CreateAlertRuleResponse.data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CREATEALERTRULERESPONSE_DATA, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=164,
  serialized_end=292,
)


_CREATEALERTRULERESPONSEWRAPPER = _descriptor.Descriptor(
  name='CreateAlertRuleResponseWrapper',
  full_name='alert_rule.CreateAlertRuleResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='alert_rule.CreateAlertRuleResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='alert_rule.CreateAlertRuleResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='alert_rule.CreateAlertRuleResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='alert_rule.CreateAlertRuleResponseWrapper.data', index=3,
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
  serialized_start=295,
  serialized_end=428,
)

_CREATEALERTRULERESPONSE_DATA.containing_type = _CREATEALERTRULERESPONSE
_CREATEALERTRULERESPONSE.fields_by_name['data'].message_type = _CREATEALERTRULERESPONSE_DATA
_CREATEALERTRULERESPONSEWRAPPER.fields_by_name['data'].message_type = _CREATEALERTRULERESPONSE
DESCRIPTOR.message_types_by_name['CreateAlertRuleResponse'] = _CREATEALERTRULERESPONSE
DESCRIPTOR.message_types_by_name['CreateAlertRuleResponseWrapper'] = _CREATEALERTRULERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateAlertRuleResponse = _reflection.GeneratedProtocolMessageType('CreateAlertRuleResponse', (_message.Message,), {

  'Data' : _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), {
    'DESCRIPTOR' : _CREATEALERTRULERESPONSE_DATA,
    '__module__' : 'create_alert_rule_pb2'
    # @@protoc_insertion_point(class_scope:alert_rule.CreateAlertRuleResponse.Data)
    })
  ,
  'DESCRIPTOR' : _CREATEALERTRULERESPONSE,
  '__module__' : 'create_alert_rule_pb2'
  # @@protoc_insertion_point(class_scope:alert_rule.CreateAlertRuleResponse)
  })
_sym_db.RegisterMessage(CreateAlertRuleResponse)
_sym_db.RegisterMessage(CreateAlertRuleResponse.Data)

CreateAlertRuleResponseWrapper = _reflection.GeneratedProtocolMessageType('CreateAlertRuleResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _CREATEALERTRULERESPONSEWRAPPER,
  '__module__' : 'create_alert_rule_pb2'
  # @@protoc_insertion_point(class_scope:alert_rule.CreateAlertRuleResponseWrapper)
  })
_sym_db.RegisterMessage(CreateAlertRuleResponseWrapper)


# @@protoc_insertion_point(module_scope)
