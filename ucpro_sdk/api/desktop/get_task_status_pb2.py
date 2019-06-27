# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_task_status.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_task_status.proto',
  package='desktop',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x15get_task_status.proto\x12\x07\x64\x65sktop\"&\n\x14GetTaskStatusRequest\x12\x0e\n\x06taskId\x18\x01 \x01(\t\"D\n\x15GetTaskStatusResponse\x12\x0e\n\x06taskId\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\x0b\n\x03msg\x18\x03 \x01(\t\"~\n\x1cGetTaskStatusResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12,\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1e.desktop.GetTaskStatusResponseb\x06proto3')
)




_GETTASKSTATUSREQUEST = _descriptor.Descriptor(
  name='GetTaskStatusRequest',
  full_name='desktop.GetTaskStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='taskId', full_name='desktop.GetTaskStatusRequest.taskId', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=34,
  serialized_end=72,
)


_GETTASKSTATUSRESPONSE = _descriptor.Descriptor(
  name='GetTaskStatusResponse',
  full_name='desktop.GetTaskStatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='taskId', full_name='desktop.GetTaskStatusResponse.taskId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='desktop.GetTaskStatusResponse.status', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='desktop.GetTaskStatusResponse.msg', index=2,
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
  serialized_start=74,
  serialized_end=142,
)


_GETTASKSTATUSRESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetTaskStatusResponseWrapper',
  full_name='desktop.GetTaskStatusResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='desktop.GetTaskStatusResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='desktop.GetTaskStatusResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='desktop.GetTaskStatusResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='desktop.GetTaskStatusResponseWrapper.data', index=3,
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
  serialized_start=144,
  serialized_end=270,
)

_GETTASKSTATUSRESPONSEWRAPPER.fields_by_name['data'].message_type = _GETTASKSTATUSRESPONSE
DESCRIPTOR.message_types_by_name['GetTaskStatusRequest'] = _GETTASKSTATUSREQUEST
DESCRIPTOR.message_types_by_name['GetTaskStatusResponse'] = _GETTASKSTATUSRESPONSE
DESCRIPTOR.message_types_by_name['GetTaskStatusResponseWrapper'] = _GETTASKSTATUSRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetTaskStatusRequest = _reflection.GeneratedProtocolMessageType('GetTaskStatusRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETTASKSTATUSREQUEST,
  __module__ = 'get_task_status_pb2'
  # @@protoc_insertion_point(class_scope:desktop.GetTaskStatusRequest)
  ))
_sym_db.RegisterMessage(GetTaskStatusRequest)

GetTaskStatusResponse = _reflection.GeneratedProtocolMessageType('GetTaskStatusResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETTASKSTATUSRESPONSE,
  __module__ = 'get_task_status_pb2'
  # @@protoc_insertion_point(class_scope:desktop.GetTaskStatusResponse)
  ))
_sym_db.RegisterMessage(GetTaskStatusResponse)

GetTaskStatusResponseWrapper = _reflection.GeneratedProtocolMessageType('GetTaskStatusResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _GETTASKSTATUSRESPONSEWRAPPER,
  __module__ = 'get_task_status_pb2'
  # @@protoc_insertion_point(class_scope:desktop.GetTaskStatusResponseWrapper)
  ))
_sym_db.RegisterMessage(GetTaskStatusResponseWrapper)


# @@protoc_insertion_point(module_scope)
