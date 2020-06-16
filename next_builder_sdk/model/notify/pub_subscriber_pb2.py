# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pub_subscriber.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pub_subscriber.proto',
  package='notify',
  syntax='proto3',
  serialized_options=_b('Z@go.easyops.local/contracts/protorepo-models/easyops/model/notify'),
  serialized_pb=_b('\n\x14pub_subscriber.proto\x12\x06notify\"\xa9\x01\n\rPubSubscriber\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x61\x64min\x18\x03 \x01(\t\x12\x10\n\x08\x63\x61llback\x18\x04 \x01(\t\x12\x0f\n\x07\x65nsName\x18\x05 \x01(\t\x12\r\n\x05retry\x18\x06 \x01(\x05\x12\r\n\x05mtime\x18\x07 \x01(\t\x12\x10\n\x08_version\x18\x08 \x01(\x05\x12\x14\n\x0ctopicVersion\x18\t \x01(\x05\x42\x42Z@go.easyops.local/contracts/protorepo-models/easyops/model/notifyb\x06proto3')
)




_PUBSUBSCRIBER = _descriptor.Descriptor(
  name='PubSubscriber',
  full_name='notify.PubSubscriber',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='notify.PubSubscriber.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='notify.PubSubscriber.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='admin', full_name='notify.PubSubscriber.admin', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='callback', full_name='notify.PubSubscriber.callback', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ensName', full_name='notify.PubSubscriber.ensName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='retry', full_name='notify.PubSubscriber.retry', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='notify.PubSubscriber.mtime', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='_version', full_name='notify.PubSubscriber._version', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='topicVersion', full_name='notify.PubSubscriber.topicVersion', index=8,
      number=9, type=5, cpp_type=1, label=1,
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
  serialized_start=33,
  serialized_end=202,
)

DESCRIPTOR.message_types_by_name['PubSubscriber'] = _PUBSUBSCRIBER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PubSubscriber = _reflection.GeneratedProtocolMessageType('PubSubscriber', (_message.Message,), {
  'DESCRIPTOR' : _PUBSUBSCRIBER,
  '__module__' : 'pub_subscriber_pb2'
  # @@protoc_insertion_point(class_scope:notify.PubSubscriber)
  })
_sym_db.RegisterMessage(PubSubscriber)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)