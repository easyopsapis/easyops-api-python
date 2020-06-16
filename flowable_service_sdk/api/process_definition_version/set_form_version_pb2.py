# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: set_form_version.proto

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
  name='set_form_version.proto',
  package='process_definition_version',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16set_form_version.proto\x12\x1aprocess_definition_version\x1a\x1bgoogle/protobuf/empty.proto\"\x86\x01\n\x15SetFormVersionRequest\x12\x11\n\tversionId\x18\x01 \x01(\t\x12\x16\n\x0e\x66orm_versionId\x18\x02 \x01(\t\x12\x12\n\nuserTaskId\x18\x03 \x01(\t\x12\x17\n\x0ftaskWorkingTime\x18\x04 \x01(\t\x12\x15\n\rapprovalLimit\x18\x05 \x01(\t\"w\n\x1dSetFormVersionResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12$\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x16.google.protobuf.Emptyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_SETFORMVERSIONREQUEST = _descriptor.Descriptor(
  name='SetFormVersionRequest',
  full_name='process_definition_version.SetFormVersionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='versionId', full_name='process_definition_version.SetFormVersionRequest.versionId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='form_versionId', full_name='process_definition_version.SetFormVersionRequest.form_versionId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userTaskId', full_name='process_definition_version.SetFormVersionRequest.userTaskId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='taskWorkingTime', full_name='process_definition_version.SetFormVersionRequest.taskWorkingTime', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='approvalLimit', full_name='process_definition_version.SetFormVersionRequest.approvalLimit', index=4,
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
  serialized_start=84,
  serialized_end=218,
)


_SETFORMVERSIONRESPONSEWRAPPER = _descriptor.Descriptor(
  name='SetFormVersionResponseWrapper',
  full_name='process_definition_version.SetFormVersionResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='process_definition_version.SetFormVersionResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='process_definition_version.SetFormVersionResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='process_definition_version.SetFormVersionResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='process_definition_version.SetFormVersionResponseWrapper.data', index=3,
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
  serialized_start=220,
  serialized_end=339,
)

_SETFORMVERSIONRESPONSEWRAPPER.fields_by_name['data'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
DESCRIPTOR.message_types_by_name['SetFormVersionRequest'] = _SETFORMVERSIONREQUEST
DESCRIPTOR.message_types_by_name['SetFormVersionResponseWrapper'] = _SETFORMVERSIONRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SetFormVersionRequest = _reflection.GeneratedProtocolMessageType('SetFormVersionRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETFORMVERSIONREQUEST,
  '__module__' : 'set_form_version_pb2'
  # @@protoc_insertion_point(class_scope:process_definition_version.SetFormVersionRequest)
  })
_sym_db.RegisterMessage(SetFormVersionRequest)

SetFormVersionResponseWrapper = _reflection.GeneratedProtocolMessageType('SetFormVersionResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _SETFORMVERSIONRESPONSEWRAPPER,
  '__module__' : 'set_form_version_pb2'
  # @@protoc_insertion_point(class_scope:process_definition_version.SetFormVersionResponseWrapper)
  })
_sym_db.RegisterMessage(SetFormVersionResponseWrapper)


# @@protoc_insertion_point(module_scope)