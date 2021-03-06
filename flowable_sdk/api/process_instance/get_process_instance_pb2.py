# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_process_instance.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flowable_sdk.model.flowable import process_variable_pb2 as flowable__sdk_dot_model_dot_flowable_dot_process__variable__pb2
from flowable_sdk.model.flowable import process_instance_pb2 as flowable__sdk_dot_model_dot_flowable_dot_process__instance__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_process_instance.proto',
  package='process_instance',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1aget_process_instance.proto\x12\x10process_instance\x1a\x32\x66lowable_sdk/model/flowable/process_variable.proto\x1a\x32\x66lowable_sdk/model/flowable/process_instance.proto\"/\n\x19GetProcessInstanceRequest\x12\x12\n\ninstanceId\x18\x01 \x01(\t\"\x86\x01\n!GetProcessInstanceResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12/\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32!.flowable.FlowableProcessInstanceb\x06proto3')
  ,
  dependencies=[flowable__sdk_dot_model_dot_flowable_dot_process__variable__pb2.DESCRIPTOR,flowable__sdk_dot_model_dot_flowable_dot_process__instance__pb2.DESCRIPTOR,])




_GETPROCESSINSTANCEREQUEST = _descriptor.Descriptor(
  name='GetProcessInstanceRequest',
  full_name='process_instance.GetProcessInstanceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='process_instance.GetProcessInstanceRequest.instanceId', index=0,
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
  serialized_start=152,
  serialized_end=199,
)


_GETPROCESSINSTANCERESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetProcessInstanceResponseWrapper',
  full_name='process_instance.GetProcessInstanceResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='process_instance.GetProcessInstanceResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='process_instance.GetProcessInstanceResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='process_instance.GetProcessInstanceResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='process_instance.GetProcessInstanceResponseWrapper.data', index=3,
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
  serialized_start=202,
  serialized_end=336,
)

_GETPROCESSINSTANCERESPONSEWRAPPER.fields_by_name['data'].message_type = flowable__sdk_dot_model_dot_flowable_dot_process__instance__pb2._FLOWABLEPROCESSINSTANCE
DESCRIPTOR.message_types_by_name['GetProcessInstanceRequest'] = _GETPROCESSINSTANCEREQUEST
DESCRIPTOR.message_types_by_name['GetProcessInstanceResponseWrapper'] = _GETPROCESSINSTANCERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetProcessInstanceRequest = _reflection.GeneratedProtocolMessageType('GetProcessInstanceRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPROCESSINSTANCEREQUEST,
  '__module__' : 'get_process_instance_pb2'
  # @@protoc_insertion_point(class_scope:process_instance.GetProcessInstanceRequest)
  })
_sym_db.RegisterMessage(GetProcessInstanceRequest)

GetProcessInstanceResponseWrapper = _reflection.GeneratedProtocolMessageType('GetProcessInstanceResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _GETPROCESSINSTANCERESPONSEWRAPPER,
  '__module__' : 'get_process_instance_pb2'
  # @@protoc_insertion_point(class_scope:process_instance.GetProcessInstanceResponseWrapper)
  })
_sym_db.RegisterMessage(GetProcessInstanceResponseWrapper)


# @@protoc_insertion_point(module_scope)
