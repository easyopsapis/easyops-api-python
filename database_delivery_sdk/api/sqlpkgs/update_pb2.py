# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: update.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from model.database_delivery import sql_package_version_pb2 as model_dot_database__delivery_dot_sql__package__version__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='update.proto',
  package='sqlpkgs',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0cupdate.proto\x12\x07sqlpkgs\x1a\x31model/database_delivery/sql_package_version.proto\"\xaf\x01\n\x17UpdateSQLPackageRequest\x12\r\n\x05pkgId\x18\x01 \x01(\t\x12\x43\n\x0cupdateSqlpkg\x18\x02 \x01(\x0b\x32-.sqlpkgs.UpdateSQLPackageRequest.UpdateSqlpkg\x1a@\n\x0cUpdateSqlpkg\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04memo\x18\x02 \x01(\t\x12\x14\n\x0c\x61ppPackageId\x18\x03 \x01(\t\"\xe9\x01\n\x18UpdateSQLPackageResponse\x12\x39\n\x0bversionList\x18\x01 \x03(\x0b\x32$.database_delivery.SQLPackageVersion\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0e\n\x06\x64\x62Type\x18\x04 \x01(\t\x12\x0c\n\x04memo\x18\x05 \x01(\t\x12\x0f\n\x07\x63reator\x18\x06 \x01(\t\x12\r\n\x05\x63time\x18\x07 \x01(\x03\x12\r\n\x05mtime\x18\x08 \x01(\x03\x12\x14\n\x0c\x61ppPackageId\x18\t \x01(\t\x12\x15\n\rrepoPackageId\x18\n \x01(\t\"\x84\x01\n\x1fUpdateSQLPackageResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12/\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32!.sqlpkgs.UpdateSQLPackageResponseb\x06proto3')
  ,
  dependencies=[model_dot_database__delivery_dot_sql__package__version__pb2.DESCRIPTOR,])




_UPDATESQLPACKAGEREQUEST_UPDATESQLPKG = _descriptor.Descriptor(
  name='UpdateSqlpkg',
  full_name='sqlpkgs.UpdateSQLPackageRequest.UpdateSqlpkg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='sqlpkgs.UpdateSQLPackageRequest.UpdateSqlpkg.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='sqlpkgs.UpdateSQLPackageRequest.UpdateSqlpkg.memo', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='appPackageId', full_name='sqlpkgs.UpdateSQLPackageRequest.UpdateSqlpkg.appPackageId', index=2,
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
  serialized_start=188,
  serialized_end=252,
)

_UPDATESQLPACKAGEREQUEST = _descriptor.Descriptor(
  name='UpdateSQLPackageRequest',
  full_name='sqlpkgs.UpdateSQLPackageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pkgId', full_name='sqlpkgs.UpdateSQLPackageRequest.pkgId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updateSqlpkg', full_name='sqlpkgs.UpdateSQLPackageRequest.updateSqlpkg', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_UPDATESQLPACKAGEREQUEST_UPDATESQLPKG, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=77,
  serialized_end=252,
)


_UPDATESQLPACKAGERESPONSE = _descriptor.Descriptor(
  name='UpdateSQLPackageResponse',
  full_name='sqlpkgs.UpdateSQLPackageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='versionList', full_name='sqlpkgs.UpdateSQLPackageResponse.versionList', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='sqlpkgs.UpdateSQLPackageResponse.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='sqlpkgs.UpdateSQLPackageResponse.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dbType', full_name='sqlpkgs.UpdateSQLPackageResponse.dbType', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='sqlpkgs.UpdateSQLPackageResponse.memo', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='sqlpkgs.UpdateSQLPackageResponse.creator', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='sqlpkgs.UpdateSQLPackageResponse.ctime', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='sqlpkgs.UpdateSQLPackageResponse.mtime', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='appPackageId', full_name='sqlpkgs.UpdateSQLPackageResponse.appPackageId', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repoPackageId', full_name='sqlpkgs.UpdateSQLPackageResponse.repoPackageId', index=9,
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
  serialized_start=255,
  serialized_end=488,
)


_UPDATESQLPACKAGERESPONSEWRAPPER = _descriptor.Descriptor(
  name='UpdateSQLPackageResponseWrapper',
  full_name='sqlpkgs.UpdateSQLPackageResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='sqlpkgs.UpdateSQLPackageResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='sqlpkgs.UpdateSQLPackageResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='sqlpkgs.UpdateSQLPackageResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='sqlpkgs.UpdateSQLPackageResponseWrapper.data', index=3,
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
  serialized_start=491,
  serialized_end=623,
)

_UPDATESQLPACKAGEREQUEST_UPDATESQLPKG.containing_type = _UPDATESQLPACKAGEREQUEST
_UPDATESQLPACKAGEREQUEST.fields_by_name['updateSqlpkg'].message_type = _UPDATESQLPACKAGEREQUEST_UPDATESQLPKG
_UPDATESQLPACKAGERESPONSE.fields_by_name['versionList'].message_type = model_dot_database__delivery_dot_sql__package__version__pb2._SQLPACKAGEVERSION
_UPDATESQLPACKAGERESPONSEWRAPPER.fields_by_name['data'].message_type = _UPDATESQLPACKAGERESPONSE
DESCRIPTOR.message_types_by_name['UpdateSQLPackageRequest'] = _UPDATESQLPACKAGEREQUEST
DESCRIPTOR.message_types_by_name['UpdateSQLPackageResponse'] = _UPDATESQLPACKAGERESPONSE
DESCRIPTOR.message_types_by_name['UpdateSQLPackageResponseWrapper'] = _UPDATESQLPACKAGERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateSQLPackageRequest = _reflection.GeneratedProtocolMessageType('UpdateSQLPackageRequest', (_message.Message,), dict(

  UpdateSqlpkg = _reflection.GeneratedProtocolMessageType('UpdateSqlpkg', (_message.Message,), dict(
    DESCRIPTOR = _UPDATESQLPACKAGEREQUEST_UPDATESQLPKG,
    __module__ = 'update_pb2'
    # @@protoc_insertion_point(class_scope:sqlpkgs.UpdateSQLPackageRequest.UpdateSqlpkg)
    ))
  ,
  DESCRIPTOR = _UPDATESQLPACKAGEREQUEST,
  __module__ = 'update_pb2'
  # @@protoc_insertion_point(class_scope:sqlpkgs.UpdateSQLPackageRequest)
  ))
_sym_db.RegisterMessage(UpdateSQLPackageRequest)
_sym_db.RegisterMessage(UpdateSQLPackageRequest.UpdateSqlpkg)

UpdateSQLPackageResponse = _reflection.GeneratedProtocolMessageType('UpdateSQLPackageResponse', (_message.Message,), dict(
  DESCRIPTOR = _UPDATESQLPACKAGERESPONSE,
  __module__ = 'update_pb2'
  # @@protoc_insertion_point(class_scope:sqlpkgs.UpdateSQLPackageResponse)
  ))
_sym_db.RegisterMessage(UpdateSQLPackageResponse)

UpdateSQLPackageResponseWrapper = _reflection.GeneratedProtocolMessageType('UpdateSQLPackageResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _UPDATESQLPACKAGERESPONSEWRAPPER,
  __module__ = 'update_pb2'
  # @@protoc_insertion_point(class_scope:sqlpkgs.UpdateSQLPackageResponseWrapper)
  ))
_sym_db.RegisterMessage(UpdateSQLPackageResponseWrapper)


# @@protoc_insertion_point(module_scope)
