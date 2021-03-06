# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: update_one.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='update_one.proto',
  package='host_resolved',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10update_one.proto\x12\rhost_resolved\x1a\x1cgoogle/protobuf/struct.proto\"E\n\x10UpdateOneRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12%\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\"s\n\x18UpdateOneResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12%\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Structb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_UPDATEONEREQUEST = _descriptor.Descriptor(
  name='UpdateOneRequest',
  full_name='host_resolved.UpdateOneRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='host_resolved.UpdateOneRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='host_resolved.UpdateOneRequest.data', index=1,
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
  serialized_start=65,
  serialized_end=134,
)


_UPDATEONERESPONSEWRAPPER = _descriptor.Descriptor(
  name='UpdateOneResponseWrapper',
  full_name='host_resolved.UpdateOneResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='host_resolved.UpdateOneResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='host_resolved.UpdateOneResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='host_resolved.UpdateOneResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='host_resolved.UpdateOneResponseWrapper.data', index=3,
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
  serialized_start=136,
  serialized_end=251,
)

_UPDATEONEREQUEST.fields_by_name['data'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_UPDATEONERESPONSEWRAPPER.fields_by_name['data'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['UpdateOneRequest'] = _UPDATEONEREQUEST
DESCRIPTOR.message_types_by_name['UpdateOneResponseWrapper'] = _UPDATEONERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateOneRequest = _reflection.GeneratedProtocolMessageType('UpdateOneRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEONEREQUEST,
  '__module__' : 'update_one_pb2'
  # @@protoc_insertion_point(class_scope:host_resolved.UpdateOneRequest)
  })
_sym_db.RegisterMessage(UpdateOneRequest)

UpdateOneResponseWrapper = _reflection.GeneratedProtocolMessageType('UpdateOneResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEONERESPONSEWRAPPER,
  '__module__' : 'update_one_pb2'
  # @@protoc_insertion_point(class_scope:host_resolved.UpdateOneResponseWrapper)
  })
_sym_db.RegisterMessage(UpdateOneResponseWrapper)


# @@protoc_insertion_point(module_scope)
