# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: delete_archive_v2.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='delete_archive_v2.proto',
  package='archive',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x17\x64\x65lete_archive_v2.proto\x12\x07\x61rchive\"g\n\x16\x44\x65leteArchiveV2Request\x12\x12\n\ndeleteFile\x18\x01 \x01(\t\x12\x13\n\x0blastVersion\x18\x02 \x01(\t\x12\x11\n\tpackageId\x18\x03 \x01(\t\x12\x11\n\tversionId\x18\x04 \x01(\t\"U\n\x17\x44\x65leteArchiveV2Response\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\r\n\x05\x65rror\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\t\"\x82\x01\n\x1e\x44\x65leteArchiveV2ResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12.\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32 .archive.DeleteArchiveV2Responseb\x06proto3')
)




_DELETEARCHIVEV2REQUEST = _descriptor.Descriptor(
  name='DeleteArchiveV2Request',
  full_name='archive.DeleteArchiveV2Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deleteFile', full_name='archive.DeleteArchiveV2Request.deleteFile', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastVersion', full_name='archive.DeleteArchiveV2Request.lastVersion', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageId', full_name='archive.DeleteArchiveV2Request.packageId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionId', full_name='archive.DeleteArchiveV2Request.versionId', index=3,
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
  serialized_start=36,
  serialized_end=139,
)


_DELETEARCHIVEV2RESPONSE = _descriptor.Descriptor(
  name='DeleteArchiveV2Response',
  full_name='archive.DeleteArchiveV2Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='archive.DeleteArchiveV2Response.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='archive.DeleteArchiveV2Response.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='archive.DeleteArchiveV2Response.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='archive.DeleteArchiveV2Response.data', index=3,
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
  serialized_start=141,
  serialized_end=226,
)


_DELETEARCHIVEV2RESPONSEWRAPPER = _descriptor.Descriptor(
  name='DeleteArchiveV2ResponseWrapper',
  full_name='archive.DeleteArchiveV2ResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='archive.DeleteArchiveV2ResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='archive.DeleteArchiveV2ResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='archive.DeleteArchiveV2ResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='archive.DeleteArchiveV2ResponseWrapper.data', index=3,
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
  serialized_start=229,
  serialized_end=359,
)

_DELETEARCHIVEV2RESPONSEWRAPPER.fields_by_name['data'].message_type = _DELETEARCHIVEV2RESPONSE
DESCRIPTOR.message_types_by_name['DeleteArchiveV2Request'] = _DELETEARCHIVEV2REQUEST
DESCRIPTOR.message_types_by_name['DeleteArchiveV2Response'] = _DELETEARCHIVEV2RESPONSE
DESCRIPTOR.message_types_by_name['DeleteArchiveV2ResponseWrapper'] = _DELETEARCHIVEV2RESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeleteArchiveV2Request = _reflection.GeneratedProtocolMessageType('DeleteArchiveV2Request', (_message.Message,), dict(
  DESCRIPTOR = _DELETEARCHIVEV2REQUEST,
  __module__ = 'delete_archive_v2_pb2'
  # @@protoc_insertion_point(class_scope:archive.DeleteArchiveV2Request)
  ))
_sym_db.RegisterMessage(DeleteArchiveV2Request)

DeleteArchiveV2Response = _reflection.GeneratedProtocolMessageType('DeleteArchiveV2Response', (_message.Message,), dict(
  DESCRIPTOR = _DELETEARCHIVEV2RESPONSE,
  __module__ = 'delete_archive_v2_pb2'
  # @@protoc_insertion_point(class_scope:archive.DeleteArchiveV2Response)
  ))
_sym_db.RegisterMessage(DeleteArchiveV2Response)

DeleteArchiveV2ResponseWrapper = _reflection.GeneratedProtocolMessageType('DeleteArchiveV2ResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _DELETEARCHIVEV2RESPONSEWRAPPER,
  __module__ = 'delete_archive_v2_pb2'
  # @@protoc_insertion_point(class_scope:archive.DeleteArchiveV2ResponseWrapper)
  ))
_sym_db.RegisterMessage(DeleteArchiveV2ResponseWrapper)


# @@protoc_insertion_point(module_scope)