# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_folder_name.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_folder_name.proto',
  package='sqlpkgs',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x15get_folder_name.proto\x12\x07sqlpkgs\"B\n\x15GetFolderNameResponse\x12\x14\n\x0c\x62\x61\x63kUpFolder\x18\x01 \x01(\t\x12\x13\n\x0b\x63heckFolder\x18\x02 \x01(\t\"~\n\x1cGetFolderNameResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12,\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1e.sqlpkgs.GetFolderNameResponseb\x06proto3')
)




_GETFOLDERNAMERESPONSE = _descriptor.Descriptor(
  name='GetFolderNameResponse',
  full_name='sqlpkgs.GetFolderNameResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='backUpFolder', full_name='sqlpkgs.GetFolderNameResponse.backUpFolder', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checkFolder', full_name='sqlpkgs.GetFolderNameResponse.checkFolder', index=1,
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
  serialized_start=34,
  serialized_end=100,
)


_GETFOLDERNAMERESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetFolderNameResponseWrapper',
  full_name='sqlpkgs.GetFolderNameResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='sqlpkgs.GetFolderNameResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='sqlpkgs.GetFolderNameResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='sqlpkgs.GetFolderNameResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='sqlpkgs.GetFolderNameResponseWrapper.data', index=3,
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
  serialized_start=102,
  serialized_end=228,
)

_GETFOLDERNAMERESPONSEWRAPPER.fields_by_name['data'].message_type = _GETFOLDERNAMERESPONSE
DESCRIPTOR.message_types_by_name['GetFolderNameResponse'] = _GETFOLDERNAMERESPONSE
DESCRIPTOR.message_types_by_name['GetFolderNameResponseWrapper'] = _GETFOLDERNAMERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetFolderNameResponse = _reflection.GeneratedProtocolMessageType('GetFolderNameResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETFOLDERNAMERESPONSE,
  __module__ = 'get_folder_name_pb2'
  # @@protoc_insertion_point(class_scope:sqlpkgs.GetFolderNameResponse)
  ))
_sym_db.RegisterMessage(GetFolderNameResponse)

GetFolderNameResponseWrapper = _reflection.GeneratedProtocolMessageType('GetFolderNameResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _GETFOLDERNAMERESPONSEWRAPPER,
  __module__ = 'get_folder_name_pb2'
  # @@protoc_insertion_point(class_scope:sqlpkgs.GetFolderNameResponseWrapper)
  ))
_sym_db.RegisterMessage(GetFolderNameResponseWrapper)


# @@protoc_insertion_point(module_scope)
