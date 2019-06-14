# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: delete_version.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='delete_version.proto',
  package='version',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14\x64\x65lete_version.proto\x12\x07version\"<\n\x14\x44\x65leteVersionRequest\x12\x11\n\tpackageId\x18\x01 \x01(\t\x12\x11\n\tversionId\x18\x02 \x01(\t\",\n\x15\x44\x65leteVersionResponse\x12\x13\n\x0blastVersion\x18\x01 \x01(\x08\"~\n\x1c\x44\x65leteVersionResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12,\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1e.version.DeleteVersionResponseb\x06proto3')
)




_DELETEVERSIONREQUEST = _descriptor.Descriptor(
  name='DeleteVersionRequest',
  full_name='version.DeleteVersionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='packageId', full_name='version.DeleteVersionRequest.packageId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionId', full_name='version.DeleteVersionRequest.versionId', index=1,
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
  serialized_start=33,
  serialized_end=93,
)


_DELETEVERSIONRESPONSE = _descriptor.Descriptor(
  name='DeleteVersionResponse',
  full_name='version.DeleteVersionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lastVersion', full_name='version.DeleteVersionResponse.lastVersion', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=95,
  serialized_end=139,
)


_DELETEVERSIONRESPONSEWRAPPER = _descriptor.Descriptor(
  name='DeleteVersionResponseWrapper',
  full_name='version.DeleteVersionResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='version.DeleteVersionResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='version.DeleteVersionResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='version.DeleteVersionResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='version.DeleteVersionResponseWrapper.data', index=3,
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
  serialized_start=141,
  serialized_end=267,
)

_DELETEVERSIONRESPONSEWRAPPER.fields_by_name['data'].message_type = _DELETEVERSIONRESPONSE
DESCRIPTOR.message_types_by_name['DeleteVersionRequest'] = _DELETEVERSIONREQUEST
DESCRIPTOR.message_types_by_name['DeleteVersionResponse'] = _DELETEVERSIONRESPONSE
DESCRIPTOR.message_types_by_name['DeleteVersionResponseWrapper'] = _DELETEVERSIONRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeleteVersionRequest = _reflection.GeneratedProtocolMessageType('DeleteVersionRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETEVERSIONREQUEST,
  __module__ = 'delete_version_pb2'
  # @@protoc_insertion_point(class_scope:version.DeleteVersionRequest)
  ))
_sym_db.RegisterMessage(DeleteVersionRequest)

DeleteVersionResponse = _reflection.GeneratedProtocolMessageType('DeleteVersionResponse', (_message.Message,), dict(
  DESCRIPTOR = _DELETEVERSIONRESPONSE,
  __module__ = 'delete_version_pb2'
  # @@protoc_insertion_point(class_scope:version.DeleteVersionResponse)
  ))
_sym_db.RegisterMessage(DeleteVersionResponse)

DeleteVersionResponseWrapper = _reflection.GeneratedProtocolMessageType('DeleteVersionResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _DELETEVERSIONRESPONSEWRAPPER,
  __module__ = 'delete_version_pb2'
  # @@protoc_insertion_point(class_scope:version.DeleteVersionResponseWrapper)
  ))
_sym_db.RegisterMessage(DeleteVersionResponseWrapper)


# @@protoc_insertion_point(module_scope)
