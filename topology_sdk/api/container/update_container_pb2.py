# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: update_container.proto

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
  name='update_container.proto',
  package='container',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16update_container.proto\x12\tcontainer\x1a*topology_sdk/model/topology/property.proto\"\x87\x02\n\x16UpdateContainerRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\ndataSource\x18\x03 \x01(\t\x12$\n\x08property\x18\x04 \x01(\x0b\x32\x12.topology.Property\x12\x36\n\x05style\x18\x05 \x01(\x0b\x32\'.container.UpdateContainerRequest.Style\x12\x10\n\x08\x63ollapse\x18\x06 \x01(\x08\x1aO\n\x05Style\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\r\n\x05width\x18\x03 \x01(\x02\x12\x0e\n\x06height\x18\x04 \x01(\x02\x12\x11\n\tclassName\x18\x05 \x01(\t\"%\n\x17UpdateContainerResponse\x12\n\n\x02id\x18\x01 \x01(\t\"\x84\x01\n\x1eUpdateContainerResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x30\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\".container.UpdateContainerResponseb\x06proto3')
  ,
  dependencies=[topology__sdk_dot_model_dot_topology_dot_property__pb2.DESCRIPTOR,])




_UPDATECONTAINERREQUEST_STYLE = _descriptor.Descriptor(
  name='Style',
  full_name='container.UpdateContainerRequest.Style',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='container.UpdateContainerRequest.Style.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='container.UpdateContainerRequest.Style.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='container.UpdateContainerRequest.Style.width', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='container.UpdateContainerRequest.Style.height', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='className', full_name='container.UpdateContainerRequest.Style.className', index=4,
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
  serialized_start=266,
  serialized_end=345,
)

_UPDATECONTAINERREQUEST = _descriptor.Descriptor(
  name='UpdateContainerRequest',
  full_name='container.UpdateContainerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='container.UpdateContainerRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='container.UpdateContainerRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataSource', full_name='container.UpdateContainerRequest.dataSource', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='property', full_name='container.UpdateContainerRequest.property', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='style', full_name='container.UpdateContainerRequest.style', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collapse', full_name='container.UpdateContainerRequest.collapse', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_UPDATECONTAINERREQUEST_STYLE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=82,
  serialized_end=345,
)


_UPDATECONTAINERRESPONSE = _descriptor.Descriptor(
  name='UpdateContainerResponse',
  full_name='container.UpdateContainerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='container.UpdateContainerResponse.id', index=0,
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
  serialized_start=347,
  serialized_end=384,
)


_UPDATECONTAINERRESPONSEWRAPPER = _descriptor.Descriptor(
  name='UpdateContainerResponseWrapper',
  full_name='container.UpdateContainerResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='container.UpdateContainerResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='container.UpdateContainerResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='container.UpdateContainerResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='container.UpdateContainerResponseWrapper.data', index=3,
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
  serialized_start=387,
  serialized_end=519,
)

_UPDATECONTAINERREQUEST_STYLE.containing_type = _UPDATECONTAINERREQUEST
_UPDATECONTAINERREQUEST.fields_by_name['property'].message_type = topology__sdk_dot_model_dot_topology_dot_property__pb2._PROPERTY
_UPDATECONTAINERREQUEST.fields_by_name['style'].message_type = _UPDATECONTAINERREQUEST_STYLE
_UPDATECONTAINERRESPONSEWRAPPER.fields_by_name['data'].message_type = _UPDATECONTAINERRESPONSE
DESCRIPTOR.message_types_by_name['UpdateContainerRequest'] = _UPDATECONTAINERREQUEST
DESCRIPTOR.message_types_by_name['UpdateContainerResponse'] = _UPDATECONTAINERRESPONSE
DESCRIPTOR.message_types_by_name['UpdateContainerResponseWrapper'] = _UPDATECONTAINERRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateContainerRequest = _reflection.GeneratedProtocolMessageType('UpdateContainerRequest', (_message.Message,), {

  'Style' : _reflection.GeneratedProtocolMessageType('Style', (_message.Message,), {
    'DESCRIPTOR' : _UPDATECONTAINERREQUEST_STYLE,
    '__module__' : 'update_container_pb2'
    # @@protoc_insertion_point(class_scope:container.UpdateContainerRequest.Style)
    })
  ,
  'DESCRIPTOR' : _UPDATECONTAINERREQUEST,
  '__module__' : 'update_container_pb2'
  # @@protoc_insertion_point(class_scope:container.UpdateContainerRequest)
  })
_sym_db.RegisterMessage(UpdateContainerRequest)
_sym_db.RegisterMessage(UpdateContainerRequest.Style)

UpdateContainerResponse = _reflection.GeneratedProtocolMessageType('UpdateContainerResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATECONTAINERRESPONSE,
  '__module__' : 'update_container_pb2'
  # @@protoc_insertion_point(class_scope:container.UpdateContainerResponse)
  })
_sym_db.RegisterMessage(UpdateContainerResponse)

UpdateContainerResponseWrapper = _reflection.GeneratedProtocolMessageType('UpdateContainerResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _UPDATECONTAINERRESPONSEWRAPPER,
  '__module__' : 'update_container_pb2'
  # @@protoc_insertion_point(class_scope:container.UpdateContainerResponseWrapper)
  })
_sym_db.RegisterMessage(UpdateContainerResponseWrapper)


# @@protoc_insertion_point(module_scope)
