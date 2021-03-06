# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_install_key.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_install_key.proto',
  package='agent',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x15get_install_key.proto\x12\x05\x61gent\"S\n\x15GetInstallKeyResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\r\n\x05\x65rror\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\t\"|\n\x1cGetInstallKeyResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12*\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1c.agent.GetInstallKeyResponseb\x06proto3')
)




_GETINSTALLKEYRESPONSE = _descriptor.Descriptor(
  name='GetInstallKeyResponse',
  full_name='agent.GetInstallKeyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='agent.GetInstallKeyResponse.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='agent.GetInstallKeyResponse.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='agent.GetInstallKeyResponse.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='agent.GetInstallKeyResponse.data', index=3,
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
  serialized_start=32,
  serialized_end=115,
)


_GETINSTALLKEYRESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetInstallKeyResponseWrapper',
  full_name='agent.GetInstallKeyResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='agent.GetInstallKeyResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='agent.GetInstallKeyResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='agent.GetInstallKeyResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='agent.GetInstallKeyResponseWrapper.data', index=3,
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
  serialized_start=117,
  serialized_end=241,
)

_GETINSTALLKEYRESPONSEWRAPPER.fields_by_name['data'].message_type = _GETINSTALLKEYRESPONSE
DESCRIPTOR.message_types_by_name['GetInstallKeyResponse'] = _GETINSTALLKEYRESPONSE
DESCRIPTOR.message_types_by_name['GetInstallKeyResponseWrapper'] = _GETINSTALLKEYRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetInstallKeyResponse = _reflection.GeneratedProtocolMessageType('GetInstallKeyResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETINSTALLKEYRESPONSE,
  '__module__' : 'get_install_key_pb2'
  # @@protoc_insertion_point(class_scope:agent.GetInstallKeyResponse)
  })
_sym_db.RegisterMessage(GetInstallKeyResponse)

GetInstallKeyResponseWrapper = _reflection.GeneratedProtocolMessageType('GetInstallKeyResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _GETINSTALLKEYRESPONSEWRAPPER,
  '__module__' : 'get_install_key_pb2'
  # @@protoc_insertion_point(class_scope:agent.GetInstallKeyResponseWrapper)
  })
_sym_db.RegisterMessage(GetInstallKeyResponseWrapper)


# @@protoc_insertion_point(module_scope)
