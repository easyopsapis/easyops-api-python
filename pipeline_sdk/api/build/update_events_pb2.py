# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: update_events.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pipeline_sdk.model.pipeline import git_meta_pb2 as pipeline__sdk_dot_model_dot_pipeline_dot_git__meta__pb2
from pipeline_sdk.model.pipeline import build_status_pb2 as pipeline__sdk_dot_model_dot_pipeline_dot_build__status__pb2
from pipeline_sdk.model.pipeline import build_pb2 as pipeline__sdk_dot_model_dot_pipeline_dot_build__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='update_events.proto',
  package='build',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13update_events.proto\x12\x05\x62uild\x1a*pipeline_sdk/model/pipeline/git_meta.proto\x1a.pipeline_sdk/model/pipeline/build_status.proto\x1a\'pipeline_sdk/model/pipeline/build.proto\"7\n\x13UpdateEventsRequest\x12\x10\n\x08\x62uild_id\x18\x01 \x01(\t\x12\x0e\n\x06\x65vents\x18\x02 \x03(\t\"n\n\x1bUpdateEventsResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x1d\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x0f.pipeline.Buildb\x06proto3')
  ,
  dependencies=[pipeline__sdk_dot_model_dot_pipeline_dot_git__meta__pb2.DESCRIPTOR,pipeline__sdk_dot_model_dot_pipeline_dot_build__status__pb2.DESCRIPTOR,pipeline__sdk_dot_model_dot_pipeline_dot_build__pb2.DESCRIPTOR,])




_UPDATEEVENTSREQUEST = _descriptor.Descriptor(
  name='UpdateEventsRequest',
  full_name='build.UpdateEventsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='build_id', full_name='build.UpdateEventsRequest.build_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='events', full_name='build.UpdateEventsRequest.events', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=163,
  serialized_end=218,
)


_UPDATEEVENTSRESPONSEWRAPPER = _descriptor.Descriptor(
  name='UpdateEventsResponseWrapper',
  full_name='build.UpdateEventsResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='build.UpdateEventsResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='build.UpdateEventsResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='build.UpdateEventsResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='build.UpdateEventsResponseWrapper.data', index=3,
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
  serialized_end=330,
)

_UPDATEEVENTSRESPONSEWRAPPER.fields_by_name['data'].message_type = pipeline__sdk_dot_model_dot_pipeline_dot_build__pb2._BUILD
DESCRIPTOR.message_types_by_name['UpdateEventsRequest'] = _UPDATEEVENTSREQUEST
DESCRIPTOR.message_types_by_name['UpdateEventsResponseWrapper'] = _UPDATEEVENTSRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateEventsRequest = _reflection.GeneratedProtocolMessageType('UpdateEventsRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEEVENTSREQUEST,
  '__module__' : 'update_events_pb2'
  # @@protoc_insertion_point(class_scope:build.UpdateEventsRequest)
  })
_sym_db.RegisterMessage(UpdateEventsRequest)

UpdateEventsResponseWrapper = _reflection.GeneratedProtocolMessageType('UpdateEventsResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEEVENTSRESPONSEWRAPPER,
  '__module__' : 'update_events_pb2'
  # @@protoc_insertion_point(class_scope:build.UpdateEventsResponseWrapper)
  })
_sym_db.RegisterMessage(UpdateEventsResponseWrapper)


# @@protoc_insertion_point(module_scope)
