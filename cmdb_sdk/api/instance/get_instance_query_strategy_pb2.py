# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_instance_query_strategy.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cmdb_sdk.model.cmdb import instance_query_strategy_pb2 as cmdb__sdk_dot_model_dot_cmdb_dot_instance__query__strategy__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_instance_query_strategy.proto',
  package='instance',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n!get_instance_query_strategy.proto\x12\x08instance\x1a\x31\x63mdb_sdk/model/cmdb/instance_query_strategy.proto\x1a\x1cgoogle/protobuf/struct.proto\"G\n\x1fGetInstanceQueryStrategyRequest\x12\x10\n\x08objectId\x18\x01 \x01(\t\x12\x12\n\nstrategyId\x18\x02 \x01(\t\"\x86\x01\n\'GetInstanceQueryStrategyResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12)\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1b.cmdb.InstanceQueryStrategyb\x06proto3')
  ,
  dependencies=[cmdb__sdk_dot_model_dot_cmdb_dot_instance__query__strategy__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_GETINSTANCEQUERYSTRATEGYREQUEST = _descriptor.Descriptor(
  name='GetInstanceQueryStrategyRequest',
  full_name='instance.GetInstanceQueryStrategyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='objectId', full_name='instance.GetInstanceQueryStrategyRequest.objectId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strategyId', full_name='instance.GetInstanceQueryStrategyRequest.strategyId', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=128,
  serialized_end=199,
)


_GETINSTANCEQUERYSTRATEGYRESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetInstanceQueryStrategyResponseWrapper',
  full_name='instance.GetInstanceQueryStrategyResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='instance.GetInstanceQueryStrategyResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='instance.GetInstanceQueryStrategyResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='instance.GetInstanceQueryStrategyResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='instance.GetInstanceQueryStrategyResponseWrapper.data', index=3,
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

_GETINSTANCEQUERYSTRATEGYRESPONSEWRAPPER.fields_by_name['data'].message_type = cmdb__sdk_dot_model_dot_cmdb_dot_instance__query__strategy__pb2._INSTANCEQUERYSTRATEGY
DESCRIPTOR.message_types_by_name['GetInstanceQueryStrategyRequest'] = _GETINSTANCEQUERYSTRATEGYREQUEST
DESCRIPTOR.message_types_by_name['GetInstanceQueryStrategyResponseWrapper'] = _GETINSTANCEQUERYSTRATEGYRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetInstanceQueryStrategyRequest = _reflection.GeneratedProtocolMessageType('GetInstanceQueryStrategyRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETINSTANCEQUERYSTRATEGYREQUEST,
  '__module__' : 'get_instance_query_strategy_pb2'
  # @@protoc_insertion_point(class_scope:instance.GetInstanceQueryStrategyRequest)
  })
_sym_db.RegisterMessage(GetInstanceQueryStrategyRequest)

GetInstanceQueryStrategyResponseWrapper = _reflection.GeneratedProtocolMessageType('GetInstanceQueryStrategyResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _GETINSTANCEQUERYSTRATEGYRESPONSEWRAPPER,
  '__module__' : 'get_instance_query_strategy_pb2'
  # @@protoc_insertion_point(class_scope:instance.GetInstanceQueryStrategyResponseWrapper)
  })
_sym_db.RegisterMessage(GetInstanceQueryStrategyResponseWrapper)


# @@protoc_insertion_point(module_scope)
