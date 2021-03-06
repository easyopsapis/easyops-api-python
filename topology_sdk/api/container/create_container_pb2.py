# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: create_container.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from topology_sdk.model.topology import property_pb2 as topology__sdk_dot_model_dot_topology_dot_property__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='create_container.proto',
  package='container',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16\x63reate_container.proto\x12\tcontainer\x1a*topology_sdk/model/topology/property.proto\"\xfb\x01\n\x16\x43reateContainerRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ndataSource\x18\x02 \x01(\t\x12$\n\x08property\x18\x03 \x01(\x0b\x32\x12.topology.Property\x12\x36\n\x05style\x18\x04 \x01(\x0b\x32\'.container.CreateContainerRequest.Style\x12\x10\n\x08\x63ollapse\x18\x05 \x01(\x08\x1aO\n\x05Style\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\r\n\x05width\x18\x03 \x01(\x02\x12\x0e\n\x06height\x18\x04 \x01(\x02\x12\x11\n\tclassName\x18\x05 \x01(\t\"%\n\x17\x43reateContainerResponse\x12\n\n\x02id\x18\x01 \x01(\t\"\x84\x01\n\x1e\x43reateContainerResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x30\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\".container.CreateContainerResponseb\x06proto3')
  ,
  dependencies=[topology__sdk_dot_model_dot_topology_dot_property__pb2.DESCRIPTOR,])




_CREATECONTAINERREQUEST_STYLE = _descriptor.Descriptor(
  name='Style',
  full_name='container.CreateContainerRequest.Style',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='container.CreateContainerRequest.Style.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='container.CreateContainerRequest.Style.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='container.CreateContainerRequest.Style.width', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='container.CreateContainerRequest.Style.height', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='className', full_name='container.CreateContainerRequest.Style.className', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=254,
  serialized_end=333,
)

_CREATECONTAINERREQUEST = _descriptor.Descriptor(
  name='CreateContainerRequest',
  full_name='container.CreateContainerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='container.CreateContainerRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataSource', full_name='container.CreateContainerRequest.dataSource', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='property', full_name='container.CreateContainerRequest.property', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='style', full_name='container.CreateContainerRequest.style', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collapse', full_name='container.CreateContainerRequest.collapse', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CREATECONTAINERREQUEST_STYLE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=82,
  serialized_end=333,
)


_CREATECONTAINERRESPONSE = _descriptor.Descriptor(
  name='CreateContainerResponse',
  full_name='container.CreateContainerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='container.CreateContainerResponse.id', index=0,
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
  serialized_start=335,
  serialized_end=372,
)


_CREATECONTAINERRESPONSEWRAPPER = _descriptor.Descriptor(
  name='CreateContainerResponseWrapper',
  full_name='container.CreateContainerResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='container.CreateContainerResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='container.CreateContainerResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='container.CreateContainerResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='container.CreateContainerResponseWrapper.data', index=3,
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
  serialized_start=375,
  serialized_end=507,
)

_CREATECONTAINERREQUEST_STYLE.containing_type = _CREATECONTAINERREQUEST
_CREATECONTAINERREQUEST.fields_by_name['property'].message_type = topology__sdk_dot_model_dot_topology_dot_property__pb2._PROPERTY
_CREATECONTAINERREQUEST.fields_by_name['style'].message_type = _CREATECONTAINERREQUEST_STYLE
_CREATECONTAINERRESPONSEWRAPPER.fields_by_name['data'].message_type = _CREATECONTAINERRESPONSE
DESCRIPTOR.message_types_by_name['CreateContainerRequest'] = _CREATECONTAINERREQUEST
DESCRIPTOR.message_types_by_name['CreateContainerResponse'] = _CREATECONTAINERRESPONSE
DESCRIPTOR.message_types_by_name['CreateContainerResponseWrapper'] = _CREATECONTAINERRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateContainerRequest = _reflection.GeneratedProtocolMessageType('CreateContainerRequest', (_message.Message,), {

  'Style' : _reflection.GeneratedProtocolMessageType('Style', (_message.Message,), {
    'DESCRIPTOR' : _CREATECONTAINERREQUEST_STYLE,
    '__module__' : 'create_container_pb2'
    # @@protoc_insertion_point(class_scope:container.CreateContainerRequest.Style)
    })
  ,
  'DESCRIPTOR' : _CREATECONTAINERREQUEST,
  '__module__' : 'create_container_pb2'
  # @@protoc_insertion_point(class_scope:container.CreateContainerRequest)
  })
_sym_db.RegisterMessage(CreateContainerRequest)
_sym_db.RegisterMessage(CreateContainerRequest.Style)

CreateContainerResponse = _reflection.GeneratedProtocolMessageType('CreateContainerResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATECONTAINERRESPONSE,
  '__module__' : 'create_container_pb2'
  # @@protoc_insertion_point(class_scope:container.CreateContainerResponse)
  })
_sym_db.RegisterMessage(CreateContainerResponse)

CreateContainerResponseWrapper = _reflection.GeneratedProtocolMessageType('CreateContainerResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _CREATECONTAINERRESPONSEWRAPPER,
  '__module__' : 'create_container_pb2'
  # @@protoc_insertion_point(class_scope:container.CreateContainerResponseWrapper)
  })
_sym_db.RegisterMessage(CreateContainerResponseWrapper)


# @@protoc_insertion_point(module_scope)
