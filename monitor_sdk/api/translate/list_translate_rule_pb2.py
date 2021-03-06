# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list_translate_rule.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from monitor_sdk.model.monitor import translate_rule_pb2 as monitor__sdk_dot_model_dot_monitor_dot_translate__rule__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='list_translate_rule.proto',
  package='translate',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x19list_translate_rule.proto\x12\ttranslate\x1a.monitor_sdk/model/monitor/translate_rule.proto\";\n\x18ListTranslateRuleRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\"\x8c\x01\n\x19ListTranslateRuleResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\r\n\x05total\x18\x03 \x01(\x05\x12\x0c\n\x04page\x18\x04 \x01(\x05\x12\x11\n\tpage_size\x18\x05 \x01(\x05\x12$\n\x04\x64\x61ta\x18\x06 \x03(\x0b\x32\x16.monitor.TransalteRule\"\x88\x01\n ListTranslateRuleResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x32\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32$.translate.ListTranslateRuleResponseb\x06proto3')
  ,
  dependencies=[monitor__sdk_dot_model_dot_monitor_dot_translate__rule__pb2.DESCRIPTOR,])




_LISTTRANSLATERULEREQUEST = _descriptor.Descriptor(
  name='ListTranslateRuleRequest',
  full_name='translate.ListTranslateRuleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='translate.ListTranslateRuleRequest.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='translate.ListTranslateRuleRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=88,
  serialized_end=147,
)


_LISTTRANSLATERULERESPONSE = _descriptor.Descriptor(
  name='ListTranslateRuleResponse',
  full_name='translate.ListTranslateRuleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='translate.ListTranslateRuleResponse.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='translate.ListTranslateRuleResponse.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='translate.ListTranslateRuleResponse.total', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page', full_name='translate.ListTranslateRuleResponse.page', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='translate.ListTranslateRuleResponse.page_size', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='translate.ListTranslateRuleResponse.data', index=5,
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
  serialized_start=150,
  serialized_end=290,
)


_LISTTRANSLATERULERESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListTranslateRuleResponseWrapper',
  full_name='translate.ListTranslateRuleResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='translate.ListTranslateRuleResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='translate.ListTranslateRuleResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='translate.ListTranslateRuleResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='translate.ListTranslateRuleResponseWrapper.data', index=3,
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
  serialized_start=293,
  serialized_end=429,
)

_LISTTRANSLATERULERESPONSE.fields_by_name['data'].message_type = monitor__sdk_dot_model_dot_monitor_dot_translate__rule__pb2._TRANSALTERULE
_LISTTRANSLATERULERESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTTRANSLATERULERESPONSE
DESCRIPTOR.message_types_by_name['ListTranslateRuleRequest'] = _LISTTRANSLATERULEREQUEST
DESCRIPTOR.message_types_by_name['ListTranslateRuleResponse'] = _LISTTRANSLATERULERESPONSE
DESCRIPTOR.message_types_by_name['ListTranslateRuleResponseWrapper'] = _LISTTRANSLATERULERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListTranslateRuleRequest = _reflection.GeneratedProtocolMessageType('ListTranslateRuleRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTTRANSLATERULEREQUEST,
  '__module__' : 'list_translate_rule_pb2'
  # @@protoc_insertion_point(class_scope:translate.ListTranslateRuleRequest)
  })
_sym_db.RegisterMessage(ListTranslateRuleRequest)

ListTranslateRuleResponse = _reflection.GeneratedProtocolMessageType('ListTranslateRuleResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTTRANSLATERULERESPONSE,
  '__module__' : 'list_translate_rule_pb2'
  # @@protoc_insertion_point(class_scope:translate.ListTranslateRuleResponse)
  })
_sym_db.RegisterMessage(ListTranslateRuleResponse)

ListTranslateRuleResponseWrapper = _reflection.GeneratedProtocolMessageType('ListTranslateRuleResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _LISTTRANSLATERULERESPONSEWRAPPER,
  '__module__' : 'list_translate_rule_pb2'
  # @@protoc_insertion_point(class_scope:translate.ListTranslateRuleResponseWrapper)
  })
_sym_db.RegisterMessage(ListTranslateRuleResponseWrapper)


# @@protoc_insertion_point(module_scope)
