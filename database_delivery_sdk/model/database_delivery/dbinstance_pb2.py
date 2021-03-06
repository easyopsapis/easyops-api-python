# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dbinstance.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dbinstance.proto',
  package='database_delivery',
  syntax='proto3',
  serialized_options=_b('ZKgo.easyops.local/contracts/protorepo-models/easyops/model/database_delivery'),
  serialized_pb=_b('\n\x10\x64\x62instance.proto\x12\x11\x64\x61tabase_delivery\"\x9e\x01\n\nDBInstance\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06\x64\x62Name\x18\x03 \x01(\t\x12\n\n\x02ip\x18\x04 \x01(\t\x12\x0c\n\x04port\x18\x05 \x01(\x05\x12\x0f\n\x07\x63onnURL\x18\x06 \x01(\t\x12\x10\n\x08userName\x18\x07 \x01(\t\x12\x10\n\x08password\x18\x08 \x01(\t\x12\x0f\n\x07isValid\x18\t \x01(\tBMZKgo.easyops.local/contracts/protorepo-models/easyops/model/database_deliveryb\x06proto3')
)




_DBINSTANCE = _descriptor.Descriptor(
  name='DBInstance',
  full_name='database_delivery.DBInstance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='database_delivery.DBInstance.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='database_delivery.DBInstance.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dbName', full_name='database_delivery.DBInstance.dbName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip', full_name='database_delivery.DBInstance.ip', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='database_delivery.DBInstance.port', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connURL', full_name='database_delivery.DBInstance.connURL', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userName', full_name='database_delivery.DBInstance.userName', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='database_delivery.DBInstance.password', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isValid', full_name='database_delivery.DBInstance.isValid', index=8,
      number=9, type=9, cpp_type=9, label=1,
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
  serialized_start=40,
  serialized_end=198,
)

DESCRIPTOR.message_types_by_name['DBInstance'] = _DBINSTANCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DBInstance = _reflection.GeneratedProtocolMessageType('DBInstance', (_message.Message,), {
  'DESCRIPTOR' : _DBINSTANCE,
  '__module__' : 'dbinstance_pb2'
  # @@protoc_insertion_point(class_scope:database_delivery.DBInstance)
  })
_sym_db.RegisterMessage(DBInstance)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
