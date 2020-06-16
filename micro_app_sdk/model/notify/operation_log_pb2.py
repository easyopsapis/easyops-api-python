# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: operation_log.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from micro_app_sdk.model.notify import device_pb2 as micro__app__sdk_dot_model_dot_notify_dot_device__pb2
from micro_app_sdk.model.notify import app_pb2 as micro__app__sdk_dot_model_dot_notify_dot_app__pb2
from micro_app_sdk.model.notify import deploy_info_pb2 as micro__app__sdk_dot_model_dot_notify_dot_deploy__info__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='operation_log.proto',
  package='notify',
  syntax='proto3',
  serialized_options=_b('Z@go.easyops.local/contracts/protorepo-models/easyops/model/notify'),
  serialized_pb=_b('\n\x13operation_log.proto\x12\x06notify\x1a\'micro_app_sdk/model/notify/device.proto\x1a$micro_app_sdk/model/notify/app.proto\x1a,micro_app_sdk/model/notify/deploy_info.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xa8\x05\n\x0cOperationLog\x12\x0e\n\x06system\x18\x01 \x01(\t\x12\r\n\x05topic\x18\x02 \x01(\t\x12\x10\n\x08\x65vent_id\x18\x03 \x01(\t\x12\x17\n\x0fparent_event_id\x18\x04 \x01(\t\x12*\n\x0cparent_event\x18\x05 \x01(\x0b\x32\x14.notify.OperationLog\x12\r\n\x05\x65vent\x18\x06 \x01(\t\x12\x0e\n\x06status\x18\x07 \x01(\t\x12#\n\x0b\x64\x65vice_list\x18\x08 \x03(\x0b\x32\x0e.notify.Device\x12\x10\n\x08operator\x18\t \x01(\t\x12\x13\n\x0btarget_name\x18\n \x01(\t\x12\x11\n\ttarget_id\x18\x0b \x01(\t\x12\x17\n\x0ftarget_category\x18\x0c \x01(\t\x12\x1d\n\x08\x61pp_list\x18\r \x03(\x0b\x32\x0b.notify.App\x12)\n\x08\x65xt_info\x18\x0e \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tnotifiers\x18\x0f \x03(\t\x12\x0f\n\x07trigger\x18\x10 \x01(\t\x12\x0c\n\x04memo\x18\x11 \x01(\t\x12\x0e\n\x06\x61pp_id\x18\x12 \x01(\t\x12\x12\n\ncluster_id\x18\x13 \x01(\t\x12\x12\n\npackage_id\x18\x14 \x01(\t\x12\x14\n\x0cpackage_name\x18\x15 \x01(\t\x12\x12\n\nversion_id\x18\x16 \x01(\t\x12\x14\n\x0cversion_name\x18\x17 \x01(\t\x12\'\n\x0b\x64\x65ploy_info\x18\x18 \x01(\x0b\x32\x12.notify.DeployInfo\x12\x0f\n\x07\x63ontent\x18\x19 \x01(\t\x12\x11\n\tdata_name\x18\x1a \x01(\t\x12\n\n\x02ip\x18\x1b \x01(\t\x12\x0f\n\x07ip_list\x18\x1c \x03(\t\x12\x0f\n\x07subject\x18\x1d \x01(\t\x12\r\n\x05mtime\x18\x1e \x01(\x03\x12\r\n\x05\x63time\x18\x1f \x01(\x03\x42\x42Z@go.easyops.local/contracts/protorepo-models/easyops/model/notifyb\x06proto3')
  ,
  dependencies=[micro__app__sdk_dot_model_dot_notify_dot_device__pb2.DESCRIPTOR,micro__app__sdk_dot_model_dot_notify_dot_app__pb2.DESCRIPTOR,micro__app__sdk_dot_model_dot_notify_dot_deploy__info__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_OPERATIONLOG = _descriptor.Descriptor(
  name='OperationLog',
  full_name='notify.OperationLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='system', full_name='notify.OperationLog.system', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='topic', full_name='notify.OperationLog.topic', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event_id', full_name='notify.OperationLog.event_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent_event_id', full_name='notify.OperationLog.parent_event_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent_event', full_name='notify.OperationLog.parent_event', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event', full_name='notify.OperationLog.event', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='notify.OperationLog.status', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_list', full_name='notify.OperationLog.device_list', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operator', full_name='notify.OperationLog.operator', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_name', full_name='notify.OperationLog.target_name', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_id', full_name='notify.OperationLog.target_id', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_category', full_name='notify.OperationLog.target_category', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='app_list', full_name='notify.OperationLog.app_list', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ext_info', full_name='notify.OperationLog.ext_info', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='notifiers', full_name='notify.OperationLog.notifiers', index=14,
      number=15, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trigger', full_name='notify.OperationLog.trigger', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='notify.OperationLog.memo', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='app_id', full_name='notify.OperationLog.app_id', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='notify.OperationLog.cluster_id', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='package_id', full_name='notify.OperationLog.package_id', index=19,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='package_name', full_name='notify.OperationLog.package_name', index=20,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version_id', full_name='notify.OperationLog.version_id', index=21,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version_name', full_name='notify.OperationLog.version_name', index=22,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deploy_info', full_name='notify.OperationLog.deploy_info', index=23,
      number=24, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='notify.OperationLog.content', index=24,
      number=25, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_name', full_name='notify.OperationLog.data_name', index=25,
      number=26, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip', full_name='notify.OperationLog.ip', index=26,
      number=27, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip_list', full_name='notify.OperationLog.ip_list', index=27,
      number=28, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subject', full_name='notify.OperationLog.subject', index=28,
      number=29, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='notify.OperationLog.mtime', index=29,
      number=30, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='notify.OperationLog.ctime', index=30,
      number=31, type=3, cpp_type=2, label=1,
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
  serialized_start=187,
  serialized_end=867,
)

_OPERATIONLOG.fields_by_name['parent_event'].message_type = _OPERATIONLOG
_OPERATIONLOG.fields_by_name['device_list'].message_type = micro__app__sdk_dot_model_dot_notify_dot_device__pb2._DEVICE
_OPERATIONLOG.fields_by_name['app_list'].message_type = micro__app__sdk_dot_model_dot_notify_dot_app__pb2._APP
_OPERATIONLOG.fields_by_name['ext_info'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_OPERATIONLOG.fields_by_name['deploy_info'].message_type = micro__app__sdk_dot_model_dot_notify_dot_deploy__info__pb2._DEPLOYINFO
DESCRIPTOR.message_types_by_name['OperationLog'] = _OPERATIONLOG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OperationLog = _reflection.GeneratedProtocolMessageType('OperationLog', (_message.Message,), {
  'DESCRIPTOR' : _OPERATIONLOG,
  '__module__' : 'operation_log_pb2'
  # @@protoc_insertion_point(class_scope:notify.OperationLog)
  })
_sym_db.RegisterMessage(OperationLog)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
