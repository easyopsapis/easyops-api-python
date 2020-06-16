# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_pipeline_v2.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pipeline_sdk.model.pipeline import pipeline_pb2 as pipeline__sdk_dot_model_dot_pipeline_dot_pipeline__pb2
from pipeline_sdk.model.pipeline import template_pb2 as pipeline__sdk_dot_model_dot_pipeline_dot_template__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_pipeline_v2.proto',
  package='pipeline',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x15get_pipeline_v2.proto\x12\x08pipeline\x1a*pipeline_sdk/model/pipeline/pipeline.proto\x1a*pipeline_sdk/model/pipeline/template.proto\"7\n\x0cGetV2Request\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x13\n\x0bpipeline_id\x18\x02 \x01(\t\"[\n\rGetV2Response\x12$\n\x08pipeline\x18\x01 \x01(\x0b\x32\x12.pipeline.Pipeline\x12$\n\x08template\x18\x02 \x01(\x0b\x32\x12.pipeline.Template\"o\n\x14GetV2ResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12%\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x17.pipeline.GetV2Responseb\x06proto3')
  ,
  dependencies=[pipeline__sdk_dot_model_dot_pipeline_dot_pipeline__pb2.DESCRIPTOR,pipeline__sdk_dot_model_dot_pipeline_dot_template__pb2.DESCRIPTOR,])




_GETV2REQUEST = _descriptor.Descriptor(
  name='GetV2Request',
  full_name='pipeline.GetV2Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project_id', full_name='pipeline.GetV2Request.project_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pipeline_id', full_name='pipeline.GetV2Request.pipeline_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=123,
  serialized_end=178,
)


_GETV2RESPONSE = _descriptor.Descriptor(
  name='GetV2Response',
  full_name='pipeline.GetV2Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pipeline', full_name='pipeline.GetV2Response.pipeline', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='template', full_name='pipeline.GetV2Response.template', index=1,
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
  serialized_start=180,
  serialized_end=271,
)


_GETV2RESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetV2ResponseWrapper',
  full_name='pipeline.GetV2ResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='pipeline.GetV2ResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='pipeline.GetV2ResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='pipeline.GetV2ResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='pipeline.GetV2ResponseWrapper.data', index=3,
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
  serialized_start=273,
  serialized_end=384,
)

_GETV2RESPONSE.fields_by_name['pipeline'].message_type = pipeline__sdk_dot_model_dot_pipeline_dot_pipeline__pb2._PIPELINE
_GETV2RESPONSE.fields_by_name['template'].message_type = pipeline__sdk_dot_model_dot_pipeline_dot_template__pb2._TEMPLATE
_GETV2RESPONSEWRAPPER.fields_by_name['data'].message_type = _GETV2RESPONSE
DESCRIPTOR.message_types_by_name['GetV2Request'] = _GETV2REQUEST
DESCRIPTOR.message_types_by_name['GetV2Response'] = _GETV2RESPONSE
DESCRIPTOR.message_types_by_name['GetV2ResponseWrapper'] = _GETV2RESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetV2Request = _reflection.GeneratedProtocolMessageType('GetV2Request', (_message.Message,), {
  'DESCRIPTOR' : _GETV2REQUEST,
  '__module__' : 'get_pipeline_v2_pb2'
  # @@protoc_insertion_point(class_scope:pipeline.GetV2Request)
  })
_sym_db.RegisterMessage(GetV2Request)

GetV2Response = _reflection.GeneratedProtocolMessageType('GetV2Response', (_message.Message,), {
  'DESCRIPTOR' : _GETV2RESPONSE,
  '__module__' : 'get_pipeline_v2_pb2'
  # @@protoc_insertion_point(class_scope:pipeline.GetV2Response)
  })
_sym_db.RegisterMessage(GetV2Response)

GetV2ResponseWrapper = _reflection.GeneratedProtocolMessageType('GetV2ResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _GETV2RESPONSEWRAPPER,
  '__module__' : 'get_pipeline_v2_pb2'
  # @@protoc_insertion_point(class_scope:pipeline.GetV2ResponseWrapper)
  })
_sym_db.RegisterMessage(GetV2ResponseWrapper)


# @@protoc_insertion_point(module_scope)