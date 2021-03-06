# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: update_portrait.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from capacity_admin_sdk.model.capacity_admin import portrait_config_pb2 as capacity__admin__sdk_dot_model_dot_capacity__admin_dot_portrait__config__pb2
from capacity_admin_sdk.model.capacity_admin import portrait_pb2 as capacity__admin__sdk_dot_model_dot_capacity__admin_dot_portrait__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='update_portrait.proto',
  package='portrait',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x15update_portrait.proto\x12\x08portrait\x1a=capacity_admin_sdk/model/capacity_admin/portrait_config.proto\x1a\x36\x63\x61pacity_admin_sdk/model/capacity_admin/portrait.proto\"\x96\x01\n\x15UpdatePortraitRequest\x12\x12\n\nportraitId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07\x63harset\x18\x03 \x01(\t\x12\x0c\n\x04user\x18\x04 \x01(\t\x12\x0c\n\x04memo\x18\x05 \x01(\t\x12.\n\x06\x63onfig\x18\x06 \x01(\x0b\x32\x1e.capacity_admin.PortraitConfig\"y\n\x1dUpdatePortraitResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12&\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x18.capacity_admin.Portraitb\x06proto3')
  ,
  dependencies=[capacity__admin__sdk_dot_model_dot_capacity__admin_dot_portrait__config__pb2.DESCRIPTOR,capacity__admin__sdk_dot_model_dot_capacity__admin_dot_portrait__pb2.DESCRIPTOR,])




_UPDATEPORTRAITREQUEST = _descriptor.Descriptor(
  name='UpdatePortraitRequest',
  full_name='portrait.UpdatePortraitRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='portraitId', full_name='portrait.UpdatePortraitRequest.portraitId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='portrait.UpdatePortraitRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='charset', full_name='portrait.UpdatePortraitRequest.charset', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='portrait.UpdatePortraitRequest.user', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='portrait.UpdatePortraitRequest.memo', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config', full_name='portrait.UpdatePortraitRequest.config', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
  serialized_start=155,
  serialized_end=305,
)


_UPDATEPORTRAITRESPONSEWRAPPER = _descriptor.Descriptor(
  name='UpdatePortraitResponseWrapper',
  full_name='portrait.UpdatePortraitResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='portrait.UpdatePortraitResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='portrait.UpdatePortraitResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='portrait.UpdatePortraitResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='portrait.UpdatePortraitResponseWrapper.data', index=3,
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
  serialized_start=307,
  serialized_end=428,
)

_UPDATEPORTRAITREQUEST.fields_by_name['config'].message_type = capacity__admin__sdk_dot_model_dot_capacity__admin_dot_portrait__config__pb2._PORTRAITCONFIG
_UPDATEPORTRAITRESPONSEWRAPPER.fields_by_name['data'].message_type = capacity__admin__sdk_dot_model_dot_capacity__admin_dot_portrait__pb2._PORTRAIT
DESCRIPTOR.message_types_by_name['UpdatePortraitRequest'] = _UPDATEPORTRAITREQUEST
DESCRIPTOR.message_types_by_name['UpdatePortraitResponseWrapper'] = _UPDATEPORTRAITRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdatePortraitRequest = _reflection.GeneratedProtocolMessageType('UpdatePortraitRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPORTRAITREQUEST,
  '__module__' : 'update_portrait_pb2'
  # @@protoc_insertion_point(class_scope:portrait.UpdatePortraitRequest)
  })
_sym_db.RegisterMessage(UpdatePortraitRequest)

UpdatePortraitResponseWrapper = _reflection.GeneratedProtocolMessageType('UpdatePortraitResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPORTRAITRESPONSEWRAPPER,
  '__module__' : 'update_portrait_pb2'
  # @@protoc_insertion_point(class_scope:portrait.UpdatePortraitResponseWrapper)
  })
_sym_db.RegisterMessage(UpdatePortraitResponseWrapper)


# @@protoc_insertion_point(module_scope)
