# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_system.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_system.proto',
  package='system_map',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10get_system.proto\x12\nsystem_map\"$\n\x10GetSystemRequest\x12\x10\n\x08systemId\x18\x01 \x01(\t\"p\n\x11GetSystemResponse\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\x12\x0c\n\x04icon\x18\x04 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x05 \x01(\t\x12\x0c\n\x04memo\x18\x06 \x01(\t\"y\n\x18GetSystemResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12+\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1d.system_map.GetSystemResponseb\x06proto3')
)




_GETSYSTEMREQUEST = _descriptor.Descriptor(
  name='GetSystemRequest',
  full_name='system_map.GetSystemRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='systemId', full_name='system_map.GetSystemRequest.systemId', index=0,
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
  serialized_start=32,
  serialized_end=68,
)


_GETSYSTEMRESPONSE = _descriptor.Descriptor(
  name='GetSystemResponse',
  full_name='system_map.GetSystemResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='system_map.GetSystemResponse.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='system_map.GetSystemResponse.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='system_map.GetSystemResponse.url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon', full_name='system_map.GetSystemResponse.icon', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='system_map.GetSystemResponse.category', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='system_map.GetSystemResponse.memo', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=70,
  serialized_end=182,
)


_GETSYSTEMRESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetSystemResponseWrapper',
  full_name='system_map.GetSystemResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='system_map.GetSystemResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='system_map.GetSystemResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='system_map.GetSystemResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='system_map.GetSystemResponseWrapper.data', index=3,
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
  serialized_start=184,
  serialized_end=305,
)

_GETSYSTEMRESPONSEWRAPPER.fields_by_name['data'].message_type = _GETSYSTEMRESPONSE
DESCRIPTOR.message_types_by_name['GetSystemRequest'] = _GETSYSTEMREQUEST
DESCRIPTOR.message_types_by_name['GetSystemResponse'] = _GETSYSTEMRESPONSE
DESCRIPTOR.message_types_by_name['GetSystemResponseWrapper'] = _GETSYSTEMRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetSystemRequest = _reflection.GeneratedProtocolMessageType('GetSystemRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSYSTEMREQUEST,
  '__module__' : 'get_system_pb2'
  # @@protoc_insertion_point(class_scope:system_map.GetSystemRequest)
  })
_sym_db.RegisterMessage(GetSystemRequest)

GetSystemResponse = _reflection.GeneratedProtocolMessageType('GetSystemResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSYSTEMRESPONSE,
  '__module__' : 'get_system_pb2'
  # @@protoc_insertion_point(class_scope:system_map.GetSystemResponse)
  })
_sym_db.RegisterMessage(GetSystemResponse)

GetSystemResponseWrapper = _reflection.GeneratedProtocolMessageType('GetSystemResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _GETSYSTEMRESPONSEWRAPPER,
  '__module__' : 'get_system_pb2'
  # @@protoc_insertion_point(class_scope:system_map.GetSystemResponseWrapper)
  })
_sym_db.RegisterMessage(GetSystemResponseWrapper)


# @@protoc_insertion_point(module_scope)