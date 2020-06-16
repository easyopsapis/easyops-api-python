# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list_user_setting.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='list_user_setting.proto',
  package='idcrack',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x17list_user_setting.proto\x12\x07idcrack\"G\n\x16ListUserSettingRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x10\n\x08pageSize\x18\x02 \x01(\x05\x12\r\n\x05types\x18\x03 \x01(\t\"\xe6\x02\n\x17ListUserSettingResponse\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12\x33\n\x04list\x18\x04 \x03(\x0b\x32%.idcrack.ListUserSettingResponse.List\x1a\xe5\x01\n\x04List\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x19\n\x11name_display_list\x18\x04 \x03(\t\x12T\n\x13\x64\x65tail_display_list\x18\x05 \x03(\x0b\x32\x37.idcrack.ListUserSettingResponse.List.DetailDisplayList\x1a=\n\x11\x44\x65tailDisplayList\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x0c\n\x04show\x18\x03 \x01(\x08\"\x82\x01\n\x1eListUserSettingResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12.\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32 .idcrack.ListUserSettingResponseb\x06proto3')
)




_LISTUSERSETTINGREQUEST = _descriptor.Descriptor(
  name='ListUserSettingRequest',
  full_name='idcrack.ListUserSettingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='idcrack.ListUserSettingRequest.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='idcrack.ListUserSettingRequest.pageSize', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='types', full_name='idcrack.ListUserSettingRequest.types', index=2,
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
  serialized_start=36,
  serialized_end=107,
)


_LISTUSERSETTINGRESPONSE_LIST_DETAILDISPLAYLIST = _descriptor.Descriptor(
  name='DetailDisplayList',
  full_name='idcrack.ListUserSettingResponse.List.DetailDisplayList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='idcrack.ListUserSettingResponse.List.DetailDisplayList.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='idcrack.ListUserSettingResponse.List.DetailDisplayList.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='show', full_name='idcrack.ListUserSettingResponse.List.DetailDisplayList.show', index=2,
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
  serialized_start=407,
  serialized_end=468,
)

_LISTUSERSETTINGRESPONSE_LIST = _descriptor.Descriptor(
  name='List',
  full_name='idcrack.ListUserSettingResponse.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='idcrack.ListUserSettingResponse.List.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='idcrack.ListUserSettingResponse.List.user_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='idcrack.ListUserSettingResponse.List.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name_display_list', full_name='idcrack.ListUserSettingResponse.List.name_display_list', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='detail_display_list', full_name='idcrack.ListUserSettingResponse.List.detail_display_list', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTUSERSETTINGRESPONSE_LIST_DETAILDISPLAYLIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=239,
  serialized_end=468,
)

_LISTUSERSETTINGRESPONSE = _descriptor.Descriptor(
  name='ListUserSettingResponse',
  full_name='idcrack.ListUserSettingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='idcrack.ListUserSettingResponse.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='idcrack.ListUserSettingResponse.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='idcrack.ListUserSettingResponse.total', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='idcrack.ListUserSettingResponse.list', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTUSERSETTINGRESPONSE_LIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=110,
  serialized_end=468,
)


_LISTUSERSETTINGRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListUserSettingResponseWrapper',
  full_name='idcrack.ListUserSettingResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='idcrack.ListUserSettingResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='idcrack.ListUserSettingResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='idcrack.ListUserSettingResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='idcrack.ListUserSettingResponseWrapper.data', index=3,
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
  serialized_start=471,
  serialized_end=601,
)

_LISTUSERSETTINGRESPONSE_LIST_DETAILDISPLAYLIST.containing_type = _LISTUSERSETTINGRESPONSE_LIST
_LISTUSERSETTINGRESPONSE_LIST.fields_by_name['detail_display_list'].message_type = _LISTUSERSETTINGRESPONSE_LIST_DETAILDISPLAYLIST
_LISTUSERSETTINGRESPONSE_LIST.containing_type = _LISTUSERSETTINGRESPONSE
_LISTUSERSETTINGRESPONSE.fields_by_name['list'].message_type = _LISTUSERSETTINGRESPONSE_LIST
_LISTUSERSETTINGRESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTUSERSETTINGRESPONSE
DESCRIPTOR.message_types_by_name['ListUserSettingRequest'] = _LISTUSERSETTINGREQUEST
DESCRIPTOR.message_types_by_name['ListUserSettingResponse'] = _LISTUSERSETTINGRESPONSE
DESCRIPTOR.message_types_by_name['ListUserSettingResponseWrapper'] = _LISTUSERSETTINGRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListUserSettingRequest = _reflection.GeneratedProtocolMessageType('ListUserSettingRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTUSERSETTINGREQUEST,
  '__module__' : 'list_user_setting_pb2'
  # @@protoc_insertion_point(class_scope:idcrack.ListUserSettingRequest)
  })
_sym_db.RegisterMessage(ListUserSettingRequest)

ListUserSettingResponse = _reflection.GeneratedProtocolMessageType('ListUserSettingResponse', (_message.Message,), {

  'List' : _reflection.GeneratedProtocolMessageType('List', (_message.Message,), {

    'DetailDisplayList' : _reflection.GeneratedProtocolMessageType('DetailDisplayList', (_message.Message,), {
      'DESCRIPTOR' : _LISTUSERSETTINGRESPONSE_LIST_DETAILDISPLAYLIST,
      '__module__' : 'list_user_setting_pb2'
      # @@protoc_insertion_point(class_scope:idcrack.ListUserSettingResponse.List.DetailDisplayList)
      })
    ,
    'DESCRIPTOR' : _LISTUSERSETTINGRESPONSE_LIST,
    '__module__' : 'list_user_setting_pb2'
    # @@protoc_insertion_point(class_scope:idcrack.ListUserSettingResponse.List)
    })
  ,
  'DESCRIPTOR' : _LISTUSERSETTINGRESPONSE,
  '__module__' : 'list_user_setting_pb2'
  # @@protoc_insertion_point(class_scope:idcrack.ListUserSettingResponse)
  })
_sym_db.RegisterMessage(ListUserSettingResponse)
_sym_db.RegisterMessage(ListUserSettingResponse.List)
_sym_db.RegisterMessage(ListUserSettingResponse.List.DetailDisplayList)

ListUserSettingResponseWrapper = _reflection.GeneratedProtocolMessageType('ListUserSettingResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _LISTUSERSETTINGRESPONSEWRAPPER,
  '__module__' : 'list_user_setting_pb2'
  # @@protoc_insertion_point(class_scope:idcrack.ListUserSettingResponseWrapper)
  })
_sym_db.RegisterMessage(ListUserSettingResponseWrapper)


# @@protoc_insertion_point(module_scope)