# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: send_message_request_data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from assets_inventory_sdk.model.msgsender import message_receiver_pb2 as assets__inventory__sdk_dot_model_dot_msgsender_dot_message__receiver__pb2
from assets_inventory_sdk.model.msgsender import messsage_data_pb2 as assets__inventory__sdk_dot_model_dot_msgsender_dot_messsage__data__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='send_message_request_data.proto',
  package='msgsender',
  syntax='proto3',
  serialized_options=_b('ZCgo.easyops.local/contracts/protorepo-models/easyops/model/msgsender'),
  serialized_pb=_b('\n\x1fsend_message_request_data.proto\x12\tmsgsender\x1a;assets_inventory_sdk/model/msgsender/message_receiver.proto\x1a\x38\x61ssets_inventory_sdk/model/msgsender/messsage_data.proto\"q\n\x16SendMessageRequestData\x12-\n\treceivers\x18\x01 \x03(\x0b\x32\x1a.msgsender.MessageReceiver\x12(\n\x08msg_data\x18\x02 \x01(\x0b\x32\x16.msgsender.MessageDataBEZCgo.easyops.local/contracts/protorepo-models/easyops/model/msgsenderb\x06proto3')
  ,
  dependencies=[assets__inventory__sdk_dot_model_dot_msgsender_dot_message__receiver__pb2.DESCRIPTOR,assets__inventory__sdk_dot_model_dot_msgsender_dot_messsage__data__pb2.DESCRIPTOR,])




_SENDMESSAGEREQUESTDATA = _descriptor.Descriptor(
  name='SendMessageRequestData',
  full_name='msgsender.SendMessageRequestData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='receivers', full_name='msgsender.SendMessageRequestData.receivers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg_data', full_name='msgsender.SendMessageRequestData.msg_data', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=165,
  serialized_end=278,
)

_SENDMESSAGEREQUESTDATA.fields_by_name['receivers'].message_type = assets__inventory__sdk_dot_model_dot_msgsender_dot_message__receiver__pb2._MESSAGERECEIVER
_SENDMESSAGEREQUESTDATA.fields_by_name['msg_data'].message_type = assets__inventory__sdk_dot_model_dot_msgsender_dot_messsage__data__pb2._MESSAGEDATA
DESCRIPTOR.message_types_by_name['SendMessageRequestData'] = _SENDMESSAGEREQUESTDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SendMessageRequestData = _reflection.GeneratedProtocolMessageType('SendMessageRequestData', (_message.Message,), {
  'DESCRIPTOR' : _SENDMESSAGEREQUESTDATA,
  '__module__' : 'send_message_request_data_pb2'
  # @@protoc_insertion_point(class_scope:msgsender.SendMessageRequestData)
  })
_sym_db.RegisterMessage(SendMessageRequestData)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
