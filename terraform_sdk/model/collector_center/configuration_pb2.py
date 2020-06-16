# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: configuration.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from terraform_sdk.model.collector_center import script_pb2 as terraform__sdk_dot_model_dot_collector__center_dot_script__pb2
from terraform_sdk.model.collector_center import target_range_pb2 as terraform__sdk_dot_model_dot_collector__center_dot_target__range__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='configuration.proto',
  package='collector_center',
  syntax='proto3',
  serialized_options=_b('ZJgo.easyops.local/contracts/protorepo-models/easyops/model/collector_center'),
  serialized_pb=_b('\n\x13\x63onfiguration.proto\x12\x10\x63ollector_center\x1a\x31terraform_sdk/model/collector_center/script.proto\x1a\x37terraform_sdk/model/collector_center/target_range.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xf2\x03\n\rConfiguration\x12\x0b\n\x03org\x18\x01 \x01(\x05\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12&\n\x06kwargs\x18\x04 \x01(\x0b\x32\x16.google.protobuf.Value\x12\x0f\n\x07timeout\x18\x05 \x01(\x05\x12#\n\x03\x65nv\x18\x06 \x01(\x0b\x32\x16.google.protobuf.Value\x12\x10\n\x08\x64isabled\x18\x07 \x01(\x08\x12\x0e\n\x06labels\x18\x08 \x03(\t\x12\x15\n\rignoreInvalid\x18\t \x01(\x08\x12(\n\x06script\x18\n \x01(\x0b\x32\x18.collector_center.Script\x12\x32\n\x0btargetRange\x18\x0b \x01(\x0b\x32\x1d.collector_center.TargetRange\x12\x10\n\x08interval\x18\x0c \x01(\x05\x12\x10\n\x08\x63\x61\x63heTtl\x18\r \x01(\x05\x12\x11\n\ttimeRange\x18\x0e \x01(\t\x12\x0f\n\x07\x63lazzId\x18\x0f \x01(\t\x12\x11\n\tclazzName\x18\x10 \x01(\t\x12\x0f\n\x07\x63reator\x18\x11 \x01(\t\x12\x10\n\x08modifier\x18\x12 \x01(\t\x12\r\n\x05\x63time\x18\x13 \x01(\x05\x12\r\n\x05mtime\x18\x14 \x01(\x05\x12\x10\n\x08objectId\x18\x15 \x01(\t\x12\x17\n\x0finstanceIdMacro\x18\x16 \x01(\tBLZJgo.easyops.local/contracts/protorepo-models/easyops/model/collector_centerb\x06proto3')
  ,
  dependencies=[terraform__sdk_dot_model_dot_collector__center_dot_script__pb2.DESCRIPTOR,terraform__sdk_dot_model_dot_collector__center_dot_target__range__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_CONFIGURATION = _descriptor.Descriptor(
  name='Configuration',
  full_name='collector_center.Configuration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='org', full_name='collector_center.Configuration.org', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='collector_center.Configuration.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='collector_center.Configuration.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kwargs', full_name='collector_center.Configuration.kwargs', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='collector_center.Configuration.timeout', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='env', full_name='collector_center.Configuration.env', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disabled', full_name='collector_center.Configuration.disabled', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='collector_center.Configuration.labels', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ignoreInvalid', full_name='collector_center.Configuration.ignoreInvalid', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='script', full_name='collector_center.Configuration.script', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targetRange', full_name='collector_center.Configuration.targetRange', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interval', full_name='collector_center.Configuration.interval', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cacheTtl', full_name='collector_center.Configuration.cacheTtl', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeRange', full_name='collector_center.Configuration.timeRange', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clazzId', full_name='collector_center.Configuration.clazzId', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clazzName', full_name='collector_center.Configuration.clazzName', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='collector_center.Configuration.creator', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='modifier', full_name='collector_center.Configuration.modifier', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='collector_center.Configuration.ctime', index=18,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='collector_center.Configuration.mtime', index=19,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectId', full_name='collector_center.Configuration.objectId', index=20,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceIdMacro', full_name='collector_center.Configuration.instanceIdMacro', index=21,
      number=22, type=9, cpp_type=9, label=1,
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
  serialized_start=180,
  serialized_end=678,
)

_CONFIGURATION.fields_by_name['kwargs'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_CONFIGURATION.fields_by_name['env'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_CONFIGURATION.fields_by_name['script'].message_type = terraform__sdk_dot_model_dot_collector__center_dot_script__pb2._SCRIPT
_CONFIGURATION.fields_by_name['targetRange'].message_type = terraform__sdk_dot_model_dot_collector__center_dot_target__range__pb2._TARGETRANGE
DESCRIPTOR.message_types_by_name['Configuration'] = _CONFIGURATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Configuration = _reflection.GeneratedProtocolMessageType('Configuration', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGURATION,
  '__module__' : 'configuration_pb2'
  # @@protoc_insertion_point(class_scope:collector_center.Configuration)
  })
_sym_db.RegisterMessage(Configuration)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
