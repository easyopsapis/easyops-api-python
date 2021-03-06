# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cmdb_relation_search.proto

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
  name='cmdb_relation_search.proto',
  package='collector_center',
  syntax='proto3',
  serialized_options=_b('ZJgo.easyops.local/contracts/protorepo-models/easyops/model/collector_center'),
  serialized_pb=_b('\n\x1a\x63mdb_relation_search.proto\x12\x10\x63ollector_center\x1a\x1cgoogle/protobuf/struct.proto\"K\n\x12\x43mdbRelationSearch\x12\x0f\n\x07querier\x18\x01 \x01(\t\x12$\n\x04path\x18\x02 \x03(\x0b\x32\x16.google.protobuf.ValueBLZJgo.easyops.local/contracts/protorepo-models/easyops/model/collector_centerb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_CMDBRELATIONSEARCH = _descriptor.Descriptor(
  name='CmdbRelationSearch',
  full_name='collector_center.CmdbRelationSearch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='querier', full_name='collector_center.CmdbRelationSearch.querier', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='collector_center.CmdbRelationSearch.path', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=78,
  serialized_end=153,
)

_CMDBRELATIONSEARCH.fields_by_name['path'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
DESCRIPTOR.message_types_by_name['CmdbRelationSearch'] = _CMDBRELATIONSEARCH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CmdbRelationSearch = _reflection.GeneratedProtocolMessageType('CmdbRelationSearch', (_message.Message,), {
  'DESCRIPTOR' : _CMDBRELATIONSEARCH,
  '__module__' : 'cmdb_relation_search_pb2'
  # @@protoc_insertion_point(class_scope:collector_center.CmdbRelationSearch)
  })
_sym_db.RegisterMessage(CmdbRelationSearch)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
