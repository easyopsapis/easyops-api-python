# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_process_definition.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flowable_sdk.model.flowable import process_definition_pb2 as flowable__sdk_dot_model_dot_flowable_dot_process__definition__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_process_definition.proto',
  package='process_definition',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1cget_process_definition.proto\x12\x12process_definition\x1a\x34\x66lowable_sdk/model/flowable/process_definition.proto\"3\n\x1bGetProcessDefinitionRequest\x12\x14\n\x0c\x64\x65\x66initionId\x18\x01 \x01(\t\"\x8a\x01\n#GetProcessDefinitionResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x31\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32#.flowable.FlowableProcessDefinitionb\x06proto3')
  ,
  dependencies=[flowable__sdk_dot_model_dot_flowable_dot_process__definition__pb2.DESCRIPTOR,])




_GETPROCESSDEFINITIONREQUEST = _descriptor.Descriptor(
  name='GetProcessDefinitionRequest',
  full_name='process_definition.GetProcessDefinitionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='definitionId', full_name='process_definition.GetProcessDefinitionRequest.definitionId', index=0,
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
  serialized_start=106,
  serialized_end=157,
)


_GETPROCESSDEFINITIONRESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetProcessDefinitionResponseWrapper',
  full_name='process_definition.GetProcessDefinitionResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='process_definition.GetProcessDefinitionResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='process_definition.GetProcessDefinitionResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='process_definition.GetProcessDefinitionResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='process_definition.GetProcessDefinitionResponseWrapper.data', index=3,
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
  serialized_start=160,
  serialized_end=298,
)

_GETPROCESSDEFINITIONRESPONSEWRAPPER.fields_by_name['data'].message_type = flowable__sdk_dot_model_dot_flowable_dot_process__definition__pb2._FLOWABLEPROCESSDEFINITION
DESCRIPTOR.message_types_by_name['GetProcessDefinitionRequest'] = _GETPROCESSDEFINITIONREQUEST
DESCRIPTOR.message_types_by_name['GetProcessDefinitionResponseWrapper'] = _GETPROCESSDEFINITIONRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetProcessDefinitionRequest = _reflection.GeneratedProtocolMessageType('GetProcessDefinitionRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPROCESSDEFINITIONREQUEST,
  '__module__' : 'get_process_definition_pb2'
  # @@protoc_insertion_point(class_scope:process_definition.GetProcessDefinitionRequest)
  })
_sym_db.RegisterMessage(GetProcessDefinitionRequest)

GetProcessDefinitionResponseWrapper = _reflection.GeneratedProtocolMessageType('GetProcessDefinitionResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _GETPROCESSDEFINITIONRESPONSEWRAPPER,
  '__module__' : 'get_process_definition_pb2'
  # @@protoc_insertion_point(class_scope:process_definition.GetProcessDefinitionResponseWrapper)
  })
_sym_db.RegisterMessage(GetProcessDefinitionResponseWrapper)


# @@protoc_insertion_point(module_scope)