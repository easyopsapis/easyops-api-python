# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: easy_command_callback.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from model.easy_command import target_log_pb2 as model_dot_easy__command_dot_target__log__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='easy_command_callback.proto',
  package='history',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1b\x65\x61sy_command_callback.proto\x12\x07history\x1a#model/easy_command/target_log.proto\x1a\x1bgoogle/protobuf/empty.proto\"\xee\x01\n\x1a\x45\x61syCommandCallbackRequest\x12\x10\n\x08pluginId\x18\x01 \x01(\t\x12\x18\n\x10inspectionTaskId\x18\x02 \x01(\t\x12\r\n\x05jobId\x18\x03 \x01(\t\x12\x0e\n\x06taskId\x18\x04 \x01(\t\x12\x0e\n\x06status\x18\x05 \x01(\t\x12\x10\n\x08usedTime\x18\x06 \x01(\x05\x12\x11\n\tstartTime\x18\x07 \x01(\t\x12\x12\n\nupdateTime\x18\x08 \x01(\t\x12\x0f\n\x07\x65ndTime\x18\t \x01(\t\x12+\n\ntargetsLog\x18\n \x03(\x0b\x32\x17.easy_command.TargetLog\"|\n\"EasyCommandCallbackResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12$\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x16.google.protobuf.Emptyb\x06proto3')
  ,
  dependencies=[model_dot_easy__command_dot_target__log__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_EASYCOMMANDCALLBACKREQUEST = _descriptor.Descriptor(
  name='EasyCommandCallbackRequest',
  full_name='history.EasyCommandCallbackRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pluginId', full_name='history.EasyCommandCallbackRequest.pluginId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inspectionTaskId', full_name='history.EasyCommandCallbackRequest.inspectionTaskId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='jobId', full_name='history.EasyCommandCallbackRequest.jobId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='taskId', full_name='history.EasyCommandCallbackRequest.taskId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='history.EasyCommandCallbackRequest.status', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='usedTime', full_name='history.EasyCommandCallbackRequest.usedTime', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='history.EasyCommandCallbackRequest.startTime', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updateTime', full_name='history.EasyCommandCallbackRequest.updateTime', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endTime', full_name='history.EasyCommandCallbackRequest.endTime', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targetsLog', full_name='history.EasyCommandCallbackRequest.targetsLog', index=9,
      number=10, type=11, cpp_type=10, label=3,
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
  serialized_start=107,
  serialized_end=345,
)


_EASYCOMMANDCALLBACKRESPONSEWRAPPER = _descriptor.Descriptor(
  name='EasyCommandCallbackResponseWrapper',
  full_name='history.EasyCommandCallbackResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='history.EasyCommandCallbackResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='history.EasyCommandCallbackResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='history.EasyCommandCallbackResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='history.EasyCommandCallbackResponseWrapper.data', index=3,
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
  serialized_start=347,
  serialized_end=471,
)

_EASYCOMMANDCALLBACKREQUEST.fields_by_name['targetsLog'].message_type = model_dot_easy__command_dot_target__log__pb2._TARGETLOG
_EASYCOMMANDCALLBACKRESPONSEWRAPPER.fields_by_name['data'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
DESCRIPTOR.message_types_by_name['EasyCommandCallbackRequest'] = _EASYCOMMANDCALLBACKREQUEST
DESCRIPTOR.message_types_by_name['EasyCommandCallbackResponseWrapper'] = _EASYCOMMANDCALLBACKRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EasyCommandCallbackRequest = _reflection.GeneratedProtocolMessageType('EasyCommandCallbackRequest', (_message.Message,), dict(
  DESCRIPTOR = _EASYCOMMANDCALLBACKREQUEST,
  __module__ = 'easy_command_callback_pb2'
  # @@protoc_insertion_point(class_scope:history.EasyCommandCallbackRequest)
  ))
_sym_db.RegisterMessage(EasyCommandCallbackRequest)

EasyCommandCallbackResponseWrapper = _reflection.GeneratedProtocolMessageType('EasyCommandCallbackResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _EASYCOMMANDCALLBACKRESPONSEWRAPPER,
  __module__ = 'easy_command_callback_pb2'
  # @@protoc_insertion_point(class_scope:history.EasyCommandCallbackResponseWrapper)
  ))
_sym_db.RegisterMessage(EasyCommandCallbackResponseWrapper)


# @@protoc_insertion_point(module_scope)