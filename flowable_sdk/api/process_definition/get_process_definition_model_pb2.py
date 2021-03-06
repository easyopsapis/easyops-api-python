# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_process_definition_model.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flowable_sdk.model.flowable import process_model_pb2 as flowable__sdk_dot_model_dot_flowable_dot_process__model__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_process_definition_model.proto',
  package='process_definition',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\"get_process_definition_model.proto\x12\x12process_definition\x1a/flowable_sdk/model/flowable/process_model.proto\x1a\x1cgoogle/protobuf/struct.proto\"8\n GetProcessDefinitionModelRequest\x12\x14\n\x0c\x64\x65\x66initionId\x18\x01 \x01(\t\"\x8e\x01\n!GetProcessDefinitionModelResponse\x12\x36\n\x15\x64\x65\x66initionsAttributes\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x31\n\tprocesses\x18\x02 \x03(\x0b\x32\x1e.flowable.FlowableProcessModel\"\xa1\x01\n(GetProcessDefinitionModelResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x43\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x35.process_definition.GetProcessDefinitionModelResponseb\x06proto3')
  ,
  dependencies=[flowable__sdk_dot_model_dot_flowable_dot_process__model__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_GETPROCESSDEFINITIONMODELREQUEST = _descriptor.Descriptor(
  name='GetProcessDefinitionModelRequest',
  full_name='process_definition.GetProcessDefinitionModelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='definitionId', full_name='process_definition.GetProcessDefinitionModelRequest.definitionId', index=0,
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
  serialized_start=137,
  serialized_end=193,
)


_GETPROCESSDEFINITIONMODELRESPONSE = _descriptor.Descriptor(
  name='GetProcessDefinitionModelResponse',
  full_name='process_definition.GetProcessDefinitionModelResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='definitionsAttributes', full_name='process_definition.GetProcessDefinitionModelResponse.definitionsAttributes', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processes', full_name='process_definition.GetProcessDefinitionModelResponse.processes', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=196,
  serialized_end=338,
)


_GETPROCESSDEFINITIONMODELRESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetProcessDefinitionModelResponseWrapper',
  full_name='process_definition.GetProcessDefinitionModelResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='process_definition.GetProcessDefinitionModelResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='process_definition.GetProcessDefinitionModelResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='process_definition.GetProcessDefinitionModelResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='process_definition.GetProcessDefinitionModelResponseWrapper.data', index=3,
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
  serialized_start=341,
  serialized_end=502,
)

_GETPROCESSDEFINITIONMODELRESPONSE.fields_by_name['definitionsAttributes'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_GETPROCESSDEFINITIONMODELRESPONSE.fields_by_name['processes'].message_type = flowable__sdk_dot_model_dot_flowable_dot_process__model__pb2._FLOWABLEPROCESSMODEL
_GETPROCESSDEFINITIONMODELRESPONSEWRAPPER.fields_by_name['data'].message_type = _GETPROCESSDEFINITIONMODELRESPONSE
DESCRIPTOR.message_types_by_name['GetProcessDefinitionModelRequest'] = _GETPROCESSDEFINITIONMODELREQUEST
DESCRIPTOR.message_types_by_name['GetProcessDefinitionModelResponse'] = _GETPROCESSDEFINITIONMODELRESPONSE
DESCRIPTOR.message_types_by_name['GetProcessDefinitionModelResponseWrapper'] = _GETPROCESSDEFINITIONMODELRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetProcessDefinitionModelRequest = _reflection.GeneratedProtocolMessageType('GetProcessDefinitionModelRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPROCESSDEFINITIONMODELREQUEST,
  '__module__' : 'get_process_definition_model_pb2'
  # @@protoc_insertion_point(class_scope:process_definition.GetProcessDefinitionModelRequest)
  })
_sym_db.RegisterMessage(GetProcessDefinitionModelRequest)

GetProcessDefinitionModelResponse = _reflection.GeneratedProtocolMessageType('GetProcessDefinitionModelResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPROCESSDEFINITIONMODELRESPONSE,
  '__module__' : 'get_process_definition_model_pb2'
  # @@protoc_insertion_point(class_scope:process_definition.GetProcessDefinitionModelResponse)
  })
_sym_db.RegisterMessage(GetProcessDefinitionModelResponse)

GetProcessDefinitionModelResponseWrapper = _reflection.GeneratedProtocolMessageType('GetProcessDefinitionModelResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _GETPROCESSDEFINITIONMODELRESPONSEWRAPPER,
  '__module__' : 'get_process_definition_model_pb2'
  # @@protoc_insertion_point(class_scope:process_definition.GetProcessDefinitionModelResponseWrapper)
  })
_sym_db.RegisterMessage(GetProcessDefinitionModelResponseWrapper)


# @@protoc_insertion_point(module_scope)
