# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: retry_sqlpkg_dbtask.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='retry_sqlpkg_dbtask.proto',
  package='dbtask',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x19retry_sqlpkg_dbtask.proto\x12\x06\x64\x62task\"@\n\x1cRetrySQLPackageDBTaskRequest\x12\x10\n\x08\x64\x62TaskId\x18\x01 \x01(\t\x12\x0e\n\x06isSkip\x18\x02 \x01(\x05\"/\n\x1dRetrySQLPackageDBTaskResponse\x12\x0e\n\x06taskId\x18\x01 \x01(\t\"\x8d\x01\n$RetrySQLPackageDBTaskResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x33\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32%.dbtask.RetrySQLPackageDBTaskResponseb\x06proto3')
)




_RETRYSQLPACKAGEDBTASKREQUEST = _descriptor.Descriptor(
  name='RetrySQLPackageDBTaskRequest',
  full_name='dbtask.RetrySQLPackageDBTaskRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dbTaskId', full_name='dbtask.RetrySQLPackageDBTaskRequest.dbTaskId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isSkip', full_name='dbtask.RetrySQLPackageDBTaskRequest.isSkip', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=37,
  serialized_end=101,
)


_RETRYSQLPACKAGEDBTASKRESPONSE = _descriptor.Descriptor(
  name='RetrySQLPackageDBTaskResponse',
  full_name='dbtask.RetrySQLPackageDBTaskResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='taskId', full_name='dbtask.RetrySQLPackageDBTaskResponse.taskId', index=0,
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
  serialized_start=103,
  serialized_end=150,
)


_RETRYSQLPACKAGEDBTASKRESPONSEWRAPPER = _descriptor.Descriptor(
  name='RetrySQLPackageDBTaskResponseWrapper',
  full_name='dbtask.RetrySQLPackageDBTaskResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='dbtask.RetrySQLPackageDBTaskResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='dbtask.RetrySQLPackageDBTaskResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dbtask.RetrySQLPackageDBTaskResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='dbtask.RetrySQLPackageDBTaskResponseWrapper.data', index=3,
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
  serialized_start=153,
  serialized_end=294,
)

_RETRYSQLPACKAGEDBTASKRESPONSEWRAPPER.fields_by_name['data'].message_type = _RETRYSQLPACKAGEDBTASKRESPONSE
DESCRIPTOR.message_types_by_name['RetrySQLPackageDBTaskRequest'] = _RETRYSQLPACKAGEDBTASKREQUEST
DESCRIPTOR.message_types_by_name['RetrySQLPackageDBTaskResponse'] = _RETRYSQLPACKAGEDBTASKRESPONSE
DESCRIPTOR.message_types_by_name['RetrySQLPackageDBTaskResponseWrapper'] = _RETRYSQLPACKAGEDBTASKRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RetrySQLPackageDBTaskRequest = _reflection.GeneratedProtocolMessageType('RetrySQLPackageDBTaskRequest', (_message.Message,), dict(
  DESCRIPTOR = _RETRYSQLPACKAGEDBTASKREQUEST,
  __module__ = 'retry_sqlpkg_dbtask_pb2'
  # @@protoc_insertion_point(class_scope:dbtask.RetrySQLPackageDBTaskRequest)
  ))
_sym_db.RegisterMessage(RetrySQLPackageDBTaskRequest)

RetrySQLPackageDBTaskResponse = _reflection.GeneratedProtocolMessageType('RetrySQLPackageDBTaskResponse', (_message.Message,), dict(
  DESCRIPTOR = _RETRYSQLPACKAGEDBTASKRESPONSE,
  __module__ = 'retry_sqlpkg_dbtask_pb2'
  # @@protoc_insertion_point(class_scope:dbtask.RetrySQLPackageDBTaskResponse)
  ))
_sym_db.RegisterMessage(RetrySQLPackageDBTaskResponse)

RetrySQLPackageDBTaskResponseWrapper = _reflection.GeneratedProtocolMessageType('RetrySQLPackageDBTaskResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _RETRYSQLPACKAGEDBTASKRESPONSEWRAPPER,
  __module__ = 'retry_sqlpkg_dbtask_pb2'
  # @@protoc_insertion_point(class_scope:dbtask.RetrySQLPackageDBTaskResponseWrapper)
  ))
_sym_db.RegisterMessage(RetrySQLPackageDBTaskResponseWrapper)


# @@protoc_insertion_point(module_scope)
