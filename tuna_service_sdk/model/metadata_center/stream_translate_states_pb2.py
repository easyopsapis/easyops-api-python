# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stream_translate_states.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tuna_service_sdk.model.metadata_center import stream_translate_package_pb2 as tuna__service__sdk_dot_model_dot_metadata__center_dot_stream__translate__package__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='stream_translate_states.proto',
  package='metadata_center',
  syntax='proto3',
  serialized_options=_b('ZIgo.easyops.local/contracts/protorepo-models/easyops/model/metadata_center'),
  serialized_pb=_b('\n\x1dstream_translate_states.proto\x12\x0fmetadata_center\x1a\x45tuna_service_sdk/model/metadata_center/stream_translate_package.proto\"o\n\x15StreamTranslateStates\x12\x0b\n\x03org\x18\x01 \x01(\x05\x12\x0f\n\x07\x63ommand\x18\x02 \x01(\t\x12\x38\n\x07payload\x18\x03 \x03(\x0b\x32\'.metadata_center.StreamTranslatePackageBKZIgo.easyops.local/contracts/protorepo-models/easyops/model/metadata_centerb\x06proto3')
  ,
  dependencies=[tuna__service__sdk_dot_model_dot_metadata__center_dot_stream__translate__package__pb2.DESCRIPTOR,])




_STREAMTRANSLATESTATES = _descriptor.Descriptor(
  name='StreamTranslateStates',
  full_name='metadata_center.StreamTranslateStates',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='org', full_name='metadata_center.StreamTranslateStates.org', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='command', full_name='metadata_center.StreamTranslateStates.command', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='metadata_center.StreamTranslateStates.payload', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=121,
  serialized_end=232,
)

_STREAMTRANSLATESTATES.fields_by_name['payload'].message_type = tuna__service__sdk_dot_model_dot_metadata__center_dot_stream__translate__package__pb2._STREAMTRANSLATEPACKAGE
DESCRIPTOR.message_types_by_name['StreamTranslateStates'] = _STREAMTRANSLATESTATES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StreamTranslateStates = _reflection.GeneratedProtocolMessageType('StreamTranslateStates', (_message.Message,), {
  'DESCRIPTOR' : _STREAMTRANSLATESTATES,
  '__module__' : 'stream_translate_states_pb2'
  # @@protoc_insertion_point(class_scope:metadata_center.StreamTranslateStates)
  })
_sym_db.RegisterMessage(StreamTranslateStates)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
