# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: task.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='task.proto',
  package='capacity_admin',
  syntax='proto3',
  serialized_options=_b('ZHgo.easyops.local/contracts/protorepo-models/easyops/model/capacity_admin'),
  serialized_pb=_b('\n\ntask.proto\x12\x0e\x63\x61pacity_admin\"\x92\x02\n\x0c\x43\x61pacityTask\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05hosts\x18\x03 \x03(\t\x12\x1a\n\x12suspectedIdleHosts\x18\x04 \x03(\t\x12\x11\n\tidleHosts\x18\x05 \x03(\t\x12\x14\n\x0cnonIdleHosts\x18\x06 \x03(\t\x12\x0e\n\x06status\x18\x07 \x01(\t\x12\x0f\n\x07\x65ndTime\x18\x08 \x01(\t\x12\x0f\n\x07hitRate\x18\t \x01(\x02\x12\r\n\x05\x63time\x18\n \x01(\t\x12\x0f\n\x07\x63reator\x18\x0b \x01(\t\x12\x0e\n\x06\x65xecId\x18\x0c \x01(\t\x12\x13\n\x0bnormalHosts\x18\r \x03(\t\x12\x15\n\rabnormalHosts\x18\x0e \x03(\tBJZHgo.easyops.local/contracts/protorepo-models/easyops/model/capacity_adminb\x06proto3')
)




_CAPACITYTASK = _descriptor.Descriptor(
  name='CapacityTask',
  full_name='capacity_admin.CapacityTask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='capacity_admin.CapacityTask.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='capacity_admin.CapacityTask.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hosts', full_name='capacity_admin.CapacityTask.hosts', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='suspectedIdleHosts', full_name='capacity_admin.CapacityTask.suspectedIdleHosts', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='idleHosts', full_name='capacity_admin.CapacityTask.idleHosts', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nonIdleHosts', full_name='capacity_admin.CapacityTask.nonIdleHosts', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='capacity_admin.CapacityTask.status', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endTime', full_name='capacity_admin.CapacityTask.endTime', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hitRate', full_name='capacity_admin.CapacityTask.hitRate', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='capacity_admin.CapacityTask.ctime', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='capacity_admin.CapacityTask.creator', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='execId', full_name='capacity_admin.CapacityTask.execId', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='normalHosts', full_name='capacity_admin.CapacityTask.normalHosts', index=12,
      number=13, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='abnormalHosts', full_name='capacity_admin.CapacityTask.abnormalHosts', index=13,
      number=14, type=9, cpp_type=9, label=3,
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
  serialized_start=31,
  serialized_end=305,
)

DESCRIPTOR.message_types_by_name['CapacityTask'] = _CAPACITYTASK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CapacityTask = _reflection.GeneratedProtocolMessageType('CapacityTask', (_message.Message,), {
  'DESCRIPTOR' : _CAPACITYTASK,
  '__module__' : 'task_pb2'
  # @@protoc_insertion_point(class_scope:capacity_admin.CapacityTask)
  })
_sym_db.RegisterMessage(CapacityTask)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)