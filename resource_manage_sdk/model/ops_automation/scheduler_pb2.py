# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: scheduler.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='scheduler.proto',
  package='ops_automation',
  syntax='proto3',
  serialized_options=_b('ZHgo.easyops.local/contracts/protorepo-models/easyops/model/ops_automation'),
  serialized_pb=_b('\n\x0fscheduler.proto\x12\x0eops_automation\"\xa3\x01\n\tScheduler\x12\x0f\n\x07isBound\x18\x01 \x01(\x08\x12\x10\n\x08isActive\x18\x02 \x01(\x08\x12>\n\rrecentHistory\x18\x03 \x03(\x0b\x32\'.ops_automation.Scheduler.RecentHistory\x1a\x33\n\rRecentHistory\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x12\n\ncreateTime\x18\x02 \x01(\tBJZHgo.easyops.local/contracts/protorepo-models/easyops/model/ops_automationb\x06proto3')
)




_SCHEDULER_RECENTHISTORY = _descriptor.Descriptor(
  name='RecentHistory',
  full_name='ops_automation.Scheduler.RecentHistory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='ops_automation.Scheduler.RecentHistory.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='createTime', full_name='ops_automation.Scheduler.RecentHistory.createTime', index=1,
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
  serialized_start=148,
  serialized_end=199,
)

_SCHEDULER = _descriptor.Descriptor(
  name='Scheduler',
  full_name='ops_automation.Scheduler',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='isBound', full_name='ops_automation.Scheduler.isBound', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isActive', full_name='ops_automation.Scheduler.isActive', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='recentHistory', full_name='ops_automation.Scheduler.recentHistory', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SCHEDULER_RECENTHISTORY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=199,
)

_SCHEDULER_RECENTHISTORY.containing_type = _SCHEDULER
_SCHEDULER.fields_by_name['recentHistory'].message_type = _SCHEDULER_RECENTHISTORY
DESCRIPTOR.message_types_by_name['Scheduler'] = _SCHEDULER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Scheduler = _reflection.GeneratedProtocolMessageType('Scheduler', (_message.Message,), dict(

  RecentHistory = _reflection.GeneratedProtocolMessageType('RecentHistory', (_message.Message,), dict(
    DESCRIPTOR = _SCHEDULER_RECENTHISTORY,
    __module__ = 'scheduler_pb2'
    # @@protoc_insertion_point(class_scope:ops_automation.Scheduler.RecentHistory)
    ))
  ,
  DESCRIPTOR = _SCHEDULER,
  __module__ = 'scheduler_pb2'
  # @@protoc_insertion_point(class_scope:ops_automation.Scheduler)
  ))
_sym_db.RegisterMessage(Scheduler)
_sym_db.RegisterMessage(Scheduler.RecentHistory)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
