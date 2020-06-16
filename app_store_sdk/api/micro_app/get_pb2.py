# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from app_store_sdk.model.app_store import app_version_pb2 as app__store__sdk_dot_model_dot_app__store_dot_app__version__pb2
from app_store_sdk.model.app_store import product_line_pb2 as app__store__sdk_dot_model_dot_app__store_dot_product__line__pb2
from app_store_sdk.model.app_store import solution_pb2 as app__store__sdk_dot_model_dot_app__store_dot_solution__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='get.proto',
  package='micro_app',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\tget.proto\x12\tmicro_app\x1a/app_store_sdk/model/app_store/app_version.proto\x1a\x30\x61pp_store_sdk/model/app_store/product_line.proto\x1a,app_store_sdk/model/app_store/solution.proto\",\n\x1aGetAppStoreMicroAppRequest\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\t\"\xff\x02\n\x1bGetAppStoreMicroAppResponse\x12-\n\x0e\x63urrentVersion\x18\x01 \x01(\x0b\x32\x15.app_store.AppVersion\x12,\n\x0cproductLines\x18\x02 \x03(\x0b\x32\x16.app_store.ProductLine\x12&\n\tsolutions\x18\x03 \x03(\x0b\x32\x13.app_store.Solution\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\n\n\x02id\x18\x05 \x01(\t\x12;\n\x05icons\x18\x06 \x01(\x0b\x32,.micro_app.GetAppStoreMicroAppResponse.Icons\x12\r\n\x05intro\x18\x07 \x01(\t\x12\x0f\n\x07preview\x18\x08 \x03(\t\x12\x13\n\x0b\x64\x65scription\x18\t \x01(\t\x12\x10\n\x08homepage\x18\n \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x0b \x01(\t\x12\x13\n\x0b\x63ontainerId\x18\x0c \x01(\t\x1a\x16\n\x05Icons\x12\r\n\x05large\x18\x01 \x01(\t\"\x8c\x01\n\"GetAppStoreMicroAppResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x34\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32&.micro_app.GetAppStoreMicroAppResponseb\x06proto3')
  ,
  dependencies=[app__store__sdk_dot_model_dot_app__store_dot_app__version__pb2.DESCRIPTOR,app__store__sdk_dot_model_dot_app__store_dot_product__line__pb2.DESCRIPTOR,app__store__sdk_dot_model_dot_app__store_dot_solution__pb2.DESCRIPTOR,])




_GETAPPSTOREMICROAPPREQUEST = _descriptor.Descriptor(
  name='GetAppStoreMicroAppRequest',
  full_name='micro_app.GetAppStoreMicroAppRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='app_id', full_name='micro_app.GetAppStoreMicroAppRequest.app_id', index=0,
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
  serialized_start=169,
  serialized_end=213,
)


_GETAPPSTOREMICROAPPRESPONSE_ICONS = _descriptor.Descriptor(
  name='Icons',
  full_name='micro_app.GetAppStoreMicroAppResponse.Icons',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='large', full_name='micro_app.GetAppStoreMicroAppResponse.Icons.large', index=0,
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
  serialized_start=577,
  serialized_end=599,
)

_GETAPPSTOREMICROAPPRESPONSE = _descriptor.Descriptor(
  name='GetAppStoreMicroAppResponse',
  full_name='micro_app.GetAppStoreMicroAppResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='currentVersion', full_name='micro_app.GetAppStoreMicroAppResponse.currentVersion', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='productLines', full_name='micro_app.GetAppStoreMicroAppResponse.productLines', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='solutions', full_name='micro_app.GetAppStoreMicroAppResponse.solutions', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='micro_app.GetAppStoreMicroAppResponse.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='micro_app.GetAppStoreMicroAppResponse.id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icons', full_name='micro_app.GetAppStoreMicroAppResponse.icons', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='intro', full_name='micro_app.GetAppStoreMicroAppResponse.intro', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preview', full_name='micro_app.GetAppStoreMicroAppResponse.preview', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='micro_app.GetAppStoreMicroAppResponse.description', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='homepage', full_name='micro_app.GetAppStoreMicroAppResponse.homepage', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='micro_app.GetAppStoreMicroAppResponse.category', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='containerId', full_name='micro_app.GetAppStoreMicroAppResponse.containerId', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETAPPSTOREMICROAPPRESPONSE_ICONS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=216,
  serialized_end=599,
)


_GETAPPSTOREMICROAPPRESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetAppStoreMicroAppResponseWrapper',
  full_name='micro_app.GetAppStoreMicroAppResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='micro_app.GetAppStoreMicroAppResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='micro_app.GetAppStoreMicroAppResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='micro_app.GetAppStoreMicroAppResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='micro_app.GetAppStoreMicroAppResponseWrapper.data', index=3,
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
  serialized_start=602,
  serialized_end=742,
)

_GETAPPSTOREMICROAPPRESPONSE_ICONS.containing_type = _GETAPPSTOREMICROAPPRESPONSE
_GETAPPSTOREMICROAPPRESPONSE.fields_by_name['currentVersion'].message_type = app__store__sdk_dot_model_dot_app__store_dot_app__version__pb2._APPVERSION
_GETAPPSTOREMICROAPPRESPONSE.fields_by_name['productLines'].message_type = app__store__sdk_dot_model_dot_app__store_dot_product__line__pb2._PRODUCTLINE
_GETAPPSTOREMICROAPPRESPONSE.fields_by_name['solutions'].message_type = app__store__sdk_dot_model_dot_app__store_dot_solution__pb2._SOLUTION
_GETAPPSTOREMICROAPPRESPONSE.fields_by_name['icons'].message_type = _GETAPPSTOREMICROAPPRESPONSE_ICONS
_GETAPPSTOREMICROAPPRESPONSEWRAPPER.fields_by_name['data'].message_type = _GETAPPSTOREMICROAPPRESPONSE
DESCRIPTOR.message_types_by_name['GetAppStoreMicroAppRequest'] = _GETAPPSTOREMICROAPPREQUEST
DESCRIPTOR.message_types_by_name['GetAppStoreMicroAppResponse'] = _GETAPPSTOREMICROAPPRESPONSE
DESCRIPTOR.message_types_by_name['GetAppStoreMicroAppResponseWrapper'] = _GETAPPSTOREMICROAPPRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetAppStoreMicroAppRequest = _reflection.GeneratedProtocolMessageType('GetAppStoreMicroAppRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETAPPSTOREMICROAPPREQUEST,
  '__module__' : 'get_pb2'
  # @@protoc_insertion_point(class_scope:micro_app.GetAppStoreMicroAppRequest)
  })
_sym_db.RegisterMessage(GetAppStoreMicroAppRequest)

GetAppStoreMicroAppResponse = _reflection.GeneratedProtocolMessageType('GetAppStoreMicroAppResponse', (_message.Message,), {

  'Icons' : _reflection.GeneratedProtocolMessageType('Icons', (_message.Message,), {
    'DESCRIPTOR' : _GETAPPSTOREMICROAPPRESPONSE_ICONS,
    '__module__' : 'get_pb2'
    # @@protoc_insertion_point(class_scope:micro_app.GetAppStoreMicroAppResponse.Icons)
    })
  ,
  'DESCRIPTOR' : _GETAPPSTOREMICROAPPRESPONSE,
  '__module__' : 'get_pb2'
  # @@protoc_insertion_point(class_scope:micro_app.GetAppStoreMicroAppResponse)
  })
_sym_db.RegisterMessage(GetAppStoreMicroAppResponse)
_sym_db.RegisterMessage(GetAppStoreMicroAppResponse.Icons)

GetAppStoreMicroAppResponseWrapper = _reflection.GeneratedProtocolMessageType('GetAppStoreMicroAppResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _GETAPPSTOREMICROAPPRESPONSEWRAPPER,
  '__module__' : 'get_pb2'
  # @@protoc_insertion_point(class_scope:micro_app.GetAppStoreMicroAppResponseWrapper)
  })
_sym_db.RegisterMessage(GetAppStoreMicroAppResponseWrapper)


# @@protoc_insertion_point(module_scope)
