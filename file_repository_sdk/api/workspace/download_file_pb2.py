# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: download_file.proto

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
  name='download_file.proto',
  package='workspace',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13\x64ownload_file.proto\x12\tworkspace\x1a\x1bgoogle/protobuf/empty.proto\"T\n\x13\x44ownloadFileRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x10\n\x08\x65ncoding\x18\x02 \x01(\t\x12\n\n\x02op\x18\x03 \x01(\t\x12\x11\n\tpackageId\x18\x04 \x01(\tb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_DOWNLOADFILEREQUEST = _descriptor.Descriptor(
  name='DownloadFileRequest',
  full_name='workspace.DownloadFileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='workspace.DownloadFileRequest.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encoding', full_name='workspace.DownloadFileRequest.encoding', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='op', full_name='workspace.DownloadFileRequest.op', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageId', full_name='workspace.DownloadFileRequest.packageId', index=3,
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
  serialized_start=63,
  serialized_end=147,
)

DESCRIPTOR.message_types_by_name['DownloadFileRequest'] = _DOWNLOADFILEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DownloadFileRequest = _reflection.GeneratedProtocolMessageType('DownloadFileRequest', (_message.Message,), dict(
  DESCRIPTOR = _DOWNLOADFILEREQUEST,
  __module__ = 'download_file_pb2'
  # @@protoc_insertion_point(class_scope:workspace.DownloadFileRequest)
  ))
_sym_db.RegisterMessage(DownloadFileRequest)


# @@protoc_insertion_point(module_scope)
