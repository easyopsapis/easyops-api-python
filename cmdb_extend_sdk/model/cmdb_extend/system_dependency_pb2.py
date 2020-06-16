# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: system_dependency.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cmdb_extend_sdk.model.cmdb_extend import subsystem_dependency_pb2 as cmdb__extend__sdk_dot_model_dot_cmdb__extend_dot_subsystem__dependency__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='system_dependency.proto',
  package='cmdb_extend',
  syntax='proto3',
  serialized_options=_b('ZEgo.easyops.local/contracts/protorepo-models/easyops/model/cmdb_extend'),
  serialized_pb=_b('\n\x17system_dependency.proto\x12\x0b\x63mdb_extend\x1a<cmdb_extend_sdk/model/cmdb_extend/subsystem_dependency.proto\"\x94\x01\n\x10SystemDependency\x12\x14\n\x0c\x61\x62\x62reviation\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tobject_id\x18\x03 \x01(\t\x12\x13\n\x0binstance_id\x18\x04 \x01(\t\x12\x34\n\nsubsystems\x18\x05 \x03(\x0b\x32 .cmdb_extend.SubsystemDependencyBGZEgo.easyops.local/contracts/protorepo-models/easyops/model/cmdb_extendb\x06proto3')
  ,
  dependencies=[cmdb__extend__sdk_dot_model_dot_cmdb__extend_dot_subsystem__dependency__pb2.DESCRIPTOR,])




_SYSTEMDEPENDENCY = _descriptor.Descriptor(
  name='SystemDependency',
  full_name='cmdb_extend.SystemDependency',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='abbreviation', full_name='cmdb_extend.SystemDependency.abbreviation', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='cmdb_extend.SystemDependency.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object_id', full_name='cmdb_extend.SystemDependency.object_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instance_id', full_name='cmdb_extend.SystemDependency.instance_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subsystems', full_name='cmdb_extend.SystemDependency.subsystems', index=4,
      number=5, type=11, cpp_type=10, label=3,
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
  serialized_start=103,
  serialized_end=251,
)

_SYSTEMDEPENDENCY.fields_by_name['subsystems'].message_type = cmdb__extend__sdk_dot_model_dot_cmdb__extend_dot_subsystem__dependency__pb2._SUBSYSTEMDEPENDENCY
DESCRIPTOR.message_types_by_name['SystemDependency'] = _SYSTEMDEPENDENCY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SystemDependency = _reflection.GeneratedProtocolMessageType('SystemDependency', (_message.Message,), {
  'DESCRIPTOR' : _SYSTEMDEPENDENCY,
  '__module__' : 'system_dependency_pb2'
  # @@protoc_insertion_point(class_scope:cmdb_extend.SystemDependency)
  })
_sym_db.RegisterMessage(SystemDependency)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
