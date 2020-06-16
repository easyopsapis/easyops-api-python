# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: import_v2.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cmdb_sdk.model.cmdb import cmdb_object_pb2 as cmdb__sdk_dot_model_dot_cmdb_dot_cmdb__object__pb2
from cmdb_sdk.model.cmdb import import_result_pb2 as cmdb__sdk_dot_model_dot_cmdb_dot_import__result__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='import_v2.proto',
  package='cmdb_object',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0fimport_v2.proto\x12\x0b\x63mdb_object\x1a%cmdb_sdk/model/cmdb/cmdb_object.proto\x1a\'cmdb_sdk/model/cmdb/import_result.proto\"8\n\x0fImportV2Request\x12%\n\x0bobject_list\x18\x01 \x03(\x0b\x32\x10.cmdb.CmdbObject\"=\n\x10ImportV2Response\x12)\n\rimport_result\x18\x01 \x03(\x0b\x32\x12.cmdb.ImportResult\"x\n\x17ImportV2ResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12+\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1d.cmdb_object.ImportV2Responseb\x06proto3')
  ,
  dependencies=[cmdb__sdk_dot_model_dot_cmdb_dot_cmdb__object__pb2.DESCRIPTOR,cmdb__sdk_dot_model_dot_cmdb_dot_import__result__pb2.DESCRIPTOR,])




_IMPORTV2REQUEST = _descriptor.Descriptor(
  name='ImportV2Request',
  full_name='cmdb_object.ImportV2Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_list', full_name='cmdb_object.ImportV2Request.object_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=112,
  serialized_end=168,
)


_IMPORTV2RESPONSE = _descriptor.Descriptor(
  name='ImportV2Response',
  full_name='cmdb_object.ImportV2Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='import_result', full_name='cmdb_object.ImportV2Response.import_result', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=170,
  serialized_end=231,
)


_IMPORTV2RESPONSEWRAPPER = _descriptor.Descriptor(
  name='ImportV2ResponseWrapper',
  full_name='cmdb_object.ImportV2ResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='cmdb_object.ImportV2ResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='cmdb_object.ImportV2ResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='cmdb_object.ImportV2ResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='cmdb_object.ImportV2ResponseWrapper.data', index=3,
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
  serialized_start=233,
  serialized_end=353,
)

_IMPORTV2REQUEST.fields_by_name['object_list'].message_type = cmdb__sdk_dot_model_dot_cmdb_dot_cmdb__object__pb2._CMDBOBJECT
_IMPORTV2RESPONSE.fields_by_name['import_result'].message_type = cmdb__sdk_dot_model_dot_cmdb_dot_import__result__pb2._IMPORTRESULT
_IMPORTV2RESPONSEWRAPPER.fields_by_name['data'].message_type = _IMPORTV2RESPONSE
DESCRIPTOR.message_types_by_name['ImportV2Request'] = _IMPORTV2REQUEST
DESCRIPTOR.message_types_by_name['ImportV2Response'] = _IMPORTV2RESPONSE
DESCRIPTOR.message_types_by_name['ImportV2ResponseWrapper'] = _IMPORTV2RESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImportV2Request = _reflection.GeneratedProtocolMessageType('ImportV2Request', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTV2REQUEST,
  '__module__' : 'import_v2_pb2'
  # @@protoc_insertion_point(class_scope:cmdb_object.ImportV2Request)
  })
_sym_db.RegisterMessage(ImportV2Request)

ImportV2Response = _reflection.GeneratedProtocolMessageType('ImportV2Response', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTV2RESPONSE,
  '__module__' : 'import_v2_pb2'
  # @@protoc_insertion_point(class_scope:cmdb_object.ImportV2Response)
  })
_sym_db.RegisterMessage(ImportV2Response)

ImportV2ResponseWrapper = _reflection.GeneratedProtocolMessageType('ImportV2ResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTV2RESPONSEWRAPPER,
  '__module__' : 'import_v2_pb2'
  # @@protoc_insertion_point(class_scope:cmdb_object.ImportV2ResponseWrapper)
  })
_sym_db.RegisterMessage(ImportV2ResponseWrapper)


# @@protoc_insertion_point(module_scope)
