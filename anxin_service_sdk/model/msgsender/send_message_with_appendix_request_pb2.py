# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: send_message_with_appendix_request.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from anxin_service_sdk.model.msgsender import send_message_request_data_pb2 as anxin__service__sdk_dot_model_dot_msgsender_dot_send__message__request__data__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='send_message_with_appendix_request.proto',
  package='msgsender',
  syntax='proto3',
  serialized_options=_b('ZCgo.easyops.local/contracts/protorepo-models/easyops/model/msgsender'),
  serialized_pb=_b('\n(send_message_with_appendix_request.proto\x12\tmsgsender\x1a\x41\x61nxin_service_sdk/model/msgsender/send_message_request_data.proto\"Q\n\x1eSendMessageWithAppendixRequest\x12/\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32!.msgsender.SendMessageRequestDataBEZCgo.easyops.local/contracts/protorepo-models/easyops/model/msgsenderb\x06proto3')
  ,
  dependencies=[anxin__service__sdk_dot_model_dot_msgsender_dot_send__message__request__data__pb2.DESCRIPTOR,])




_SENDMESSAGEWITHAPPENDIXREQUEST = _descriptor.Descriptor(
  name='SendMessageWithAppendixRequest',
  full_name='msgsender.SendMessageWithAppendixRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='msgsender.SendMessageWithAppendixRequest.data', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=122,
  serialized_end=203,
)

_SENDMESSAGEWITHAPPENDIXREQUEST.fields_by_name['data'].message_type = anxin__service__sdk_dot_model_dot_msgsender_dot_send__message__request__data__pb2._SENDMESSAGEREQUESTDATA
DESCRIPTOR.message_types_by_name['SendMessageWithAppendixRequest'] = _SENDMESSAGEWITHAPPENDIXREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SendMessageWithAppendixRequest = _reflection.GeneratedProtocolMessageType('SendMessageWithAppendixRequest', (_message.Message,), {
  'DESCRIPTOR' : _SENDMESSAGEWITHAPPENDIXREQUEST,
  '__module__' : 'send_message_with_appendix_request_pb2'
  # @@protoc_insertion_point(class_scope:msgsender.SendMessageWithAppendixRequest)
  })
_sym_db.RegisterMessage(SendMessageWithAppendixRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
