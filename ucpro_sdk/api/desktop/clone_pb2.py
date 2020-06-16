# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: clone.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ucpro_sdk.model.micro_app import installed_micro_app_pb2 as ucpro__sdk_dot_model_dot_micro__app_dot_installed__micro__app__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='clone.proto',
  package='desktop',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0b\x63lone.proto\x12\x07\x64\x65sktop\x1a\x33ucpro_sdk/model/micro_app/installed_micro_app.proto\x1a\x1cgoogle/protobuf/struct.proto\"R\n\x0c\x43loneRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x61ppId\x18\x02 \x01(\t\x12\x13\n\x0bparentAppId\x18\x03 \x01(\t\x12\x10\n\x08homepage\x18\x04 \x01(\t\"t\n\x14\x43loneResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12*\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1c.micro_app.InstalledMicroAppb\x06proto3')
  ,
  dependencies=[ucpro__sdk_dot_model_dot_micro__app_dot_installed__micro__app__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_CLONEREQUEST = _descriptor.Descriptor(
  name='CloneRequest',
  full_name='desktop.CloneRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='desktop.CloneRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='appId', full_name='desktop.CloneRequest.appId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parentAppId', full_name='desktop.CloneRequest.parentAppId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='homepage', full_name='desktop.CloneRequest.homepage', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=107,
  serialized_end=189,
)


_CLONERESPONSEWRAPPER = _descriptor.Descriptor(
  name='CloneResponseWrapper',
  full_name='desktop.CloneResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='desktop.CloneResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='desktop.CloneResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='desktop.CloneResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='desktop.CloneResponseWrapper.data', index=3,
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
  serialized_start=191,
  serialized_end=307,
)

_CLONERESPONSEWRAPPER.fields_by_name['data'].message_type = ucpro__sdk_dot_model_dot_micro__app_dot_installed__micro__app__pb2._INSTALLEDMICROAPP
DESCRIPTOR.message_types_by_name['CloneRequest'] = _CLONEREQUEST
DESCRIPTOR.message_types_by_name['CloneResponseWrapper'] = _CLONERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CloneRequest = _reflection.GeneratedProtocolMessageType('CloneRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLONEREQUEST,
  '__module__' : 'clone_pb2'
  # @@protoc_insertion_point(class_scope:desktop.CloneRequest)
  })
_sym_db.RegisterMessage(CloneRequest)

CloneResponseWrapper = _reflection.GeneratedProtocolMessageType('CloneResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _CLONERESPONSEWRAPPER,
  '__module__' : 'clone_pb2'
  # @@protoc_insertion_point(class_scope:desktop.CloneResponseWrapper)
  })
_sym_db.RegisterMessage(CloneResponseWrapper)


# @@protoc_insertion_point(module_scope)