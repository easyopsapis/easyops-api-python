# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: target.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='target.proto',
  package='inspection',
  syntax='proto3',
  serialized_options=_b('ZDgo.easyops.local/contracts/protorepo-models/easyops/model/inspection'),
  serialized_pb=_b('\n\x0ctarget.proto\x12\ninspection\"q\n\x10InspectionTarget\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\n\n\x02ip\x18\x02 \x01(\t\x12\x10\n\x08hostname\x18\x03 \x01(\t\x12\x0c\n\x04port\x18\x04 \x01(\x05\x12\r\n\x05score\x18\x05 \x01(\x02\x12\x0e\n\x06status\x18\x06 \x01(\tBFZDgo.easyops.local/contracts/protorepo-models/easyops/model/inspectionb\x06proto3')
)




_INSPECTIONTARGET = _descriptor.Descriptor(
  name='InspectionTarget',
  full_name='inspection.InspectionTarget',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='inspection.InspectionTarget.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip', full_name='inspection.InspectionTarget.ip', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hostname', full_name='inspection.InspectionTarget.hostname', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='inspection.InspectionTarget.port', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score', full_name='inspection.InspectionTarget.score', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='inspection.InspectionTarget.status', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=28,
  serialized_end=141,
)

DESCRIPTOR.message_types_by_name['InspectionTarget'] = _INSPECTIONTARGET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InspectionTarget = _reflection.GeneratedProtocolMessageType('InspectionTarget', (_message.Message,), dict(
  DESCRIPTOR = _INSPECTIONTARGET,
  __module__ = 'target_pb2'
  # @@protoc_insertion_point(class_scope:inspection.InspectionTarget)
  ))
_sym_db.RegisterMessage(InspectionTarget)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)