# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: export.proto

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
  name='export.proto',
  package='info',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0c\x65xport.proto\x12\x04info\x1a\x1bgoogle/protobuf/empty.proto\"&\n\x12\x45xportSuiteRequest\x12\x10\n\x08pluginId\x18\x01 \x01(\tb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_EXPORTSUITEREQUEST = _descriptor.Descriptor(
  name='ExportSuiteRequest',
  full_name='info.ExportSuiteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pluginId', full_name='info.ExportSuiteRequest.pluginId', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=51,
  serialized_end=89,
)

DESCRIPTOR.message_types_by_name['ExportSuiteRequest'] = _EXPORTSUITEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExportSuiteRequest = _reflection.GeneratedProtocolMessageType('ExportSuiteRequest', (_message.Message,), {
  'DESCRIPTOR' : _EXPORTSUITEREQUEST,
  '__module__' : 'export_pb2'
  # @@protoc_insertion_point(class_scope:info.ExportSuiteRequest)
  })
_sym_db.RegisterMessage(ExportSuiteRequest)


# @@protoc_insertion_point(module_scope)
