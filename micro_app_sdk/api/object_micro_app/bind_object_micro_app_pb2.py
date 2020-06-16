# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bind_object_micro_app.proto

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
  name='bind_object_micro_app.proto',
  package='object_micro_app',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1b\x62ind_object_micro_app.proto\x12\x10object_micro_app\x1a\x1bgoogle/protobuf/empty.proto\"*\n\x19\x42indObjectMicroAppRequest\x12\r\n\x05\x61ppId\x18\x01 \x01(\t\"{\n!BindObjectMicroAppResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12$\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x16.google.protobuf.Emptyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_BINDOBJECTMICROAPPREQUEST = _descriptor.Descriptor(
  name='BindObjectMicroAppRequest',
  full_name='object_micro_app.BindObjectMicroAppRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appId', full_name='object_micro_app.BindObjectMicroAppRequest.appId', index=0,
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
  serialized_start=78,
  serialized_end=120,
)


_BINDOBJECTMICROAPPRESPONSEWRAPPER = _descriptor.Descriptor(
  name='BindObjectMicroAppResponseWrapper',
  full_name='object_micro_app.BindObjectMicroAppResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='object_micro_app.BindObjectMicroAppResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='object_micro_app.BindObjectMicroAppResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='object_micro_app.BindObjectMicroAppResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='object_micro_app.BindObjectMicroAppResponseWrapper.data', index=3,
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
  serialized_start=122,
  serialized_end=245,
)

_BINDOBJECTMICROAPPRESPONSEWRAPPER.fields_by_name['data'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
DESCRIPTOR.message_types_by_name['BindObjectMicroAppRequest'] = _BINDOBJECTMICROAPPREQUEST
DESCRIPTOR.message_types_by_name['BindObjectMicroAppResponseWrapper'] = _BINDOBJECTMICROAPPRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BindObjectMicroAppRequest = _reflection.GeneratedProtocolMessageType('BindObjectMicroAppRequest', (_message.Message,), {
  'DESCRIPTOR' : _BINDOBJECTMICROAPPREQUEST,
  '__module__' : 'bind_object_micro_app_pb2'
  # @@protoc_insertion_point(class_scope:object_micro_app.BindObjectMicroAppRequest)
  })
_sym_db.RegisterMessage(BindObjectMicroAppRequest)

BindObjectMicroAppResponseWrapper = _reflection.GeneratedProtocolMessageType('BindObjectMicroAppResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _BINDOBJECTMICROAPPRESPONSEWRAPPER,
  '__module__' : 'bind_object_micro_app_pb2'
  # @@protoc_insertion_point(class_scope:object_micro_app.BindObjectMicroAppResponseWrapper)
  })
_sym_db.RegisterMessage(BindObjectMicroAppResponseWrapper)


# @@protoc_insertion_point(module_scope)
