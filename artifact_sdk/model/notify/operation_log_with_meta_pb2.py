# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: operation_log_with_meta.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from artifact_sdk.model.notify import operation_log_pb2 as artifact__sdk_dot_model_dot_notify_dot_operation__log__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='operation_log_with_meta.proto',
  package='notify',
  syntax='proto3',
  serialized_options=_b('Z@go.easyops.local/contracts/protorepo-models/easyops/model/notify'),
  serialized_pb=_b('\n\x1doperation_log_with_meta.proto\x12\x06notify\x1a-artifact_sdk/model/notify/operation_log.proto\"Y\n\x14OperationLogWithMeta\x12\x0e\n\x06system\x18\x01 \x01(\t\x12\r\n\x05topic\x18\x02 \x01(\t\x12\"\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x14.notify.OperationLogBBZ@go.easyops.local/contracts/protorepo-models/easyops/model/notifyb\x06proto3')
  ,
  dependencies=[artifact__sdk_dot_model_dot_notify_dot_operation__log__pb2.DESCRIPTOR,])




_OPERATIONLOGWITHMETA = _descriptor.Descriptor(
  name='OperationLogWithMeta',
  full_name='notify.OperationLogWithMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='system', full_name='notify.OperationLogWithMeta.system', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='topic', full_name='notify.OperationLogWithMeta.topic', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='notify.OperationLogWithMeta.data', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=88,
  serialized_end=177,
)

_OPERATIONLOGWITHMETA.fields_by_name['data'].message_type = artifact__sdk_dot_model_dot_notify_dot_operation__log__pb2._OPERATIONLOG
DESCRIPTOR.message_types_by_name['OperationLogWithMeta'] = _OPERATIONLOGWITHMETA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OperationLogWithMeta = _reflection.GeneratedProtocolMessageType('OperationLogWithMeta', (_message.Message,), {
  'DESCRIPTOR' : _OPERATIONLOGWITHMETA,
  '__module__' : 'operation_log_with_meta_pb2'
  # @@protoc_insertion_point(class_scope:notify.OperationLogWithMeta)
  })
_sym_db.RegisterMessage(OperationLogWithMeta)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
