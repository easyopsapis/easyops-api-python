# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: resource_list.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='resource_list.proto',
  package='container',
  syntax='proto3',
  serialized_options=_b('ZCgo.easyops.local/contracts/protorepo-models/easyops/model/container'),
  serialized_pb=_b('\n\x13resource_list.proto\x12\tcontainer\"+\n\x0cResourceList\x12\x0b\n\x03\x63pu\x18\x01 \x01(\t\x12\x0e\n\x06memory\x18\x02 \x01(\tBEZCgo.easyops.local/contracts/protorepo-models/easyops/model/containerb\x06proto3')
)




_RESOURCELIST = _descriptor.Descriptor(
  name='ResourceList',
  full_name='container.ResourceList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cpu', full_name='container.ResourceList.cpu', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memory', full_name='container.ResourceList.memory', index=1,
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
  serialized_start=34,
  serialized_end=77,
)

DESCRIPTOR.message_types_by_name['ResourceList'] = _RESOURCELIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResourceList = _reflection.GeneratedProtocolMessageType('ResourceList', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCELIST,
  '__module__' : 'resource_list_pb2'
  # @@protoc_insertion_point(class_scope:container.ResourceList)
  })
_sym_db.RegisterMessage(ResourceList)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)