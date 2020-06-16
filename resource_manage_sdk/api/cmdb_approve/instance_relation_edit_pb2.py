# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: instance_relation_edit.proto

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
  name='instance_relation_edit.proto',
  package='cmdb_approve',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1cinstance_relation_edit.proto\x12\x0c\x63mdb_approve\x1a\x1bgoogle/protobuf/empty.proto\"\xa1\x01\n\x1bInstanceRelationEditRequest\x12\x11\n\tobject_id\x18\x01 \x01(\t\x12\x18\n\x10relation_side_id\x18\x02 \x01(\t\x12\x11\n\toperation\x18\x03 \x01(\t\x12\x0e\n\x06source\x18\x04 \x01(\t\x12\x14\n\x0cinstance_ids\x18\x05 \x03(\t\x12\x1c\n\x14related_instance_ids\x18\x06 \x03(\t\"}\n#InstanceRelationEditResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12$\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x16.google.protobuf.Emptyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_INSTANCERELATIONEDITREQUEST = _descriptor.Descriptor(
  name='InstanceRelationEditRequest',
  full_name='cmdb_approve.InstanceRelationEditRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_id', full_name='cmdb_approve.InstanceRelationEditRequest.object_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relation_side_id', full_name='cmdb_approve.InstanceRelationEditRequest.relation_side_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operation', full_name='cmdb_approve.InstanceRelationEditRequest.operation', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='cmdb_approve.InstanceRelationEditRequest.source', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instance_ids', full_name='cmdb_approve.InstanceRelationEditRequest.instance_ids', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='related_instance_ids', full_name='cmdb_approve.InstanceRelationEditRequest.related_instance_ids', index=5,
      number=6, type=9, cpp_type=9, label=3,
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
  serialized_start=76,
  serialized_end=237,
)


_INSTANCERELATIONEDITRESPONSEWRAPPER = _descriptor.Descriptor(
  name='InstanceRelationEditResponseWrapper',
  full_name='cmdb_approve.InstanceRelationEditResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='cmdb_approve.InstanceRelationEditResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='cmdb_approve.InstanceRelationEditResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='cmdb_approve.InstanceRelationEditResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='cmdb_approve.InstanceRelationEditResponseWrapper.data', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=239,
  serialized_end=364,
)

_INSTANCERELATIONEDITRESPONSEWRAPPER.fields_by_name['data'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
DESCRIPTOR.message_types_by_name['InstanceRelationEditRequest'] = _INSTANCERELATIONEDITREQUEST
DESCRIPTOR.message_types_by_name['InstanceRelationEditResponseWrapper'] = _INSTANCERELATIONEDITRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InstanceRelationEditRequest = _reflection.GeneratedProtocolMessageType('InstanceRelationEditRequest', (_message.Message,), {
  'DESCRIPTOR' : _INSTANCERELATIONEDITREQUEST,
  '__module__' : 'instance_relation_edit_pb2'
  # @@protoc_insertion_point(class_scope:cmdb_approve.InstanceRelationEditRequest)
  })
_sym_db.RegisterMessage(InstanceRelationEditRequest)

InstanceRelationEditResponseWrapper = _reflection.GeneratedProtocolMessageType('InstanceRelationEditResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _INSTANCERELATIONEDITRESPONSEWRAPPER,
  '__module__' : 'instance_relation_edit_pb2'
  # @@protoc_insertion_point(class_scope:cmdb_approve.InstanceRelationEditResponseWrapper)
  })
_sym_db.RegisterMessage(InstanceRelationEditResponseWrapper)


# @@protoc_insertion_point(module_scope)
