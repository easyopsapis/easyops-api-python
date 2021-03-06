# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_micro_app.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='object_micro_app.proto',
  package='micro_app',
  syntax='proto3',
  serialized_options=_b('ZCgo.easyops.local/contracts/protorepo-models/easyops/model/micro_app'),
  serialized_pb=_b('\n\x16object_micro_app.proto\x12\tmicro_app\"\xbb\x01\n\x0eObjectMicroApp\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08objectId\x18\x02 \x01(\t\x12\x12\n\nmicroAppId\x18\x03 \x01(\t\x12\x14\n\x0cmicroAppName\x18\x04 \x01(\t\x12\x10\n\x08homepage\x18\x05 \x01(\t\x12\x0f\n\x07subPath\x18\x06 \x01(\t\x12\r\n\x05order\x18\x07 \x01(\x05\x12\x0e\n\x06status\x18\x08 \x01(\t\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\t \x01(\t\x12\x0c\n\x04tags\x18\n \x03(\tBEZCgo.easyops.local/contracts/protorepo-models/easyops/model/micro_appb\x06proto3')
)




_OBJECTMICROAPP = _descriptor.Descriptor(
  name='ObjectMicroApp',
  full_name='micro_app.ObjectMicroApp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='micro_app.ObjectMicroApp.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectId', full_name='micro_app.ObjectMicroApp.objectId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='microAppId', full_name='micro_app.ObjectMicroApp.microAppId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='microAppName', full_name='micro_app.ObjectMicroApp.microAppName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='homepage', full_name='micro_app.ObjectMicroApp.homepage', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subPath', full_name='micro_app.ObjectMicroApp.subPath', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order', full_name='micro_app.ObjectMicroApp.order', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='micro_app.ObjectMicroApp.status', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default', full_name='micro_app.ObjectMicroApp.default', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='micro_app.ObjectMicroApp.tags', index=9,
      number=10, type=9, cpp_type=9, label=3,
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
  serialized_start=38,
  serialized_end=225,
)

DESCRIPTOR.message_types_by_name['ObjectMicroApp'] = _OBJECTMICROAPP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ObjectMicroApp = _reflection.GeneratedProtocolMessageType('ObjectMicroApp', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTMICROAPP,
  '__module__' : 'object_micro_app_pb2'
  # @@protoc_insertion_point(class_scope:micro_app.ObjectMicroApp)
  })
_sym_db.RegisterMessage(ObjectMicroApp)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
