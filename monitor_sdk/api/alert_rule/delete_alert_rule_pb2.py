# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: delete_alert_rule.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='delete_alert_rule.proto',
  package='alert_rule',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x17\x64\x65lete_alert_rule.proto\x12\nalert_rule\x1a\x1cgoogle/protobuf/struct.proto\"$\n\x16\x44\x65leteAlertRuleRequest\x12\n\n\x02id\x18\x01 \x01(\t\"[\n\x17\x44\x65leteAlertRuleResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12%\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\"\x85\x01\n\x1e\x44\x65leteAlertRuleResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x31\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32#.alert_rule.DeleteAlertRuleResponseb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_DELETEALERTRULEREQUEST = _descriptor.Descriptor(
  name='DeleteAlertRuleRequest',
  full_name='alert_rule.DeleteAlertRuleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='alert_rule.DeleteAlertRuleRequest.id', index=0,
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
  serialized_start=69,
  serialized_end=105,
)


_DELETEALERTRULERESPONSE = _descriptor.Descriptor(
  name='DeleteAlertRuleResponse',
  full_name='alert_rule.DeleteAlertRuleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='alert_rule.DeleteAlertRuleResponse.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='alert_rule.DeleteAlertRuleResponse.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='alert_rule.DeleteAlertRuleResponse.data', index=2,
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
  serialized_start=107,
  serialized_end=198,
)


_DELETEALERTRULERESPONSEWRAPPER = _descriptor.Descriptor(
  name='DeleteAlertRuleResponseWrapper',
  full_name='alert_rule.DeleteAlertRuleResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='alert_rule.DeleteAlertRuleResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='alert_rule.DeleteAlertRuleResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='alert_rule.DeleteAlertRuleResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='alert_rule.DeleteAlertRuleResponseWrapper.data', index=3,
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
  serialized_start=201,
  serialized_end=334,
)

_DELETEALERTRULERESPONSE.fields_by_name['data'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_DELETEALERTRULERESPONSEWRAPPER.fields_by_name['data'].message_type = _DELETEALERTRULERESPONSE
DESCRIPTOR.message_types_by_name['DeleteAlertRuleRequest'] = _DELETEALERTRULEREQUEST
DESCRIPTOR.message_types_by_name['DeleteAlertRuleResponse'] = _DELETEALERTRULERESPONSE
DESCRIPTOR.message_types_by_name['DeleteAlertRuleResponseWrapper'] = _DELETEALERTRULERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeleteAlertRuleRequest = _reflection.GeneratedProtocolMessageType('DeleteAlertRuleRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEALERTRULEREQUEST,
  '__module__' : 'delete_alert_rule_pb2'
  # @@protoc_insertion_point(class_scope:alert_rule.DeleteAlertRuleRequest)
  })
_sym_db.RegisterMessage(DeleteAlertRuleRequest)

DeleteAlertRuleResponse = _reflection.GeneratedProtocolMessageType('DeleteAlertRuleResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEALERTRULERESPONSE,
  '__module__' : 'delete_alert_rule_pb2'
  # @@protoc_insertion_point(class_scope:alert_rule.DeleteAlertRuleResponse)
  })
_sym_db.RegisterMessage(DeleteAlertRuleResponse)

DeleteAlertRuleResponseWrapper = _reflection.GeneratedProtocolMessageType('DeleteAlertRuleResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _DELETEALERTRULERESPONSEWRAPPER,
  '__module__' : 'delete_alert_rule_pb2'
  # @@protoc_insertion_point(class_scope:alert_rule.DeleteAlertRuleResponseWrapper)
  })
_sym_db.RegisterMessage(DeleteAlertRuleResponseWrapper)


# @@protoc_insertion_point(module_scope)