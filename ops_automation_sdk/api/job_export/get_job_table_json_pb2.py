# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_job_table_json.proto

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
  name='get_job_table_json.proto',
  package='job_export',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x18get_job_table_json.proto\x12\njob_export\x1a\x1cgoogle/protobuf/struct.proto\"+\n\x16GetJobTableJsonRequest\x12\x11\n\tjobTaskId\x18\x01 \x01(\t\"y\n\x1eGetJobTableJsonResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12%\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Structb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_GETJOBTABLEJSONREQUEST = _descriptor.Descriptor(
  name='GetJobTableJsonRequest',
  full_name='job_export.GetJobTableJsonRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='jobTaskId', full_name='job_export.GetJobTableJsonRequest.jobTaskId', index=0,
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
  serialized_start=70,
  serialized_end=113,
)


_GETJOBTABLEJSONRESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetJobTableJsonResponseWrapper',
  full_name='job_export.GetJobTableJsonResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='job_export.GetJobTableJsonResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='job_export.GetJobTableJsonResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='job_export.GetJobTableJsonResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='job_export.GetJobTableJsonResponseWrapper.data', index=3,
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
  serialized_start=115,
  serialized_end=236,
)

_GETJOBTABLEJSONRESPONSEWRAPPER.fields_by_name['data'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['GetJobTableJsonRequest'] = _GETJOBTABLEJSONREQUEST
DESCRIPTOR.message_types_by_name['GetJobTableJsonResponseWrapper'] = _GETJOBTABLEJSONRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetJobTableJsonRequest = _reflection.GeneratedProtocolMessageType('GetJobTableJsonRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETJOBTABLEJSONREQUEST,
  __module__ = 'get_job_table_json_pb2'
  # @@protoc_insertion_point(class_scope:job_export.GetJobTableJsonRequest)
  ))
_sym_db.RegisterMessage(GetJobTableJsonRequest)

GetJobTableJsonResponseWrapper = _reflection.GeneratedProtocolMessageType('GetJobTableJsonResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _GETJOBTABLEJSONRESPONSEWRAPPER,
  __module__ = 'get_job_table_json_pb2'
  # @@protoc_insertion_point(class_scope:job_export.GetJobTableJsonResponseWrapper)
  ))
_sym_db.RegisterMessage(GetJobTableJsonResponseWrapper)


# @@protoc_insertion_point(module_scope)
