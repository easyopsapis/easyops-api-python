# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: instance_relation_pair.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='instance_relation_pair.proto',
  package='cmdb',
  syntax='proto3',
  serialized_options=_b('Z>go.easyops.local/contracts/protorepo-models/easyops/model/cmdb'),
  serialized_pb=_b('\n\x1cinstance_relation_pair.proto\x12\x04\x63mdb\"K\n\x14InstanceRelationPair\x12\x18\n\x10left_instance_id\x18\x01 \x01(\t\x12\x19\n\x11right_instance_id\x18\x02 \x01(\tB@Z>go.easyops.local/contracts/protorepo-models/easyops/model/cmdbb\x06proto3')
)




_INSTANCERELATIONPAIR = _descriptor.Descriptor(
  name='InstanceRelationPair',
  full_name='cmdb.InstanceRelationPair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='left_instance_id', full_name='cmdb.InstanceRelationPair.left_instance_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right_instance_id', full_name='cmdb.InstanceRelationPair.right_instance_id', index=1,
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
  serialized_start=38,
  serialized_end=113,
)

DESCRIPTOR.message_types_by_name['InstanceRelationPair'] = _INSTANCERELATIONPAIR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InstanceRelationPair = _reflection.GeneratedProtocolMessageType('InstanceRelationPair', (_message.Message,), {
  'DESCRIPTOR' : _INSTANCERELATIONPAIR,
  '__module__' : 'instance_relation_pair_pb2'
  # @@protoc_insertion_point(class_scope:cmdb.InstanceRelationPair)
  })
_sym_db.RegisterMessage(InstanceRelationPair)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)