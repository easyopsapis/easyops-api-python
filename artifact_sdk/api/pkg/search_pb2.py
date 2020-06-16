# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: search.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='search.proto',
  package='pkg',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0csearch.proto\x12\x03pkg\"\xa3\x01\n\rSearchRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x10\n\x08pageSize\x18\x02 \x01(\x05\x12\r\n\x05order\x18\x03 \x01(\t\x12\r\n\x05\x65xact\x18\x04 \x01(\t\x12\x19\n\x11XXX_RestFieldMask\x18\x05 \x03(\t\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x0c\n\x04type\x18\x07 \x01(\x05\x12\x0b\n\x03\x63Id\x18\x08 \x01(\x05\x12\x10\n\x08\x63\x61tegory\x18\t \x01(\t\"\xcf\x04\n\x0eSearchResponse\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12&\n\x04list\x18\x04 \x03(\x0b\x32\x18.pkg.SearchResponse.List\x1a\xe4\x03\n\x04List\x12\x11\n\tpackageId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\x05\x12\x0b\n\x03\x63Id\x18\x04 \x01(\x05\x12\x0e\n\x06source\x18\x05 \x01(\t\x12\x0e\n\x06repoId\x18\x06 \x01(\t\x12\x10\n\x08repoPath\x18\x07 \x01(\t\x12\x0c\n\x04memo\x18\x08 \x01(\t\x12\x0f\n\x07\x63reator\x18\t \x01(\t\x12\x0b\n\x03org\x18\n \x01(\x05\x12\x10\n\x08\x63\x61tegory\x18\x0b \x01(\t\x12\x0c\n\x04icon\x18\x0c \x01(\t\x12\r\n\x05style\x18\r \x01(\t\x12\r\n\x05\x63time\x18\x0e \x01(\t\x12\r\n\x05mtime\x18\x0f \x01(\t\x12\x11\n\tauthUsers\x18\x10 \x01(\t\x12\x13\n\x0binstallPath\x18\x11 \x01(\t\x12\x10\n\x08platform\x18\x12 \x01(\t\x12\x41\n\x0flastVersionInfo\x18\x13 \x01(\x0b\x32(.pkg.SearchResponse.List.LastVersionInfo\x12\x15\n\rinstanceCount\x18\x14 \x01(\x05\x1a\x61\n\x0fLastVersionInfo\x12\r\n\x05\x63time\x18\x01 \x01(\t\x12\x10\n\x08\x65nv_type\x18\x02 \x01(\x05\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0c\n\x04memo\x18\x04 \x01(\t\x12\x11\n\tversionId\x18\x05 \x01(\t\"l\n\x15SearchResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12!\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x13.pkg.SearchResponseb\x06proto3')
)




_SEARCHREQUEST = _descriptor.Descriptor(
  name='SearchRequest',
  full_name='pkg.SearchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='pkg.SearchRequest.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='pkg.SearchRequest.pageSize', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order', full_name='pkg.SearchRequest.order', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exact', full_name='pkg.SearchRequest.exact', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='XXX_RestFieldMask', full_name='pkg.SearchRequest.XXX_RestFieldMask', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='pkg.SearchRequest.name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='pkg.SearchRequest.type', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cId', full_name='pkg.SearchRequest.cId', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='pkg.SearchRequest.category', index=8,
      number=9, type=9, cpp_type=9, label=1,
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
  serialized_start=22,
  serialized_end=185,
)


_SEARCHRESPONSE_LIST_LASTVERSIONINFO = _descriptor.Descriptor(
  name='LastVersionInfo',
  full_name='pkg.SearchResponse.List.LastVersionInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ctime', full_name='pkg.SearchResponse.List.LastVersionInfo.ctime', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='env_type', full_name='pkg.SearchResponse.List.LastVersionInfo.env_type', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='pkg.SearchResponse.List.LastVersionInfo.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='pkg.SearchResponse.List.LastVersionInfo.memo', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionId', full_name='pkg.SearchResponse.List.LastVersionInfo.versionId', index=4,
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
  serialized_start=682,
  serialized_end=779,
)

_SEARCHRESPONSE_LIST = _descriptor.Descriptor(
  name='List',
  full_name='pkg.SearchResponse.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='packageId', full_name='pkg.SearchResponse.List.packageId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='pkg.SearchResponse.List.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='pkg.SearchResponse.List.type', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cId', full_name='pkg.SearchResponse.List.cId', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='pkg.SearchResponse.List.source', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repoId', full_name='pkg.SearchResponse.List.repoId', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repoPath', full_name='pkg.SearchResponse.List.repoPath', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='pkg.SearchResponse.List.memo', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='pkg.SearchResponse.List.creator', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org', full_name='pkg.SearchResponse.List.org', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='pkg.SearchResponse.List.category', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon', full_name='pkg.SearchResponse.List.icon', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='style', full_name='pkg.SearchResponse.List.style', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='pkg.SearchResponse.List.ctime', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='pkg.SearchResponse.List.mtime', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='authUsers', full_name='pkg.SearchResponse.List.authUsers', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='installPath', full_name='pkg.SearchResponse.List.installPath', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='platform', full_name='pkg.SearchResponse.List.platform', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastVersionInfo', full_name='pkg.SearchResponse.List.lastVersionInfo', index=18,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceCount', full_name='pkg.SearchResponse.List.instanceCount', index=19,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SEARCHRESPONSE_LIST_LASTVERSIONINFO, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=295,
  serialized_end=779,
)

_SEARCHRESPONSE = _descriptor.Descriptor(
  name='SearchResponse',
  full_name='pkg.SearchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='pkg.SearchResponse.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='pkg.SearchResponse.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='pkg.SearchResponse.total', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='pkg.SearchResponse.list', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SEARCHRESPONSE_LIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=188,
  serialized_end=779,
)


_SEARCHRESPONSEWRAPPER = _descriptor.Descriptor(
  name='SearchResponseWrapper',
  full_name='pkg.SearchResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='pkg.SearchResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='pkg.SearchResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='pkg.SearchResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='pkg.SearchResponseWrapper.data', index=3,
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
  serialized_start=781,
  serialized_end=889,
)

_SEARCHRESPONSE_LIST_LASTVERSIONINFO.containing_type = _SEARCHRESPONSE_LIST
_SEARCHRESPONSE_LIST.fields_by_name['lastVersionInfo'].message_type = _SEARCHRESPONSE_LIST_LASTVERSIONINFO
_SEARCHRESPONSE_LIST.containing_type = _SEARCHRESPONSE
_SEARCHRESPONSE.fields_by_name['list'].message_type = _SEARCHRESPONSE_LIST
_SEARCHRESPONSEWRAPPER.fields_by_name['data'].message_type = _SEARCHRESPONSE
DESCRIPTOR.message_types_by_name['SearchRequest'] = _SEARCHREQUEST
DESCRIPTOR.message_types_by_name['SearchResponse'] = _SEARCHRESPONSE
DESCRIPTOR.message_types_by_name['SearchResponseWrapper'] = _SEARCHRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SearchRequest = _reflection.GeneratedProtocolMessageType('SearchRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHREQUEST,
  '__module__' : 'search_pb2'
  # @@protoc_insertion_point(class_scope:pkg.SearchRequest)
  })
_sym_db.RegisterMessage(SearchRequest)

SearchResponse = _reflection.GeneratedProtocolMessageType('SearchResponse', (_message.Message,), {

  'List' : _reflection.GeneratedProtocolMessageType('List', (_message.Message,), {

    'LastVersionInfo' : _reflection.GeneratedProtocolMessageType('LastVersionInfo', (_message.Message,), {
      'DESCRIPTOR' : _SEARCHRESPONSE_LIST_LASTVERSIONINFO,
      '__module__' : 'search_pb2'
      # @@protoc_insertion_point(class_scope:pkg.SearchResponse.List.LastVersionInfo)
      })
    ,
    'DESCRIPTOR' : _SEARCHRESPONSE_LIST,
    '__module__' : 'search_pb2'
    # @@protoc_insertion_point(class_scope:pkg.SearchResponse.List)
    })
  ,
  'DESCRIPTOR' : _SEARCHRESPONSE,
  '__module__' : 'search_pb2'
  # @@protoc_insertion_point(class_scope:pkg.SearchResponse)
  })
_sym_db.RegisterMessage(SearchResponse)
_sym_db.RegisterMessage(SearchResponse.List)
_sym_db.RegisterMessage(SearchResponse.List.LastVersionInfo)

SearchResponseWrapper = _reflection.GeneratedProtocolMessageType('SearchResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHRESPONSEWRAPPER,
  '__module__' : 'search_pb2'
  # @@protoc_insertion_point(class_scope:pkg.SearchResponseWrapper)
  })
_sym_db.RegisterMessage(SearchResponseWrapper)


# @@protoc_insertion_point(module_scope)
