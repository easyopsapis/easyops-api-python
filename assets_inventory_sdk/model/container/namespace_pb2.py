# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: namespace.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='namespace.proto',
  package='container',
  syntax='proto3',
  serialized_options=_b('ZCgo.easyops.local/contracts/protorepo-models/easyops/model/container'),
  serialized_pb=_b('\n\x0fnamespace.proto\x12\tcontainer\"\xda\x01\n\tNamespace\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0c\n\x04kind\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x14\n\x0cresourceName\x18\x04 \x01(\t\x12\x13\n\x0b\x64isplayName\x18\x05 \x01(\t\x12\x14\n\x0cresourceSpec\x18\x06 \x01(\t\x12\x16\n\x0elimitRangeSpec\x18\x07 \x01(\t\x12\x0e\n\x06status\x18\x08 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\t \x01(\t\x12\x0e\n\x06system\x18\n \x01(\x08\x12\x0f\n\x07\x63reator\x18\x0b \x01(\tBEZCgo.easyops.local/contracts/protorepo-models/easyops/model/containerb\x06proto3')
)




_NAMESPACE = _descriptor.Descriptor(
  name='Namespace',
  full_name='container.Namespace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='container.Namespace.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kind', full_name='container.Namespace.kind', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='container.Namespace.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resourceName', full_name='container.Namespace.resourceName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='displayName', full_name='container.Namespace.displayName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resourceSpec', full_name='container.Namespace.resourceSpec', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limitRangeSpec', full_name='container.Namespace.limitRangeSpec', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='container.Namespace.status', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='container.Namespace.description', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='system', full_name='container.Namespace.system', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='container.Namespace.creator', index=10,
      number=11, type=9, cpp_type=9, label=1,
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
  serialized_start=31,
  serialized_end=249,
)

DESCRIPTOR.message_types_by_name['Namespace'] = _NAMESPACE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Namespace = _reflection.GeneratedProtocolMessageType('Namespace', (_message.Message,), {
  'DESCRIPTOR' : _NAMESPACE,
  '__module__' : 'namespace_pb2'
  # @@protoc_insertion_point(class_scope:container.Namespace)
  })
_sym_db.RegisterMessage(Namespace)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
