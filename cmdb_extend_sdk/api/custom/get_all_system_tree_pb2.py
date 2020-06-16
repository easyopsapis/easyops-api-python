# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_all_system_tree.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cmdb_extend_sdk.model.cmdb_extend import system_dependency_pb2 as cmdb__extend__sdk_dot_model_dot_cmdb__extend_dot_system__dependency__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_all_system_tree.proto',
  package='custom',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x19get_all_system_tree.proto\x12\x06\x63ustom\x1a\x39\x63mdb_extend_sdk/model/cmdb_extend/system_dependency.proto\"J\n\x18GetAllSystemTreeResponse\x12.\n\x07systems\x18\x01 \x03(\x0b\x32\x1d.cmdb_extend.SystemDependency\"\x83\x01\n\x1fGetAllSystemTreeResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12.\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32 .custom.GetAllSystemTreeResponseb\x06proto3')
  ,
  dependencies=[cmdb__extend__sdk_dot_model_dot_cmdb__extend_dot_system__dependency__pb2.DESCRIPTOR,])




_GETALLSYSTEMTREERESPONSE = _descriptor.Descriptor(
  name='GetAllSystemTreeResponse',
  full_name='custom.GetAllSystemTreeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='systems', full_name='custom.GetAllSystemTreeResponse.systems', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=96,
  serialized_end=170,
)


_GETALLSYSTEMTREERESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetAllSystemTreeResponseWrapper',
  full_name='custom.GetAllSystemTreeResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='custom.GetAllSystemTreeResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='custom.GetAllSystemTreeResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='custom.GetAllSystemTreeResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='custom.GetAllSystemTreeResponseWrapper.data', index=3,
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
  serialized_start=173,
  serialized_end=304,
)

_GETALLSYSTEMTREERESPONSE.fields_by_name['systems'].message_type = cmdb__extend__sdk_dot_model_dot_cmdb__extend_dot_system__dependency__pb2._SYSTEMDEPENDENCY
_GETALLSYSTEMTREERESPONSEWRAPPER.fields_by_name['data'].message_type = _GETALLSYSTEMTREERESPONSE
DESCRIPTOR.message_types_by_name['GetAllSystemTreeResponse'] = _GETALLSYSTEMTREERESPONSE
DESCRIPTOR.message_types_by_name['GetAllSystemTreeResponseWrapper'] = _GETALLSYSTEMTREERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetAllSystemTreeResponse = _reflection.GeneratedProtocolMessageType('GetAllSystemTreeResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETALLSYSTEMTREERESPONSE,
  '__module__' : 'get_all_system_tree_pb2'
  # @@protoc_insertion_point(class_scope:custom.GetAllSystemTreeResponse)
  })
_sym_db.RegisterMessage(GetAllSystemTreeResponse)

GetAllSystemTreeResponseWrapper = _reflection.GeneratedProtocolMessageType('GetAllSystemTreeResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _GETALLSYSTEMTREERESPONSEWRAPPER,
  '__module__' : 'get_all_system_tree_pb2'
  # @@protoc_insertion_point(class_scope:custom.GetAllSystemTreeResponseWrapper)
  })
_sym_db.RegisterMessage(GetAllSystemTreeResponseWrapper)


# @@protoc_insertion_point(module_scope)
