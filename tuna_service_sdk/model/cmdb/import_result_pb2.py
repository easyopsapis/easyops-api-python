# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: import_result.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tuna_service_sdk.model.cmdb import import_status_pb2 as tuna__service__sdk_dot_model_dot_cmdb_dot_import__status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='import_result.proto',
  package='cmdb',
  syntax='proto3',
  serialized_options=_b('Z>go.easyops.local/contracts/protorepo-models/easyops/model/cmdb'),
  serialized_pb=_b('\n\x13import_result.proto\x12\x04\x63mdb\x1a/tuna_service_sdk/model/cmdb/import_status.proto\"\x83\x04\n\x0cImportResult\x12\x10\n\x08objectId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x03 \x01(\t\x12\x0c\n\x04memo\x18\x04 \x01(\t\x12\x11\n\tprotected\x18\x05 \x01(\x08\x12\x0e\n\x06system\x18\x06 \x01(\t\x12\x0c\n\x04\x63ode\x18\x07 \x01(\x05\x12\x0f\n\x07message\x18\x08 \x01(\t\x12\'\n\x0binfo_result\x18\t \x03(\x0b\x32\x12.cmdb.ImportStatus\x12\x31\n\x15relation_group_result\x18\n \x03(\x0b\x32\x12.cmdb.ImportStatus\x12,\n\x10\x61ttr_list_result\x18\x0b \x03(\x0b\x32\x12.cmdb.ImportStatus\x12\x30\n\x14relation_list_result\x18\x0c \x03(\x0b\x32\x12.cmdb.ImportStatus\x12=\n\x11index_list_result\x18\r \x03(\x0b\x32\".cmdb.ImportResult.IndexListResult\x12\x11\n\tis_create\x18\x0e \x01(\x08\x1a\x63\n\x0fIndexListResult\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0bpropertyIds\x18\x04 \x03(\t\x12\x0e\n\x06unique\x18\x05 \x01(\x08\x42@Z>go.easyops.local/contracts/protorepo-models/easyops/model/cmdbb\x06proto3')
  ,
  dependencies=[tuna__service__sdk_dot_model_dot_cmdb_dot_import__status__pb2.DESCRIPTOR,])




_IMPORTRESULT_INDEXLISTRESULT = _descriptor.Descriptor(
  name='IndexListResult',
  full_name='cmdb.ImportResult.IndexListResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='cmdb.ImportResult.IndexListResult.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='cmdb.ImportResult.IndexListResult.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='cmdb.ImportResult.IndexListResult.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='propertyIds', full_name='cmdb.ImportResult.IndexListResult.propertyIds', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unique', full_name='cmdb.ImportResult.IndexListResult.unique', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=495,
  serialized_end=594,
)

_IMPORTRESULT = _descriptor.Descriptor(
  name='ImportResult',
  full_name='cmdb.ImportResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='objectId', full_name='cmdb.ImportResult.objectId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='cmdb.ImportResult.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='cmdb.ImportResult.category', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='cmdb.ImportResult.memo', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='protected', full_name='cmdb.ImportResult.protected', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='system', full_name='cmdb.ImportResult.system', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='cmdb.ImportResult.code', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='cmdb.ImportResult.message', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='info_result', full_name='cmdb.ImportResult.info_result', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relation_group_result', full_name='cmdb.ImportResult.relation_group_result', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attr_list_result', full_name='cmdb.ImportResult.attr_list_result', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relation_list_result', full_name='cmdb.ImportResult.relation_list_result', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='index_list_result', full_name='cmdb.ImportResult.index_list_result', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_create', full_name='cmdb.ImportResult.is_create', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_IMPORTRESULT_INDEXLISTRESULT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=79,
  serialized_end=594,
)

_IMPORTRESULT_INDEXLISTRESULT.containing_type = _IMPORTRESULT
_IMPORTRESULT.fields_by_name['info_result'].message_type = tuna__service__sdk_dot_model_dot_cmdb_dot_import__status__pb2._IMPORTSTATUS
_IMPORTRESULT.fields_by_name['relation_group_result'].message_type = tuna__service__sdk_dot_model_dot_cmdb_dot_import__status__pb2._IMPORTSTATUS
_IMPORTRESULT.fields_by_name['attr_list_result'].message_type = tuna__service__sdk_dot_model_dot_cmdb_dot_import__status__pb2._IMPORTSTATUS
_IMPORTRESULT.fields_by_name['relation_list_result'].message_type = tuna__service__sdk_dot_model_dot_cmdb_dot_import__status__pb2._IMPORTSTATUS
_IMPORTRESULT.fields_by_name['index_list_result'].message_type = _IMPORTRESULT_INDEXLISTRESULT
DESCRIPTOR.message_types_by_name['ImportResult'] = _IMPORTRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImportResult = _reflection.GeneratedProtocolMessageType('ImportResult', (_message.Message,), {

  'IndexListResult' : _reflection.GeneratedProtocolMessageType('IndexListResult', (_message.Message,), {
    'DESCRIPTOR' : _IMPORTRESULT_INDEXLISTRESULT,
    '__module__' : 'import_result_pb2'
    # @@protoc_insertion_point(class_scope:cmdb.ImportResult.IndexListResult)
    })
  ,
  'DESCRIPTOR' : _IMPORTRESULT,
  '__module__' : 'import_result_pb2'
  # @@protoc_insertion_point(class_scope:cmdb.ImportResult)
  })
_sym_db.RegisterMessage(ImportResult)
_sym_db.RegisterMessage(ImportResult.IndexListResult)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
