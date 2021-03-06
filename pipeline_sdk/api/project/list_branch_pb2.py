# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list_branch.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='list_branch.proto',
  package='project',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11list_branch.proto\x12\x07project\"X\n\x11ListBranchRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0c\n\x04page\x18\x02 \x01(\x05\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x0e\n\x06search\x18\x04 \x01(\t\"\xae\x01\n\x12ListBranchResponse\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12.\n\x04list\x18\x04 \x03(\x0b\x32 .project.ListBranchResponse.List\x1a\x38\n\x04List\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tprotected\x18\x02 \x01(\x08\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x03 \x01(\x08\"x\n\x19ListBranchResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12)\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1b.project.ListBranchResponseb\x06proto3')
)




_LISTBRANCHREQUEST = _descriptor.Descriptor(
  name='ListBranchRequest',
  full_name='project.ListBranchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project_id', full_name='project.ListBranchRequest.project_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page', full_name='project.ListBranchRequest.page', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='project.ListBranchRequest.page_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='search', full_name='project.ListBranchRequest.search', index=3,
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
  serialized_start=30,
  serialized_end=118,
)


_LISTBRANCHRESPONSE_LIST = _descriptor.Descriptor(
  name='List',
  full_name='project.ListBranchResponse.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='project.ListBranchResponse.List.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='protected', full_name='project.ListBranchResponse.List.protected', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default', full_name='project.ListBranchResponse.List.default', index=2,
      number=3, type=8, cpp_type=7, label=1,
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
  serialized_start=239,
  serialized_end=295,
)

_LISTBRANCHRESPONSE = _descriptor.Descriptor(
  name='ListBranchResponse',
  full_name='project.ListBranchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='project.ListBranchResponse.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='project.ListBranchResponse.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='project.ListBranchResponse.total', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='project.ListBranchResponse.list', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTBRANCHRESPONSE_LIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=295,
)


_LISTBRANCHRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListBranchResponseWrapper',
  full_name='project.ListBranchResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='project.ListBranchResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='project.ListBranchResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='project.ListBranchResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='project.ListBranchResponseWrapper.data', index=3,
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
  serialized_start=297,
  serialized_end=417,
)

_LISTBRANCHRESPONSE_LIST.containing_type = _LISTBRANCHRESPONSE
_LISTBRANCHRESPONSE.fields_by_name['list'].message_type = _LISTBRANCHRESPONSE_LIST
_LISTBRANCHRESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTBRANCHRESPONSE
DESCRIPTOR.message_types_by_name['ListBranchRequest'] = _LISTBRANCHREQUEST
DESCRIPTOR.message_types_by_name['ListBranchResponse'] = _LISTBRANCHRESPONSE
DESCRIPTOR.message_types_by_name['ListBranchResponseWrapper'] = _LISTBRANCHRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListBranchRequest = _reflection.GeneratedProtocolMessageType('ListBranchRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTBRANCHREQUEST,
  '__module__' : 'list_branch_pb2'
  # @@protoc_insertion_point(class_scope:project.ListBranchRequest)
  })
_sym_db.RegisterMessage(ListBranchRequest)

ListBranchResponse = _reflection.GeneratedProtocolMessageType('ListBranchResponse', (_message.Message,), {

  'List' : _reflection.GeneratedProtocolMessageType('List', (_message.Message,), {
    'DESCRIPTOR' : _LISTBRANCHRESPONSE_LIST,
    '__module__' : 'list_branch_pb2'
    # @@protoc_insertion_point(class_scope:project.ListBranchResponse.List)
    })
  ,
  'DESCRIPTOR' : _LISTBRANCHRESPONSE,
  '__module__' : 'list_branch_pb2'
  # @@protoc_insertion_point(class_scope:project.ListBranchResponse)
  })
_sym_db.RegisterMessage(ListBranchResponse)
_sym_db.RegisterMessage(ListBranchResponse.List)

ListBranchResponseWrapper = _reflection.GeneratedProtocolMessageType('ListBranchResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _LISTBRANCHRESPONSEWRAPPER,
  '__module__' : 'list_branch_pb2'
  # @@protoc_insertion_point(class_scope:project.ListBranchResponseWrapper)
  })
_sym_db.RegisterMessage(ListBranchResponseWrapper)


# @@protoc_insertion_point(module_scope)
