# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: callback_task_v1.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from agent_admin_sdk.model.easy_command import target_log_pb2 as agent__admin__sdk_dot_model_dot_easy__command_dot_target__log__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='callback_task_v1.proto',
  package='admin_task',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16\x63\x61llback_task_v1.proto\x12\nadmin_task\x1a\x33\x61gent_admin_sdk/model/easy_command/target_log.proto\"\x85\x01\n\x1a\x43\x61llbackAdminTaskV1Request\x12\x0e\n\x06taskId\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\x05\x12+\n\ntargetsLog\x18\x04 \x03(\x0b\x32\x17.easy_command.TargetLog\x12\x0c\n\x04name\x18\x05 \x01(\t\"-\n\x1b\x43\x61llbackAdminTaskV1Response\x12\x0e\n\x06status\x18\x01 \x01(\t\"\x8d\x01\n\"CallbackAdminTaskV1ResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x35\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\'.admin_task.CallbackAdminTaskV1Responseb\x06proto3')
  ,
  dependencies=[agent__admin__sdk_dot_model_dot_easy__command_dot_target__log__pb2.DESCRIPTOR,])




_CALLBACKADMINTASKV1REQUEST = _descriptor.Descriptor(
  name='CallbackAdminTaskV1Request',
  full_name='admin_task.CallbackAdminTaskV1Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='taskId', full_name='admin_task.CallbackAdminTaskV1Request.taskId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='admin_task.CallbackAdminTaskV1Request.status', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='admin_task.CallbackAdminTaskV1Request.code', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targetsLog', full_name='admin_task.CallbackAdminTaskV1Request.targetsLog', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='admin_task.CallbackAdminTaskV1Request.name', index=4,
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
  serialized_start=92,
  serialized_end=225,
)


_CALLBACKADMINTASKV1RESPONSE = _descriptor.Descriptor(
  name='CallbackAdminTaskV1Response',
  full_name='admin_task.CallbackAdminTaskV1Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='admin_task.CallbackAdminTaskV1Response.status', index=0,
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
  serialized_start=227,
  serialized_end=272,
)


_CALLBACKADMINTASKV1RESPONSEWRAPPER = _descriptor.Descriptor(
  name='CallbackAdminTaskV1ResponseWrapper',
  full_name='admin_task.CallbackAdminTaskV1ResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='admin_task.CallbackAdminTaskV1ResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='admin_task.CallbackAdminTaskV1ResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='admin_task.CallbackAdminTaskV1ResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='admin_task.CallbackAdminTaskV1ResponseWrapper.data', index=3,
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
  serialized_start=275,
  serialized_end=416,
)

_CALLBACKADMINTASKV1REQUEST.fields_by_name['targetsLog'].message_type = agent__admin__sdk_dot_model_dot_easy__command_dot_target__log__pb2._TARGETLOG
_CALLBACKADMINTASKV1RESPONSEWRAPPER.fields_by_name['data'].message_type = _CALLBACKADMINTASKV1RESPONSE
DESCRIPTOR.message_types_by_name['CallbackAdminTaskV1Request'] = _CALLBACKADMINTASKV1REQUEST
DESCRIPTOR.message_types_by_name['CallbackAdminTaskV1Response'] = _CALLBACKADMINTASKV1RESPONSE
DESCRIPTOR.message_types_by_name['CallbackAdminTaskV1ResponseWrapper'] = _CALLBACKADMINTASKV1RESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CallbackAdminTaskV1Request = _reflection.GeneratedProtocolMessageType('CallbackAdminTaskV1Request', (_message.Message,), {
  'DESCRIPTOR' : _CALLBACKADMINTASKV1REQUEST,
  '__module__' : 'callback_task_v1_pb2'
  # @@protoc_insertion_point(class_scope:admin_task.CallbackAdminTaskV1Request)
  })
_sym_db.RegisterMessage(CallbackAdminTaskV1Request)

CallbackAdminTaskV1Response = _reflection.GeneratedProtocolMessageType('CallbackAdminTaskV1Response', (_message.Message,), {
  'DESCRIPTOR' : _CALLBACKADMINTASKV1RESPONSE,
  '__module__' : 'callback_task_v1_pb2'
  # @@protoc_insertion_point(class_scope:admin_task.CallbackAdminTaskV1Response)
  })
_sym_db.RegisterMessage(CallbackAdminTaskV1Response)

CallbackAdminTaskV1ResponseWrapper = _reflection.GeneratedProtocolMessageType('CallbackAdminTaskV1ResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _CALLBACKADMINTASKV1RESPONSEWRAPPER,
  '__module__' : 'callback_task_v1_pb2'
  # @@protoc_insertion_point(class_scope:admin_task.CallbackAdminTaskV1ResponseWrapper)
  })
_sym_db.RegisterMessage(CallbackAdminTaskV1ResponseWrapper)


# @@protoc_insertion_point(module_scope)
