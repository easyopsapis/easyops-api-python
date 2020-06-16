# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tf_lock_info.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tf_lock_info.proto',
  package='cmdb',
  syntax='proto3',
  serialized_options=_b('Z>go.easyops.local/contracts/protorepo-models/easyops/model/cmdb'),
  serialized_pb=_b('\n\x12tf_lock_info.proto\x12\x04\x63mdb\"v\n\nTFLockInfo\x12\n\n\x02ID\x18\x01 \x01(\t\x12\x11\n\tOperation\x18\x02 \x01(\t\x12\x0c\n\x04Info\x18\x03 \x01(\t\x12\x0b\n\x03Who\x18\x04 \x01(\t\x12\x0f\n\x07Version\x18\x05 \x01(\t\x12\x0f\n\x07\x43reated\x18\x06 \x01(\t\x12\x0c\n\x04Path\x18\x07 \x01(\tB@Z>go.easyops.local/contracts/protorepo-models/easyops/model/cmdbb\x06proto3')
)




_TFLOCKINFO = _descriptor.Descriptor(
  name='TFLockInfo',
  full_name='cmdb.TFLockInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ID', full_name='cmdb.TFLockInfo.ID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Operation', full_name='cmdb.TFLockInfo.Operation', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Info', full_name='cmdb.TFLockInfo.Info', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Who', full_name='cmdb.TFLockInfo.Who', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Version', full_name='cmdb.TFLockInfo.Version', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Created', full_name='cmdb.TFLockInfo.Created', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Path', full_name='cmdb.TFLockInfo.Path', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_end=146,
)

DESCRIPTOR.message_types_by_name['TFLockInfo'] = _TFLOCKINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TFLockInfo = _reflection.GeneratedProtocolMessageType('TFLockInfo', (_message.Message,), {
  'DESCRIPTOR' : _TFLOCKINFO,
  '__module__' : 'tf_lock_info_pb2'
  # @@protoc_insertion_point(class_scope:cmdb.TFLockInfo)
  })
_sym_db.RegisterMessage(TFLockInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
