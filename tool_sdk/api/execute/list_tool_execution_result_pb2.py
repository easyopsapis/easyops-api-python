# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list_tool_execution_result.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tool_sdk.model.tool import tool_task_pb2 as tool__sdk_dot_model_dot_tool_dot_tool__task__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='list_tool_execution_result.proto',
  package='execute',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n list_tool_execution_result.proto\x12\x07\x65xecute\x1a#tool_sdk/model/tool/tool_task.proto\"a\n\x1eListToolExecutionResultRequest\x12\x11\n\tstartTime\x18\x01 \x01(\t\x12\x0f\n\x07\x65ndTime\x18\x02 \x01(\t\x12\x0e\n\x06toolId\x18\x03 \x01(\t\x12\x0b\n\x03vId\x18\x04 \x01(\t\"o\n\x1fListToolExecutionResultResponse\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12\x1c\n\x04list\x18\x04 \x03(\x0b\x32\x0e.tool.ToolTask\"\x92\x01\n&ListToolExecutionResultResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x36\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32(.execute.ListToolExecutionResultResponseb\x06proto3')
  ,
  dependencies=[tool__sdk_dot_model_dot_tool_dot_tool__task__pb2.DESCRIPTOR,])




_LISTTOOLEXECUTIONRESULTREQUEST = _descriptor.Descriptor(
  name='ListToolExecutionResultRequest',
  full_name='execute.ListToolExecutionResultRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='startTime', full_name='execute.ListToolExecutionResultRequest.startTime', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endTime', full_name='execute.ListToolExecutionResultRequest.endTime', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='toolId', full_name='execute.ListToolExecutionResultRequest.toolId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vId', full_name='execute.ListToolExecutionResultRequest.vId', index=3,
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
  serialized_start=82,
  serialized_end=179,
)


_LISTTOOLEXECUTIONRESULTRESPONSE = _descriptor.Descriptor(
  name='ListToolExecutionResultResponse',
  full_name='execute.ListToolExecutionResultResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='execute.ListToolExecutionResultResponse.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='execute.ListToolExecutionResultResponse.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='execute.ListToolExecutionResultResponse.total', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='execute.ListToolExecutionResultResponse.list', index=3,
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
  serialized_start=181,
  serialized_end=292,
)


_LISTTOOLEXECUTIONRESULTRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListToolExecutionResultResponseWrapper',
  full_name='execute.ListToolExecutionResultResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='execute.ListToolExecutionResultResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='execute.ListToolExecutionResultResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='execute.ListToolExecutionResultResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='execute.ListToolExecutionResultResponseWrapper.data', index=3,
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
  serialized_end=441,
)

_LISTTOOLEXECUTIONRESULTRESPONSE.fields_by_name['list'].message_type = tool__sdk_dot_model_dot_tool_dot_tool__task__pb2._TOOLTASK
_LISTTOOLEXECUTIONRESULTRESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTTOOLEXECUTIONRESULTRESPONSE
DESCRIPTOR.message_types_by_name['ListToolExecutionResultRequest'] = _LISTTOOLEXECUTIONRESULTREQUEST
DESCRIPTOR.message_types_by_name['ListToolExecutionResultResponse'] = _LISTTOOLEXECUTIONRESULTRESPONSE
DESCRIPTOR.message_types_by_name['ListToolExecutionResultResponseWrapper'] = _LISTTOOLEXECUTIONRESULTRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListToolExecutionResultRequest = _reflection.GeneratedProtocolMessageType('ListToolExecutionResultRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTTOOLEXECUTIONRESULTREQUEST,
  '__module__' : 'list_tool_execution_result_pb2'
  # @@protoc_insertion_point(class_scope:execute.ListToolExecutionResultRequest)
  })
_sym_db.RegisterMessage(ListToolExecutionResultRequest)

ListToolExecutionResultResponse = _reflection.GeneratedProtocolMessageType('ListToolExecutionResultResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTTOOLEXECUTIONRESULTRESPONSE,
  '__module__' : 'list_tool_execution_result_pb2'
  # @@protoc_insertion_point(class_scope:execute.ListToolExecutionResultResponse)
  })
_sym_db.RegisterMessage(ListToolExecutionResultResponse)

ListToolExecutionResultResponseWrapper = _reflection.GeneratedProtocolMessageType('ListToolExecutionResultResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _LISTTOOLEXECUTIONRESULTRESPONSEWRAPPER,
  '__module__' : 'list_tool_execution_result_pb2'
  # @@protoc_insertion_point(class_scope:execute.ListToolExecutionResultResponseWrapper)
  })
_sym_db.RegisterMessage(ListToolExecutionResultResponseWrapper)


# @@protoc_insertion_point(module_scope)