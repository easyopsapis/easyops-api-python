# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cmdb_host_search.proto

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
  name='cmdb_host_search.proto',
  package='collector_center',
  syntax='proto3',
  serialized_options=_b('ZJgo.easyops.local/contracts/protorepo-models/easyops/model/collector_center'),
  serialized_pb=_b('\n\x16\x63mdb_host_search.proto\x12\x10\x63ollector_center\x1a\x1cgoogle/protobuf/struct.proto\"\xd3\x01\n\x0e\x43mdbHostSearch\x12\x10\n\x08objectId\x18\x01 \x01(\t\x12\x0f\n\x07querier\x18\x02 \x01(\t\x12\x0f\n\x07hostKey\x18\x03 \x01(\t\x12?\n\nconditions\x18\x04 \x03(\x0b\x32+.collector_center.CmdbHostSearch.Conditions\x1aL\n\nConditions\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\n\n\x02op\x18\x02 \x01(\t\x12%\n\x05value\x18\x03 \x01(\x0b\x32\x16.google.protobuf.ValueBLZJgo.easyops.local/contracts/protorepo-models/easyops/model/collector_centerb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_CMDBHOSTSEARCH_CONDITIONS = _descriptor.Descriptor(
  name='Conditions',
  full_name='collector_center.CmdbHostSearch.Conditions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='collector_center.CmdbHostSearch.Conditions.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='op', full_name='collector_center.CmdbHostSearch.Conditions.op', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='collector_center.CmdbHostSearch.Conditions.value', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=210,
  serialized_end=286,
)

_CMDBHOSTSEARCH = _descriptor.Descriptor(
  name='CmdbHostSearch',
  full_name='collector_center.CmdbHostSearch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='objectId', full_name='collector_center.CmdbHostSearch.objectId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='querier', full_name='collector_center.CmdbHostSearch.querier', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hostKey', full_name='collector_center.CmdbHostSearch.hostKey', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conditions', full_name='collector_center.CmdbHostSearch.conditions', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CMDBHOSTSEARCH_CONDITIONS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=75,
  serialized_end=286,
)

_CMDBHOSTSEARCH_CONDITIONS.fields_by_name['value'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_CMDBHOSTSEARCH_CONDITIONS.containing_type = _CMDBHOSTSEARCH
_CMDBHOSTSEARCH.fields_by_name['conditions'].message_type = _CMDBHOSTSEARCH_CONDITIONS
DESCRIPTOR.message_types_by_name['CmdbHostSearch'] = _CMDBHOSTSEARCH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CmdbHostSearch = _reflection.GeneratedProtocolMessageType('CmdbHostSearch', (_message.Message,), {

  'Conditions' : _reflection.GeneratedProtocolMessageType('Conditions', (_message.Message,), {
    'DESCRIPTOR' : _CMDBHOSTSEARCH_CONDITIONS,
    '__module__' : 'cmdb_host_search_pb2'
    # @@protoc_insertion_point(class_scope:collector_center.CmdbHostSearch.Conditions)
    })
  ,
  'DESCRIPTOR' : _CMDBHOSTSEARCH,
  '__module__' : 'cmdb_host_search_pb2'
  # @@protoc_insertion_point(class_scope:collector_center.CmdbHostSearch)
  })
_sym_db.RegisterMessage(CmdbHostSearch)
_sym_db.RegisterMessage(CmdbHostSearch.Conditions)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
