# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list_device_type.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='list_device_type.proto',
  package='idcrack',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16list_device_type.proto\x12\x07idcrack\"-\n\x16ListDeviceTypeResponse\x12\x13\n\x0b\x64\x65viceTypes\x18\x01 \x03(\t\"\x80\x01\n\x1dListDeviceTypeResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12-\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1f.idcrack.ListDeviceTypeResponseb\x06proto3')
)




_LISTDEVICETYPERESPONSE = _descriptor.Descriptor(
  name='ListDeviceTypeResponse',
  full_name='idcrack.ListDeviceTypeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceTypes', full_name='idcrack.ListDeviceTypeResponse.deviceTypes', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=35,
  serialized_end=80,
)


_LISTDEVICETYPERESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListDeviceTypeResponseWrapper',
  full_name='idcrack.ListDeviceTypeResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='idcrack.ListDeviceTypeResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='idcrack.ListDeviceTypeResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='idcrack.ListDeviceTypeResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='idcrack.ListDeviceTypeResponseWrapper.data', index=3,
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
  serialized_start=83,
  serialized_end=211,
)

_LISTDEVICETYPERESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTDEVICETYPERESPONSE
DESCRIPTOR.message_types_by_name['ListDeviceTypeResponse'] = _LISTDEVICETYPERESPONSE
DESCRIPTOR.message_types_by_name['ListDeviceTypeResponseWrapper'] = _LISTDEVICETYPERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListDeviceTypeResponse = _reflection.GeneratedProtocolMessageType('ListDeviceTypeResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTDEVICETYPERESPONSE,
  '__module__' : 'list_device_type_pb2'
  # @@protoc_insertion_point(class_scope:idcrack.ListDeviceTypeResponse)
  })
_sym_db.RegisterMessage(ListDeviceTypeResponse)

ListDeviceTypeResponseWrapper = _reflection.GeneratedProtocolMessageType('ListDeviceTypeResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _LISTDEVICETYPERESPONSEWRAPPER,
  '__module__' : 'list_device_type_pb2'
  # @@protoc_insertion_point(class_scope:idcrack.ListDeviceTypeResponseWrapper)
  })
_sym_db.RegisterMessage(ListDeviceTypeResponseWrapper)


# @@protoc_insertion_point(module_scope)
