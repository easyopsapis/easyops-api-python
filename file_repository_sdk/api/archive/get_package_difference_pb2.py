# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_package_difference.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from file_repository_sdk.model.file_repository import diff_pb2 as file__repository__sdk_dot_model_dot_file__repository_dot_diff__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_package_difference.proto',
  package='archive',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1cget_package_difference.proto\x12\x07\x61rchive\x1a\x34\x66ile_repository_sdk/model/file_repository/diff.proto\"\x9c\x01\n\x1bGetPackageDifferenceRequest\x12\x14\n\x0cpackage_from\x18\x01 \x01(\t\x12\x12\n\npackage_to\x18\x02 \x01(\t\x12\x10\n\x08ver_from\x18\x03 \x01(\t\x12\x0e\n\x06ver_to\x18\x04 \x01(\t\x12\x11\n\tdiff_file\x18\x05 \x01(\t\x12\x0c\n\x04path\x18\x06 \x01(\t\x12\x10\n\x08\x65nconing\x18\x07 \x01(\t\"|\n#GetPackageDifferenceResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12#\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x15.file_repository.Diffb\x06proto3')
  ,
  dependencies=[file__repository__sdk_dot_model_dot_file__repository_dot_diff__pb2.DESCRIPTOR,])




_GETPACKAGEDIFFERENCEREQUEST = _descriptor.Descriptor(
  name='GetPackageDifferenceRequest',
  full_name='archive.GetPackageDifferenceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='package_from', full_name='archive.GetPackageDifferenceRequest.package_from', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='package_to', full_name='archive.GetPackageDifferenceRequest.package_to', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ver_from', full_name='archive.GetPackageDifferenceRequest.ver_from', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ver_to', full_name='archive.GetPackageDifferenceRequest.ver_to', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='diff_file', full_name='archive.GetPackageDifferenceRequest.diff_file', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='archive.GetPackageDifferenceRequest.path', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enconing', full_name='archive.GetPackageDifferenceRequest.enconing', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=96,
  serialized_end=252,
)


_GETPACKAGEDIFFERENCERESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetPackageDifferenceResponseWrapper',
  full_name='archive.GetPackageDifferenceResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='archive.GetPackageDifferenceResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='archive.GetPackageDifferenceResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='archive.GetPackageDifferenceResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='archive.GetPackageDifferenceResponseWrapper.data', index=3,
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
  serialized_start=254,
  serialized_end=378,
)

_GETPACKAGEDIFFERENCERESPONSEWRAPPER.fields_by_name['data'].message_type = file__repository__sdk_dot_model_dot_file__repository_dot_diff__pb2._DIFF
DESCRIPTOR.message_types_by_name['GetPackageDifferenceRequest'] = _GETPACKAGEDIFFERENCEREQUEST
DESCRIPTOR.message_types_by_name['GetPackageDifferenceResponseWrapper'] = _GETPACKAGEDIFFERENCERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetPackageDifferenceRequest = _reflection.GeneratedProtocolMessageType('GetPackageDifferenceRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPACKAGEDIFFERENCEREQUEST,
  '__module__' : 'get_package_difference_pb2'
  # @@protoc_insertion_point(class_scope:archive.GetPackageDifferenceRequest)
  })
_sym_db.RegisterMessage(GetPackageDifferenceRequest)

GetPackageDifferenceResponseWrapper = _reflection.GeneratedProtocolMessageType('GetPackageDifferenceResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _GETPACKAGEDIFFERENCERESPONSEWRAPPER,
  '__module__' : 'get_package_difference_pb2'
  # @@protoc_insertion_point(class_scope:archive.GetPackageDifferenceResponseWrapper)
  })
_sym_db.RegisterMessage(GetPackageDifferenceResponseWrapper)


# @@protoc_insertion_point(module_scope)
