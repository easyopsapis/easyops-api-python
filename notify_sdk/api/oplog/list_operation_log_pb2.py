# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list_operation_log.proto

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
  name='list_operation_log.proto',
  package='oplog',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x18list_operation_log.proto\x12\x05oplog\x1a+notify_sdk/model/notify/operation_log.proto\"n\n\x18ListOperationLogResponse\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12\"\n\x04list\x18\x04 \x03(\x0b\x32\x14.notify.OperationLog\"\x82\x01\n\x1fListOperationLogResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12-\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1f.oplog.ListOperationLogResponseb\x06proto3')
  ,
  dependencies=[notify__sdk_dot_model_dot_notify_dot_operation__log__pb2.DESCRIPTOR,])




_LISTOPERATIONLOGRESPONSE = _descriptor.Descriptor(
  name='ListOperationLogResponse',
  full_name='oplog.ListOperationLogResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='oplog.ListOperationLogResponse.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='oplog.ListOperationLogResponse.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='oplog.ListOperationLogResponse.total', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='oplog.ListOperationLogResponse.list', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=80,
  serialized_end=190,
)


_LISTOPERATIONLOGRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListOperationLogResponseWrapper',
  full_name='oplog.ListOperationLogResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='oplog.ListOperationLogResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='oplog.ListOperationLogResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='oplog.ListOperationLogResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='oplog.ListOperationLogResponseWrapper.data', index=3,
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
  serialized_start=193,
  serialized_end=323,
)

_LISTOPERATIONLOGRESPONSE.fields_by_name['list'].message_type = notify__sdk_dot_model_dot_notify_dot_operation__log__pb2._OPERATIONLOG
_LISTOPERATIONLOGRESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTOPERATIONLOGRESPONSE
DESCRIPTOR.message_types_by_name['ListOperationLogResponse'] = _LISTOPERATIONLOGRESPONSE
DESCRIPTOR.message_types_by_name['ListOperationLogResponseWrapper'] = _LISTOPERATIONLOGRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListOperationLogResponse = _reflection.GeneratedProtocolMessageType('ListOperationLogResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTOPERATIONLOGRESPONSE,
  '__module__' : 'list_operation_log_pb2'
  # @@protoc_insertion_point(class_scope:oplog.ListOperationLogResponse)
  })
_sym_db.RegisterMessage(ListOperationLogResponse)

ListOperationLogResponseWrapper = _reflection.GeneratedProtocolMessageType('ListOperationLogResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _LISTOPERATIONLOGRESPONSEWRAPPER,
  '__module__' : 'list_operation_log_pb2'
  # @@protoc_insertion_point(class_scope:oplog.ListOperationLogResponseWrapper)
  })
_sym_db.RegisterMessage(ListOperationLogResponseWrapper)


# @@protoc_insertion_point(module_scope)
