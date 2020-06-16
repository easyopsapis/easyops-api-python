# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app_health_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from idcmanager_sdk.model.monitor_config import app_health_config_variable_pb2 as idcmanager__sdk_dot_model_dot_monitor__config_dot_app__health__config__variable__pb2
from idcmanager_sdk.model.monitor_config import app_health_config_layer_pb2 as idcmanager__sdk_dot_model_dot_monitor__config_dot_app__health__config__layer__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='app_health_config.proto',
  package='monitor_config',
  syntax='proto3',
  serialized_options=_b('ZHgo.easyops.local/contracts/protorepo-models/easyops/model/monitor_config'),
  serialized_pb=_b('\n\x17\x61pp_health_config.proto\x12\x0emonitor_config\x1a\x44idcmanager_sdk/model/monitor_config/app_health_config_variable.proto\x1a\x41idcmanager_sdk/model/monitor_config/app_health_config_layer.proto\"\x81\x02\n\x0f\x41ppHealthConfig\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x12\n\nversion_id\x18\x03 \x01(\t\x12\x0f\n\x07\x63reator\x18\x04 \x01(\t\x12\r\n\x05\x63time\x18\x05 \x01(\x05\x12\x10\n\x08modifier\x18\x06 \x01(\t\x12\r\n\x05mtime\x18\x07 \x01(\x05\x12\x0b\n\x03org\x18\x08 \x01(\x05\x12:\n\tvariables\x18\t \x03(\x0b\x32\'.monitor_config.AppHealthConfigVariable\x12\x34\n\x06layers\x18\n \x03(\x0b\x32$.monitor_config.AppHealthConfigLayerBJZHgo.easyops.local/contracts/protorepo-models/easyops/model/monitor_configb\x06proto3')
  ,
  dependencies=[idcmanager__sdk_dot_model_dot_monitor__config_dot_app__health__config__variable__pb2.DESCRIPTOR,idcmanager__sdk_dot_model_dot_monitor__config_dot_app__health__config__layer__pb2.DESCRIPTOR,])




_APPHEALTHCONFIG = _descriptor.Descriptor(
  name='AppHealthConfig',
  full_name='monitor_config.AppHealthConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='app_id', full_name='monitor_config.AppHealthConfig.app_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='monitor_config.AppHealthConfig.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version_id', full_name='monitor_config.AppHealthConfig.version_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='monitor_config.AppHealthConfig.creator', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='monitor_config.AppHealthConfig.ctime', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='modifier', full_name='monitor_config.AppHealthConfig.modifier', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='monitor_config.AppHealthConfig.mtime', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org', full_name='monitor_config.AppHealthConfig.org', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='variables', full_name='monitor_config.AppHealthConfig.variables', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='layers', full_name='monitor_config.AppHealthConfig.layers', index=9,
      number=10, type=11, cpp_type=10, label=3,
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
  serialized_start=181,
  serialized_end=438,
)

_APPHEALTHCONFIG.fields_by_name['variables'].message_type = idcmanager__sdk_dot_model_dot_monitor__config_dot_app__health__config__variable__pb2._APPHEALTHCONFIGVARIABLE
_APPHEALTHCONFIG.fields_by_name['layers'].message_type = idcmanager__sdk_dot_model_dot_monitor__config_dot_app__health__config__layer__pb2._APPHEALTHCONFIGLAYER
DESCRIPTOR.message_types_by_name['AppHealthConfig'] = _APPHEALTHCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AppHealthConfig = _reflection.GeneratedProtocolMessageType('AppHealthConfig', (_message.Message,), {
  'DESCRIPTOR' : _APPHEALTHCONFIG,
  '__module__' : 'app_health_config_pb2'
  # @@protoc_insertion_point(class_scope:monitor_config.AppHealthConfig)
  })
_sym_db.RegisterMessage(AppHealthConfig)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
