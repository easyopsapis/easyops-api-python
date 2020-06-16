# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_relation.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='object_relation.proto',
  package='cmdb',
  syntax='proto3',
  serialized_options=_b('Z>go.easyops.local/contracts/protorepo-models/easyops/model/cmdb'),
  serialized_pb=_b('\n\x15object_relation.proto\x12\x04\x63mdb\"\xe4\x03\n\x0eObjectRelation\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tprotected\x18\x02 \x01(\x08\x12\x13\n\x0brelation_id\x18\x03 \x01(\t\x12\x10\n\x08right_id\x18\x04 \x01(\t\x12\x12\n\nright_name\x18\x05 \x01(\t\x12\x19\n\x11right_description\x18\x06 \x01(\t\x12\x14\n\x0cright_groups\x18\x07 \x03(\t\x12\x12\n\nright_tags\x18\x08 \x03(\t\x12\x11\n\tright_max\x18\t \x01(\x05\x12\x11\n\tright_min\x18\n \x01(\x05\x12\x17\n\x0fright_object_id\x18\x0b \x01(\t\x12\x0f\n\x07left_id\x18\x0c \x01(\t\x12\x11\n\tleft_name\x18\r \x01(\t\x12\x18\n\x10left_description\x18\x0e \x01(\t\x12\x13\n\x0bleft_groups\x18\x0f \x03(\t\x12\x11\n\tleft_tags\x18\x10 \x03(\t\x12\x10\n\x08left_max\x18\x11 \x01(\x05\x12\x10\n\x08left_min\x18\x12 \x01(\x05\x12\x16\n\x0eleft_object_id\x18\x13 \x01(\t\x12\x0f\n\x07\x63reator\x18\x14 \x01(\t\x12\r\n\x05\x63time\x18\x15 \x01(\t\x12\x0b\n\x03_ts\x18\x16 \x01(\x05\x12\x10\n\x08_version\x18\x17 \x01(\x05\x12\x11\n\tisInherit\x18\x18 \x01(\x08\x42@Z>go.easyops.local/contracts/protorepo-models/easyops/model/cmdbb\x06proto3')
)




_OBJECTRELATION = _descriptor.Descriptor(
  name='ObjectRelation',
  full_name='cmdb.ObjectRelation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cmdb.ObjectRelation.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='protected', full_name='cmdb.ObjectRelation.protected', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relation_id', full_name='cmdb.ObjectRelation.relation_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right_id', full_name='cmdb.ObjectRelation.right_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right_name', full_name='cmdb.ObjectRelation.right_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right_description', full_name='cmdb.ObjectRelation.right_description', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right_groups', full_name='cmdb.ObjectRelation.right_groups', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right_tags', full_name='cmdb.ObjectRelation.right_tags', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right_max', full_name='cmdb.ObjectRelation.right_max', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right_min', full_name='cmdb.ObjectRelation.right_min', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right_object_id', full_name='cmdb.ObjectRelation.right_object_id', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='left_id', full_name='cmdb.ObjectRelation.left_id', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='left_name', full_name='cmdb.ObjectRelation.left_name', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='left_description', full_name='cmdb.ObjectRelation.left_description', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='left_groups', full_name='cmdb.ObjectRelation.left_groups', index=14,
      number=15, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='left_tags', full_name='cmdb.ObjectRelation.left_tags', index=15,
      number=16, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='left_max', full_name='cmdb.ObjectRelation.left_max', index=16,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='left_min', full_name='cmdb.ObjectRelation.left_min', index=17,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='left_object_id', full_name='cmdb.ObjectRelation.left_object_id', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='cmdb.ObjectRelation.creator', index=19,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='cmdb.ObjectRelation.ctime', index=20,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='_ts', full_name='cmdb.ObjectRelation._ts', index=21,
      number=22, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='_version', full_name='cmdb.ObjectRelation._version', index=22,
      number=23, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isInherit', full_name='cmdb.ObjectRelation.isInherit', index=23,
      number=24, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=32,
  serialized_end=516,
)

DESCRIPTOR.message_types_by_name['ObjectRelation'] = _OBJECTRELATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ObjectRelation = _reflection.GeneratedProtocolMessageType('ObjectRelation', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTRELATION,
  '__module__' : 'object_relation_pb2'
  # @@protoc_insertion_point(class_scope:cmdb.ObjectRelation)
  })
_sym_db.RegisterMessage(ObjectRelation)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)