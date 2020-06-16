# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: update_metric.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='update_metric.proto',
  package='metric',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13update_metric.proto\x12\x06metric\"\xdf\x04\n\"UpdateCollectorMetricByNameRequest\x12\x41\n\x06parent\x18\x01 \x01(\x0b\x32\x31.metric.UpdateCollectorMetricByNameRequest.Parent\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03key\x18\x03 \x01(\t\x12\x0f\n\x07keyName\x18\x04 \x01(\t\x12\x0e\n\x06labels\x18\x05 \x03(\t\x12\x12\n\nmetricType\x18\x06 \x01(\t\x12\x10\n\x08\x64\x61taType\x18\x07 \x01(\t\x12\x11\n\tagentType\x18\x08 \x01(\t\x12G\n\ttagDefine\x18\t \x03(\x0b\x32\x34.metric.UpdateCollectorMetricByNameRequest.TagDefine\x12K\n\x0bparamDefine\x18\n \x03(\x0b\x32\x36.metric.UpdateCollectorMetricByNameRequest.ParamDefine\x12\x0c\n\x04help\x18\x0b \x01(\t\x12\x0c\n\x04unit\x18\x0c \x01(\t\x1a\x16\n\x06Parent\x12\x0c\n\x04name\x18\x01 \x01(\t\x1a\x64\n\tTagDefine\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x02 \x01(\t\x12\x10\n\x08readOnly\x18\x03 \x01(\x08\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x11\n\tvalueType\x18\x05 \x01(\t\x1aQ\n\x0bParamDefine\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tvalueType\x18\x02 \x01(\t\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x03 \x01(\t\x12\x10\n\x08readOnly\x18\x04 \x01(\x08\"7\n#UpdateCollectorMetricByNameResponse\x12\x10\n\x08metricId\x18\x01 \x01(\t\"\x99\x01\n*UpdateCollectorMetricByNameResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x39\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32+.metric.UpdateCollectorMetricByNameResponseb\x06proto3')
)




_UPDATECOLLECTORMETRICBYNAMEREQUEST_PARENT = _descriptor.Descriptor(
  name='Parent',
  full_name='metric.UpdateCollectorMetricByNameRequest.Parent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='metric.UpdateCollectorMetricByNameRequest.Parent.name', index=0,
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
  serialized_start=432,
  serialized_end=454,
)

_UPDATECOLLECTORMETRICBYNAMEREQUEST_TAGDEFINE = _descriptor.Descriptor(
  name='TagDefine',
  full_name='metric.UpdateCollectorMetricByNameRequest.TagDefine',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='metric.UpdateCollectorMetricByNameRequest.TagDefine.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default', full_name='metric.UpdateCollectorMetricByNameRequest.TagDefine.default', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readOnly', full_name='metric.UpdateCollectorMetricByNameRequest.TagDefine.readOnly', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='metric.UpdateCollectorMetricByNameRequest.TagDefine.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='valueType', full_name='metric.UpdateCollectorMetricByNameRequest.TagDefine.valueType', index=4,
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
  serialized_start=456,
  serialized_end=556,
)

_UPDATECOLLECTORMETRICBYNAMEREQUEST_PARAMDEFINE = _descriptor.Descriptor(
  name='ParamDefine',
  full_name='metric.UpdateCollectorMetricByNameRequest.ParamDefine',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='metric.UpdateCollectorMetricByNameRequest.ParamDefine.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='valueType', full_name='metric.UpdateCollectorMetricByNameRequest.ParamDefine.valueType', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default', full_name='metric.UpdateCollectorMetricByNameRequest.ParamDefine.default', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readOnly', full_name='metric.UpdateCollectorMetricByNameRequest.ParamDefine.readOnly', index=3,
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
  serialized_start=558,
  serialized_end=639,
)

_UPDATECOLLECTORMETRICBYNAMEREQUEST = _descriptor.Descriptor(
  name='UpdateCollectorMetricByNameRequest',
  full_name='metric.UpdateCollectorMetricByNameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='metric.UpdateCollectorMetricByNameRequest.parent', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='metric.UpdateCollectorMetricByNameRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='metric.UpdateCollectorMetricByNameRequest.key', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keyName', full_name='metric.UpdateCollectorMetricByNameRequest.keyName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='metric.UpdateCollectorMetricByNameRequest.labels', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metricType', full_name='metric.UpdateCollectorMetricByNameRequest.metricType', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataType', full_name='metric.UpdateCollectorMetricByNameRequest.dataType', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agentType', full_name='metric.UpdateCollectorMetricByNameRequest.agentType', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tagDefine', full_name='metric.UpdateCollectorMetricByNameRequest.tagDefine', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paramDefine', full_name='metric.UpdateCollectorMetricByNameRequest.paramDefine', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='help', full_name='metric.UpdateCollectorMetricByNameRequest.help', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unit', full_name='metric.UpdateCollectorMetricByNameRequest.unit', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_UPDATECOLLECTORMETRICBYNAMEREQUEST_PARENT, _UPDATECOLLECTORMETRICBYNAMEREQUEST_TAGDEFINE, _UPDATECOLLECTORMETRICBYNAMEREQUEST_PARAMDEFINE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=639,
)


_UPDATECOLLECTORMETRICBYNAMERESPONSE = _descriptor.Descriptor(
  name='UpdateCollectorMetricByNameResponse',
  full_name='metric.UpdateCollectorMetricByNameResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metricId', full_name='metric.UpdateCollectorMetricByNameResponse.metricId', index=0,
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
  serialized_start=641,
  serialized_end=696,
)


_UPDATECOLLECTORMETRICBYNAMERESPONSEWRAPPER = _descriptor.Descriptor(
  name='UpdateCollectorMetricByNameResponseWrapper',
  full_name='metric.UpdateCollectorMetricByNameResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='metric.UpdateCollectorMetricByNameResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='metric.UpdateCollectorMetricByNameResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='metric.UpdateCollectorMetricByNameResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='metric.UpdateCollectorMetricByNameResponseWrapper.data', index=3,
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
  serialized_start=699,
  serialized_end=852,
)

_UPDATECOLLECTORMETRICBYNAMEREQUEST_PARENT.containing_type = _UPDATECOLLECTORMETRICBYNAMEREQUEST
_UPDATECOLLECTORMETRICBYNAMEREQUEST_TAGDEFINE.containing_type = _UPDATECOLLECTORMETRICBYNAMEREQUEST
_UPDATECOLLECTORMETRICBYNAMEREQUEST_PARAMDEFINE.containing_type = _UPDATECOLLECTORMETRICBYNAMEREQUEST
_UPDATECOLLECTORMETRICBYNAMEREQUEST.fields_by_name['parent'].message_type = _UPDATECOLLECTORMETRICBYNAMEREQUEST_PARENT
_UPDATECOLLECTORMETRICBYNAMEREQUEST.fields_by_name['tagDefine'].message_type = _UPDATECOLLECTORMETRICBYNAMEREQUEST_TAGDEFINE
_UPDATECOLLECTORMETRICBYNAMEREQUEST.fields_by_name['paramDefine'].message_type = _UPDATECOLLECTORMETRICBYNAMEREQUEST_PARAMDEFINE
_UPDATECOLLECTORMETRICBYNAMERESPONSEWRAPPER.fields_by_name['data'].message_type = _UPDATECOLLECTORMETRICBYNAMERESPONSE
DESCRIPTOR.message_types_by_name['UpdateCollectorMetricByNameRequest'] = _UPDATECOLLECTORMETRICBYNAMEREQUEST
DESCRIPTOR.message_types_by_name['UpdateCollectorMetricByNameResponse'] = _UPDATECOLLECTORMETRICBYNAMERESPONSE
DESCRIPTOR.message_types_by_name['UpdateCollectorMetricByNameResponseWrapper'] = _UPDATECOLLECTORMETRICBYNAMERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateCollectorMetricByNameRequest = _reflection.GeneratedProtocolMessageType('UpdateCollectorMetricByNameRequest', (_message.Message,), {

  'Parent' : _reflection.GeneratedProtocolMessageType('Parent', (_message.Message,), {
    'DESCRIPTOR' : _UPDATECOLLECTORMETRICBYNAMEREQUEST_PARENT,
    '__module__' : 'update_metric_pb2'
    # @@protoc_insertion_point(class_scope:metric.UpdateCollectorMetricByNameRequest.Parent)
    })
  ,

  'TagDefine' : _reflection.GeneratedProtocolMessageType('TagDefine', (_message.Message,), {
    'DESCRIPTOR' : _UPDATECOLLECTORMETRICBYNAMEREQUEST_TAGDEFINE,
    '__module__' : 'update_metric_pb2'
    # @@protoc_insertion_point(class_scope:metric.UpdateCollectorMetricByNameRequest.TagDefine)
    })
  ,

  'ParamDefine' : _reflection.GeneratedProtocolMessageType('ParamDefine', (_message.Message,), {
    'DESCRIPTOR' : _UPDATECOLLECTORMETRICBYNAMEREQUEST_PARAMDEFINE,
    '__module__' : 'update_metric_pb2'
    # @@protoc_insertion_point(class_scope:metric.UpdateCollectorMetricByNameRequest.ParamDefine)
    })
  ,
  'DESCRIPTOR' : _UPDATECOLLECTORMETRICBYNAMEREQUEST,
  '__module__' : 'update_metric_pb2'
  # @@protoc_insertion_point(class_scope:metric.UpdateCollectorMetricByNameRequest)
  })
_sym_db.RegisterMessage(UpdateCollectorMetricByNameRequest)
_sym_db.RegisterMessage(UpdateCollectorMetricByNameRequest.Parent)
_sym_db.RegisterMessage(UpdateCollectorMetricByNameRequest.TagDefine)
_sym_db.RegisterMessage(UpdateCollectorMetricByNameRequest.ParamDefine)

UpdateCollectorMetricByNameResponse = _reflection.GeneratedProtocolMessageType('UpdateCollectorMetricByNameResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATECOLLECTORMETRICBYNAMERESPONSE,
  '__module__' : 'update_metric_pb2'
  # @@protoc_insertion_point(class_scope:metric.UpdateCollectorMetricByNameResponse)
  })
_sym_db.RegisterMessage(UpdateCollectorMetricByNameResponse)

UpdateCollectorMetricByNameResponseWrapper = _reflection.GeneratedProtocolMessageType('UpdateCollectorMetricByNameResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _UPDATECOLLECTORMETRICBYNAMERESPONSEWRAPPER,
  '__module__' : 'update_metric_pb2'
  # @@protoc_insertion_point(class_scope:metric.UpdateCollectorMetricByNameResponseWrapper)
  })
_sym_db.RegisterMessage(UpdateCollectorMetricByNameResponseWrapper)


# @@protoc_insertion_point(module_scope)