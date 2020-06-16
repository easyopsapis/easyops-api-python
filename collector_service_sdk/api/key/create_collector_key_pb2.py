# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: create_collector_key.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='create_collector_key.proto',
  package='key',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1a\x63reate_collector_key.proto\x12\x03key\"\xfc\x03\n\x19\x43reateCollectorKeyRequest\x12\x35\n\x06parent\x18\x01 \x01(\x0b\x32%.key.CreateCollectorKeyRequest.Parent\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x0f\n\x07keyName\x18\x03 \x01(\t\x12\x0e\n\x06labels\x18\x04 \x03(\t\x12\x12\n\nmetricType\x18\x05 \x01(\t\x12\x10\n\x08\x64\x61taType\x18\x06 \x01(\t\x12\x11\n\tagentType\x18\x07 \x01(\t\x12;\n\ttagDefine\x18\x08 \x03(\x0b\x32(.key.CreateCollectorKeyRequest.TagDefine\x12?\n\x0bparamDefine\x18\t \x03(\x0b\x32*.key.CreateCollectorKeyRequest.ParamDefine\x12\x0c\n\x04help\x18\n \x01(\t\x12\x0c\n\x04unit\x18\x0b \x01(\t\x1a\x16\n\x06Parent\x12\x0c\n\x04name\x18\x01 \x01(\t\x1a<\n\tTagDefine\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x02 \x01(\t\x12\x10\n\x08readOnly\x18\x03 \x01(\x08\x1aQ\n\x0bParamDefine\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tvalueType\x18\x02 \x01(\t\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x03 \x01(\t\x12\x10\n\x08readOnly\x18\x04 \x01(\x08\"+\n\x1a\x43reateCollectorKeyResponse\x12\r\n\x05keyId\x18\x01 \x01(\t\"\x84\x01\n!CreateCollectorKeyResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12-\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1f.key.CreateCollectorKeyResponseb\x06proto3')
)




_CREATECOLLECTORKEYREQUEST_PARENT = _descriptor.Descriptor(
  name='Parent',
  full_name='key.CreateCollectorKeyRequest.Parent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='key.CreateCollectorKeyRequest.Parent.name', index=0,
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
  serialized_start=377,
  serialized_end=399,
)

_CREATECOLLECTORKEYREQUEST_TAGDEFINE = _descriptor.Descriptor(
  name='TagDefine',
  full_name='key.CreateCollectorKeyRequest.TagDefine',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='key.CreateCollectorKeyRequest.TagDefine.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default', full_name='key.CreateCollectorKeyRequest.TagDefine.default', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readOnly', full_name='key.CreateCollectorKeyRequest.TagDefine.readOnly', index=2,
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
  serialized_start=401,
  serialized_end=461,
)

_CREATECOLLECTORKEYREQUEST_PARAMDEFINE = _descriptor.Descriptor(
  name='ParamDefine',
  full_name='key.CreateCollectorKeyRequest.ParamDefine',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='key.CreateCollectorKeyRequest.ParamDefine.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='valueType', full_name='key.CreateCollectorKeyRequest.ParamDefine.valueType', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default', full_name='key.CreateCollectorKeyRequest.ParamDefine.default', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readOnly', full_name='key.CreateCollectorKeyRequest.ParamDefine.readOnly', index=3,
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
  serialized_start=463,
  serialized_end=544,
)

_CREATECOLLECTORKEYREQUEST = _descriptor.Descriptor(
  name='CreateCollectorKeyRequest',
  full_name='key.CreateCollectorKeyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='key.CreateCollectorKeyRequest.parent', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='key.CreateCollectorKeyRequest.key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keyName', full_name='key.CreateCollectorKeyRequest.keyName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='key.CreateCollectorKeyRequest.labels', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metricType', full_name='key.CreateCollectorKeyRequest.metricType', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataType', full_name='key.CreateCollectorKeyRequest.dataType', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agentType', full_name='key.CreateCollectorKeyRequest.agentType', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tagDefine', full_name='key.CreateCollectorKeyRequest.tagDefine', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paramDefine', full_name='key.CreateCollectorKeyRequest.paramDefine', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='help', full_name='key.CreateCollectorKeyRequest.help', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unit', full_name='key.CreateCollectorKeyRequest.unit', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CREATECOLLECTORKEYREQUEST_PARENT, _CREATECOLLECTORKEYREQUEST_TAGDEFINE, _CREATECOLLECTORKEYREQUEST_PARAMDEFINE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=544,
)


_CREATECOLLECTORKEYRESPONSE = _descriptor.Descriptor(
  name='CreateCollectorKeyResponse',
  full_name='key.CreateCollectorKeyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keyId', full_name='key.CreateCollectorKeyResponse.keyId', index=0,
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
  serialized_start=546,
  serialized_end=589,
)


_CREATECOLLECTORKEYRESPONSEWRAPPER = _descriptor.Descriptor(
  name='CreateCollectorKeyResponseWrapper',
  full_name='key.CreateCollectorKeyResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='key.CreateCollectorKeyResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='key.CreateCollectorKeyResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='key.CreateCollectorKeyResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='key.CreateCollectorKeyResponseWrapper.data', index=3,
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
  serialized_start=592,
  serialized_end=724,
)

_CREATECOLLECTORKEYREQUEST_PARENT.containing_type = _CREATECOLLECTORKEYREQUEST
_CREATECOLLECTORKEYREQUEST_TAGDEFINE.containing_type = _CREATECOLLECTORKEYREQUEST
_CREATECOLLECTORKEYREQUEST_PARAMDEFINE.containing_type = _CREATECOLLECTORKEYREQUEST
_CREATECOLLECTORKEYREQUEST.fields_by_name['parent'].message_type = _CREATECOLLECTORKEYREQUEST_PARENT
_CREATECOLLECTORKEYREQUEST.fields_by_name['tagDefine'].message_type = _CREATECOLLECTORKEYREQUEST_TAGDEFINE
_CREATECOLLECTORKEYREQUEST.fields_by_name['paramDefine'].message_type = _CREATECOLLECTORKEYREQUEST_PARAMDEFINE
_CREATECOLLECTORKEYRESPONSEWRAPPER.fields_by_name['data'].message_type = _CREATECOLLECTORKEYRESPONSE
DESCRIPTOR.message_types_by_name['CreateCollectorKeyRequest'] = _CREATECOLLECTORKEYREQUEST
DESCRIPTOR.message_types_by_name['CreateCollectorKeyResponse'] = _CREATECOLLECTORKEYRESPONSE
DESCRIPTOR.message_types_by_name['CreateCollectorKeyResponseWrapper'] = _CREATECOLLECTORKEYRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateCollectorKeyRequest = _reflection.GeneratedProtocolMessageType('CreateCollectorKeyRequest', (_message.Message,), {

  'Parent' : _reflection.GeneratedProtocolMessageType('Parent', (_message.Message,), {
    'DESCRIPTOR' : _CREATECOLLECTORKEYREQUEST_PARENT,
    '__module__' : 'create_collector_key_pb2'
    # @@protoc_insertion_point(class_scope:key.CreateCollectorKeyRequest.Parent)
    })
  ,

  'TagDefine' : _reflection.GeneratedProtocolMessageType('TagDefine', (_message.Message,), {
    'DESCRIPTOR' : _CREATECOLLECTORKEYREQUEST_TAGDEFINE,
    '__module__' : 'create_collector_key_pb2'
    # @@protoc_insertion_point(class_scope:key.CreateCollectorKeyRequest.TagDefine)
    })
  ,

  'ParamDefine' : _reflection.GeneratedProtocolMessageType('ParamDefine', (_message.Message,), {
    'DESCRIPTOR' : _CREATECOLLECTORKEYREQUEST_PARAMDEFINE,
    '__module__' : 'create_collector_key_pb2'
    # @@protoc_insertion_point(class_scope:key.CreateCollectorKeyRequest.ParamDefine)
    })
  ,
  'DESCRIPTOR' : _CREATECOLLECTORKEYREQUEST,
  '__module__' : 'create_collector_key_pb2'
  # @@protoc_insertion_point(class_scope:key.CreateCollectorKeyRequest)
  })
_sym_db.RegisterMessage(CreateCollectorKeyRequest)
_sym_db.RegisterMessage(CreateCollectorKeyRequest.Parent)
_sym_db.RegisterMessage(CreateCollectorKeyRequest.TagDefine)
_sym_db.RegisterMessage(CreateCollectorKeyRequest.ParamDefine)

CreateCollectorKeyResponse = _reflection.GeneratedProtocolMessageType('CreateCollectorKeyResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATECOLLECTORKEYRESPONSE,
  '__module__' : 'create_collector_key_pb2'
  # @@protoc_insertion_point(class_scope:key.CreateCollectorKeyResponse)
  })
_sym_db.RegisterMessage(CreateCollectorKeyResponse)

CreateCollectorKeyResponseWrapper = _reflection.GeneratedProtocolMessageType('CreateCollectorKeyResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _CREATECOLLECTORKEYRESPONSEWRAPPER,
  '__module__' : 'create_collector_key_pb2'
  # @@protoc_insertion_point(class_scope:key.CreateCollectorKeyResponseWrapper)
  })
_sym_db.RegisterMessage(CreateCollectorKeyResponseWrapper)


# @@protoc_insertion_point(module_scope)
