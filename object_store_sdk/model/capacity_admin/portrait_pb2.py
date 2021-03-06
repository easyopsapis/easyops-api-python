# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: portrait.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from object_store_sdk.model.capacity_admin import portrait_config_pb2 as object__store__sdk_dot_model_dot_capacity__admin_dot_portrait__config__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='portrait.proto',
  package='capacity_admin',
  syntax='proto3',
  serialized_options=_b('ZHgo.easyops.local/contracts/protorepo-models/easyops/model/capacity_admin'),
  serialized_pb=_b('\n\x0eportrait.proto\x12\x0e\x63\x61pacity_admin\x1a;object_store_sdk/model/capacity_admin/portrait_config.proto\"\xa9\x01\n\x08Portrait\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07\x63harset\x18\x03 \x01(\t\x12\x0c\n\x04user\x18\x04 \x01(\t\x12\x0c\n\x04memo\x18\x05 \x01(\t\x12.\n\x06\x63onfig\x18\x06 \x01(\x0b\x32\x1e.capacity_admin.PortraitConfig\x12\r\n\x05\x63time\x18\x07 \x01(\t\x12\x0f\n\x07\x63reator\x18\x08 \x01(\tBJZHgo.easyops.local/contracts/protorepo-models/easyops/model/capacity_adminb\x06proto3')
  ,
  dependencies=[object__store__sdk_dot_model_dot_capacity__admin_dot_portrait__config__pb2.DESCRIPTOR,])




_PORTRAIT = _descriptor.Descriptor(
  name='Portrait',
  full_name='capacity_admin.Portrait',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='capacity_admin.Portrait.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='capacity_admin.Portrait.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='charset', full_name='capacity_admin.Portrait.charset', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='capacity_admin.Portrait.user', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='capacity_admin.Portrait.memo', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config', full_name='capacity_admin.Portrait.config', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='capacity_admin.Portrait.ctime', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='capacity_admin.Portrait.creator', index=7,
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
  serialized_start=96,
  serialized_end=265,
)

_PORTRAIT.fields_by_name['config'].message_type = object__store__sdk_dot_model_dot_capacity__admin_dot_portrait__config__pb2._PORTRAITCONFIG
DESCRIPTOR.message_types_by_name['Portrait'] = _PORTRAIT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Portrait = _reflection.GeneratedProtocolMessageType('Portrait', (_message.Message,), {
  'DESCRIPTOR' : _PORTRAIT,
  '__module__' : 'portrait_pb2'
  # @@protoc_insertion_point(class_scope:capacity_admin.Portrait)
  })
_sym_db.RegisterMessage(Portrait)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
