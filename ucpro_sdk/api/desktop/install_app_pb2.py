# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: install_app.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='install_app.proto',
  package='desktop',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11install_app.proto\x12\x07\x64\x65sktop\"3\n\x11InstallAppRequest\x12\r\n\x05\x61ppId\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\"$\n\x12InstallAppResponse\x12\x0e\n\x06taskId\x18\x01 \x01(\t\"x\n\x19InstallAppResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12)\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1b.desktop.InstallAppResponseb\x06proto3')
)




_INSTALLAPPREQUEST = _descriptor.Descriptor(
  name='InstallAppRequest',
  full_name='desktop.InstallAppRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appId', full_name='desktop.InstallAppRequest.appId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='desktop.InstallAppRequest.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=30,
  serialized_end=81,
)


_INSTALLAPPRESPONSE = _descriptor.Descriptor(
  name='InstallAppResponse',
  full_name='desktop.InstallAppResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='taskId', full_name='desktop.InstallAppResponse.taskId', index=0,
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
  serialized_start=83,
  serialized_end=119,
)


_INSTALLAPPRESPONSEWRAPPER = _descriptor.Descriptor(
  name='InstallAppResponseWrapper',
  full_name='desktop.InstallAppResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='desktop.InstallAppResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='desktop.InstallAppResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='desktop.InstallAppResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='desktop.InstallAppResponseWrapper.data', index=3,
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
  serialized_start=121,
  serialized_end=241,
)

_INSTALLAPPRESPONSEWRAPPER.fields_by_name['data'].message_type = _INSTALLAPPRESPONSE
DESCRIPTOR.message_types_by_name['InstallAppRequest'] = _INSTALLAPPREQUEST
DESCRIPTOR.message_types_by_name['InstallAppResponse'] = _INSTALLAPPRESPONSE
DESCRIPTOR.message_types_by_name['InstallAppResponseWrapper'] = _INSTALLAPPRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InstallAppRequest = _reflection.GeneratedProtocolMessageType('InstallAppRequest', (_message.Message,), dict(
  DESCRIPTOR = _INSTALLAPPREQUEST,
  __module__ = 'install_app_pb2'
  # @@protoc_insertion_point(class_scope:desktop.InstallAppRequest)
  ))
_sym_db.RegisterMessage(InstallAppRequest)

InstallAppResponse = _reflection.GeneratedProtocolMessageType('InstallAppResponse', (_message.Message,), dict(
  DESCRIPTOR = _INSTALLAPPRESPONSE,
  __module__ = 'install_app_pb2'
  # @@protoc_insertion_point(class_scope:desktop.InstallAppResponse)
  ))
_sym_db.RegisterMessage(InstallAppResponse)

InstallAppResponseWrapper = _reflection.GeneratedProtocolMessageType('InstallAppResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _INSTALLAPPRESPONSEWRAPPER,
  __module__ = 'install_app_pb2'
  # @@protoc_insertion_point(class_scope:desktop.InstallAppResponseWrapper)
  ))
_sym_db.RegisterMessage(InstallAppResponseWrapper)


# @@protoc_insertion_point(module_scope)
