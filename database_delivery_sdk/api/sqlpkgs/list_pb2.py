# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from database_delivery_sdk.model.database_delivery import sql_package_version_pb2 as database__delivery__sdk_dot_model_dot_database__delivery_dot_sql__package__version__pb2
from database_delivery_sdk.model.database_delivery import app_pb2 as database__delivery__sdk_dot_model_dot_database__delivery_dot_app__pb2
from database_delivery_sdk.model.database_delivery import dbservice_pb2 as database__delivery__sdk_dot_model_dot_database__delivery_dot_dbservice__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='list.proto',
  package='sqlpkgs',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\nlist.proto\x12\x07sqlpkgs\x1aGdatabase_delivery_sdk/model/database_delivery/sql_package_version.proto\x1a\x37\x64\x61tabase_delivery_sdk/model/database_delivery/app.proto\x1a=database_delivery_sdk/model/database_delivery/dbservice.proto\"[\n\x15ListSQLPackageRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x10\n\x08pageSize\x18\x02 \x01(\x05\x12\r\n\x05\x61ppId\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x62ServiceId\x18\x04 \x01(\t\"\x8c\x03\n\x16ListSQLPackageResponse\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12\x32\n\x04list\x18\x04 \x03(\x0b\x32$.sqlpkgs.ListSQLPackageResponse.List\x1a\x8d\x02\n\x04List\x12\x39\n\x0bversionList\x18\x01 \x03(\x0b\x32$.database_delivery.SQLPackageVersion\x12+\n\x03\x41PP\x18\x02 \x03(\x0b\x32\x1e.database_delivery.Application\x12/\n\tDBSERVICE\x18\x03 \x03(\x0b\x32\x1c.database_delivery.DBService\x12\n\n\x02id\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x0c\n\x04memo\x18\x06 \x01(\t\x12\x0f\n\x07\x63reator\x18\x07 \x01(\t\x12\r\n\x05\x63time\x18\x08 \x01(\x03\x12\r\n\x05mtime\x18\t \x01(\x03\x12\x15\n\rrepoPackageId\x18\n \x01(\t\"\x80\x01\n\x1dListSQLPackageResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12-\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1f.sqlpkgs.ListSQLPackageResponseb\x06proto3')
  ,
  dependencies=[database__delivery__sdk_dot_model_dot_database__delivery_dot_sql__package__version__pb2.DESCRIPTOR,database__delivery__sdk_dot_model_dot_database__delivery_dot_app__pb2.DESCRIPTOR,database__delivery__sdk_dot_model_dot_database__delivery_dot_dbservice__pb2.DESCRIPTOR,])




_LISTSQLPACKAGEREQUEST = _descriptor.Descriptor(
  name='ListSQLPackageRequest',
  full_name='sqlpkgs.ListSQLPackageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='sqlpkgs.ListSQLPackageRequest.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='sqlpkgs.ListSQLPackageRequest.pageSize', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='appId', full_name='sqlpkgs.ListSQLPackageRequest.appId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dbServiceId', full_name='sqlpkgs.ListSQLPackageRequest.dbServiceId', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=216,
  serialized_end=307,
)


_LISTSQLPACKAGERESPONSE_LIST = _descriptor.Descriptor(
  name='List',
  full_name='sqlpkgs.ListSQLPackageResponse.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='versionList', full_name='sqlpkgs.ListSQLPackageResponse.List.versionList', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='APP', full_name='sqlpkgs.ListSQLPackageResponse.List.APP', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='DBSERVICE', full_name='sqlpkgs.ListSQLPackageResponse.List.DBSERVICE', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='sqlpkgs.ListSQLPackageResponse.List.id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='sqlpkgs.ListSQLPackageResponse.List.name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='sqlpkgs.ListSQLPackageResponse.List.memo', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='sqlpkgs.ListSQLPackageResponse.List.creator', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='sqlpkgs.ListSQLPackageResponse.List.ctime', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='sqlpkgs.ListSQLPackageResponse.List.mtime', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repoPackageId', full_name='sqlpkgs.ListSQLPackageResponse.List.repoPackageId', index=9,
      number=10, type=9, cpp_type=9, label=1,
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
  serialized_start=437,
  serialized_end=706,
)

_LISTSQLPACKAGERESPONSE = _descriptor.Descriptor(
  name='ListSQLPackageResponse',
  full_name='sqlpkgs.ListSQLPackageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='sqlpkgs.ListSQLPackageResponse.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='sqlpkgs.ListSQLPackageResponse.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='sqlpkgs.ListSQLPackageResponse.total', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='sqlpkgs.ListSQLPackageResponse.list', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTSQLPACKAGERESPONSE_LIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=310,
  serialized_end=706,
)


_LISTSQLPACKAGERESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListSQLPackageResponseWrapper',
  full_name='sqlpkgs.ListSQLPackageResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='sqlpkgs.ListSQLPackageResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='sqlpkgs.ListSQLPackageResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='sqlpkgs.ListSQLPackageResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='sqlpkgs.ListSQLPackageResponseWrapper.data', index=3,
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
  serialized_start=709,
  serialized_end=837,
)

_LISTSQLPACKAGERESPONSE_LIST.fields_by_name['versionList'].message_type = database__delivery__sdk_dot_model_dot_database__delivery_dot_sql__package__version__pb2._SQLPACKAGEVERSION
_LISTSQLPACKAGERESPONSE_LIST.fields_by_name['APP'].message_type = database__delivery__sdk_dot_model_dot_database__delivery_dot_app__pb2._APPLICATION
_LISTSQLPACKAGERESPONSE_LIST.fields_by_name['DBSERVICE'].message_type = database__delivery__sdk_dot_model_dot_database__delivery_dot_dbservice__pb2._DBSERVICE
_LISTSQLPACKAGERESPONSE_LIST.containing_type = _LISTSQLPACKAGERESPONSE
_LISTSQLPACKAGERESPONSE.fields_by_name['list'].message_type = _LISTSQLPACKAGERESPONSE_LIST
_LISTSQLPACKAGERESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTSQLPACKAGERESPONSE
DESCRIPTOR.message_types_by_name['ListSQLPackageRequest'] = _LISTSQLPACKAGEREQUEST
DESCRIPTOR.message_types_by_name['ListSQLPackageResponse'] = _LISTSQLPACKAGERESPONSE
DESCRIPTOR.message_types_by_name['ListSQLPackageResponseWrapper'] = _LISTSQLPACKAGERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListSQLPackageRequest = _reflection.GeneratedProtocolMessageType('ListSQLPackageRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTSQLPACKAGEREQUEST,
  '__module__' : 'list_pb2'
  # @@protoc_insertion_point(class_scope:sqlpkgs.ListSQLPackageRequest)
  })
_sym_db.RegisterMessage(ListSQLPackageRequest)

ListSQLPackageResponse = _reflection.GeneratedProtocolMessageType('ListSQLPackageResponse', (_message.Message,), {

  'List' : _reflection.GeneratedProtocolMessageType('List', (_message.Message,), {
    'DESCRIPTOR' : _LISTSQLPACKAGERESPONSE_LIST,
    '__module__' : 'list_pb2'
    # @@protoc_insertion_point(class_scope:sqlpkgs.ListSQLPackageResponse.List)
    })
  ,
  'DESCRIPTOR' : _LISTSQLPACKAGERESPONSE,
  '__module__' : 'list_pb2'
  # @@protoc_insertion_point(class_scope:sqlpkgs.ListSQLPackageResponse)
  })
_sym_db.RegisterMessage(ListSQLPackageResponse)
_sym_db.RegisterMessage(ListSQLPackageResponse.List)

ListSQLPackageResponseWrapper = _reflection.GeneratedProtocolMessageType('ListSQLPackageResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _LISTSQLPACKAGERESPONSEWRAPPER,
  '__module__' : 'list_pb2'
  # @@protoc_insertion_point(class_scope:sqlpkgs.ListSQLPackageResponseWrapper)
  })
_sym_db.RegisterMessage(ListSQLPackageResponseWrapper)


# @@protoc_insertion_point(module_scope)
