# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: update_collector_key_by_name.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='update_collector_key_by_name.proto',
  package='key',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\"update_collector_key_by_name.proto\x12\x03key\"\xa2\x04\n\x1fUpdateCollectorKeyByNameRequest\x12;\n\x06parent\x18\x01 \x01(\x0b\x32+.key.UpdateCollectorKeyByNameRequest.Parent\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03key\x18\x03 \x01(\t\x12\x0f\n\x07keyName\x18\x04 \x01(\t\x12\x0e\n\x06labels\x18\x05 \x03(\t\x12\x12\n\nmetricType\x18\x06 \x01(\t\x12\x10\n\x08\x64\x61taType\x18\x07 \x01(\t\x12\x11\n\tagentType\x18\x08 \x01(\t\x12\x41\n\ttagDefine\x18\t \x03(\x0b\x32..key.UpdateCollectorKeyByNameRequest.TagDefine\x12\x45\n\x0bparamDefine\x18\n \x03(\x0b\x32\x30.key.UpdateCollectorKeyByNameRequest.ParamDefine\x12\x0c\n\x04help\x18\x0b \x01(\t\x12\x0c\n\x04unit\x18\x0c \x01(\t\x1a\x16\n\x06Parent\x12\x0c\n\x04name\x18\x01 \x01(\t\x1a<\n\tTagDefine\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x02 \x01(\t\x12\x10\n\x08readOnly\x18\x03 \x01(\x08\x1aQ\n\x0bParamDefine\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tvalueType\x18\x02 \x01(\t\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x03 \x01(\t\x12\x10\n\x08readOnly\x18\x04 \x01(\x08\"1\n UpdateCollectorKeyByNameResponse\x12\r\n\x05keyId\x18\x01 \x01(\t\"\x90\x01\n\'UpdateCollectorKeyByNameResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x33\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32%.key.UpdateCollectorKeyByNameResponseb\x06proto3')
)




_UPDATECOLLECTORKEYBYNAMEREQUEST_PARENT = _descriptor.Descriptor(
  name='Parent',
  full_name='key.UpdateCollectorKeyByNameRequest.Parent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='key.UpdateCollectorKeyByNameRequest.Parent.name', index=0,
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
  serialized_start=423,
  serialized_end=445,
)

_UPDATECOLLECTORKEYBYNAMEREQUEST_TAGDEFINE = _descriptor.Descriptor(
  name='TagDefine',
  full_name='key.UpdateCollectorKeyByNameRequest.TagDefine',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='key.UpdateCollectorKeyByNameRequest.TagDefine.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default', full_name='key.UpdateCollectorKeyByNameRequest.TagDefine.default', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readOnly', full_name='key.UpdateCollectorKeyByNameRequest.TagDefine.readOnly', index=2,
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
  serialized_start=447,
  serialized_end=507,
)

_UPDATECOLLECTORKEYBYNAMEREQUEST_PARAMDEFINE = _descriptor.Descriptor(
  name='ParamDefine',
  full_name='key.UpdateCollectorKeyByNameRequest.ParamDefine',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='key.UpdateCollectorKeyByNameRequest.ParamDefine.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='valueType', full_name='key.UpdateCollectorKeyByNameRequest.ParamDefine.valueType', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default', full_name='key.UpdateCollectorKeyByNameRequest.ParamDefine.default', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readOnly', full_name='key.UpdateCollectorKeyByNameRequest.ParamDefine.readOnly', index=3,
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
  serialized_start=509,
  serialized_end=590,
)

_UPDATECOLLECTORKEYBYNAMEREQUEST = _descriptor.Descriptor(
  name='UpdateCollectorKeyByNameRequest',
  full_name='key.UpdateCollectorKeyByNameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='key.UpdateCollectorKeyByNameRequest.parent', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='key.UpdateCollectorKeyByNameRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='key.UpdateCollectorKeyByNameRequest.key', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keyName', full_name='key.UpdateCollectorKeyByNameRequest.keyName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='key.UpdateCollectorKeyByNameRequest.labels', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metricType', full_name='key.UpdateCollectorKeyByNameRequest.metricType', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataType', full_name='key.UpdateCollectorKeyByNameRequest.dataType', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agentType', full_name='key.UpdateCollectorKeyByNameRequest.agentType', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tagDefine', full_name='key.UpdateCollectorKeyByNameRequest.tagDefine', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paramDefine', full_name='key.UpdateCollectorKeyByNameRequest.paramDefine', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='help', full_name='key.UpdateCollectorKeyByNameRequest.help', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unit', full_name='key.UpdateCollectorKeyByNameRequest.unit', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_UPDATECOLLECTORKEYBYNAMEREQUEST_PARENT, _UPDATECOLLECTORKEYBYNAMEREQUEST_TAGDEFINE, _UPDATECOLLECTORKEYBYNAMEREQUEST_PARAMDEFINE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=44,
  serialized_end=590,
)


_UPDATECOLLECTORKEYBYNAMERESPONSE = _descriptor.Descriptor(
  name='UpdateCollectorKeyByNameResponse',
  full_name='key.UpdateCollectorKeyByNameResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keyId', full_name='key.UpdateCollectorKeyByNameResponse.keyId', index=0,
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
  serialized_start=592,
  serialized_end=641,
)


_UPDATECOLLECTORKEYBYNAMERESPONSEWRAPPER = _descriptor.Descriptor(
  name='UpdateCollectorKeyByNameResponseWrapper',
  full_name='key.UpdateCollectorKeyByNameResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='key.UpdateCollectorKeyByNameResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='key.UpdateCollectorKeyByNameResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='key.UpdateCollectorKeyByNameResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='key.UpdateCollectorKeyByNameResponseWrapper.data', index=3,
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
  serialized_start=644,
  serialized_end=788,
)

_UPDATECOLLECTORKEYBYNAMEREQUEST_PARENT.containing_type = _UPDATECOLLECTORKEYBYNAMEREQUEST
_UPDATECOLLECTORKEYBYNAMEREQUEST_TAGDEFINE.containing_type = _UPDATECOLLECTORKEYBYNAMEREQUEST
_UPDATECOLLECTORKEYBYNAMEREQUEST_PARAMDEFINE.containing_type = _UPDATECOLLECTORKEYBYNAMEREQUEST
_UPDATECOLLECTORKEYBYNAMEREQUEST.fields_by_name['parent'].message_type = _UPDATECOLLECTORKEYBYNAMEREQUEST_PARENT
_UPDATECOLLECTORKEYBYNAMEREQUEST.fields_by_name['tagDefine'].message_type = _UPDATECOLLECTORKEYBYNAMEREQUEST_TAGDEFINE
_UPDATECOLLECTORKEYBYNAMEREQUEST.fields_by_name['paramDefine'].message_type = _UPDATECOLLECTORKEYBYNAMEREQUEST_PARAMDEFINE
_UPDATECOLLECTORKEYBYNAMERESPONSEWRAPPER.fields_by_name['data'].message_type = _UPDATECOLLECTORKEYBYNAMERESPONSE
DESCRIPTOR.message_types_by_name['UpdateCollectorKeyByNameRequest'] = _UPDATECOLLECTORKEYBYNAMEREQUEST
DESCRIPTOR.message_types_by_name['UpdateCollectorKeyByNameResponse'] = _UPDATECOLLECTORKEYBYNAMERESPONSE
DESCRIPTOR.message_types_by_name['UpdateCollectorKeyByNameResponseWrapper'] = _UPDATECOLLECTORKEYBYNAMERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateCollectorKeyByNameRequest = _reflection.GeneratedProtocolMessageType('UpdateCollectorKeyByNameRequest', (_message.Message,), {

  'Parent' : _reflection.GeneratedProtocolMessageType('Parent', (_message.Message,), {
    'DESCRIPTOR' : _UPDATECOLLECTORKEYBYNAMEREQUEST_PARENT,
    '__module__' : 'update_collector_key_by_name_pb2'
    # @@protoc_insertion_point(class_scope:key.UpdateCollectorKeyByNameRequest.Parent)
    })
  ,

  'TagDefine' : _reflection.GeneratedProtocolMessageType('TagDefine', (_message.Message,), {
    'DESCRIPTOR' : _UPDATECOLLECTORKEYBYNAMEREQUEST_TAGDEFINE,
    '__module__' : 'update_collector_key_by_name_pb2'
    # @@protoc_insertion_point(class_scope:key.UpdateCollectorKeyByNameRequest.TagDefine)
    })
  ,

  'ParamDefine' : _reflection.GeneratedProtocolMessageType('ParamDefine', (_message.Message,), {
    'DESCRIPTOR' : _UPDATECOLLECTORKEYBYNAMEREQUEST_PARAMDEFINE,
    '__module__' : 'update_collector_key_by_name_pb2'
    # @@protoc_insertion_point(class_scope:key.UpdateCollectorKeyByNameRequest.ParamDefine)
    })
  ,
  'DESCRIPTOR' : _UPDATECOLLECTORKEYBYNAMEREQUEST,
  '__module__' : 'update_collector_key_by_name_pb2'
  # @@protoc_insertion_point(class_scope:key.UpdateCollectorKeyByNameRequest)
  })
_sym_db.RegisterMessage(UpdateCollectorKeyByNameRequest)
_sym_db.RegisterMessage(UpdateCollectorKeyByNameRequest.Parent)
_sym_db.RegisterMessage(UpdateCollectorKeyByNameRequest.TagDefine)
_sym_db.RegisterMessage(UpdateCollectorKeyByNameRequest.ParamDefine)

UpdateCollectorKeyByNameResponse = _reflection.GeneratedProtocolMessageType('UpdateCollectorKeyByNameResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATECOLLECTORKEYBYNAMERESPONSE,
  '__module__' : 'update_collector_key_by_name_pb2'
  # @@protoc_insertion_point(class_scope:key.UpdateCollectorKeyByNameResponse)
  })
_sym_db.RegisterMessage(UpdateCollectorKeyByNameResponse)

UpdateCollectorKeyByNameResponseWrapper = _reflection.GeneratedProtocolMessageType('UpdateCollectorKeyByNameResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _UPDATECOLLECTORKEYBYNAMERESPONSEWRAPPER,
  '__module__' : 'update_collector_key_by_name_pb2'
  # @@protoc_insertion_point(class_scope:key.UpdateCollectorKeyByNameResponseWrapper)
  })
_sym_db.RegisterMessage(UpdateCollectorKeyByNameResponseWrapper)


# @@protoc_insertion_point(module_scope)