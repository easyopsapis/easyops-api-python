# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: collector_template.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='collector_template.proto',
  package='collector_service',
  syntax='proto3',
  serialized_options=_b('ZKgo.easyops.local/contracts/protorepo-models/easyops/model/collector_service'),
  serialized_pb=_b('\n\x18\x63ollector_template.proto\x12\x11\x63ollector_service\"\xdc\x05\n\x11\x43ollectorTemplate\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08interval\x18\x03 \x01(\x05\x12\x45\n\x0bmetricNames\x18\x04 \x03(\x0b\x32\x30.collector_service.CollectorTemplate.MetricNames\x12\x10\n\x08objectId\x18\x05 \x01(\t\x12;\n\x06params\x18\x06 \x03(\x0b\x32+.collector_service.CollectorTemplate.Params\x12\x0e\n\x06\x65xpand\x18\x07 \x01(\t\x12\x0c\n\x04type\x18\x08 \x01(\t\x12G\n\x0cprocessSteps\x18\t \x03(\x0b\x32\x31.collector_service.CollectorTemplate.ProcessSteps\x12\x11\n\tagentType\x18\n \x01(\t\x12\x12\n\nconfigYaml\x18\x0b \x01(\t\x12O\n\x10metricProperties\x18\x0c \x03(\x0b\x32\x35.collector_service.CollectorTemplate.MetricProperties\x12\r\n\x05logId\x18\r \x01(\t\x1aJ\n\x0bMetricNames\x12\x10\n\x08metricId\x18\x01 \x01(\t\x12\x12\n\nmetricName\x18\x02 \x01(\t\x12\x15\n\rcalculateOnly\x18\x03 \x01(\x08\x1a\x37\n\x06Params\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x11\n\tparamType\x18\x03 \x01(\t\x1aM\n\x0cProcessSteps\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x02 \x01(\t\x12\x0e\n\x06params\x18\x03 \x01(\t\x12\x0f\n\x07parents\x18\x04 \x03(\t\x1a;\n\x10MetricProperties\x12\x10\n\x08metricId\x18\x01 \x01(\t\x12\x15\n\rcalculateOnly\x18\x02 \x01(\x08\x42MZKgo.easyops.local/contracts/protorepo-models/easyops/model/collector_serviceb\x06proto3')
)




_COLLECTORTEMPLATE_METRICNAMES = _descriptor.Descriptor(
  name='MetricNames',
  full_name='collector_service.CollectorTemplate.MetricNames',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metricId', full_name='collector_service.CollectorTemplate.MetricNames.metricId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metricName', full_name='collector_service.CollectorTemplate.MetricNames.metricName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='calculateOnly', full_name='collector_service.CollectorTemplate.MetricNames.calculateOnly', index=2,
      number=3, type=8, cpp_type=7, label=1,
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
  serialized_start=509,
  serialized_end=583,
)

_COLLECTORTEMPLATE_PARAMS = _descriptor.Descriptor(
  name='Params',
  full_name='collector_service.CollectorTemplate.Params',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='collector_service.CollectorTemplate.Params.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='collector_service.CollectorTemplate.Params.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paramType', full_name='collector_service.CollectorTemplate.Params.paramType', index=2,
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
  serialized_start=585,
  serialized_end=640,
)

_COLLECTORTEMPLATE_PROCESSSTEPS = _descriptor.Descriptor(
  name='ProcessSteps',
  full_name='collector_service.CollectorTemplate.ProcessSteps',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='collector_service.CollectorTemplate.ProcessSteps.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='collector_service.CollectorTemplate.ProcessSteps.action', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='params', full_name='collector_service.CollectorTemplate.ProcessSteps.params', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parents', full_name='collector_service.CollectorTemplate.ProcessSteps.parents', index=3,
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
  serialized_start=642,
  serialized_end=719,
)

_COLLECTORTEMPLATE_METRICPROPERTIES = _descriptor.Descriptor(
  name='MetricProperties',
  full_name='collector_service.CollectorTemplate.MetricProperties',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metricId', full_name='collector_service.CollectorTemplate.MetricProperties.metricId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='calculateOnly', full_name='collector_service.CollectorTemplate.MetricProperties.calculateOnly', index=1,
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
  serialized_start=721,
  serialized_end=780,
)

_COLLECTORTEMPLATE = _descriptor.Descriptor(
  name='CollectorTemplate',
  full_name='collector_service.CollectorTemplate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='collector_service.CollectorTemplate.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='collector_service.CollectorTemplate.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interval', full_name='collector_service.CollectorTemplate.interval', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metricNames', full_name='collector_service.CollectorTemplate.metricNames', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectId', full_name='collector_service.CollectorTemplate.objectId', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='params', full_name='collector_service.CollectorTemplate.params', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expand', full_name='collector_service.CollectorTemplate.expand', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='collector_service.CollectorTemplate.type', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processSteps', full_name='collector_service.CollectorTemplate.processSteps', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agentType', full_name='collector_service.CollectorTemplate.agentType', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='configYaml', full_name='collector_service.CollectorTemplate.configYaml', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metricProperties', full_name='collector_service.CollectorTemplate.metricProperties', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logId', full_name='collector_service.CollectorTemplate.logId', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_COLLECTORTEMPLATE_METRICNAMES, _COLLECTORTEMPLATE_PARAMS, _COLLECTORTEMPLATE_PROCESSSTEPS, _COLLECTORTEMPLATE_METRICPROPERTIES, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=780,
)

_COLLECTORTEMPLATE_METRICNAMES.containing_type = _COLLECTORTEMPLATE
_COLLECTORTEMPLATE_PARAMS.containing_type = _COLLECTORTEMPLATE
_COLLECTORTEMPLATE_PROCESSSTEPS.containing_type = _COLLECTORTEMPLATE
_COLLECTORTEMPLATE_METRICPROPERTIES.containing_type = _COLLECTORTEMPLATE
_COLLECTORTEMPLATE.fields_by_name['metricNames'].message_type = _COLLECTORTEMPLATE_METRICNAMES
_COLLECTORTEMPLATE.fields_by_name['params'].message_type = _COLLECTORTEMPLATE_PARAMS
_COLLECTORTEMPLATE.fields_by_name['processSteps'].message_type = _COLLECTORTEMPLATE_PROCESSSTEPS
_COLLECTORTEMPLATE.fields_by_name['metricProperties'].message_type = _COLLECTORTEMPLATE_METRICPROPERTIES
DESCRIPTOR.message_types_by_name['CollectorTemplate'] = _COLLECTORTEMPLATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CollectorTemplate = _reflection.GeneratedProtocolMessageType('CollectorTemplate', (_message.Message,), {

  'MetricNames' : _reflection.GeneratedProtocolMessageType('MetricNames', (_message.Message,), {
    'DESCRIPTOR' : _COLLECTORTEMPLATE_METRICNAMES,
    '__module__' : 'collector_template_pb2'
    # @@protoc_insertion_point(class_scope:collector_service.CollectorTemplate.MetricNames)
    })
  ,

  'Params' : _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {
    'DESCRIPTOR' : _COLLECTORTEMPLATE_PARAMS,
    '__module__' : 'collector_template_pb2'
    # @@protoc_insertion_point(class_scope:collector_service.CollectorTemplate.Params)
    })
  ,

  'ProcessSteps' : _reflection.GeneratedProtocolMessageType('ProcessSteps', (_message.Message,), {
    'DESCRIPTOR' : _COLLECTORTEMPLATE_PROCESSSTEPS,
    '__module__' : 'collector_template_pb2'
    # @@protoc_insertion_point(class_scope:collector_service.CollectorTemplate.ProcessSteps)
    })
  ,

  'MetricProperties' : _reflection.GeneratedProtocolMessageType('MetricProperties', (_message.Message,), {
    'DESCRIPTOR' : _COLLECTORTEMPLATE_METRICPROPERTIES,
    '__module__' : 'collector_template_pb2'
    # @@protoc_insertion_point(class_scope:collector_service.CollectorTemplate.MetricProperties)
    })
  ,
  'DESCRIPTOR' : _COLLECTORTEMPLATE,
  '__module__' : 'collector_template_pb2'
  # @@protoc_insertion_point(class_scope:collector_service.CollectorTemplate)
  })
_sym_db.RegisterMessage(CollectorTemplate)
_sym_db.RegisterMessage(CollectorTemplate.MetricNames)
_sym_db.RegisterMessage(CollectorTemplate.Params)
_sym_db.RegisterMessage(CollectorTemplate.ProcessSteps)
_sym_db.RegisterMessage(CollectorTemplate.MetricProperties)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
