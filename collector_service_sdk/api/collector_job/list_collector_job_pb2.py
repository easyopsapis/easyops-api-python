# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list_collector_job.proto

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
  name='list_collector_job.proto',
  package='collector_job',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x18list_collector_job.proto\x12\rcollector_job\x1a\x46\x63ollector_service_sdk/model/collector_service/collector_template.proto\"r\n\x17ListCollectorJobRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x10\n\x08pageSize\x18\x02 \x01(\x05\x12\t\n\x01q\x18\x03 \x01(\t\x12\x1a\n\x12templateInstanceId\x18\x04 \x01(\t\x12\x10\n\x08objectId\x18\x05 \x01(\t\"\xf9\x03\n\x18ListCollectorJobResponse\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12:\n\x04list\x18\x04 \x03(\x0b\x32,.collector_job.ListCollectorJobResponse.List\x1a\xf0\x02\n\x04List\x12?\n\x11\x63ollectorTemplate\x18\x01 \x01(\x0b\x32$.collector_service.CollectorTemplate\x12\x12\n\ninstanceId\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x10\n\x08objectId\x18\x04 \x01(\t\x12\x0f\n\x07jobName\x18\x05 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x06 \x01(\t\x12M\n\x0b\x63ollectTime\x18\x07 \x01(\x0b\x32\x38.collector_job.ListCollectorJobResponse.List.CollectTime\x12\x0f\n\x07timeout\x18\x08 \x01(\x05\x12\x0f\n\x07\x65nabled\x18\t \x01(\x08\x12\x10\n\x08interval\x18\n \x01(\x05\x12\x0c\n\x04path\x18\x0b \x01(\t\x12\x0e\n\x06pathId\x18\x0c \x01(\t\x1a\x31\n\x0b\x43ollectTime\x12\x11\n\tstartTime\x18\x01 \x01(\t\x12\x0f\n\x07\x65ndTime\x18\x02 \x01(\t\"\x8a\x01\n\x1fListCollectorJobResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x35\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\'.collector_job.ListCollectorJobResponseb\x06proto3')
  ,
  dependencies=[collector__service__sdk_dot_model_dot_collector__service_dot_collector__template__pb2.DESCRIPTOR,])




_LISTCOLLECTORJOBREQUEST = _descriptor.Descriptor(
  name='ListCollectorJobRequest',
  full_name='collector_job.ListCollectorJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='collector_job.ListCollectorJobRequest.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='collector_job.ListCollectorJobRequest.pageSize', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='q', full_name='collector_job.ListCollectorJobRequest.q', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='templateInstanceId', full_name='collector_job.ListCollectorJobRequest.templateInstanceId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectId', full_name='collector_job.ListCollectorJobRequest.objectId', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=115,
  serialized_end=229,
)


_LISTCOLLECTORJOBRESPONSE_LIST_COLLECTTIME = _descriptor.Descriptor(
  name='CollectTime',
  full_name='collector_job.ListCollectorJobResponse.List.CollectTime',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='startTime', full_name='collector_job.ListCollectorJobResponse.List.CollectTime.startTime', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endTime', full_name='collector_job.ListCollectorJobResponse.List.CollectTime.endTime', index=1,
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
  serialized_start=688,
  serialized_end=737,
)

_LISTCOLLECTORJOBRESPONSE_LIST = _descriptor.Descriptor(
  name='List',
  full_name='collector_job.ListCollectorJobResponse.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='collectorTemplate', full_name='collector_job.ListCollectorJobResponse.List.collectorTemplate', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='collector_job.ListCollectorJobResponse.List.instanceId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='collector_job.ListCollectorJobResponse.List.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectId', full_name='collector_job.ListCollectorJobResponse.List.objectId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='jobName', full_name='collector_job.ListCollectorJobResponse.List.jobName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter', full_name='collector_job.ListCollectorJobResponse.List.filter', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collectTime', full_name='collector_job.ListCollectorJobResponse.List.collectTime', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='collector_job.ListCollectorJobResponse.List.timeout', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enabled', full_name='collector_job.ListCollectorJobResponse.List.enabled', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interval', full_name='collector_job.ListCollectorJobResponse.List.interval', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='collector_job.ListCollectorJobResponse.List.path', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pathId', full_name='collector_job.ListCollectorJobResponse.List.pathId', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTCOLLECTORJOBRESPONSE_LIST_COLLECTTIME, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=369,
  serialized_end=737,
)

_LISTCOLLECTORJOBRESPONSE = _descriptor.Descriptor(
  name='ListCollectorJobResponse',
  full_name='collector_job.ListCollectorJobResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='collector_job.ListCollectorJobResponse.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='collector_job.ListCollectorJobResponse.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='collector_job.ListCollectorJobResponse.total', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='collector_job.ListCollectorJobResponse.list', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTCOLLECTORJOBRESPONSE_LIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=232,
  serialized_end=737,
)


_LISTCOLLECTORJOBRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListCollectorJobResponseWrapper',
  full_name='collector_job.ListCollectorJobResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='collector_job.ListCollectorJobResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='collector_job.ListCollectorJobResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='collector_job.ListCollectorJobResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='collector_job.ListCollectorJobResponseWrapper.data', index=3,
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
  serialized_start=740,
  serialized_end=878,
)

_LISTCOLLECTORJOBRESPONSE_LIST_COLLECTTIME.containing_type = _LISTCOLLECTORJOBRESPONSE_LIST
_LISTCOLLECTORJOBRESPONSE_LIST.fields_by_name['collectorTemplate'].message_type = collector__service__sdk_dot_model_dot_collector__service_dot_collector__template__pb2._COLLECTORTEMPLATE
_LISTCOLLECTORJOBRESPONSE_LIST.fields_by_name['collectTime'].message_type = _LISTCOLLECTORJOBRESPONSE_LIST_COLLECTTIME
_LISTCOLLECTORJOBRESPONSE_LIST.containing_type = _LISTCOLLECTORJOBRESPONSE
_LISTCOLLECTORJOBRESPONSE.fields_by_name['list'].message_type = _LISTCOLLECTORJOBRESPONSE_LIST
_LISTCOLLECTORJOBRESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTCOLLECTORJOBRESPONSE
DESCRIPTOR.message_types_by_name['ListCollectorJobRequest'] = _LISTCOLLECTORJOBREQUEST
DESCRIPTOR.message_types_by_name['ListCollectorJobResponse'] = _LISTCOLLECTORJOBRESPONSE
DESCRIPTOR.message_types_by_name['ListCollectorJobResponseWrapper'] = _LISTCOLLECTORJOBRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListCollectorJobRequest = _reflection.GeneratedProtocolMessageType('ListCollectorJobRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTCOLLECTORJOBREQUEST,
  '__module__' : 'list_collector_job_pb2'
  # @@protoc_insertion_point(class_scope:collector_job.ListCollectorJobRequest)
  })
_sym_db.RegisterMessage(ListCollectorJobRequest)

ListCollectorJobResponse = _reflection.GeneratedProtocolMessageType('ListCollectorJobResponse', (_message.Message,), {

  'List' : _reflection.GeneratedProtocolMessageType('List', (_message.Message,), {

    'CollectTime' : _reflection.GeneratedProtocolMessageType('CollectTime', (_message.Message,), {
      'DESCRIPTOR' : _LISTCOLLECTORJOBRESPONSE_LIST_COLLECTTIME,
      '__module__' : 'list_collector_job_pb2'
      # @@protoc_insertion_point(class_scope:collector_job.ListCollectorJobResponse.List.CollectTime)
      })
    ,
    'DESCRIPTOR' : _LISTCOLLECTORJOBRESPONSE_LIST,
    '__module__' : 'list_collector_job_pb2'
    # @@protoc_insertion_point(class_scope:collector_job.ListCollectorJobResponse.List)
    })
  ,
  'DESCRIPTOR' : _LISTCOLLECTORJOBRESPONSE,
  '__module__' : 'list_collector_job_pb2'
  # @@protoc_insertion_point(class_scope:collector_job.ListCollectorJobResponse)
  })
_sym_db.RegisterMessage(ListCollectorJobResponse)
_sym_db.RegisterMessage(ListCollectorJobResponse.List)
_sym_db.RegisterMessage(ListCollectorJobResponse.List.CollectTime)

ListCollectorJobResponseWrapper = _reflection.GeneratedProtocolMessageType('ListCollectorJobResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _LISTCOLLECTORJOBRESPONSEWRAPPER,
  '__module__' : 'list_collector_job_pb2'
  # @@protoc_insertion_point(class_scope:collector_job.ListCollectorJobResponseWrapper)
  })
_sym_db.RegisterMessage(ListCollectorJobResponseWrapper)


# @@protoc_insertion_point(module_scope)