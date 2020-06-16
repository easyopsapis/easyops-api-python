# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: create_trigger.proto

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
  name='create_trigger.proto',
  package='pipeline',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14\x63reate_trigger.proto\x12\x08pipeline\x1a)pipeline_sdk/model/pipeline/trigger.proto\"c\n\x14\x43reateTriggerRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x13\n\x0bpipeline_id\x18\x02 \x01(\t\x12\"\n\x07trigger\x18\x03 \x01(\x0b\x32\x11.pipeline.Trigger\"q\n\x1c\x43reateTriggerResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x1f\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x11.pipeline.Triggerb\x06proto3')
  ,
  dependencies=[pipeline__sdk_dot_model_dot_pipeline_dot_trigger__pb2.DESCRIPTOR,])




_CREATETRIGGERREQUEST = _descriptor.Descriptor(
  name='CreateTriggerRequest',
  full_name='pipeline.CreateTriggerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project_id', full_name='pipeline.CreateTriggerRequest.project_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pipeline_id', full_name='pipeline.CreateTriggerRequest.pipeline_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trigger', full_name='pipeline.CreateTriggerRequest.trigger', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=77,
  serialized_end=176,
)


_CREATETRIGGERRESPONSEWRAPPER = _descriptor.Descriptor(
  name='CreateTriggerResponseWrapper',
  full_name='pipeline.CreateTriggerResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='pipeline.CreateTriggerResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='pipeline.CreateTriggerResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='pipeline.CreateTriggerResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='pipeline.CreateTriggerResponseWrapper.data', index=3,
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
  serialized_start=178,
  serialized_end=291,
)

_CREATETRIGGERREQUEST.fields_by_name['trigger'].message_type = pipeline__sdk_dot_model_dot_pipeline_dot_trigger__pb2._TRIGGER
_CREATETRIGGERRESPONSEWRAPPER.fields_by_name['data'].message_type = pipeline__sdk_dot_model_dot_pipeline_dot_trigger__pb2._TRIGGER
DESCRIPTOR.message_types_by_name['CreateTriggerRequest'] = _CREATETRIGGERREQUEST
DESCRIPTOR.message_types_by_name['CreateTriggerResponseWrapper'] = _CREATETRIGGERRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateTriggerRequest = _reflection.GeneratedProtocolMessageType('CreateTriggerRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATETRIGGERREQUEST,
  '__module__' : 'create_trigger_pb2'
  # @@protoc_insertion_point(class_scope:pipeline.CreateTriggerRequest)
  })
_sym_db.RegisterMessage(CreateTriggerRequest)

CreateTriggerResponseWrapper = _reflection.GeneratedProtocolMessageType('CreateTriggerResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _CREATETRIGGERRESPONSEWRAPPER,
  '__module__' : 'create_trigger_pb2'
  # @@protoc_insertion_point(class_scope:pipeline.CreateTriggerResponseWrapper)
  })
_sym_db.RegisterMessage(CreateTriggerResponseWrapper)


# @@protoc_insertion_point(module_scope)
