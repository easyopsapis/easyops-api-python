# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: subscribe_info.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='subscribe_info.proto',
  package='notify',
  syntax='proto3',
  serialized_options=_b('Z@go.easyops.local/contracts/protorepo-models/easyops/model/notify'),
  serialized_pb=_b('\n\x14subscribe_info.proto\x12\x06notify\"/\n\rSubscribeInfo\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\t\x12\r\n\x05\x65vent\x18\x02 \x03(\tBBZ@go.easyops.local/contracts/protorepo-models/easyops/model/notifyb\x06proto3')
)




_SUBSCRIBEINFO = _descriptor.Descriptor(
  name='SubscribeInfo',
  full_name='notify.SubscribeInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel', full_name='notify.SubscribeInfo.channel', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event', full_name='notify.SubscribeInfo.event', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=32,
  serialized_end=79,
)

DESCRIPTOR.message_types_by_name['SubscribeInfo'] = _SUBSCRIBEINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SubscribeInfo = _reflection.GeneratedProtocolMessageType('SubscribeInfo', (_message.Message,), dict(
  DESCRIPTOR = _SUBSCRIBEINFO,
  __module__ = 'subscribe_info_pb2'
  # @@protoc_insertion_point(class_scope:notify.SubscribeInfo)
  ))
_sym_db.RegisterMessage(SubscribeInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
