# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_job_change_log.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_job_change_log.proto',
  package='jobs',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x18get_job_change_log.proto\x12\x04jobs\"G\n\x16GetJobChangeLogRequest\x12\r\n\x05jobId\x18\x01 \x01(\t\x12\x0c\n\x04page\x18\x02 \x01(\x05\x12\x10\n\x08pageSize\x18\x03 \x01(\x05\"\xf4\x01\n\x17GetJobChangeLogResponse\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12\x30\n\x04list\x18\x04 \x03(\x0b\x32\".jobs.GetJobChangeLogResponse.List\x1aw\n\x04List\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\x05\x12\x12\n\ncreateTime\x18\x04 \x01(\t\x12\x12\n\nupdateTime\x18\x05 \x01(\t\x12\x0f\n\x07\x63reator\x18\x06 \x01(\t\x12\x0b\n\x03org\x18\x07 \x01(\x05\"\x7f\n\x1eGetJobChangeLogResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12+\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1d.jobs.GetJobChangeLogResponseb\x06proto3')
)




_GETJOBCHANGELOGREQUEST = _descriptor.Descriptor(
  name='GetJobChangeLogRequest',
  full_name='jobs.GetJobChangeLogRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='jobId', full_name='jobs.GetJobChangeLogRequest.jobId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page', full_name='jobs.GetJobChangeLogRequest.page', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='jobs.GetJobChangeLogRequest.pageSize', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=34,
  serialized_end=105,
)


_GETJOBCHANGELOGRESPONSE_LIST = _descriptor.Descriptor(
  name='List',
  full_name='jobs.GetJobChangeLogResponse.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='jobs.GetJobChangeLogResponse.List.data', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='jobs.GetJobChangeLogResponse.List.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='jobs.GetJobChangeLogResponse.List.version', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='createTime', full_name='jobs.GetJobChangeLogResponse.List.createTime', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updateTime', full_name='jobs.GetJobChangeLogResponse.List.updateTime', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='jobs.GetJobChangeLogResponse.List.creator', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org', full_name='jobs.GetJobChangeLogResponse.List.org', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_end=352,
)

_GETJOBCHANGELOGRESPONSE = _descriptor.Descriptor(
  name='GetJobChangeLogResponse',
  full_name='jobs.GetJobChangeLogResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='jobs.GetJobChangeLogResponse.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='jobs.GetJobChangeLogResponse.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='jobs.GetJobChangeLogResponse.total', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='jobs.GetJobChangeLogResponse.list', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETJOBCHANGELOGRESPONSE_LIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=108,
  serialized_end=352,
)


_GETJOBCHANGELOGRESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetJobChangeLogResponseWrapper',
  full_name='jobs.GetJobChangeLogResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='jobs.GetJobChangeLogResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='jobs.GetJobChangeLogResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='jobs.GetJobChangeLogResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='jobs.GetJobChangeLogResponseWrapper.data', index=3,
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
  serialized_start=354,
  serialized_end=481,
)

_GETJOBCHANGELOGRESPONSE_LIST.containing_type = _GETJOBCHANGELOGRESPONSE
_GETJOBCHANGELOGRESPONSE.fields_by_name['list'].message_type = _GETJOBCHANGELOGRESPONSE_LIST
_GETJOBCHANGELOGRESPONSEWRAPPER.fields_by_name['data'].message_type = _GETJOBCHANGELOGRESPONSE
DESCRIPTOR.message_types_by_name['GetJobChangeLogRequest'] = _GETJOBCHANGELOGREQUEST
DESCRIPTOR.message_types_by_name['GetJobChangeLogResponse'] = _GETJOBCHANGELOGRESPONSE
DESCRIPTOR.message_types_by_name['GetJobChangeLogResponseWrapper'] = _GETJOBCHANGELOGRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetJobChangeLogRequest = _reflection.GeneratedProtocolMessageType('GetJobChangeLogRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETJOBCHANGELOGREQUEST,
  '__module__' : 'get_job_change_log_pb2'
  # @@protoc_insertion_point(class_scope:jobs.GetJobChangeLogRequest)
  })
_sym_db.RegisterMessage(GetJobChangeLogRequest)

GetJobChangeLogResponse = _reflection.GeneratedProtocolMessageType('GetJobChangeLogResponse', (_message.Message,), {

  'List' : _reflection.GeneratedProtocolMessageType('List', (_message.Message,), {
    'DESCRIPTOR' : _GETJOBCHANGELOGRESPONSE_LIST,
    '__module__' : 'get_job_change_log_pb2'
    # @@protoc_insertion_point(class_scope:jobs.GetJobChangeLogResponse.List)
    })
  ,
  'DESCRIPTOR' : _GETJOBCHANGELOGRESPONSE,
  '__module__' : 'get_job_change_log_pb2'
  # @@protoc_insertion_point(class_scope:jobs.GetJobChangeLogResponse)
  })
_sym_db.RegisterMessage(GetJobChangeLogResponse)
_sym_db.RegisterMessage(GetJobChangeLogResponse.List)

GetJobChangeLogResponseWrapper = _reflection.GeneratedProtocolMessageType('GetJobChangeLogResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _GETJOBCHANGELOGRESPONSEWRAPPER,
  '__module__' : 'get_job_change_log_pb2'
  # @@protoc_insertion_point(class_scope:jobs.GetJobChangeLogResponseWrapper)
  })
_sym_db.RegisterMessage(GetJobChangeLogResponseWrapper)


# @@protoc_insertion_point(module_scope)
