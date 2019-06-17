# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_archive_diff_size.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_archive_diff_size.proto',
  package='archive',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1bget_archive_diff_size.proto\x12\x07\x61rchive\"I\n\x12GetDiffSizeRequest\x12\x10\n\x08ver_from\x18\x01 \x01(\t\x12\x0e\n\x06ver_to\x18\x02 \x01(\t\x12\x11\n\tpackageId\x18\x03 \x01(\t\"5\n\x13GetDiffSizeResponse\x12\x0c\n\x04size\x18\x01 \x01(\x03\x12\x10\n\x08\x64iffSize\x18\x02 \x01(\x03\"z\n\x1aGetDiffSizeResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12*\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1c.archive.GetDiffSizeResponseb\x06proto3')
)




_GETDIFFSIZEREQUEST = _descriptor.Descriptor(
  name='GetDiffSizeRequest',
  full_name='archive.GetDiffSizeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ver_from', full_name='archive.GetDiffSizeRequest.ver_from', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ver_to', full_name='archive.GetDiffSizeRequest.ver_to', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageId', full_name='archive.GetDiffSizeRequest.packageId', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=40,
  serialized_end=113,
)


_GETDIFFSIZERESPONSE = _descriptor.Descriptor(
  name='GetDiffSizeResponse',
  full_name='archive.GetDiffSizeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='size', full_name='archive.GetDiffSizeResponse.size', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='diffSize', full_name='archive.GetDiffSizeResponse.diffSize', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=115,
  serialized_end=168,
)


_GETDIFFSIZERESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetDiffSizeResponseWrapper',
  full_name='archive.GetDiffSizeResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='archive.GetDiffSizeResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='archive.GetDiffSizeResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='archive.GetDiffSizeResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='archive.GetDiffSizeResponseWrapper.data', index=3,
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
  serialized_start=170,
  serialized_end=292,
)

_GETDIFFSIZERESPONSEWRAPPER.fields_by_name['data'].message_type = _GETDIFFSIZERESPONSE
DESCRIPTOR.message_types_by_name['GetDiffSizeRequest'] = _GETDIFFSIZEREQUEST
DESCRIPTOR.message_types_by_name['GetDiffSizeResponse'] = _GETDIFFSIZERESPONSE
DESCRIPTOR.message_types_by_name['GetDiffSizeResponseWrapper'] = _GETDIFFSIZERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetDiffSizeRequest = _reflection.GeneratedProtocolMessageType('GetDiffSizeRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETDIFFSIZEREQUEST,
  __module__ = 'get_archive_diff_size_pb2'
  # @@protoc_insertion_point(class_scope:archive.GetDiffSizeRequest)
  ))
_sym_db.RegisterMessage(GetDiffSizeRequest)

GetDiffSizeResponse = _reflection.GeneratedProtocolMessageType('GetDiffSizeResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETDIFFSIZERESPONSE,
  __module__ = 'get_archive_diff_size_pb2'
  # @@protoc_insertion_point(class_scope:archive.GetDiffSizeResponse)
  ))
_sym_db.RegisterMessage(GetDiffSizeResponse)

GetDiffSizeResponseWrapper = _reflection.GeneratedProtocolMessageType('GetDiffSizeResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _GETDIFFSIZERESPONSEWRAPPER,
  __module__ = 'get_archive_diff_size_pb2'
  # @@protoc_insertion_point(class_scope:archive.GetDiffSizeResponseWrapper)
  ))
_sym_db.RegisterMessage(GetDiffSizeResponseWrapper)


# @@protoc_insertion_point(module_scope)