# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_flow_result.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flow_sdk.model.flow import flow_execute_step_pb2 as flow__sdk_dot_model_dot_flow_dot_flow__execute__step__pb2
from flow_sdk.model.flow import flow_instance_pb2 as flow__sdk_dot_model_dot_flow_dot_flow__instance__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_flow_result.proto',
  package='execute',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x15get_flow_result.proto\x12\x07\x65xecute\x1a+flow_sdk/model/flow/flow_execute_step.proto\x1a\'flow_sdk/model/flow/flow_instance.proto\x1a\x1cgoogle/protobuf/struct.proto\"&\n\x14GetFlowResultRequest\x12\x0e\n\x06taskId\x18\x01 \x01(\t\"r\n\x1cGetFlowResultResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12 \n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x12.flow.FlowInstanceb\x06proto3')
  ,
  dependencies=[flow__sdk_dot_model_dot_flow_dot_flow__execute__step__pb2.DESCRIPTOR,flow__sdk_dot_model_dot_flow_dot_flow__instance__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_GETFLOWRESULTREQUEST = _descriptor.Descriptor(
  name='GetFlowResultRequest',
  full_name='execute.GetFlowResultRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='taskId', full_name='execute.GetFlowResultRequest.taskId', index=0,
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
  serialized_start=150,
  serialized_end=188,
)


_GETFLOWRESULTRESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetFlowResultResponseWrapper',
  full_name='execute.GetFlowResultResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='execute.GetFlowResultResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='execute.GetFlowResultResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='execute.GetFlowResultResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='execute.GetFlowResultResponseWrapper.data', index=3,
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
  serialized_start=190,
  serialized_end=304,
)

_GETFLOWRESULTRESPONSEWRAPPER.fields_by_name['data'].message_type = flow__sdk_dot_model_dot_flow_dot_flow__instance__pb2._FLOWINSTANCE
DESCRIPTOR.message_types_by_name['GetFlowResultRequest'] = _GETFLOWRESULTREQUEST
DESCRIPTOR.message_types_by_name['GetFlowResultResponseWrapper'] = _GETFLOWRESULTRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetFlowResultRequest = _reflection.GeneratedProtocolMessageType('GetFlowResultRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETFLOWRESULTREQUEST,
  '__module__' : 'get_flow_result_pb2'
  # @@protoc_insertion_point(class_scope:execute.GetFlowResultRequest)
  })
_sym_db.RegisterMessage(GetFlowResultRequest)

GetFlowResultResponseWrapper = _reflection.GeneratedProtocolMessageType('GetFlowResultResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _GETFLOWRESULTRESPONSEWRAPPER,
  '__module__' : 'get_flow_result_pb2'
  # @@protoc_insertion_point(class_scope:execute.GetFlowResultResponseWrapper)
  })
_sym_db.RegisterMessage(GetFlowResultResponseWrapper)


# @@protoc_insertion_point(module_scope)
