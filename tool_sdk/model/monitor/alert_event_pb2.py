# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: alert_event.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tool_sdk.model.monitor import alert_conditions_pb2 as tool__sdk_dot_model_dot_monitor_dot_alert__conditions__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='alert_event.proto',
  package='monitor',
  syntax='proto3',
  serialized_options=_b('ZAgo.easyops.local/contracts/protorepo-models/easyops/model/monitor'),
  serialized_pb=_b('\n\x11\x61lert_event.proto\x12\x07monitor\x1a-tool_sdk/model/monitor/alert_conditions.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xa7\t\n\nAlertEvent\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08\x61lert_id\x18\x02 \x01(\t\x12\x0f\n\x07rule_id\x18\x03 \x01(\t\x12\x12\n\nis_recover\x18\x04 \x01(\x08\x12\x11\n\tsend_succ\x18\x05 \x01(\x08\x12\x0f\n\x07subject\x18\x06 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x07 \x01(\t\x12\x0e\n\x06source\x18\x08 \x01(\t\x12\x0e\n\x06status\x18\t \x01(\x05\x12\x13\n\x0bsend_detail\x18\n \x01(\x05\x12\x14\n\x0crecover_type\x18\x0b \x01(\t\x12\x0b\n\x03org\x18\x0c \x01(\x05\x12\x0e\n\x06target\x18\r \x01(\t\x12\r\n\x05level\x18\x0e \x01(\x05\x12%\n\x05value\x18\x0f \x01(\x0b\x32\x16.google.protobuf.Value\x12\x16\n\x0e\x61lert_duration\x18\x10 \x01(\x02\x12\x18\n\x10\x61lert_begin_time\x18\x11 \x01(\x05\x12\x16\n\x0e\x61lert_end_time\x18\x12 \x01(\x05\x12\x0c\n\x04time\x18\x13 \x01(\x05\x12\x12\n\nstart_time\x18\x14 \x01(\x05\x12\x13\n\x0binsert_time\x18\x15 \x01(\x05\x12;\n\x0f\x61lert_receivers\x18\x16 \x03(\x0b\x32\".monitor.AlertEvent.AlertReceivers\x12\x31\n\nalert_dims\x18\x17 \x03(\x0b\x32\x1d.monitor.AlertEvent.AlertDims\x12,\n\x07\x61\x63tions\x18\x18 \x03(\x0b\x32\x1b.monitor.AlertEvent.Actions\x12\x32\n\x10\x61lert_conditions\x18\x19 \x01(\x0b\x32\x18.monitor.AlertConditions\x12\x10\n\x08objectId\x18\x1a \x01(\t\x12\x12\n\ninstanceId\x18\x1b \x01(\t\x12\x0e\n\x06system\x18\x1c \x01(\t\x1a.\n\x0e\x41lertReceivers\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06method\x18\x02 \x01(\t\x1a@\n\tAlertDims\x12\x0c\n\x04name\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.Value\x1a\x87\x03\n\x07\x41\x63tions\x12\x38\n\tcondition\x18\x01 \x01(\x0b\x32%.monitor.AlertEvent.Actions.Condition\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\x05\x12\x0f\n\x07upgrade\x18\x04 \x01(\x08\x12\x0b\n\x03run\x18\x05 \x01(\x08\x12\x0f\n\x07methods\x18\x06 \x03(\t\x12\x11\n\treceivers\x18\x07 \x03(\t\x12\x1c\n\x14receiver_user_groups\x18\x08 \x03(\t\x12\x43\n\x0freceiver_owners\x18\t \x03(\x0b\x32*.monitor.AlertEvent.Actions.ReceiverOwners\x1a/\n\tCondition\x12\x13\n\x0blasting_for\x18\x01 \x01(\x05\x12\r\n\x05level\x18\x02 \x01(\x05\x1aN\n\x0eReceiverOwners\x12\x11\n\ttranslate\x18\x01 \x01(\t\x12\x11\n\tobject_id\x18\x02 \x01(\t\x12\x16\n\x0eobject_attr_id\x18\x03 \x01(\tBCZAgo.easyops.local/contracts/protorepo-models/easyops/model/monitorb\x06proto3')
  ,
  dependencies=[tool__sdk_dot_model_dot_monitor_dot_alert__conditions__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_ALERTEVENT_ALERTRECEIVERS = _descriptor.Descriptor(
  name='AlertReceivers',
  full_name='monitor.AlertEvent.AlertReceivers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='monitor.AlertEvent.AlertReceivers.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='method', full_name='monitor.AlertEvent.AlertReceivers.method', index=1,
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
  serialized_start=793,
  serialized_end=839,
)

_ALERTEVENT_ALERTDIMS = _descriptor.Descriptor(
  name='AlertDims',
  full_name='monitor.AlertEvent.AlertDims',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='monitor.AlertEvent.AlertDims.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='monitor.AlertEvent.AlertDims.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=841,
  serialized_end=905,
)

_ALERTEVENT_ACTIONS_CONDITION = _descriptor.Descriptor(
  name='Condition',
  full_name='monitor.AlertEvent.Actions.Condition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lasting_for', full_name='monitor.AlertEvent.Actions.Condition.lasting_for', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level', full_name='monitor.AlertEvent.Actions.Condition.level', index=1,
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
  serialized_start=1172,
  serialized_end=1219,
)

_ALERTEVENT_ACTIONS_RECEIVEROWNERS = _descriptor.Descriptor(
  name='ReceiverOwners',
  full_name='monitor.AlertEvent.Actions.ReceiverOwners',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='translate', full_name='monitor.AlertEvent.Actions.ReceiverOwners.translate', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object_id', full_name='monitor.AlertEvent.Actions.ReceiverOwners.object_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object_attr_id', full_name='monitor.AlertEvent.Actions.ReceiverOwners.object_attr_id', index=2,
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
  serialized_start=1221,
  serialized_end=1299,
)

_ALERTEVENT_ACTIONS = _descriptor.Descriptor(
  name='Actions',
  full_name='monitor.AlertEvent.Actions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='condition', full_name='monitor.AlertEvent.Actions.condition', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='monitor.AlertEvent.Actions.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='monitor.AlertEvent.Actions.status', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='upgrade', full_name='monitor.AlertEvent.Actions.upgrade', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='run', full_name='monitor.AlertEvent.Actions.run', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='methods', full_name='monitor.AlertEvent.Actions.methods', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='receivers', full_name='monitor.AlertEvent.Actions.receivers', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='receiver_user_groups', full_name='monitor.AlertEvent.Actions.receiver_user_groups', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='receiver_owners', full_name='monitor.AlertEvent.Actions.receiver_owners', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ALERTEVENT_ACTIONS_CONDITION, _ALERTEVENT_ACTIONS_RECEIVEROWNERS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=908,
  serialized_end=1299,
)

_ALERTEVENT = _descriptor.Descriptor(
  name='AlertEvent',
  full_name='monitor.AlertEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='monitor.AlertEvent.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alert_id', full_name='monitor.AlertEvent.alert_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rule_id', full_name='monitor.AlertEvent.rule_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_recover', full_name='monitor.AlertEvent.is_recover', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='send_succ', full_name='monitor.AlertEvent.send_succ', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subject', full_name='monitor.AlertEvent.subject', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='monitor.AlertEvent.content', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='monitor.AlertEvent.source', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='monitor.AlertEvent.status', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='send_detail', full_name='monitor.AlertEvent.send_detail', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='recover_type', full_name='monitor.AlertEvent.recover_type', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org', full_name='monitor.AlertEvent.org', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target', full_name='monitor.AlertEvent.target', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level', full_name='monitor.AlertEvent.level', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='monitor.AlertEvent.value', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alert_duration', full_name='monitor.AlertEvent.alert_duration', index=15,
      number=16, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alert_begin_time', full_name='monitor.AlertEvent.alert_begin_time', index=16,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alert_end_time', full_name='monitor.AlertEvent.alert_end_time', index=17,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='monitor.AlertEvent.time', index=18,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='monitor.AlertEvent.start_time', index=19,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='insert_time', full_name='monitor.AlertEvent.insert_time', index=20,
      number=21, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alert_receivers', full_name='monitor.AlertEvent.alert_receivers', index=21,
      number=22, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alert_dims', full_name='monitor.AlertEvent.alert_dims', index=22,
      number=23, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actions', full_name='monitor.AlertEvent.actions', index=23,
      number=24, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alert_conditions', full_name='monitor.AlertEvent.alert_conditions', index=24,
      number=25, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectId', full_name='monitor.AlertEvent.objectId', index=25,
      number=26, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='monitor.AlertEvent.instanceId', index=26,
      number=27, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='system', full_name='monitor.AlertEvent.system', index=27,
      number=28, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ALERTEVENT_ALERTRECEIVERS, _ALERTEVENT_ALERTDIMS, _ALERTEVENT_ACTIONS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=108,
  serialized_end=1299,
)

_ALERTEVENT_ALERTRECEIVERS.containing_type = _ALERTEVENT
_ALERTEVENT_ALERTDIMS.fields_by_name['value'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_ALERTEVENT_ALERTDIMS.containing_type = _ALERTEVENT
_ALERTEVENT_ACTIONS_CONDITION.containing_type = _ALERTEVENT_ACTIONS
_ALERTEVENT_ACTIONS_RECEIVEROWNERS.containing_type = _ALERTEVENT_ACTIONS
_ALERTEVENT_ACTIONS.fields_by_name['condition'].message_type = _ALERTEVENT_ACTIONS_CONDITION
_ALERTEVENT_ACTIONS.fields_by_name['receiver_owners'].message_type = _ALERTEVENT_ACTIONS_RECEIVEROWNERS
_ALERTEVENT_ACTIONS.containing_type = _ALERTEVENT
_ALERTEVENT.fields_by_name['value'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_ALERTEVENT.fields_by_name['alert_receivers'].message_type = _ALERTEVENT_ALERTRECEIVERS
_ALERTEVENT.fields_by_name['alert_dims'].message_type = _ALERTEVENT_ALERTDIMS
_ALERTEVENT.fields_by_name['actions'].message_type = _ALERTEVENT_ACTIONS
_ALERTEVENT.fields_by_name['alert_conditions'].message_type = tool__sdk_dot_model_dot_monitor_dot_alert__conditions__pb2._ALERTCONDITIONS
DESCRIPTOR.message_types_by_name['AlertEvent'] = _ALERTEVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AlertEvent = _reflection.GeneratedProtocolMessageType('AlertEvent', (_message.Message,), {

  'AlertReceivers' : _reflection.GeneratedProtocolMessageType('AlertReceivers', (_message.Message,), {
    'DESCRIPTOR' : _ALERTEVENT_ALERTRECEIVERS,
    '__module__' : 'alert_event_pb2'
    # @@protoc_insertion_point(class_scope:monitor.AlertEvent.AlertReceivers)
    })
  ,

  'AlertDims' : _reflection.GeneratedProtocolMessageType('AlertDims', (_message.Message,), {
    'DESCRIPTOR' : _ALERTEVENT_ALERTDIMS,
    '__module__' : 'alert_event_pb2'
    # @@protoc_insertion_point(class_scope:monitor.AlertEvent.AlertDims)
    })
  ,

  'Actions' : _reflection.GeneratedProtocolMessageType('Actions', (_message.Message,), {

    'Condition' : _reflection.GeneratedProtocolMessageType('Condition', (_message.Message,), {
      'DESCRIPTOR' : _ALERTEVENT_ACTIONS_CONDITION,
      '__module__' : 'alert_event_pb2'
      # @@protoc_insertion_point(class_scope:monitor.AlertEvent.Actions.Condition)
      })
    ,

    'ReceiverOwners' : _reflection.GeneratedProtocolMessageType('ReceiverOwners', (_message.Message,), {
      'DESCRIPTOR' : _ALERTEVENT_ACTIONS_RECEIVEROWNERS,
      '__module__' : 'alert_event_pb2'
      # @@protoc_insertion_point(class_scope:monitor.AlertEvent.Actions.ReceiverOwners)
      })
    ,
    'DESCRIPTOR' : _ALERTEVENT_ACTIONS,
    '__module__' : 'alert_event_pb2'
    # @@protoc_insertion_point(class_scope:monitor.AlertEvent.Actions)
    })
  ,
  'DESCRIPTOR' : _ALERTEVENT,
  '__module__' : 'alert_event_pb2'
  # @@protoc_insertion_point(class_scope:monitor.AlertEvent)
  })
_sym_db.RegisterMessage(AlertEvent)
_sym_db.RegisterMessage(AlertEvent.AlertReceivers)
_sym_db.RegisterMessage(AlertEvent.AlertDims)
_sym_db.RegisterMessage(AlertEvent.Actions)
_sym_db.RegisterMessage(AlertEvent.Actions.Condition)
_sym_db.RegisterMessage(AlertEvent.Actions.ReceiverOwners)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)