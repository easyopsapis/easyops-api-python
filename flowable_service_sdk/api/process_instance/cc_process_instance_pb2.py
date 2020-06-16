# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cc_process_instance.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cc_process_instance.proto',
  package='process_instance',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x19\x63\x63_process_instance.proto\x12\x10process_instance\x1a\x1bgoogle/protobuf/empty.proto\"H\n CarbonCopyProcessInstanceRequest\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x10\n\x08userList\x18\x02 \x03(\t\"\x82\x01\n(CarbonCopyProcessInstanceResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12$\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x16.google.protobuf.Emptyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_CARBONCOPYPROCESSINSTANCEREQUEST = _descriptor.Descriptor(
  name='CarbonCopyProcessInstanceRequest',
  full_name='process_instance.CarbonCopyProcessInstanceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='process_instance.CarbonCopyProcessInstanceRequest.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userList', full_name='process_instance.CarbonCopyProcessInstanceRequest.userList', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=76,
  serialized_end=148,
)


_CARBONCOPYPROCESSINSTANCERESPONSEWRAPPER = _descriptor.Descriptor(
  name='CarbonCopyProcessInstanceResponseWrapper',
  full_name='process_instance.CarbonCopyProcessInstanceResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='process_instance.CarbonCopyProcessInstanceResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='process_instance.CarbonCopyProcessInstanceResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='process_instance.CarbonCopyProcessInstanceResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='process_instance.CarbonCopyProcessInstanceResponseWrapper.data', index=3,
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
  serialized_start=151,
  serialized_end=281,
)

_CARBONCOPYPROCESSINSTANCERESPONSEWRAPPER.fields_by_name['data'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
DESCRIPTOR.message_types_by_name['CarbonCopyProcessInstanceRequest'] = _CARBONCOPYPROCESSINSTANCEREQUEST
DESCRIPTOR.message_types_by_name['CarbonCopyProcessInstanceResponseWrapper'] = _CARBONCOPYPROCESSINSTANCERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CarbonCopyProcessInstanceRequest = _reflection.GeneratedProtocolMessageType('CarbonCopyProcessInstanceRequest', (_message.Message,), {
  'DESCRIPTOR' : _CARBONCOPYPROCESSINSTANCEREQUEST,
  '__module__' : 'cc_process_instance_pb2'
  # @@protoc_insertion_point(class_scope:process_instance.CarbonCopyProcessInstanceRequest)
  })
_sym_db.RegisterMessage(CarbonCopyProcessInstanceRequest)

CarbonCopyProcessInstanceResponseWrapper = _reflection.GeneratedProtocolMessageType('CarbonCopyProcessInstanceResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _CARBONCOPYPROCESSINSTANCERESPONSEWRAPPER,
  '__module__' : 'cc_process_instance_pb2'
  # @@protoc_insertion_point(class_scope:process_instance.CarbonCopyProcessInstanceResponseWrapper)
  })
_sym_db.RegisterMessage(CarbonCopyProcessInstanceResponseWrapper)


# @@protoc_insertion_point(module_scope)