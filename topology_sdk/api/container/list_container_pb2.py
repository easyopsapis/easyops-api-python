# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list_container.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from model.topology import container_pb2 as model_dot_topology_dot_container__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='list_container.proto',
  package='container',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14list_container.proto\x12\tcontainer\x1a\x1emodel/topology/container.proto\"6\n\x14ListContainerRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x10\n\x08pageSize\x18\x02 \x01(\x05\"j\n\x15ListContainerResponse\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12!\n\x04list\x18\x04 \x03(\x0b\x32\x13.topology.Container\"\x80\x01\n\x1cListContainerResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12.\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32 .container.ListContainerResponseb\x06proto3')
  ,
  dependencies=[model_dot_topology_dot_container__pb2.DESCRIPTOR,])




_LISTCONTAINERREQUEST = _descriptor.Descriptor(
  name='ListContainerRequest',
  full_name='container.ListContainerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='container.ListContainerRequest.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='container.ListContainerRequest.pageSize', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=67,
  serialized_end=121,
)


_LISTCONTAINERRESPONSE = _descriptor.Descriptor(
  name='ListContainerResponse',
  full_name='container.ListContainerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='container.ListContainerResponse.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='container.ListContainerResponse.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='container.ListContainerResponse.total', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='container.ListContainerResponse.list', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=123,
  serialized_end=229,
)


_LISTCONTAINERRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListContainerResponseWrapper',
  full_name='container.ListContainerResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='container.ListContainerResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='container.ListContainerResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='container.ListContainerResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='container.ListContainerResponseWrapper.data', index=3,
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
  serialized_start=232,
  serialized_end=360,
)

_LISTCONTAINERRESPONSE.fields_by_name['list'].message_type = model_dot_topology_dot_container__pb2._CONTAINER
_LISTCONTAINERRESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTCONTAINERRESPONSE
DESCRIPTOR.message_types_by_name['ListContainerRequest'] = _LISTCONTAINERREQUEST
DESCRIPTOR.message_types_by_name['ListContainerResponse'] = _LISTCONTAINERRESPONSE
DESCRIPTOR.message_types_by_name['ListContainerResponseWrapper'] = _LISTCONTAINERRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListContainerRequest = _reflection.GeneratedProtocolMessageType('ListContainerRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTCONTAINERREQUEST,
  __module__ = 'list_container_pb2'
  # @@protoc_insertion_point(class_scope:container.ListContainerRequest)
  ))
_sym_db.RegisterMessage(ListContainerRequest)

ListContainerResponse = _reflection.GeneratedProtocolMessageType('ListContainerResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTCONTAINERRESPONSE,
  __module__ = 'list_container_pb2'
  # @@protoc_insertion_point(class_scope:container.ListContainerResponse)
  ))
_sym_db.RegisterMessage(ListContainerResponse)

ListContainerResponseWrapper = _reflection.GeneratedProtocolMessageType('ListContainerResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _LISTCONTAINERRESPONSEWRAPPER,
  __module__ = 'list_container_pb2'
  # @@protoc_insertion_point(class_scope:container.ListContainerResponseWrapper)
  ))
_sym_db.RegisterMessage(ListContainerResponseWrapper)


# @@protoc_insertion_point(module_scope)