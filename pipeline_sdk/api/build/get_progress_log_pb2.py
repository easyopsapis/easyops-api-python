# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_progress_log.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from model.pipeline import progress_log_pb2 as model_dot_pipeline_dot_progress__log__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_progress_log.proto',
  package='build',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16get_progress_log.proto\x12\x05\x62uild\x1a!model/pipeline/progress_log.proto\"#\n\x15GetProgressLogRequest\x12\n\n\x02id\x18\x01 \x01(\t\"v\n\x1dGetProgressLogResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12#\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x15.pipeline.ProgressLogb\x06proto3')
  ,
  dependencies=[model_dot_pipeline_dot_progress__log__pb2.DESCRIPTOR,])




_GETPROGRESSLOGREQUEST = _descriptor.Descriptor(
  name='GetProgressLogRequest',
  full_name='build.GetProgressLogRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='build.GetProgressLogRequest.id', index=0,
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
  serialized_start=68,
  serialized_end=103,
)


_GETPROGRESSLOGRESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetProgressLogResponseWrapper',
  full_name='build.GetProgressLogResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='build.GetProgressLogResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='build.GetProgressLogResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='build.GetProgressLogResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='build.GetProgressLogResponseWrapper.data', index=3,
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
  serialized_start=105,
  serialized_end=223,
)

_GETPROGRESSLOGRESPONSEWRAPPER.fields_by_name['data'].message_type = model_dot_pipeline_dot_progress__log__pb2._PROGRESSLOG
DESCRIPTOR.message_types_by_name['GetProgressLogRequest'] = _GETPROGRESSLOGREQUEST
DESCRIPTOR.message_types_by_name['GetProgressLogResponseWrapper'] = _GETPROGRESSLOGRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetProgressLogRequest = _reflection.GeneratedProtocolMessageType('GetProgressLogRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETPROGRESSLOGREQUEST,
  __module__ = 'get_progress_log_pb2'
  # @@protoc_insertion_point(class_scope:build.GetProgressLogRequest)
  ))
_sym_db.RegisterMessage(GetProgressLogRequest)

GetProgressLogResponseWrapper = _reflection.GeneratedProtocolMessageType('GetProgressLogResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _GETPROGRESSLOGRESPONSEWRAPPER,
  __module__ = 'get_progress_log_pb2'
  # @@protoc_insertion_point(class_scope:build.GetProgressLogResponseWrapper)
  ))
_sym_db.RegisterMessage(GetProgressLogResponseWrapper)


# @@protoc_insertion_point(module_scope)
