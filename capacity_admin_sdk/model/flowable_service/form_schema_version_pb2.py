# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: form_schema_version.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='form_schema_version.proto',
  package='flowable_service',
  syntax='proto3',
  serialized_options=_b('ZJgo.easyops.local/contracts/protorepo-models/easyops/model/flowable_service'),
  serialized_pb=_b('\n\x19\x66orm_schema_version.proto\x12\x10\x66lowable_service\"\xa1\x01\n\x11\x46ormSchemaVersion\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x13\n\x0bversionName\x18\x02 \x01(\t\x12\x0e\n\x06isMain\x18\x03 \x01(\x08\x12\r\n\x05state\x18\x04 \x01(\t\x12\x0c\n\x04memo\x18\x05 \x01(\t\x12\x0f\n\x07\x63reator\x18\x06 \x01(\t\x12\x16\n\x0e\x66ormDefinition\x18\x07 \x01(\t\x12\r\n\x05\x63time\x18\x08 \x01(\tBLZJgo.easyops.local/contracts/protorepo-models/easyops/model/flowable_serviceb\x06proto3')
)




_FORMSCHEMAVERSION = _descriptor.Descriptor(
  name='FormSchemaVersion',
  full_name='flowable_service.FormSchemaVersion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='flowable_service.FormSchemaVersion.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionName', full_name='flowable_service.FormSchemaVersion.versionName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isMain', full_name='flowable_service.FormSchemaVersion.isMain', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='flowable_service.FormSchemaVersion.state', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='flowable_service.FormSchemaVersion.memo', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='flowable_service.FormSchemaVersion.creator', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='formDefinition', full_name='flowable_service.FormSchemaVersion.formDefinition', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='flowable_service.FormSchemaVersion.ctime', index=7,
      number=8, type=9, cpp_type=9, label=1,
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
  serialized_start=48,
  serialized_end=209,
)

DESCRIPTOR.message_types_by_name['FormSchemaVersion'] = _FORMSCHEMAVERSION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FormSchemaVersion = _reflection.GeneratedProtocolMessageType('FormSchemaVersion', (_message.Message,), {
  'DESCRIPTOR' : _FORMSCHEMAVERSION,
  '__module__' : 'form_schema_version_pb2'
  # @@protoc_insertion_point(class_scope:flowable_service.FormSchemaVersion)
  })
_sym_db.RegisterMessage(FormSchemaVersion)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
