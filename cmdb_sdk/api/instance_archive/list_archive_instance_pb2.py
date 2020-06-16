# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list_archive_instance.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='list_archive_instance.proto',
  package='instance_archive',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1blist_archive_instance.proto\x12\x10instance_archive\x1a\x1cgoogle/protobuf/struct.proto\"P\n\x1aListArchiveInstanceRequest\x12\x11\n\tobject_id\x18\x01 \x01(\t\x12\x0c\n\x04page\x18\x02 \x01(\x05\x12\x11\n\tpage_size\x18\x03 \x01(\x05\"t\n\x1bListArchiveInstanceResponse\x12%\n\x04list\x18\x01 \x03(\x0b\x32\x17.google.protobuf.Struct\x12\r\n\x05total\x18\x02 \x01(\x05\x12\x0c\n\x04page\x18\x03 \x01(\x05\x12\x11\n\tpage_size\x18\x04 \x01(\x05\"\x93\x01\n\"ListArchiveInstanceResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12;\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32-.instance_archive.ListArchiveInstanceResponseb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_LISTARCHIVEINSTANCEREQUEST = _descriptor.Descriptor(
  name='ListArchiveInstanceRequest',
  full_name='instance_archive.ListArchiveInstanceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_id', full_name='instance_archive.ListArchiveInstanceRequest.object_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page', full_name='instance_archive.ListArchiveInstanceRequest.page', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='instance_archive.ListArchiveInstanceRequest.page_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=79,
  serialized_end=159,
)


_LISTARCHIVEINSTANCERESPONSE = _descriptor.Descriptor(
  name='ListArchiveInstanceResponse',
  full_name='instance_archive.ListArchiveInstanceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='list', full_name='instance_archive.ListArchiveInstanceResponse.list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='instance_archive.ListArchiveInstanceResponse.total', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page', full_name='instance_archive.ListArchiveInstanceResponse.page', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='instance_archive.ListArchiveInstanceResponse.page_size', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=161,
  serialized_end=277,
)


_LISTARCHIVEINSTANCERESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListArchiveInstanceResponseWrapper',
  full_name='instance_archive.ListArchiveInstanceResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='instance_archive.ListArchiveInstanceResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='instance_archive.ListArchiveInstanceResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='instance_archive.ListArchiveInstanceResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='instance_archive.ListArchiveInstanceResponseWrapper.data', index=3,
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
  serialized_start=280,
  serialized_end=427,
)

_LISTARCHIVEINSTANCERESPONSE.fields_by_name['list'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_LISTARCHIVEINSTANCERESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTARCHIVEINSTANCERESPONSE
DESCRIPTOR.message_types_by_name['ListArchiveInstanceRequest'] = _LISTARCHIVEINSTANCEREQUEST
DESCRIPTOR.message_types_by_name['ListArchiveInstanceResponse'] = _LISTARCHIVEINSTANCERESPONSE
DESCRIPTOR.message_types_by_name['ListArchiveInstanceResponseWrapper'] = _LISTARCHIVEINSTANCERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListArchiveInstanceRequest = _reflection.GeneratedProtocolMessageType('ListArchiveInstanceRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTARCHIVEINSTANCEREQUEST,
  '__module__' : 'list_archive_instance_pb2'
  # @@protoc_insertion_point(class_scope:instance_archive.ListArchiveInstanceRequest)
  })
_sym_db.RegisterMessage(ListArchiveInstanceRequest)

ListArchiveInstanceResponse = _reflection.GeneratedProtocolMessageType('ListArchiveInstanceResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTARCHIVEINSTANCERESPONSE,
  '__module__' : 'list_archive_instance_pb2'
  # @@protoc_insertion_point(class_scope:instance_archive.ListArchiveInstanceResponse)
  })
_sym_db.RegisterMessage(ListArchiveInstanceResponse)

ListArchiveInstanceResponseWrapper = _reflection.GeneratedProtocolMessageType('ListArchiveInstanceResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _LISTARCHIVEINSTANCERESPONSEWRAPPER,
  '__module__' : 'list_archive_instance_pb2'
  # @@protoc_insertion_point(class_scope:instance_archive.ListArchiveInstanceResponseWrapper)
  })
_sym_db.RegisterMessage(ListArchiveInstanceResponseWrapper)


# @@protoc_insertion_point(module_scope)