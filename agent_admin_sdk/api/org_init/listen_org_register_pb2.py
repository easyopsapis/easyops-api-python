# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: listen_org_register.proto

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
  name='listen_org_register.proto',
  package='org_init',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x19listen_org_register.proto\x12\x08org_init\x1a\x1bgoogle/protobuf/empty.proto\"~\n\x18ListenOrgRegisterRequest\x12\x39\n\x06params\x18\x01 \x01(\x0b\x32).org_init.ListenOrgRegisterRequest.Params\x1a\'\n\x06Params\x12\x0e\n\x06system\x18\x01 \x01(\t\x12\r\n\x05topic\x18\x02 \x01(\t\"z\n ListenOrgRegisterResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12$\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x16.google.protobuf.Emptyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_LISTENORGREGISTERREQUEST_PARAMS = _descriptor.Descriptor(
  name='Params',
  full_name='org_init.ListenOrgRegisterRequest.Params',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='system', full_name='org_init.ListenOrgRegisterRequest.Params.system', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='topic', full_name='org_init.ListenOrgRegisterRequest.Params.topic', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=155,
  serialized_end=194,
)

_LISTENORGREGISTERREQUEST = _descriptor.Descriptor(
  name='ListenOrgRegisterRequest',
  full_name='org_init.ListenOrgRegisterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='params', full_name='org_init.ListenOrgRegisterRequest.params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTENORGREGISTERREQUEST_PARAMS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=68,
  serialized_end=194,
)


_LISTENORGREGISTERRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListenOrgRegisterResponseWrapper',
  full_name='org_init.ListenOrgRegisterResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='org_init.ListenOrgRegisterResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='org_init.ListenOrgRegisterResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='org_init.ListenOrgRegisterResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='org_init.ListenOrgRegisterResponseWrapper.data', index=3,
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
  serialized_start=196,
  serialized_end=318,
)

_LISTENORGREGISTERREQUEST_PARAMS.containing_type = _LISTENORGREGISTERREQUEST
_LISTENORGREGISTERREQUEST.fields_by_name['params'].message_type = _LISTENORGREGISTERREQUEST_PARAMS
_LISTENORGREGISTERRESPONSEWRAPPER.fields_by_name['data'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
DESCRIPTOR.message_types_by_name['ListenOrgRegisterRequest'] = _LISTENORGREGISTERREQUEST
DESCRIPTOR.message_types_by_name['ListenOrgRegisterResponseWrapper'] = _LISTENORGREGISTERRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListenOrgRegisterRequest = _reflection.GeneratedProtocolMessageType('ListenOrgRegisterRequest', (_message.Message,), {

  'Params' : _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {
    'DESCRIPTOR' : _LISTENORGREGISTERREQUEST_PARAMS,
    '__module__' : 'listen_org_register_pb2'
    # @@protoc_insertion_point(class_scope:org_init.ListenOrgRegisterRequest.Params)
    })
  ,
  'DESCRIPTOR' : _LISTENORGREGISTERREQUEST,
  '__module__' : 'listen_org_register_pb2'
  # @@protoc_insertion_point(class_scope:org_init.ListenOrgRegisterRequest)
  })
_sym_db.RegisterMessage(ListenOrgRegisterRequest)
_sym_db.RegisterMessage(ListenOrgRegisterRequest.Params)

ListenOrgRegisterResponseWrapper = _reflection.GeneratedProtocolMessageType('ListenOrgRegisterResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _LISTENORGREGISTERRESPONSEWRAPPER,
  '__module__' : 'listen_org_register_pb2'
  # @@protoc_insertion_point(class_scope:org_init.ListenOrgRegisterResponseWrapper)
  })
_sym_db.RegisterMessage(ListenOrgRegisterResponseWrapper)


# @@protoc_insertion_point(module_scope)
