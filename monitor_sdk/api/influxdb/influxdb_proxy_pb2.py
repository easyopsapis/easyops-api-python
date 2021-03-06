# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: influxdb_proxy.proto

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
  name='influxdb_proxy.proto',
  package='influxdb',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14influxdb_proxy.proto\x12\x08influxdb\x1a\x1cgoogle/protobuf/struct.proto\"<\n\x14InfluxdbProxyRequest\x12\n\n\x02\x64\x62\x18\x01 \x01(\t\x12\t\n\x01q\x18\x02 \x01(\t\x12\r\n\x05\x65poch\x18\x03 \x01(\t\"\xba\x02\n\x15InfluxdbProxyResponse\x12\x38\n\x07results\x18\x01 \x03(\x0b\x32\'.influxdb.InfluxdbProxyResponse.Results\x1a\xe6\x01\n\x07Results\x12>\n\x06series\x18\x01 \x03(\x0b\x32..influxdb.InfluxdbProxyResponse.Results.Series\x12\r\n\x05\x65rror\x18\x02 \x01(\t\x12\x14\n\x0cstatement_id\x18\x03 \x01(\x05\x1av\n\x06Series\x12&\n\x06values\x18\x01 \x01(\x0b\x32\x16.google.protobuf.Value\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07\x63olumns\x18\x03 \x03(\t\x12%\n\x04tags\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\"\x7f\n\x1cInfluxdbProxyResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12-\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1f.influxdb.InfluxdbProxyResponseb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_INFLUXDBPROXYREQUEST = _descriptor.Descriptor(
  name='InfluxdbProxyRequest',
  full_name='influxdb.InfluxdbProxyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='db', full_name='influxdb.InfluxdbProxyRequest.db', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='q', full_name='influxdb.InfluxdbProxyRequest.q', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='epoch', full_name='influxdb.InfluxdbProxyRequest.epoch', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=64,
  serialized_end=124,
)


_INFLUXDBPROXYRESPONSE_RESULTS_SERIES = _descriptor.Descriptor(
  name='Series',
  full_name='influxdb.InfluxdbProxyResponse.Results.Series',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='influxdb.InfluxdbProxyResponse.Results.Series.values', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='influxdb.InfluxdbProxyResponse.Results.Series.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='columns', full_name='influxdb.InfluxdbProxyResponse.Results.Series.columns', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='influxdb.InfluxdbProxyResponse.Results.Series.tags', index=3,
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
  serialized_start=323,
  serialized_end=441,
)

_INFLUXDBPROXYRESPONSE_RESULTS = _descriptor.Descriptor(
  name='Results',
  full_name='influxdb.InfluxdbProxyResponse.Results',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='series', full_name='influxdb.InfluxdbProxyResponse.Results.series', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='influxdb.InfluxdbProxyResponse.Results.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='statement_id', full_name='influxdb.InfluxdbProxyResponse.Results.statement_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_INFLUXDBPROXYRESPONSE_RESULTS_SERIES, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=211,
  serialized_end=441,
)

_INFLUXDBPROXYRESPONSE = _descriptor.Descriptor(
  name='InfluxdbProxyResponse',
  full_name='influxdb.InfluxdbProxyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='influxdb.InfluxdbProxyResponse.results', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_INFLUXDBPROXYRESPONSE_RESULTS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=127,
  serialized_end=441,
)


_INFLUXDBPROXYRESPONSEWRAPPER = _descriptor.Descriptor(
  name='InfluxdbProxyResponseWrapper',
  full_name='influxdb.InfluxdbProxyResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='influxdb.InfluxdbProxyResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='influxdb.InfluxdbProxyResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='influxdb.InfluxdbProxyResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='influxdb.InfluxdbProxyResponseWrapper.data', index=3,
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
  serialized_start=443,
  serialized_end=570,
)

_INFLUXDBPROXYRESPONSE_RESULTS_SERIES.fields_by_name['values'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_INFLUXDBPROXYRESPONSE_RESULTS_SERIES.fields_by_name['tags'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_INFLUXDBPROXYRESPONSE_RESULTS_SERIES.containing_type = _INFLUXDBPROXYRESPONSE_RESULTS
_INFLUXDBPROXYRESPONSE_RESULTS.fields_by_name['series'].message_type = _INFLUXDBPROXYRESPONSE_RESULTS_SERIES
_INFLUXDBPROXYRESPONSE_RESULTS.containing_type = _INFLUXDBPROXYRESPONSE
_INFLUXDBPROXYRESPONSE.fields_by_name['results'].message_type = _INFLUXDBPROXYRESPONSE_RESULTS
_INFLUXDBPROXYRESPONSEWRAPPER.fields_by_name['data'].message_type = _INFLUXDBPROXYRESPONSE
DESCRIPTOR.message_types_by_name['InfluxdbProxyRequest'] = _INFLUXDBPROXYREQUEST
DESCRIPTOR.message_types_by_name['InfluxdbProxyResponse'] = _INFLUXDBPROXYRESPONSE
DESCRIPTOR.message_types_by_name['InfluxdbProxyResponseWrapper'] = _INFLUXDBPROXYRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InfluxdbProxyRequest = _reflection.GeneratedProtocolMessageType('InfluxdbProxyRequest', (_message.Message,), {
  'DESCRIPTOR' : _INFLUXDBPROXYREQUEST,
  '__module__' : 'influxdb_proxy_pb2'
  # @@protoc_insertion_point(class_scope:influxdb.InfluxdbProxyRequest)
  })
_sym_db.RegisterMessage(InfluxdbProxyRequest)

InfluxdbProxyResponse = _reflection.GeneratedProtocolMessageType('InfluxdbProxyResponse', (_message.Message,), {

  'Results' : _reflection.GeneratedProtocolMessageType('Results', (_message.Message,), {

    'Series' : _reflection.GeneratedProtocolMessageType('Series', (_message.Message,), {
      'DESCRIPTOR' : _INFLUXDBPROXYRESPONSE_RESULTS_SERIES,
      '__module__' : 'influxdb_proxy_pb2'
      # @@protoc_insertion_point(class_scope:influxdb.InfluxdbProxyResponse.Results.Series)
      })
    ,
    'DESCRIPTOR' : _INFLUXDBPROXYRESPONSE_RESULTS,
    '__module__' : 'influxdb_proxy_pb2'
    # @@protoc_insertion_point(class_scope:influxdb.InfluxdbProxyResponse.Results)
    })
  ,
  'DESCRIPTOR' : _INFLUXDBPROXYRESPONSE,
  '__module__' : 'influxdb_proxy_pb2'
  # @@protoc_insertion_point(class_scope:influxdb.InfluxdbProxyResponse)
  })
_sym_db.RegisterMessage(InfluxdbProxyResponse)
_sym_db.RegisterMessage(InfluxdbProxyResponse.Results)
_sym_db.RegisterMessage(InfluxdbProxyResponse.Results.Series)

InfluxdbProxyResponseWrapper = _reflection.GeneratedProtocolMessageType('InfluxdbProxyResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _INFLUXDBPROXYRESPONSEWRAPPER,
  '__module__' : 'influxdb_proxy_pb2'
  # @@protoc_insertion_point(class_scope:influxdb.InfluxdbProxyResponseWrapper)
  })
_sym_db.RegisterMessage(InfluxdbProxyResponseWrapper)


# @@protoc_insertion_point(module_scope)
