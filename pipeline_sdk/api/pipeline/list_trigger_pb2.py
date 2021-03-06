# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list_trigger.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pipeline_sdk.model.pipeline import trigger_pb2 as pipeline__sdk_dot_model_dot_pipeline_dot_trigger__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='list_trigger.proto',
  package='pipeline',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x12list_trigger.proto\x12\x08pipeline\x1a)pipeline_sdk/model/pipeline/trigger.proto\")\n\x12ListTriggerRequest\x12\x13\n\x0bpipeline_id\x18\x01 \x01(\t\"f\n\x13ListTriggerResponse\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12\x1f\n\x04list\x18\x04 \x03(\x0b\x32\x11.pipeline.Trigger\"{\n\x1aListTriggerResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12+\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1d.pipeline.ListTriggerResponseb\x06proto3')
  ,
  dependencies=[pipeline__sdk_dot_model_dot_pipeline_dot_trigger__pb2.DESCRIPTOR,])




_LISTTRIGGERREQUEST = _descriptor.Descriptor(
  name='ListTriggerRequest',
  full_name='pipeline.ListTriggerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pipeline_id', full_name='pipeline.ListTriggerRequest.pipeline_id', index=0,
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
  serialized_start=75,
  serialized_end=116,
)


_LISTTRIGGERRESPONSE = _descriptor.Descriptor(
  name='ListTriggerResponse',
  full_name='pipeline.ListTriggerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='pipeline.ListTriggerResponse.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='pipeline.ListTriggerResponse.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='pipeline.ListTriggerResponse.total', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='pipeline.ListTriggerResponse.list', index=3,
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
  serialized_start=118,
  serialized_end=220,
)


_LISTTRIGGERRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListTriggerResponseWrapper',
  full_name='pipeline.ListTriggerResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='pipeline.ListTriggerResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='pipeline.ListTriggerResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='pipeline.ListTriggerResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='pipeline.ListTriggerResponseWrapper.data', index=3,
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
  serialized_start=222,
  serialized_end=345,
)

_LISTTRIGGERRESPONSE.fields_by_name['list'].message_type = pipeline__sdk_dot_model_dot_pipeline_dot_trigger__pb2._TRIGGER
_LISTTRIGGERRESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTTRIGGERRESPONSE
DESCRIPTOR.message_types_by_name['ListTriggerRequest'] = _LISTTRIGGERREQUEST
DESCRIPTOR.message_types_by_name['ListTriggerResponse'] = _LISTTRIGGERRESPONSE
DESCRIPTOR.message_types_by_name['ListTriggerResponseWrapper'] = _LISTTRIGGERRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListTriggerRequest = _reflection.GeneratedProtocolMessageType('ListTriggerRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTTRIGGERREQUEST,
  '__module__' : 'list_trigger_pb2'
  # @@protoc_insertion_point(class_scope:pipeline.ListTriggerRequest)
  })
_sym_db.RegisterMessage(ListTriggerRequest)

ListTriggerResponse = _reflection.GeneratedProtocolMessageType('ListTriggerResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTTRIGGERRESPONSE,
  '__module__' : 'list_trigger_pb2'
  # @@protoc_insertion_point(class_scope:pipeline.ListTriggerResponse)
  })
_sym_db.RegisterMessage(ListTriggerResponse)

ListTriggerResponseWrapper = _reflection.GeneratedProtocolMessageType('ListTriggerResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _LISTTRIGGERRESPONSEWRAPPER,
  '__module__' : 'list_trigger_pb2'
  # @@protoc_insertion_point(class_scope:pipeline.ListTriggerResponseWrapper)
  })
_sym_db.RegisterMessage(ListTriggerResponseWrapper)


# @@protoc_insertion_point(module_scope)
