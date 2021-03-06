# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: easy_tornado_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='easy_tornado_response.proto',
  package='monitor',
  syntax='proto3',
  serialized_options=_b('ZAgo.easyops.local/contracts/protorepo-models/easyops/model/monitor'),
  serialized_pb=_b('\n\x1b\x65\x61sy_tornado_response.proto\x12\x07monitor\"6\n\x19\x45\x61syTornadoCommonResponse\x12\x0b\n\x03msg\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x05\x42\x43ZAgo.easyops.local/contracts/protorepo-models/easyops/model/monitorb\x06proto3')
)




_EASYTORNADOCOMMONRESPONSE = _descriptor.Descriptor(
  name='EasyTornadoCommonResponse',
  full_name='monitor.EasyTornadoCommonResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='monitor.EasyTornadoCommonResponse.msg', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='monitor.EasyTornadoCommonResponse.code', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=40,
  serialized_end=94,
)

DESCRIPTOR.message_types_by_name['EasyTornadoCommonResponse'] = _EASYTORNADOCOMMONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EasyTornadoCommonResponse = _reflection.GeneratedProtocolMessageType('EasyTornadoCommonResponse', (_message.Message,), {
  'DESCRIPTOR' : _EASYTORNADOCOMMONRESPONSE,
  '__module__' : 'easy_tornado_response_pb2'
  # @@protoc_insertion_point(class_scope:monitor.EasyTornadoCommonResponse)
  })
_sym_db.RegisterMessage(EasyTornadoCommonResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
