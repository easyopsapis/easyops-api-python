# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_collector_job.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from collector_service_sdk.model.collector_service import collector_template_pb2 as collector__service__sdk_dot_model_dot_collector__service_dot_collector__template__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_collector_job.proto',
  package='collector_job',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x17get_collector_job.proto\x12\rcollector_job\x1a\x46\x63ollector_service_sdk/model/collector_service/collector_template.proto\",\n\x16GetCollectorJobRequest\x12\x12\n\ninstanceId\x18\x01 \x01(\t\"\xfd\x02\n\x17GetCollectorJobResponse\x12?\n\x11\x63ollectorTemplate\x18\x01 \x01(\x0b\x32$.collector_service.CollectorTemplate\x12\x12\n\ninstanceId\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x10\n\x08objectId\x18\x04 \x01(\t\x12\x0f\n\x07jobName\x18\x05 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x06 \x01(\t\x12G\n\x0b\x63ollectTime\x18\x07 \x01(\x0b\x32\x32.collector_job.GetCollectorJobResponse.CollectTime\x12\x0f\n\x07timeout\x18\x08 \x01(\x05\x12\x0f\n\x07\x65nabled\x18\t \x01(\x08\x12\x10\n\x08interval\x18\n \x01(\x05\x12\x0c\n\x04path\x18\x0b \x01(\t\x12\x0e\n\x06pathId\x18\x0c \x01(\t\x1a\x31\n\x0b\x43ollectTime\x12\x11\n\tstartTime\x18\x01 \x01(\t\x12\x0f\n\x07\x65ndTime\x18\x02 \x01(\t\"\x88\x01\n\x1eGetCollectorJobResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x34\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32&.collector_job.GetCollectorJobResponseb\x06proto3')
  ,
  dependencies=[collector__service__sdk_dot_model_dot_collector__service_dot_collector__template__pb2.DESCRIPTOR,])




_GETCOLLECTORJOBREQUEST = _descriptor.Descriptor(
  name='GetCollectorJobRequest',
  full_name='collector_job.GetCollectorJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='collector_job.GetCollectorJobRequest.instanceId', index=0,
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
  serialized_start=114,
  serialized_end=158,
)


_GETCOLLECTORJOBRESPONSE_COLLECTTIME = _descriptor.Descriptor(
  name='CollectTime',
  full_name='collector_job.GetCollectorJobResponse.CollectTime',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='startTime', full_name='collector_job.GetCollectorJobResponse.CollectTime.startTime', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endTime', full_name='collector_job.GetCollectorJobResponse.CollectTime.endTime', index=1,
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
  serialized_start=493,
  serialized_end=542,
)

_GETCOLLECTORJOBRESPONSE = _descriptor.Descriptor(
  name='GetCollectorJobResponse',
  full_name='collector_job.GetCollectorJobResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='collectorTemplate', full_name='collector_job.GetCollectorJobResponse.collectorTemplate', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='collector_job.GetCollectorJobResponse.instanceId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='collector_job.GetCollectorJobResponse.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectId', full_name='collector_job.GetCollectorJobResponse.objectId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='jobName', full_name='collector_job.GetCollectorJobResponse.jobName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter', full_name='collector_job.GetCollectorJobResponse.filter', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collectTime', full_name='collector_job.GetCollectorJobResponse.collectTime', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='collector_job.GetCollectorJobResponse.timeout', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enabled', full_name='collector_job.GetCollectorJobResponse.enabled', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interval', full_name='collector_job.GetCollectorJobResponse.interval', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='collector_job.GetCollectorJobResponse.path', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pathId', full_name='collector_job.GetCollectorJobResponse.pathId', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETCOLLECTORJOBRESPONSE_COLLECTTIME, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=161,
  serialized_end=542,
)


_GETCOLLECTORJOBRESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetCollectorJobResponseWrapper',
  full_name='collector_job.GetCollectorJobResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='collector_job.GetCollectorJobResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='collector_job.GetCollectorJobResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='collector_job.GetCollectorJobResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='collector_job.GetCollectorJobResponseWrapper.data', index=3,
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
  serialized_start=545,
  serialized_end=681,
)

_GETCOLLECTORJOBRESPONSE_COLLECTTIME.containing_type = _GETCOLLECTORJOBRESPONSE
_GETCOLLECTORJOBRESPONSE.fields_by_name['collectorTemplate'].message_type = collector__service__sdk_dot_model_dot_collector__service_dot_collector__template__pb2._COLLECTORTEMPLATE
_GETCOLLECTORJOBRESPONSE.fields_by_name['collectTime'].message_type = _GETCOLLECTORJOBRESPONSE_COLLECTTIME
_GETCOLLECTORJOBRESPONSEWRAPPER.fields_by_name['data'].message_type = _GETCOLLECTORJOBRESPONSE
DESCRIPTOR.message_types_by_name['GetCollectorJobRequest'] = _GETCOLLECTORJOBREQUEST
DESCRIPTOR.message_types_by_name['GetCollectorJobResponse'] = _GETCOLLECTORJOBRESPONSE
DESCRIPTOR.message_types_by_name['GetCollectorJobResponseWrapper'] = _GETCOLLECTORJOBRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetCollectorJobRequest = _reflection.GeneratedProtocolMessageType('GetCollectorJobRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCOLLECTORJOBREQUEST,
  '__module__' : 'get_collector_job_pb2'
  # @@protoc_insertion_point(class_scope:collector_job.GetCollectorJobRequest)
  })
_sym_db.RegisterMessage(GetCollectorJobRequest)

GetCollectorJobResponse = _reflection.GeneratedProtocolMessageType('GetCollectorJobResponse', (_message.Message,), {

  'CollectTime' : _reflection.GeneratedProtocolMessageType('CollectTime', (_message.Message,), {
    'DESCRIPTOR' : _GETCOLLECTORJOBRESPONSE_COLLECTTIME,
    '__module__' : 'get_collector_job_pb2'
    # @@protoc_insertion_point(class_scope:collector_job.GetCollectorJobResponse.CollectTime)
    })
  ,
  'DESCRIPTOR' : _GETCOLLECTORJOBRESPONSE,
  '__module__' : 'get_collector_job_pb2'
  # @@protoc_insertion_point(class_scope:collector_job.GetCollectorJobResponse)
  })
_sym_db.RegisterMessage(GetCollectorJobResponse)
_sym_db.RegisterMessage(GetCollectorJobResponse.CollectTime)

GetCollectorJobResponseWrapper = _reflection.GeneratedProtocolMessageType('GetCollectorJobResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _GETCOLLECTORJOBRESPONSEWRAPPER,
  '__module__' : 'get_collector_job_pb2'
  # @@protoc_insertion_point(class_scope:collector_job.GetCollectorJobResponseWrapper)
  })
_sym_db.RegisterMessage(GetCollectorJobResponseWrapper)


# @@protoc_insertion_point(module_scope)
