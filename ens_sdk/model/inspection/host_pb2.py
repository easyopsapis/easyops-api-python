# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: host.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='host.proto',
  package='inspection',
  syntax='proto3',
  serialized_options=_b('ZDgo.easyops.local/contracts/protorepo-models/easyops/model/inspection'),
  serialized_pb=_b('\n\nhost.proto\x12\ninspection\"B\n\x0eInspectionHost\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x10\n\x08hostname\x18\x02 \x01(\t\x12\n\n\x02ip\x18\x03 \x01(\tBFZDgo.easyops.local/contracts/protorepo-models/easyops/model/inspectionb\x06proto3')
)




_INSPECTIONHOST = _descriptor.Descriptor(
  name='InspectionHost',
  full_name='inspection.InspectionHost',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='inspection.InspectionHost.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hostname', full_name='inspection.InspectionHost.hostname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip', full_name='inspection.InspectionHost.ip', index=2,
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
  serialized_start=26,
  serialized_end=92,
)

DESCRIPTOR.message_types_by_name['InspectionHost'] = _INSPECTIONHOST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InspectionHost = _reflection.GeneratedProtocolMessageType('InspectionHost', (_message.Message,), {
  'DESCRIPTOR' : _INSPECTIONHOST,
  '__module__' : 'host_pb2'
  # @@protoc_insertion_point(class_scope:inspection.InspectionHost)
  })
_sym_db.RegisterMessage(InspectionHost)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)