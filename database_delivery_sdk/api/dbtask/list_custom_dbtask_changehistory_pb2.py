# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list_custom_dbtask_changehistory.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='list_custom_dbtask_changehistory.proto',
  package='dbtask',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n&list_custom_dbtask_changehistory.proto\x12\x06\x64\x62task\"[\n$ListCustomDBTaskChangeHistoryRequest\x12\x13\n\x0b\x64\x62ServiceId\x18\x01 \x01(\t\x12\x0c\n\x04page\x18\x02 \x01(\x05\x12\x10\n\x08pageSize\x18\x03 \x01(\x05\"\xb7\x02\n%ListCustomDBTaskChangeHistoryResponse\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12@\n\x04list\x18\x04 \x03(\x0b\x32\x32.dbtask.ListCustomDBTaskChangeHistoryResponse.List\x1a\x9b\x01\n\x04List\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x62ServiceId\x18\x02 \x01(\t\x12\x1a\n\x12\x64\x62InstanceNameList\x18\x03 \x03(\t\x12\x19\n\x11\x63hangesetNameList\x18\x04 \x03(\t\x12\r\n\x05state\x18\x05 \x01(\t\x12\x0e\n\x06status\x18\x06 \x01(\t\x12\r\n\x05\x63time\x18\x07 \x01(\x03\x12\r\n\x05mtime\x18\x08 \x01(\x03\"\x9d\x01\n,ListCustomDBTaskChangeHistoryResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12;\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32-.dbtask.ListCustomDBTaskChangeHistoryResponseb\x06proto3')
)




_LISTCUSTOMDBTASKCHANGEHISTORYREQUEST = _descriptor.Descriptor(
  name='ListCustomDBTaskChangeHistoryRequest',
  full_name='dbtask.ListCustomDBTaskChangeHistoryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dbServiceId', full_name='dbtask.ListCustomDBTaskChangeHistoryRequest.dbServiceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page', full_name='dbtask.ListCustomDBTaskChangeHistoryRequest.page', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='dbtask.ListCustomDBTaskChangeHistoryRequest.pageSize', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=50,
  serialized_end=141,
)


_LISTCUSTOMDBTASKCHANGEHISTORYRESPONSE_LIST = _descriptor.Descriptor(
  name='List',
  full_name='dbtask.ListCustomDBTaskChangeHistoryResponse.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='dbtask.ListCustomDBTaskChangeHistoryResponse.List.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dbServiceId', full_name='dbtask.ListCustomDBTaskChangeHistoryResponse.List.dbServiceId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dbInstanceNameList', full_name='dbtask.ListCustomDBTaskChangeHistoryResponse.List.dbInstanceNameList', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='changesetNameList', full_name='dbtask.ListCustomDBTaskChangeHistoryResponse.List.changesetNameList', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='dbtask.ListCustomDBTaskChangeHistoryResponse.List.state', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='dbtask.ListCustomDBTaskChangeHistoryResponse.List.status', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='dbtask.ListCustomDBTaskChangeHistoryResponse.List.ctime', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='dbtask.ListCustomDBTaskChangeHistoryResponse.List.mtime', index=7,
      number=8, type=3, cpp_type=2, label=1,
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
  serialized_start=300,
  serialized_end=455,
)

_LISTCUSTOMDBTASKCHANGEHISTORYRESPONSE = _descriptor.Descriptor(
  name='ListCustomDBTaskChangeHistoryResponse',
  full_name='dbtask.ListCustomDBTaskChangeHistoryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='dbtask.ListCustomDBTaskChangeHistoryResponse.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='dbtask.ListCustomDBTaskChangeHistoryResponse.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='dbtask.ListCustomDBTaskChangeHistoryResponse.total', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='dbtask.ListCustomDBTaskChangeHistoryResponse.list', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTCUSTOMDBTASKCHANGEHISTORYRESPONSE_LIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=144,
  serialized_end=455,
)


_LISTCUSTOMDBTASKCHANGEHISTORYRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListCustomDBTaskChangeHistoryResponseWrapper',
  full_name='dbtask.ListCustomDBTaskChangeHistoryResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='dbtask.ListCustomDBTaskChangeHistoryResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='dbtask.ListCustomDBTaskChangeHistoryResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dbtask.ListCustomDBTaskChangeHistoryResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='dbtask.ListCustomDBTaskChangeHistoryResponseWrapper.data', index=3,
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
  serialized_start=458,
  serialized_end=615,
)

_LISTCUSTOMDBTASKCHANGEHISTORYRESPONSE_LIST.containing_type = _LISTCUSTOMDBTASKCHANGEHISTORYRESPONSE
_LISTCUSTOMDBTASKCHANGEHISTORYRESPONSE.fields_by_name['list'].message_type = _LISTCUSTOMDBTASKCHANGEHISTORYRESPONSE_LIST
_LISTCUSTOMDBTASKCHANGEHISTORYRESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTCUSTOMDBTASKCHANGEHISTORYRESPONSE
DESCRIPTOR.message_types_by_name['ListCustomDBTaskChangeHistoryRequest'] = _LISTCUSTOMDBTASKCHANGEHISTORYREQUEST
DESCRIPTOR.message_types_by_name['ListCustomDBTaskChangeHistoryResponse'] = _LISTCUSTOMDBTASKCHANGEHISTORYRESPONSE
DESCRIPTOR.message_types_by_name['ListCustomDBTaskChangeHistoryResponseWrapper'] = _LISTCUSTOMDBTASKCHANGEHISTORYRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListCustomDBTaskChangeHistoryRequest = _reflection.GeneratedProtocolMessageType('ListCustomDBTaskChangeHistoryRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTCUSTOMDBTASKCHANGEHISTORYREQUEST,
  __module__ = 'list_custom_dbtask_changehistory_pb2'
  # @@protoc_insertion_point(class_scope:dbtask.ListCustomDBTaskChangeHistoryRequest)
  ))
_sym_db.RegisterMessage(ListCustomDBTaskChangeHistoryRequest)

ListCustomDBTaskChangeHistoryResponse = _reflection.GeneratedProtocolMessageType('ListCustomDBTaskChangeHistoryResponse', (_message.Message,), dict(

  List = _reflection.GeneratedProtocolMessageType('List', (_message.Message,), dict(
    DESCRIPTOR = _LISTCUSTOMDBTASKCHANGEHISTORYRESPONSE_LIST,
    __module__ = 'list_custom_dbtask_changehistory_pb2'
    # @@protoc_insertion_point(class_scope:dbtask.ListCustomDBTaskChangeHistoryResponse.List)
    ))
  ,
  DESCRIPTOR = _LISTCUSTOMDBTASKCHANGEHISTORYRESPONSE,
  __module__ = 'list_custom_dbtask_changehistory_pb2'
  # @@protoc_insertion_point(class_scope:dbtask.ListCustomDBTaskChangeHistoryResponse)
  ))
_sym_db.RegisterMessage(ListCustomDBTaskChangeHistoryResponse)
_sym_db.RegisterMessage(ListCustomDBTaskChangeHistoryResponse.List)

ListCustomDBTaskChangeHistoryResponseWrapper = _reflection.GeneratedProtocolMessageType('ListCustomDBTaskChangeHistoryResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _LISTCUSTOMDBTASKCHANGEHISTORYRESPONSEWRAPPER,
  __module__ = 'list_custom_dbtask_changehistory_pb2'
  # @@protoc_insertion_point(class_scope:dbtask.ListCustomDBTaskChangeHistoryResponseWrapper)
  ))
_sym_db.RegisterMessage(ListCustomDBTaskChangeHistoryResponseWrapper)


# @@protoc_insertion_point(module_scope)