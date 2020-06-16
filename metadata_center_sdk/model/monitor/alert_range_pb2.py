# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: alert_range.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from metadata_center_sdk.model.monitor import alert_event_pb2 as metadata__center__sdk_dot_model_dot_monitor_dot_alert__event__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='alert_range.proto',
  package='monitor',
  syntax='proto3',
  serialized_options=_b('ZAgo.easyops.local/contracts/protorepo-models/easyops/model/monitor'),
  serialized_pb=_b('\n\x11\x61lert_range.proto\x12\x07monitor\x1a\x33metadata_center_sdk/model/monitor/alert_event.proto\"j\n\nAlertRange\x12\x0b\n\x03org\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12(\n\x0b\x66irst_alert\x18\x03 \x01(\x0b\x32\x13.monitor.AlertEvent\x12\x18\n\x10\x61lert_begin_time\x18\x04 \x01(\x05\x42\x43ZAgo.easyops.local/contracts/protorepo-models/easyops/model/monitorb\x06proto3')
  ,
  dependencies=[metadata__center__sdk_dot_model_dot_monitor_dot_alert__event__pb2.DESCRIPTOR,])




_ALERTRANGE = _descriptor.Descriptor(
  name='AlertRange',
  full_name='monitor.AlertRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='org', full_name='monitor.AlertRange.org', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='monitor.AlertRange.key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='first_alert', full_name='monitor.AlertRange.first_alert', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alert_begin_time', full_name='monitor.AlertRange.alert_begin_time', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=83,
  serialized_end=189,
)

_ALERTRANGE.fields_by_name['first_alert'].message_type = metadata__center__sdk_dot_model_dot_monitor_dot_alert__event__pb2._ALERTEVENT
DESCRIPTOR.message_types_by_name['AlertRange'] = _ALERTRANGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AlertRange = _reflection.GeneratedProtocolMessageType('AlertRange', (_message.Message,), {
  'DESCRIPTOR' : _ALERTRANGE,
  '__module__' : 'alert_range_pb2'
  # @@protoc_insertion_point(class_scope:monitor.AlertRange)
  })
_sym_db.RegisterMessage(AlertRange)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
