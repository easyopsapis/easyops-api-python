# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: debug_collection_config_callback.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='debug_collection_config_callback.proto',
  package='collection_config',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n&debug_collection_config_callback.proto\x12\x11\x63ollection_config\"\xf5\x01\n$DebugCollectionConfigCallbackRequest\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x0e\n\x06taskId\x18\x04 \x01(\t\x12V\n\ntargetsLog\x18\x05 \x03(\x0b\x32\x42.collection_config.DebugCollectionConfigCallbackRequest.TargetsLog\x1a\x37\n\nTargetsLog\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\"7\n%DebugCollectionConfigCallbackResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"\xa8\x01\n,DebugCollectionConfigCallbackResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x46\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x38.collection_config.DebugCollectionConfigCallbackResponseb\x06proto3')
)




_DEBUGCOLLECTIONCONFIGCALLBACKREQUEST_TARGETSLOG = _descriptor.Descriptor(
  name='TargetsLog',
  full_name='collection_config.DebugCollectionConfigCallbackRequest.TargetsLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='collection_config.DebugCollectionConfigCallbackRequest.TargetsLog.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='collection_config.DebugCollectionConfigCallbackRequest.TargetsLog.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='collection_config.DebugCollectionConfigCallbackRequest.TargetsLog.status', index=2,
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
  serialized_start=252,
  serialized_end=307,
)

_DEBUGCOLLECTIONCONFIGCALLBACKREQUEST = _descriptor.Descriptor(
  name='DebugCollectionConfigCallbackRequest',
  full_name='collection_config.DebugCollectionConfigCallbackRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='collection_config.DebugCollectionConfigCallbackRequest.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='collection_config.DebugCollectionConfigCallbackRequest.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='collection_config.DebugCollectionConfigCallbackRequest.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='taskId', full_name='collection_config.DebugCollectionConfigCallbackRequest.taskId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targetsLog', full_name='collection_config.DebugCollectionConfigCallbackRequest.targetsLog', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DEBUGCOLLECTIONCONFIGCALLBACKREQUEST_TARGETSLOG, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=307,
)


_DEBUGCOLLECTIONCONFIGCALLBACKRESPONSE = _descriptor.Descriptor(
  name='DebugCollectionConfigCallbackResponse',
  full_name='collection_config.DebugCollectionConfigCallbackResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='collection_config.DebugCollectionConfigCallbackResponse.status', index=0,
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
  serialized_start=309,
  serialized_end=364,
)


_DEBUGCOLLECTIONCONFIGCALLBACKRESPONSEWRAPPER = _descriptor.Descriptor(
  name='DebugCollectionConfigCallbackResponseWrapper',
  full_name='collection_config.DebugCollectionConfigCallbackResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='collection_config.DebugCollectionConfigCallbackResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='collection_config.DebugCollectionConfigCallbackResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='collection_config.DebugCollectionConfigCallbackResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='collection_config.DebugCollectionConfigCallbackResponseWrapper.data', index=3,
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
  serialized_start=367,
  serialized_end=535,
)

_DEBUGCOLLECTIONCONFIGCALLBACKREQUEST_TARGETSLOG.containing_type = _DEBUGCOLLECTIONCONFIGCALLBACKREQUEST
_DEBUGCOLLECTIONCONFIGCALLBACKREQUEST.fields_by_name['targetsLog'].message_type = _DEBUGCOLLECTIONCONFIGCALLBACKREQUEST_TARGETSLOG
_DEBUGCOLLECTIONCONFIGCALLBACKRESPONSEWRAPPER.fields_by_name['data'].message_type = _DEBUGCOLLECTIONCONFIGCALLBACKRESPONSE
DESCRIPTOR.message_types_by_name['DebugCollectionConfigCallbackRequest'] = _DEBUGCOLLECTIONCONFIGCALLBACKREQUEST
DESCRIPTOR.message_types_by_name['DebugCollectionConfigCallbackResponse'] = _DEBUGCOLLECTIONCONFIGCALLBACKRESPONSE
DESCRIPTOR.message_types_by_name['DebugCollectionConfigCallbackResponseWrapper'] = _DEBUGCOLLECTIONCONFIGCALLBACKRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DebugCollectionConfigCallbackRequest = _reflection.GeneratedProtocolMessageType('DebugCollectionConfigCallbackRequest', (_message.Message,), {

  'TargetsLog' : _reflection.GeneratedProtocolMessageType('TargetsLog', (_message.Message,), {
    'DESCRIPTOR' : _DEBUGCOLLECTIONCONFIGCALLBACKREQUEST_TARGETSLOG,
    '__module__' : 'debug_collection_config_callback_pb2'
    # @@protoc_insertion_point(class_scope:collection_config.DebugCollectionConfigCallbackRequest.TargetsLog)
    })
  ,
  'DESCRIPTOR' : _DEBUGCOLLECTIONCONFIGCALLBACKREQUEST,
  '__module__' : 'debug_collection_config_callback_pb2'
  # @@protoc_insertion_point(class_scope:collection_config.DebugCollectionConfigCallbackRequest)
  })
_sym_db.RegisterMessage(DebugCollectionConfigCallbackRequest)
_sym_db.RegisterMessage(DebugCollectionConfigCallbackRequest.TargetsLog)

DebugCollectionConfigCallbackResponse = _reflection.GeneratedProtocolMessageType('DebugCollectionConfigCallbackResponse', (_message.Message,), {
  'DESCRIPTOR' : _DEBUGCOLLECTIONCONFIGCALLBACKRESPONSE,
  '__module__' : 'debug_collection_config_callback_pb2'
  # @@protoc_insertion_point(class_scope:collection_config.DebugCollectionConfigCallbackResponse)
  })
_sym_db.RegisterMessage(DebugCollectionConfigCallbackResponse)

DebugCollectionConfigCallbackResponseWrapper = _reflection.GeneratedProtocolMessageType('DebugCollectionConfigCallbackResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _DEBUGCOLLECTIONCONFIGCALLBACKRESPONSEWRAPPER,
  '__module__' : 'debug_collection_config_callback_pb2'
  # @@protoc_insertion_point(class_scope:collection_config.DebugCollectionConfigCallbackResponseWrapper)
  })
_sym_db.RegisterMessage(DebugCollectionConfigCallbackResponseWrapper)


# @@protoc_insertion_point(module_scope)