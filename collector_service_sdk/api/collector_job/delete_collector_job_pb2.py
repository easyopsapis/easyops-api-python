# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: delete_collector_job.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='delete_collector_job.proto',
  package='collector_job',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1a\x64\x65lete_collector_job.proto\x12\rcollector_job\"/\n\x19\x44\x65leteCollectorJobRequest\x12\x12\n\ninstanceId\x18\x01 \x01(\t\"0\n\x1a\x44\x65leteCollectorJobResponse\x12\x12\n\ninstanceId\x18\x01 \x01(\t\"\x8e\x01\n!DeleteCollectorJobResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x37\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32).collector_job.DeleteCollectorJobResponseb\x06proto3')
)




_DELETECOLLECTORJOBREQUEST = _descriptor.Descriptor(
  name='DeleteCollectorJobRequest',
  full_name='collector_job.DeleteCollectorJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='collector_job.DeleteCollectorJobRequest.instanceId', index=0,
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
  serialized_start=45,
  serialized_end=92,
)


_DELETECOLLECTORJOBRESPONSE = _descriptor.Descriptor(
  name='DeleteCollectorJobResponse',
  full_name='collector_job.DeleteCollectorJobResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='collector_job.DeleteCollectorJobResponse.instanceId', index=0,
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
  serialized_start=94,
  serialized_end=142,
)


_DELETECOLLECTORJOBRESPONSEWRAPPER = _descriptor.Descriptor(
  name='DeleteCollectorJobResponseWrapper',
  full_name='collector_job.DeleteCollectorJobResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='collector_job.DeleteCollectorJobResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='collector_job.DeleteCollectorJobResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='collector_job.DeleteCollectorJobResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='collector_job.DeleteCollectorJobResponseWrapper.data', index=3,
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
  serialized_end=287,
)

_DELETECOLLECTORJOBRESPONSEWRAPPER.fields_by_name['data'].message_type = _DELETECOLLECTORJOBRESPONSE
DESCRIPTOR.message_types_by_name['DeleteCollectorJobRequest'] = _DELETECOLLECTORJOBREQUEST
DESCRIPTOR.message_types_by_name['DeleteCollectorJobResponse'] = _DELETECOLLECTORJOBRESPONSE
DESCRIPTOR.message_types_by_name['DeleteCollectorJobResponseWrapper'] = _DELETECOLLECTORJOBRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeleteCollectorJobRequest = _reflection.GeneratedProtocolMessageType('DeleteCollectorJobRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETECOLLECTORJOBREQUEST,
  '__module__' : 'delete_collector_job_pb2'
  # @@protoc_insertion_point(class_scope:collector_job.DeleteCollectorJobRequest)
  })
_sym_db.RegisterMessage(DeleteCollectorJobRequest)

DeleteCollectorJobResponse = _reflection.GeneratedProtocolMessageType('DeleteCollectorJobResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETECOLLECTORJOBRESPONSE,
  '__module__' : 'delete_collector_job_pb2'
  # @@protoc_insertion_point(class_scope:collector_job.DeleteCollectorJobResponse)
  })
_sym_db.RegisterMessage(DeleteCollectorJobResponse)

DeleteCollectorJobResponseWrapper = _reflection.GeneratedProtocolMessageType('DeleteCollectorJobResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _DELETECOLLECTORJOBRESPONSEWRAPPER,
  '__module__' : 'delete_collector_job_pb2'
  # @@protoc_insertion_point(class_scope:collector_job.DeleteCollectorJobResponseWrapper)
  })
_sym_db.RegisterMessage(DeleteCollectorJobResponseWrapper)


# @@protoc_insertion_point(module_scope)
