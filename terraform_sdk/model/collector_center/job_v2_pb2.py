# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: job_v2.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from terraform_sdk.model.collector_center import script_pb2 as terraform__sdk_dot_model_dot_collector__center_dot_script__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='job_v2.proto',
  package='collector_center',
  syntax='proto3',
  serialized_options=_b('ZJgo.easyops.local/contracts/protorepo-models/easyops/model/collector_center'),
  serialized_pb=_b('\n\x0cjob_v2.proto\x12\x10\x63ollector_center\x1a\x31terraform_sdk/model/collector_center/script.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xe9\x05\n\tCollJobV2\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08interval\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x05\x12\x11\n\ttimeRange\x18\x04 \x01(\t\x12\x13\n\x0bjobFilePath\x18\x05 \x03(\t\x12\x0f\n\x07version\x18\x06 \x01(\t\x12\x32\n\x06target\x18\x07 \x01(\x0b\x32\".collector_center.CollJobV2.Target\x12\x0c\n\x04name\x18\x08 \x01(\t\x12(\n\x06script\x18\t \x01(\x0b\x32\x18.collector_center.Script\x12\x0e\n\x06\x64\x61taId\x18\n \x01(\x05\x12#\n\x03\x65nv\x18\x0b \x01(\x0b\x32\x16.google.protobuf.Value\x12&\n\x06kwargs\x18\x0c \x01(\x0b\x32\x16.google.protobuf.Value\x12\x0b\n\x03\x66un\x18\r \x01(\t\x12\x0f\n\x07\x63lazzId\x18\x0e \x01(\t\x12\x11\n\tclazzName\x18\x0f \x01(\t\x12\x10\n\x08\x63onfigId\x18\x10 \x01(\t\x12\x16\n\x0erequiredFields\x18\x11 \x03(\t\x12\x10\n\x08\x63\x61\x63heTtl\x18\x12 \x01(\x05\x12\x15\n\rignoreInvalid\x18\x13 \x01(\x08\x12\x0e\n\x06labels\x18\x14 \x03(\t\x12\x10\n\x08\x64isabled\x18\x15 \x01(\x08\x12\x0b\n\x03org\x18\x16 \x01(\x05\x12\x0f\n\x07\x63reator\x18\x17 \x01(\t\x12\x10\n\x08modifier\x18\x18 \x01(\t\x12\r\n\x05\x63time\x18\x19 \x01(\x05\x12\r\n\x05mtime\x18\x1a \x01(\x05\x12\x10\n\x08objectId\x18\x1b \x01(\t\x12\x12\n\ninstanceId\x18\x1c \x01(\t\x1a\x90\x01\n\x06Target\x12\n\n\x02id\x18\x01 \x01(\t\x12?\n\tagentHost\x18\x02 \x01(\x0b\x32,.collector_center.CollJobV2.Target.AgentHost\x1a\x39\n\tAgentHost\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\n\n\x02ip\x18\x02 \x01(\t\x12\x0c\n\x04uuid\x18\x03 \x01(\tBLZJgo.easyops.local/contracts/protorepo-models/easyops/model/collector_centerb\x06proto3')
  ,
  dependencies=[terraform__sdk_dot_model_dot_collector__center_dot_script__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_COLLJOBV2_TARGET_AGENTHOST = _descriptor.Descriptor(
  name='AgentHost',
  full_name='collector_center.CollJobV2.Target.AgentHost',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='collector_center.CollJobV2.Target.AgentHost.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip', full_name='collector_center.CollJobV2.Target.AgentHost.ip', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='collector_center.CollJobV2.Target.AgentHost.uuid', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=804,
  serialized_end=861,
)

_COLLJOBV2_TARGET = _descriptor.Descriptor(
  name='Target',
  full_name='collector_center.CollJobV2.Target',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='collector_center.CollJobV2.Target.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agentHost', full_name='collector_center.CollJobV2.Target.agentHost', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_COLLJOBV2_TARGET_AGENTHOST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=717,
  serialized_end=861,
)

_COLLJOBV2 = _descriptor.Descriptor(
  name='CollJobV2',
  full_name='collector_center.CollJobV2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='collector_center.CollJobV2.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interval', full_name='collector_center.CollJobV2.interval', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='collector_center.CollJobV2.timeout', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeRange', full_name='collector_center.CollJobV2.timeRange', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='jobFilePath', full_name='collector_center.CollJobV2.jobFilePath', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='collector_center.CollJobV2.version', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target', full_name='collector_center.CollJobV2.target', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='collector_center.CollJobV2.name', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='script', full_name='collector_center.CollJobV2.script', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataId', full_name='collector_center.CollJobV2.dataId', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='env', full_name='collector_center.CollJobV2.env', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kwargs', full_name='collector_center.CollJobV2.kwargs', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fun', full_name='collector_center.CollJobV2.fun', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clazzId', full_name='collector_center.CollJobV2.clazzId', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clazzName', full_name='collector_center.CollJobV2.clazzName', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='configId', full_name='collector_center.CollJobV2.configId', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requiredFields', full_name='collector_center.CollJobV2.requiredFields', index=16,
      number=17, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cacheTtl', full_name='collector_center.CollJobV2.cacheTtl', index=17,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ignoreInvalid', full_name='collector_center.CollJobV2.ignoreInvalid', index=18,
      number=19, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='collector_center.CollJobV2.labels', index=19,
      number=20, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disabled', full_name='collector_center.CollJobV2.disabled', index=20,
      number=21, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org', full_name='collector_center.CollJobV2.org', index=21,
      number=22, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='collector_center.CollJobV2.creator', index=22,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='modifier', full_name='collector_center.CollJobV2.modifier', index=23,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='collector_center.CollJobV2.ctime', index=24,
      number=25, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='collector_center.CollJobV2.mtime', index=25,
      number=26, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectId', full_name='collector_center.CollJobV2.objectId', index=26,
      number=27, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='collector_center.CollJobV2.instanceId', index=27,
      number=28, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_COLLJOBV2_TARGET, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=116,
  serialized_end=861,
)

_COLLJOBV2_TARGET_AGENTHOST.containing_type = _COLLJOBV2_TARGET
_COLLJOBV2_TARGET.fields_by_name['agentHost'].message_type = _COLLJOBV2_TARGET_AGENTHOST
_COLLJOBV2_TARGET.containing_type = _COLLJOBV2
_COLLJOBV2.fields_by_name['target'].message_type = _COLLJOBV2_TARGET
_COLLJOBV2.fields_by_name['script'].message_type = terraform__sdk_dot_model_dot_collector__center_dot_script__pb2._SCRIPT
_COLLJOBV2.fields_by_name['env'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_COLLJOBV2.fields_by_name['kwargs'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
DESCRIPTOR.message_types_by_name['CollJobV2'] = _COLLJOBV2
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CollJobV2 = _reflection.GeneratedProtocolMessageType('CollJobV2', (_message.Message,), {

  'Target' : _reflection.GeneratedProtocolMessageType('Target', (_message.Message,), {

    'AgentHost' : _reflection.GeneratedProtocolMessageType('AgentHost', (_message.Message,), {
      'DESCRIPTOR' : _COLLJOBV2_TARGET_AGENTHOST,
      '__module__' : 'job_v2_pb2'
      # @@protoc_insertion_point(class_scope:collector_center.CollJobV2.Target.AgentHost)
      })
    ,
    'DESCRIPTOR' : _COLLJOBV2_TARGET,
    '__module__' : 'job_v2_pb2'
    # @@protoc_insertion_point(class_scope:collector_center.CollJobV2.Target)
    })
  ,
  'DESCRIPTOR' : _COLLJOBV2,
  '__module__' : 'job_v2_pb2'
  # @@protoc_insertion_point(class_scope:collector_center.CollJobV2)
  })
_sym_db.RegisterMessage(CollJobV2)
_sym_db.RegisterMessage(CollJobV2.Target)
_sym_db.RegisterMessage(CollJobV2.Target.AgentHost)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
