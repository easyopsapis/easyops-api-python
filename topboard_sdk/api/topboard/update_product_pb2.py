# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: update_product.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from topboard_sdk.model.topboard import product_pb2 as topboard__sdk_dot_model_dot_topboard_dot_product__pb2
from topboard_sdk.model.topboard import sprint_pb2 as topboard__sdk_dot_model_dot_topboard_dot_sprint__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='update_product.proto',
  package='topboard',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14update_product.proto\x12\x08topboard\x1a)topboard_sdk/model/topboard/product.proto\x1a(topboard_sdk/model/topboard/sprint.proto\"M\n\x14UpdateProductRequest\x12\x11\n\tproductID\x18\x01 \x01(\t\x12\"\n\x07product\x18\x02 \x01(\x0b\x32\x11.topboard.Product\"q\n\x1cUpdateProductResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x1f\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x11.topboard.Productb\x06proto3')
  ,
  dependencies=[topboard__sdk_dot_model_dot_topboard_dot_product__pb2.DESCRIPTOR,topboard__sdk_dot_model_dot_topboard_dot_sprint__pb2.DESCRIPTOR,])




_UPDATEPRODUCTREQUEST = _descriptor.Descriptor(
  name='UpdateProductRequest',
  full_name='topboard.UpdateProductRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='productID', full_name='topboard.UpdateProductRequest.productID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='product', full_name='topboard.UpdateProductRequest.product', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=119,
  serialized_end=196,
)


_UPDATEPRODUCTRESPONSEWRAPPER = _descriptor.Descriptor(
  name='UpdateProductResponseWrapper',
  full_name='topboard.UpdateProductResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='topboard.UpdateProductResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='topboard.UpdateProductResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='topboard.UpdateProductResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='topboard.UpdateProductResponseWrapper.data', index=3,
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
  serialized_start=198,
  serialized_end=311,
)

_UPDATEPRODUCTREQUEST.fields_by_name['product'].message_type = topboard__sdk_dot_model_dot_topboard_dot_product__pb2._PRODUCT
_UPDATEPRODUCTRESPONSEWRAPPER.fields_by_name['data'].message_type = topboard__sdk_dot_model_dot_topboard_dot_product__pb2._PRODUCT
DESCRIPTOR.message_types_by_name['UpdateProductRequest'] = _UPDATEPRODUCTREQUEST
DESCRIPTOR.message_types_by_name['UpdateProductResponseWrapper'] = _UPDATEPRODUCTRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateProductRequest = _reflection.GeneratedProtocolMessageType('UpdateProductRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPRODUCTREQUEST,
  '__module__' : 'update_product_pb2'
  # @@protoc_insertion_point(class_scope:topboard.UpdateProductRequest)
  })
_sym_db.RegisterMessage(UpdateProductRequest)

UpdateProductResponseWrapper = _reflection.GeneratedProtocolMessageType('UpdateProductResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPRODUCTRESPONSEWRAPPER,
  '__module__' : 'update_product_pb2'
  # @@protoc_insertion_point(class_scope:topboard.UpdateProductResponseWrapper)
  })
_sym_db.RegisterMessage(UpdateProductResponseWrapper)


# @@protoc_insertion_point(module_scope)
