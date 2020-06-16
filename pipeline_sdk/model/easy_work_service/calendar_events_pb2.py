# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calendar_events.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='calendar_events.proto',
  package='easy_work_service',
  syntax='proto3',
  serialized_options=_b('ZKgo.easyops.local/contracts/protorepo-models/easyops/model/easy_work_service'),
  serialized_pb=_b('\n\x15\x63\x61lendar_events.proto\x12\x11\x65\x61sy_work_service\"\xa4\x02\n\x0e\x43\x61lendarEvents\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\teventName\x18\x02 \x01(\t\x12\x10\n\x08\x63\x61lendar\x18\x03 \x01(\t\x12\x0f\n\x07members\x18\x04 \x03(\t\x12\x0f\n\x07\x63reator\x18\x05 \x01(\t\x12\x10\n\x08modifier\x18\x06 \x01(\t\x12\x0c\n\x04type\x18\x07 \x01(\t\x12\x10\n\x08startDay\x18\x08 \x01(\t\x12\x11\n\tstartTime\x18\t \x01(\t\x12\x0e\n\x06\x65ndDay\x18\n \x01(\t\x12\x0f\n\x07\x65ndTime\x18\x0b \x01(\t\x12\x0c\n\x04memo\x18\x0c \x01(\t\x12\r\n\x05level\x18\r \x01(\t\x12\x11\n\tisDeleted\x18\x0e \x01(\x08\x12\x0b\n\x03org\x18\x0f \x01(\x05\x12\r\n\x05\x63time\x18\x10 \x01(\t\x12\r\n\x05mtime\x18\x11 \x01(\tBMZKgo.easyops.local/contracts/protorepo-models/easyops/model/easy_work_serviceb\x06proto3')
)




_CALENDAREVENTS = _descriptor.Descriptor(
  name='CalendarEvents',
  full_name='easy_work_service.CalendarEvents',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='easy_work_service.CalendarEvents.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eventName', full_name='easy_work_service.CalendarEvents.eventName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='calendar', full_name='easy_work_service.CalendarEvents.calendar', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='members', full_name='easy_work_service.CalendarEvents.members', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='easy_work_service.CalendarEvents.creator', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='modifier', full_name='easy_work_service.CalendarEvents.modifier', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='easy_work_service.CalendarEvents.type', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startDay', full_name='easy_work_service.CalendarEvents.startDay', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='easy_work_service.CalendarEvents.startTime', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endDay', full_name='easy_work_service.CalendarEvents.endDay', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endTime', full_name='easy_work_service.CalendarEvents.endTime', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='easy_work_service.CalendarEvents.memo', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level', full_name='easy_work_service.CalendarEvents.level', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isDeleted', full_name='easy_work_service.CalendarEvents.isDeleted', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org', full_name='easy_work_service.CalendarEvents.org', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='easy_work_service.CalendarEvents.ctime', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='easy_work_service.CalendarEvents.mtime', index=16,
      number=17, type=9, cpp_type=9, label=1,
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
  serialized_start=45,
  serialized_end=337,
)

DESCRIPTOR.message_types_by_name['CalendarEvents'] = _CALENDAREVENTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CalendarEvents = _reflection.GeneratedProtocolMessageType('CalendarEvents', (_message.Message,), {
  'DESCRIPTOR' : _CALENDAREVENTS,
  '__module__' : 'calendar_events_pb2'
  # @@protoc_insertion_point(class_scope:easy_work_service.CalendarEvents)
  })
_sym_db.RegisterMessage(CalendarEvents)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
