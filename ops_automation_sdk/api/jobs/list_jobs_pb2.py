# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list_jobs.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from model.ops_automation import scheduler_pb2 as model_dot_ops__automation_dot_scheduler__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='list_jobs.proto',
  package='jobs',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0flist_jobs.proto\x12\x04jobs\x1a$model/ops_automation/scheduler.proto\"2\n\x0fListJobsRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\"\xdd\x01\n\x10ListJobsResponse\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12)\n\x04list\x18\x04 \x03(\x0b\x32\x1b.jobs.ListJobsResponse.List\x1an\n\x04List\x12,\n\tscheduler\x18\x01 \x01(\x0b\x32\x19.ops_automation.Scheduler\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x04 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x05 \x01(\t\"q\n\x17ListJobsResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12$\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x16.jobs.ListJobsResponseb\x06proto3')
  ,
  dependencies=[model_dot_ops__automation_dot_scheduler__pb2.DESCRIPTOR,])




_LISTJOBSREQUEST = _descriptor.Descriptor(
  name='ListJobsRequest',
  full_name='jobs.ListJobsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='jobs.ListJobsRequest.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='jobs.ListJobsRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=63,
  serialized_end=113,
)


_LISTJOBSRESPONSE_LIST = _descriptor.Descriptor(
  name='List',
  full_name='jobs.ListJobsResponse.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scheduler', full_name='jobs.ListJobsResponse.List.scheduler', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='jobs.ListJobsResponse.List.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='jobs.ListJobsResponse.List.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='jobs.ListJobsResponse.List.category', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='desc', full_name='jobs.ListJobsResponse.List.desc', index=4,
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
  serialized_start=227,
  serialized_end=337,
)

_LISTJOBSRESPONSE = _descriptor.Descriptor(
  name='ListJobsResponse',
  full_name='jobs.ListJobsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='jobs.ListJobsResponse.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='jobs.ListJobsResponse.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='jobs.ListJobsResponse.total', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='jobs.ListJobsResponse.list', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTJOBSRESPONSE_LIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=116,
  serialized_end=337,
)


_LISTJOBSRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListJobsResponseWrapper',
  full_name='jobs.ListJobsResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='jobs.ListJobsResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='jobs.ListJobsResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='jobs.ListJobsResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='jobs.ListJobsResponseWrapper.data', index=3,
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
  serialized_start=339,
  serialized_end=452,
)

_LISTJOBSRESPONSE_LIST.fields_by_name['scheduler'].message_type = model_dot_ops__automation_dot_scheduler__pb2._SCHEDULER
_LISTJOBSRESPONSE_LIST.containing_type = _LISTJOBSRESPONSE
_LISTJOBSRESPONSE.fields_by_name['list'].message_type = _LISTJOBSRESPONSE_LIST
_LISTJOBSRESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTJOBSRESPONSE
DESCRIPTOR.message_types_by_name['ListJobsRequest'] = _LISTJOBSREQUEST
DESCRIPTOR.message_types_by_name['ListJobsResponse'] = _LISTJOBSRESPONSE
DESCRIPTOR.message_types_by_name['ListJobsResponseWrapper'] = _LISTJOBSRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListJobsRequest = _reflection.GeneratedProtocolMessageType('ListJobsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTJOBSREQUEST,
  __module__ = 'list_jobs_pb2'
  # @@protoc_insertion_point(class_scope:jobs.ListJobsRequest)
  ))
_sym_db.RegisterMessage(ListJobsRequest)

ListJobsResponse = _reflection.GeneratedProtocolMessageType('ListJobsResponse', (_message.Message,), dict(

  List = _reflection.GeneratedProtocolMessageType('List', (_message.Message,), dict(
    DESCRIPTOR = _LISTJOBSRESPONSE_LIST,
    __module__ = 'list_jobs_pb2'
    # @@protoc_insertion_point(class_scope:jobs.ListJobsResponse.List)
    ))
  ,
  DESCRIPTOR = _LISTJOBSRESPONSE,
  __module__ = 'list_jobs_pb2'
  # @@protoc_insertion_point(class_scope:jobs.ListJobsResponse)
  ))
_sym_db.RegisterMessage(ListJobsResponse)
_sym_db.RegisterMessage(ListJobsResponse.List)

ListJobsResponseWrapper = _reflection.GeneratedProtocolMessageType('ListJobsResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _LISTJOBSRESPONSEWRAPPER,
  __module__ = 'list_jobs_pb2'
  # @@protoc_insertion_point(class_scope:jobs.ListJobsResponseWrapper)
  ))
_sym_db.RegisterMessage(ListJobsResponseWrapper)


# @@protoc_insertion_point(module_scope)
