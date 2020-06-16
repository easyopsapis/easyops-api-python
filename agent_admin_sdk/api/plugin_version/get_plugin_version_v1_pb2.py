# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_plugin_version_v1.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from agent_admin_sdk.model.agent_admin import plugin_pb2 as agent__admin__sdk_dot_model_dot_agent__admin_dot_plugin__pb2
from agent_admin_sdk.model.agent_admin import plugin_version_pb2 as agent__admin__sdk_dot_model_dot_agent__admin_dot_plugin__version__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_plugin_version_v1.proto',
  package='plugin_version',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1bget_plugin_version_v1.proto\x12\x0eplugin_version\x1a.agent_admin_sdk/model/agent_admin/plugin.proto\x1a\x36\x61gent_admin_sdk/model/agent_admin/plugin_version.proto\"6\n\x19GetPluginVersionV1Request\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05verId\x18\x02 \x01(\t\"\x8c\x02\n\x1aGetPluginVersionV1Response\x12\x13\n\x0bversionName\x18\x01 \x01(\t\x12(\n\x0b\x61gentPlugin\x18\x02 \x01(\x0b\x32\x13.agent_admin.Plugin\x12/\n\x0b\x62\x61seVersion\x18\x03 \x01(\x0b\x32\x1a.agent_admin.PluginVersion\x12\n\n\x02id\x18\x04 \x01(\t\x12\x15\n\rrepoVersionId\x18\x05 \x01(\t\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x0c\n\x04memo\x18\x07 \x01(\t\x12\x10\n\x08pluginId\x18\x08 \x01(\t\x12\x0f\n\x07\x63reator\x18\t \x01(\t\x12\r\n\x05\x63time\x18\n \x01(\x05\x12\r\n\x05mtime\x18\x0b \x01(\x05\"\x8f\x01\n!GetPluginVersionV1ResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x38\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32*.plugin_version.GetPluginVersionV1Responseb\x06proto3')
  ,
  dependencies=[agent__admin__sdk_dot_model_dot_agent__admin_dot_plugin__pb2.DESCRIPTOR,agent__admin__sdk_dot_model_dot_agent__admin_dot_plugin__version__pb2.DESCRIPTOR,])




_GETPLUGINVERSIONV1REQUEST = _descriptor.Descriptor(
  name='GetPluginVersionV1Request',
  full_name='plugin_version.GetPluginVersionV1Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='plugin_version.GetPluginVersionV1Request.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='verId', full_name='plugin_version.GetPluginVersionV1Request.verId', index=1,
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
  serialized_start=151,
  serialized_end=205,
)


_GETPLUGINVERSIONV1RESPONSE = _descriptor.Descriptor(
  name='GetPluginVersionV1Response',
  full_name='plugin_version.GetPluginVersionV1Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='versionName', full_name='plugin_version.GetPluginVersionV1Response.versionName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agentPlugin', full_name='plugin_version.GetPluginVersionV1Response.agentPlugin', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='baseVersion', full_name='plugin_version.GetPluginVersionV1Response.baseVersion', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='plugin_version.GetPluginVersionV1Response.id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repoVersionId', full_name='plugin_version.GetPluginVersionV1Response.repoVersionId', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='plugin_version.GetPluginVersionV1Response.name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='plugin_version.GetPluginVersionV1Response.memo', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pluginId', full_name='plugin_version.GetPluginVersionV1Response.pluginId', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='plugin_version.GetPluginVersionV1Response.creator', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='plugin_version.GetPluginVersionV1Response.ctime', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='plugin_version.GetPluginVersionV1Response.mtime', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=208,
  serialized_end=476,
)


_GETPLUGINVERSIONV1RESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetPluginVersionV1ResponseWrapper',
  full_name='plugin_version.GetPluginVersionV1ResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='plugin_version.GetPluginVersionV1ResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='plugin_version.GetPluginVersionV1ResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='plugin_version.GetPluginVersionV1ResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='plugin_version.GetPluginVersionV1ResponseWrapper.data', index=3,
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
  serialized_start=479,
  serialized_end=622,
)

_GETPLUGINVERSIONV1RESPONSE.fields_by_name['agentPlugin'].message_type = agent__admin__sdk_dot_model_dot_agent__admin_dot_plugin__pb2._PLUGIN
_GETPLUGINVERSIONV1RESPONSE.fields_by_name['baseVersion'].message_type = agent__admin__sdk_dot_model_dot_agent__admin_dot_plugin__version__pb2._PLUGINVERSION
_GETPLUGINVERSIONV1RESPONSEWRAPPER.fields_by_name['data'].message_type = _GETPLUGINVERSIONV1RESPONSE
DESCRIPTOR.message_types_by_name['GetPluginVersionV1Request'] = _GETPLUGINVERSIONV1REQUEST
DESCRIPTOR.message_types_by_name['GetPluginVersionV1Response'] = _GETPLUGINVERSIONV1RESPONSE
DESCRIPTOR.message_types_by_name['GetPluginVersionV1ResponseWrapper'] = _GETPLUGINVERSIONV1RESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetPluginVersionV1Request = _reflection.GeneratedProtocolMessageType('GetPluginVersionV1Request', (_message.Message,), {
  'DESCRIPTOR' : _GETPLUGINVERSIONV1REQUEST,
  '__module__' : 'get_plugin_version_v1_pb2'
  # @@protoc_insertion_point(class_scope:plugin_version.GetPluginVersionV1Request)
  })
_sym_db.RegisterMessage(GetPluginVersionV1Request)

GetPluginVersionV1Response = _reflection.GeneratedProtocolMessageType('GetPluginVersionV1Response', (_message.Message,), {
  'DESCRIPTOR' : _GETPLUGINVERSIONV1RESPONSE,
  '__module__' : 'get_plugin_version_v1_pb2'
  # @@protoc_insertion_point(class_scope:plugin_version.GetPluginVersionV1Response)
  })
_sym_db.RegisterMessage(GetPluginVersionV1Response)

GetPluginVersionV1ResponseWrapper = _reflection.GeneratedProtocolMessageType('GetPluginVersionV1ResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _GETPLUGINVERSIONV1RESPONSEWRAPPER,
  '__module__' : 'get_plugin_version_v1_pb2'
  # @@protoc_insertion_point(class_scope:plugin_version.GetPluginVersionV1ResponseWrapper)
  })
_sym_db.RegisterMessage(GetPluginVersionV1ResponseWrapper)


# @@protoc_insertion_point(module_scope)
