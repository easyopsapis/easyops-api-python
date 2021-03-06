# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: create_task.proto

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
  name='create_task.proto',
  package='task',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11\x63reate_task.proto\x12\x04task\x1a\x1cgoogle/protobuf/struct.proto\"p\n\x12\x43reateTaskResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12+\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x1d.task.CreateTaskResponse.Data\x1a\x12\n\x04\x44\x61ta\x12\n\n\x02id\x18\x01 \x01(\t\"u\n\x19\x43reateTaskResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12&\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x18.task.CreateTaskResponseb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_CREATETASKRESPONSE_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='task.CreateTaskResponse.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='task.CreateTaskResponse.Data.id', index=0,
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
  serialized_start=151,
  serialized_end=169,
)

_CREATETASKRESPONSE = _descriptor.Descriptor(
  name='CreateTaskResponse',
  full_name='task.CreateTaskResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='task.CreateTaskResponse.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='task.CreateTaskResponse.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='task.CreateTaskResponse.data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CREATETASKRESPONSE_DATA, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=57,
  serialized_end=169,
)


_CREATETASKRESPONSEWRAPPER = _descriptor.Descriptor(
  name='CreateTaskResponseWrapper',
  full_name='task.CreateTaskResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='task.CreateTaskResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='task.CreateTaskResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='task.CreateTaskResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='task.CreateTaskResponseWrapper.data', index=3,
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
  serialized_start=171,
  serialized_end=288,
)

_CREATETASKRESPONSE_DATA.containing_type = _CREATETASKRESPONSE
_CREATETASKRESPONSE.fields_by_name['data'].message_type = _CREATETASKRESPONSE_DATA
_CREATETASKRESPONSEWRAPPER.fields_by_name['data'].message_type = _CREATETASKRESPONSE
DESCRIPTOR.message_types_by_name['CreateTaskResponse'] = _CREATETASKRESPONSE
DESCRIPTOR.message_types_by_name['CreateTaskResponseWrapper'] = _CREATETASKRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateTaskResponse = _reflection.GeneratedProtocolMessageType('CreateTaskResponse', (_message.Message,), {

  'Data' : _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), {
    'DESCRIPTOR' : _CREATETASKRESPONSE_DATA,
    '__module__' : 'create_task_pb2'
    # @@protoc_insertion_point(class_scope:task.CreateTaskResponse.Data)
    })
  ,
  'DESCRIPTOR' : _CREATETASKRESPONSE,
  '__module__' : 'create_task_pb2'
  # @@protoc_insertion_point(class_scope:task.CreateTaskResponse)
  })
_sym_db.RegisterMessage(CreateTaskResponse)
_sym_db.RegisterMessage(CreateTaskResponse.Data)

CreateTaskResponseWrapper = _reflection.GeneratedProtocolMessageType('CreateTaskResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _CREATETASKRESPONSEWRAPPER,
  '__module__' : 'create_task_pb2'
  # @@protoc_insertion_point(class_scope:task.CreateTaskResponseWrapper)
  })
_sym_db.RegisterMessage(CreateTaskResponseWrapper)


# @@protoc_insertion_point(module_scope)
