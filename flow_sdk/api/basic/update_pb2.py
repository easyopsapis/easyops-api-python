# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: update.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flow_sdk.model.flow import flow_step_pb2 as flow__sdk_dot_model_dot_flow_dot_flow__step__pb2
from flow_sdk.model.flow import flow_pb2 as flow__sdk_dot_model_dot_flow_dot_flow__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='update.proto',
  package='basic',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0cupdate.proto\x12\x05\x62\x61sic\x1a#flow_sdk/model/flow/flow_step.proto\x1a\x1e\x66low_sdk/model/flow/flow.proto\x1a\x1cgoogle/protobuf/struct.proto\"g\n\x19UpdateFlowResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x18\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\n.flow.Flowb\x06proto3')
  ,
  dependencies=[flow__sdk_dot_model_dot_flow_dot_flow__step__pb2.DESCRIPTOR,flow__sdk_dot_model_dot_flow_dot_flow__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_UPDATEFLOWRESPONSEWRAPPER = _descriptor.Descriptor(
  name='UpdateFlowResponseWrapper',
  full_name='basic.UpdateFlowResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='basic.UpdateFlowResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='basic.UpdateFlowResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='basic.UpdateFlowResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='basic.UpdateFlowResponseWrapper.data', index=3,
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
  serialized_start=122,
  serialized_end=225,
)

_UPDATEFLOWRESPONSEWRAPPER.fields_by_name['data'].message_type = flow__sdk_dot_model_dot_flow_dot_flow__pb2._FLOW
DESCRIPTOR.message_types_by_name['UpdateFlowResponseWrapper'] = _UPDATEFLOWRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateFlowResponseWrapper = _reflection.GeneratedProtocolMessageType('UpdateFlowResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEFLOWRESPONSEWRAPPER,
  '__module__' : 'update_pb2'
  # @@protoc_insertion_point(class_scope:basic.UpdateFlowResponseWrapper)
  })
_sym_db.RegisterMessage(UpdateFlowResponseWrapper)


# @@protoc_insertion_point(module_scope)
