# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_jobcategories.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_jobcategories.proto',
  package='jobs',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x17get_jobcategories.proto\x12\x04jobs\x1a\x1bgoogle/protobuf/empty.proto\")\n\x17GetJobCategoriesRequest\x12\x0e\n\x06menuId\x18\x01 \x01(\t\"a\n\x1fGetJobCategoriesResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x04 \x03(\tb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_GETJOBCATEGORIESREQUEST = _descriptor.Descriptor(
  name='GetJobCategoriesRequest',
  full_name='jobs.GetJobCategoriesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='menuId', full_name='jobs.GetJobCategoriesRequest.menuId', index=0,
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
  serialized_start=62,
  serialized_end=103,
)


_GETJOBCATEGORIESRESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetJobCategoriesResponseWrapper',
  full_name='jobs.GetJobCategoriesResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='jobs.GetJobCategoriesResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='jobs.GetJobCategoriesResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='jobs.GetJobCategoriesResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='jobs.GetJobCategoriesResponseWrapper.data', index=3,
      number=4, type=9, cpp_type=9, label=3,
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
  serialized_start=105,
  serialized_end=202,
)

DESCRIPTOR.message_types_by_name['GetJobCategoriesRequest'] = _GETJOBCATEGORIESREQUEST
DESCRIPTOR.message_types_by_name['GetJobCategoriesResponseWrapper'] = _GETJOBCATEGORIESRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetJobCategoriesRequest = _reflection.GeneratedProtocolMessageType('GetJobCategoriesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETJOBCATEGORIESREQUEST,
  '__module__' : 'get_jobcategories_pb2'
  # @@protoc_insertion_point(class_scope:jobs.GetJobCategoriesRequest)
  })
_sym_db.RegisterMessage(GetJobCategoriesRequest)

GetJobCategoriesResponseWrapper = _reflection.GeneratedProtocolMessageType('GetJobCategoriesResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _GETJOBCATEGORIESRESPONSEWRAPPER,
  '__module__' : 'get_jobcategories_pb2'
  # @@protoc_insertion_point(class_scope:jobs.GetJobCategoriesResponseWrapper)
  })
_sym_db.RegisterMessage(GetJobCategoriesResponseWrapper)


# @@protoc_insertion_point(module_scope)
