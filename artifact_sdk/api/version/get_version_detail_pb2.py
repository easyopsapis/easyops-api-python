# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_version_detail.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from model.artifact import version_pb2 as model_dot_artifact_dot_version__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_version_detail.proto',
  package='version',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x18get_version_detail.proto\x12\x07version\x1a\x1cmodel/artifact/version.proto\x1a\x1cgoogle/protobuf/struct.proto\",\n\x17GetVersionDetailRequest\x12\x11\n\tversionId\x18\x01 \x01(\t\"t\n\x1fGetVersionDetailResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x1f\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x11.artifact.Versionb\x06proto3')
  ,
  dependencies=[model_dot_artifact_dot_version__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_GETVERSIONDETAILREQUEST = _descriptor.Descriptor(
  name='GetVersionDetailRequest',
  full_name='version.GetVersionDetailRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='versionId', full_name='version.GetVersionDetailRequest.versionId', index=0,
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
  serialized_start=97,
  serialized_end=141,
)


_GETVERSIONDETAILRESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetVersionDetailResponseWrapper',
  full_name='version.GetVersionDetailResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='version.GetVersionDetailResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='version.GetVersionDetailResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='version.GetVersionDetailResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='version.GetVersionDetailResponseWrapper.data', index=3,
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
  serialized_start=143,
  serialized_end=259,
)

_GETVERSIONDETAILRESPONSEWRAPPER.fields_by_name['data'].message_type = model_dot_artifact_dot_version__pb2._VERSION
DESCRIPTOR.message_types_by_name['GetVersionDetailRequest'] = _GETVERSIONDETAILREQUEST
DESCRIPTOR.message_types_by_name['GetVersionDetailResponseWrapper'] = _GETVERSIONDETAILRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetVersionDetailRequest = _reflection.GeneratedProtocolMessageType('GetVersionDetailRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETVERSIONDETAILREQUEST,
  __module__ = 'get_version_detail_pb2'
  # @@protoc_insertion_point(class_scope:version.GetVersionDetailRequest)
  ))
_sym_db.RegisterMessage(GetVersionDetailRequest)

GetVersionDetailResponseWrapper = _reflection.GeneratedProtocolMessageType('GetVersionDetailResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _GETVERSIONDETAILRESPONSEWRAPPER,
  __module__ = 'get_version_detail_pb2'
  # @@protoc_insertion_point(class_scope:version.GetVersionDetailResponseWrapper)
  ))
_sym_db.RegisterMessage(GetVersionDetailResponseWrapper)


# @@protoc_insertion_point(module_scope)
