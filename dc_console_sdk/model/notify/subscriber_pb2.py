# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: subscriber.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from dc_console_sdk.model.notify import subscribe_info_pb2 as dc__console__sdk_dot_model_dot_notify_dot_subscribe__info__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='subscriber.proto',
  package='notify',
  syntax='proto3',
  serialized_options=_b('Z@go.easyops.local/contracts/protorepo-models/easyops/model/notify'),
  serialized_pb=_b('\n\x10subscriber.proto\x12\x06notify\x1a\x30\x64\x63_console_sdk/model/notify/subscribe_info.proto\"\xab\x01\n\nSubscriber\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x61\x64min\x18\x02 \x01(\t\x12\x10\n\x08\x63\x61llback\x18\x03 \x01(\t\x12\x0f\n\x07\x65nsName\x18\x04 \x01(\t\x12\x0f\n\x07procNum\x18\x05 \x01(\x05\x12\x0f\n\x07msgType\x18\x06 \x01(\x05\x12\r\n\x05retry\x18\x07 \x01(\x05\x12,\n\rsubscribeInfo\x18\x08 \x03(\x0b\x32\x15.notify.SubscribeInfoBBZ@go.easyops.local/contracts/protorepo-models/easyops/model/notifyb\x06proto3')
  ,
  dependencies=[dc__console__sdk_dot_model_dot_notify_dot_subscribe__info__pb2.DESCRIPTOR,])




_SUBSCRIBER = _descriptor.Descriptor(
  name='Subscriber',
  full_name='notify.Subscriber',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='notify.Subscriber.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='admin', full_name='notify.Subscriber.admin', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='callback', full_name='notify.Subscriber.callback', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ensName', full_name='notify.Subscriber.ensName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='procNum', full_name='notify.Subscriber.procNum', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msgType', full_name='notify.Subscriber.msgType', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='retry', full_name='notify.Subscriber.retry', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subscribeInfo', full_name='notify.Subscriber.subscribeInfo', index=7,
      number=8, type=11, cpp_type=10, label=3,
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
  serialized_start=79,
  serialized_end=250,
)

_SUBSCRIBER.fields_by_name['subscribeInfo'].message_type = dc__console__sdk_dot_model_dot_notify_dot_subscribe__info__pb2._SUBSCRIBEINFO
DESCRIPTOR.message_types_by_name['Subscriber'] = _SUBSCRIBER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Subscriber = _reflection.GeneratedProtocolMessageType('Subscriber', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBER,
  '__module__' : 'subscriber_pb2'
  # @@protoc_insertion_point(class_scope:notify.Subscriber)
  })
_sym_db.RegisterMessage(Subscriber)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
