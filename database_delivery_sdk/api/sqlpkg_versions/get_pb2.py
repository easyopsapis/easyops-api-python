# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='get.proto',
  package='sqlpkg_versions',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\tget.proto\x12\x0fsqlpkg_versions\"?\n\x1bGetSQLPackageVersionRequest\x12\r\n\x05pkgId\x18\x01 \x01(\t\x12\x11\n\tversionId\x18\x02 \x01(\t\"\xf2\x02\n\x1cGetSQLPackageVersionResponse\x12L\n\nsqlPackage\x18\x01 \x01(\x0b\x32\x38.sqlpkg_versions.GetSQLPackageVersionResponse.SqlPackage\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x15\n\rrepoVersionId\x18\x04 \x01(\t\x12\x14\n\x0c\x61ppVersionId\x18\x05 \x01(\t\x12\x13\n\x0bversionName\x18\x06 \x01(\t\x12\x0c\n\x04memo\x18\x07 \x01(\t\x12\x0f\n\x07\x63reator\x18\x08 \x01(\t\x12\r\n\x05\x63time\x18\t \x01(\x03\x12\r\n\x05mtime\x18\n \x01(\x03\x1ak\n\nSqlPackage\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04memo\x18\x03 \x01(\t\x12\x15\n\rrepoPackageId\x18\x04 \x01(\t\x12\x0f\n\x07\x63reator\x18\x05 \x01(\t\x12\r\n\x05mtime\x18\x06 \x01(\x03\"\x94\x01\n#GetSQLPackageVersionResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12;\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32-.sqlpkg_versions.GetSQLPackageVersionResponseb\x06proto3')
)




_GETSQLPACKAGEVERSIONREQUEST = _descriptor.Descriptor(
  name='GetSQLPackageVersionRequest',
  full_name='sqlpkg_versions.GetSQLPackageVersionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pkgId', full_name='sqlpkg_versions.GetSQLPackageVersionRequest.pkgId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionId', full_name='sqlpkg_versions.GetSQLPackageVersionRequest.versionId', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=30,
  serialized_end=93,
)


_GETSQLPACKAGEVERSIONRESPONSE_SQLPACKAGE = _descriptor.Descriptor(
  name='SqlPackage',
  full_name='sqlpkg_versions.GetSQLPackageVersionResponse.SqlPackage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='sqlpkg_versions.GetSQLPackageVersionResponse.SqlPackage.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='sqlpkg_versions.GetSQLPackageVersionResponse.SqlPackage.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='sqlpkg_versions.GetSQLPackageVersionResponse.SqlPackage.memo', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repoPackageId', full_name='sqlpkg_versions.GetSQLPackageVersionResponse.SqlPackage.repoPackageId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='sqlpkg_versions.GetSQLPackageVersionResponse.SqlPackage.creator', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='sqlpkg_versions.GetSQLPackageVersionResponse.SqlPackage.mtime', index=5,
      number=6, type=3, cpp_type=2, label=1,
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
  serialized_start=359,
  serialized_end=466,
)

_GETSQLPACKAGEVERSIONRESPONSE = _descriptor.Descriptor(
  name='GetSQLPackageVersionResponse',
  full_name='sqlpkg_versions.GetSQLPackageVersionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sqlPackage', full_name='sqlpkg_versions.GetSQLPackageVersionResponse.sqlPackage', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='sqlpkg_versions.GetSQLPackageVersionResponse.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='sqlpkg_versions.GetSQLPackageVersionResponse.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repoVersionId', full_name='sqlpkg_versions.GetSQLPackageVersionResponse.repoVersionId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='appVersionId', full_name='sqlpkg_versions.GetSQLPackageVersionResponse.appVersionId', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionName', full_name='sqlpkg_versions.GetSQLPackageVersionResponse.versionName', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='sqlpkg_versions.GetSQLPackageVersionResponse.memo', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='sqlpkg_versions.GetSQLPackageVersionResponse.creator', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='sqlpkg_versions.GetSQLPackageVersionResponse.ctime', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='sqlpkg_versions.GetSQLPackageVersionResponse.mtime', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETSQLPACKAGEVERSIONRESPONSE_SQLPACKAGE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=96,
  serialized_end=466,
)


_GETSQLPACKAGEVERSIONRESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetSQLPackageVersionResponseWrapper',
  full_name='sqlpkg_versions.GetSQLPackageVersionResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='sqlpkg_versions.GetSQLPackageVersionResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='sqlpkg_versions.GetSQLPackageVersionResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='sqlpkg_versions.GetSQLPackageVersionResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='sqlpkg_versions.GetSQLPackageVersionResponseWrapper.data', index=3,
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
  serialized_start=469,
  serialized_end=617,
)

_GETSQLPACKAGEVERSIONRESPONSE_SQLPACKAGE.containing_type = _GETSQLPACKAGEVERSIONRESPONSE
_GETSQLPACKAGEVERSIONRESPONSE.fields_by_name['sqlPackage'].message_type = _GETSQLPACKAGEVERSIONRESPONSE_SQLPACKAGE
_GETSQLPACKAGEVERSIONRESPONSEWRAPPER.fields_by_name['data'].message_type = _GETSQLPACKAGEVERSIONRESPONSE
DESCRIPTOR.message_types_by_name['GetSQLPackageVersionRequest'] = _GETSQLPACKAGEVERSIONREQUEST
DESCRIPTOR.message_types_by_name['GetSQLPackageVersionResponse'] = _GETSQLPACKAGEVERSIONRESPONSE
DESCRIPTOR.message_types_by_name['GetSQLPackageVersionResponseWrapper'] = _GETSQLPACKAGEVERSIONRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetSQLPackageVersionRequest = _reflection.GeneratedProtocolMessageType('GetSQLPackageVersionRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETSQLPACKAGEVERSIONREQUEST,
  __module__ = 'get_pb2'
  # @@protoc_insertion_point(class_scope:sqlpkg_versions.GetSQLPackageVersionRequest)
  ))
_sym_db.RegisterMessage(GetSQLPackageVersionRequest)

GetSQLPackageVersionResponse = _reflection.GeneratedProtocolMessageType('GetSQLPackageVersionResponse', (_message.Message,), dict(

  SqlPackage = _reflection.GeneratedProtocolMessageType('SqlPackage', (_message.Message,), dict(
    DESCRIPTOR = _GETSQLPACKAGEVERSIONRESPONSE_SQLPACKAGE,
    __module__ = 'get_pb2'
    # @@protoc_insertion_point(class_scope:sqlpkg_versions.GetSQLPackageVersionResponse.SqlPackage)
    ))
  ,
  DESCRIPTOR = _GETSQLPACKAGEVERSIONRESPONSE,
  __module__ = 'get_pb2'
  # @@protoc_insertion_point(class_scope:sqlpkg_versions.GetSQLPackageVersionResponse)
  ))
_sym_db.RegisterMessage(GetSQLPackageVersionResponse)
_sym_db.RegisterMessage(GetSQLPackageVersionResponse.SqlPackage)

GetSQLPackageVersionResponseWrapper = _reflection.GeneratedProtocolMessageType('GetSQLPackageVersionResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _GETSQLPACKAGEVERSIONRESPONSEWRAPPER,
  __module__ = 'get_pb2'
  # @@protoc_insertion_point(class_scope:sqlpkg_versions.GetSQLPackageVersionResponseWrapper)
  ))
_sym_db.RegisterMessage(GetSQLPackageVersionResponseWrapper)


# @@protoc_insertion_point(module_scope)
