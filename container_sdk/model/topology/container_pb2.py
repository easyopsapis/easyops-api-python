# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: container.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from container_sdk.model.topology import property_pb2 as container__sdk_dot_model_dot_topology_dot_property__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='container.proto',
  package='topology',
  syntax='proto3',
  serialized_options=_b('ZBgo.easyops.local/contracts/protorepo-models/easyops/model/topology'),
  serialized_pb=_b('\n\x0f\x63ontainer.proto\x12\x08topology\x1a+container_sdk/model/topology/property.proto\"\xad\x02\n\tContainer\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ndataSource\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12$\n\x08property\x18\x04 \x01(\x0b\x32\x12.topology.Property\x12\x10\n\x08\x63ollapse\x18\x05 \x01(\x08\x12\x0f\n\x07\x63reator\x18\x06 \x01(\t\x12\x10\n\x08modifier\x18\x07 \x01(\t\x12\r\n\x05\x63time\x18\x08 \x01(\x05\x12\r\n\x05mtime\x18\t \x01(\x05\x12(\n\x05style\x18\n \x01(\x0b\x32\x19.topology.Container.Style\x1aO\n\x05Style\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\r\n\x05width\x18\x03 \x01(\x02\x12\x0e\n\x06height\x18\x04 \x01(\x02\x12\x11\n\tclassName\x18\x05 \x01(\tBDZBgo.easyops.local/contracts/protorepo-models/easyops/model/topologyb\x06proto3')
  ,
  dependencies=[container__sdk_dot_model_dot_topology_dot_property__pb2.DESCRIPTOR,])




_CONTAINER_STYLE = _descriptor.Descriptor(
  name='Style',
  full_name='topology.Container.Style',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='topology.Container.Style.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='topology.Container.Style.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='topology.Container.Style.width', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='topology.Container.Style.height', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='className', full_name='topology.Container.Style.className', index=4,
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
  serialized_start=297,
  serialized_end=376,
)

_CONTAINER = _descriptor.Descriptor(
  name='Container',
  full_name='topology.Container',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='topology.Container.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataSource', full_name='topology.Container.dataSource', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='topology.Container.id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='property', full_name='topology.Container.property', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collapse', full_name='topology.Container.collapse', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='topology.Container.creator', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='modifier', full_name='topology.Container.modifier', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='topology.Container.ctime', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='topology.Container.mtime', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='style', full_name='topology.Container.style', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CONTAINER_STYLE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=75,
  serialized_end=376,
)

_CONTAINER_STYLE.containing_type = _CONTAINER
_CONTAINER.fields_by_name['property'].message_type = container__sdk_dot_model_dot_topology_dot_property__pb2._PROPERTY
_CONTAINER.fields_by_name['style'].message_type = _CONTAINER_STYLE
DESCRIPTOR.message_types_by_name['Container'] = _CONTAINER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Container = _reflection.GeneratedProtocolMessageType('Container', (_message.Message,), {

  'Style' : _reflection.GeneratedProtocolMessageType('Style', (_message.Message,), {
    'DESCRIPTOR' : _CONTAINER_STYLE,
    '__module__' : 'container_pb2'
    # @@protoc_insertion_point(class_scope:topology.Container.Style)
    })
  ,
  'DESCRIPTOR' : _CONTAINER,
  '__module__' : 'container_pb2'
  # @@protoc_insertion_point(class_scope:topology.Container)
  })
_sym_db.RegisterMessage(Container)
_sym_db.RegisterMessage(Container.Style)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
