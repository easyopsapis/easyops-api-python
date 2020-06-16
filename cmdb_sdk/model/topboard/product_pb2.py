# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: product.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cmdb_sdk.model.topboard import sprint_pb2 as cmdb__sdk_dot_model_dot_topboard_dot_sprint__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='product.proto',
  package='topboard',
  syntax='proto3',
  serialized_options=_b('ZBgo.easyops.local/contracts/protorepo-models/easyops/model/topboard'),
  serialized_pb=_b('\n\rproduct.proto\x12\x08topboard\x1a$cmdb_sdk/model/topboard/sprint.proto\"r\n\x07Product\x12!\n\x07sprints\x18\x01 \x03(\x0b\x32\x10.topboard.Sprint\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\ninstanceId\x18\x03 \x01(\t\x12\r\n\x05title\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\tBDZBgo.easyops.local/contracts/protorepo-models/easyops/model/topboardb\x06proto3')
  ,
  dependencies=[cmdb__sdk_dot_model_dot_topboard_dot_sprint__pb2.DESCRIPTOR,])




_PRODUCT = _descriptor.Descriptor(
  name='Product',
  full_name='topboard.Product',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sprints', full_name='topboard.Product.sprints', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='topboard.Product.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='topboard.Product.instanceId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='topboard.Product.title', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='topboard.Product.description', index=4,
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
  serialized_start=65,
  serialized_end=179,
)

_PRODUCT.fields_by_name['sprints'].message_type = cmdb__sdk_dot_model_dot_topboard_dot_sprint__pb2._SPRINT
DESCRIPTOR.message_types_by_name['Product'] = _PRODUCT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Product = _reflection.GeneratedProtocolMessageType('Product', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCT,
  '__module__' : 'product_pb2'
  # @@protoc_insertion_point(class_scope:topboard.Product)
  })
_sym_db.RegisterMessage(Product)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
