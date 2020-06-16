# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: strategy_path_node_basic.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='strategy_path_node_basic.proto',
  package='cmdb',
  syntax='proto3',
  serialized_options=_b('Z>go.easyops.local/contracts/protorepo-models/easyops/model/cmdb'),
  serialized_pb=_b('\n\x1estrategy_path_node_basic.proto\x12\x04\x63mdb\"\x89\x01\n\x15StrategyPathNodeBasic\x12\x10\n\x08objectId\x18\x01 \x01(\t\x12\x13\n\x0bobject_name\x18\x02 \x01(\t\x12\x13\n\x0brelation_id\x18\x03 \x01(\t\x12\x18\n\x10relation_side_id\x18\x04 \x01(\t\x12\x1a\n\x12relation_side_name\x18\x05 \x01(\tB@Z>go.easyops.local/contracts/protorepo-models/easyops/model/cmdbb\x06proto3')
)




_STRATEGYPATHNODEBASIC = _descriptor.Descriptor(
  name='StrategyPathNodeBasic',
  full_name='cmdb.StrategyPathNodeBasic',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='objectId', full_name='cmdb.StrategyPathNodeBasic.objectId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object_name', full_name='cmdb.StrategyPathNodeBasic.object_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relation_id', full_name='cmdb.StrategyPathNodeBasic.relation_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relation_side_id', full_name='cmdb.StrategyPathNodeBasic.relation_side_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relation_side_name', full_name='cmdb.StrategyPathNodeBasic.relation_side_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=41,
  serialized_end=178,
)

DESCRIPTOR.message_types_by_name['StrategyPathNodeBasic'] = _STRATEGYPATHNODEBASIC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StrategyPathNodeBasic = _reflection.GeneratedProtocolMessageType('StrategyPathNodeBasic', (_message.Message,), {
  'DESCRIPTOR' : _STRATEGYPATHNODEBASIC,
  '__module__' : 'strategy_path_node_basic_pb2'
  # @@protoc_insertion_point(class_scope:cmdb.StrategyPathNodeBasic)
  })
_sym_db.RegisterMessage(StrategyPathNodeBasic)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
