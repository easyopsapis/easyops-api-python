# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: execute_strategy.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='execute_strategy.proto',
  package='datafilter',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16\x65xecute_strategy.proto\x12\ndatafilter\"=\n\x16\x45xecuteStrategyRequest\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0f\n\x07sendMsg\x18\x02 \x01(\x08\")\n\x17\x45xecuteStrategyResponse\x12\x0e\n\x06\x65xecId\x18\x01 \x01(\t\"\x85\x01\n\x1e\x45xecuteStrategyResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x31\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32#.datafilter.ExecuteStrategyResponseb\x06proto3')
)




_EXECUTESTRATEGYREQUEST = _descriptor.Descriptor(
  name='ExecuteStrategyRequest',
  full_name='datafilter.ExecuteStrategyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='datafilter.ExecuteStrategyRequest.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sendMsg', full_name='datafilter.ExecuteStrategyRequest.sendMsg', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=38,
  serialized_end=99,
)


_EXECUTESTRATEGYRESPONSE = _descriptor.Descriptor(
  name='ExecuteStrategyResponse',
  full_name='datafilter.ExecuteStrategyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='execId', full_name='datafilter.ExecuteStrategyResponse.execId', index=0,
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
  serialized_start=101,
  serialized_end=142,
)


_EXECUTESTRATEGYRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ExecuteStrategyResponseWrapper',
  full_name='datafilter.ExecuteStrategyResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='datafilter.ExecuteStrategyResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='datafilter.ExecuteStrategyResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='datafilter.ExecuteStrategyResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='datafilter.ExecuteStrategyResponseWrapper.data', index=3,
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
  serialized_start=145,
  serialized_end=278,
)

_EXECUTESTRATEGYRESPONSEWRAPPER.fields_by_name['data'].message_type = _EXECUTESTRATEGYRESPONSE
DESCRIPTOR.message_types_by_name['ExecuteStrategyRequest'] = _EXECUTESTRATEGYREQUEST
DESCRIPTOR.message_types_by_name['ExecuteStrategyResponse'] = _EXECUTESTRATEGYRESPONSE
DESCRIPTOR.message_types_by_name['ExecuteStrategyResponseWrapper'] = _EXECUTESTRATEGYRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExecuteStrategyRequest = _reflection.GeneratedProtocolMessageType('ExecuteStrategyRequest', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTESTRATEGYREQUEST,
  '__module__' : 'execute_strategy_pb2'
  # @@protoc_insertion_point(class_scope:datafilter.ExecuteStrategyRequest)
  })
_sym_db.RegisterMessage(ExecuteStrategyRequest)

ExecuteStrategyResponse = _reflection.GeneratedProtocolMessageType('ExecuteStrategyResponse', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTESTRATEGYRESPONSE,
  '__module__' : 'execute_strategy_pb2'
  # @@protoc_insertion_point(class_scope:datafilter.ExecuteStrategyResponse)
  })
_sym_db.RegisterMessage(ExecuteStrategyResponse)

ExecuteStrategyResponseWrapper = _reflection.GeneratedProtocolMessageType('ExecuteStrategyResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTESTRATEGYRESPONSEWRAPPER,
  '__module__' : 'execute_strategy_pb2'
  # @@protoc_insertion_point(class_scope:datafilter.ExecuteStrategyResponseWrapper)
  })
_sym_db.RegisterMessage(ExecuteStrategyResponseWrapper)


# @@protoc_insertion_point(module_scope)
