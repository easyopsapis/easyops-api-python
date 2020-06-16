# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cmdb_object.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flowable_service_sdk.model.cmdb import object_attr_pb2 as flowable__service__sdk_dot_model_dot_cmdb_dot_object__attr__pb2
from flowable_service_sdk.model.cmdb import object_relation_pb2 as flowable__service__sdk_dot_model_dot_cmdb_dot_object__relation__pb2
from flowable_service_sdk.model.cmdb import object_relation_group_pb2 as flowable__service__sdk_dot_model_dot_cmdb_dot_object__relation__group__pb2
from flowable_service_sdk.model.cmdb import object_index_pb2 as flowable__service__sdk_dot_model_dot_cmdb_dot_object__index__pb2
from flowable_service_sdk.model.cmdb import object_view_pb2 as flowable__service__sdk_dot_model_dot_cmdb_dot_object__view__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cmdb_object.proto',
  package='cmdb',
  syntax='proto3',
  serialized_options=_b('Z>go.easyops.local/contracts/protorepo-models/easyops/model/cmdb'),
  serialized_pb=_b('\n\x11\x63mdb_object.proto\x12\x04\x63mdb\x1a\x31\x66lowable_service_sdk/model/cmdb/object_attr.proto\x1a\x35\x66lowable_service_sdk/model/cmdb/object_relation.proto\x1a;flowable_service_sdk/model/cmdb/object_relation_group.proto\x1a\x32\x66lowable_service_sdk/model/cmdb/object_index.proto\x1a\x31\x66lowable_service_sdk/model/cmdb/object_view.proto\"\xbd\x04\n\nCmdbObject\x12\"\n\x08\x61ttrList\x18\x01 \x03(\x0b\x32\x10.cmdb.ObjectAttr\x12+\n\rrelation_list\x18\x02 \x03(\x0b\x32\x14.cmdb.ObjectRelation\x12\x32\n\x0frelation_groups\x18\x03 \x03(\x0b\x32\x19.cmdb.ObjectRelationGroup\x12$\n\tindexList\x18\x04 \x03(\x0b\x32\x11.cmdb.ObjectIndex\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x10\n\x08objectId\x18\x06 \x01(\t\x12\x0c\n\x04memo\x18\x07 \x01(\t\x12\x1e\n\x04view\x18\x08 \x01(\x0b\x32\x10.cmdb.ObjectView\x12\x11\n\tprotected\x18\t \x01(\x08\x12\x17\n\x0fwordIndexDenied\x18\n \x01(\x08\x12\x10\n\x08\x63\x61tegory\x18\x0b \x01(\t\x12\x0c\n\x04icon\x18\x0c \x01(\t\x12\x0e\n\x06system\x18\r \x01(\t\x12\r\n\x05\x63time\x18\x0e \x01(\t\x12\r\n\x05mtime\x18\x0f \x01(\t\x12\x0f\n\x07\x63reator\x18\x10 \x01(\t\x12\x10\n\x08modifier\x18\x11 \x01(\t\x12\x0b\n\x03_ts\x18\x12 \x01(\x05\x12\x10\n\x08_version\x18\x13 \x01(\x05\x12\x19\n\x11updateAuthorizers\x18\x14 \x03(\t\x12\x19\n\x11\x64\x65leteAuthorizers\x18\x15 \x03(\t\x12\x12\n\nisAbstract\x18\x16 \x01(\x08\x12\x16\n\x0eparentObjectId\x18\x17 \x01(\t\x12\x18\n\x10permissionDenied\x18\x18 \x01(\x08\x42@Z>go.easyops.local/contracts/protorepo-models/easyops/model/cmdbb\x06proto3')
  ,
  dependencies=[flowable__service__sdk_dot_model_dot_cmdb_dot_object__attr__pb2.DESCRIPTOR,flowable__service__sdk_dot_model_dot_cmdb_dot_object__relation__pb2.DESCRIPTOR,flowable__service__sdk_dot_model_dot_cmdb_dot_object__relation__group__pb2.DESCRIPTOR,flowable__service__sdk_dot_model_dot_cmdb_dot_object__index__pb2.DESCRIPTOR,flowable__service__sdk_dot_model_dot_cmdb_dot_object__view__pb2.DESCRIPTOR,])




_CMDBOBJECT = _descriptor.Descriptor(
  name='CmdbObject',
  full_name='cmdb.CmdbObject',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='attrList', full_name='cmdb.CmdbObject.attrList', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relation_list', full_name='cmdb.CmdbObject.relation_list', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relation_groups', full_name='cmdb.CmdbObject.relation_groups', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='indexList', full_name='cmdb.CmdbObject.indexList', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='cmdb.CmdbObject.name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectId', full_name='cmdb.CmdbObject.objectId', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='cmdb.CmdbObject.memo', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='view', full_name='cmdb.CmdbObject.view', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='protected', full_name='cmdb.CmdbObject.protected', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wordIndexDenied', full_name='cmdb.CmdbObject.wordIndexDenied', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='cmdb.CmdbObject.category', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon', full_name='cmdb.CmdbObject.icon', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='system', full_name='cmdb.CmdbObject.system', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='cmdb.CmdbObject.ctime', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='cmdb.CmdbObject.mtime', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='cmdb.CmdbObject.creator', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='modifier', full_name='cmdb.CmdbObject.modifier', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='_ts', full_name='cmdb.CmdbObject._ts', index=17,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='_version', full_name='cmdb.CmdbObject._version', index=18,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updateAuthorizers', full_name='cmdb.CmdbObject.updateAuthorizers', index=19,
      number=20, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deleteAuthorizers', full_name='cmdb.CmdbObject.deleteAuthorizers', index=20,
      number=21, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isAbstract', full_name='cmdb.CmdbObject.isAbstract', index=21,
      number=22, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parentObjectId', full_name='cmdb.CmdbObject.parentObjectId', index=22,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='permissionDenied', full_name='cmdb.CmdbObject.permissionDenied', index=23,
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
  serialized_start=298,
  serialized_end=871,
)

_CMDBOBJECT.fields_by_name['attrList'].message_type = flowable__service__sdk_dot_model_dot_cmdb_dot_object__attr__pb2._OBJECTATTR
_CMDBOBJECT.fields_by_name['relation_list'].message_type = flowable__service__sdk_dot_model_dot_cmdb_dot_object__relation__pb2._OBJECTRELATION
_CMDBOBJECT.fields_by_name['relation_groups'].message_type = flowable__service__sdk_dot_model_dot_cmdb_dot_object__relation__group__pb2._OBJECTRELATIONGROUP
_CMDBOBJECT.fields_by_name['indexList'].message_type = flowable__service__sdk_dot_model_dot_cmdb_dot_object__index__pb2._OBJECTINDEX
_CMDBOBJECT.fields_by_name['view'].message_type = flowable__service__sdk_dot_model_dot_cmdb_dot_object__view__pb2._OBJECTVIEW
DESCRIPTOR.message_types_by_name['CmdbObject'] = _CMDBOBJECT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CmdbObject = _reflection.GeneratedProtocolMessageType('CmdbObject', (_message.Message,), {
  'DESCRIPTOR' : _CMDBOBJECT,
  '__module__' : 'cmdb_object_pb2'
  # @@protoc_insertion_point(class_scope:cmdb.CmdbObject)
  })
_sym_db.RegisterMessage(CmdbObject)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
