# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: disable_alert_rule.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='disable_alert_rule.proto',
  package='alert_rule',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x18\x64isable_alert_rule.proto\x12\nalert_rule\"7\n\x17\x44isableAlertRuleRequest\x12\x10\n\x08\x64isabled\x18\x01 \x01(\x08\x12\n\n\x02id\x18\x02 \x01(\t\"\x85\x01\n\x18\x44isableAlertRuleResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x37\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32).alert_rule.DisableAlertRuleResponse.Data\x1a\x15\n\x04\x44\x61ta\x12\r\n\x05\x63ount\x18\x01 \x01(\x05\"\x87\x01\n\x1f\x44isableAlertRuleResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x32\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32$.alert_rule.DisableAlertRuleResponseb\x06proto3')
)




_DISABLEALERTRULEREQUEST = _descriptor.Descriptor(
  name='DisableAlertRuleRequest',
  full_name='alert_rule.DisableAlertRuleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='disabled', full_name='alert_rule.DisableAlertRuleRequest.disabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='alert_rule.DisableAlertRuleRequest.id', index=1,
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
  serialized_end=95,
)


_DISABLEALERTRULERESPONSE_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='alert_rule.DisableAlertRuleResponse.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='alert_rule.DisableAlertRuleResponse.Data.count', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_end=231,
)

_DISABLEALERTRULERESPONSE = _descriptor.Descriptor(
  name='DisableAlertRuleResponse',
  full_name='alert_rule.DisableAlertRuleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='alert_rule.DisableAlertRuleResponse.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='alert_rule.DisableAlertRuleResponse.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='alert_rule.DisableAlertRuleResponse.data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DISABLEALERTRULERESPONSE_DATA, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=98,
  serialized_end=231,
)


_DISABLEALERTRULERESPONSEWRAPPER = _descriptor.Descriptor(
  name='DisableAlertRuleResponseWrapper',
  full_name='alert_rule.DisableAlertRuleResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='alert_rule.DisableAlertRuleResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='alert_rule.DisableAlertRuleResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='alert_rule.DisableAlertRuleResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='alert_rule.DisableAlertRuleResponseWrapper.data', index=3,
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
  serialized_start=234,
  serialized_end=369,
)

_DISABLEALERTRULERESPONSE_DATA.containing_type = _DISABLEALERTRULERESPONSE
_DISABLEALERTRULERESPONSE.fields_by_name['data'].message_type = _DISABLEALERTRULERESPONSE_DATA
_DISABLEALERTRULERESPONSEWRAPPER.fields_by_name['data'].message_type = _DISABLEALERTRULERESPONSE
DESCRIPTOR.message_types_by_name['DisableAlertRuleRequest'] = _DISABLEALERTRULEREQUEST
DESCRIPTOR.message_types_by_name['DisableAlertRuleResponse'] = _DISABLEALERTRULERESPONSE
DESCRIPTOR.message_types_by_name['DisableAlertRuleResponseWrapper'] = _DISABLEALERTRULERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DisableAlertRuleRequest = _reflection.GeneratedProtocolMessageType('DisableAlertRuleRequest', (_message.Message,), {
  'DESCRIPTOR' : _DISABLEALERTRULEREQUEST,
  '__module__' : 'disable_alert_rule_pb2'
  # @@protoc_insertion_point(class_scope:alert_rule.DisableAlertRuleRequest)
  })
_sym_db.RegisterMessage(DisableAlertRuleRequest)

DisableAlertRuleResponse = _reflection.GeneratedProtocolMessageType('DisableAlertRuleResponse', (_message.Message,), {

  'Data' : _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), {
    'DESCRIPTOR' : _DISABLEALERTRULERESPONSE_DATA,
    '__module__' : 'disable_alert_rule_pb2'
    # @@protoc_insertion_point(class_scope:alert_rule.DisableAlertRuleResponse.Data)
    })
  ,
  'DESCRIPTOR' : _DISABLEALERTRULERESPONSE,
  '__module__' : 'disable_alert_rule_pb2'
  # @@protoc_insertion_point(class_scope:alert_rule.DisableAlertRuleResponse)
  })
_sym_db.RegisterMessage(DisableAlertRuleResponse)
_sym_db.RegisterMessage(DisableAlertRuleResponse.Data)

DisableAlertRuleResponseWrapper = _reflection.GeneratedProtocolMessageType('DisableAlertRuleResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _DISABLEALERTRULERESPONSEWRAPPER,
  '__module__' : 'disable_alert_rule_pb2'
  # @@protoc_insertion_point(class_scope:alert_rule.DisableAlertRuleResponseWrapper)
  })
_sym_db.RegisterMessage(DisableAlertRuleResponseWrapper)


# @@protoc_insertion_point(module_scope)