# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_import.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from next_builder_sdk.model.cmdb import object_attr_value_pb2 as next__builder__sdk_dot_model_dot_cmdb_dot_object__attr__value__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='object_import.proto',
  package='cmdb',
  syntax='proto3',
  serialized_options=_b('Z>go.easyops.local/contracts/protorepo-models/easyops/model/cmdb'),
  serialized_pb=_b('\n\x13object_import.proto\x12\x04\x63mdb\x1a\x33next_builder_sdk/model/cmdb/object_attr_value.proto\"\xa0\x06\n\x0cObjectImport\x12\x10\n\x08objectId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04icon\x18\x03 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x04 \x01(\t\x12\x0c\n\x04memo\x18\x05 \x01(\t\x12-\n\x08\x61ttrList\x18\x06 \x03(\x0b\x32\x1b.cmdb.ObjectImport.AttrList\x12:\n\x0frelation_groups\x18\x07 \x03(\x0b\x32!.cmdb.ObjectImport.RelationGroups\x12\x36\n\rrelation_list\x18\x08 \x03(\x0b\x32\x1f.cmdb.ObjectImport.RelationList\x1a\xae\x01\n\x08\x41ttrList\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06unique\x18\x03 \x01(\t\x12\x10\n\x08readonly\x18\x04 \x01(\t\x12\x10\n\x08required\x18\x05 \x01(\t\x12\x0b\n\x03tag\x18\x06 \x03(\t\x12\x13\n\x0b\x64\x65scription\x18\x07 \x01(\t\x12\x0c\n\x04tips\x18\x08 \x01(\t\x12$\n\x05value\x18\t \x01(\x0b\x32\x15.cmdb.ObjectAttrValue\x1a*\n\x0eRelationGroups\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x1a\xc1\x02\n\x0cRelationList\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\x0eleft_object_id\x18\x02 \x01(\t\x12\x0f\n\x07left_id\x18\x03 \x01(\t\x12\x18\n\x10left_description\x18\x04 \x01(\t\x12\x10\n\x08left_min\x18\x05 \x01(\x05\x12\x10\n\x08left_max\x18\x06 \x01(\x05\x12\x13\n\x0bleft_groups\x18\x07 \x03(\t\x12\x11\n\tleft_tags\x18\x08 \x03(\t\x12\x17\n\x0fright_object_id\x18\t \x01(\t\x12\x10\n\x08right_id\x18\n \x01(\t\x12\x19\n\x11right_description\x18\x0b \x01(\t\x12\x11\n\tright_min\x18\x0c \x01(\x05\x12\x11\n\tright_max\x18\r \x01(\x05\x12\x14\n\x0cright_groups\x18\x0e \x03(\t\x12\x12\n\nright_tags\x18\x0f \x03(\tB@Z>go.easyops.local/contracts/protorepo-models/easyops/model/cmdbb\x06proto3')
  ,
  dependencies=[next__builder__sdk_dot_model_dot_cmdb_dot_object__attr__value__pb2.DESCRIPTOR,])




_OBJECTIMPORT_ATTRLIST = _descriptor.Descriptor(
  name='AttrList',
  full_name='cmdb.ObjectImport.AttrList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cmdb.ObjectImport.AttrList.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='cmdb.ObjectImport.AttrList.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unique', full_name='cmdb.ObjectImport.AttrList.unique', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readonly', full_name='cmdb.ObjectImport.AttrList.readonly', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='required', full_name='cmdb.ObjectImport.AttrList.required', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tag', full_name='cmdb.ObjectImport.AttrList.tag', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='cmdb.ObjectImport.AttrList.description', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tips', full_name='cmdb.ObjectImport.AttrList.tips', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='cmdb.ObjectImport.AttrList.value', index=8,
      number=9, type=11, cpp_type=10, label=1,
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
  serialized_start=341,
  serialized_end=515,
)

_OBJECTIMPORT_RELATIONGROUPS = _descriptor.Descriptor(
  name='RelationGroups',
  full_name='cmdb.ObjectImport.RelationGroups',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cmdb.ObjectImport.RelationGroups.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='cmdb.ObjectImport.RelationGroups.name', index=1,
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
  serialized_start=517,
  serialized_end=559,
)

_OBJECTIMPORT_RELATIONLIST = _descriptor.Descriptor(
  name='RelationList',
  full_name='cmdb.ObjectImport.RelationList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cmdb.ObjectImport.RelationList.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='left_object_id', full_name='cmdb.ObjectImport.RelationList.left_object_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='left_id', full_name='cmdb.ObjectImport.RelationList.left_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='left_description', full_name='cmdb.ObjectImport.RelationList.left_description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='left_min', full_name='cmdb.ObjectImport.RelationList.left_min', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='left_max', full_name='cmdb.ObjectImport.RelationList.left_max', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='left_groups', full_name='cmdb.ObjectImport.RelationList.left_groups', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='left_tags', full_name='cmdb.ObjectImport.RelationList.left_tags', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right_object_id', full_name='cmdb.ObjectImport.RelationList.right_object_id', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right_id', full_name='cmdb.ObjectImport.RelationList.right_id', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right_description', full_name='cmdb.ObjectImport.RelationList.right_description', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right_min', full_name='cmdb.ObjectImport.RelationList.right_min', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right_max', full_name='cmdb.ObjectImport.RelationList.right_max', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right_groups', full_name='cmdb.ObjectImport.RelationList.right_groups', index=13,
      number=14, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right_tags', full_name='cmdb.ObjectImport.RelationList.right_tags', index=14,
      number=15, type=9, cpp_type=9, label=3,
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
  serialized_start=562,
  serialized_end=883,
)

_OBJECTIMPORT = _descriptor.Descriptor(
  name='ObjectImport',
  full_name='cmdb.ObjectImport',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='objectId', full_name='cmdb.ObjectImport.objectId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='cmdb.ObjectImport.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon', full_name='cmdb.ObjectImport.icon', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='cmdb.ObjectImport.category', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='cmdb.ObjectImport.memo', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attrList', full_name='cmdb.ObjectImport.attrList', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relation_groups', full_name='cmdb.ObjectImport.relation_groups', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relation_list', full_name='cmdb.ObjectImport.relation_list', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_OBJECTIMPORT_ATTRLIST, _OBJECTIMPORT_RELATIONGROUPS, _OBJECTIMPORT_RELATIONLIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=83,
  serialized_end=883,
)

_OBJECTIMPORT_ATTRLIST.fields_by_name['value'].message_type = next__builder__sdk_dot_model_dot_cmdb_dot_object__attr__value__pb2._OBJECTATTRVALUE
_OBJECTIMPORT_ATTRLIST.containing_type = _OBJECTIMPORT
_OBJECTIMPORT_RELATIONGROUPS.containing_type = _OBJECTIMPORT
_OBJECTIMPORT_RELATIONLIST.containing_type = _OBJECTIMPORT
_OBJECTIMPORT.fields_by_name['attrList'].message_type = _OBJECTIMPORT_ATTRLIST
_OBJECTIMPORT.fields_by_name['relation_groups'].message_type = _OBJECTIMPORT_RELATIONGROUPS
_OBJECTIMPORT.fields_by_name['relation_list'].message_type = _OBJECTIMPORT_RELATIONLIST
DESCRIPTOR.message_types_by_name['ObjectImport'] = _OBJECTIMPORT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ObjectImport = _reflection.GeneratedProtocolMessageType('ObjectImport', (_message.Message,), {

  'AttrList' : _reflection.GeneratedProtocolMessageType('AttrList', (_message.Message,), {
    'DESCRIPTOR' : _OBJECTIMPORT_ATTRLIST,
    '__module__' : 'object_import_pb2'
    # @@protoc_insertion_point(class_scope:cmdb.ObjectImport.AttrList)
    })
  ,

  'RelationGroups' : _reflection.GeneratedProtocolMessageType('RelationGroups', (_message.Message,), {
    'DESCRIPTOR' : _OBJECTIMPORT_RELATIONGROUPS,
    '__module__' : 'object_import_pb2'
    # @@protoc_insertion_point(class_scope:cmdb.ObjectImport.RelationGroups)
    })
  ,

  'RelationList' : _reflection.GeneratedProtocolMessageType('RelationList', (_message.Message,), {
    'DESCRIPTOR' : _OBJECTIMPORT_RELATIONLIST,
    '__module__' : 'object_import_pb2'
    # @@protoc_insertion_point(class_scope:cmdb.ObjectImport.RelationList)
    })
  ,
  'DESCRIPTOR' : _OBJECTIMPORT,
  '__module__' : 'object_import_pb2'
  # @@protoc_insertion_point(class_scope:cmdb.ObjectImport)
  })
_sym_db.RegisterMessage(ObjectImport)
_sym_db.RegisterMessage(ObjectImport.AttrList)
_sym_db.RegisterMessage(ObjectImport.RelationGroups)
_sym_db.RegisterMessage(ObjectImport.RelationList)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
