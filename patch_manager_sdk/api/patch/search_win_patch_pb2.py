# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: search_win_patch.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from patch_manager_sdk.model.patch_manager import win_patch_pb2 as patch__manager__sdk_dot_model_dot_patch__manager_dot_win__patch__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='search_win_patch.proto',
  package='patch',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16search_win_patch.proto\x12\x05patch\x1a\x35patch_manager_sdk/model/patch_manager/win_patch.proto\"I\n\x15SearchWinPatchRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x0f\n\x07keyword\x18\x03 \x01(\t\"\xe3\x03\n\x16SearchWinPatchResponse\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12\x30\n\x04list\x18\x04 \x03(\x0b\x32\".patch.SearchWinPatchResponse.List\x1a\xe6\x02\n\x04List\x12*\n\tPRE_PATCH\x18\x01 \x03(\x0b\x32\x17.patch_manager.WinPatch\x12\x1f\n\x17hostsWithPatchInstalled\x18\x02 \x03(\t\x12\"\n\x1ahostsWithoutPatchInstalled\x18\x03 \x03(\t\x12\x18\n\x10hostsNotRebooted\x18\x04 \x03(\t\x12\x12\n\ninstanceId\x18\x05 \x01(\t\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x11\n\tarticleId\x18\x07 \x01(\t\x12\x13\n\x0breleaseTime\x18\x08 \x01(\t\x12\x10\n\x08osSystem\x18\t \x01(\t\x12\x11\n\tosVersion\x18\n \x03(\t\x12\x16\n\x0eosArchitecture\x18\x0b \x03(\t\x12\x15\n\rrequireReboot\x18\x0c \x01(\x08\x12\x0c\n\x04msrc\x18\r \x01(\t\x12\x0c\n\x04size\x18\x0e \x01(\x05\x12\x0c\n\x04memo\x18\x0f \x01(\t\x12\x0b\n\x03url\x18\x10 \x01(\t\"~\n\x1dSearchWinPatchResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12+\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1d.patch.SearchWinPatchResponseb\x06proto3')
  ,
  dependencies=[patch__manager__sdk_dot_model_dot_patch__manager_dot_win__patch__pb2.DESCRIPTOR,])




_SEARCHWINPATCHREQUEST = _descriptor.Descriptor(
  name='SearchWinPatchRequest',
  full_name='patch.SearchWinPatchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='patch.SearchWinPatchRequest.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='patch.SearchWinPatchRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keyword', full_name='patch.SearchWinPatchRequest.keyword', index=2,
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
  serialized_start=88,
  serialized_end=161,
)


_SEARCHWINPATCHRESPONSE_LIST = _descriptor.Descriptor(
  name='List',
  full_name='patch.SearchWinPatchResponse.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='PRE_PATCH', full_name='patch.SearchWinPatchResponse.List.PRE_PATCH', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hostsWithPatchInstalled', full_name='patch.SearchWinPatchResponse.List.hostsWithPatchInstalled', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hostsWithoutPatchInstalled', full_name='patch.SearchWinPatchResponse.List.hostsWithoutPatchInstalled', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hostsNotRebooted', full_name='patch.SearchWinPatchResponse.List.hostsNotRebooted', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='patch.SearchWinPatchResponse.List.instanceId', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='patch.SearchWinPatchResponse.List.name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='articleId', full_name='patch.SearchWinPatchResponse.List.articleId', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='releaseTime', full_name='patch.SearchWinPatchResponse.List.releaseTime', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='osSystem', full_name='patch.SearchWinPatchResponse.List.osSystem', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='osVersion', full_name='patch.SearchWinPatchResponse.List.osVersion', index=9,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='osArchitecture', full_name='patch.SearchWinPatchResponse.List.osArchitecture', index=10,
      number=11, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requireReboot', full_name='patch.SearchWinPatchResponse.List.requireReboot', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msrc', full_name='patch.SearchWinPatchResponse.List.msrc', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='patch.SearchWinPatchResponse.List.size', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='patch.SearchWinPatchResponse.List.memo', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='patch.SearchWinPatchResponse.List.url', index=15,
      number=16, type=9, cpp_type=9, label=1,
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
  serialized_start=289,
  serialized_end=647,
)

_SEARCHWINPATCHRESPONSE = _descriptor.Descriptor(
  name='SearchWinPatchResponse',
  full_name='patch.SearchWinPatchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='patch.SearchWinPatchResponse.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='patch.SearchWinPatchResponse.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='patch.SearchWinPatchResponse.total', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='patch.SearchWinPatchResponse.list', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SEARCHWINPATCHRESPONSE_LIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=164,
  serialized_end=647,
)


_SEARCHWINPATCHRESPONSEWRAPPER = _descriptor.Descriptor(
  name='SearchWinPatchResponseWrapper',
  full_name='patch.SearchWinPatchResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='patch.SearchWinPatchResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='patch.SearchWinPatchResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='patch.SearchWinPatchResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='patch.SearchWinPatchResponseWrapper.data', index=3,
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
  serialized_start=649,
  serialized_end=775,
)

_SEARCHWINPATCHRESPONSE_LIST.fields_by_name['PRE_PATCH'].message_type = patch__manager__sdk_dot_model_dot_patch__manager_dot_win__patch__pb2._WINPATCH
_SEARCHWINPATCHRESPONSE_LIST.containing_type = _SEARCHWINPATCHRESPONSE
_SEARCHWINPATCHRESPONSE.fields_by_name['list'].message_type = _SEARCHWINPATCHRESPONSE_LIST
_SEARCHWINPATCHRESPONSEWRAPPER.fields_by_name['data'].message_type = _SEARCHWINPATCHRESPONSE
DESCRIPTOR.message_types_by_name['SearchWinPatchRequest'] = _SEARCHWINPATCHREQUEST
DESCRIPTOR.message_types_by_name['SearchWinPatchResponse'] = _SEARCHWINPATCHRESPONSE
DESCRIPTOR.message_types_by_name['SearchWinPatchResponseWrapper'] = _SEARCHWINPATCHRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SearchWinPatchRequest = _reflection.GeneratedProtocolMessageType('SearchWinPatchRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHWINPATCHREQUEST,
  '__module__' : 'search_win_patch_pb2'
  # @@protoc_insertion_point(class_scope:patch.SearchWinPatchRequest)
  })
_sym_db.RegisterMessage(SearchWinPatchRequest)

SearchWinPatchResponse = _reflection.GeneratedProtocolMessageType('SearchWinPatchResponse', (_message.Message,), {

  'List' : _reflection.GeneratedProtocolMessageType('List', (_message.Message,), {
    'DESCRIPTOR' : _SEARCHWINPATCHRESPONSE_LIST,
    '__module__' : 'search_win_patch_pb2'
    # @@protoc_insertion_point(class_scope:patch.SearchWinPatchResponse.List)
    })
  ,
  'DESCRIPTOR' : _SEARCHWINPATCHRESPONSE,
  '__module__' : 'search_win_patch_pb2'
  # @@protoc_insertion_point(class_scope:patch.SearchWinPatchResponse)
  })
_sym_db.RegisterMessage(SearchWinPatchResponse)
_sym_db.RegisterMessage(SearchWinPatchResponse.List)

SearchWinPatchResponseWrapper = _reflection.GeneratedProtocolMessageType('SearchWinPatchResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHWINPATCHRESPONSEWRAPPER,
  '__module__' : 'search_win_patch_pb2'
  # @@protoc_insertion_point(class_scope:patch.SearchWinPatchResponseWrapper)
  })
_sym_db.RegisterMessage(SearchWinPatchResponseWrapper)


# @@protoc_insertion_point(module_scope)