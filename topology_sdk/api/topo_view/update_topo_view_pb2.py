# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: update_topo_view.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from topology_sdk.model.topology import topo_view_pb2 as topology__sdk_dot_model_dot_topology_dot_topo__view__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='update_topo_view.proto',
  package='topo_view',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16update_topo_view.proto\x12\ttopo_view\x1a+topology_sdk/model/topology/topo_view.proto\"M\n\x15UpdateTopoViewRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\t\"s\n\x1dUpdateTopoViewResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12 \n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x12.topology.TopoViewb\x06proto3')
  ,
  dependencies=[topology__sdk_dot_model_dot_topology_dot_topo__view__pb2.DESCRIPTOR,])




_UPDATETOPOVIEWREQUEST = _descriptor.Descriptor(
  name='UpdateTopoViewRequest',
  full_name='topo_view.UpdateTopoViewRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='topo_view.UpdateTopoViewRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='topo_view.UpdateTopoViewRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='topo_view.UpdateTopoViewRequest.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='topo_view.UpdateTopoViewRequest.data', index=3,
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
  serialized_start=82,
  serialized_end=159,
)


_UPDATETOPOVIEWRESPONSEWRAPPER = _descriptor.Descriptor(
  name='UpdateTopoViewResponseWrapper',
  full_name='topo_view.UpdateTopoViewResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='topo_view.UpdateTopoViewResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='topo_view.UpdateTopoViewResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='topo_view.UpdateTopoViewResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='topo_view.UpdateTopoViewResponseWrapper.data', index=3,
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
  serialized_start=161,
  serialized_end=276,
)

_UPDATETOPOVIEWRESPONSEWRAPPER.fields_by_name['data'].message_type = topology__sdk_dot_model_dot_topology_dot_topo__view__pb2._TOPOVIEW
DESCRIPTOR.message_types_by_name['UpdateTopoViewRequest'] = _UPDATETOPOVIEWREQUEST
DESCRIPTOR.message_types_by_name['UpdateTopoViewResponseWrapper'] = _UPDATETOPOVIEWRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateTopoViewRequest = _reflection.GeneratedProtocolMessageType('UpdateTopoViewRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATETOPOVIEWREQUEST,
  '__module__' : 'update_topo_view_pb2'
  # @@protoc_insertion_point(class_scope:topo_view.UpdateTopoViewRequest)
  })
_sym_db.RegisterMessage(UpdateTopoViewRequest)

UpdateTopoViewResponseWrapper = _reflection.GeneratedProtocolMessageType('UpdateTopoViewResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _UPDATETOPOVIEWRESPONSEWRAPPER,
  '__module__' : 'update_topo_view_pb2'
  # @@protoc_insertion_point(class_scope:topo_view.UpdateTopoViewResponseWrapper)
  })
_sym_db.RegisterMessage(UpdateTopoViewResponseWrapper)


# @@protoc_insertion_point(module_scope)
