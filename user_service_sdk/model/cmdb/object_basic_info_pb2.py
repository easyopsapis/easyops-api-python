# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_basic_info.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from user_service_sdk.model.cmdb import object_view_pb2 as user__service__sdk_dot_model_dot_cmdb_dot_object__view__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='object_basic_info.proto',
  package='cmdb',
  syntax='proto3',
  serialized_options=_b('Z>go.easyops.local/contracts/protorepo-models/easyops/model/cmdb'),
  serialized_pb=_b('\n\x17object_basic_info.proto\x12\x04\x63mdb\x1a-user_service_sdk/model/cmdb/object_view.proto\"\x97\x03\n\x0fObjectBasicInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08objectId\x18\x02 \x01(\t\x12\x0c\n\x04memo\x18\x03 \x01(\t\x12\x1e\n\x04view\x18\x04 \x01(\x0b\x32\x10.cmdb.ObjectView\x12\x11\n\tprotected\x18\x05 \x01(\x08\x12\x17\n\x0fwordIndexDenied\x18\x06 \x01(\x08\x12\x10\n\x08\x63\x61tegory\x18\x07 \x01(\t\x12\x0c\n\x04icon\x18\x08 \x01(\t\x12\x0e\n\x06system\x18\t \x01(\t\x12\r\n\x05\x63time\x18\n \x01(\t\x12\r\n\x05mtime\x18\x0b \x01(\t\x12\x0f\n\x07\x63reator\x18\x0c \x01(\t\x12\x10\n\x08modifier\x18\r \x01(\t\x12\x0b\n\x03_ts\x18\x0e \x01(\x05\x12\x10\n\x08_version\x18\x0f \x01(\x05\x12\x19\n\x11updateAuthorizers\x18\x10 \x03(\t\x12\x19\n\x11\x64\x65leteAuthorizers\x18\x11 \x03(\t\x12\x12\n\nisAbstract\x18\x12 \x01(\x08\x12\x16\n\x0eparentObjectId\x18\x13 \x01(\t\x12\x18\n\x10permissionDenied\x18\x14 \x01(\x08\x42@Z>go.easyops.local/contracts/protorepo-models/easyops/model/cmdbb\x06proto3')
  ,
  dependencies=[user__service__sdk_dot_model_dot_cmdb_dot_object__view__pb2.DESCRIPTOR,])




_OBJECTBASICINFO = _descriptor.Descriptor(
  name='ObjectBasicInfo',
  full_name='cmdb.ObjectBasicInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cmdb.ObjectBasicInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectId', full_name='cmdb.ObjectBasicInfo.objectId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='cmdb.ObjectBasicInfo.memo', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='view', full_name='cmdb.ObjectBasicInfo.view', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='protected', full_name='cmdb.ObjectBasicInfo.protected', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wordIndexDenied', full_name='cmdb.ObjectBasicInfo.wordIndexDenied', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='cmdb.ObjectBasicInfo.category', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon', full_name='cmdb.ObjectBasicInfo.icon', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='system', full_name='cmdb.ObjectBasicInfo.system', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='cmdb.ObjectBasicInfo.ctime', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='cmdb.ObjectBasicInfo.mtime', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='cmdb.ObjectBasicInfo.creator', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='modifier', full_name='cmdb.ObjectBasicInfo.modifier', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='_ts', full_name='cmdb.ObjectBasicInfo._ts', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='_version', full_name='cmdb.ObjectBasicInfo._version', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updateAuthorizers', full_name='cmdb.ObjectBasicInfo.updateAuthorizers', index=15,
      number=16, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deleteAuthorizers', full_name='cmdb.ObjectBasicInfo.deleteAuthorizers', index=16,
      number=17, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isAbstract', full_name='cmdb.ObjectBasicInfo.isAbstract', index=17,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parentObjectId', full_name='cmdb.ObjectBasicInfo.parentObjectId', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='permissionDenied', full_name='cmdb.ObjectBasicInfo.permissionDenied', index=19,
      number=20, type=8, cpp_type=7, label=1,
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
  serialized_start=81,
  serialized_end=488,
)

_OBJECTBASICINFO.fields_by_name['view'].message_type = user__service__sdk_dot_model_dot_cmdb_dot_object__view__pb2._OBJECTVIEW
DESCRIPTOR.message_types_by_name['ObjectBasicInfo'] = _OBJECTBASICINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ObjectBasicInfo = _reflection.GeneratedProtocolMessageType('ObjectBasicInfo', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTBASICINFO,
  '__module__' : 'object_basic_info_pb2'
  # @@protoc_insertion_point(class_scope:cmdb.ObjectBasicInfo)
  })
_sym_db.RegisterMessage(ObjectBasicInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
