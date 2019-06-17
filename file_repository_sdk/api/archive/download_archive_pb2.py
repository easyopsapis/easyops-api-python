# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: download_archive.proto

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
  name='download_archive.proto',
  package='archive',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16\x64ownload_archive.proto\x12\x07\x61rchive\x1a\x1bgoogle/protobuf/empty.proto\"^\n\x16\x44ownloadArchiveRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x10\n\x08\x65ncoding\x18\x02 \x01(\t\x12\x11\n\tpackageId\x18\x03 \x01(\t\x12\x11\n\tversionId\x18\x04 \x01(\tb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_DOWNLOADARCHIVEREQUEST = _descriptor.Descriptor(
  name='DownloadArchiveRequest',
  full_name='archive.DownloadArchiveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='archive.DownloadArchiveRequest.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encoding', full_name='archive.DownloadArchiveRequest.encoding', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageId', full_name='archive.DownloadArchiveRequest.packageId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionId', full_name='archive.DownloadArchiveRequest.versionId', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=64,
  serialized_end=158,
)

DESCRIPTOR.message_types_by_name['DownloadArchiveRequest'] = _DOWNLOADARCHIVEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DownloadArchiveRequest = _reflection.GeneratedProtocolMessageType('DownloadArchiveRequest', (_message.Message,), dict(
  DESCRIPTOR = _DOWNLOADARCHIVEREQUEST,
  __module__ = 'download_archive_pb2'
  # @@protoc_insertion_point(class_scope:archive.DownloadArchiveRequest)
  ))
_sym_db.RegisterMessage(DownloadArchiveRequest)


# @@protoc_insertion_point(module_scope)