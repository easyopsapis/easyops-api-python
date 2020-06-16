# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flowable_service_sdk.model.flowable_service import form_schema_version_pb2 as flowable__service__sdk_dot_model_dot_flowable__service_dot_form__schema__version__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='list.proto',
  package='form_schema',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\nlist.proto\x12\x0b\x66orm_schema\x1a\x45\x66lowable_service_sdk/model/flowable_service/form_schema_version.proto\"\x92\x01\n\x15ListFormSchemaRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x10\n\x08pageSize\x18\x02 \x01(\x05\x12\x10\n\x08\x63\x61tegory\x18\x03 \x01(\t\x12\x0f\n\x07\x63reator\x18\x04 \x01(\t\x12\x0e\n\x06isMain\x18\x05 \x01(\x08\x12\t\n\x01Q\x18\x06 \x01(\t\x12\x0c\n\x04name\x18\x07 \x01(\t\x12\r\n\x05state\x18\x08 \x01(\t\"\xac\x02\n\x16ListFormSchemaResponse\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12\x36\n\x04list\x18\x04 \x03(\x0b\x32(.form_schema.ListFormSchemaResponse.List\x1a\xa9\x01\n\x04List\x12?\n\x12lastestMainVersion\x18\x01 \x01(\x0b\x32#.flowable_service.FormSchemaVersion\x12\x12\n\ninstanceId\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x04 \x01(\t\x12\x0c\n\x04memo\x18\x05 \x01(\t\x12\x0f\n\x07\x63reator\x18\x06 \x01(\t\x12\r\n\x05\x63time\x18\x07 \x01(\t\"\x84\x01\n\x1dListFormSchemaResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x31\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32#.form_schema.ListFormSchemaResponseb\x06proto3')
  ,
  dependencies=[flowable__service__sdk_dot_model_dot_flowable__service_dot_form__schema__version__pb2.DESCRIPTOR,])




_LISTFORMSCHEMAREQUEST = _descriptor.Descriptor(
  name='ListFormSchemaRequest',
  full_name='form_schema.ListFormSchemaRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='form_schema.ListFormSchemaRequest.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='form_schema.ListFormSchemaRequest.pageSize', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='form_schema.ListFormSchemaRequest.category', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='form_schema.ListFormSchemaRequest.creator', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isMain', full_name='form_schema.ListFormSchemaRequest.isMain', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Q', full_name='form_schema.ListFormSchemaRequest.Q', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='form_schema.ListFormSchemaRequest.name', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='form_schema.ListFormSchemaRequest.state', index=7,
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
  serialized_start=99,
  serialized_end=245,
)


_LISTFORMSCHEMARESPONSE_LIST = _descriptor.Descriptor(
  name='List',
  full_name='form_schema.ListFormSchemaResponse.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lastestMainVersion', full_name='form_schema.ListFormSchemaResponse.List.lastestMainVersion', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='form_schema.ListFormSchemaResponse.List.instanceId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='form_schema.ListFormSchemaResponse.List.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='form_schema.ListFormSchemaResponse.List.category', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='form_schema.ListFormSchemaResponse.List.memo', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='form_schema.ListFormSchemaResponse.List.creator', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='form_schema.ListFormSchemaResponse.List.ctime', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=379,
  serialized_end=548,
)

_LISTFORMSCHEMARESPONSE = _descriptor.Descriptor(
  name='ListFormSchemaResponse',
  full_name='form_schema.ListFormSchemaResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='form_schema.ListFormSchemaResponse.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='form_schema.ListFormSchemaResponse.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='form_schema.ListFormSchemaResponse.total', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='form_schema.ListFormSchemaResponse.list', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTFORMSCHEMARESPONSE_LIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=248,
  serialized_end=548,
)


_LISTFORMSCHEMARESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListFormSchemaResponseWrapper',
  full_name='form_schema.ListFormSchemaResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='form_schema.ListFormSchemaResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='form_schema.ListFormSchemaResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='form_schema.ListFormSchemaResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='form_schema.ListFormSchemaResponseWrapper.data', index=3,
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
  serialized_start=551,
  serialized_end=683,
)

_LISTFORMSCHEMARESPONSE_LIST.fields_by_name['lastestMainVersion'].message_type = flowable__service__sdk_dot_model_dot_flowable__service_dot_form__schema__version__pb2._FORMSCHEMAVERSION
_LISTFORMSCHEMARESPONSE_LIST.containing_type = _LISTFORMSCHEMARESPONSE
_LISTFORMSCHEMARESPONSE.fields_by_name['list'].message_type = _LISTFORMSCHEMARESPONSE_LIST
_LISTFORMSCHEMARESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTFORMSCHEMARESPONSE
DESCRIPTOR.message_types_by_name['ListFormSchemaRequest'] = _LISTFORMSCHEMAREQUEST
DESCRIPTOR.message_types_by_name['ListFormSchemaResponse'] = _LISTFORMSCHEMARESPONSE
DESCRIPTOR.message_types_by_name['ListFormSchemaResponseWrapper'] = _LISTFORMSCHEMARESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListFormSchemaRequest = _reflection.GeneratedProtocolMessageType('ListFormSchemaRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTFORMSCHEMAREQUEST,
  '__module__' : 'list_pb2'
  # @@protoc_insertion_point(class_scope:form_schema.ListFormSchemaRequest)
  })
_sym_db.RegisterMessage(ListFormSchemaRequest)

ListFormSchemaResponse = _reflection.GeneratedProtocolMessageType('ListFormSchemaResponse', (_message.Message,), {

  'List' : _reflection.GeneratedProtocolMessageType('List', (_message.Message,), {
    'DESCRIPTOR' : _LISTFORMSCHEMARESPONSE_LIST,
    '__module__' : 'list_pb2'
    # @@protoc_insertion_point(class_scope:form_schema.ListFormSchemaResponse.List)
    })
  ,
  'DESCRIPTOR' : _LISTFORMSCHEMARESPONSE,
  '__module__' : 'list_pb2'
  # @@protoc_insertion_point(class_scope:form_schema.ListFormSchemaResponse)
  })
_sym_db.RegisterMessage(ListFormSchemaResponse)
_sym_db.RegisterMessage(ListFormSchemaResponse.List)

ListFormSchemaResponseWrapper = _reflection.GeneratedProtocolMessageType('ListFormSchemaResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _LISTFORMSCHEMARESPONSEWRAPPER,
  '__module__' : 'list_pb2'
  # @@protoc_insertion_point(class_scope:form_schema.ListFormSchemaResponseWrapper)
  })
_sym_db.RegisterMessage(ListFormSchemaResponseWrapper)


# @@protoc_insertion_point(module_scope)
