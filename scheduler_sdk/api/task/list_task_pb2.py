# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list_task.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='list_task.proto',
  package='task',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0flist_task.proto\x12\x04task\x1a\x1cgoogle/protobuf/struct.proto\"\x8e\x01\n\x0fListTaskRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\n__select__\x18\x03 \x01(\t\x12\x12\n\n__sortby__\x18\x04 \x01(\t\x12\x0e\n\x06src_id\x18\x05 \x01(\t\x12\x0f\n\x07\x64isable\x18\x06 \x01(\x05\x12\x11\n\tassignner\x18\x07 \x01(\t\"\xa3\x07\n\x10ListTaskResponse\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12)\n\x04list\x18\x04 \x03(\x0b\x32\x1b.task.ListTaskResponse.List\x1a\xb3\x06\n\x04List\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06job_id\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\x05\x12\x0f\n\x07\x64isable\x18\x04 \x01(\x05\x12\x16\n\x0etask_scheduler\x18\x05 \x01(\t\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\r\n\x05\x65rror\x18\x07 \x01(\t\x12\x39\n\ncmd_config\x18\x08 \x01(\x0b\x32%.task.ListTaskResponse.List.CmdConfig\x12\x10\n\x08job_type\x18\t \x01(\t\x12\x19\n\x11updateAuthorizers\x18\n \x03(\t\x12\x13\n\x0b\x63reate_time\x18\x0b \x01(\t\x12\x11\n\ttask_type\x18\x0c \x01(\t\x12\x0e\n\x06src_id\x18\r \x01(\t\x12<\n\x0b\x61nnotations\x18\x0e \x01(\x0b\x32\'.task.ListTaskResponse.List.Annotations\x12\x13\n\x0bupdate_time\x18\x0f \x01(\t\x12\x10\n\x08\x63md_type\x18\x10 \x01(\t\x12\x19\n\x11\x64\x65leteAuthorizers\x18\x11 \x03(\t\x12\x0c\n\x04user\x18\x12 \x01(\t\x12\x11\n\tinvisible\x18\x13 \x01(\x05\x12\x0b\n\x03org\x18\x14 \x01(\x05\x12\x1a\n\x12operateAuthorizers\x18\x15 \x03(\t\x12\x36\n\x08\x63\x61llback\x18\x16 \x01(\x0b\x32$.task.ListTaskResponse.List.Callback\x12\x11\n\tassignner\x18\x17 \x01(\t\x1a\xad\x01\n\tCmdConfig\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x14\n\x0cservice_name\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\x05\x12\x0c\n\x04host\x18\x04 \x01(\t\x12\x0e\n\x06method\x18\x05 \x01(\t\x12(\n\x07headers\x18\x06 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\'\n\x06params\x18\x07 \x01(\x0b\x32\x17.google.protobuf.Struct\x1a\x1c\n\x0b\x41nnotations\x12\r\n\x05\x61ppId\x18\x01 \x01(\t\x1a\x36\n\x08\x43\x61llback\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x0c\n\x04host\x18\x02 \x01(\t\x12\x0f\n\x07\x65nsName\x18\x03 \x01(\t\"q\n\x17ListTaskResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12$\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x16.task.ListTaskResponseb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_LISTTASKREQUEST = _descriptor.Descriptor(
  name='ListTaskRequest',
  full_name='task.ListTaskRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='task.ListTaskRequest.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='task.ListTaskRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='__select__', full_name='task.ListTaskRequest.__select__', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='__sortby__', full_name='task.ListTaskRequest.__sortby__', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='src_id', full_name='task.ListTaskRequest.src_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disable', full_name='task.ListTaskRequest.disable', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='assignner', full_name='task.ListTaskRequest.assignner', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=56,
  serialized_end=198,
)


_LISTTASKRESPONSE_LIST_CMDCONFIG = _descriptor.Descriptor(
  name='CmdConfig',
  full_name='task.ListTaskResponse.List.CmdConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='task.ListTaskResponse.List.CmdConfig.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service_name', full_name='task.ListTaskResponse.List.CmdConfig.service_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='task.ListTaskResponse.List.CmdConfig.port', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host', full_name='task.ListTaskResponse.List.CmdConfig.host', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='method', full_name='task.ListTaskResponse.List.CmdConfig.method', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='headers', full_name='task.ListTaskResponse.List.CmdConfig.headers', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='params', full_name='task.ListTaskResponse.List.CmdConfig.params', index=6,
      number=7, type=11, cpp_type=10, label=1,
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
  serialized_start=873,
  serialized_end=1046,
)

_LISTTASKRESPONSE_LIST_ANNOTATIONS = _descriptor.Descriptor(
  name='Annotations',
  full_name='task.ListTaskResponse.List.Annotations',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appId', full_name='task.ListTaskResponse.List.Annotations.appId', index=0,
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
  serialized_start=1048,
  serialized_end=1076,
)

_LISTTASKRESPONSE_LIST_CALLBACK = _descriptor.Descriptor(
  name='Callback',
  full_name='task.ListTaskResponse.List.Callback',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='task.ListTaskResponse.List.Callback.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host', full_name='task.ListTaskResponse.List.Callback.host', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ensName', full_name='task.ListTaskResponse.List.Callback.ensName', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=1078,
  serialized_end=1132,
)

_LISTTASKRESPONSE_LIST = _descriptor.Descriptor(
  name='List',
  full_name='task.ListTaskResponse.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='task.ListTaskResponse.List.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='job_id', full_name='task.ListTaskResponse.List.job_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='task.ListTaskResponse.List.status', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disable', full_name='task.ListTaskResponse.List.disable', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='task_scheduler', full_name='task.ListTaskResponse.List.task_scheduler', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='task.ListTaskResponse.List.name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='task.ListTaskResponse.List.error', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cmd_config', full_name='task.ListTaskResponse.List.cmd_config', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='job_type', full_name='task.ListTaskResponse.List.job_type', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updateAuthorizers', full_name='task.ListTaskResponse.List.updateAuthorizers', index=9,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='task.ListTaskResponse.List.create_time', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='task_type', full_name='task.ListTaskResponse.List.task_type', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='src_id', full_name='task.ListTaskResponse.List.src_id', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='annotations', full_name='task.ListTaskResponse.List.annotations', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_time', full_name='task.ListTaskResponse.List.update_time', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cmd_type', full_name='task.ListTaskResponse.List.cmd_type', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deleteAuthorizers', full_name='task.ListTaskResponse.List.deleteAuthorizers', index=16,
      number=17, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='task.ListTaskResponse.List.user', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='invisible', full_name='task.ListTaskResponse.List.invisible', index=18,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org', full_name='task.ListTaskResponse.List.org', index=19,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operateAuthorizers', full_name='task.ListTaskResponse.List.operateAuthorizers', index=20,
      number=21, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='callback', full_name='task.ListTaskResponse.List.callback', index=21,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='assignner', full_name='task.ListTaskResponse.List.assignner', index=22,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTTASKRESPONSE_LIST_CMDCONFIG, _LISTTASKRESPONSE_LIST_ANNOTATIONS, _LISTTASKRESPONSE_LIST_CALLBACK, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=313,
  serialized_end=1132,
)

_LISTTASKRESPONSE = _descriptor.Descriptor(
  name='ListTaskResponse',
  full_name='task.ListTaskResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='task.ListTaskResponse.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='task.ListTaskResponse.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='task.ListTaskResponse.total', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='task.ListTaskResponse.list', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTTASKRESPONSE_LIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=201,
  serialized_end=1132,
)


_LISTTASKRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListTaskResponseWrapper',
  full_name='task.ListTaskResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='task.ListTaskResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='task.ListTaskResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='task.ListTaskResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='task.ListTaskResponseWrapper.data', index=3,
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
  serialized_start=1134,
  serialized_end=1247,
)

_LISTTASKRESPONSE_LIST_CMDCONFIG.fields_by_name['headers'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_LISTTASKRESPONSE_LIST_CMDCONFIG.fields_by_name['params'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_LISTTASKRESPONSE_LIST_CMDCONFIG.containing_type = _LISTTASKRESPONSE_LIST
_LISTTASKRESPONSE_LIST_ANNOTATIONS.containing_type = _LISTTASKRESPONSE_LIST
_LISTTASKRESPONSE_LIST_CALLBACK.containing_type = _LISTTASKRESPONSE_LIST
_LISTTASKRESPONSE_LIST.fields_by_name['cmd_config'].message_type = _LISTTASKRESPONSE_LIST_CMDCONFIG
_LISTTASKRESPONSE_LIST.fields_by_name['annotations'].message_type = _LISTTASKRESPONSE_LIST_ANNOTATIONS
_LISTTASKRESPONSE_LIST.fields_by_name['callback'].message_type = _LISTTASKRESPONSE_LIST_CALLBACK
_LISTTASKRESPONSE_LIST.containing_type = _LISTTASKRESPONSE
_LISTTASKRESPONSE.fields_by_name['list'].message_type = _LISTTASKRESPONSE_LIST
_LISTTASKRESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTTASKRESPONSE
DESCRIPTOR.message_types_by_name['ListTaskRequest'] = _LISTTASKREQUEST
DESCRIPTOR.message_types_by_name['ListTaskResponse'] = _LISTTASKRESPONSE
DESCRIPTOR.message_types_by_name['ListTaskResponseWrapper'] = _LISTTASKRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListTaskRequest = _reflection.GeneratedProtocolMessageType('ListTaskRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTTASKREQUEST,
  __module__ = 'list_task_pb2'
  # @@protoc_insertion_point(class_scope:task.ListTaskRequest)
  ))
_sym_db.RegisterMessage(ListTaskRequest)

ListTaskResponse = _reflection.GeneratedProtocolMessageType('ListTaskResponse', (_message.Message,), dict(

  List = _reflection.GeneratedProtocolMessageType('List', (_message.Message,), dict(

    CmdConfig = _reflection.GeneratedProtocolMessageType('CmdConfig', (_message.Message,), dict(
      DESCRIPTOR = _LISTTASKRESPONSE_LIST_CMDCONFIG,
      __module__ = 'list_task_pb2'
      # @@protoc_insertion_point(class_scope:task.ListTaskResponse.List.CmdConfig)
      ))
    ,

    Annotations = _reflection.GeneratedProtocolMessageType('Annotations', (_message.Message,), dict(
      DESCRIPTOR = _LISTTASKRESPONSE_LIST_ANNOTATIONS,
      __module__ = 'list_task_pb2'
      # @@protoc_insertion_point(class_scope:task.ListTaskResponse.List.Annotations)
      ))
    ,

    Callback = _reflection.GeneratedProtocolMessageType('Callback', (_message.Message,), dict(
      DESCRIPTOR = _LISTTASKRESPONSE_LIST_CALLBACK,
      __module__ = 'list_task_pb2'
      # @@protoc_insertion_point(class_scope:task.ListTaskResponse.List.Callback)
      ))
    ,
    DESCRIPTOR = _LISTTASKRESPONSE_LIST,
    __module__ = 'list_task_pb2'
    # @@protoc_insertion_point(class_scope:task.ListTaskResponse.List)
    ))
  ,
  DESCRIPTOR = _LISTTASKRESPONSE,
  __module__ = 'list_task_pb2'
  # @@protoc_insertion_point(class_scope:task.ListTaskResponse)
  ))
_sym_db.RegisterMessage(ListTaskResponse)
_sym_db.RegisterMessage(ListTaskResponse.List)
_sym_db.RegisterMessage(ListTaskResponse.List.CmdConfig)
_sym_db.RegisterMessage(ListTaskResponse.List.Annotations)
_sym_db.RegisterMessage(ListTaskResponse.List.Callback)

ListTaskResponseWrapper = _reflection.GeneratedProtocolMessageType('ListTaskResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _LISTTASKRESPONSEWRAPPER,
  __module__ = 'list_task_pb2'
  # @@protoc_insertion_point(class_scope:task.ListTaskResponseWrapper)
  ))
_sym_db.RegisterMessage(ListTaskResponseWrapper)


# @@protoc_insertion_point(module_scope)
