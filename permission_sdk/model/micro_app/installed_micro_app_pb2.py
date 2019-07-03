# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: installed_micro_app.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='installed_micro_app.proto',
  package='micro_app',
  syntax='proto3',
  serialized_options=_b('ZCgo.easyops.local/contracts/protorepo-models/easyops/model/micro_app'),
  serialized_pb=_b('\n\x19installed_micro_app.proto\x12\tmicro_app\"\xcc\x01\n\x11InstalledMicroApp\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x61ppId\x18\x02 \x01(\t\x12\x31\n\x05icons\x18\x03 \x01(\x0b\x32\".micro_app.InstalledMicroApp.Icons\x12\x12\n\nstoryboard\x18\x04 \x01(\t\x12\x0c\n\x04tags\x18\x05 \x03(\t\x12\x16\n\x0e\x63urrentVersion\x18\x06 \x01(\t\x12\x15\n\rinstallStatus\x18\x07 \x01(\t\x1a\x16\n\x05Icons\x12\r\n\x05large\x18\x01 \x01(\tBEZCgo.easyops.local/contracts/protorepo-models/easyops/model/micro_appb\x06proto3')
)




_INSTALLEDMICROAPP_ICONS = _descriptor.Descriptor(
  name='Icons',
  full_name='micro_app.InstalledMicroApp.Icons',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='large', full_name='micro_app.InstalledMicroApp.Icons.large', index=0,
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
  serialized_start=223,
  serialized_end=245,
)

_INSTALLEDMICROAPP = _descriptor.Descriptor(
  name='InstalledMicroApp',
  full_name='micro_app.InstalledMicroApp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='micro_app.InstalledMicroApp.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='appId', full_name='micro_app.InstalledMicroApp.appId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icons', full_name='micro_app.InstalledMicroApp.icons', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='storyboard', full_name='micro_app.InstalledMicroApp.storyboard', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='micro_app.InstalledMicroApp.tags', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currentVersion', full_name='micro_app.InstalledMicroApp.currentVersion', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='installStatus', full_name='micro_app.InstalledMicroApp.installStatus', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_INSTALLEDMICROAPP_ICONS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=245,
)

_INSTALLEDMICROAPP_ICONS.containing_type = _INSTALLEDMICROAPP
_INSTALLEDMICROAPP.fields_by_name['icons'].message_type = _INSTALLEDMICROAPP_ICONS
DESCRIPTOR.message_types_by_name['InstalledMicroApp'] = _INSTALLEDMICROAPP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InstalledMicroApp = _reflection.GeneratedProtocolMessageType('InstalledMicroApp', (_message.Message,), dict(

  Icons = _reflection.GeneratedProtocolMessageType('Icons', (_message.Message,), dict(
    DESCRIPTOR = _INSTALLEDMICROAPP_ICONS,
    __module__ = 'installed_micro_app_pb2'
    # @@protoc_insertion_point(class_scope:micro_app.InstalledMicroApp.Icons)
    ))
  ,
  DESCRIPTOR = _INSTALLEDMICROAPP,
  __module__ = 'installed_micro_app_pb2'
  # @@protoc_insertion_point(class_scope:micro_app.InstalledMicroApp)
  ))
_sym_db.RegisterMessage(InstalledMicroApp)
_sym_db.RegisterMessage(InstalledMicroApp.Icons)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)