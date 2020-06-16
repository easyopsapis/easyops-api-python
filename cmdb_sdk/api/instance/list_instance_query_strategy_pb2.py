# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list_instance_query_strategy.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cmdb_sdk.model.cmdb import instance_query_strategy_pb2 as cmdb__sdk_dot_model_dot_cmdb_dot_instance__query__strategy__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='list_instance_query_strategy.proto',
  package='instance',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\"list_instance_query_strategy.proto\x12\x08instance\x1a\x31\x63mdb_sdk/model/cmdb/instance_query_strategy.proto\"C\n ListInstanceQueryStrategyRequest\x12\x11\n\tobject_id\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\"|\n!ListInstanceQueryStrategyResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\r\n\x05\x65rror\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\x12)\n\x04\x64\x61ta\x18\x04 \x03(\x0b\x32\x1b.cmdb.InstanceQueryStrategy\"\x97\x01\n(ListInstanceQueryStrategyResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x39\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32+.instance.ListInstanceQueryStrategyResponseb\x06proto3')
  ,
  dependencies=[cmdb__sdk_dot_model_dot_cmdb_dot_instance__query__strategy__pb2.DESCRIPTOR,])




_LISTINSTANCEQUERYSTRATEGYREQUEST = _descriptor.Descriptor(
  name='ListInstanceQueryStrategyRequest',
  full_name='instance.ListInstanceQueryStrategyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_id', full_name='instance.ListInstanceQueryStrategyRequest.object_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='instance.ListInstanceQueryStrategyRequest.type', index=1,
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
  serialized_start=99,
  serialized_end=166,
)


_LISTINSTANCEQUERYSTRATEGYRESPONSE = _descriptor.Descriptor(
  name='ListInstanceQueryStrategyResponse',
  full_name='instance.ListInstanceQueryStrategyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='instance.ListInstanceQueryStrategyResponse.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='instance.ListInstanceQueryStrategyResponse.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='instance.ListInstanceQueryStrategyResponse.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='instance.ListInstanceQueryStrategyResponse.data', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=168,
  serialized_end=292,
)


_LISTINSTANCEQUERYSTRATEGYRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListInstanceQueryStrategyResponseWrapper',
  full_name='instance.ListInstanceQueryStrategyResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='instance.ListInstanceQueryStrategyResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='instance.ListInstanceQueryStrategyResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='instance.ListInstanceQueryStrategyResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='instance.ListInstanceQueryStrategyResponseWrapper.data', index=3,
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
  serialized_start=295,
  serialized_end=446,
)

_LISTINSTANCEQUERYSTRATEGYRESPONSE.fields_by_name['data'].message_type = cmdb__sdk_dot_model_dot_cmdb_dot_instance__query__strategy__pb2._INSTANCEQUERYSTRATEGY
_LISTINSTANCEQUERYSTRATEGYRESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTINSTANCEQUERYSTRATEGYRESPONSE
DESCRIPTOR.message_types_by_name['ListInstanceQueryStrategyRequest'] = _LISTINSTANCEQUERYSTRATEGYREQUEST
DESCRIPTOR.message_types_by_name['ListInstanceQueryStrategyResponse'] = _LISTINSTANCEQUERYSTRATEGYRESPONSE
DESCRIPTOR.message_types_by_name['ListInstanceQueryStrategyResponseWrapper'] = _LISTINSTANCEQUERYSTRATEGYRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListInstanceQueryStrategyRequest = _reflection.GeneratedProtocolMessageType('ListInstanceQueryStrategyRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTINSTANCEQUERYSTRATEGYREQUEST,
  '__module__' : 'list_instance_query_strategy_pb2'
  # @@protoc_insertion_point(class_scope:instance.ListInstanceQueryStrategyRequest)
  })
_sym_db.RegisterMessage(ListInstanceQueryStrategyRequest)

ListInstanceQueryStrategyResponse = _reflection.GeneratedProtocolMessageType('ListInstanceQueryStrategyResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTINSTANCEQUERYSTRATEGYRESPONSE,
  '__module__' : 'list_instance_query_strategy_pb2'
  # @@protoc_insertion_point(class_scope:instance.ListInstanceQueryStrategyResponse)
  })
_sym_db.RegisterMessage(ListInstanceQueryStrategyResponse)

ListInstanceQueryStrategyResponseWrapper = _reflection.GeneratedProtocolMessageType('ListInstanceQueryStrategyResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _LISTINSTANCEQUERYSTRATEGYRESPONSEWRAPPER,
  '__module__' : 'list_instance_query_strategy_pb2'
  # @@protoc_insertion_point(class_scope:instance.ListInstanceQueryStrategyResponseWrapper)
  })
_sym_db.RegisterMessage(ListInstanceQueryStrategyResponseWrapper)


# @@protoc_insertion_point(module_scope)
