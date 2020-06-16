# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: micro_app.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='micro_app.proto',
  package='app_store',
  syntax='proto3',
  serialized_options=_b('ZCgo.easyops.local/contracts/protorepo-models/easyops/model/app_store'),
  serialized_pb=_b('\n\x0fmicro_app.proto\x12\tapp_store\"\xe4\x01\n\x10\x41ppStoreMicroApp\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x30\n\x05icons\x18\x03 \x01(\x0b\x32!.app_store.AppStoreMicroApp.Icons\x12\r\n\x05intro\x18\x04 \x01(\t\x12\x0f\n\x07preview\x18\x05 \x03(\t\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\x10\n\x08homepage\x18\x07 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x08 \x01(\t\x12\x13\n\x0b\x63ontainerId\x18\t \x01(\t\x1a\x16\n\x05Icons\x12\r\n\x05large\x18\x01 \x01(\tBEZCgo.easyops.local/contracts/protorepo-models/easyops/model/app_storeb\x06proto3')
)




_APPSTOREMICROAPP_ICONS = _descriptor.Descriptor(
  name='Icons',
  full_name='app_store.AppStoreMicroApp.Icons',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='large', full_name='app_store.AppStoreMicroApp.Icons.large', index=0,
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
  serialized_start=237,
  serialized_end=259,
)

_APPSTOREMICROAPP = _descriptor.Descriptor(
  name='AppStoreMicroApp',
  full_name='app_store.AppStoreMicroApp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='app_store.AppStoreMicroApp.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='app_store.AppStoreMicroApp.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icons', full_name='app_store.AppStoreMicroApp.icons', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='intro', full_name='app_store.AppStoreMicroApp.intro', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preview', full_name='app_store.AppStoreMicroApp.preview', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='app_store.AppStoreMicroApp.description', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='homepage', full_name='app_store.AppStoreMicroApp.homepage', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='app_store.AppStoreMicroApp.category', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='containerId', full_name='app_store.AppStoreMicroApp.containerId', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_APPSTOREMICROAPP_ICONS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=259,
)

_APPSTOREMICROAPP_ICONS.containing_type = _APPSTOREMICROAPP
_APPSTOREMICROAPP.fields_by_name['icons'].message_type = _APPSTOREMICROAPP_ICONS
DESCRIPTOR.message_types_by_name['AppStoreMicroApp'] = _APPSTOREMICROAPP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AppStoreMicroApp = _reflection.GeneratedProtocolMessageType('AppStoreMicroApp', (_message.Message,), {

  'Icons' : _reflection.GeneratedProtocolMessageType('Icons', (_message.Message,), {
    'DESCRIPTOR' : _APPSTOREMICROAPP_ICONS,
    '__module__' : 'micro_app_pb2'
    # @@protoc_insertion_point(class_scope:app_store.AppStoreMicroApp.Icons)
    })
  ,
  'DESCRIPTOR' : _APPSTOREMICROAPP,
  '__module__' : 'micro_app_pb2'
  # @@protoc_insertion_point(class_scope:app_store.AppStoreMicroApp)
  })
_sym_db.RegisterMessage(AppStoreMicroApp)
_sym_db.RegisterMessage(AppStoreMicroApp.Icons)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
