# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_object_snapshot.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cmdb_sdk.model.cmdb import object_attr_pb2 as cmdb__sdk_dot_model_dot_cmdb_dot_object__attr__pb2
from cmdb_sdk.model.cmdb import object_relation_pb2 as cmdb__sdk_dot_model_dot_cmdb_dot_object__relation__pb2
from cmdb_sdk.model.cmdb import object_relation_group_pb2 as cmdb__sdk_dot_model_dot_cmdb_dot_object__relation__group__pb2
from cmdb_sdk.model.cmdb import object_index_pb2 as cmdb__sdk_dot_model_dot_cmdb_dot_object__index__pb2
from cmdb_sdk.model.cmdb import object_view_pb2 as cmdb__sdk_dot_model_dot_cmdb_dot_object__view__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_object_snapshot.proto',
  package='cmdb_object',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x19get_object_snapshot.proto\x12\x0b\x63mdb_object\x1a%cmdb_sdk/model/cmdb/object_attr.proto\x1a)cmdb_sdk/model/cmdb/object_relation.proto\x1a/cmdb_sdk/model/cmdb/object_relation_group.proto\x1a&cmdb_sdk/model/cmdb/object_index.proto\x1a%cmdb_sdk/model/cmdb/object_view.proto\"<\n\x15ObjectSnapshotRequest\x12\x11\n\tobject_id\x18\x01 \x01(\t\x12\x10\n\x08_version\x18\x02 \x01(\x05\"\xd6\x04\n\x16ObjectSnapshotResponse\x12\x0b\n\x03_id\x18\x01 \x01(\t\x12\"\n\x08\x61ttrList\x18\x02 \x03(\x0b\x32\x10.cmdb.ObjectAttr\x12+\n\rrelation_list\x18\x03 \x03(\x0b\x32\x14.cmdb.ObjectRelation\x12\x32\n\x0frelation_groups\x18\x04 \x03(\x0b\x32\x19.cmdb.ObjectRelationGroup\x12$\n\tindexList\x18\x05 \x03(\x0b\x32\x11.cmdb.ObjectIndex\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x10\n\x08objectId\x18\x07 \x01(\t\x12\x0c\n\x04memo\x18\x08 \x01(\t\x12\x1e\n\x04view\x18\t \x01(\x0b\x32\x10.cmdb.ObjectView\x12\x11\n\tprotected\x18\n \x01(\x08\x12\x17\n\x0fwordIndexDenied\x18\x0b \x01(\x08\x12\x10\n\x08\x63\x61tegory\x18\x0c \x01(\t\x12\x0c\n\x04icon\x18\r \x01(\t\x12\x0e\n\x06system\x18\x0e \x01(\t\x12\r\n\x05\x63time\x18\x0f \x01(\t\x12\r\n\x05mtime\x18\x10 \x01(\t\x12\x0f\n\x07\x63reator\x18\x11 \x01(\t\x12\x10\n\x08modifier\x18\x12 \x01(\t\x12\x0b\n\x03_ts\x18\x13 \x01(\x05\x12\x10\n\x08_version\x18\x14 \x01(\x05\x12\x19\n\x11updateAuthorizers\x18\x15 \x03(\t\x12\x19\n\x11\x64\x65leteAuthorizers\x18\x16 \x03(\t\x12\x12\n\nisAbstract\x18\x17 \x01(\x08\x12\x16\n\x0eparentObjectId\x18\x18 \x01(\t\x12\x18\n\x10permissionDenied\x18\x19 \x01(\x08\"\x84\x01\n\x1dObjectSnapshotResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x31\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32#.cmdb_object.ObjectSnapshotResponseb\x06proto3')
  ,
  dependencies=[cmdb__sdk_dot_model_dot_cmdb_dot_object__attr__pb2.DESCRIPTOR,cmdb__sdk_dot_model_dot_cmdb_dot_object__relation__pb2.DESCRIPTOR,cmdb__sdk_dot_model_dot_cmdb_dot_object__relation__group__pb2.DESCRIPTOR,cmdb__sdk_dot_model_dot_cmdb_dot_object__index__pb2.DESCRIPTOR,cmdb__sdk_dot_model_dot_cmdb_dot_object__view__pb2.DESCRIPTOR,])




_OBJECTSNAPSHOTREQUEST = _descriptor.Descriptor(
  name='ObjectSnapshotRequest',
  full_name='cmdb_object.ObjectSnapshotRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_id', full_name='cmdb_object.ObjectSnapshotRequest.object_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='_version', full_name='cmdb_object.ObjectSnapshotRequest._version', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=252,
  serialized_end=312,
)


_OBJECTSNAPSHOTRESPONSE = _descriptor.Descriptor(
  name='ObjectSnapshotResponse',
  full_name='cmdb_object.ObjectSnapshotResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='_id', full_name='cmdb_object.ObjectSnapshotResponse._id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attrList', full_name='cmdb_object.ObjectSnapshotResponse.attrList', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relation_list', full_name='cmdb_object.ObjectSnapshotResponse.relation_list', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relation_groups', full_name='cmdb_object.ObjectSnapshotResponse.relation_groups', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='indexList', full_name='cmdb_object.ObjectSnapshotResponse.indexList', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='cmdb_object.ObjectSnapshotResponse.name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectId', full_name='cmdb_object.ObjectSnapshotResponse.objectId', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='cmdb_object.ObjectSnapshotResponse.memo', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='view', full_name='cmdb_object.ObjectSnapshotResponse.view', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='protected', full_name='cmdb_object.ObjectSnapshotResponse.protected', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wordIndexDenied', full_name='cmdb_object.ObjectSnapshotResponse.wordIndexDenied', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='cmdb_object.ObjectSnapshotResponse.category', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon', full_name='cmdb_object.ObjectSnapshotResponse.icon', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='system', full_name='cmdb_object.ObjectSnapshotResponse.system', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='cmdb_object.ObjectSnapshotResponse.ctime', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='cmdb_object.ObjectSnapshotResponse.mtime', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='cmdb_object.ObjectSnapshotResponse.creator', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='modifier', full_name='cmdb_object.ObjectSnapshotResponse.modifier', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='_ts', full_name='cmdb_object.ObjectSnapshotResponse._ts', index=18,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='_version', full_name='cmdb_object.ObjectSnapshotResponse._version', index=19,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updateAuthorizers', full_name='cmdb_object.ObjectSnapshotResponse.updateAuthorizers', index=20,
      number=21, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deleteAuthorizers', full_name='cmdb_object.ObjectSnapshotResponse.deleteAuthorizers', index=21,
      number=22, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isAbstract', full_name='cmdb_object.ObjectSnapshotResponse.isAbstract', index=22,
      number=23, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parentObjectId', full_name='cmdb_object.ObjectSnapshotResponse.parentObjectId', index=23,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='permissionDenied', full_name='cmdb_object.ObjectSnapshotResponse.permissionDenied', index=24,
      number=25, type=8, cpp_type=7, label=1,
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
  serialized_start=315,
  serialized_end=913,
)


_OBJECTSNAPSHOTRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ObjectSnapshotResponseWrapper',
  full_name='cmdb_object.ObjectSnapshotResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='cmdb_object.ObjectSnapshotResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='cmdb_object.ObjectSnapshotResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='cmdb_object.ObjectSnapshotResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='cmdb_object.ObjectSnapshotResponseWrapper.data', index=3,
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
  serialized_start=916,
  serialized_end=1048,
)

_OBJECTSNAPSHOTRESPONSE.fields_by_name['attrList'].message_type = cmdb__sdk_dot_model_dot_cmdb_dot_object__attr__pb2._OBJECTATTR
_OBJECTSNAPSHOTRESPONSE.fields_by_name['relation_list'].message_type = cmdb__sdk_dot_model_dot_cmdb_dot_object__relation__pb2._OBJECTRELATION
_OBJECTSNAPSHOTRESPONSE.fields_by_name['relation_groups'].message_type = cmdb__sdk_dot_model_dot_cmdb_dot_object__relation__group__pb2._OBJECTRELATIONGROUP
_OBJECTSNAPSHOTRESPONSE.fields_by_name['indexList'].message_type = cmdb__sdk_dot_model_dot_cmdb_dot_object__index__pb2._OBJECTINDEX
_OBJECTSNAPSHOTRESPONSE.fields_by_name['view'].message_type = cmdb__sdk_dot_model_dot_cmdb_dot_object__view__pb2._OBJECTVIEW
_OBJECTSNAPSHOTRESPONSEWRAPPER.fields_by_name['data'].message_type = _OBJECTSNAPSHOTRESPONSE
DESCRIPTOR.message_types_by_name['ObjectSnapshotRequest'] = _OBJECTSNAPSHOTREQUEST
DESCRIPTOR.message_types_by_name['ObjectSnapshotResponse'] = _OBJECTSNAPSHOTRESPONSE
DESCRIPTOR.message_types_by_name['ObjectSnapshotResponseWrapper'] = _OBJECTSNAPSHOTRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ObjectSnapshotRequest = _reflection.GeneratedProtocolMessageType('ObjectSnapshotRequest', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTSNAPSHOTREQUEST,
  '__module__' : 'get_object_snapshot_pb2'
  # @@protoc_insertion_point(class_scope:cmdb_object.ObjectSnapshotRequest)
  })
_sym_db.RegisterMessage(ObjectSnapshotRequest)

ObjectSnapshotResponse = _reflection.GeneratedProtocolMessageType('ObjectSnapshotResponse', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTSNAPSHOTRESPONSE,
  '__module__' : 'get_object_snapshot_pb2'
  # @@protoc_insertion_point(class_scope:cmdb_object.ObjectSnapshotResponse)
  })
_sym_db.RegisterMessage(ObjectSnapshotResponse)

ObjectSnapshotResponseWrapper = _reflection.GeneratedProtocolMessageType('ObjectSnapshotResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTSNAPSHOTRESPONSEWRAPPER,
  '__module__' : 'get_object_snapshot_pb2'
  # @@protoc_insertion_point(class_scope:cmdb_object.ObjectSnapshotResponseWrapper)
  })
_sym_db.RegisterMessage(ObjectSnapshotResponseWrapper)


# @@protoc_insertion_point(module_scope)
