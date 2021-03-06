# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: detail_template.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='detail_template.proto',
  package='template',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x15\x64\x65tail_template.proto\x12\x08template\"4\n\x1e\x44\x65tailCollectorTemplateRequest\x12\x12\n\ninstanceId\x18\x01 \x01(\t\"\x85\t\n\x1f\x44\x65tailCollectorTemplateResponse\x12T\n\x10\x63ollectorMetrics\x18\x01 \x03(\x0b\x32:.template.DetailCollectorTemplateResponse.CollectorMetrics\x12\x12\n\ninstanceId\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x10\n\x08interval\x18\x04 \x01(\x05\x12J\n\x0bmetricNames\x18\x05 \x03(\x0b\x32\x35.template.DetailCollectorTemplateResponse.MetricNames\x12\x10\n\x08objectId\x18\x06 \x01(\t\x12@\n\x06params\x18\x07 \x03(\x0b\x32\x30.template.DetailCollectorTemplateResponse.Params\x12\x0e\n\x06\x65xpand\x18\x08 \x01(\t\x12\x0c\n\x04type\x18\t \x01(\t\x12L\n\x0cprocessSteps\x18\n \x03(\x0b\x32\x36.template.DetailCollectorTemplateResponse.ProcessSteps\x12\x11\n\tagentType\x18\x0b \x01(\t\x12\x12\n\nconfigYaml\x18\x0c \x01(\t\x12T\n\x10metricProperties\x18\r \x03(\x0b\x32:.template.DetailCollectorTemplateResponse.MetricProperties\x12\r\n\x05logId\x18\x0e \x01(\t\x1a\xae\x02\n\x10\x43ollectorMetrics\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04unit\x18\x02 \x01(\t\x12\x10\n\x08\x64\x61taType\x18\x03 \x01(\t\x12\x12\n\nmetricType\x18\x04 \x01(\t\x12\x0c\n\x04help\x18\x05 \x01(\t\x12\x0b\n\x03key\x18\x06 \x01(\t\x12W\n\ttagDefine\x18\x07 \x03(\x0b\x32\x44.template.DetailCollectorTemplateResponse.CollectorMetrics.TagDefine\x1a\x64\n\tTagDefine\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x02 \x01(\t\x12\x10\n\x08readOnly\x18\x03 \x01(\x08\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x11\n\tvalueType\x18\x05 \x01(\t\x1aJ\n\x0bMetricNames\x12\x10\n\x08metricId\x18\x01 \x01(\t\x12\x12\n\nmetricName\x18\x02 \x01(\t\x12\x15\n\rcalculateOnly\x18\x03 \x01(\x08\x1a\x37\n\x06Params\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x11\n\tparamType\x18\x03 \x01(\t\x1aM\n\x0cProcessSteps\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x02 \x01(\t\x12\x0e\n\x06params\x18\x03 \x01(\t\x12\x0f\n\x07parents\x18\x04 \x03(\t\x1a;\n\x10MetricProperties\x12\x10\n\x08metricId\x18\x01 \x01(\t\x12\x15\n\rcalculateOnly\x18\x02 \x01(\x08\"\x93\x01\n&DetailCollectorTemplateResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x37\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32).template.DetailCollectorTemplateResponseb\x06proto3')
)




_DETAILCOLLECTORTEMPLATEREQUEST = _descriptor.Descriptor(
  name='DetailCollectorTemplateRequest',
  full_name='template.DetailCollectorTemplateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='template.DetailCollectorTemplateRequest.instanceId', index=0,
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
  serialized_start=35,
  serialized_end=87,
)


_DETAILCOLLECTORTEMPLATERESPONSE_COLLECTORMETRICS_TAGDEFINE = _descriptor.Descriptor(
  name='TagDefine',
  full_name='template.DetailCollectorTemplateResponse.CollectorMetrics.TagDefine',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='template.DetailCollectorTemplateResponse.CollectorMetrics.TagDefine.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default', full_name='template.DetailCollectorTemplateResponse.CollectorMetrics.TagDefine.default', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readOnly', full_name='template.DetailCollectorTemplateResponse.CollectorMetrics.TagDefine.readOnly', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='template.DetailCollectorTemplateResponse.CollectorMetrics.TagDefine.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='valueType', full_name='template.DetailCollectorTemplateResponse.CollectorMetrics.TagDefine.valueType', index=4,
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
  serialized_start=874,
  serialized_end=974,
)

_DETAILCOLLECTORTEMPLATERESPONSE_COLLECTORMETRICS = _descriptor.Descriptor(
  name='CollectorMetrics',
  full_name='template.DetailCollectorTemplateResponse.CollectorMetrics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='template.DetailCollectorTemplateResponse.CollectorMetrics.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unit', full_name='template.DetailCollectorTemplateResponse.CollectorMetrics.unit', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataType', full_name='template.DetailCollectorTemplateResponse.CollectorMetrics.dataType', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metricType', full_name='template.DetailCollectorTemplateResponse.CollectorMetrics.metricType', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='help', full_name='template.DetailCollectorTemplateResponse.CollectorMetrics.help', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='template.DetailCollectorTemplateResponse.CollectorMetrics.key', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tagDefine', full_name='template.DetailCollectorTemplateResponse.CollectorMetrics.tagDefine', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DETAILCOLLECTORTEMPLATERESPONSE_COLLECTORMETRICS_TAGDEFINE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=672,
  serialized_end=974,
)

_DETAILCOLLECTORTEMPLATERESPONSE_METRICNAMES = _descriptor.Descriptor(
  name='MetricNames',
  full_name='template.DetailCollectorTemplateResponse.MetricNames',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metricId', full_name='template.DetailCollectorTemplateResponse.MetricNames.metricId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metricName', full_name='template.DetailCollectorTemplateResponse.MetricNames.metricName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='calculateOnly', full_name='template.DetailCollectorTemplateResponse.MetricNames.calculateOnly', index=2,
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
  serialized_start=976,
  serialized_end=1050,
)

_DETAILCOLLECTORTEMPLATERESPONSE_PARAMS = _descriptor.Descriptor(
  name='Params',
  full_name='template.DetailCollectorTemplateResponse.Params',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='template.DetailCollectorTemplateResponse.Params.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='template.DetailCollectorTemplateResponse.Params.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paramType', full_name='template.DetailCollectorTemplateResponse.Params.paramType', index=2,
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
  serialized_start=1052,
  serialized_end=1107,
)

_DETAILCOLLECTORTEMPLATERESPONSE_PROCESSSTEPS = _descriptor.Descriptor(
  name='ProcessSteps',
  full_name='template.DetailCollectorTemplateResponse.ProcessSteps',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='template.DetailCollectorTemplateResponse.ProcessSteps.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='template.DetailCollectorTemplateResponse.ProcessSteps.action', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='params', full_name='template.DetailCollectorTemplateResponse.ProcessSteps.params', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parents', full_name='template.DetailCollectorTemplateResponse.ProcessSteps.parents', index=3,
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
  serialized_start=1109,
  serialized_end=1186,
)

_DETAILCOLLECTORTEMPLATERESPONSE_METRICPROPERTIES = _descriptor.Descriptor(
  name='MetricProperties',
  full_name='template.DetailCollectorTemplateResponse.MetricProperties',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metricId', full_name='template.DetailCollectorTemplateResponse.MetricProperties.metricId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='calculateOnly', full_name='template.DetailCollectorTemplateResponse.MetricProperties.calculateOnly', index=1,
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
  serialized_start=1188,
  serialized_end=1247,
)

_DETAILCOLLECTORTEMPLATERESPONSE = _descriptor.Descriptor(
  name='DetailCollectorTemplateResponse',
  full_name='template.DetailCollectorTemplateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='collectorMetrics', full_name='template.DetailCollectorTemplateResponse.collectorMetrics', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='template.DetailCollectorTemplateResponse.instanceId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='template.DetailCollectorTemplateResponse.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interval', full_name='template.DetailCollectorTemplateResponse.interval', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metricNames', full_name='template.DetailCollectorTemplateResponse.metricNames', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectId', full_name='template.DetailCollectorTemplateResponse.objectId', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='params', full_name='template.DetailCollectorTemplateResponse.params', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expand', full_name='template.DetailCollectorTemplateResponse.expand', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='template.DetailCollectorTemplateResponse.type', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processSteps', full_name='template.DetailCollectorTemplateResponse.processSteps', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agentType', full_name='template.DetailCollectorTemplateResponse.agentType', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='configYaml', full_name='template.DetailCollectorTemplateResponse.configYaml', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metricProperties', full_name='template.DetailCollectorTemplateResponse.metricProperties', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logId', full_name='template.DetailCollectorTemplateResponse.logId', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DETAILCOLLECTORTEMPLATERESPONSE_COLLECTORMETRICS, _DETAILCOLLECTORTEMPLATERESPONSE_METRICNAMES, _DETAILCOLLECTORTEMPLATERESPONSE_PARAMS, _DETAILCOLLECTORTEMPLATERESPONSE_PROCESSSTEPS, _DETAILCOLLECTORTEMPLATERESPONSE_METRICPROPERTIES, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=1247,
)


_DETAILCOLLECTORTEMPLATERESPONSEWRAPPER = _descriptor.Descriptor(
  name='DetailCollectorTemplateResponseWrapper',
  full_name='template.DetailCollectorTemplateResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='template.DetailCollectorTemplateResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='template.DetailCollectorTemplateResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='template.DetailCollectorTemplateResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='template.DetailCollectorTemplateResponseWrapper.data', index=3,
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
  serialized_start=1250,
  serialized_end=1397,
)

_DETAILCOLLECTORTEMPLATERESPONSE_COLLECTORMETRICS_TAGDEFINE.containing_type = _DETAILCOLLECTORTEMPLATERESPONSE_COLLECTORMETRICS
_DETAILCOLLECTORTEMPLATERESPONSE_COLLECTORMETRICS.fields_by_name['tagDefine'].message_type = _DETAILCOLLECTORTEMPLATERESPONSE_COLLECTORMETRICS_TAGDEFINE
_DETAILCOLLECTORTEMPLATERESPONSE_COLLECTORMETRICS.containing_type = _DETAILCOLLECTORTEMPLATERESPONSE
_DETAILCOLLECTORTEMPLATERESPONSE_METRICNAMES.containing_type = _DETAILCOLLECTORTEMPLATERESPONSE
_DETAILCOLLECTORTEMPLATERESPONSE_PARAMS.containing_type = _DETAILCOLLECTORTEMPLATERESPONSE
_DETAILCOLLECTORTEMPLATERESPONSE_PROCESSSTEPS.containing_type = _DETAILCOLLECTORTEMPLATERESPONSE
_DETAILCOLLECTORTEMPLATERESPONSE_METRICPROPERTIES.containing_type = _DETAILCOLLECTORTEMPLATERESPONSE
_DETAILCOLLECTORTEMPLATERESPONSE.fields_by_name['collectorMetrics'].message_type = _DETAILCOLLECTORTEMPLATERESPONSE_COLLECTORMETRICS
_DETAILCOLLECTORTEMPLATERESPONSE.fields_by_name['metricNames'].message_type = _DETAILCOLLECTORTEMPLATERESPONSE_METRICNAMES
_DETAILCOLLECTORTEMPLATERESPONSE.fields_by_name['params'].message_type = _DETAILCOLLECTORTEMPLATERESPONSE_PARAMS
_DETAILCOLLECTORTEMPLATERESPONSE.fields_by_name['processSteps'].message_type = _DETAILCOLLECTORTEMPLATERESPONSE_PROCESSSTEPS
_DETAILCOLLECTORTEMPLATERESPONSE.fields_by_name['metricProperties'].message_type = _DETAILCOLLECTORTEMPLATERESPONSE_METRICPROPERTIES
_DETAILCOLLECTORTEMPLATERESPONSEWRAPPER.fields_by_name['data'].message_type = _DETAILCOLLECTORTEMPLATERESPONSE
DESCRIPTOR.message_types_by_name['DetailCollectorTemplateRequest'] = _DETAILCOLLECTORTEMPLATEREQUEST
DESCRIPTOR.message_types_by_name['DetailCollectorTemplateResponse'] = _DETAILCOLLECTORTEMPLATERESPONSE
DESCRIPTOR.message_types_by_name['DetailCollectorTemplateResponseWrapper'] = _DETAILCOLLECTORTEMPLATERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DetailCollectorTemplateRequest = _reflection.GeneratedProtocolMessageType('DetailCollectorTemplateRequest', (_message.Message,), {
  'DESCRIPTOR' : _DETAILCOLLECTORTEMPLATEREQUEST,
  '__module__' : 'detail_template_pb2'
  # @@protoc_insertion_point(class_scope:template.DetailCollectorTemplateRequest)
  })
_sym_db.RegisterMessage(DetailCollectorTemplateRequest)

DetailCollectorTemplateResponse = _reflection.GeneratedProtocolMessageType('DetailCollectorTemplateResponse', (_message.Message,), {

  'CollectorMetrics' : _reflection.GeneratedProtocolMessageType('CollectorMetrics', (_message.Message,), {

    'TagDefine' : _reflection.GeneratedProtocolMessageType('TagDefine', (_message.Message,), {
      'DESCRIPTOR' : _DETAILCOLLECTORTEMPLATERESPONSE_COLLECTORMETRICS_TAGDEFINE,
      '__module__' : 'detail_template_pb2'
      # @@protoc_insertion_point(class_scope:template.DetailCollectorTemplateResponse.CollectorMetrics.TagDefine)
      })
    ,
    'DESCRIPTOR' : _DETAILCOLLECTORTEMPLATERESPONSE_COLLECTORMETRICS,
    '__module__' : 'detail_template_pb2'
    # @@protoc_insertion_point(class_scope:template.DetailCollectorTemplateResponse.CollectorMetrics)
    })
  ,

  'MetricNames' : _reflection.GeneratedProtocolMessageType('MetricNames', (_message.Message,), {
    'DESCRIPTOR' : _DETAILCOLLECTORTEMPLATERESPONSE_METRICNAMES,
    '__module__' : 'detail_template_pb2'
    # @@protoc_insertion_point(class_scope:template.DetailCollectorTemplateResponse.MetricNames)
    })
  ,

  'Params' : _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {
    'DESCRIPTOR' : _DETAILCOLLECTORTEMPLATERESPONSE_PARAMS,
    '__module__' : 'detail_template_pb2'
    # @@protoc_insertion_point(class_scope:template.DetailCollectorTemplateResponse.Params)
    })
  ,

  'ProcessSteps' : _reflection.GeneratedProtocolMessageType('ProcessSteps', (_message.Message,), {
    'DESCRIPTOR' : _DETAILCOLLECTORTEMPLATERESPONSE_PROCESSSTEPS,
    '__module__' : 'detail_template_pb2'
    # @@protoc_insertion_point(class_scope:template.DetailCollectorTemplateResponse.ProcessSteps)
    })
  ,

  'MetricProperties' : _reflection.GeneratedProtocolMessageType('MetricProperties', (_message.Message,), {
    'DESCRIPTOR' : _DETAILCOLLECTORTEMPLATERESPONSE_METRICPROPERTIES,
    '__module__' : 'detail_template_pb2'
    # @@protoc_insertion_point(class_scope:template.DetailCollectorTemplateResponse.MetricProperties)
    })
  ,
  'DESCRIPTOR' : _DETAILCOLLECTORTEMPLATERESPONSE,
  '__module__' : 'detail_template_pb2'
  # @@protoc_insertion_point(class_scope:template.DetailCollectorTemplateResponse)
  })
_sym_db.RegisterMessage(DetailCollectorTemplateResponse)
_sym_db.RegisterMessage(DetailCollectorTemplateResponse.CollectorMetrics)
_sym_db.RegisterMessage(DetailCollectorTemplateResponse.CollectorMetrics.TagDefine)
_sym_db.RegisterMessage(DetailCollectorTemplateResponse.MetricNames)
_sym_db.RegisterMessage(DetailCollectorTemplateResponse.Params)
_sym_db.RegisterMessage(DetailCollectorTemplateResponse.ProcessSteps)
_sym_db.RegisterMessage(DetailCollectorTemplateResponse.MetricProperties)

DetailCollectorTemplateResponseWrapper = _reflection.GeneratedProtocolMessageType('DetailCollectorTemplateResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _DETAILCOLLECTORTEMPLATERESPONSEWRAPPER,
  '__module__' : 'detail_template_pb2'
  # @@protoc_insertion_point(class_scope:template.DetailCollectorTemplateResponseWrapper)
  })
_sym_db.RegisterMessage(DetailCollectorTemplateResponseWrapper)


# @@protoc_insertion_point(module_scope)
