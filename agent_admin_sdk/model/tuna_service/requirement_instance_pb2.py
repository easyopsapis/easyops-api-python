# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: requirement_instance.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from agent_admin_sdk.model.topboard import issue_pb2 as agent__admin__sdk_dot_model_dot_topboard_dot_issue__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='requirement_instance.proto',
  package='tuna_service',
  syntax='proto3',
  serialized_options=_b('ZFgo.easyops.local/contracts/protorepo-models/easyops/model/tuna_service'),
  serialized_pb=_b('\n\x1arequirement_instance.proto\x12\x0ctuna_service\x1a*agent_admin_sdk/model/topboard/issue.proto\x1a\x1cgoogle/protobuf/struct.proto\"\x99\x02\n\x13RequirementInstance\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08sequence\x18\x03 \x01(\t\x12\r\n\x05given\x18\x04 \x01(\t\x12\x0c\n\x04when\x18\x05 \x01(\t\x12\x0c\n\x04then\x18\x06 \x01(\t\x12\x0c\n\x04type\x18\x07 \x01(\t\x12\x17\n\x0f\x64\x61taDescription\x18\x08 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\t \x01(\t\x12\x0b\n\x03tag\x18\n \x01(\t\x12\x15\n\rinterfaceName\x18\x0b \x01(\t\x12*\n\tcontracts\x18\x0c \x03(\x0b\x32\x17.google.protobuf.Struct\x12\x1e\n\x05ISSUE\x18\r \x03(\x0b\x32\x0f.topboard.IssueBHZFgo.easyops.local/contracts/protorepo-models/easyops/model/tuna_serviceb\x06proto3')
  ,
  dependencies=[agent__admin__sdk_dot_model_dot_topboard_dot_issue__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_REQUIREMENTINSTANCE = _descriptor.Descriptor(
  name='RequirementInstance',
  full_name='tuna_service.RequirementInstance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='tuna_service.RequirementInstance.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='tuna_service.RequirementInstance.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sequence', full_name='tuna_service.RequirementInstance.sequence', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='given', full_name='tuna_service.RequirementInstance.given', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='when', full_name='tuna_service.RequirementInstance.when', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='then', full_name='tuna_service.RequirementInstance.then', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='tuna_service.RequirementInstance.type', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataDescription', full_name='tuna_service.RequirementInstance.dataDescription', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='tuna_service.RequirementInstance.data', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tag', full_name='tuna_service.RequirementInstance.tag', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interfaceName', full_name='tuna_service.RequirementInstance.interfaceName', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contracts', full_name='tuna_service.RequirementInstance.contracts', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ISSUE', full_name='tuna_service.RequirementInstance.ISSUE', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=119,
  serialized_end=400,
)

_REQUIREMENTINSTANCE.fields_by_name['contracts'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_REQUIREMENTINSTANCE.fields_by_name['ISSUE'].message_type = agent__admin__sdk_dot_model_dot_topboard_dot_issue__pb2._ISSUE
DESCRIPTOR.message_types_by_name['RequirementInstance'] = _REQUIREMENTINSTANCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequirementInstance = _reflection.GeneratedProtocolMessageType('RequirementInstance', (_message.Message,), {
  'DESCRIPTOR' : _REQUIREMENTINSTANCE,
  '__module__' : 'requirement_instance_pb2'
  # @@protoc_insertion_point(class_scope:tuna_service.RequirementInstance)
  })
_sym_db.RegisterMessage(RequirementInstance)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
