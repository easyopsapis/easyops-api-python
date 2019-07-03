# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list_menus.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='list_menus.proto',
  package='menu',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10list_menus.proto\x12\x04menu\"d\n\x10ListMenusRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x10\n\x08\x63\x61tegory\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0f\n\x07keyword\x18\x05 \x01(\t\"\xc2\x01\n\x11ListMenusResponse\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12*\n\x04list\x18\x04 \x03(\x0b\x32\x1c.menu.ListMenusResponse.List\x1aQ\n\x04List\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x03 \x01(\t\x12\x0c\n\x04icon\x18\x04 \x01(\t\x12\x0f\n\x07\x63reator\x18\x05 \x01(\t\"s\n\x18ListMenusResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12%\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x17.menu.ListMenusResponseb\x06proto3')
)




_LISTMENUSREQUEST = _descriptor.Descriptor(
  name='ListMenusRequest',
  full_name='menu.ListMenusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='menu.ListMenusRequest.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='menu.ListMenusRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='menu.ListMenusRequest.category', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='menu.ListMenusRequest.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keyword', full_name='menu.ListMenusRequest.keyword', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=26,
  serialized_end=126,
)


_LISTMENUSRESPONSE_LIST = _descriptor.Descriptor(
  name='List',
  full_name='menu.ListMenusResponse.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='menu.ListMenusResponse.List.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='menu.ListMenusResponse.List.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='menu.ListMenusResponse.List.category', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon', full_name='menu.ListMenusResponse.List.icon', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='menu.ListMenusResponse.List.creator', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=242,
  serialized_end=323,
)

_LISTMENUSRESPONSE = _descriptor.Descriptor(
  name='ListMenusResponse',
  full_name='menu.ListMenusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='menu.ListMenusResponse.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='menu.ListMenusResponse.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='menu.ListMenusResponse.total', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='menu.ListMenusResponse.list', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTMENUSRESPONSE_LIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=323,
)


_LISTMENUSRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListMenusResponseWrapper',
  full_name='menu.ListMenusResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='menu.ListMenusResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='menu.ListMenusResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='menu.ListMenusResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='menu.ListMenusResponseWrapper.data', index=3,
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
  serialized_start=325,
  serialized_end=440,
)

_LISTMENUSRESPONSE_LIST.containing_type = _LISTMENUSRESPONSE
_LISTMENUSRESPONSE.fields_by_name['list'].message_type = _LISTMENUSRESPONSE_LIST
_LISTMENUSRESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTMENUSRESPONSE
DESCRIPTOR.message_types_by_name['ListMenusRequest'] = _LISTMENUSREQUEST
DESCRIPTOR.message_types_by_name['ListMenusResponse'] = _LISTMENUSRESPONSE
DESCRIPTOR.message_types_by_name['ListMenusResponseWrapper'] = _LISTMENUSRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListMenusRequest = _reflection.GeneratedProtocolMessageType('ListMenusRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTMENUSREQUEST,
  __module__ = 'list_menus_pb2'
  # @@protoc_insertion_point(class_scope:menu.ListMenusRequest)
  ))
_sym_db.RegisterMessage(ListMenusRequest)

ListMenusResponse = _reflection.GeneratedProtocolMessageType('ListMenusResponse', (_message.Message,), dict(

  List = _reflection.GeneratedProtocolMessageType('List', (_message.Message,), dict(
    DESCRIPTOR = _LISTMENUSRESPONSE_LIST,
    __module__ = 'list_menus_pb2'
    # @@protoc_insertion_point(class_scope:menu.ListMenusResponse.List)
    ))
  ,
  DESCRIPTOR = _LISTMENUSRESPONSE,
  __module__ = 'list_menus_pb2'
  # @@protoc_insertion_point(class_scope:menu.ListMenusResponse)
  ))
_sym_db.RegisterMessage(ListMenusResponse)
_sym_db.RegisterMessage(ListMenusResponse.List)

ListMenusResponseWrapper = _reflection.GeneratedProtocolMessageType('ListMenusResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _LISTMENUSRESPONSEWRAPPER,
  __module__ = 'list_menus_pb2'
  # @@protoc_insertion_point(class_scope:menu.ListMenusResponseWrapper)
  ))
_sym_db.RegisterMessage(ListMenusResponseWrapper)


# @@protoc_insertion_point(module_scope)
