# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sqlpkg_dbtask_history.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sqlpkg_dbtask_history.proto',
  package='database_delivery',
  syntax='proto3',
  serialized_options=_b('ZKgo.easyops.local/contracts/protorepo-models/easyops/model/database_delivery'),
  serialized_pb=_b('\n\x1bsqlpkg_dbtask_history.proto\x12\x11\x64\x61tabase_delivery\"\xe9\x04\n\x1dSQLPackageDBTaskChangeHistory\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05state\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x62ServiceId\x18\x04 \x01(\t\x12\r\n\x05\x63time\x18\x05 \x01(\x03\x12\r\n\x05mtime\x18\x06 \x01(\x03\x12S\n\x0c\x62\x61\x63kupResult\x18\x07 \x01(\x0b\x32=.database_delivery.SQLPackageDBTaskChangeHistory.BackupResult\x12Q\n\x0b\x63heckResult\x18\x08 \x01(\x0b\x32<.database_delivery.SQLPackageDBTaskChangeHistory.CheckResult\x12_\n\x12sqlpkgChangeResult\x18\t \x01(\x0b\x32\x43.database_delivery.SQLPackageDBTaskChangeHistory.SqlpkgChangeResult\x1aV\n\x0c\x42\x61\x63kupResult\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0e\n\x06hostId\x18\x02 \x01(\t\x12\x0e\n\x06hostIp\x18\x03 \x01(\t\x12\x16\n\x0escriptNameList\x18\x04 \x03(\t\x1aG\n\x0b\x43heckResult\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x12\n\nupdatedNum\x18\x02 \x01(\x05\x12\x14\n\x0cunUpdatedNum\x18\x03 \x01(\x05\x1a@\n\x12SqlpkgChangeResult\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x1a\n\x12\x64\x62InstanceNameList\x18\x02 \x03(\tBMZKgo.easyops.local/contracts/protorepo-models/easyops/model/database_deliveryb\x06proto3')
)




_SQLPACKAGEDBTASKCHANGEHISTORY_BACKUPRESULT = _descriptor.Descriptor(
  name='BackupResult',
  full_name='database_delivery.SQLPackageDBTaskChangeHistory.BackupResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='database_delivery.SQLPackageDBTaskChangeHistory.BackupResult.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hostId', full_name='database_delivery.SQLPackageDBTaskChangeHistory.BackupResult.hostId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hostIp', full_name='database_delivery.SQLPackageDBTaskChangeHistory.BackupResult.hostIp', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scriptNameList', full_name='database_delivery.SQLPackageDBTaskChangeHistory.BackupResult.scriptNameList', index=3,
      number=4, type=9, cpp_type=9, label=3,
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
  serialized_start=443,
  serialized_end=529,
)

_SQLPACKAGEDBTASKCHANGEHISTORY_CHECKRESULT = _descriptor.Descriptor(
  name='CheckResult',
  full_name='database_delivery.SQLPackageDBTaskChangeHistory.CheckResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='database_delivery.SQLPackageDBTaskChangeHistory.CheckResult.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updatedNum', full_name='database_delivery.SQLPackageDBTaskChangeHistory.CheckResult.updatedNum', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unUpdatedNum', full_name='database_delivery.SQLPackageDBTaskChangeHistory.CheckResult.unUpdatedNum', index=2,
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
  serialized_start=531,
  serialized_end=602,
)

_SQLPACKAGEDBTASKCHANGEHISTORY_SQLPKGCHANGERESULT = _descriptor.Descriptor(
  name='SqlpkgChangeResult',
  full_name='database_delivery.SQLPackageDBTaskChangeHistory.SqlpkgChangeResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='database_delivery.SQLPackageDBTaskChangeHistory.SqlpkgChangeResult.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dbInstanceNameList', full_name='database_delivery.SQLPackageDBTaskChangeHistory.SqlpkgChangeResult.dbInstanceNameList', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=604,
  serialized_end=668,
)

_SQLPACKAGEDBTASKCHANGEHISTORY = _descriptor.Descriptor(
  name='SQLPackageDBTaskChangeHistory',
  full_name='database_delivery.SQLPackageDBTaskChangeHistory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='database_delivery.SQLPackageDBTaskChangeHistory.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='database_delivery.SQLPackageDBTaskChangeHistory.state', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='database_delivery.SQLPackageDBTaskChangeHistory.status', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dbServiceId', full_name='database_delivery.SQLPackageDBTaskChangeHistory.dbServiceId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='database_delivery.SQLPackageDBTaskChangeHistory.ctime', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='database_delivery.SQLPackageDBTaskChangeHistory.mtime', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='backupResult', full_name='database_delivery.SQLPackageDBTaskChangeHistory.backupResult', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checkResult', full_name='database_delivery.SQLPackageDBTaskChangeHistory.checkResult', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sqlpkgChangeResult', full_name='database_delivery.SQLPackageDBTaskChangeHistory.sqlpkgChangeResult', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SQLPACKAGEDBTASKCHANGEHISTORY_BACKUPRESULT, _SQLPACKAGEDBTASKCHANGEHISTORY_CHECKRESULT, _SQLPACKAGEDBTASKCHANGEHISTORY_SQLPKGCHANGERESULT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=668,
)

_SQLPACKAGEDBTASKCHANGEHISTORY_BACKUPRESULT.containing_type = _SQLPACKAGEDBTASKCHANGEHISTORY
_SQLPACKAGEDBTASKCHANGEHISTORY_CHECKRESULT.containing_type = _SQLPACKAGEDBTASKCHANGEHISTORY
_SQLPACKAGEDBTASKCHANGEHISTORY_SQLPKGCHANGERESULT.containing_type = _SQLPACKAGEDBTASKCHANGEHISTORY
_SQLPACKAGEDBTASKCHANGEHISTORY.fields_by_name['backupResult'].message_type = _SQLPACKAGEDBTASKCHANGEHISTORY_BACKUPRESULT
_SQLPACKAGEDBTASKCHANGEHISTORY.fields_by_name['checkResult'].message_type = _SQLPACKAGEDBTASKCHANGEHISTORY_CHECKRESULT
_SQLPACKAGEDBTASKCHANGEHISTORY.fields_by_name['sqlpkgChangeResult'].message_type = _SQLPACKAGEDBTASKCHANGEHISTORY_SQLPKGCHANGERESULT
DESCRIPTOR.message_types_by_name['SQLPackageDBTaskChangeHistory'] = _SQLPACKAGEDBTASKCHANGEHISTORY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SQLPackageDBTaskChangeHistory = _reflection.GeneratedProtocolMessageType('SQLPackageDBTaskChangeHistory', (_message.Message,), {

  'BackupResult' : _reflection.GeneratedProtocolMessageType('BackupResult', (_message.Message,), {
    'DESCRIPTOR' : _SQLPACKAGEDBTASKCHANGEHISTORY_BACKUPRESULT,
    '__module__' : 'sqlpkg_dbtask_history_pb2'
    # @@protoc_insertion_point(class_scope:database_delivery.SQLPackageDBTaskChangeHistory.BackupResult)
    })
  ,

  'CheckResult' : _reflection.GeneratedProtocolMessageType('CheckResult', (_message.Message,), {
    'DESCRIPTOR' : _SQLPACKAGEDBTASKCHANGEHISTORY_CHECKRESULT,
    '__module__' : 'sqlpkg_dbtask_history_pb2'
    # @@protoc_insertion_point(class_scope:database_delivery.SQLPackageDBTaskChangeHistory.CheckResult)
    })
  ,

  'SqlpkgChangeResult' : _reflection.GeneratedProtocolMessageType('SqlpkgChangeResult', (_message.Message,), {
    'DESCRIPTOR' : _SQLPACKAGEDBTASKCHANGEHISTORY_SQLPKGCHANGERESULT,
    '__module__' : 'sqlpkg_dbtask_history_pb2'
    # @@protoc_insertion_point(class_scope:database_delivery.SQLPackageDBTaskChangeHistory.SqlpkgChangeResult)
    })
  ,
  'DESCRIPTOR' : _SQLPACKAGEDBTASKCHANGEHISTORY,
  '__module__' : 'sqlpkg_dbtask_history_pb2'
  # @@protoc_insertion_point(class_scope:database_delivery.SQLPackageDBTaskChangeHistory)
  })
_sym_db.RegisterMessage(SQLPackageDBTaskChangeHistory)
_sym_db.RegisterMessage(SQLPackageDBTaskChangeHistory.BackupResult)
_sym_db.RegisterMessage(SQLPackageDBTaskChangeHistory.CheckResult)
_sym_db.RegisterMessage(SQLPackageDBTaskChangeHistory.SqlpkgChangeResult)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
