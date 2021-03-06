# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: delete.proto

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
  name='delete.proto',
  package='dbservice',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0c\x64\x65lete.proto\x12\tdbservice\x1a\x1bgoogle/protobuf/empty.proto\"-\n\x16\x44\x65leteDBServiceRequest\x12\x13\n\x0b\x64\x62ServiceId\x18\x01 \x01(\t\"x\n\x1e\x44\x65leteDBServiceResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12$\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x16.google.protobuf.Emptyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_DELETEDBSERVICEREQUEST = _descriptor.Descriptor(
  name='DeleteDBServiceRequest',
  full_name='dbservice.DeleteDBServiceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dbServiceId', full_name='dbservice.DeleteDBServiceRequest.dbServiceId', index=0,
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
  serialized_start=56,
  serialized_end=101,
)


_DELETEDBSERVICERESPONSEWRAPPER = _descriptor.Descriptor(
  name='DeleteDBServiceResponseWrapper',
  full_name='dbservice.DeleteDBServiceResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='dbservice.DeleteDBServiceResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='dbservice.DeleteDBServiceResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dbservice.DeleteDBServiceResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='dbservice.DeleteDBServiceResponseWrapper.data', index=3,
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
  serialized_start=103,
  serialized_end=223,
)

_DELETEDBSERVICERESPONSEWRAPPER.fields_by_name['data'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
DESCRIPTOR.message_types_by_name['DeleteDBServiceRequest'] = _DELETEDBSERVICEREQUEST
DESCRIPTOR.message_types_by_name['DeleteDBServiceResponseWrapper'] = _DELETEDBSERVICERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeleteDBServiceRequest = _reflection.GeneratedProtocolMessageType('DeleteDBServiceRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEDBSERVICEREQUEST,
  '__module__' : 'delete_pb2'
  # @@protoc_insertion_point(class_scope:dbservice.DeleteDBServiceRequest)
  })
_sym_db.RegisterMessage(DeleteDBServiceRequest)

DeleteDBServiceResponseWrapper = _reflection.GeneratedProtocolMessageType('DeleteDBServiceResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _DELETEDBSERVICERESPONSEWRAPPER,
  '__module__' : 'delete_pb2'
  # @@protoc_insertion_point(class_scope:dbservice.DeleteDBServiceResponseWrapper)
  })
_sym_db.RegisterMessage(DeleteDBServiceResponseWrapper)


# @@protoc_insertion_point(module_scope)
