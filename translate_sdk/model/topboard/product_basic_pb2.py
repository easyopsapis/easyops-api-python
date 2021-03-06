# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: product_basic.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='product_basic.proto',
  package='topboard',
  syntax='proto3',
  serialized_options=_b('ZBgo.easyops.local/contracts/protorepo-models/easyops/model/topboard'),
  serialized_pb=_b('\n\x13product_basic.proto\x12\x08topboard\"T\n\x0cProductBasic\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ninstanceId\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\tBDZBgo.easyops.local/contracts/protorepo-models/easyops/model/topboardb\x06proto3')
)




_PRODUCTBASIC = _descriptor.Descriptor(
  name='ProductBasic',
  full_name='topboard.ProductBasic',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='topboard.ProductBasic.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='topboard.ProductBasic.instanceId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='topboard.ProductBasic.title', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='topboard.ProductBasic.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=33,
  serialized_end=117,
)

DESCRIPTOR.message_types_by_name['ProductBasic'] = _PRODUCTBASIC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProductBasic = _reflection.GeneratedProtocolMessageType('ProductBasic', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCTBASIC,
  '__module__' : 'product_basic_pb2'
  # @@protoc_insertion_point(class_scope:topboard.ProductBasic)
  })
_sym_db.RegisterMessage(ProductBasic)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
