# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: subsystem_dependency.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from metadata_center_sdk.model.cmdb_extend import app_dependency_pb2 as metadata__center__sdk_dot_model_dot_cmdb__extend_dot_app__dependency__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='subsystem_dependency.proto',
  package='cmdb_extend',
  syntax='proto3',
  serialized_options=_b('ZEgo.easyops.local/contracts/protorepo-models/easyops/model/cmdb_extend'),
  serialized_pb=_b('\n\x1asubsystem_dependency.proto\x12\x0b\x63mdb_extend\x1a:metadata_center_sdk/model/cmdb_extend/app_dependency.proto\"\xc2\x02\n\x13SubsystemDependency\x12\x14\n\x0c\x61\x62\x62reviation\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tobject_id\x18\x03 \x01(\t\x12\x13\n\x0binstance_id\x18\x04 \x01(\t\x12.\n\ncomponents\x18\x05 \x03(\x0b\x32\x1a.cmdb_extend.AppDependency\x12N\n\x12\x63onnect_subsystems\x18\x06 \x03(\x0b\x32\x32.cmdb_extend.SubsystemDependency.ConnectSubsystems\x1a_\n\x11\x43onnectSubsystems\x12\x14\n\x0c\x61\x62\x62reviation\x18\x01 \x01(\t\x12\x11\n\tobject_id\x18\x02 \x01(\t\x12\x13\n\x0binstance_id\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\tBGZEgo.easyops.local/contracts/protorepo-models/easyops/model/cmdb_extendb\x06proto3')
  ,
  dependencies=[metadata__center__sdk_dot_model_dot_cmdb__extend_dot_app__dependency__pb2.DESCRIPTOR,])




_SUBSYSTEMDEPENDENCY_CONNECTSUBSYSTEMS = _descriptor.Descriptor(
  name='ConnectSubsystems',
  full_name='cmdb_extend.SubsystemDependency.ConnectSubsystems',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='abbreviation', full_name='cmdb_extend.SubsystemDependency.ConnectSubsystems.abbreviation', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object_id', full_name='cmdb_extend.SubsystemDependency.ConnectSubsystems.object_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instance_id', full_name='cmdb_extend.SubsystemDependency.ConnectSubsystems.instance_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='cmdb_extend.SubsystemDependency.ConnectSubsystems.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=331,
  serialized_end=426,
)

_SUBSYSTEMDEPENDENCY = _descriptor.Descriptor(
  name='SubsystemDependency',
  full_name='cmdb_extend.SubsystemDependency',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='abbreviation', full_name='cmdb_extend.SubsystemDependency.abbreviation', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='cmdb_extend.SubsystemDependency.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object_id', full_name='cmdb_extend.SubsystemDependency.object_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instance_id', full_name='cmdb_extend.SubsystemDependency.instance_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='components', full_name='cmdb_extend.SubsystemDependency.components', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connect_subsystems', full_name='cmdb_extend.SubsystemDependency.connect_subsystems', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SUBSYSTEMDEPENDENCY_CONNECTSUBSYSTEMS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=104,
  serialized_end=426,
)

_SUBSYSTEMDEPENDENCY_CONNECTSUBSYSTEMS.containing_type = _SUBSYSTEMDEPENDENCY
_SUBSYSTEMDEPENDENCY.fields_by_name['components'].message_type = metadata__center__sdk_dot_model_dot_cmdb__extend_dot_app__dependency__pb2._APPDEPENDENCY
_SUBSYSTEMDEPENDENCY.fields_by_name['connect_subsystems'].message_type = _SUBSYSTEMDEPENDENCY_CONNECTSUBSYSTEMS
DESCRIPTOR.message_types_by_name['SubsystemDependency'] = _SUBSYSTEMDEPENDENCY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SubsystemDependency = _reflection.GeneratedProtocolMessageType('SubsystemDependency', (_message.Message,), {

  'ConnectSubsystems' : _reflection.GeneratedProtocolMessageType('ConnectSubsystems', (_message.Message,), {
    'DESCRIPTOR' : _SUBSYSTEMDEPENDENCY_CONNECTSUBSYSTEMS,
    '__module__' : 'subsystem_dependency_pb2'
    # @@protoc_insertion_point(class_scope:cmdb_extend.SubsystemDependency.ConnectSubsystems)
    })
  ,
  'DESCRIPTOR' : _SUBSYSTEMDEPENDENCY,
  '__module__' : 'subsystem_dependency_pb2'
  # @@protoc_insertion_point(class_scope:cmdb_extend.SubsystemDependency)
  })
_sym_db.RegisterMessage(SubsystemDependency)
_sym_db.RegisterMessage(SubsystemDependency.ConnectSubsystems)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
