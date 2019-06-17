# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_view.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from model.topology import node_pb2 as model_dot_topology_dot_node__pb2
from model.topology import link_pb2 as model_dot_topology_dot_link__pb2
from model.topology import area_pb2 as model_dot_topology_dot_area__pb2
from model.topology import note_pb2 as model_dot_topology_dot_note__pb2
from model.topology import view_pb2 as model_dot_topology_dot_view__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_view.proto',
  package='view',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0eget_view.proto\x12\x04view\x1a\x19model/topology/node.proto\x1a\x19model/topology/link.proto\x1a\x19model/topology/area.proto\x1a\x19model/topology/note.proto\x1a\x19model/topology/view.proto\"\x1c\n\x0eGetViewRequest\x12\n\n\x02id\x18\x01 \x01(\t\"h\n\x16GetViewResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x1c\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x0e.topology.Viewb\x06proto3')
  ,
  dependencies=[model_dot_topology_dot_node__pb2.DESCRIPTOR,model_dot_topology_dot_link__pb2.DESCRIPTOR,model_dot_topology_dot_area__pb2.DESCRIPTOR,model_dot_topology_dot_note__pb2.DESCRIPTOR,model_dot_topology_dot_view__pb2.DESCRIPTOR,])




_GETVIEWREQUEST = _descriptor.Descriptor(
  name='GetViewRequest',
  full_name='view.GetViewRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='view.GetViewRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=159,
  serialized_end=187,
)


_GETVIEWRESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetViewResponseWrapper',
  full_name='view.GetViewResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='view.GetViewResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='view.GetViewResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='view.GetViewResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='view.GetViewResponseWrapper.data', index=3,
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
  serialized_start=189,
  serialized_end=293,
)

_GETVIEWRESPONSEWRAPPER.fields_by_name['data'].message_type = model_dot_topology_dot_view__pb2._VIEW
DESCRIPTOR.message_types_by_name['GetViewRequest'] = _GETVIEWREQUEST
DESCRIPTOR.message_types_by_name['GetViewResponseWrapper'] = _GETVIEWRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetViewRequest = _reflection.GeneratedProtocolMessageType('GetViewRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETVIEWREQUEST,
  __module__ = 'get_view_pb2'
  # @@protoc_insertion_point(class_scope:view.GetViewRequest)
  ))
_sym_db.RegisterMessage(GetViewRequest)

GetViewResponseWrapper = _reflection.GeneratedProtocolMessageType('GetViewResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _GETVIEWRESPONSEWRAPPER,
  __module__ = 'get_view_pb2'
  # @@protoc_insertion_point(class_scope:view.GetViewResponseWrapper)
  ))
_sym_db.RegisterMessage(GetViewResponseWrapper)


# @@protoc_insertion_point(module_scope)