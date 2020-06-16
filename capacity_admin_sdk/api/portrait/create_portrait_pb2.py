# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: create_portrait.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from capacity_admin_sdk.model.capacity_admin import portrait_config_pb2 as capacity__admin__sdk_dot_model_dot_capacity__admin_dot_portrait__config__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='create_portrait.proto',
  package='portrait',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x15\x63reate_portrait.proto\x12\x08portrait\x1a=capacity_admin_sdk/model/capacity_admin/portrait_config.proto\"\x82\x01\n\x15\x43reatePortraitRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x63harset\x18\x02 \x01(\t\x12\x0c\n\x04user\x18\x03 \x01(\t\x12\x0c\n\x04memo\x18\x04 \x01(\t\x12.\n\x06\x63onfig\x18\x05 \x01(\x0b\x32\x1e.capacity_admin.PortraitConfig\",\n\x16\x43reatePortraitResponse\x12\x12\n\ninstanceId\x18\x01 \x01(\t\"\x81\x01\n\x1d\x43reatePortraitResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12.\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32 .portrait.CreatePortraitResponseb\x06proto3')
  ,
  dependencies=[capacity__admin__sdk_dot_model_dot_capacity__admin_dot_portrait__config__pb2.DESCRIPTOR,])




_CREATEPORTRAITREQUEST = _descriptor.Descriptor(
  name='CreatePortraitRequest',
  full_name='portrait.CreatePortraitRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='portrait.CreatePortraitRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='charset', full_name='portrait.CreatePortraitRequest.charset', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='portrait.CreatePortraitRequest.user', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='portrait.CreatePortraitRequest.memo', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config', full_name='portrait.CreatePortraitRequest.config', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=99,
  serialized_end=229,
)


_CREATEPORTRAITRESPONSE = _descriptor.Descriptor(
  name='CreatePortraitResponse',
  full_name='portrait.CreatePortraitResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='portrait.CreatePortraitResponse.instanceId', index=0,
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
  serialized_start=231,
  serialized_end=275,
)


_CREATEPORTRAITRESPONSEWRAPPER = _descriptor.Descriptor(
  name='CreatePortraitResponseWrapper',
  full_name='portrait.CreatePortraitResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='portrait.CreatePortraitResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='portrait.CreatePortraitResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='portrait.CreatePortraitResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='portrait.CreatePortraitResponseWrapper.data', index=3,
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
  serialized_start=278,
  serialized_end=407,
)

_CREATEPORTRAITREQUEST.fields_by_name['config'].message_type = capacity__admin__sdk_dot_model_dot_capacity__admin_dot_portrait__config__pb2._PORTRAITCONFIG
_CREATEPORTRAITRESPONSEWRAPPER.fields_by_name['data'].message_type = _CREATEPORTRAITRESPONSE
DESCRIPTOR.message_types_by_name['CreatePortraitRequest'] = _CREATEPORTRAITREQUEST
DESCRIPTOR.message_types_by_name['CreatePortraitResponse'] = _CREATEPORTRAITRESPONSE
DESCRIPTOR.message_types_by_name['CreatePortraitResponseWrapper'] = _CREATEPORTRAITRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreatePortraitRequest = _reflection.GeneratedProtocolMessageType('CreatePortraitRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEPORTRAITREQUEST,
  '__module__' : 'create_portrait_pb2'
  # @@protoc_insertion_point(class_scope:portrait.CreatePortraitRequest)
  })
_sym_db.RegisterMessage(CreatePortraitRequest)

CreatePortraitResponse = _reflection.GeneratedProtocolMessageType('CreatePortraitResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEPORTRAITRESPONSE,
  '__module__' : 'create_portrait_pb2'
  # @@protoc_insertion_point(class_scope:portrait.CreatePortraitResponse)
  })
_sym_db.RegisterMessage(CreatePortraitResponse)

CreatePortraitResponseWrapper = _reflection.GeneratedProtocolMessageType('CreatePortraitResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _CREATEPORTRAITRESPONSEWRAPPER,
  '__module__' : 'create_portrait_pb2'
  # @@protoc_insertion_point(class_scope:portrait.CreatePortraitResponseWrapper)
  })
_sym_db.RegisterMessage(CreatePortraitResponseWrapper)


# @@protoc_insertion_point(module_scope)