# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='config.proto',
  package='collector_service',
  syntax='proto3',
  serialized_options=_b('ZKgo.easyops.local/contracts/protorepo-models/easyops/model/collector_service'),
  serialized_pb=_b('\n\x0c\x63onfig.proto\x12\x11\x63ollector_service\"\x82\x06\n\x0f\x43ollectorConfig\x12\x10\n\x08\x63onfigId\x18\x01 \x01(\t\x12\x12\n\njobVersion\x18\x02 \x01(\x05\x12\x17\n\x0ftemplateVersion\x18\x03 \x01(\x05\x12\x10\n\x08objectId\x18\x04 \x01(\t\x12\x43\n\x0b\x63ollectTime\x18\x05 \x01(\x0b\x32..collector_service.CollectorConfig.CollectTime\x12\x0f\n\x07timeout\x18\x06 \x01(\x05\x12\x10\n\x08interval\x18\x07 \x01(\x05\x12\x0f\n\x07\x65nabled\x18\x08 \x01(\x08\x12\x0e\n\x06\x66ilter\x18\t \x01(\t\x12\x0c\n\x04path\x18\n \x01(\t\x12\x39\n\x06params\x18\x0b \x03(\x0b\x32).collector_service.CollectorConfig.Params\x12\x0e\n\x06\x65xpand\x18\x0c \x01(\t\x12\x0c\n\x04type\x18\r \x01(\t\x12\x45\n\x0cprocessSteps\x18\x0e \x03(\x0b\x32/.collector_service.CollectorConfig.ProcessSteps\x12M\n\x10metricProperties\x18\x0f \x03(\x0b\x32\x33.collector_service.CollectorConfig.MetricProperties\x12\r\n\x05logId\x18\x10 \x01(\t\x12\x11\n\tagentType\x18\x11 \x01(\t\x1a\x31\n\x0b\x43ollectTime\x12\x11\n\tstartTime\x18\x01 \x01(\t\x12\x0f\n\x07\x65ndTime\x18\x02 \x01(\t\x1a\x37\n\x06Params\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x11\n\tparamType\x18\x03 \x01(\t\x1aM\n\x0cProcessSteps\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x02 \x01(\t\x12\x0e\n\x06params\x18\x03 \x01(\t\x12\x0f\n\x07parents\x18\x04 \x03(\t\x1a;\n\x10MetricProperties\x12\x10\n\x08metricId\x18\x01 \x01(\t\x12\x15\n\rcalculateOnly\x18\x02 \x01(\x08\x42MZKgo.easyops.local/contracts/protorepo-models/easyops/model/collector_serviceb\x06proto3')
)




_COLLECTORCONFIG_COLLECTTIME = _descriptor.Descriptor(
  name='CollectTime',
  full_name='collector_service.CollectorConfig.CollectTime',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='startTime', full_name='collector_service.CollectorConfig.CollectTime.startTime', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endTime', full_name='collector_service.CollectorConfig.CollectTime.endTime', index=1,
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
  serialized_start=560,
  serialized_end=609,
)

_COLLECTORCONFIG_PARAMS = _descriptor.Descriptor(
  name='Params',
  full_name='collector_service.CollectorConfig.Params',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='collector_service.CollectorConfig.Params.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='collector_service.CollectorConfig.Params.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paramType', full_name='collector_service.CollectorConfig.Params.paramType', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=611,
  serialized_end=666,
)

_COLLECTORCONFIG_PROCESSSTEPS = _descriptor.Descriptor(
  name='ProcessSteps',
  full_name='collector_service.CollectorConfig.ProcessSteps',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='collector_service.CollectorConfig.ProcessSteps.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='collector_service.CollectorConfig.ProcessSteps.action', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='params', full_name='collector_service.CollectorConfig.ProcessSteps.params', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parents', full_name='collector_service.CollectorConfig.ProcessSteps.parents', index=3,
      number=4, type=9, cpp_type=9, label=3,
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
  serialized_start=668,
  serialized_end=745,
)

_COLLECTORCONFIG_METRICPROPERTIES = _descriptor.Descriptor(
  name='MetricProperties',
  full_name='collector_service.CollectorConfig.MetricProperties',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metricId', full_name='collector_service.CollectorConfig.MetricProperties.metricId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='calculateOnly', full_name='collector_service.CollectorConfig.MetricProperties.calculateOnly', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  serialized_start=747,
  serialized_end=806,
)

_COLLECTORCONFIG = _descriptor.Descriptor(
  name='CollectorConfig',
  full_name='collector_service.CollectorConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='configId', full_name='collector_service.CollectorConfig.configId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='jobVersion', full_name='collector_service.CollectorConfig.jobVersion', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='templateVersion', full_name='collector_service.CollectorConfig.templateVersion', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectId', full_name='collector_service.CollectorConfig.objectId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collectTime', full_name='collector_service.CollectorConfig.collectTime', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='collector_service.CollectorConfig.timeout', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interval', full_name='collector_service.CollectorConfig.interval', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enabled', full_name='collector_service.CollectorConfig.enabled', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter', full_name='collector_service.CollectorConfig.filter', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='collector_service.CollectorConfig.path', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='params', full_name='collector_service.CollectorConfig.params', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expand', full_name='collector_service.CollectorConfig.expand', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='collector_service.CollectorConfig.type', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processSteps', full_name='collector_service.CollectorConfig.processSteps', index=13,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metricProperties', full_name='collector_service.CollectorConfig.metricProperties', index=14,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logId', full_name='collector_service.CollectorConfig.logId', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agentType', full_name='collector_service.CollectorConfig.agentType', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_COLLECTORCONFIG_COLLECTTIME, _COLLECTORCONFIG_PARAMS, _COLLECTORCONFIG_PROCESSSTEPS, _COLLECTORCONFIG_METRICPROPERTIES, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=806,
)

_COLLECTORCONFIG_COLLECTTIME.containing_type = _COLLECTORCONFIG
_COLLECTORCONFIG_PARAMS.containing_type = _COLLECTORCONFIG
_COLLECTORCONFIG_PROCESSSTEPS.containing_type = _COLLECTORCONFIG
_COLLECTORCONFIG_METRICPROPERTIES.containing_type = _COLLECTORCONFIG
_COLLECTORCONFIG.fields_by_name['collectTime'].message_type = _COLLECTORCONFIG_COLLECTTIME
_COLLECTORCONFIG.fields_by_name['params'].message_type = _COLLECTORCONFIG_PARAMS
_COLLECTORCONFIG.fields_by_name['processSteps'].message_type = _COLLECTORCONFIG_PROCESSSTEPS
_COLLECTORCONFIG.fields_by_name['metricProperties'].message_type = _COLLECTORCONFIG_METRICPROPERTIES
DESCRIPTOR.message_types_by_name['CollectorConfig'] = _COLLECTORCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CollectorConfig = _reflection.GeneratedProtocolMessageType('CollectorConfig', (_message.Message,), {

  'CollectTime' : _reflection.GeneratedProtocolMessageType('CollectTime', (_message.Message,), {
    'DESCRIPTOR' : _COLLECTORCONFIG_COLLECTTIME,
    '__module__' : 'config_pb2'
    # @@protoc_insertion_point(class_scope:collector_service.CollectorConfig.CollectTime)
    })
  ,

  'Params' : _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {
    'DESCRIPTOR' : _COLLECTORCONFIG_PARAMS,
    '__module__' : 'config_pb2'
    # @@protoc_insertion_point(class_scope:collector_service.CollectorConfig.Params)
    })
  ,

  'ProcessSteps' : _reflection.GeneratedProtocolMessageType('ProcessSteps', (_message.Message,), {
    'DESCRIPTOR' : _COLLECTORCONFIG_PROCESSSTEPS,
    '__module__' : 'config_pb2'
    # @@protoc_insertion_point(class_scope:collector_service.CollectorConfig.ProcessSteps)
    })
  ,

  'MetricProperties' : _reflection.GeneratedProtocolMessageType('MetricProperties', (_message.Message,), {
    'DESCRIPTOR' : _COLLECTORCONFIG_METRICPROPERTIES,
    '__module__' : 'config_pb2'
    # @@protoc_insertion_point(class_scope:collector_service.CollectorConfig.MetricProperties)
    })
  ,
  'DESCRIPTOR' : _COLLECTORCONFIG,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:collector_service.CollectorConfig)
  })
_sym_db.RegisterMessage(CollectorConfig)
_sym_db.RegisterMessage(CollectorConfig.CollectTime)
_sym_db.RegisterMessage(CollectorConfig.Params)
_sym_db.RegisterMessage(CollectorConfig.ProcessSteps)
_sym_db.RegisterMessage(CollectorConfig.MetricProperties)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
