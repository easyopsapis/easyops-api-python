# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messsage_data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='messsage_data.proto',
  package='msgsender',
  syntax='proto3',
  serialized_options=_b('ZCgo.easyops.local/contracts/protorepo-models/easyops/model/msgsender'),
  serialized_pb=_b('\n\x13messsage_data.proto\x12\tmsgsender\"\x9b\x01\n\x0bMessageData\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\x12\x0f\n\x07subject\x18\x02 \x01(\t\x12\x0f\n\x07\x63\x63_addr\x18\x03 \x03(\t\x12\x0f\n\x07\x63\x63_user\x18\x04 \x03(\t\x12\x10\n\x08\x63\x63_group\x18\x05 \x03(\t\x12\x11\n\tfrom_name\x18\x06 \x01(\t\x12\x11\n\tfrom_addr\x18\x07 \x01(\t\x12\x10\n\x08msg_type\x18\x08 \x01(\tBEZCgo.easyops.local/contracts/protorepo-models/easyops/model/msgsenderb\x06proto3')
)




_MESSAGEDATA = _descriptor.Descriptor(
  name='MessageData',
  full_name='msgsender.MessageData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='msgsender.MessageData.content', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subject', full_name='msgsender.MessageData.subject', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cc_addr', full_name='msgsender.MessageData.cc_addr', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cc_user', full_name='msgsender.MessageData.cc_user', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cc_group', full_name='msgsender.MessageData.cc_group', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='from_name', full_name='msgsender.MessageData.from_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='from_addr', full_name='msgsender.MessageData.from_addr', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg_type', full_name='msgsender.MessageData.msg_type', index=7,
      number=8, type=9, cpp_type=9, label=1,
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
  serialized_end=190,
)

DESCRIPTOR.message_types_by_name['MessageData'] = _MESSAGEDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MessageData = _reflection.GeneratedProtocolMessageType('MessageData', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEDATA,
  '__module__' : 'messsage_data_pb2'
  # @@protoc_insertion_point(class_scope:msgsender.MessageData)
  })
_sym_db.RegisterMessage(MessageData)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
