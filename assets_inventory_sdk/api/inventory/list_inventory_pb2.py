# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list_inventory.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='list_inventory.proto',
  package='inventory',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14list_inventory.proto\x12\tinventory\"I\n\x12ListHistoryRequest\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\x11\n\tstartTime\x18\x02 \x01(\t\x12\x0f\n\x07\x65ndTime\x18\x03 \x01(\t\"\x9d\x02\n\x13ListHistoryResponse\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12\x31\n\x04list\x18\x04 \x03(\x0b\x32#.inventory.ListHistoryResponse.List\x1a\xa2\x01\n\x04List\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\r\n\x05\x63time\x18\x02 \x01(\t\x12\r\n\x05total\x18\x03 \x01(\x05\x12\x0f\n\x07\x63hanged\x18\x04 \x01(\x05\x12\x0f\n\x07invalid\x18\x05 \x01(\x05\x12\x0e\n\x06normal\x18\x06 \x01(\x05\x12\x0b\n\x03xin\x18\x07 \x01(\x05\x12\x0b\n\x03out\x18\x08 \x01(\x05\x12\x0e\n\x06online\x18\t \x01(\x05\x12\x0f\n\x07offline\x18\n \x01(\x05\"|\n\x1aListHistoryResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12,\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1e.inventory.ListHistoryResponseb\x06proto3')
)




_LISTHISTORYREQUEST = _descriptor.Descriptor(
  name='ListHistoryRequest',
  full_name='inventory.ListHistoryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='creator', full_name='inventory.ListHistoryRequest.creator', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='inventory.ListHistoryRequest.startTime', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endTime', full_name='inventory.ListHistoryRequest.endTime', index=2,
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
  serialized_start=35,
  serialized_end=108,
)


_LISTHISTORYRESPONSE_LIST = _descriptor.Descriptor(
  name='List',
  full_name='inventory.ListHistoryResponse.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='creator', full_name='inventory.ListHistoryResponse.List.creator', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='inventory.ListHistoryResponse.List.ctime', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='inventory.ListHistoryResponse.List.total', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='changed', full_name='inventory.ListHistoryResponse.List.changed', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='invalid', full_name='inventory.ListHistoryResponse.List.invalid', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='normal', full_name='inventory.ListHistoryResponse.List.normal', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='xin', full_name='inventory.ListHistoryResponse.List.xin', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='out', full_name='inventory.ListHistoryResponse.List.out', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='online', full_name='inventory.ListHistoryResponse.List.online', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offline', full_name='inventory.ListHistoryResponse.List.offline', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=234,
  serialized_end=396,
)

_LISTHISTORYRESPONSE = _descriptor.Descriptor(
  name='ListHistoryResponse',
  full_name='inventory.ListHistoryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='inventory.ListHistoryResponse.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='inventory.ListHistoryResponse.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='inventory.ListHistoryResponse.total', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='inventory.ListHistoryResponse.list', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTHISTORYRESPONSE_LIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=111,
  serialized_end=396,
)


_LISTHISTORYRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListHistoryResponseWrapper',
  full_name='inventory.ListHistoryResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='inventory.ListHistoryResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='inventory.ListHistoryResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='inventory.ListHistoryResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='inventory.ListHistoryResponseWrapper.data', index=3,
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
  serialized_start=398,
  serialized_end=522,
)

_LISTHISTORYRESPONSE_LIST.containing_type = _LISTHISTORYRESPONSE
_LISTHISTORYRESPONSE.fields_by_name['list'].message_type = _LISTHISTORYRESPONSE_LIST
_LISTHISTORYRESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTHISTORYRESPONSE
DESCRIPTOR.message_types_by_name['ListHistoryRequest'] = _LISTHISTORYREQUEST
DESCRIPTOR.message_types_by_name['ListHistoryResponse'] = _LISTHISTORYRESPONSE
DESCRIPTOR.message_types_by_name['ListHistoryResponseWrapper'] = _LISTHISTORYRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListHistoryRequest = _reflection.GeneratedProtocolMessageType('ListHistoryRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTHISTORYREQUEST,
  '__module__' : 'list_inventory_pb2'
  # @@protoc_insertion_point(class_scope:inventory.ListHistoryRequest)
  })
_sym_db.RegisterMessage(ListHistoryRequest)

ListHistoryResponse = _reflection.GeneratedProtocolMessageType('ListHistoryResponse', (_message.Message,), {

  'List' : _reflection.GeneratedProtocolMessageType('List', (_message.Message,), {
    'DESCRIPTOR' : _LISTHISTORYRESPONSE_LIST,
    '__module__' : 'list_inventory_pb2'
    # @@protoc_insertion_point(class_scope:inventory.ListHistoryResponse.List)
    })
  ,
  'DESCRIPTOR' : _LISTHISTORYRESPONSE,
  '__module__' : 'list_inventory_pb2'
  # @@protoc_insertion_point(class_scope:inventory.ListHistoryResponse)
  })
_sym_db.RegisterMessage(ListHistoryResponse)
_sym_db.RegisterMessage(ListHistoryResponse.List)

ListHistoryResponseWrapper = _reflection.GeneratedProtocolMessageType('ListHistoryResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _LISTHISTORYRESPONSEWRAPPER,
  '__module__' : 'list_inventory_pb2'
  # @@protoc_insertion_point(class_scope:inventory.ListHistoryResponseWrapper)
  })
_sym_db.RegisterMessage(ListHistoryResponseWrapper)


# @@protoc_insertion_point(module_scope)
