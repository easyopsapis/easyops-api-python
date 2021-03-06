# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tool_executon_callback.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tool_sdk.model.tool import extra_info_pb2 as tool__sdk_dot_model_dot_tool_dot_extra__info__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tool_executon_callback.proto',
  package='execute',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1ctool_executon_callback.proto\x12\x07\x65xecute\x1a$tool_sdk/model/tool/extra_info.proto\"b\n\x1cToolExecutionCallbackRequest\x12\x0e\n\x06taskId\x18\x01 \x01(\t\x12\"\n\textraInfo\x18\x02 \x01(\x0b\x32\x0f.tool.ExtraInfo\x12\x0e\n\x06status\x18\x03 \x01(\t\"c\n\x1dToolExecutionCallbackResponse\x12\x0e\n\x06taskId\x18\x01 \x01(\t\x12\"\n\textraInfo\x18\x02 \x01(\x0b\x32\x0f.tool.ExtraInfo\x12\x0e\n\x06status\x18\x03 \x01(\t\"\x8e\x01\n$ToolExecutionCallbackResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x34\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32&.execute.ToolExecutionCallbackResponseb\x06proto3')
  ,
  dependencies=[tool__sdk_dot_model_dot_tool_dot_extra__info__pb2.DESCRIPTOR,])




_TOOLEXECUTIONCALLBACKREQUEST = _descriptor.Descriptor(
  name='ToolExecutionCallbackRequest',
  full_name='execute.ToolExecutionCallbackRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='taskId', full_name='execute.ToolExecutionCallbackRequest.taskId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extraInfo', full_name='execute.ToolExecutionCallbackRequest.extraInfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='execute.ToolExecutionCallbackRequest.status', index=2,
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
  serialized_start=79,
  serialized_end=177,
)


_TOOLEXECUTIONCALLBACKRESPONSE = _descriptor.Descriptor(
  name='ToolExecutionCallbackResponse',
  full_name='execute.ToolExecutionCallbackResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='taskId', full_name='execute.ToolExecutionCallbackResponse.taskId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extraInfo', full_name='execute.ToolExecutionCallbackResponse.extraInfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='execute.ToolExecutionCallbackResponse.status', index=2,
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
  serialized_start=179,
  serialized_end=278,
)


_TOOLEXECUTIONCALLBACKRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ToolExecutionCallbackResponseWrapper',
  full_name='execute.ToolExecutionCallbackResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='execute.ToolExecutionCallbackResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='execute.ToolExecutionCallbackResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='execute.ToolExecutionCallbackResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='execute.ToolExecutionCallbackResponseWrapper.data', index=3,
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
  serialized_start=281,
  serialized_end=423,
)

_TOOLEXECUTIONCALLBACKREQUEST.fields_by_name['extraInfo'].message_type = tool__sdk_dot_model_dot_tool_dot_extra__info__pb2._EXTRAINFO
_TOOLEXECUTIONCALLBACKRESPONSE.fields_by_name['extraInfo'].message_type = tool__sdk_dot_model_dot_tool_dot_extra__info__pb2._EXTRAINFO
_TOOLEXECUTIONCALLBACKRESPONSEWRAPPER.fields_by_name['data'].message_type = _TOOLEXECUTIONCALLBACKRESPONSE
DESCRIPTOR.message_types_by_name['ToolExecutionCallbackRequest'] = _TOOLEXECUTIONCALLBACKREQUEST
DESCRIPTOR.message_types_by_name['ToolExecutionCallbackResponse'] = _TOOLEXECUTIONCALLBACKRESPONSE
DESCRIPTOR.message_types_by_name['ToolExecutionCallbackResponseWrapper'] = _TOOLEXECUTIONCALLBACKRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ToolExecutionCallbackRequest = _reflection.GeneratedProtocolMessageType('ToolExecutionCallbackRequest', (_message.Message,), {
  'DESCRIPTOR' : _TOOLEXECUTIONCALLBACKREQUEST,
  '__module__' : 'tool_executon_callback_pb2'
  # @@protoc_insertion_point(class_scope:execute.ToolExecutionCallbackRequest)
  })
_sym_db.RegisterMessage(ToolExecutionCallbackRequest)

ToolExecutionCallbackResponse = _reflection.GeneratedProtocolMessageType('ToolExecutionCallbackResponse', (_message.Message,), {
  'DESCRIPTOR' : _TOOLEXECUTIONCALLBACKRESPONSE,
  '__module__' : 'tool_executon_callback_pb2'
  # @@protoc_insertion_point(class_scope:execute.ToolExecutionCallbackResponse)
  })
_sym_db.RegisterMessage(ToolExecutionCallbackResponse)

ToolExecutionCallbackResponseWrapper = _reflection.GeneratedProtocolMessageType('ToolExecutionCallbackResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _TOOLEXECUTIONCALLBACKRESPONSEWRAPPER,
  '__module__' : 'tool_executon_callback_pb2'
  # @@protoc_insertion_point(class_scope:execute.ToolExecutionCallbackResponseWrapper)
  })
_sym_db.RegisterMessage(ToolExecutionCallbackResponseWrapper)


# @@protoc_insertion_point(module_scope)
