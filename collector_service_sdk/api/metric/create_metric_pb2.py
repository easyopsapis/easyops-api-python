# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: create_metric.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='create_metric.proto',
  package='metric',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13\x63reate_metric.proto\x12\x06metric\"\xb9\x04\n\x1c\x43reateCollectorMetricRequest\x12;\n\x06parent\x18\x01 \x01(\x0b\x32+.metric.CreateCollectorMetricRequest.Parent\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x0f\n\x07keyName\x18\x03 \x01(\t\x12\x0e\n\x06labels\x18\x04 \x03(\t\x12\x12\n\nmetricType\x18\x05 \x01(\t\x12\x10\n\x08\x64\x61taType\x18\x06 \x01(\t\x12\x11\n\tagentType\x18\x07 \x01(\t\x12\x41\n\ttagDefine\x18\x08 \x03(\x0b\x32..metric.CreateCollectorMetricRequest.TagDefine\x12\x45\n\x0bparamDefine\x18\t \x03(\x0b\x32\x30.metric.CreateCollectorMetricRequest.ParamDefine\x12\x0c\n\x04help\x18\n \x01(\t\x12\x0c\n\x04unit\x18\x0b \x01(\t\x1a\x16\n\x06Parent\x12\x0c\n\x04name\x18\x01 \x01(\t\x1a\x64\n\tTagDefine\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x02 \x01(\t\x12\x10\n\x08readOnly\x18\x03 \x01(\x08\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x11\n\tvalueType\x18\x05 \x01(\t\x1aQ\n\x0bParamDefine\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tvalueType\x18\x02 \x01(\t\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x03 \x01(\t\x12\x10\n\x08readOnly\x18\x04 \x01(\x08\"1\n\x1d\x43reateCollectorMetricResponse\x12\x10\n\x08metricId\x18\x01 \x01(\t\"\x8d\x01\n$CreateCollectorMetricResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x33\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32%.metric.CreateCollectorMetricResponseb\x06proto3')
)




_CREATECOLLECTORMETRICREQUEST_PARENT = _descriptor.Descriptor(
  name='Parent',
  full_name='metric.CreateCollectorMetricRequest.Parent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='metric.CreateCollectorMetricRequest.Parent.name', index=0,
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
  serialized_start=394,
  serialized_end=416,
)

_CREATECOLLECTORMETRICREQUEST_TAGDEFINE = _descriptor.Descriptor(
  name='TagDefine',
  full_name='metric.CreateCollectorMetricRequest.TagDefine',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='metric.CreateCollectorMetricRequest.TagDefine.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default', full_name='metric.CreateCollectorMetricRequest.TagDefine.default', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readOnly', full_name='metric.CreateCollectorMetricRequest.TagDefine.readOnly', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='metric.CreateCollectorMetricRequest.TagDefine.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='valueType', full_name='metric.CreateCollectorMetricRequest.TagDefine.valueType', index=4,
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
  serialized_start=418,
  serialized_end=518,
)

_CREATECOLLECTORMETRICREQUEST_PARAMDEFINE = _descriptor.Descriptor(
  name='ParamDefine',
  full_name='metric.CreateCollectorMetricRequest.ParamDefine',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='metric.CreateCollectorMetricRequest.ParamDefine.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='valueType', full_name='metric.CreateCollectorMetricRequest.ParamDefine.valueType', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default', full_name='metric.CreateCollectorMetricRequest.ParamDefine.default', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readOnly', full_name='metric.CreateCollectorMetricRequest.ParamDefine.readOnly', index=3,
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
  serialized_start=520,
  serialized_end=601,
)

_CREATECOLLECTORMETRICREQUEST = _descriptor.Descriptor(
  name='CreateCollectorMetricRequest',
  full_name='metric.CreateCollectorMetricRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='metric.CreateCollectorMetricRequest.parent', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='metric.CreateCollectorMetricRequest.key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keyName', full_name='metric.CreateCollectorMetricRequest.keyName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='metric.CreateCollectorMetricRequest.labels', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metricType', full_name='metric.CreateCollectorMetricRequest.metricType', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataType', full_name='metric.CreateCollectorMetricRequest.dataType', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agentType', full_name='metric.CreateCollectorMetricRequest.agentType', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tagDefine', full_name='metric.CreateCollectorMetricRequest.tagDefine', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paramDefine', full_name='metric.CreateCollectorMetricRequest.paramDefine', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='help', full_name='metric.CreateCollectorMetricRequest.help', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unit', full_name='metric.CreateCollectorMetricRequest.unit', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CREATECOLLECTORMETRICREQUEST_PARENT, _CREATECOLLECTORMETRICREQUEST_TAGDEFINE, _CREATECOLLECTORMETRICREQUEST_PARAMDEFINE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=601,
)


_CREATECOLLECTORMETRICRESPONSE = _descriptor.Descriptor(
  name='CreateCollectorMetricResponse',
  full_name='metric.CreateCollectorMetricResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metricId', full_name='metric.CreateCollectorMetricResponse.metricId', index=0,
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
  serialized_start=603,
  serialized_end=652,
)


_CREATECOLLECTORMETRICRESPONSEWRAPPER = _descriptor.Descriptor(
  name='CreateCollectorMetricResponseWrapper',
  full_name='metric.CreateCollectorMetricResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='metric.CreateCollectorMetricResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='metric.CreateCollectorMetricResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='metric.CreateCollectorMetricResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='metric.CreateCollectorMetricResponseWrapper.data', index=3,
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
  serialized_start=655,
  serialized_end=796,
)

_CREATECOLLECTORMETRICREQUEST_PARENT.containing_type = _CREATECOLLECTORMETRICREQUEST
_CREATECOLLECTORMETRICREQUEST_TAGDEFINE.containing_type = _CREATECOLLECTORMETRICREQUEST
_CREATECOLLECTORMETRICREQUEST_PARAMDEFINE.containing_type = _CREATECOLLECTORMETRICREQUEST
_CREATECOLLECTORMETRICREQUEST.fields_by_name['parent'].message_type = _CREATECOLLECTORMETRICREQUEST_PARENT
_CREATECOLLECTORMETRICREQUEST.fields_by_name['tagDefine'].message_type = _CREATECOLLECTORMETRICREQUEST_TAGDEFINE
_CREATECOLLECTORMETRICREQUEST.fields_by_name['paramDefine'].message_type = _CREATECOLLECTORMETRICREQUEST_PARAMDEFINE
_CREATECOLLECTORMETRICRESPONSEWRAPPER.fields_by_name['data'].message_type = _CREATECOLLECTORMETRICRESPONSE
DESCRIPTOR.message_types_by_name['CreateCollectorMetricRequest'] = _CREATECOLLECTORMETRICREQUEST
DESCRIPTOR.message_types_by_name['CreateCollectorMetricResponse'] = _CREATECOLLECTORMETRICRESPONSE
DESCRIPTOR.message_types_by_name['CreateCollectorMetricResponseWrapper'] = _CREATECOLLECTORMETRICRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateCollectorMetricRequest = _reflection.GeneratedProtocolMessageType('CreateCollectorMetricRequest', (_message.Message,), {

  'Parent' : _reflection.GeneratedProtocolMessageType('Parent', (_message.Message,), {
    'DESCRIPTOR' : _CREATECOLLECTORMETRICREQUEST_PARENT,
    '__module__' : 'create_metric_pb2'
    # @@protoc_insertion_point(class_scope:metric.CreateCollectorMetricRequest.Parent)
    })
  ,

  'TagDefine' : _reflection.GeneratedProtocolMessageType('TagDefine', (_message.Message,), {
    'DESCRIPTOR' : _CREATECOLLECTORMETRICREQUEST_TAGDEFINE,
    '__module__' : 'create_metric_pb2'
    # @@protoc_insertion_point(class_scope:metric.CreateCollectorMetricRequest.TagDefine)
    })
  ,

  'ParamDefine' : _reflection.GeneratedProtocolMessageType('ParamDefine', (_message.Message,), {
    'DESCRIPTOR' : _CREATECOLLECTORMETRICREQUEST_PARAMDEFINE,
    '__module__' : 'create_metric_pb2'
    # @@protoc_insertion_point(class_scope:metric.CreateCollectorMetricRequest.ParamDefine)
    })
  ,
  'DESCRIPTOR' : _CREATECOLLECTORMETRICREQUEST,
  '__module__' : 'create_metric_pb2'
  # @@protoc_insertion_point(class_scope:metric.CreateCollectorMetricRequest)
  })
_sym_db.RegisterMessage(CreateCollectorMetricRequest)
_sym_db.RegisterMessage(CreateCollectorMetricRequest.Parent)
_sym_db.RegisterMessage(CreateCollectorMetricRequest.TagDefine)
_sym_db.RegisterMessage(CreateCollectorMetricRequest.ParamDefine)

CreateCollectorMetricResponse = _reflection.GeneratedProtocolMessageType('CreateCollectorMetricResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATECOLLECTORMETRICRESPONSE,
  '__module__' : 'create_metric_pb2'
  # @@protoc_insertion_point(class_scope:metric.CreateCollectorMetricResponse)
  })
_sym_db.RegisterMessage(CreateCollectorMetricResponse)

CreateCollectorMetricResponseWrapper = _reflection.GeneratedProtocolMessageType('CreateCollectorMetricResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _CREATECOLLECTORMETRICRESPONSEWRAPPER,
  '__module__' : 'create_metric_pb2'
  # @@protoc_insertion_point(class_scope:metric.CreateCollectorMetricResponseWrapper)
  })
_sym_db.RegisterMessage(CreateCollectorMetricResponseWrapper)


# @@protoc_insertion_point(module_scope)