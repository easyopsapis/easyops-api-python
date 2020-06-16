# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: target_range.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flowable_sdk.model.collector_center import cmdb_relation_search_pb2 as flowable__sdk_dot_model_dot_collector__center_dot_cmdb__relation__search__pb2
from flowable_sdk.model.collector_center import cmdb_host_search_pb2 as flowable__sdk_dot_model_dot_collector__center_dot_cmdb__host__search__pb2
from flowable_sdk.model.collector_center import cmdb_host_strategy_pb2 as flowable__sdk_dot_model_dot_collector__center_dot_cmdb__host__strategy__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='target_range.proto',
  package='collector_center',
  syntax='proto3',
  serialized_options=_b('ZJgo.easyops.local/contracts/protorepo-models/easyops/model/collector_center'),
  serialized_pb=_b('\n\x12target_range.proto\x12\x10\x63ollector_center\x1a>flowable_sdk/model/collector_center/cmdb_relation_search.proto\x1a:flowable_sdk/model/collector_center/cmdb_host_search.proto\x1a<flowable_sdk/model/collector_center/cmdb_host_strategy.proto\"\xd5\x01\n\x0bTargetRange\x12\x0c\n\x04type\x18\x01 \x01(\t\x12@\n\x12\x63mdbRelationSearch\x18\x02 \x01(\x0b\x32$.collector_center.CmdbRelationSearch\x12\x38\n\x0e\x63mdbHostSearch\x18\x03 \x01(\x0b\x32 .collector_center.CmdbHostSearch\x12<\n\x10\x63mdbHostStrategy\x18\x04 \x01(\x0b\x32\".collector_center.CmdbHostStrategyBLZJgo.easyops.local/contracts/protorepo-models/easyops/model/collector_centerb\x06proto3')
  ,
  dependencies=[flowable__sdk_dot_model_dot_collector__center_dot_cmdb__relation__search__pb2.DESCRIPTOR,flowable__sdk_dot_model_dot_collector__center_dot_cmdb__host__search__pb2.DESCRIPTOR,flowable__sdk_dot_model_dot_collector__center_dot_cmdb__host__strategy__pb2.DESCRIPTOR,])




_TARGETRANGE = _descriptor.Descriptor(
  name='TargetRange',
  full_name='collector_center.TargetRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='collector_center.TargetRange.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cmdbRelationSearch', full_name='collector_center.TargetRange.cmdbRelationSearch', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cmdbHostSearch', full_name='collector_center.TargetRange.cmdbHostSearch', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cmdbHostStrategy', full_name='collector_center.TargetRange.cmdbHostStrategy', index=3,
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
  serialized_start=227,
  serialized_end=440,
)

_TARGETRANGE.fields_by_name['cmdbRelationSearch'].message_type = flowable__sdk_dot_model_dot_collector__center_dot_cmdb__relation__search__pb2._CMDBRELATIONSEARCH
_TARGETRANGE.fields_by_name['cmdbHostSearch'].message_type = flowable__sdk_dot_model_dot_collector__center_dot_cmdb__host__search__pb2._CMDBHOSTSEARCH
_TARGETRANGE.fields_by_name['cmdbHostStrategy'].message_type = flowable__sdk_dot_model_dot_collector__center_dot_cmdb__host__strategy__pb2._CMDBHOSTSTRATEGY
DESCRIPTOR.message_types_by_name['TargetRange'] = _TARGETRANGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TargetRange = _reflection.GeneratedProtocolMessageType('TargetRange', (_message.Message,), {
  'DESCRIPTOR' : _TARGETRANGE,
  '__module__' : 'target_range_pb2'
  # @@protoc_insertion_point(class_scope:collector_center.TargetRange)
  })
_sym_db.RegisterMessage(TargetRange)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
