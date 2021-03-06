# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: create_operation_log.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from notify_sdk.model.notify import operation_log_pb2 as notify__sdk_dot_model_dot_notify_dot_operation__log__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='create_operation_log.proto',
  package='oplog',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1a\x63reate_operation_log.proto\x12\x05oplog\x1a+notify_sdk/model/notify/operation_log.proto\".\n\x1a\x43reateOperationLogResponse\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\t\"\x86\x01\n!CreateOperationLogResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12/\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32!.oplog.CreateOperationLogResponseb\x06proto3')
  ,
  dependencies=[notify__sdk_dot_model_dot_notify_dot_operation__log__pb2.DESCRIPTOR,])




_CREATEOPERATIONLOGRESPONSE = _descriptor.Descriptor(
  name='CreateOperationLogResponse',
  full_name='oplog.CreateOperationLogResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_id', full_name='oplog.CreateOperationLogResponse.event_id', index=0,
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
  serialized_start=82,
  serialized_end=128,
)


_CREATEOPERATIONLOGRESPONSEWRAPPER = _descriptor.Descriptor(
  name='CreateOperationLogResponseWrapper',
  full_name='oplog.CreateOperationLogResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='oplog.CreateOperationLogResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='oplog.CreateOperationLogResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='oplog.CreateOperationLogResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='oplog.CreateOperationLogResponseWrapper.data', index=3,
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
  serialized_start=131,
  serialized_end=265,
)

_CREATEOPERATIONLOGRESPONSEWRAPPER.fields_by_name['data'].message_type = _CREATEOPERATIONLOGRESPONSE
DESCRIPTOR.message_types_by_name['CreateOperationLogResponse'] = _CREATEOPERATIONLOGRESPONSE
DESCRIPTOR.message_types_by_name['CreateOperationLogResponseWrapper'] = _CREATEOPERATIONLOGRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateOperationLogResponse = _reflection.GeneratedProtocolMessageType('CreateOperationLogResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEOPERATIONLOGRESPONSE,
  '__module__' : 'create_operation_log_pb2'
  # @@protoc_insertion_point(class_scope:oplog.CreateOperationLogResponse)
  })
_sym_db.RegisterMessage(CreateOperationLogResponse)

CreateOperationLogResponseWrapper = _reflection.GeneratedProtocolMessageType('CreateOperationLogResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _CREATEOPERATIONLOGRESPONSEWRAPPER,
  '__module__' : 'create_operation_log_pb2'
  # @@protoc_insertion_point(class_scope:oplog.CreateOperationLogResponseWrapper)
  })
_sym_db.RegisterMessage(CreateOperationLogResponseWrapper)


# @@protoc_insertion_point(module_scope)
