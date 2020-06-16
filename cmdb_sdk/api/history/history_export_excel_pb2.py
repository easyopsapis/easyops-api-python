# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: history_export_excel.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='history_export_excel.proto',
  package='history',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1ahistory_export_excel.proto\x12\x07history\x1a\x1bgoogle/protobuf/empty.proto\"\xe2\x01\n\x19HistoryExportExcelRequest\x12\x11\n\tobject_id\x18\x01 \x01(\t\x12\x12\n\ninstanceId\x18\x02 \x01(\t\x12\x10\n\x08operator\x18\x03 \x01(\t\x12\r\n\x05\x65vent\x18\x04 \x01(\t\x12\x15\n\rexclude_event\x18\x05 \x01(\t\x12\x17\n\x0fparent_event_id\x18\x06 \x01(\t\x12\r\n\x05range\x18\x07 \x01(\t\x12\n\n\x02st\x18\x08 \x01(\t\x12\n\n\x02\x65t\x18\t \x01(\t\x12\x15\n\rwith_children\x18\n \x01(\x08\x12\x0f\n\x07is_next\x18\x0b \x01(\x08\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_HISTORYEXPORTEXCELREQUEST = _descriptor.Descriptor(
  name='HistoryExportExcelRequest',
  full_name='history.HistoryExportExcelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_id', full_name='history.HistoryExportExcelRequest.object_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='history.HistoryExportExcelRequest.instanceId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operator', full_name='history.HistoryExportExcelRequest.operator', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event', full_name='history.HistoryExportExcelRequest.event', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exclude_event', full_name='history.HistoryExportExcelRequest.exclude_event', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent_event_id', full_name='history.HistoryExportExcelRequest.parent_event_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='range', full_name='history.HistoryExportExcelRequest.range', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='st', full_name='history.HistoryExportExcelRequest.st', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='et', full_name='history.HistoryExportExcelRequest.et', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='with_children', full_name='history.HistoryExportExcelRequest.with_children', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_next', full_name='history.HistoryExportExcelRequest.is_next', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=69,
  serialized_end=295,
)

DESCRIPTOR.message_types_by_name['HistoryExportExcelRequest'] = _HISTORYEXPORTEXCELREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HistoryExportExcelRequest = _reflection.GeneratedProtocolMessageType('HistoryExportExcelRequest', (_message.Message,), {
  'DESCRIPTOR' : _HISTORYEXPORTEXCELREQUEST,
  '__module__' : 'history_export_excel_pb2'
  # @@protoc_insertion_point(class_scope:history.HistoryExportExcelRequest)
  })
_sym_db.RegisterMessage(HistoryExportExcelRequest)


# @@protoc_insertion_point(module_scope)