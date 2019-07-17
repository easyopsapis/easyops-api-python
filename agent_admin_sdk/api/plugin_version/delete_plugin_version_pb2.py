# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: delete_plugin_version.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='delete_plugin_version.proto',
  package='plugin_version',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1b\x64\x65lete_plugin_version.proto\x12\x0eplugin_version\"7\n\x1a\x44\x65letePluginVersionRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05verId\x18\x02 \x01(\t\")\n\x1b\x44\x65letePluginVersionResponse\x12\n\n\x02id\x18\x01 \x01(\t\"\x91\x01\n\"DeletePluginVersionResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x39\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32+.plugin_version.DeletePluginVersionResponseb\x06proto3')
)




_DELETEPLUGINVERSIONREQUEST = _descriptor.Descriptor(
  name='DeletePluginVersionRequest',
  full_name='plugin_version.DeletePluginVersionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='plugin_version.DeletePluginVersionRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='verId', full_name='plugin_version.DeletePluginVersionRequest.verId', index=1,
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
  serialized_start=47,
  serialized_end=102,
)


_DELETEPLUGINVERSIONRESPONSE = _descriptor.Descriptor(
  name='DeletePluginVersionResponse',
  full_name='plugin_version.DeletePluginVersionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='plugin_version.DeletePluginVersionResponse.id', index=0,
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
  serialized_start=104,
  serialized_end=145,
)


_DELETEPLUGINVERSIONRESPONSEWRAPPER = _descriptor.Descriptor(
  name='DeletePluginVersionResponseWrapper',
  full_name='plugin_version.DeletePluginVersionResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='plugin_version.DeletePluginVersionResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='plugin_version.DeletePluginVersionResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='plugin_version.DeletePluginVersionResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='plugin_version.DeletePluginVersionResponseWrapper.data', index=3,
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
  serialized_start=148,
  serialized_end=293,
)

_DELETEPLUGINVERSIONRESPONSEWRAPPER.fields_by_name['data'].message_type = _DELETEPLUGINVERSIONRESPONSE
DESCRIPTOR.message_types_by_name['DeletePluginVersionRequest'] = _DELETEPLUGINVERSIONREQUEST
DESCRIPTOR.message_types_by_name['DeletePluginVersionResponse'] = _DELETEPLUGINVERSIONRESPONSE
DESCRIPTOR.message_types_by_name['DeletePluginVersionResponseWrapper'] = _DELETEPLUGINVERSIONRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeletePluginVersionRequest = _reflection.GeneratedProtocolMessageType('DeletePluginVersionRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETEPLUGINVERSIONREQUEST,
  __module__ = 'delete_plugin_version_pb2'
  # @@protoc_insertion_point(class_scope:plugin_version.DeletePluginVersionRequest)
  ))
_sym_db.RegisterMessage(DeletePluginVersionRequest)

DeletePluginVersionResponse = _reflection.GeneratedProtocolMessageType('DeletePluginVersionResponse', (_message.Message,), dict(
  DESCRIPTOR = _DELETEPLUGINVERSIONRESPONSE,
  __module__ = 'delete_plugin_version_pb2'
  # @@protoc_insertion_point(class_scope:plugin_version.DeletePluginVersionResponse)
  ))
_sym_db.RegisterMessage(DeletePluginVersionResponse)

DeletePluginVersionResponseWrapper = _reflection.GeneratedProtocolMessageType('DeletePluginVersionResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _DELETEPLUGINVERSIONRESPONSEWRAPPER,
  __module__ = 'delete_plugin_version_pb2'
  # @@protoc_insertion_point(class_scope:plugin_version.DeletePluginVersionResponseWrapper)
  ))
_sym_db.RegisterMessage(DeletePluginVersionResponseWrapper)


# @@protoc_insertion_point(module_scope)