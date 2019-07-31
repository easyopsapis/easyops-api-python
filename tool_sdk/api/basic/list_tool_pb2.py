# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list_tool.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from model.tool import tool_pb2 as model_dot_tool_dot_tool__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='list_tool.proto',
  package='basic',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0flist_tool.proto\x12\x05\x62\x61sic\x1a\x15model/tool/tool.proto\"\x95\x01\n\x0fListToolRequest\x12\x0e\n\x06\x64\x65tail\x18\x01 \x01(\t\x12\x0e\n\x06plugin\x18\x02 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x03 \x01(\t\x12\x13\n\x0bpermissions\x18\x04 \x01(\t\x12\x16\n\x0eonlyProduction\x18\x05 \x01(\t\x12\x15\n\rshowInvisible\x18\x06 \x01(\t\x12\x0c\n\x04tags\x18\x07 \x01(\t\"\\\n\x10ListToolResponse\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12\x18\n\x04list\x18\x04 \x03(\x0b\x32\n.tool.Tool\"r\n\x17ListToolResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12%\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x17.basic.ListToolResponseb\x06proto3')
  ,
  dependencies=[model_dot_tool_dot_tool__pb2.DESCRIPTOR,])




_LISTTOOLREQUEST = _descriptor.Descriptor(
  name='ListToolRequest',
  full_name='basic.ListToolRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='detail', full_name='basic.ListToolRequest.detail', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='plugin', full_name='basic.ListToolRequest.plugin', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='basic.ListToolRequest.category', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='permissions', full_name='basic.ListToolRequest.permissions', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='onlyProduction', full_name='basic.ListToolRequest.onlyProduction', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='showInvisible', full_name='basic.ListToolRequest.showInvisible', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='basic.ListToolRequest.tags', index=6,
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
  serialized_start=50,
  serialized_end=199,
)


_LISTTOOLRESPONSE = _descriptor.Descriptor(
  name='ListToolResponse',
  full_name='basic.ListToolResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='basic.ListToolResponse.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='basic.ListToolResponse.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='basic.ListToolResponse.total', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='basic.ListToolResponse.list', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=201,
  serialized_end=293,
)


_LISTTOOLRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListToolResponseWrapper',
  full_name='basic.ListToolResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='basic.ListToolResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='basic.ListToolResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='basic.ListToolResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='basic.ListToolResponseWrapper.data', index=3,
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
  serialized_start=295,
  serialized_end=409,
)

_LISTTOOLRESPONSE.fields_by_name['list'].message_type = model_dot_tool_dot_tool__pb2._TOOL
_LISTTOOLRESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTTOOLRESPONSE
DESCRIPTOR.message_types_by_name['ListToolRequest'] = _LISTTOOLREQUEST
DESCRIPTOR.message_types_by_name['ListToolResponse'] = _LISTTOOLRESPONSE
DESCRIPTOR.message_types_by_name['ListToolResponseWrapper'] = _LISTTOOLRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListToolRequest = _reflection.GeneratedProtocolMessageType('ListToolRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTTOOLREQUEST,
  __module__ = 'list_tool_pb2'
  # @@protoc_insertion_point(class_scope:basic.ListToolRequest)
  ))
_sym_db.RegisterMessage(ListToolRequest)

ListToolResponse = _reflection.GeneratedProtocolMessageType('ListToolResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTTOOLRESPONSE,
  __module__ = 'list_tool_pb2'
  # @@protoc_insertion_point(class_scope:basic.ListToolResponse)
  ))
_sym_db.RegisterMessage(ListToolResponse)

ListToolResponseWrapper = _reflection.GeneratedProtocolMessageType('ListToolResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _LISTTOOLRESPONSEWRAPPER,
  __module__ = 'list_tool_pb2'
  # @@protoc_insertion_point(class_scope:basic.ListToolResponseWrapper)
  ))
_sym_db.RegisterMessage(ListToolResponseWrapper)


# @@protoc_insertion_point(module_scope)
