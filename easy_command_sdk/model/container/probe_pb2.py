# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: probe.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='probe.proto',
  package='container',
  syntax='proto3',
  serialized_options=_b('ZCgo.easyops.local/contracts/protorepo-models/easyops/model/container'),
  serialized_pb=_b('\n\x0bprobe.proto\x12\tcontainer\"\x83\x04\n\x05Probe\x12\x0c\n\x04type\x18\x01 \x01(\t\x12#\n\x04\x65xec\x18\x02 \x01(\x0b\x32\x15.container.Probe.Exec\x12)\n\x07httpGet\x18\x03 \x01(\x0b\x32\x18.container.Probe.HttpGet\x12-\n\ttcpSocket\x18\x04 \x01(\x0b\x32\x1a.container.Probe.TcpSocket\x12\x1b\n\x13initialDelaySeconds\x18\x05 \x01(\x05\x12\x16\n\x0etimeoutSeconds\x18\x06 \x01(\x05\x12\x15\n\rperiodSeconds\x18\x07 \x01(\x05\x12\x18\n\x10successThreshold\x18\x08 \x01(\x05\x12\x18\n\x10\x66\x61ilureThreshold\x18\t \x01(\x05\x1a\x17\n\x04\x45xec\x12\x0f\n\x07\x63ommand\x18\x01 \x03(\t\x1a\xaa\x01\n\x07HttpGet\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\x12\x0c\n\x04host\x18\x03 \x01(\t\x12\x0e\n\x06schema\x18\x04 \x01(\t\x12\x39\n\x0bhttpHeaders\x18\x05 \x03(\x0b\x32$.container.Probe.HttpGet.HttpHeaders\x1a*\n\x0bHttpHeaders\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x1a\'\n\tTcpSocket\x12\x0c\n\x04port\x18\x01 \x01(\x05\x12\x0c\n\x04host\x18\x02 \x01(\tBEZCgo.easyops.local/contracts/protorepo-models/easyops/model/containerb\x06proto3')
)




_PROBE_EXEC = _descriptor.Descriptor(
  name='Exec',
  full_name='container.Probe.Exec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='command', full_name='container.Probe.Exec.command', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=305,
  serialized_end=328,
)

_PROBE_HTTPGET_HTTPHEADERS = _descriptor.Descriptor(
  name='HttpHeaders',
  full_name='container.Probe.HttpGet.HttpHeaders',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='container.Probe.HttpGet.HttpHeaders.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='container.Probe.HttpGet.HttpHeaders.value', index=1,
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
  serialized_start=459,
  serialized_end=501,
)

_PROBE_HTTPGET = _descriptor.Descriptor(
  name='HttpGet',
  full_name='container.Probe.HttpGet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='container.Probe.HttpGet.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='container.Probe.HttpGet.port', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host', full_name='container.Probe.HttpGet.host', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='schema', full_name='container.Probe.HttpGet.schema', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='httpHeaders', full_name='container.Probe.HttpGet.httpHeaders', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PROBE_HTTPGET_HTTPHEADERS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=331,
  serialized_end=501,
)

_PROBE_TCPSOCKET = _descriptor.Descriptor(
  name='TcpSocket',
  full_name='container.Probe.TcpSocket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='port', full_name='container.Probe.TcpSocket.port', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host', full_name='container.Probe.TcpSocket.host', index=1,
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
  serialized_start=503,
  serialized_end=542,
)

_PROBE = _descriptor.Descriptor(
  name='Probe',
  full_name='container.Probe',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='container.Probe.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exec', full_name='container.Probe.exec', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='httpGet', full_name='container.Probe.httpGet', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tcpSocket', full_name='container.Probe.tcpSocket', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='initialDelaySeconds', full_name='container.Probe.initialDelaySeconds', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeoutSeconds', full_name='container.Probe.timeoutSeconds', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='periodSeconds', full_name='container.Probe.periodSeconds', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='successThreshold', full_name='container.Probe.successThreshold', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='failureThreshold', full_name='container.Probe.failureThreshold', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PROBE_EXEC, _PROBE_HTTPGET, _PROBE_TCPSOCKET, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=542,
)

_PROBE_EXEC.containing_type = _PROBE
_PROBE_HTTPGET_HTTPHEADERS.containing_type = _PROBE_HTTPGET
_PROBE_HTTPGET.fields_by_name['httpHeaders'].message_type = _PROBE_HTTPGET_HTTPHEADERS
_PROBE_HTTPGET.containing_type = _PROBE
_PROBE_TCPSOCKET.containing_type = _PROBE
_PROBE.fields_by_name['exec'].message_type = _PROBE_EXEC
_PROBE.fields_by_name['httpGet'].message_type = _PROBE_HTTPGET
_PROBE.fields_by_name['tcpSocket'].message_type = _PROBE_TCPSOCKET
DESCRIPTOR.message_types_by_name['Probe'] = _PROBE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Probe = _reflection.GeneratedProtocolMessageType('Probe', (_message.Message,), {

  'Exec' : _reflection.GeneratedProtocolMessageType('Exec', (_message.Message,), {
    'DESCRIPTOR' : _PROBE_EXEC,
    '__module__' : 'probe_pb2'
    # @@protoc_insertion_point(class_scope:container.Probe.Exec)
    })
  ,

  'HttpGet' : _reflection.GeneratedProtocolMessageType('HttpGet', (_message.Message,), {

    'HttpHeaders' : _reflection.GeneratedProtocolMessageType('HttpHeaders', (_message.Message,), {
      'DESCRIPTOR' : _PROBE_HTTPGET_HTTPHEADERS,
      '__module__' : 'probe_pb2'
      # @@protoc_insertion_point(class_scope:container.Probe.HttpGet.HttpHeaders)
      })
    ,
    'DESCRIPTOR' : _PROBE_HTTPGET,
    '__module__' : 'probe_pb2'
    # @@protoc_insertion_point(class_scope:container.Probe.HttpGet)
    })
  ,

  'TcpSocket' : _reflection.GeneratedProtocolMessageType('TcpSocket', (_message.Message,), {
    'DESCRIPTOR' : _PROBE_TCPSOCKET,
    '__module__' : 'probe_pb2'
    # @@protoc_insertion_point(class_scope:container.Probe.TcpSocket)
    })
  ,
  'DESCRIPTOR' : _PROBE,
  '__module__' : 'probe_pb2'
  # @@protoc_insertion_point(class_scope:container.Probe)
  })
_sym_db.RegisterMessage(Probe)
_sym_db.RegisterMessage(Probe.Exec)
_sym_db.RegisterMessage(Probe.HttpGet)
_sym_db.RegisterMessage(Probe.HttpGet.HttpHeaders)
_sym_db.RegisterMessage(Probe.TcpSocket)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
