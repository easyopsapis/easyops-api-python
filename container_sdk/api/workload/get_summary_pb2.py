# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_summary.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from container_sdk.model.container import workload_pb2 as container__sdk_dot_model_dot_container_dot_workload__pb2
from container_sdk.model.container import pod_detail_pb2 as container__sdk_dot_model_dot_container_dot_pod__detail__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_summary.proto',
  package='workload',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11get_summary.proto\x12\x08workload\x1a,container_sdk/model/container/workload.proto\x1a.container_sdk/model/container/pod_detail.proto\"\'\n\x11GetSummaryRequest\x12\x12\n\ninstanceId\x18\x01 \x01(\t\"_\n\x12GetSummaryResponse\x12%\n\x08workload\x18\x01 \x01(\x0b\x32\x13.container.Workload\x12\"\n\x04pods\x18\x02 \x03(\x0b\x32\x14.container.PodDetail\"y\n\x19GetSummaryResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12*\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1c.workload.GetSummaryResponseb\x06proto3')
  ,
  dependencies=[container__sdk_dot_model_dot_container_dot_workload__pb2.DESCRIPTOR,container__sdk_dot_model_dot_container_dot_pod__detail__pb2.DESCRIPTOR,])




_GETSUMMARYREQUEST = _descriptor.Descriptor(
  name='GetSummaryRequest',
  full_name='workload.GetSummaryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='workload.GetSummaryRequest.instanceId', index=0,
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
  serialized_start=125,
  serialized_end=164,
)


_GETSUMMARYRESPONSE = _descriptor.Descriptor(
  name='GetSummaryResponse',
  full_name='workload.GetSummaryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='workload', full_name='workload.GetSummaryResponse.workload', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pods', full_name='workload.GetSummaryResponse.pods', index=1,
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
  serialized_start=166,
  serialized_end=261,
)


_GETSUMMARYRESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetSummaryResponseWrapper',
  full_name='workload.GetSummaryResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='workload.GetSummaryResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='workload.GetSummaryResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='workload.GetSummaryResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='workload.GetSummaryResponseWrapper.data', index=3,
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
  serialized_start=263,
  serialized_end=384,
)

_GETSUMMARYRESPONSE.fields_by_name['workload'].message_type = container__sdk_dot_model_dot_container_dot_workload__pb2._WORKLOAD
_GETSUMMARYRESPONSE.fields_by_name['pods'].message_type = container__sdk_dot_model_dot_container_dot_pod__detail__pb2._PODDETAIL
_GETSUMMARYRESPONSEWRAPPER.fields_by_name['data'].message_type = _GETSUMMARYRESPONSE
DESCRIPTOR.message_types_by_name['GetSummaryRequest'] = _GETSUMMARYREQUEST
DESCRIPTOR.message_types_by_name['GetSummaryResponse'] = _GETSUMMARYRESPONSE
DESCRIPTOR.message_types_by_name['GetSummaryResponseWrapper'] = _GETSUMMARYRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetSummaryRequest = _reflection.GeneratedProtocolMessageType('GetSummaryRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSUMMARYREQUEST,
  '__module__' : 'get_summary_pb2'
  # @@protoc_insertion_point(class_scope:workload.GetSummaryRequest)
  })
_sym_db.RegisterMessage(GetSummaryRequest)

GetSummaryResponse = _reflection.GeneratedProtocolMessageType('GetSummaryResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSUMMARYRESPONSE,
  '__module__' : 'get_summary_pb2'
  # @@protoc_insertion_point(class_scope:workload.GetSummaryResponse)
  })
_sym_db.RegisterMessage(GetSummaryResponse)

GetSummaryResponseWrapper = _reflection.GeneratedProtocolMessageType('GetSummaryResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _GETSUMMARYRESPONSEWRAPPER,
  '__module__' : 'get_summary_pb2'
  # @@protoc_insertion_point(class_scope:workload.GetSummaryResponseWrapper)
  })
_sym_db.RegisterMessage(GetSummaryResponseWrapper)


# @@protoc_insertion_point(module_scope)
