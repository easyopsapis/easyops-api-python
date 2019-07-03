# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mail_info.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mail_info.proto',
  package='ops_automation',
  syntax='proto3',
  serialized_options=_b('ZHgo.easyops.local/contracts/protorepo-models/easyops/model/ops_automation'),
  serialized_pb=_b('\n\x0fmail_info.proto\x12\x0eops_automation\"/\n\x08MailInfo\x12\x11\n\tnotifiers\x18\x01 \x03(\t\x12\x10\n\x08strategy\x18\x02 \x01(\tBJZHgo.easyops.local/contracts/protorepo-models/easyops/model/ops_automationb\x06proto3')
)




_MAILINFO = _descriptor.Descriptor(
  name='MailInfo',
  full_name='ops_automation.MailInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='notifiers', full_name='ops_automation.MailInfo.notifiers', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strategy', full_name='ops_automation.MailInfo.strategy', index=1,
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
  serialized_start=35,
  serialized_end=82,
)

DESCRIPTOR.message_types_by_name['MailInfo'] = _MAILINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MailInfo = _reflection.GeneratedProtocolMessageType('MailInfo', (_message.Message,), dict(
  DESCRIPTOR = _MAILINFO,
  __module__ = 'mail_info_pb2'
  # @@protoc_insertion_point(class_scope:ops_automation.MailInfo)
  ))
_sym_db.RegisterMessage(MailInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)