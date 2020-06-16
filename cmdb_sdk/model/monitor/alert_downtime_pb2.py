# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: alert_downtime.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cmdb_sdk.model.monitor import alert_dims_pb2 as cmdb__sdk_dot_model_dot_monitor_dot_alert__dims__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='alert_downtime.proto',
  package='monitor',
  syntax='proto3',
  serialized_options=_b('ZAgo.easyops.local/contracts/protorepo-models/easyops/model/monitor'),
  serialized_pb=_b('\n\x14\x61lert_downtime.proto\x12\x07monitor\x1a\'cmdb_sdk/model/monitor/alert_dims.proto\"\xd2\x02\n\rAlertDowntime\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\ralert_rule_id\x18\x02 \x01(\t\x12&\n\nalert_dims\x18\x03 \x03(\x0b\x32\x12.monitor.AlertDims\x12\x31\n\x08schedule\x18\x04 \x01(\x0b\x32\x1f.monitor.AlertDowntime.Schedule\x12\x0e\n\x06reason\x18\x05 \x01(\t\x12\x0f\n\x07\x63reator\x18\x06 \x01(\t\x12\r\n\x05\x63time\x18\x07 \x01(\x05\x12\r\n\x05mtime\x18\x08 \x01(\x05\x12\x0b\n\x03org\x18\t \x01(\x05\x1aw\n\x08Schedule\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x12\n\nstart_time\x18\x02 \x01(\t\x12\x10\n\x08\x65nd_time\x18\x03 \x01(\t\x12\x12\n\nstart_date\x18\x04 \x01(\t\x12\x10\n\x08\x65nd_date\x18\x05 \x01(\t\x12\x11\n\trepeat_on\x18\x06 \x03(\tBCZAgo.easyops.local/contracts/protorepo-models/easyops/model/monitorb\x06proto3')
  ,
  dependencies=[cmdb__sdk_dot_model_dot_monitor_dot_alert__dims__pb2.DESCRIPTOR,])




_ALERTDOWNTIME_SCHEDULE = _descriptor.Descriptor(
  name='Schedule',
  full_name='monitor.AlertDowntime.Schedule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='monitor.AlertDowntime.Schedule.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='monitor.AlertDowntime.Schedule.start_time', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='monitor.AlertDowntime.Schedule.end_time', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_date', full_name='monitor.AlertDowntime.Schedule.start_date', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_date', full_name='monitor.AlertDowntime.Schedule.end_date', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repeat_on', full_name='monitor.AlertDowntime.Schedule.repeat_on', index=5,
      number=6, type=9, cpp_type=9, label=3,
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
  serialized_start=294,
  serialized_end=413,
)

_ALERTDOWNTIME = _descriptor.Descriptor(
  name='AlertDowntime',
  full_name='monitor.AlertDowntime',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='monitor.AlertDowntime.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alert_rule_id', full_name='monitor.AlertDowntime.alert_rule_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alert_dims', full_name='monitor.AlertDowntime.alert_dims', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='schedule', full_name='monitor.AlertDowntime.schedule', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reason', full_name='monitor.AlertDowntime.reason', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='monitor.AlertDowntime.creator', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='monitor.AlertDowntime.ctime', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='monitor.AlertDowntime.mtime', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org', full_name='monitor.AlertDowntime.org', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ALERTDOWNTIME_SCHEDULE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=75,
  serialized_end=413,
)

_ALERTDOWNTIME_SCHEDULE.containing_type = _ALERTDOWNTIME
_ALERTDOWNTIME.fields_by_name['alert_dims'].message_type = cmdb__sdk_dot_model_dot_monitor_dot_alert__dims__pb2._ALERTDIMS
_ALERTDOWNTIME.fields_by_name['schedule'].message_type = _ALERTDOWNTIME_SCHEDULE
DESCRIPTOR.message_types_by_name['AlertDowntime'] = _ALERTDOWNTIME
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AlertDowntime = _reflection.GeneratedProtocolMessageType('AlertDowntime', (_message.Message,), {

  'Schedule' : _reflection.GeneratedProtocolMessageType('Schedule', (_message.Message,), {
    'DESCRIPTOR' : _ALERTDOWNTIME_SCHEDULE,
    '__module__' : 'alert_downtime_pb2'
    # @@protoc_insertion_point(class_scope:monitor.AlertDowntime.Schedule)
    })
  ,
  'DESCRIPTOR' : _ALERTDOWNTIME,
  '__module__' : 'alert_downtime_pb2'
  # @@protoc_insertion_point(class_scope:monitor.AlertDowntime)
  })
_sym_db.RegisterMessage(AlertDowntime)
_sym_db.RegisterMessage(AlertDowntime.Schedule)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
