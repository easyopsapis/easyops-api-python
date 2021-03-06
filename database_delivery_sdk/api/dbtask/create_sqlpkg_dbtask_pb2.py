# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: create_sqlpkg_dbtask.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='create_sqlpkg_dbtask.proto',
  package='dbtask',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1a\x63reate_sqlpkg_dbtask.proto\x12\x06\x64\x62task\"\xe4\x07\n\x1d\x43reateSQLPackageDBTaskRequest\x12\r\n\x05pkgId\x18\x01 \x01(\t\x12\x11\n\tversionId\x18\x02 \x01(\t\x12@\n\x08taskInfo\x18\x03 \x01(\x0b\x32..dbtask.CreateSQLPackageDBTaskRequest.TaskInfo\x1a\xde\x06\n\x08TaskInfo\x12\x13\n\x0b\x64\x62ServiceId\x18\x01 \x01(\t\x12K\n\tbackupCfg\x18\x02 \x03(\x0b\x32\x38.dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.BackupCfg\x12K\n\tchangeCfg\x18\x03 \x03(\x0b\x32\x38.dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.ChangeCfg\x12I\n\x08\x63heckCfg\x18\x04 \x03(\x0b\x32\x37.dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.CheckCfg\x1a\xb8\x02\n\tBackupCfg\x12\x14\n\x0c\x64\x62InstanceId\x18\x01 \x01(\t\x12\x0e\n\x06hostId\x18\x02 \x01(\t\x12\x0e\n\x06hostIp\x18\x03 \x01(\t\x12Q\n\x07scripts\x18\x04 \x03(\x0b\x32@.dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.BackupCfg.Scripts\x1a\xa1\x01\n\x07Scripts\x12\x0e\n\x06script\x18\x01 \x01(\t\x12]\n\tvariables\x18\x02 \x03(\x0b\x32J.dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.BackupCfg.Scripts.Variables\x1a\'\n\tVariables\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x1a\xc5\x01\n\tChangeCfg\x12\x14\n\x0c\x64\x62InstanceId\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12Q\n\x07scripts\x18\x04 \x03(\x0b\x32@.dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.ChangeCfg.Scripts\x1a+\n\x07Scripts\x12\x0e\n\x06update\x18\x01 \x01(\t\x12\x10\n\x08rollback\x18\x02 \x01(\t\x1aU\n\x08\x43heckCfg\x12\x14\n\x0c\x64\x62InstanceId\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12\x0f\n\x07scripts\x18\x04 \x03(\t\"0\n\x1e\x43reateSQLPackageDBTaskResponse\x12\x0e\n\x06taskId\x18\x01 \x01(\t\"\x8f\x01\n%CreateSQLPackageDBTaskResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x34\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32&.dbtask.CreateSQLPackageDBTaskResponseb\x06proto3')
)




_CREATESQLPACKAGEDBTASKREQUEST_TASKINFO_BACKUPCFG_SCRIPTS_VARIABLES = _descriptor.Descriptor(
  name='Variables',
  full_name='dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.BackupCfg.Scripts.Variables',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.BackupCfg.Scripts.Variables.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.BackupCfg.Scripts.Variables.value', index=1,
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
  serialized_start=709,
  serialized_end=748,
)

_CREATESQLPACKAGEDBTASKREQUEST_TASKINFO_BACKUPCFG_SCRIPTS = _descriptor.Descriptor(
  name='Scripts',
  full_name='dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.BackupCfg.Scripts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='script', full_name='dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.BackupCfg.Scripts.script', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='variables', full_name='dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.BackupCfg.Scripts.variables', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CREATESQLPACKAGEDBTASKREQUEST_TASKINFO_BACKUPCFG_SCRIPTS_VARIABLES, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=587,
  serialized_end=748,
)

_CREATESQLPACKAGEDBTASKREQUEST_TASKINFO_BACKUPCFG = _descriptor.Descriptor(
  name='BackupCfg',
  full_name='dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.BackupCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dbInstanceId', full_name='dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.BackupCfg.dbInstanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hostId', full_name='dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.BackupCfg.hostId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hostIp', full_name='dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.BackupCfg.hostIp', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scripts', full_name='dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.BackupCfg.scripts', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CREATESQLPACKAGEDBTASKREQUEST_TASKINFO_BACKUPCFG_SCRIPTS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=436,
  serialized_end=748,
)

_CREATESQLPACKAGEDBTASKREQUEST_TASKINFO_CHANGECFG_SCRIPTS = _descriptor.Descriptor(
  name='Scripts',
  full_name='dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.ChangeCfg.Scripts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='update', full_name='dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.ChangeCfg.Scripts.update', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rollback', full_name='dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.ChangeCfg.Scripts.rollback', index=1,
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
  serialized_start=905,
  serialized_end=948,
)

_CREATESQLPACKAGEDBTASKREQUEST_TASKINFO_CHANGECFG = _descriptor.Descriptor(
  name='ChangeCfg',
  full_name='dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.ChangeCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dbInstanceId', full_name='dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.ChangeCfg.dbInstanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='username', full_name='dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.ChangeCfg.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.ChangeCfg.password', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scripts', full_name='dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.ChangeCfg.scripts', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CREATESQLPACKAGEDBTASKREQUEST_TASKINFO_CHANGECFG_SCRIPTS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=751,
  serialized_end=948,
)

_CREATESQLPACKAGEDBTASKREQUEST_TASKINFO_CHECKCFG = _descriptor.Descriptor(
  name='CheckCfg',
  full_name='dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.CheckCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dbInstanceId', full_name='dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.CheckCfg.dbInstanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='username', full_name='dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.CheckCfg.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.CheckCfg.password', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scripts', full_name='dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.CheckCfg.scripts', index=3,
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
  serialized_start=950,
  serialized_end=1035,
)

_CREATESQLPACKAGEDBTASKREQUEST_TASKINFO = _descriptor.Descriptor(
  name='TaskInfo',
  full_name='dbtask.CreateSQLPackageDBTaskRequest.TaskInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dbServiceId', full_name='dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.dbServiceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='backupCfg', full_name='dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.backupCfg', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='changeCfg', full_name='dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.changeCfg', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checkCfg', full_name='dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.checkCfg', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CREATESQLPACKAGEDBTASKREQUEST_TASKINFO_BACKUPCFG, _CREATESQLPACKAGEDBTASKREQUEST_TASKINFO_CHANGECFG, _CREATESQLPACKAGEDBTASKREQUEST_TASKINFO_CHECKCFG, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=173,
  serialized_end=1035,
)

_CREATESQLPACKAGEDBTASKREQUEST = _descriptor.Descriptor(
  name='CreateSQLPackageDBTaskRequest',
  full_name='dbtask.CreateSQLPackageDBTaskRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pkgId', full_name='dbtask.CreateSQLPackageDBTaskRequest.pkgId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionId', full_name='dbtask.CreateSQLPackageDBTaskRequest.versionId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='taskInfo', full_name='dbtask.CreateSQLPackageDBTaskRequest.taskInfo', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CREATESQLPACKAGEDBTASKREQUEST_TASKINFO, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=39,
  serialized_end=1035,
)


_CREATESQLPACKAGEDBTASKRESPONSE = _descriptor.Descriptor(
  name='CreateSQLPackageDBTaskResponse',
  full_name='dbtask.CreateSQLPackageDBTaskResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='taskId', full_name='dbtask.CreateSQLPackageDBTaskResponse.taskId', index=0,
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
  serialized_start=1037,
  serialized_end=1085,
)


_CREATESQLPACKAGEDBTASKRESPONSEWRAPPER = _descriptor.Descriptor(
  name='CreateSQLPackageDBTaskResponseWrapper',
  full_name='dbtask.CreateSQLPackageDBTaskResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='dbtask.CreateSQLPackageDBTaskResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='dbtask.CreateSQLPackageDBTaskResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dbtask.CreateSQLPackageDBTaskResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='dbtask.CreateSQLPackageDBTaskResponseWrapper.data', index=3,
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
  serialized_start=1088,
  serialized_end=1231,
)

_CREATESQLPACKAGEDBTASKREQUEST_TASKINFO_BACKUPCFG_SCRIPTS_VARIABLES.containing_type = _CREATESQLPACKAGEDBTASKREQUEST_TASKINFO_BACKUPCFG_SCRIPTS
_CREATESQLPACKAGEDBTASKREQUEST_TASKINFO_BACKUPCFG_SCRIPTS.fields_by_name['variables'].message_type = _CREATESQLPACKAGEDBTASKREQUEST_TASKINFO_BACKUPCFG_SCRIPTS_VARIABLES
_CREATESQLPACKAGEDBTASKREQUEST_TASKINFO_BACKUPCFG_SCRIPTS.containing_type = _CREATESQLPACKAGEDBTASKREQUEST_TASKINFO_BACKUPCFG
_CREATESQLPACKAGEDBTASKREQUEST_TASKINFO_BACKUPCFG.fields_by_name['scripts'].message_type = _CREATESQLPACKAGEDBTASKREQUEST_TASKINFO_BACKUPCFG_SCRIPTS
_CREATESQLPACKAGEDBTASKREQUEST_TASKINFO_BACKUPCFG.containing_type = _CREATESQLPACKAGEDBTASKREQUEST_TASKINFO
_CREATESQLPACKAGEDBTASKREQUEST_TASKINFO_CHANGECFG_SCRIPTS.containing_type = _CREATESQLPACKAGEDBTASKREQUEST_TASKINFO_CHANGECFG
_CREATESQLPACKAGEDBTASKREQUEST_TASKINFO_CHANGECFG.fields_by_name['scripts'].message_type = _CREATESQLPACKAGEDBTASKREQUEST_TASKINFO_CHANGECFG_SCRIPTS
_CREATESQLPACKAGEDBTASKREQUEST_TASKINFO_CHANGECFG.containing_type = _CREATESQLPACKAGEDBTASKREQUEST_TASKINFO
_CREATESQLPACKAGEDBTASKREQUEST_TASKINFO_CHECKCFG.containing_type = _CREATESQLPACKAGEDBTASKREQUEST_TASKINFO
_CREATESQLPACKAGEDBTASKREQUEST_TASKINFO.fields_by_name['backupCfg'].message_type = _CREATESQLPACKAGEDBTASKREQUEST_TASKINFO_BACKUPCFG
_CREATESQLPACKAGEDBTASKREQUEST_TASKINFO.fields_by_name['changeCfg'].message_type = _CREATESQLPACKAGEDBTASKREQUEST_TASKINFO_CHANGECFG
_CREATESQLPACKAGEDBTASKREQUEST_TASKINFO.fields_by_name['checkCfg'].message_type = _CREATESQLPACKAGEDBTASKREQUEST_TASKINFO_CHECKCFG
_CREATESQLPACKAGEDBTASKREQUEST_TASKINFO.containing_type = _CREATESQLPACKAGEDBTASKREQUEST
_CREATESQLPACKAGEDBTASKREQUEST.fields_by_name['taskInfo'].message_type = _CREATESQLPACKAGEDBTASKREQUEST_TASKINFO
_CREATESQLPACKAGEDBTASKRESPONSEWRAPPER.fields_by_name['data'].message_type = _CREATESQLPACKAGEDBTASKRESPONSE
DESCRIPTOR.message_types_by_name['CreateSQLPackageDBTaskRequest'] = _CREATESQLPACKAGEDBTASKREQUEST
DESCRIPTOR.message_types_by_name['CreateSQLPackageDBTaskResponse'] = _CREATESQLPACKAGEDBTASKRESPONSE
DESCRIPTOR.message_types_by_name['CreateSQLPackageDBTaskResponseWrapper'] = _CREATESQLPACKAGEDBTASKRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateSQLPackageDBTaskRequest = _reflection.GeneratedProtocolMessageType('CreateSQLPackageDBTaskRequest', (_message.Message,), {

  'TaskInfo' : _reflection.GeneratedProtocolMessageType('TaskInfo', (_message.Message,), {

    'BackupCfg' : _reflection.GeneratedProtocolMessageType('BackupCfg', (_message.Message,), {

      'Scripts' : _reflection.GeneratedProtocolMessageType('Scripts', (_message.Message,), {

        'Variables' : _reflection.GeneratedProtocolMessageType('Variables', (_message.Message,), {
          'DESCRIPTOR' : _CREATESQLPACKAGEDBTASKREQUEST_TASKINFO_BACKUPCFG_SCRIPTS_VARIABLES,
          '__module__' : 'create_sqlpkg_dbtask_pb2'
          # @@protoc_insertion_point(class_scope:dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.BackupCfg.Scripts.Variables)
          })
        ,
        'DESCRIPTOR' : _CREATESQLPACKAGEDBTASKREQUEST_TASKINFO_BACKUPCFG_SCRIPTS,
        '__module__' : 'create_sqlpkg_dbtask_pb2'
        # @@protoc_insertion_point(class_scope:dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.BackupCfg.Scripts)
        })
      ,
      'DESCRIPTOR' : _CREATESQLPACKAGEDBTASKREQUEST_TASKINFO_BACKUPCFG,
      '__module__' : 'create_sqlpkg_dbtask_pb2'
      # @@protoc_insertion_point(class_scope:dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.BackupCfg)
      })
    ,

    'ChangeCfg' : _reflection.GeneratedProtocolMessageType('ChangeCfg', (_message.Message,), {

      'Scripts' : _reflection.GeneratedProtocolMessageType('Scripts', (_message.Message,), {
        'DESCRIPTOR' : _CREATESQLPACKAGEDBTASKREQUEST_TASKINFO_CHANGECFG_SCRIPTS,
        '__module__' : 'create_sqlpkg_dbtask_pb2'
        # @@protoc_insertion_point(class_scope:dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.ChangeCfg.Scripts)
        })
      ,
      'DESCRIPTOR' : _CREATESQLPACKAGEDBTASKREQUEST_TASKINFO_CHANGECFG,
      '__module__' : 'create_sqlpkg_dbtask_pb2'
      # @@protoc_insertion_point(class_scope:dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.ChangeCfg)
      })
    ,

    'CheckCfg' : _reflection.GeneratedProtocolMessageType('CheckCfg', (_message.Message,), {
      'DESCRIPTOR' : _CREATESQLPACKAGEDBTASKREQUEST_TASKINFO_CHECKCFG,
      '__module__' : 'create_sqlpkg_dbtask_pb2'
      # @@protoc_insertion_point(class_scope:dbtask.CreateSQLPackageDBTaskRequest.TaskInfo.CheckCfg)
      })
    ,
    'DESCRIPTOR' : _CREATESQLPACKAGEDBTASKREQUEST_TASKINFO,
    '__module__' : 'create_sqlpkg_dbtask_pb2'
    # @@protoc_insertion_point(class_scope:dbtask.CreateSQLPackageDBTaskRequest.TaskInfo)
    })
  ,
  'DESCRIPTOR' : _CREATESQLPACKAGEDBTASKREQUEST,
  '__module__' : 'create_sqlpkg_dbtask_pb2'
  # @@protoc_insertion_point(class_scope:dbtask.CreateSQLPackageDBTaskRequest)
  })
_sym_db.RegisterMessage(CreateSQLPackageDBTaskRequest)
_sym_db.RegisterMessage(CreateSQLPackageDBTaskRequest.TaskInfo)
_sym_db.RegisterMessage(CreateSQLPackageDBTaskRequest.TaskInfo.BackupCfg)
_sym_db.RegisterMessage(CreateSQLPackageDBTaskRequest.TaskInfo.BackupCfg.Scripts)
_sym_db.RegisterMessage(CreateSQLPackageDBTaskRequest.TaskInfo.BackupCfg.Scripts.Variables)
_sym_db.RegisterMessage(CreateSQLPackageDBTaskRequest.TaskInfo.ChangeCfg)
_sym_db.RegisterMessage(CreateSQLPackageDBTaskRequest.TaskInfo.ChangeCfg.Scripts)
_sym_db.RegisterMessage(CreateSQLPackageDBTaskRequest.TaskInfo.CheckCfg)

CreateSQLPackageDBTaskResponse = _reflection.GeneratedProtocolMessageType('CreateSQLPackageDBTaskResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATESQLPACKAGEDBTASKRESPONSE,
  '__module__' : 'create_sqlpkg_dbtask_pb2'
  # @@protoc_insertion_point(class_scope:dbtask.CreateSQLPackageDBTaskResponse)
  })
_sym_db.RegisterMessage(CreateSQLPackageDBTaskResponse)

CreateSQLPackageDBTaskResponseWrapper = _reflection.GeneratedProtocolMessageType('CreateSQLPackageDBTaskResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _CREATESQLPACKAGEDBTASKRESPONSEWRAPPER,
  '__module__' : 'create_sqlpkg_dbtask_pb2'
  # @@protoc_insertion_point(class_scope:dbtask.CreateSQLPackageDBTaskResponseWrapper)
  })
_sym_db.RegisterMessage(CreateSQLPackageDBTaskResponseWrapper)


# @@protoc_insertion_point(module_scope)
