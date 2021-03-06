# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: key.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='key.proto',
  package='collector_service',
  syntax='proto3',
  serialized_options=_b('ZKgo.easyops.local/contracts/protorepo-models/easyops/model/collector_service'),
  serialized_pb=_b('\n\tkey.proto\x12\x11\x63ollector_service\"\xe7\x03\n\x0c\x43ollectorKey\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07keyName\x18\x02 \x01(\t\x12\x0e\n\x06labels\x18\x03 \x03(\t\x12\r\n\x05keyId\x18\x04 \x01(\t\x12\x0f\n\x07version\x18\x05 \x01(\x05\x12\x0b\n\x03key\x18\x06 \x01(\t\x12\x12\n\nmetricType\x18\x07 \x01(\t\x12\x10\n\x08\x64\x61taType\x18\x08 \x01(\t\x12\x11\n\tagentType\x18\t \x01(\t\x12<\n\ttagDefine\x18\n \x03(\x0b\x32).collector_service.CollectorKey.TagDefine\x12@\n\x0bparamDefine\x18\x0b \x03(\x0b\x32+.collector_service.CollectorKey.ParamDefine\x12\x0c\n\x04help\x18\x0c \x01(\t\x12\x0c\n\x04unit\x18\r \x01(\t\x12\x15\n\rmetricVersion\x18\x0e \x01(\x05\x1a<\n\tTagDefine\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x02 \x01(\t\x12\x10\n\x08readOnly\x18\x03 \x01(\x08\x1aQ\n\x0bParamDefine\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tvalueType\x18\x02 \x01(\t\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x03 \x01(\t\x12\x10\n\x08readOnly\x18\x04 \x01(\x08\x42MZKgo.easyops.local/contracts/protorepo-models/easyops/model/collector_serviceb\x06proto3')
)




_COLLECTORKEY_TAGDEFINE = _descriptor.Descriptor(
  name='TagDefine',
  full_name='collector_service.CollectorKey.TagDefine',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='collector_service.CollectorKey.TagDefine.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default', full_name='collector_service.CollectorKey.TagDefine.default', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readOnly', full_name='collector_service.CollectorKey.TagDefine.readOnly', index=2,
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
  serialized_start=377,
  serialized_end=437,
)

_COLLECTORKEY_PARAMDEFINE = _descriptor.Descriptor(
  name='ParamDefine',
  full_name='collector_service.CollectorKey.ParamDefine',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='collector_service.CollectorKey.ParamDefine.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='valueType', full_name='collector_service.CollectorKey.ParamDefine.valueType', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default', full_name='collector_service.CollectorKey.ParamDefine.default', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readOnly', full_name='collector_service.CollectorKey.ParamDefine.readOnly', index=3,
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
  serialized_start=439,
  serialized_end=520,
)

_COLLECTORKEY = _descriptor.Descriptor(
  name='CollectorKey',
  full_name='collector_service.CollectorKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='collector_service.CollectorKey.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keyName', full_name='collector_service.CollectorKey.keyName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='collector_service.CollectorKey.labels', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keyId', full_name='collector_service.CollectorKey.keyId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='collector_service.CollectorKey.version', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='collector_service.CollectorKey.key', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metricType', full_name='collector_service.CollectorKey.metricType', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataType', full_name='collector_service.CollectorKey.dataType', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agentType', full_name='collector_service.CollectorKey.agentType', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tagDefine', full_name='collector_service.CollectorKey.tagDefine', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paramDefine', full_name='collector_service.CollectorKey.paramDefine', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='help', full_name='collector_service.CollectorKey.help', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unit', full_name='collector_service.CollectorKey.unit', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metricVersion', full_name='collector_service.CollectorKey.metricVersion', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_COLLECTORKEY_TAGDEFINE, _COLLECTORKEY_PARAMDEFINE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=520,
)

_COLLECTORKEY_TAGDEFINE.containing_type = _COLLECTORKEY
_COLLECTORKEY_PARAMDEFINE.containing_type = _COLLECTORKEY
_COLLECTORKEY.fields_by_name['tagDefine'].message_type = _COLLECTORKEY_TAGDEFINE
_COLLECTORKEY.fields_by_name['paramDefine'].message_type = _COLLECTORKEY_PARAMDEFINE
DESCRIPTOR.message_types_by_name['CollectorKey'] = _COLLECTORKEY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CollectorKey = _reflection.GeneratedProtocolMessageType('CollectorKey', (_message.Message,), {

  'TagDefine' : _reflection.GeneratedProtocolMessageType('TagDefine', (_message.Message,), {
    'DESCRIPTOR' : _COLLECTORKEY_TAGDEFINE,
    '__module__' : 'key_pb2'
    # @@protoc_insertion_point(class_scope:collector_service.CollectorKey.TagDefine)
    })
  ,

  'ParamDefine' : _reflection.GeneratedProtocolMessageType('ParamDefine', (_message.Message,), {
    'DESCRIPTOR' : _COLLECTORKEY_PARAMDEFINE,
    '__module__' : 'key_pb2'
    # @@protoc_insertion_point(class_scope:collector_service.CollectorKey.ParamDefine)
    })
  ,
  'DESCRIPTOR' : _COLLECTORKEY,
  '__module__' : 'key_pb2'
  # @@protoc_insertion_point(class_scope:collector_service.CollectorKey)
  })
_sym_db.RegisterMessage(CollectorKey)
_sym_db.RegisterMessage(CollectorKey.TagDefine)
_sym_db.RegisterMessage(CollectorKey.ParamDefine)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
