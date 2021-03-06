# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list_backlog_data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from easy_work_service_sdk.model.easy_work_service import backlog_pb2 as easy__work__service__sdk_dot_model_dot_easy__work__service_dot_backlog__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='list_backlog_data.proto',
  package='backlog',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x17list_backlog_data.proto\x12\x07\x62\x61\x63klog\x1a;easy_work_service_sdk/model/easy_work_service/backlog.proto\"k\n\x16ListBacklogDataRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x10\n\x08pageSize\x18\x02 \x01(\x05\x12\x10\n\x08\x63\x61tegory\x18\x03 \x01(\t\x12\x0f\n\x07keyword\x18\x04 \x01(\t\x12\x0e\n\x06status\x18\x05 \x01(\t\"s\n\x17ListBacklogDataResponse\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12(\n\x04list\x18\x04 \x03(\x0b\x32\x1a.easy_work_service.Backlog\"\x82\x01\n\x1eListBacklogDataResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12.\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32 .backlog.ListBacklogDataResponseb\x06proto3')
  ,
  dependencies=[easy__work__service__sdk_dot_model_dot_easy__work__service_dot_backlog__pb2.DESCRIPTOR,])




_LISTBACKLOGDATAREQUEST = _descriptor.Descriptor(
  name='ListBacklogDataRequest',
  full_name='backlog.ListBacklogDataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='backlog.ListBacklogDataRequest.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='backlog.ListBacklogDataRequest.pageSize', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='backlog.ListBacklogDataRequest.category', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keyword', full_name='backlog.ListBacklogDataRequest.keyword', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='backlog.ListBacklogDataRequest.status', index=4,
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
  serialized_start=97,
  serialized_end=204,
)


_LISTBACKLOGDATARESPONSE = _descriptor.Descriptor(
  name='ListBacklogDataResponse',
  full_name='backlog.ListBacklogDataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='backlog.ListBacklogDataResponse.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='backlog.ListBacklogDataResponse.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='backlog.ListBacklogDataResponse.total', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='backlog.ListBacklogDataResponse.list', index=3,
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
  serialized_start=206,
  serialized_end=321,
)


_LISTBACKLOGDATARESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListBacklogDataResponseWrapper',
  full_name='backlog.ListBacklogDataResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='backlog.ListBacklogDataResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='backlog.ListBacklogDataResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='backlog.ListBacklogDataResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='backlog.ListBacklogDataResponseWrapper.data', index=3,
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
  serialized_start=324,
  serialized_end=454,
)

_LISTBACKLOGDATARESPONSE.fields_by_name['list'].message_type = easy__work__service__sdk_dot_model_dot_easy__work__service_dot_backlog__pb2._BACKLOG
_LISTBACKLOGDATARESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTBACKLOGDATARESPONSE
DESCRIPTOR.message_types_by_name['ListBacklogDataRequest'] = _LISTBACKLOGDATAREQUEST
DESCRIPTOR.message_types_by_name['ListBacklogDataResponse'] = _LISTBACKLOGDATARESPONSE
DESCRIPTOR.message_types_by_name['ListBacklogDataResponseWrapper'] = _LISTBACKLOGDATARESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListBacklogDataRequest = _reflection.GeneratedProtocolMessageType('ListBacklogDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTBACKLOGDATAREQUEST,
  '__module__' : 'list_backlog_data_pb2'
  # @@protoc_insertion_point(class_scope:backlog.ListBacklogDataRequest)
  })
_sym_db.RegisterMessage(ListBacklogDataRequest)

ListBacklogDataResponse = _reflection.GeneratedProtocolMessageType('ListBacklogDataResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTBACKLOGDATARESPONSE,
  '__module__' : 'list_backlog_data_pb2'
  # @@protoc_insertion_point(class_scope:backlog.ListBacklogDataResponse)
  })
_sym_db.RegisterMessage(ListBacklogDataResponse)

ListBacklogDataResponseWrapper = _reflection.GeneratedProtocolMessageType('ListBacklogDataResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _LISTBACKLOGDATARESPONSEWRAPPER,
  '__module__' : 'list_backlog_data_pb2'
  # @@protoc_insertion_point(class_scope:backlog.ListBacklogDataResponseWrapper)
  })
_sym_db.RegisterMessage(ListBacklogDataResponseWrapper)


# @@protoc_insertion_point(module_scope)
