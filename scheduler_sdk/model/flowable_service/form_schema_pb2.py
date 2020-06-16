# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: form_schema.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='form_schema.proto',
  package='flowable_service',
  syntax='proto3',
  serialized_options=_b('ZJgo.easyops.local/contracts/protorepo-models/easyops/model/flowable_service'),
  serialized_pb=_b('\n\x11\x66orm_schema.proto\x12\x10\x66lowable_service\"n\n\nFormSchema\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x03 \x01(\t\x12\x0f\n\x07\x63reator\x18\x04 \x01(\t\x12\x0c\n\x04memo\x18\x05 \x01(\t\x12\r\n\x05\x63time\x18\x06 \x01(\tBLZJgo.easyops.local/contracts/protorepo-models/easyops/model/flowable_serviceb\x06proto3')
)




_FORMSCHEMA = _descriptor.Descriptor(
  name='FormSchema',
  full_name='flowable_service.FormSchema',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='flowable_service.FormSchema.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='flowable_service.FormSchema.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='flowable_service.FormSchema.category', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='flowable_service.FormSchema.creator', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='flowable_service.FormSchema.memo', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='flowable_service.FormSchema.ctime', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=39,
  serialized_end=149,
)

DESCRIPTOR.message_types_by_name['FormSchema'] = _FORMSCHEMA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FormSchema = _reflection.GeneratedProtocolMessageType('FormSchema', (_message.Message,), {
  'DESCRIPTOR' : _FORMSCHEMA,
  '__module__' : 'form_schema_pb2'
  # @@protoc_insertion_point(class_scope:flowable_service.FormSchema)
  })
_sym_db.RegisterMessage(FormSchema)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
