# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: export_instance_csv.proto

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
  name='export_instance_csv.proto',
  package='instance',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x19\x65xport_instance_csv.proto\x12\x08instance\x1a\x1bgoogle/protobuf/empty.proto\";\n\x18\x45xportInstanceCsvRequest\x12\x11\n\tobject_id\x18\x01 \x01(\t\x12\x0c\n\x04json\x18\x02 \x01(\tb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_EXPORTINSTANCECSVREQUEST = _descriptor.Descriptor(
  name='ExportInstanceCsvRequest',
  full_name='instance.ExportInstanceCsvRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_id', full_name='instance.ExportInstanceCsvRequest.object_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='json', full_name='instance.ExportInstanceCsvRequest.json', index=1,
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
  serialized_start=68,
  serialized_end=127,
)

DESCRIPTOR.message_types_by_name['ExportInstanceCsvRequest'] = _EXPORTINSTANCECSVREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExportInstanceCsvRequest = _reflection.GeneratedProtocolMessageType('ExportInstanceCsvRequest', (_message.Message,), {
  'DESCRIPTOR' : _EXPORTINSTANCECSVREQUEST,
  '__module__' : 'export_instance_csv_pb2'
  # @@protoc_insertion_point(class_scope:instance.ExportInstanceCsvRequest)
  })
_sym_db.RegisterMessage(ExportInstanceCsvRequest)


# @@protoc_insertion_point(module_scope)
