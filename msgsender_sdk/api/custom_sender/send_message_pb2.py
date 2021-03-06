# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: send_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from msgsender_sdk.model.msgsender import send_message_request_data_pb2 as msgsender__sdk_dot_model_dot_msgsender_dot_send__message__request__data__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='send_message.proto',
  package='custom_sender',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x12send_message.proto\x12\rcustom_sender\x1a=msgsender_sdk/model/msgsender/send_message_request_data.proto\x1a\x1cgoogle/protobuf/struct.proto\"W\n\x13SendMessageResponse\x12%\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\x05\"\x80\x01\n\x1aSendMessageResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x30\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\".custom_sender.SendMessageResponseb\x06proto3')
  ,
  dependencies=[msgsender__sdk_dot_model_dot_msgsender_dot_send__message__request__data__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_SENDMESSAGERESPONSE = _descriptor.Descriptor(
  name='SendMessageResponse',
  full_name='custom_sender.SendMessageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='custom_sender.SendMessageResponse.data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='custom_sender.SendMessageResponse.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='custom_sender.SendMessageResponse.code', index=2,
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
  serialized_start=130,
  serialized_end=217,
)


_SENDMESSAGERESPONSEWRAPPER = _descriptor.Descriptor(
  name='SendMessageResponseWrapper',
  full_name='custom_sender.SendMessageResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='custom_sender.SendMessageResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='custom_sender.SendMessageResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='custom_sender.SendMessageResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='custom_sender.SendMessageResponseWrapper.data', index=3,
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
  serialized_start=220,
  serialized_end=348,
)

_SENDMESSAGERESPONSE.fields_by_name['data'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SENDMESSAGERESPONSEWRAPPER.fields_by_name['data'].message_type = _SENDMESSAGERESPONSE
DESCRIPTOR.message_types_by_name['SendMessageResponse'] = _SENDMESSAGERESPONSE
DESCRIPTOR.message_types_by_name['SendMessageResponseWrapper'] = _SENDMESSAGERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SendMessageResponse = _reflection.GeneratedProtocolMessageType('SendMessageResponse', (_message.Message,), {
  'DESCRIPTOR' : _SENDMESSAGERESPONSE,
  '__module__' : 'send_message_pb2'
  # @@protoc_insertion_point(class_scope:custom_sender.SendMessageResponse)
  })
_sym_db.RegisterMessage(SendMessageResponse)

SendMessageResponseWrapper = _reflection.GeneratedProtocolMessageType('SendMessageResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _SENDMESSAGERESPONSEWRAPPER,
  '__module__' : 'send_message_pb2'
  # @@protoc_insertion_point(class_scope:custom_sender.SendMessageResponseWrapper)
  })
_sym_db.RegisterMessage(SendMessageResponseWrapper)


# @@protoc_insertion_point(module_scope)
