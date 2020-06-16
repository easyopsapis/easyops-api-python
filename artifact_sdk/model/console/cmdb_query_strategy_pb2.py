# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cmdb_query_strategy.proto

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
  name='cmdb_query_strategy.proto',
  package='console',
  syntax='proto3',
  serialized_options=_b('ZAgo.easyops.local/contracts/protorepo-models/easyops/model/console'),
  serialized_pb=_b('\n\x19\x63mdb_query_strategy.proto\x12\x07\x63onsole\x1a\x1cgoogle/protobuf/struct.proto\"\xdf\x01\n\x11\x43mdbQueryStrategy\x12\x10\n\x08objectId\x18\x01 \x01(\t\x12\x37\n\tinstances\x18\x02 \x01(\x0b\x32$.console.CmdbQueryStrategy.Instances\x12\'\n\x06\x66ields\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x1aV\n\tInstances\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x13\n\x0binstanceIds\x18\x02 \x03(\t\x12&\n\x05query\x18\x03 \x01(\x0b\x32\x17.google.protobuf.StructBCZAgo.easyops.local/contracts/protorepo-models/easyops/model/consoleb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_CMDBQUERYSTRATEGY_INSTANCES = _descriptor.Descriptor(
  name='Instances',
  full_name='console.CmdbQueryStrategy.Instances',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='console.CmdbQueryStrategy.Instances.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceIds', full_name='console.CmdbQueryStrategy.Instances.instanceIds', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='query', full_name='console.CmdbQueryStrategy.Instances.query', index=2,
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
  serialized_start=206,
  serialized_end=292,
)

_CMDBQUERYSTRATEGY = _descriptor.Descriptor(
  name='CmdbQueryStrategy',
  full_name='console.CmdbQueryStrategy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='objectId', full_name='console.CmdbQueryStrategy.objectId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instances', full_name='console.CmdbQueryStrategy.instances', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fields', full_name='console.CmdbQueryStrategy.fields', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CMDBQUERYSTRATEGY_INSTANCES, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=292,
)

_CMDBQUERYSTRATEGY_INSTANCES.fields_by_name['query'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_CMDBQUERYSTRATEGY_INSTANCES.containing_type = _CMDBQUERYSTRATEGY
_CMDBQUERYSTRATEGY.fields_by_name['instances'].message_type = _CMDBQUERYSTRATEGY_INSTANCES
_CMDBQUERYSTRATEGY.fields_by_name['fields'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['CmdbQueryStrategy'] = _CMDBQUERYSTRATEGY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CmdbQueryStrategy = _reflection.GeneratedProtocolMessageType('CmdbQueryStrategy', (_message.Message,), {

  'Instances' : _reflection.GeneratedProtocolMessageType('Instances', (_message.Message,), {
    'DESCRIPTOR' : _CMDBQUERYSTRATEGY_INSTANCES,
    '__module__' : 'cmdb_query_strategy_pb2'
    # @@protoc_insertion_point(class_scope:console.CmdbQueryStrategy.Instances)
    })
  ,
  'DESCRIPTOR' : _CMDBQUERYSTRATEGY,
  '__module__' : 'cmdb_query_strategy_pb2'
  # @@protoc_insertion_point(class_scope:console.CmdbQueryStrategy)
  })
_sym_db.RegisterMessage(CmdbQueryStrategy)
_sym_db.RegisterMessage(CmdbQueryStrategy.Instances)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)