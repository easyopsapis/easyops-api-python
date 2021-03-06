# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: package_upload.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='package_upload.proto',
  package='installed_micro_app',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14package_upload.proto\x12\x13installed_micro_app\"^\n\x14PackageUploadRequest\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x11\n\tobjectIds\x18\x03 \x03(\t\x12\r\n\x05\x61ppId\x18\x04 \x01(\t\"7\n\x15PackageUploadResponse\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\r\n\x05\x61ppId\x18\x02 \x01(\t\"\x8a\x01\n\x1cPackageUploadResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x38\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32*.installed_micro_app.PackageUploadResponseb\x06proto3')
)




_PACKAGEUPLOADREQUEST = _descriptor.Descriptor(
  name='PackageUploadRequest',
  full_name='installed_micro_app.PackageUploadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='installed_micro_app.PackageUploadRequest.version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='installed_micro_app.PackageUploadRequest.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectIds', full_name='installed_micro_app.PackageUploadRequest.objectIds', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='appId', full_name='installed_micro_app.PackageUploadRequest.appId', index=3,
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
  serialized_start=45,
  serialized_end=139,
)


_PACKAGEUPLOADRESPONSE = _descriptor.Descriptor(
  name='PackageUploadResponse',
  full_name='installed_micro_app.PackageUploadResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='installed_micro_app.PackageUploadResponse.version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='appId', full_name='installed_micro_app.PackageUploadResponse.appId', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_end=196,
)


_PACKAGEUPLOADRESPONSEWRAPPER = _descriptor.Descriptor(
  name='PackageUploadResponseWrapper',
  full_name='installed_micro_app.PackageUploadResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='installed_micro_app.PackageUploadResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='installed_micro_app.PackageUploadResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='installed_micro_app.PackageUploadResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='installed_micro_app.PackageUploadResponseWrapper.data', index=3,
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
  serialized_start=199,
  serialized_end=337,
)

_PACKAGEUPLOADRESPONSEWRAPPER.fields_by_name['data'].message_type = _PACKAGEUPLOADRESPONSE
DESCRIPTOR.message_types_by_name['PackageUploadRequest'] = _PACKAGEUPLOADREQUEST
DESCRIPTOR.message_types_by_name['PackageUploadResponse'] = _PACKAGEUPLOADRESPONSE
DESCRIPTOR.message_types_by_name['PackageUploadResponseWrapper'] = _PACKAGEUPLOADRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PackageUploadRequest = _reflection.GeneratedProtocolMessageType('PackageUploadRequest', (_message.Message,), {
  'DESCRIPTOR' : _PACKAGEUPLOADREQUEST,
  '__module__' : 'package_upload_pb2'
  # @@protoc_insertion_point(class_scope:installed_micro_app.PackageUploadRequest)
  })
_sym_db.RegisterMessage(PackageUploadRequest)

PackageUploadResponse = _reflection.GeneratedProtocolMessageType('PackageUploadResponse', (_message.Message,), {
  'DESCRIPTOR' : _PACKAGEUPLOADRESPONSE,
  '__module__' : 'package_upload_pb2'
  # @@protoc_insertion_point(class_scope:installed_micro_app.PackageUploadResponse)
  })
_sym_db.RegisterMessage(PackageUploadResponse)

PackageUploadResponseWrapper = _reflection.GeneratedProtocolMessageType('PackageUploadResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _PACKAGEUPLOADRESPONSEWRAPPER,
  '__module__' : 'package_upload_pb2'
  # @@protoc_insertion_point(class_scope:installed_micro_app.PackageUploadResponseWrapper)
  })
_sym_db.RegisterMessage(PackageUploadResponseWrapper)


# @@protoc_insertion_point(module_scope)
