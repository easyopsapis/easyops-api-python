# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: metric.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='metric.proto',
  package='collector_service',
  syntax='proto3',
  serialized_options=_b('ZKgo.easyops.local/contracts/protorepo-models/easyops/model/collector_service'),
  serialized_pb=_b('\n\x0cmetric.proto\x12\x11\x63ollector_service\"\xfc\x04\n\x0f\x43ollectorMetric\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07keyName\x18\x02 \x01(\t\x12\x0e\n\x06labels\x18\x03 \x03(\t\x12\x10\n\x08metricId\x18\x04 \x01(\t\x12\x0f\n\x07version\x18\x05 \x01(\x05\x12\x0b\n\x03key\x18\x06 \x01(\t\x12\x12\n\nmetricType\x18\x07 \x01(\t\x12\x10\n\x08\x64\x61taType\x18\x08 \x01(\t\x12\x11\n\tagentType\x18\t \x01(\t\x12?\n\ttagDefine\x18\n \x03(\x0b\x32,.collector_service.CollectorMetric.TagDefine\x12\x43\n\x0bparamDefine\x18\x0b \x03(\x0b\x32..collector_service.CollectorMetric.ParamDefine\x12\x0c\n\x04help\x18\x0c \x01(\t\x12\x0c\n\x04unit\x18\r \x01(\t\x12\x15\n\rmetricVersion\x18\x0e \x01(\x05\x12\x39\n\x06plugin\x18\x0f \x01(\x0b\x32).collector_service.CollectorMetric.Plugin\x1a\x64\n\tTagDefine\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x02 \x01(\t\x12\x10\n\x08readOnly\x18\x03 \x01(\x08\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x11\n\tvalueType\x18\x05 \x01(\t\x1aQ\n\x0bParamDefine\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tvalueType\x18\x02 \x01(\t\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x03 \x01(\t\x12\x10\n\x08readOnly\x18\x04 \x01(\x08\x1a$\n\x06Plugin\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\tBMZKgo.easyops.local/contracts/protorepo-models/easyops/model/collector_serviceb\x06proto3')
)




_COLLECTORMETRIC_TAGDEFINE = _descriptor.Descriptor(
  name='TagDefine',
  full_name='collector_service.CollectorMetric.TagDefine',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='collector_service.CollectorMetric.TagDefine.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default', full_name='collector_service.CollectorMetric.TagDefine.default', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readOnly', full_name='collector_service.CollectorMetric.TagDefine.readOnly', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='collector_service.CollectorMetric.TagDefine.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='valueType', full_name='collector_service.CollectorMetric.TagDefine.valueType', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=451,
  serialized_end=551,
)

_COLLECTORMETRIC_PARAMDEFINE = _descriptor.Descriptor(
  name='ParamDefine',
  full_name='collector_service.CollectorMetric.ParamDefine',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='collector_service.CollectorMetric.ParamDefine.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='valueType', full_name='collector_service.CollectorMetric.ParamDefine.valueType', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default', full_name='collector_service.CollectorMetric.ParamDefine.default', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readOnly', full_name='collector_service.CollectorMetric.ParamDefine.readOnly', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=553,
  serialized_end=634,
)

_COLLECTORMETRIC_PLUGIN = _descriptor.Descriptor(
  name='Plugin',
  full_name='collector_service.CollectorMetric.Plugin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='collector_service.CollectorMetric.Plugin.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='collector_service.CollectorMetric.Plugin.path', index=1,
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
  serialized_start=636,
  serialized_end=672,
)

_COLLECTORMETRIC = _descriptor.Descriptor(
  name='CollectorMetric',
  full_name='collector_service.CollectorMetric',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='collector_service.CollectorMetric.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keyName', full_name='collector_service.CollectorMetric.keyName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='collector_service.CollectorMetric.labels', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metricId', full_name='collector_service.CollectorMetric.metricId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='collector_service.CollectorMetric.version', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='collector_service.CollectorMetric.key', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metricType', full_name='collector_service.CollectorMetric.metricType', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataType', full_name='collector_service.CollectorMetric.dataType', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agentType', full_name='collector_service.CollectorMetric.agentType', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tagDefine', full_name='collector_service.CollectorMetric.tagDefine', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paramDefine', full_name='collector_service.CollectorMetric.paramDefine', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='help', full_name='collector_service.CollectorMetric.help', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unit', full_name='collector_service.CollectorMetric.unit', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metricVersion', full_name='collector_service.CollectorMetric.metricVersion', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='plugin', full_name='collector_service.CollectorMetric.plugin', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_COLLECTORMETRIC_TAGDEFINE, _COLLECTORMETRIC_PARAMDEFINE, _COLLECTORMETRIC_PLUGIN, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=672,
)

_COLLECTORMETRIC_TAGDEFINE.containing_type = _COLLECTORMETRIC
_COLLECTORMETRIC_PARAMDEFINE.containing_type = _COLLECTORMETRIC
_COLLECTORMETRIC_PLUGIN.containing_type = _COLLECTORMETRIC
_COLLECTORMETRIC.fields_by_name['tagDefine'].message_type = _COLLECTORMETRIC_TAGDEFINE
_COLLECTORMETRIC.fields_by_name['paramDefine'].message_type = _COLLECTORMETRIC_PARAMDEFINE
_COLLECTORMETRIC.fields_by_name['plugin'].message_type = _COLLECTORMETRIC_PLUGIN
DESCRIPTOR.message_types_by_name['CollectorMetric'] = _COLLECTORMETRIC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CollectorMetric = _reflection.GeneratedProtocolMessageType('CollectorMetric', (_message.Message,), {

  'TagDefine' : _reflection.GeneratedProtocolMessageType('TagDefine', (_message.Message,), {
    'DESCRIPTOR' : _COLLECTORMETRIC_TAGDEFINE,
    '__module__' : 'metric_pb2'
    # @@protoc_insertion_point(class_scope:collector_service.CollectorMetric.TagDefine)
    })
  ,

  'ParamDefine' : _reflection.GeneratedProtocolMessageType('ParamDefine', (_message.Message,), {
    'DESCRIPTOR' : _COLLECTORMETRIC_PARAMDEFINE,
    '__module__' : 'metric_pb2'
    # @@protoc_insertion_point(class_scope:collector_service.CollectorMetric.ParamDefine)
    })
  ,

  'Plugin' : _reflection.GeneratedProtocolMessageType('Plugin', (_message.Message,), {
    'DESCRIPTOR' : _COLLECTORMETRIC_PLUGIN,
    '__module__' : 'metric_pb2'
    # @@protoc_insertion_point(class_scope:collector_service.CollectorMetric.Plugin)
    })
  ,
  'DESCRIPTOR' : _COLLECTORMETRIC,
  '__module__' : 'metric_pb2'
  # @@protoc_insertion_point(class_scope:collector_service.CollectorMetric)
  })
_sym_db.RegisterMessage(CollectorMetric)
_sym_db.RegisterMessage(CollectorMetric.TagDefine)
_sym_db.RegisterMessage(CollectorMetric.ParamDefine)
_sym_db.RegisterMessage(CollectorMetric.Plugin)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
