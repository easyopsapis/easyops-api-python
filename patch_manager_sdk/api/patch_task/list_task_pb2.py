# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list_task.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='list_task.proto',
  package='patch_task',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0flist_task.proto\x12\npatch_task\"[\n\x14ListPatchTaskRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x11\n\tstartTime\x18\x03 \x01(\x05\x12\x0f\n\x07\x65ndTime\x18\x04 \x01(\x05\"\x81\x03\n\x15ListPatchTaskResponse\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12\x34\n\x04list\x18\x04 \x03(\x0b\x32&.patch_task.ListPatchTaskResponse.List\x1a\x81\x02\n\x04List\x12\x0e\n\x06taskId\x18\x01 \x01(\t\x12?\n\x07request\x18\x02 \x03(\x0b\x32..patch_task.ListPatchTaskResponse.List.Request\x12\x0f\n\x07\x63reator\x18\x03 \x01(\t\x12\r\n\x05\x63time\x18\x04 \x01(\x05\x12\r\n\x05\x65time\x18\x05 \x01(\x05\x12\x0e\n\x06status\x18\x06 \x01(\t\x12\x11\n\tgroupSize\x18\x07 \x01(\x05\x12\x16\n\x0eprocessedCount\x18\x08 \x01(\x05\x1a>\n\x07Request\x12\x0e\n\x06hostId\x18\x01 \x01(\t\x12\x0e\n\x06hostIp\x18\x02 \x01(\t\x12\x13\n\x0bpatchIdList\x18\x03 \x03(\t\"\x81\x01\n\x1cListPatchTaskResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12/\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32!.patch_task.ListPatchTaskResponseb\x06proto3')
)




_LISTPATCHTASKREQUEST = _descriptor.Descriptor(
  name='ListPatchTaskRequest',
  full_name='patch_task.ListPatchTaskRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='patch_task.ListPatchTaskRequest.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='patch_task.ListPatchTaskRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='patch_task.ListPatchTaskRequest.startTime', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endTime', full_name='patch_task.ListPatchTaskRequest.endTime', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=31,
  serialized_end=122,
)


_LISTPATCHTASKRESPONSE_LIST_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='patch_task.ListPatchTaskResponse.List.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hostId', full_name='patch_task.ListPatchTaskResponse.List.Request.hostId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hostIp', full_name='patch_task.ListPatchTaskResponse.List.Request.hostIp', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='patchIdList', full_name='patch_task.ListPatchTaskResponse.List.Request.patchIdList', index=2,
      number=3, type=9, cpp_type=9, label=3,
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
  serialized_start=448,
  serialized_end=510,
)

_LISTPATCHTASKRESPONSE_LIST = _descriptor.Descriptor(
  name='List',
  full_name='patch_task.ListPatchTaskResponse.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='taskId', full_name='patch_task.ListPatchTaskResponse.List.taskId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request', full_name='patch_task.ListPatchTaskResponse.List.request', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='patch_task.ListPatchTaskResponse.List.creator', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='patch_task.ListPatchTaskResponse.List.ctime', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='etime', full_name='patch_task.ListPatchTaskResponse.List.etime', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='patch_task.ListPatchTaskResponse.List.status', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='groupSize', full_name='patch_task.ListPatchTaskResponse.List.groupSize', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processedCount', full_name='patch_task.ListPatchTaskResponse.List.processedCount', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTPATCHTASKRESPONSE_LIST_REQUEST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=253,
  serialized_end=510,
)

_LISTPATCHTASKRESPONSE = _descriptor.Descriptor(
  name='ListPatchTaskResponse',
  full_name='patch_task.ListPatchTaskResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='patch_task.ListPatchTaskResponse.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='patch_task.ListPatchTaskResponse.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='patch_task.ListPatchTaskResponse.total', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='patch_task.ListPatchTaskResponse.list', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTPATCHTASKRESPONSE_LIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=125,
  serialized_end=510,
)


_LISTPATCHTASKRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListPatchTaskResponseWrapper',
  full_name='patch_task.ListPatchTaskResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='patch_task.ListPatchTaskResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='patch_task.ListPatchTaskResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='patch_task.ListPatchTaskResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='patch_task.ListPatchTaskResponseWrapper.data', index=3,
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
  serialized_start=513,
  serialized_end=642,
)

_LISTPATCHTASKRESPONSE_LIST_REQUEST.containing_type = _LISTPATCHTASKRESPONSE_LIST
_LISTPATCHTASKRESPONSE_LIST.fields_by_name['request'].message_type = _LISTPATCHTASKRESPONSE_LIST_REQUEST
_LISTPATCHTASKRESPONSE_LIST.containing_type = _LISTPATCHTASKRESPONSE
_LISTPATCHTASKRESPONSE.fields_by_name['list'].message_type = _LISTPATCHTASKRESPONSE_LIST
_LISTPATCHTASKRESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTPATCHTASKRESPONSE
DESCRIPTOR.message_types_by_name['ListPatchTaskRequest'] = _LISTPATCHTASKREQUEST
DESCRIPTOR.message_types_by_name['ListPatchTaskResponse'] = _LISTPATCHTASKRESPONSE
DESCRIPTOR.message_types_by_name['ListPatchTaskResponseWrapper'] = _LISTPATCHTASKRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListPatchTaskRequest = _reflection.GeneratedProtocolMessageType('ListPatchTaskRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTPATCHTASKREQUEST,
  '__module__' : 'list_task_pb2'
  # @@protoc_insertion_point(class_scope:patch_task.ListPatchTaskRequest)
  })
_sym_db.RegisterMessage(ListPatchTaskRequest)

ListPatchTaskResponse = _reflection.GeneratedProtocolMessageType('ListPatchTaskResponse', (_message.Message,), {

  'List' : _reflection.GeneratedProtocolMessageType('List', (_message.Message,), {

    'Request' : _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
      'DESCRIPTOR' : _LISTPATCHTASKRESPONSE_LIST_REQUEST,
      '__module__' : 'list_task_pb2'
      # @@protoc_insertion_point(class_scope:patch_task.ListPatchTaskResponse.List.Request)
      })
    ,
    'DESCRIPTOR' : _LISTPATCHTASKRESPONSE_LIST,
    '__module__' : 'list_task_pb2'
    # @@protoc_insertion_point(class_scope:patch_task.ListPatchTaskResponse.List)
    })
  ,
  'DESCRIPTOR' : _LISTPATCHTASKRESPONSE,
  '__module__' : 'list_task_pb2'
  # @@protoc_insertion_point(class_scope:patch_task.ListPatchTaskResponse)
  })
_sym_db.RegisterMessage(ListPatchTaskResponse)
_sym_db.RegisterMessage(ListPatchTaskResponse.List)
_sym_db.RegisterMessage(ListPatchTaskResponse.List.Request)

ListPatchTaskResponseWrapper = _reflection.GeneratedProtocolMessageType('ListPatchTaskResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _LISTPATCHTASKRESPONSEWRAPPER,
  '__module__' : 'list_task_pb2'
  # @@protoc_insertion_point(class_scope:patch_task.ListPatchTaskResponseWrapper)
  })
_sym_db.RegisterMessage(ListPatchTaskResponseWrapper)


# @@protoc_insertion_point(module_scope)
