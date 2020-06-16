# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: debug_collection_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='debug_collection_config.proto',
  package='collection_config',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1d\x64\x65\x62ug_collection_config.proto\x12\x11\x63ollection_config\x1a\x1cgoogle/protobuf/struct.proto\"\xb7\x04\n\x1c\x44\x65\x62ugCollectionConfigRequest\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0f\n\x07\x63lazzId\x18\x02 \x01(\t\x12\x15\n\rignoreInvalid\x18\x03 \x01(\x08\x12\x0f\n\x07timeout\x18\x04 \x01(\x05\x12\x46\n\x06script\x18\x05 \x01(\x0b\x32\x36.collection_config.DebugCollectionConfigRequest.Script\x12\x11\n\ttimeRange\x18\x06 \x01(\t\x12\x0c\n\x04name\x18\x07 \x01(\t\x12@\n\x03\x65nv\x18\x08 \x03(\x0b\x32\x33.collection_config.DebugCollectionConfigRequest.Env\x12\x46\n\x06kwargs\x18\t \x03(\x0b\x32\x36.collection_config.DebugCollectionConfigRequest.Kwargs\x12\x10\n\x08objectId\x18\n \x01(\t\x1aR\n\x06Script\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x1a\x39\n\x03\x45nv\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.Value\x1a<\n\x06Kwargs\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.Value\"+\n\x1d\x44\x65\x62ugCollectionConfigResponse\x12\n\n\x02id\x18\x01 \x01(\t\"\x98\x01\n$DebugCollectionConfigResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12>\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x30.collection_config.DebugCollectionConfigResponseb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_DEBUGCOLLECTIONCONFIGREQUEST_SCRIPT = _descriptor.Descriptor(
  name='Script',
  full_name='collection_config.DebugCollectionConfigRequest.Script',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='collection_config.DebugCollectionConfigRequest.Script.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='collection_config.DebugCollectionConfigRequest.Script.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='collection_config.DebugCollectionConfigRequest.Script.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='collection_config.DebugCollectionConfigRequest.Script.content', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='collection_config.DebugCollectionConfigRequest.Script.name', index=4,
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
  serialized_start=447,
  serialized_end=529,
)

_DEBUGCOLLECTIONCONFIGREQUEST_ENV = _descriptor.Descriptor(
  name='Env',
  full_name='collection_config.DebugCollectionConfigRequest.Env',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='collection_config.DebugCollectionConfigRequest.Env.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='collection_config.DebugCollectionConfigRequest.Env.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=531,
  serialized_end=588,
)

_DEBUGCOLLECTIONCONFIGREQUEST_KWARGS = _descriptor.Descriptor(
  name='Kwargs',
  full_name='collection_config.DebugCollectionConfigRequest.Kwargs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='collection_config.DebugCollectionConfigRequest.Kwargs.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='collection_config.DebugCollectionConfigRequest.Kwargs.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=590,
  serialized_end=650,
)

_DEBUGCOLLECTIONCONFIGREQUEST = _descriptor.Descriptor(
  name='DebugCollectionConfigRequest',
  full_name='collection_config.DebugCollectionConfigRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='host', full_name='collection_config.DebugCollectionConfigRequest.host', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clazzId', full_name='collection_config.DebugCollectionConfigRequest.clazzId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ignoreInvalid', full_name='collection_config.DebugCollectionConfigRequest.ignoreInvalid', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='collection_config.DebugCollectionConfigRequest.timeout', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='script', full_name='collection_config.DebugCollectionConfigRequest.script', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeRange', full_name='collection_config.DebugCollectionConfigRequest.timeRange', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='collection_config.DebugCollectionConfigRequest.name', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='env', full_name='collection_config.DebugCollectionConfigRequest.env', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kwargs', full_name='collection_config.DebugCollectionConfigRequest.kwargs', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectId', full_name='collection_config.DebugCollectionConfigRequest.objectId', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DEBUGCOLLECTIONCONFIGREQUEST_SCRIPT, _DEBUGCOLLECTIONCONFIGREQUEST_ENV, _DEBUGCOLLECTIONCONFIGREQUEST_KWARGS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=83,
  serialized_end=650,
)


_DEBUGCOLLECTIONCONFIGRESPONSE = _descriptor.Descriptor(
  name='DebugCollectionConfigResponse',
  full_name='collection_config.DebugCollectionConfigResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='collection_config.DebugCollectionConfigResponse.id', index=0,
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
  serialized_start=652,
  serialized_end=695,
)


_DEBUGCOLLECTIONCONFIGRESPONSEWRAPPER = _descriptor.Descriptor(
  name='DebugCollectionConfigResponseWrapper',
  full_name='collection_config.DebugCollectionConfigResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='collection_config.DebugCollectionConfigResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='collection_config.DebugCollectionConfigResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='collection_config.DebugCollectionConfigResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='collection_config.DebugCollectionConfigResponseWrapper.data', index=3,
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
  serialized_start=698,
  serialized_end=850,
)

_DEBUGCOLLECTIONCONFIGREQUEST_SCRIPT.containing_type = _DEBUGCOLLECTIONCONFIGREQUEST
_DEBUGCOLLECTIONCONFIGREQUEST_ENV.fields_by_name['value'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_DEBUGCOLLECTIONCONFIGREQUEST_ENV.containing_type = _DEBUGCOLLECTIONCONFIGREQUEST
_DEBUGCOLLECTIONCONFIGREQUEST_KWARGS.fields_by_name['value'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_DEBUGCOLLECTIONCONFIGREQUEST_KWARGS.containing_type = _DEBUGCOLLECTIONCONFIGREQUEST
_DEBUGCOLLECTIONCONFIGREQUEST.fields_by_name['script'].message_type = _DEBUGCOLLECTIONCONFIGREQUEST_SCRIPT
_DEBUGCOLLECTIONCONFIGREQUEST.fields_by_name['env'].message_type = _DEBUGCOLLECTIONCONFIGREQUEST_ENV
_DEBUGCOLLECTIONCONFIGREQUEST.fields_by_name['kwargs'].message_type = _DEBUGCOLLECTIONCONFIGREQUEST_KWARGS
_DEBUGCOLLECTIONCONFIGRESPONSEWRAPPER.fields_by_name['data'].message_type = _DEBUGCOLLECTIONCONFIGRESPONSE
DESCRIPTOR.message_types_by_name['DebugCollectionConfigRequest'] = _DEBUGCOLLECTIONCONFIGREQUEST
DESCRIPTOR.message_types_by_name['DebugCollectionConfigResponse'] = _DEBUGCOLLECTIONCONFIGRESPONSE
DESCRIPTOR.message_types_by_name['DebugCollectionConfigResponseWrapper'] = _DEBUGCOLLECTIONCONFIGRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DebugCollectionConfigRequest = _reflection.GeneratedProtocolMessageType('DebugCollectionConfigRequest', (_message.Message,), {

  'Script' : _reflection.GeneratedProtocolMessageType('Script', (_message.Message,), {
    'DESCRIPTOR' : _DEBUGCOLLECTIONCONFIGREQUEST_SCRIPT,
    '__module__' : 'debug_collection_config_pb2'
    # @@protoc_insertion_point(class_scope:collection_config.DebugCollectionConfigRequest.Script)
    })
  ,

  'Env' : _reflection.GeneratedProtocolMessageType('Env', (_message.Message,), {
    'DESCRIPTOR' : _DEBUGCOLLECTIONCONFIGREQUEST_ENV,
    '__module__' : 'debug_collection_config_pb2'
    # @@protoc_insertion_point(class_scope:collection_config.DebugCollectionConfigRequest.Env)
    })
  ,

  'Kwargs' : _reflection.GeneratedProtocolMessageType('Kwargs', (_message.Message,), {
    'DESCRIPTOR' : _DEBUGCOLLECTIONCONFIGREQUEST_KWARGS,
    '__module__' : 'debug_collection_config_pb2'
    # @@protoc_insertion_point(class_scope:collection_config.DebugCollectionConfigRequest.Kwargs)
    })
  ,
  'DESCRIPTOR' : _DEBUGCOLLECTIONCONFIGREQUEST,
  '__module__' : 'debug_collection_config_pb2'
  # @@protoc_insertion_point(class_scope:collection_config.DebugCollectionConfigRequest)
  })
_sym_db.RegisterMessage(DebugCollectionConfigRequest)
_sym_db.RegisterMessage(DebugCollectionConfigRequest.Script)
_sym_db.RegisterMessage(DebugCollectionConfigRequest.Env)
_sym_db.RegisterMessage(DebugCollectionConfigRequest.Kwargs)

DebugCollectionConfigResponse = _reflection.GeneratedProtocolMessageType('DebugCollectionConfigResponse', (_message.Message,), {
  'DESCRIPTOR' : _DEBUGCOLLECTIONCONFIGRESPONSE,
  '__module__' : 'debug_collection_config_pb2'
  # @@protoc_insertion_point(class_scope:collection_config.DebugCollectionConfigResponse)
  })
_sym_db.RegisterMessage(DebugCollectionConfigResponse)

DebugCollectionConfigResponseWrapper = _reflection.GeneratedProtocolMessageType('DebugCollectionConfigResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _DEBUGCOLLECTIONCONFIGRESPONSEWRAPPER,
  '__module__' : 'debug_collection_config_pb2'
  # @@protoc_insertion_point(class_scope:collection_config.DebugCollectionConfigResponseWrapper)
  })
_sym_db.RegisterMessage(DebugCollectionConfigResponseWrapper)


# @@protoc_insertion_point(module_scope)