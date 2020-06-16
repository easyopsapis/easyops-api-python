# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bootstrap.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api_gateway_sdk.model.api_gateway import storyboard_pb2 as api__gateway__sdk_dot_model_dot_api__gateway_dot_storyboard__pb2
from api_gateway_sdk.model.api_gateway import settings_pb2 as api__gateway__sdk_dot_model_dot_api__gateway_dot_settings__pb2
from api_gateway_sdk.model.api_gateway import desktop_pb2 as api__gateway__sdk_dot_model_dot_api__gateway_dot_desktop__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bootstrap.proto',
  package='bootstrap',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0f\x62ootstrap.proto\x12\tbootstrap\x1a\x32\x61pi_gateway_sdk/model/api_gateway/storyboard.proto\x1a\x30\x61pi_gateway_sdk/model/api_gateway/settings.proto\x1a/api_gateway_sdk/model/api_gateway/desktop.proto\x1a\x1cgoogle/protobuf/struct.proto\"\'\n\x10\x42ootstrapRequest\x12\x13\n\x0b\x63heck_login\x18\x01 \x01(\x08\"\x9e\x02\n\x11\x42ootstrapResponse\x12\'\n\x06navbar\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12,\n\x0bstoryboards\x18\x02 \x03(\x0b\x32\x17.api_gateway.StoryBoard\x12.\n\rbrickPackages\x18\x03 \x03(\x0b\x32\x17.google.protobuf.Struct\x12\x31\n\x10templatePackages\x18\x04 \x03(\x0b\x32\x17.google.protobuf.Struct\x12\'\n\x08settings\x18\x05 \x01(\x0b\x32\x15.api_gateway.Settings\x12&\n\x08\x64\x65sktops\x18\x06 \x03(\x0b\x32\x14.api_gateway.Desktop\"x\n\x18\x42ootstrapResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12*\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1c.bootstrap.BootstrapResponseb\x06proto3')
  ,
  dependencies=[api__gateway__sdk_dot_model_dot_api__gateway_dot_storyboard__pb2.DESCRIPTOR,api__gateway__sdk_dot_model_dot_api__gateway_dot_settings__pb2.DESCRIPTOR,api__gateway__sdk_dot_model_dot_api__gateway_dot_desktop__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_BOOTSTRAPREQUEST = _descriptor.Descriptor(
  name='BootstrapRequest',
  full_name='bootstrap.BootstrapRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='check_login', full_name='bootstrap.BootstrapRequest.check_login', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=211,
  serialized_end=250,
)


_BOOTSTRAPRESPONSE = _descriptor.Descriptor(
  name='BootstrapResponse',
  full_name='bootstrap.BootstrapResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='navbar', full_name='bootstrap.BootstrapResponse.navbar', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='storyboards', full_name='bootstrap.BootstrapResponse.storyboards', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='brickPackages', full_name='bootstrap.BootstrapResponse.brickPackages', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='templatePackages', full_name='bootstrap.BootstrapResponse.templatePackages', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='settings', full_name='bootstrap.BootstrapResponse.settings', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='desktops', full_name='bootstrap.BootstrapResponse.desktops', index=5,
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
  serialized_start=253,
  serialized_end=539,
)


_BOOTSTRAPRESPONSEWRAPPER = _descriptor.Descriptor(
  name='BootstrapResponseWrapper',
  full_name='bootstrap.BootstrapResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='bootstrap.BootstrapResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='bootstrap.BootstrapResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='bootstrap.BootstrapResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='bootstrap.BootstrapResponseWrapper.data', index=3,
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
  serialized_start=541,
  serialized_end=661,
)

_BOOTSTRAPRESPONSE.fields_by_name['navbar'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_BOOTSTRAPRESPONSE.fields_by_name['storyboards'].message_type = api__gateway__sdk_dot_model_dot_api__gateway_dot_storyboard__pb2._STORYBOARD
_BOOTSTRAPRESPONSE.fields_by_name['brickPackages'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_BOOTSTRAPRESPONSE.fields_by_name['templatePackages'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_BOOTSTRAPRESPONSE.fields_by_name['settings'].message_type = api__gateway__sdk_dot_model_dot_api__gateway_dot_settings__pb2._SETTINGS
_BOOTSTRAPRESPONSE.fields_by_name['desktops'].message_type = api__gateway__sdk_dot_model_dot_api__gateway_dot_desktop__pb2._DESKTOP
_BOOTSTRAPRESPONSEWRAPPER.fields_by_name['data'].message_type = _BOOTSTRAPRESPONSE
DESCRIPTOR.message_types_by_name['BootstrapRequest'] = _BOOTSTRAPREQUEST
DESCRIPTOR.message_types_by_name['BootstrapResponse'] = _BOOTSTRAPRESPONSE
DESCRIPTOR.message_types_by_name['BootstrapResponseWrapper'] = _BOOTSTRAPRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BootstrapRequest = _reflection.GeneratedProtocolMessageType('BootstrapRequest', (_message.Message,), {
  'DESCRIPTOR' : _BOOTSTRAPREQUEST,
  '__module__' : 'bootstrap_pb2'
  # @@protoc_insertion_point(class_scope:bootstrap.BootstrapRequest)
  })
_sym_db.RegisterMessage(BootstrapRequest)

BootstrapResponse = _reflection.GeneratedProtocolMessageType('BootstrapResponse', (_message.Message,), {
  'DESCRIPTOR' : _BOOTSTRAPRESPONSE,
  '__module__' : 'bootstrap_pb2'
  # @@protoc_insertion_point(class_scope:bootstrap.BootstrapResponse)
  })
_sym_db.RegisterMessage(BootstrapResponse)

BootstrapResponseWrapper = _reflection.GeneratedProtocolMessageType('BootstrapResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _BOOTSTRAPRESPONSEWRAPPER,
  '__module__' : 'bootstrap_pb2'
  # @@protoc_insertion_point(class_scope:bootstrap.BootstrapResponseWrapper)
  })
_sym_db.RegisterMessage(BootstrapResponseWrapper)


# @@protoc_insertion_point(module_scope)
