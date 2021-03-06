# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_file_info.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_file_info.proto',
  package='workspace',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13get_file_info.proto\x12\tworkspace\"T\n\x12GetFileInfoRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x11\n\tencodeing\x18\x02 \x01(\t\x12\n\n\x02op\x18\x03 \x01(\t\x12\x11\n\tpackageId\x18\x04 \x01(\t\"y\n\x13GetFileInfoResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0c\n\x04size\x18\x03 \x01(\x05\x12\x0c\n\x04perm\x18\x04 \x01(\t\x12\x0c\n\x04link\x18\x05 \x01(\t\x12\r\n\x05mtime\x18\x06 \x01(\t\x12\r\n\x05\x63time\x18\x07 \x01(\t\"|\n\x1aGetFileInfoResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12,\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1e.workspace.GetFileInfoResponseb\x06proto3')
)




_GETFILEINFOREQUEST = _descriptor.Descriptor(
  name='GetFileInfoRequest',
  full_name='workspace.GetFileInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='workspace.GetFileInfoRequest.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encodeing', full_name='workspace.GetFileInfoRequest.encodeing', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='op', full_name='workspace.GetFileInfoRequest.op', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageId', full_name='workspace.GetFileInfoRequest.packageId', index=3,
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
  serialized_start=34,
  serialized_end=118,
)


_GETFILEINFORESPONSE = _descriptor.Descriptor(
  name='GetFileInfoResponse',
  full_name='workspace.GetFileInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='workspace.GetFileInfoResponse.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='workspace.GetFileInfoResponse.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='workspace.GetFileInfoResponse.size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='perm', full_name='workspace.GetFileInfoResponse.perm', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='link', full_name='workspace.GetFileInfoResponse.link', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='workspace.GetFileInfoResponse.mtime', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='workspace.GetFileInfoResponse.ctime', index=6,
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
  serialized_start=120,
  serialized_end=241,
)


_GETFILEINFORESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetFileInfoResponseWrapper',
  full_name='workspace.GetFileInfoResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='workspace.GetFileInfoResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='workspace.GetFileInfoResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='workspace.GetFileInfoResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='workspace.GetFileInfoResponseWrapper.data', index=3,
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
  serialized_start=243,
  serialized_end=367,
)

_GETFILEINFORESPONSEWRAPPER.fields_by_name['data'].message_type = _GETFILEINFORESPONSE
DESCRIPTOR.message_types_by_name['GetFileInfoRequest'] = _GETFILEINFOREQUEST
DESCRIPTOR.message_types_by_name['GetFileInfoResponse'] = _GETFILEINFORESPONSE
DESCRIPTOR.message_types_by_name['GetFileInfoResponseWrapper'] = _GETFILEINFORESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetFileInfoRequest = _reflection.GeneratedProtocolMessageType('GetFileInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETFILEINFOREQUEST,
  '__module__' : 'get_file_info_pb2'
  # @@protoc_insertion_point(class_scope:workspace.GetFileInfoRequest)
  })
_sym_db.RegisterMessage(GetFileInfoRequest)

GetFileInfoResponse = _reflection.GeneratedProtocolMessageType('GetFileInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETFILEINFORESPONSE,
  '__module__' : 'get_file_info_pb2'
  # @@protoc_insertion_point(class_scope:workspace.GetFileInfoResponse)
  })
_sym_db.RegisterMessage(GetFileInfoResponse)

GetFileInfoResponseWrapper = _reflection.GeneratedProtocolMessageType('GetFileInfoResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _GETFILEINFORESPONSEWRAPPER,
  '__module__' : 'get_file_info_pb2'
  # @@protoc_insertion_point(class_scope:workspace.GetFileInfoResponseWrapper)
  })
_sym_db.RegisterMessage(GetFileInfoResponseWrapper)


# @@protoc_insertion_point(module_scope)
