# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: deploy_label.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='deploy_label.proto',
  package='easy_flow',
  syntax='proto3',
  serialized_options=_b('ZCgo.easyops.local/contracts/protorepo-models/easyops/model/easy_flow'),
  serialized_pb=_b('\n\x12\x64\x65ploy_label.proto\x12\teasy_flow\"1\n\x0b\x44\x65ployLabel\x12\x0c\n\x04\x66rom\x18\x01 \x01(\t\x12\x14\n\x0cstrategyName\x18\x02 \x01(\tBEZCgo.easyops.local/contracts/protorepo-models/easyops/model/easy_flowb\x06proto3')
)




_DEPLOYLABEL = _descriptor.Descriptor(
  name='DeployLabel',
  full_name='easy_flow.DeployLabel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='from', full_name='easy_flow.DeployLabel.from', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strategyName', full_name='easy_flow.DeployLabel.strategyName', index=1,
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
  serialized_start=33,
  serialized_end=82,
)

DESCRIPTOR.message_types_by_name['DeployLabel'] = _DEPLOYLABEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeployLabel = _reflection.GeneratedProtocolMessageType('DeployLabel', (_message.Message,), {
  'DESCRIPTOR' : _DEPLOYLABEL,
  '__module__' : 'deploy_label_pb2'
  # @@protoc_insertion_point(class_scope:easy_flow.DeployLabel)
  })
_sym_db.RegisterMessage(DeployLabel)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
