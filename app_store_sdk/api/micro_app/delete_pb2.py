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
  package='micro_app',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0c\x64\x65lete.proto\x12\tmicro_app\x1a\x1bgoogle/protobuf/empty.proto\"/\n\x1d\x44\x65leteAppStoreMicroAppRequest\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\t\"\x7f\n%DeleteAppStoreMicroAppResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12$\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x16.google.protobuf.Emptyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_DELETEAPPSTOREMICROAPPREQUEST = _descriptor.Descriptor(
  name='DeleteAppStoreMicroAppRequest',
  full_name='micro_app.DeleteAppStoreMicroAppRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='app_id', full_name='micro_app.DeleteAppStoreMicroAppRequest.app_id', index=0,
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
  serialized_end=103,
)


_DELETEAPPSTOREMICROAPPRESPONSEWRAPPER = _descriptor.Descriptor(
  name='DeleteAppStoreMicroAppResponseWrapper',
  full_name='micro_app.DeleteAppStoreMicroAppResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='micro_app.DeleteAppStoreMicroAppResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='micro_app.DeleteAppStoreMicroAppResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='micro_app.DeleteAppStoreMicroAppResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='micro_app.DeleteAppStoreMicroAppResponseWrapper.data', index=3,
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
  serialized_start=105,
  serialized_end=232,
)

_DELETEAPPSTOREMICROAPPRESPONSEWRAPPER.fields_by_name['data'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
DESCRIPTOR.message_types_by_name['DeleteAppStoreMicroAppRequest'] = _DELETEAPPSTOREMICROAPPREQUEST
DESCRIPTOR.message_types_by_name['DeleteAppStoreMicroAppResponseWrapper'] = _DELETEAPPSTOREMICROAPPRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeleteAppStoreMicroAppRequest = _reflection.GeneratedProtocolMessageType('DeleteAppStoreMicroAppRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEAPPSTOREMICROAPPREQUEST,
  '__module__' : 'delete_pb2'
  # @@protoc_insertion_point(class_scope:micro_app.DeleteAppStoreMicroAppRequest)
  })
_sym_db.RegisterMessage(DeleteAppStoreMicroAppRequest)

DeleteAppStoreMicroAppResponseWrapper = _reflection.GeneratedProtocolMessageType('DeleteAppStoreMicroAppResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _DELETEAPPSTOREMICROAPPRESPONSEWRAPPER,
  '__module__' : 'delete_pb2'
  # @@protoc_insertion_point(class_scope:micro_app.DeleteAppStoreMicroAppResponseWrapper)
  })
_sym_db.RegisterMessage(DeleteAppStoreMicroAppResponseWrapper)


# @@protoc_insertion_point(module_scope)
