# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_alert_rule_list.proto

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
  name='get_alert_rule_list.proto',
  package='alert_rule',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x19get_alert_rule_list.proto\x12\nalert_rule\x1a*monitor_sdk/model/monitor/alert_rule.proto\"\x88\x01\n\x17GetAlertRuleListRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x0e\n\x06system\x18\x03 \x01(\t\x12\x0f\n\x07_id__in\x18\x04 \x01(\t\x12\x10\n\x08objectId\x18\x05 \x01(\t\x12\x19\n\x11XXX_RestFieldMask\x18\x06 \x03(\t\"\x87\x01\n\x18GetAlertRuleListResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x0c\n\x04page\x18\x03 \x01(\x05\x12\r\n\x05total\x18\x04 \x01(\x05\x12\x0b\n\x03msg\x18\x05 \x01(\t\x12 \n\x04\x64\x61ta\x18\x06 \x03(\x0b\x32\x12.monitor.AlertRule\"\x87\x01\n\x1fGetAlertRuleListResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x32\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32$.alert_rule.GetAlertRuleListResponseb\x06proto3')
  ,
  dependencies=[monitor__sdk_dot_model_dot_monitor_dot_alert__rule__pb2.DESCRIPTOR,])




_GETALERTRULELISTREQUEST = _descriptor.Descriptor(
  name='GetAlertRuleListRequest',
  full_name='alert_rule.GetAlertRuleListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='alert_rule.GetAlertRuleListRequest.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='alert_rule.GetAlertRuleListRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='system', full_name='alert_rule.GetAlertRuleListRequest.system', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='_id__in', full_name='alert_rule.GetAlertRuleListRequest._id__in', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectId', full_name='alert_rule.GetAlertRuleListRequest.objectId', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='XXX_RestFieldMask', full_name='alert_rule.GetAlertRuleListRequest.XXX_RestFieldMask', index=5,
      number=6, type=9, cpp_type=9, label=3,
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
  serialized_start=86,
  serialized_end=222,
)


_GETALERTRULELISTRESPONSE = _descriptor.Descriptor(
  name='GetAlertRuleListResponse',
  full_name='alert_rule.GetAlertRuleListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='alert_rule.GetAlertRuleListResponse.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='alert_rule.GetAlertRuleListResponse.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page', full_name='alert_rule.GetAlertRuleListResponse.page', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='alert_rule.GetAlertRuleListResponse.total', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='alert_rule.GetAlertRuleListResponse.msg', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='alert_rule.GetAlertRuleListResponse.data', index=5,
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
  serialized_start=225,
  serialized_end=360,
)


_GETALERTRULELISTRESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetAlertRuleListResponseWrapper',
  full_name='alert_rule.GetAlertRuleListResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='alert_rule.GetAlertRuleListResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='alert_rule.GetAlertRuleListResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='alert_rule.GetAlertRuleListResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='alert_rule.GetAlertRuleListResponseWrapper.data', index=3,
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
  serialized_start=363,
  serialized_end=498,
)

_GETALERTRULELISTRESPONSE.fields_by_name['data'].message_type = monitor__sdk_dot_model_dot_monitor_dot_alert__rule__pb2._ALERTRULE
_GETALERTRULELISTRESPONSEWRAPPER.fields_by_name['data'].message_type = _GETALERTRULELISTRESPONSE
DESCRIPTOR.message_types_by_name['GetAlertRuleListRequest'] = _GETALERTRULELISTREQUEST
DESCRIPTOR.message_types_by_name['GetAlertRuleListResponse'] = _GETALERTRULELISTRESPONSE
DESCRIPTOR.message_types_by_name['GetAlertRuleListResponseWrapper'] = _GETALERTRULELISTRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetAlertRuleListRequest = _reflection.GeneratedProtocolMessageType('GetAlertRuleListRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETALERTRULELISTREQUEST,
  '__module__' : 'get_alert_rule_list_pb2'
  # @@protoc_insertion_point(class_scope:alert_rule.GetAlertRuleListRequest)
  })
_sym_db.RegisterMessage(GetAlertRuleListRequest)

GetAlertRuleListResponse = _reflection.GeneratedProtocolMessageType('GetAlertRuleListResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETALERTRULELISTRESPONSE,
  '__module__' : 'get_alert_rule_list_pb2'
  # @@protoc_insertion_point(class_scope:alert_rule.GetAlertRuleListResponse)
  })
_sym_db.RegisterMessage(GetAlertRuleListResponse)

GetAlertRuleListResponseWrapper = _reflection.GeneratedProtocolMessageType('GetAlertRuleListResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _GETALERTRULELISTRESPONSEWRAPPER,
  '__module__' : 'get_alert_rule_list_pb2'
  # @@protoc_insertion_point(class_scope:alert_rule.GetAlertRuleListResponseWrapper)
  })
_sym_db.RegisterMessage(GetAlertRuleListResponseWrapper)


# @@protoc_insertion_point(module_scope)