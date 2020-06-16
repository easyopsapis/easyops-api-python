# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: settings.proto

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
  name='settings.proto',
  package='api_gateway',
  syntax='proto3',
  serialized_options=_b('ZEgo.easyops.local/contracts/protorepo-models/easyops/model/api_gateway'),
  serialized_pb=_b('\n\x0esettings.proto\x12\x0b\x61pi_gateway\x1a\x1cgoogle/protobuf/struct.proto\"\xd3\x01\n\x08Settings\x12-\n\x0c\x66\x65\x61tureFlags\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x10\n\x08homepage\x18\x02 \x01(\t\x12&\n\x05\x62rand\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x32\n\tlaunchpad\x18\x04 \x01(\x0b\x32\x1f.api_gateway.Settings.Launchpad\x1a*\n\tLaunchpad\x12\x0f\n\x07\x63olumns\x18\x01 \x01(\x05\x12\x0c\n\x04rows\x18\x02 \x01(\x05\x42GZEgo.easyops.local/contracts/protorepo-models/easyops/model/api_gatewayb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_SETTINGS_LAUNCHPAD = _descriptor.Descriptor(
  name='Launchpad',
  full_name='api_gateway.Settings.Launchpad',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='columns', full_name='api_gateway.Settings.Launchpad.columns', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rows', full_name='api_gateway.Settings.Launchpad.rows', index=1,
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
  serialized_start=231,
  serialized_end=273,
)

_SETTINGS = _descriptor.Descriptor(
  name='Settings',
  full_name='api_gateway.Settings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='featureFlags', full_name='api_gateway.Settings.featureFlags', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='homepage', full_name='api_gateway.Settings.homepage', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='brand', full_name='api_gateway.Settings.brand', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='launchpad', full_name='api_gateway.Settings.launchpad', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SETTINGS_LAUNCHPAD, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=273,
)

_SETTINGS_LAUNCHPAD.containing_type = _SETTINGS
_SETTINGS.fields_by_name['featureFlags'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SETTINGS.fields_by_name['brand'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SETTINGS.fields_by_name['launchpad'].message_type = _SETTINGS_LAUNCHPAD
DESCRIPTOR.message_types_by_name['Settings'] = _SETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Settings = _reflection.GeneratedProtocolMessageType('Settings', (_message.Message,), {

  'Launchpad' : _reflection.GeneratedProtocolMessageType('Launchpad', (_message.Message,), {
    'DESCRIPTOR' : _SETTINGS_LAUNCHPAD,
    '__module__' : 'settings_pb2'
    # @@protoc_insertion_point(class_scope:api_gateway.Settings.Launchpad)
    })
  ,
  'DESCRIPTOR' : _SETTINGS,
  '__module__' : 'settings_pb2'
  # @@protoc_insertion_point(class_scope:api_gateway.Settings)
  })
_sym_db.RegisterMessage(Settings)
_sym_db.RegisterMessage(Settings.Launchpad)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)