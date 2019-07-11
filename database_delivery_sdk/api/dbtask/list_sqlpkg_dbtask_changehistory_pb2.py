# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list_sqlpkg_dbtask_changehistory.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from model.database_delivery import sqlpkg_dbtask_history_pb2 as model_dot_database__delivery_dot_sqlpkg__dbtask__history__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='list_sqlpkg_dbtask_changehistory.proto',
  package='dbtask',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n&list_sqlpkg_dbtask_changehistory.proto\x12\x06\x64\x62task\x1a\x33model/database_delivery/sqlpkg_dbtask_history.proto\"_\n(ListSQLPackageDBTaskChangeHistoryRequest\x12\x13\n\x0b\x64\x62ServiceId\x18\x01 \x01(\t\x12\x0c\n\x04page\x18\x02 \x01(\x05\x12\x10\n\x08pageSize\x18\x03 \x01(\x05\"\x9b\x01\n)ListSQLPackageDBTaskChangeHistoryResponse\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12>\n\x04list\x18\x04 \x03(\x0b\x32\x30.database_delivery.SQLPackageDBTaskChangeHistory\"\xa5\x01\n0ListSQLPackageDBTaskChangeHistoryResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12?\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x31.dbtask.ListSQLPackageDBTaskChangeHistoryResponseb\x06proto3')
  ,
  dependencies=[model_dot_database__delivery_dot_sqlpkg__dbtask__history__pb2.DESCRIPTOR,])




_LISTSQLPACKAGEDBTASKCHANGEHISTORYREQUEST = _descriptor.Descriptor(
  name='ListSQLPackageDBTaskChangeHistoryRequest',
  full_name='dbtask.ListSQLPackageDBTaskChangeHistoryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dbServiceId', full_name='dbtask.ListSQLPackageDBTaskChangeHistoryRequest.dbServiceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page', full_name='dbtask.ListSQLPackageDBTaskChangeHistoryRequest.page', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='dbtask.ListSQLPackageDBTaskChangeHistoryRequest.pageSize', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=103,
  serialized_end=198,
)


_LISTSQLPACKAGEDBTASKCHANGEHISTORYRESPONSE = _descriptor.Descriptor(
  name='ListSQLPackageDBTaskChangeHistoryResponse',
  full_name='dbtask.ListSQLPackageDBTaskChangeHistoryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='dbtask.ListSQLPackageDBTaskChangeHistoryResponse.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='dbtask.ListSQLPackageDBTaskChangeHistoryResponse.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='dbtask.ListSQLPackageDBTaskChangeHistoryResponse.total', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='dbtask.ListSQLPackageDBTaskChangeHistoryResponse.list', index=3,
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
  serialized_start=201,
  serialized_end=356,
)


_LISTSQLPACKAGEDBTASKCHANGEHISTORYRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListSQLPackageDBTaskChangeHistoryResponseWrapper',
  full_name='dbtask.ListSQLPackageDBTaskChangeHistoryResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='dbtask.ListSQLPackageDBTaskChangeHistoryResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='dbtask.ListSQLPackageDBTaskChangeHistoryResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dbtask.ListSQLPackageDBTaskChangeHistoryResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='dbtask.ListSQLPackageDBTaskChangeHistoryResponseWrapper.data', index=3,
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
  serialized_start=359,
  serialized_end=524,
)

_LISTSQLPACKAGEDBTASKCHANGEHISTORYRESPONSE.fields_by_name['list'].message_type = model_dot_database__delivery_dot_sqlpkg__dbtask__history__pb2._SQLPACKAGEDBTASKCHANGEHISTORY
_LISTSQLPACKAGEDBTASKCHANGEHISTORYRESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTSQLPACKAGEDBTASKCHANGEHISTORYRESPONSE
DESCRIPTOR.message_types_by_name['ListSQLPackageDBTaskChangeHistoryRequest'] = _LISTSQLPACKAGEDBTASKCHANGEHISTORYREQUEST
DESCRIPTOR.message_types_by_name['ListSQLPackageDBTaskChangeHistoryResponse'] = _LISTSQLPACKAGEDBTASKCHANGEHISTORYRESPONSE
DESCRIPTOR.message_types_by_name['ListSQLPackageDBTaskChangeHistoryResponseWrapper'] = _LISTSQLPACKAGEDBTASKCHANGEHISTORYRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListSQLPackageDBTaskChangeHistoryRequest = _reflection.GeneratedProtocolMessageType('ListSQLPackageDBTaskChangeHistoryRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTSQLPACKAGEDBTASKCHANGEHISTORYREQUEST,
  __module__ = 'list_sqlpkg_dbtask_changehistory_pb2'
  # @@protoc_insertion_point(class_scope:dbtask.ListSQLPackageDBTaskChangeHistoryRequest)
  ))
_sym_db.RegisterMessage(ListSQLPackageDBTaskChangeHistoryRequest)

ListSQLPackageDBTaskChangeHistoryResponse = _reflection.GeneratedProtocolMessageType('ListSQLPackageDBTaskChangeHistoryResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTSQLPACKAGEDBTASKCHANGEHISTORYRESPONSE,
  __module__ = 'list_sqlpkg_dbtask_changehistory_pb2'
  # @@protoc_insertion_point(class_scope:dbtask.ListSQLPackageDBTaskChangeHistoryResponse)
  ))
_sym_db.RegisterMessage(ListSQLPackageDBTaskChangeHistoryResponse)

ListSQLPackageDBTaskChangeHistoryResponseWrapper = _reflection.GeneratedProtocolMessageType('ListSQLPackageDBTaskChangeHistoryResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _LISTSQLPACKAGEDBTASKCHANGEHISTORYRESPONSEWRAPPER,
  __module__ = 'list_sqlpkg_dbtask_changehistory_pb2'
  # @@protoc_insertion_point(class_scope:dbtask.ListSQLPackageDBTaskChangeHistoryResponseWrapper)
  ))
_sym_db.RegisterMessage(ListSQLPackageDBTaskChangeHistoryResponseWrapper)


# @@protoc_insertion_point(module_scope)