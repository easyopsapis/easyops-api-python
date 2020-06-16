# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: valid_template_yaml.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='valid_template_yaml.proto',
  package='template',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x19valid_template_yaml.proto\x12\x08template\"N\n\x18ValidTemplateYamlRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08objectId\x18\x02 \x01(\t\x12\x12\n\nconfigYaml\x18\x03 \x01(\t\"\xf4\x05\n\x19ValidTemplateYamlResponse\x12N\n\x10\x63ollectorMetrics\x18\x01 \x03(\x0b\x32\x34.template.ValidTemplateYamlResponse.CollectorMetrics\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08objectId\x18\x03 \x01(\t\x12\x44\n\x0bmetricNames\x18\x04 \x03(\x0b\x32/.template.ValidTemplateYamlResponse.MetricNames\x12:\n\x06params\x18\x05 \x03(\x0b\x32*.template.ValidTemplateYamlResponse.Params\x12\x0e\n\x06\x65xpand\x18\x06 \x01(\t\x12\x11\n\tagentType\x18\x07 \x01(\t\x12\x12\n\nconfigYaml\x18\x08 \x01(\t\x1a\xa8\x02\n\x10\x43ollectorMetrics\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04unit\x18\x02 \x01(\t\x12\x10\n\x08\x64\x61taType\x18\x03 \x01(\t\x12\x12\n\nmetricType\x18\x04 \x01(\t\x12\x0c\n\x04help\x18\x05 \x01(\t\x12\x0b\n\x03key\x18\x06 \x01(\t\x12Q\n\ttagDefine\x18\x07 \x03(\x0b\x32>.template.ValidTemplateYamlResponse.CollectorMetrics.TagDefine\x1a\x64\n\tTagDefine\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x02 \x01(\t\x12\x10\n\x08readOnly\x18\x03 \x01(\x08\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x11\n\tvalueType\x18\x05 \x01(\t\x1aJ\n\x0bMetricNames\x12\x10\n\x08metricId\x18\x01 \x01(\t\x12\x12\n\nmetricName\x18\x02 \x01(\t\x12\x15\n\rcalculateOnly\x18\x03 \x01(\x08\x1a\x37\n\x06Params\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x11\n\tparamType\x18\x03 \x01(\t\"\x87\x01\n ValidTemplateYamlResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x31\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32#.template.ValidTemplateYamlResponseb\x06proto3')
)




_VALIDTEMPLATEYAMLREQUEST = _descriptor.Descriptor(
  name='ValidTemplateYamlRequest',
  full_name='template.ValidTemplateYamlRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='template.ValidTemplateYamlRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectId', full_name='template.ValidTemplateYamlRequest.objectId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='configYaml', full_name='template.ValidTemplateYamlRequest.configYaml', index=2,
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
  serialized_start=39,
  serialized_end=117,
)


_VALIDTEMPLATEYAMLRESPONSE_COLLECTORMETRICS_TAGDEFINE = _descriptor.Descriptor(
  name='TagDefine',
  full_name='template.ValidTemplateYamlResponse.CollectorMetrics.TagDefine',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='template.ValidTemplateYamlResponse.CollectorMetrics.TagDefine.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default', full_name='template.ValidTemplateYamlResponse.CollectorMetrics.TagDefine.default', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readOnly', full_name='template.ValidTemplateYamlResponse.CollectorMetrics.TagDefine.readOnly', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='template.ValidTemplateYamlResponse.CollectorMetrics.TagDefine.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='valueType', full_name='template.ValidTemplateYamlResponse.CollectorMetrics.TagDefine.valueType', index=4,
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
  serialized_start=643,
  serialized_end=743,
)

_VALIDTEMPLATEYAMLRESPONSE_COLLECTORMETRICS = _descriptor.Descriptor(
  name='CollectorMetrics',
  full_name='template.ValidTemplateYamlResponse.CollectorMetrics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='template.ValidTemplateYamlResponse.CollectorMetrics.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unit', full_name='template.ValidTemplateYamlResponse.CollectorMetrics.unit', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataType', full_name='template.ValidTemplateYamlResponse.CollectorMetrics.dataType', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metricType', full_name='template.ValidTemplateYamlResponse.CollectorMetrics.metricType', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='help', full_name='template.ValidTemplateYamlResponse.CollectorMetrics.help', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='template.ValidTemplateYamlResponse.CollectorMetrics.key', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tagDefine', full_name='template.ValidTemplateYamlResponse.CollectorMetrics.tagDefine', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_VALIDTEMPLATEYAMLRESPONSE_COLLECTORMETRICS_TAGDEFINE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=447,
  serialized_end=743,
)

_VALIDTEMPLATEYAMLRESPONSE_METRICNAMES = _descriptor.Descriptor(
  name='MetricNames',
  full_name='template.ValidTemplateYamlResponse.MetricNames',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metricId', full_name='template.ValidTemplateYamlResponse.MetricNames.metricId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metricName', full_name='template.ValidTemplateYamlResponse.MetricNames.metricName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='calculateOnly', full_name='template.ValidTemplateYamlResponse.MetricNames.calculateOnly', index=2,
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
  serialized_start=745,
  serialized_end=819,
)

_VALIDTEMPLATEYAMLRESPONSE_PARAMS = _descriptor.Descriptor(
  name='Params',
  full_name='template.ValidTemplateYamlResponse.Params',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='template.ValidTemplateYamlResponse.Params.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='template.ValidTemplateYamlResponse.Params.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paramType', full_name='template.ValidTemplateYamlResponse.Params.paramType', index=2,
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
  serialized_start=821,
  serialized_end=876,
)

_VALIDTEMPLATEYAMLRESPONSE = _descriptor.Descriptor(
  name='ValidTemplateYamlResponse',
  full_name='template.ValidTemplateYamlResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='collectorMetrics', full_name='template.ValidTemplateYamlResponse.collectorMetrics', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='template.ValidTemplateYamlResponse.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectId', full_name='template.ValidTemplateYamlResponse.objectId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metricNames', full_name='template.ValidTemplateYamlResponse.metricNames', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='params', full_name='template.ValidTemplateYamlResponse.params', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expand', full_name='template.ValidTemplateYamlResponse.expand', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agentType', full_name='template.ValidTemplateYamlResponse.agentType', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='configYaml', full_name='template.ValidTemplateYamlResponse.configYaml', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_VALIDTEMPLATEYAMLRESPONSE_COLLECTORMETRICS, _VALIDTEMPLATEYAMLRESPONSE_METRICNAMES, _VALIDTEMPLATEYAMLRESPONSE_PARAMS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=120,
  serialized_end=876,
)


_VALIDTEMPLATEYAMLRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ValidTemplateYamlResponseWrapper',
  full_name='template.ValidTemplateYamlResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='template.ValidTemplateYamlResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='template.ValidTemplateYamlResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='template.ValidTemplateYamlResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='template.ValidTemplateYamlResponseWrapper.data', index=3,
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
  serialized_start=879,
  serialized_end=1014,
)

_VALIDTEMPLATEYAMLRESPONSE_COLLECTORMETRICS_TAGDEFINE.containing_type = _VALIDTEMPLATEYAMLRESPONSE_COLLECTORMETRICS
_VALIDTEMPLATEYAMLRESPONSE_COLLECTORMETRICS.fields_by_name['tagDefine'].message_type = _VALIDTEMPLATEYAMLRESPONSE_COLLECTORMETRICS_TAGDEFINE
_VALIDTEMPLATEYAMLRESPONSE_COLLECTORMETRICS.containing_type = _VALIDTEMPLATEYAMLRESPONSE
_VALIDTEMPLATEYAMLRESPONSE_METRICNAMES.containing_type = _VALIDTEMPLATEYAMLRESPONSE
_VALIDTEMPLATEYAMLRESPONSE_PARAMS.containing_type = _VALIDTEMPLATEYAMLRESPONSE
_VALIDTEMPLATEYAMLRESPONSE.fields_by_name['collectorMetrics'].message_type = _VALIDTEMPLATEYAMLRESPONSE_COLLECTORMETRICS
_VALIDTEMPLATEYAMLRESPONSE.fields_by_name['metricNames'].message_type = _VALIDTEMPLATEYAMLRESPONSE_METRICNAMES
_VALIDTEMPLATEYAMLRESPONSE.fields_by_name['params'].message_type = _VALIDTEMPLATEYAMLRESPONSE_PARAMS
_VALIDTEMPLATEYAMLRESPONSEWRAPPER.fields_by_name['data'].message_type = _VALIDTEMPLATEYAMLRESPONSE
DESCRIPTOR.message_types_by_name['ValidTemplateYamlRequest'] = _VALIDTEMPLATEYAMLREQUEST
DESCRIPTOR.message_types_by_name['ValidTemplateYamlResponse'] = _VALIDTEMPLATEYAMLRESPONSE
DESCRIPTOR.message_types_by_name['ValidTemplateYamlResponseWrapper'] = _VALIDTEMPLATEYAMLRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ValidTemplateYamlRequest = _reflection.GeneratedProtocolMessageType('ValidTemplateYamlRequest', (_message.Message,), {
  'DESCRIPTOR' : _VALIDTEMPLATEYAMLREQUEST,
  '__module__' : 'valid_template_yaml_pb2'
  # @@protoc_insertion_point(class_scope:template.ValidTemplateYamlRequest)
  })
_sym_db.RegisterMessage(ValidTemplateYamlRequest)

ValidTemplateYamlResponse = _reflection.GeneratedProtocolMessageType('ValidTemplateYamlResponse', (_message.Message,), {

  'CollectorMetrics' : _reflection.GeneratedProtocolMessageType('CollectorMetrics', (_message.Message,), {

    'TagDefine' : _reflection.GeneratedProtocolMessageType('TagDefine', (_message.Message,), {
      'DESCRIPTOR' : _VALIDTEMPLATEYAMLRESPONSE_COLLECTORMETRICS_TAGDEFINE,
      '__module__' : 'valid_template_yaml_pb2'
      # @@protoc_insertion_point(class_scope:template.ValidTemplateYamlResponse.CollectorMetrics.TagDefine)
      })
    ,
    'DESCRIPTOR' : _VALIDTEMPLATEYAMLRESPONSE_COLLECTORMETRICS,
    '__module__' : 'valid_template_yaml_pb2'
    # @@protoc_insertion_point(class_scope:template.ValidTemplateYamlResponse.CollectorMetrics)
    })
  ,

  'MetricNames' : _reflection.GeneratedProtocolMessageType('MetricNames', (_message.Message,), {
    'DESCRIPTOR' : _VALIDTEMPLATEYAMLRESPONSE_METRICNAMES,
    '__module__' : 'valid_template_yaml_pb2'
    # @@protoc_insertion_point(class_scope:template.ValidTemplateYamlResponse.MetricNames)
    })
  ,

  'Params' : _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {
    'DESCRIPTOR' : _VALIDTEMPLATEYAMLRESPONSE_PARAMS,
    '__module__' : 'valid_template_yaml_pb2'
    # @@protoc_insertion_point(class_scope:template.ValidTemplateYamlResponse.Params)
    })
  ,
  'DESCRIPTOR' : _VALIDTEMPLATEYAMLRESPONSE,
  '__module__' : 'valid_template_yaml_pb2'
  # @@protoc_insertion_point(class_scope:template.ValidTemplateYamlResponse)
  })
_sym_db.RegisterMessage(ValidTemplateYamlResponse)
_sym_db.RegisterMessage(ValidTemplateYamlResponse.CollectorMetrics)
_sym_db.RegisterMessage(ValidTemplateYamlResponse.CollectorMetrics.TagDefine)
_sym_db.RegisterMessage(ValidTemplateYamlResponse.MetricNames)
_sym_db.RegisterMessage(ValidTemplateYamlResponse.Params)

ValidTemplateYamlResponseWrapper = _reflection.GeneratedProtocolMessageType('ValidTemplateYamlResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _VALIDTEMPLATEYAMLRESPONSEWRAPPER,
  '__module__' : 'valid_template_yaml_pb2'
  # @@protoc_insertion_point(class_scope:template.ValidTemplateYamlResponseWrapper)
  })
_sym_db.RegisterMessage(ValidTemplateYamlResponseWrapper)


# @@protoc_insertion_point(module_scope)