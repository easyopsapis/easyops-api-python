# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: convert_sql.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='convert_sql.proto',
  package='dbtask',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11\x63onvert_sql.proto\x12\x06\x64\x62task\"\x82\x01\n\x1c\x43onvertSQLToChangesetRequest\x12\x43\n\nconvertSQL\x18\x01 \x01(\x0b\x32/.dbtask.ConvertSQLToChangesetRequest.ConvertSQL\x1a\x1d\n\nConvertSQL\x12\x0f\n\x07sqlText\x18\x01 \x01(\t\"x\n\x1d\x43onvertSQLToChangesetResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x02 \x01(\t\x12\x11\n\totherAttr\x18\x03 \x01(\t\x12\x11\n\tupdateSql\x18\x04 \x01(\t\x12\x13\n\x0brollbackSql\x18\x05 \x01(\t\"\x8d\x01\n$ConvertSQLToChangesetResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x33\n\x04\x64\x61ta\x18\x04 \x03(\x0b\x32%.dbtask.ConvertSQLToChangesetResponseb\x06proto3')
)




_CONVERTSQLTOCHANGESETREQUEST_CONVERTSQL = _descriptor.Descriptor(
  name='ConvertSQL',
  full_name='dbtask.ConvertSQLToChangesetRequest.ConvertSQL',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sqlText', full_name='dbtask.ConvertSQLToChangesetRequest.ConvertSQL.sqlText', index=0,
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
  serialized_start=131,
  serialized_end=160,
)

_CONVERTSQLTOCHANGESETREQUEST = _descriptor.Descriptor(
  name='ConvertSQLToChangesetRequest',
  full_name='dbtask.ConvertSQLToChangesetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='convertSQL', full_name='dbtask.ConvertSQLToChangesetRequest.convertSQL', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CONVERTSQLTOCHANGESETREQUEST_CONVERTSQL, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=160,
)


_CONVERTSQLTOCHANGESETRESPONSE = _descriptor.Descriptor(
  name='ConvertSQLToChangesetResponse',
  full_name='dbtask.ConvertSQLToChangesetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='dbtask.ConvertSQLToChangesetResponse.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='author', full_name='dbtask.ConvertSQLToChangesetResponse.author', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='otherAttr', full_name='dbtask.ConvertSQLToChangesetResponse.otherAttr', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updateSql', full_name='dbtask.ConvertSQLToChangesetResponse.updateSql', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rollbackSql', full_name='dbtask.ConvertSQLToChangesetResponse.rollbackSql', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=162,
  serialized_end=282,
)


_CONVERTSQLTOCHANGESETRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ConvertSQLToChangesetResponseWrapper',
  full_name='dbtask.ConvertSQLToChangesetResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='dbtask.ConvertSQLToChangesetResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='dbtask.ConvertSQLToChangesetResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dbtask.ConvertSQLToChangesetResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='dbtask.ConvertSQLToChangesetResponseWrapper.data', index=3,
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
  serialized_start=285,
  serialized_end=426,
)

_CONVERTSQLTOCHANGESETREQUEST_CONVERTSQL.containing_type = _CONVERTSQLTOCHANGESETREQUEST
_CONVERTSQLTOCHANGESETREQUEST.fields_by_name['convertSQL'].message_type = _CONVERTSQLTOCHANGESETREQUEST_CONVERTSQL
_CONVERTSQLTOCHANGESETRESPONSEWRAPPER.fields_by_name['data'].message_type = _CONVERTSQLTOCHANGESETRESPONSE
DESCRIPTOR.message_types_by_name['ConvertSQLToChangesetRequest'] = _CONVERTSQLTOCHANGESETREQUEST
DESCRIPTOR.message_types_by_name['ConvertSQLToChangesetResponse'] = _CONVERTSQLTOCHANGESETRESPONSE
DESCRIPTOR.message_types_by_name['ConvertSQLToChangesetResponseWrapper'] = _CONVERTSQLTOCHANGESETRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConvertSQLToChangesetRequest = _reflection.GeneratedProtocolMessageType('ConvertSQLToChangesetRequest', (_message.Message,), {

  'ConvertSQL' : _reflection.GeneratedProtocolMessageType('ConvertSQL', (_message.Message,), {
    'DESCRIPTOR' : _CONVERTSQLTOCHANGESETREQUEST_CONVERTSQL,
    '__module__' : 'convert_sql_pb2'
    # @@protoc_insertion_point(class_scope:dbtask.ConvertSQLToChangesetRequest.ConvertSQL)
    })
  ,
  'DESCRIPTOR' : _CONVERTSQLTOCHANGESETREQUEST,
  '__module__' : 'convert_sql_pb2'
  # @@protoc_insertion_point(class_scope:dbtask.ConvertSQLToChangesetRequest)
  })
_sym_db.RegisterMessage(ConvertSQLToChangesetRequest)
_sym_db.RegisterMessage(ConvertSQLToChangesetRequest.ConvertSQL)

ConvertSQLToChangesetResponse = _reflection.GeneratedProtocolMessageType('ConvertSQLToChangesetResponse', (_message.Message,), {
  'DESCRIPTOR' : _CONVERTSQLTOCHANGESETRESPONSE,
  '__module__' : 'convert_sql_pb2'
  # @@protoc_insertion_point(class_scope:dbtask.ConvertSQLToChangesetResponse)
  })
_sym_db.RegisterMessage(ConvertSQLToChangesetResponse)

ConvertSQLToChangesetResponseWrapper = _reflection.GeneratedProtocolMessageType('ConvertSQLToChangesetResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _CONVERTSQLTOCHANGESETRESPONSEWRAPPER,
  '__module__' : 'convert_sql_pb2'
  # @@protoc_insertion_point(class_scope:dbtask.ConvertSQLToChangesetResponseWrapper)
  })
_sym_db.RegisterMessage(ConvertSQLToChangesetResponseWrapper)


# @@protoc_insertion_point(module_scope)
