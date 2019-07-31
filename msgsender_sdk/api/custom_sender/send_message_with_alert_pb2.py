# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: send_message_with_alert.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='send_message_with_alert.proto',
  package='custom_sender',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1dsend_message_with_alert.proto\x12\rcustom_sender\x1a\x1cgoogle/protobuf/struct.proto\"_\n\x1bSendMessageForAlertResponse\x12%\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\x05\"\x90\x01\n\"SendMessageForAlertResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x38\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32*.custom_sender.SendMessageForAlertResponseb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_SENDMESSAGEFORALERTRESPONSE = _descriptor.Descriptor(
  name='SendMessageForAlertResponse',
  full_name='custom_sender.SendMessageForAlertResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='custom_sender.SendMessageForAlertResponse.data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='custom_sender.SendMessageForAlertResponse.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='custom_sender.SendMessageForAlertResponse.code', index=2,
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
  serialized_start=78,
  serialized_end=173,
)


_SENDMESSAGEFORALERTRESPONSEWRAPPER = _descriptor.Descriptor(
  name='SendMessageForAlertResponseWrapper',
  full_name='custom_sender.SendMessageForAlertResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='custom_sender.SendMessageForAlertResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='custom_sender.SendMessageForAlertResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='custom_sender.SendMessageForAlertResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='custom_sender.SendMessageForAlertResponseWrapper.data', index=3,
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
  serialized_start=176,
  serialized_end=320,
)

_SENDMESSAGEFORALERTRESPONSE.fields_by_name['data'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SENDMESSAGEFORALERTRESPONSEWRAPPER.fields_by_name['data'].message_type = _SENDMESSAGEFORALERTRESPONSE
DESCRIPTOR.message_types_by_name['SendMessageForAlertResponse'] = _SENDMESSAGEFORALERTRESPONSE
DESCRIPTOR.message_types_by_name['SendMessageForAlertResponseWrapper'] = _SENDMESSAGEFORALERTRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SendMessageForAlertResponse = _reflection.GeneratedProtocolMessageType('SendMessageForAlertResponse', (_message.Message,), dict(
  DESCRIPTOR = _SENDMESSAGEFORALERTRESPONSE,
  __module__ = 'send_message_with_alert_pb2'
  # @@protoc_insertion_point(class_scope:custom_sender.SendMessageForAlertResponse)
  ))
_sym_db.RegisterMessage(SendMessageForAlertResponse)

SendMessageForAlertResponseWrapper = _reflection.GeneratedProtocolMessageType('SendMessageForAlertResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _SENDMESSAGEFORALERTRESPONSEWRAPPER,
  __module__ = 'send_message_with_alert_pb2'
  # @@protoc_insertion_point(class_scope:custom_sender.SendMessageForAlertResponseWrapper)
  ))
_sym_db.RegisterMessage(SendMessageForAlertResponseWrapper)


# @@protoc_insertion_point(module_scope)
