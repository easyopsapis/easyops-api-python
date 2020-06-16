# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: edit_custom_dbtask_rollbacksql.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='edit_custom_dbtask_rollbacksql.proto',
  package='dbtask',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n$edit_custom_dbtask_rollbacksql.proto\x12\x06\x64\x62task\x1a\x1bgoogle/protobuf/empty.proto\"\xcf\x01\n\"EditCustomDBTaskRollbackSQLRequest\x12\x10\n\x08\x64\x62TaskId\x18\x01 \x01(\t\x12I\n\neditParams\x18\x02 \x01(\x0b\x32\x35.dbtask.EditCustomDBTaskRollbackSQLRequest.EditParams\x1aL\n\nEditParams\x12\x14\n\x0c\x65ntityTaskId\x18\x01 \x01(\t\x12\x13\n\x0b\x63hangesetId\x18\x02 \x01(\t\x12\x13\n\x0brollbackSql\x18\x03 \x01(\t\"\x84\x01\n*EditCustomDBTaskRollbackSQLResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12$\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x16.google.protobuf.Emptyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_EDITCUSTOMDBTASKROLLBACKSQLREQUEST_EDITPARAMS = _descriptor.Descriptor(
  name='EditParams',
  full_name='dbtask.EditCustomDBTaskRollbackSQLRequest.EditParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entityTaskId', full_name='dbtask.EditCustomDBTaskRollbackSQLRequest.EditParams.entityTaskId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='changesetId', full_name='dbtask.EditCustomDBTaskRollbackSQLRequest.EditParams.changesetId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rollbackSql', full_name='dbtask.EditCustomDBTaskRollbackSQLRequest.EditParams.rollbackSql', index=2,
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
  serialized_start=209,
  serialized_end=285,
)

_EDITCUSTOMDBTASKROLLBACKSQLREQUEST = _descriptor.Descriptor(
  name='EditCustomDBTaskRollbackSQLRequest',
  full_name='dbtask.EditCustomDBTaskRollbackSQLRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dbTaskId', full_name='dbtask.EditCustomDBTaskRollbackSQLRequest.dbTaskId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='editParams', full_name='dbtask.EditCustomDBTaskRollbackSQLRequest.editParams', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_EDITCUSTOMDBTASKROLLBACKSQLREQUEST_EDITPARAMS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=78,
  serialized_end=285,
)


_EDITCUSTOMDBTASKROLLBACKSQLRESPONSEWRAPPER = _descriptor.Descriptor(
  name='EditCustomDBTaskRollbackSQLResponseWrapper',
  full_name='dbtask.EditCustomDBTaskRollbackSQLResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='dbtask.EditCustomDBTaskRollbackSQLResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='dbtask.EditCustomDBTaskRollbackSQLResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dbtask.EditCustomDBTaskRollbackSQLResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='dbtask.EditCustomDBTaskRollbackSQLResponseWrapper.data', index=3,
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
  serialized_start=288,
  serialized_end=420,
)

_EDITCUSTOMDBTASKROLLBACKSQLREQUEST_EDITPARAMS.containing_type = _EDITCUSTOMDBTASKROLLBACKSQLREQUEST
_EDITCUSTOMDBTASKROLLBACKSQLREQUEST.fields_by_name['editParams'].message_type = _EDITCUSTOMDBTASKROLLBACKSQLREQUEST_EDITPARAMS
_EDITCUSTOMDBTASKROLLBACKSQLRESPONSEWRAPPER.fields_by_name['data'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
DESCRIPTOR.message_types_by_name['EditCustomDBTaskRollbackSQLRequest'] = _EDITCUSTOMDBTASKROLLBACKSQLREQUEST
DESCRIPTOR.message_types_by_name['EditCustomDBTaskRollbackSQLResponseWrapper'] = _EDITCUSTOMDBTASKROLLBACKSQLRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EditCustomDBTaskRollbackSQLRequest = _reflection.GeneratedProtocolMessageType('EditCustomDBTaskRollbackSQLRequest', (_message.Message,), {

  'EditParams' : _reflection.GeneratedProtocolMessageType('EditParams', (_message.Message,), {
    'DESCRIPTOR' : _EDITCUSTOMDBTASKROLLBACKSQLREQUEST_EDITPARAMS,
    '__module__' : 'edit_custom_dbtask_rollbacksql_pb2'
    # @@protoc_insertion_point(class_scope:dbtask.EditCustomDBTaskRollbackSQLRequest.EditParams)
    })
  ,
  'DESCRIPTOR' : _EDITCUSTOMDBTASKROLLBACKSQLREQUEST,
  '__module__' : 'edit_custom_dbtask_rollbacksql_pb2'
  # @@protoc_insertion_point(class_scope:dbtask.EditCustomDBTaskRollbackSQLRequest)
  })
_sym_db.RegisterMessage(EditCustomDBTaskRollbackSQLRequest)
_sym_db.RegisterMessage(EditCustomDBTaskRollbackSQLRequest.EditParams)

EditCustomDBTaskRollbackSQLResponseWrapper = _reflection.GeneratedProtocolMessageType('EditCustomDBTaskRollbackSQLResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _EDITCUSTOMDBTASKROLLBACKSQLRESPONSEWRAPPER,
  '__module__' : 'edit_custom_dbtask_rollbacksql_pb2'
  # @@protoc_insertion_point(class_scope:dbtask.EditCustomDBTaskRollbackSQLResponseWrapper)
  })
_sym_db.RegisterMessage(EditCustomDBTaskRollbackSQLResponseWrapper)


# @@protoc_insertion_point(module_scope)
