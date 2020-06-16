# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: version_info.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from collector_center_sdk.model.file_repository import diff_pb2 as collector__center__sdk_dot_model_dot_file__repository_dot_diff__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='version_info.proto',
  package='easy_flow',
  syntax='proto3',
  serialized_options=_b('ZCgo.easyops.local/contracts/protorepo-models/easyops/model/easy_flow'),
  serialized_pb=_b('\n\x12version_info.proto\x12\teasy_flow\x1a\x35\x63ollector_center_sdk/model/file_repository/diff.proto\"\xa9\x03\n\x0bVersionInfo\x12\x13\n\x0brepoVersion\x18\x01 \x01(\t\x12\x0e\n\x06source\x18\x02 \x01(\t\x12\x39\n\x0csourceDecode\x18\x03 \x01(\x0b\x32#.easy_flow.VersionInfo.SourceDecode\x12#\n\x04\x64iff\x18\x04 \x03(\x0b\x32\x15.file_repository.Diff\x12\x11\n\tpackageId\x18\x05 \x01(\t\x12\x11\n\tversionId\x18\x06 \x01(\t\x12\x0c\n\x04name\x18\x07 \x01(\t\x12\x0f\n\x07\x63reator\x18\x08 \x01(\t\x12\x0b\n\x03org\x18\t \x01(\x05\x12\x0c\n\x04memo\x18\n \x01(\t\x12\r\n\x05\x63time\x18\x0b \x01(\t\x12\r\n\x05mtime\x18\x0c \x01(\t\x12\x0c\n\x04sign\x18\r \x01(\t\x12\x12\n\nsourceType\x18\x0e \x01(\t\x12\x0c\n\x04\x63onf\x18\x0f \x01(\t\x12\x10\n\x08\x65nv_type\x18\x10 \x01(\x05\x1aU\n\x0cSourceDecode\x12\x0f\n\x07\x65nsName\x18\x01 \x01(\t\x12\x0c\n\x04host\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\n\n\x02ip\x18\x04 \x01(\t\x12\x0c\n\x04port\x18\x05 \x01(\x05\x42\x45ZCgo.easyops.local/contracts/protorepo-models/easyops/model/easy_flowb\x06proto3')
  ,
  dependencies=[collector__center__sdk_dot_model_dot_file__repository_dot_diff__pb2.DESCRIPTOR,])




_VERSIONINFO_SOURCEDECODE = _descriptor.Descriptor(
  name='SourceDecode',
  full_name='easy_flow.VersionInfo.SourceDecode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ensName', full_name='easy_flow.VersionInfo.SourceDecode.ensName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host', full_name='easy_flow.VersionInfo.SourceDecode.host', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='easy_flow.VersionInfo.SourceDecode.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip', full_name='easy_flow.VersionInfo.SourceDecode.ip', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='easy_flow.VersionInfo.SourceDecode.port', index=4,
      number=5, type=5, cpp_type=1, label=1,
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
  serialized_start=429,
  serialized_end=514,
)

_VERSIONINFO = _descriptor.Descriptor(
  name='VersionInfo',
  full_name='easy_flow.VersionInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='repoVersion', full_name='easy_flow.VersionInfo.repoVersion', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='easy_flow.VersionInfo.source', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sourceDecode', full_name='easy_flow.VersionInfo.sourceDecode', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='diff', full_name='easy_flow.VersionInfo.diff', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageId', full_name='easy_flow.VersionInfo.packageId', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionId', full_name='easy_flow.VersionInfo.versionId', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='easy_flow.VersionInfo.name', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='easy_flow.VersionInfo.creator', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org', full_name='easy_flow.VersionInfo.org', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='easy_flow.VersionInfo.memo', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='easy_flow.VersionInfo.ctime', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='easy_flow.VersionInfo.mtime', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sign', full_name='easy_flow.VersionInfo.sign', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sourceType', full_name='easy_flow.VersionInfo.sourceType', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conf', full_name='easy_flow.VersionInfo.conf', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='env_type', full_name='easy_flow.VersionInfo.env_type', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_VERSIONINFO_SOURCEDECODE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=89,
  serialized_end=514,
)

_VERSIONINFO_SOURCEDECODE.containing_type = _VERSIONINFO
_VERSIONINFO.fields_by_name['sourceDecode'].message_type = _VERSIONINFO_SOURCEDECODE
_VERSIONINFO.fields_by_name['diff'].message_type = collector__center__sdk_dot_model_dot_file__repository_dot_diff__pb2._DIFF
DESCRIPTOR.message_types_by_name['VersionInfo'] = _VERSIONINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VersionInfo = _reflection.GeneratedProtocolMessageType('VersionInfo', (_message.Message,), {

  'SourceDecode' : _reflection.GeneratedProtocolMessageType('SourceDecode', (_message.Message,), {
    'DESCRIPTOR' : _VERSIONINFO_SOURCEDECODE,
    '__module__' : 'version_info_pb2'
    # @@protoc_insertion_point(class_scope:easy_flow.VersionInfo.SourceDecode)
    })
  ,
  'DESCRIPTOR' : _VERSIONINFO,
  '__module__' : 'version_info_pb2'
  # @@protoc_insertion_point(class_scope:easy_flow.VersionInfo)
  })
_sym_db.RegisterMessage(VersionInfo)
_sym_db.RegisterMessage(VersionInfo.SourceDecode)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
