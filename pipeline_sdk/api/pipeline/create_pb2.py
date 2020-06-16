# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: create.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pipeline_sdk.model.pipeline import pipeline_pb2 as pipeline__sdk_dot_model_dot_pipeline_dot_pipeline__pb2
from pipeline_sdk.model.pipeline import trigger_pb2 as pipeline__sdk_dot_model_dot_pipeline_dot_trigger__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='create.proto',
  package='pipeline',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0c\x63reate.proto\x12\x08pipeline\x1a*pipeline_sdk/model/pipeline/pipeline.proto\x1a)pipeline_sdk/model/pipeline/trigger.proto\"\x82\x01\n\rCreateRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x13\n\x0btemplate_id\x18\x02 \x01(\t\x12$\n\x08pipeline\x18\x03 \x01(\x0b\x32\x12.pipeline.Pipeline\x12\"\n\x07trigger\x18\x04 \x01(\x0b\x32\x11.pipeline.Trigger\"k\n\x15\x43reateResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12 \n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x12.pipeline.Pipelineb\x06proto3')
  ,
  dependencies=[pipeline__sdk_dot_model_dot_pipeline_dot_pipeline__pb2.DESCRIPTOR,pipeline__sdk_dot_model_dot_pipeline_dot_trigger__pb2.DESCRIPTOR,])




_CREATEREQUEST = _descriptor.Descriptor(
  name='CreateRequest',
  full_name='pipeline.CreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project_id', full_name='pipeline.CreateRequest.project_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='template_id', full_name='pipeline.CreateRequest.template_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pipeline', full_name='pipeline.CreateRequest.pipeline', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trigger', full_name='pipeline.CreateRequest.trigger', index=3,
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
  serialized_start=114,
  serialized_end=244,
)


_CREATERESPONSEWRAPPER = _descriptor.Descriptor(
  name='CreateResponseWrapper',
  full_name='pipeline.CreateResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='pipeline.CreateResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='pipeline.CreateResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='pipeline.CreateResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='pipeline.CreateResponseWrapper.data', index=3,
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
  serialized_start=246,
  serialized_end=353,
)

_CREATEREQUEST.fields_by_name['pipeline'].message_type = pipeline__sdk_dot_model_dot_pipeline_dot_pipeline__pb2._PIPELINE
_CREATEREQUEST.fields_by_name['trigger'].message_type = pipeline__sdk_dot_model_dot_pipeline_dot_trigger__pb2._TRIGGER
_CREATERESPONSEWRAPPER.fields_by_name['data'].message_type = pipeline__sdk_dot_model_dot_pipeline_dot_pipeline__pb2._PIPELINE
DESCRIPTOR.message_types_by_name['CreateRequest'] = _CREATEREQUEST
DESCRIPTOR.message_types_by_name['CreateResponseWrapper'] = _CREATERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateRequest = _reflection.GeneratedProtocolMessageType('CreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEREQUEST,
  '__module__' : 'create_pb2'
  # @@protoc_insertion_point(class_scope:pipeline.CreateRequest)
  })
_sym_db.RegisterMessage(CreateRequest)

CreateResponseWrapper = _reflection.GeneratedProtocolMessageType('CreateResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _CREATERESPONSEWRAPPER,
  '__module__' : 'create_pb2'
  # @@protoc_insertion_point(class_scope:pipeline.CreateResponseWrapper)
  })
_sym_db.RegisterMessage(CreateResponseWrapper)


# @@protoc_insertion_point(module_scope)
