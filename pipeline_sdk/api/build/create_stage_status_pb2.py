# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: create_stage_status.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from model.pipeline import stage_status_pb2 as model_dot_pipeline_dot_stage__status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='create_stage_status.proto',
  package='build',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x19\x63reate_stage_status.proto\x12\x05\x62uild\x1a!model/pipeline/stage_status.proto\"S\n\x18\x43reateStageStatusRequest\x12\x10\n\x08\x62uild_id\x18\x01 \x01(\t\x12%\n\x06status\x18\x02 \x01(\x0b\x32\x15.pipeline.StageStatus\"y\n CreateStageStatusResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12#\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x15.pipeline.StageStatusb\x06proto3')
  ,
  dependencies=[model_dot_pipeline_dot_stage__status__pb2.DESCRIPTOR,])




_CREATESTAGESTATUSREQUEST = _descriptor.Descriptor(
  name='CreateStageStatusRequest',
  full_name='build.CreateStageStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='build_id', full_name='build.CreateStageStatusRequest.build_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='build.CreateStageStatusRequest.status', index=1,
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
  serialized_start=71,
  serialized_end=154,
)


_CREATESTAGESTATUSRESPONSEWRAPPER = _descriptor.Descriptor(
  name='CreateStageStatusResponseWrapper',
  full_name='build.CreateStageStatusResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='build.CreateStageStatusResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='build.CreateStageStatusResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='build.CreateStageStatusResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='build.CreateStageStatusResponseWrapper.data', index=3,
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
  serialized_start=156,
  serialized_end=277,
)

_CREATESTAGESTATUSREQUEST.fields_by_name['status'].message_type = model_dot_pipeline_dot_stage__status__pb2._STAGESTATUS
_CREATESTAGESTATUSRESPONSEWRAPPER.fields_by_name['data'].message_type = model_dot_pipeline_dot_stage__status__pb2._STAGESTATUS
DESCRIPTOR.message_types_by_name['CreateStageStatusRequest'] = _CREATESTAGESTATUSREQUEST
DESCRIPTOR.message_types_by_name['CreateStageStatusResponseWrapper'] = _CREATESTAGESTATUSRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateStageStatusRequest = _reflection.GeneratedProtocolMessageType('CreateStageStatusRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATESTAGESTATUSREQUEST,
  __module__ = 'create_stage_status_pb2'
  # @@protoc_insertion_point(class_scope:build.CreateStageStatusRequest)
  ))
_sym_db.RegisterMessage(CreateStageStatusRequest)

CreateStageStatusResponseWrapper = _reflection.GeneratedProtocolMessageType('CreateStageStatusResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _CREATESTAGESTATUSRESPONSEWRAPPER,
  __module__ = 'create_stage_status_pb2'
  # @@protoc_insertion_point(class_scope:build.CreateStageStatusResponseWrapper)
  ))
_sym_db.RegisterMessage(CreateStageStatusResponseWrapper)


# @@protoc_insertion_point(module_scope)
