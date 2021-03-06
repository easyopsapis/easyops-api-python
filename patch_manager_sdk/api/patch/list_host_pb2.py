# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list_host.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='list_host.proto',
  package='patch',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0flist_host.proto\x12\x05patch\"&\n\x0fListHostRequest\x12\x13\n\x0binstanceIds\x18\x01 \x03(\t\"\x8c\x02\n\x10ListHostResponse\x12,\n\x05hosts\x18\x01 \x03(\x0b\x32\x1d.patch.ListHostResponse.Hosts\x1a\xc9\x01\n\x05Hosts\x12\x12\n\nbusinesses\x18\x01 \x03(\t\x12\x12\n\ninstanceId\x18\x02 \x01(\t\x12\x10\n\x08hostname\x18\x03 \x01(\t\x12\n\n\x02ip\x18\x04 \x01(\t\x12\x14\n\x0c_environment\x18\x05 \x01(\t\x12\x10\n\x08osSystem\x18\x06 \x01(\t\x12\x16\n\x0eosArchitecture\x18\x07 \x01(\t\x12\x11\n\tosVersion\x18\x08 \x01(\t\x12\x11\n\tosRelease\x18\t \x01(\t\x12\x14\n\x0c_agentStatus\x18\n \x01(\t\"r\n\x17ListHostResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12%\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x17.patch.ListHostResponseb\x06proto3')
)




_LISTHOSTREQUEST = _descriptor.Descriptor(
  name='ListHostRequest',
  full_name='patch.ListHostRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceIds', full_name='patch.ListHostRequest.instanceIds', index=0,
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
  serialized_start=26,
  serialized_end=64,
)


_LISTHOSTRESPONSE_HOSTS = _descriptor.Descriptor(
  name='Hosts',
  full_name='patch.ListHostResponse.Hosts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='businesses', full_name='patch.ListHostResponse.Hosts.businesses', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='patch.ListHostResponse.Hosts.instanceId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hostname', full_name='patch.ListHostResponse.Hosts.hostname', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip', full_name='patch.ListHostResponse.Hosts.ip', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='_environment', full_name='patch.ListHostResponse.Hosts._environment', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='osSystem', full_name='patch.ListHostResponse.Hosts.osSystem', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='osArchitecture', full_name='patch.ListHostResponse.Hosts.osArchitecture', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='osVersion', full_name='patch.ListHostResponse.Hosts.osVersion', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='osRelease', full_name='patch.ListHostResponse.Hosts.osRelease', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='_agentStatus', full_name='patch.ListHostResponse.Hosts._agentStatus', index=9,
      number=10, type=9, cpp_type=9, label=1,
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
  serialized_start=134,
  serialized_end=335,
)

_LISTHOSTRESPONSE = _descriptor.Descriptor(
  name='ListHostResponse',
  full_name='patch.ListHostResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hosts', full_name='patch.ListHostResponse.hosts', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTHOSTRESPONSE_HOSTS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=67,
  serialized_end=335,
)


_LISTHOSTRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListHostResponseWrapper',
  full_name='patch.ListHostResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='patch.ListHostResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='patch.ListHostResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='patch.ListHostResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='patch.ListHostResponseWrapper.data', index=3,
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
  serialized_start=337,
  serialized_end=451,
)

_LISTHOSTRESPONSE_HOSTS.containing_type = _LISTHOSTRESPONSE
_LISTHOSTRESPONSE.fields_by_name['hosts'].message_type = _LISTHOSTRESPONSE_HOSTS
_LISTHOSTRESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTHOSTRESPONSE
DESCRIPTOR.message_types_by_name['ListHostRequest'] = _LISTHOSTREQUEST
DESCRIPTOR.message_types_by_name['ListHostResponse'] = _LISTHOSTRESPONSE
DESCRIPTOR.message_types_by_name['ListHostResponseWrapper'] = _LISTHOSTRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListHostRequest = _reflection.GeneratedProtocolMessageType('ListHostRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTHOSTREQUEST,
  '__module__' : 'list_host_pb2'
  # @@protoc_insertion_point(class_scope:patch.ListHostRequest)
  })
_sym_db.RegisterMessage(ListHostRequest)

ListHostResponse = _reflection.GeneratedProtocolMessageType('ListHostResponse', (_message.Message,), {

  'Hosts' : _reflection.GeneratedProtocolMessageType('Hosts', (_message.Message,), {
    'DESCRIPTOR' : _LISTHOSTRESPONSE_HOSTS,
    '__module__' : 'list_host_pb2'
    # @@protoc_insertion_point(class_scope:patch.ListHostResponse.Hosts)
    })
  ,
  'DESCRIPTOR' : _LISTHOSTRESPONSE,
  '__module__' : 'list_host_pb2'
  # @@protoc_insertion_point(class_scope:patch.ListHostResponse)
  })
_sym_db.RegisterMessage(ListHostResponse)
_sym_db.RegisterMessage(ListHostResponse.Hosts)

ListHostResponseWrapper = _reflection.GeneratedProtocolMessageType('ListHostResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _LISTHOSTRESPONSEWRAPPER,
  '__module__' : 'list_host_pb2'
  # @@protoc_insertion_point(class_scope:patch.ListHostResponseWrapper)
  })
_sym_db.RegisterMessage(ListHostResponseWrapper)


# @@protoc_insertion_point(module_scope)
