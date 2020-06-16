# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: add_str_to_array.proto

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
  name='add_str_to_array.proto',
  package='instance',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16\x61\x64\x64_str_to_array.proto\x12\x08instance\x1a\x1cgoogle/protobuf/struct.proto\"q\n\x14\x41\x64\x64StrToArrayRequest\x12\x10\n\x08objectId\x18\x01 \x01(\t\x12\x0f\n\x07\x61ttr_id\x18\x02 \x01(\t\x12&\n\x05query\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0e\n\x06values\x18\x04 \x03(\t\";\n\x15\x41\x64\x64StrToArrayResponse\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0e\n\x06values\x18\x02 \x03(\t\"\x7f\n\x1c\x41\x64\x64StrToArrayResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12-\n\x04\x64\x61ta\x18\x04 \x03(\x0b\x32\x1f.instance.AddStrToArrayResponseb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_ADDSTRTOARRAYREQUEST = _descriptor.Descriptor(
  name='AddStrToArrayRequest',
  full_name='instance.AddStrToArrayRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='objectId', full_name='instance.AddStrToArrayRequest.objectId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attr_id', full_name='instance.AddStrToArrayRequest.attr_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='query', full_name='instance.AddStrToArrayRequest.query', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='values', full_name='instance.AddStrToArrayRequest.values', index=3,
      number=4, type=9, cpp_type=9, label=3,
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
  serialized_start=66,
  serialized_end=179,
)


_ADDSTRTOARRAYRESPONSE = _descriptor.Descriptor(
  name='AddStrToArrayResponse',
  full_name='instance.AddStrToArrayResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='instance.AddStrToArrayResponse.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='values', full_name='instance.AddStrToArrayResponse.values', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=181,
  serialized_end=240,
)


_ADDSTRTOARRAYRESPONSEWRAPPER = _descriptor.Descriptor(
  name='AddStrToArrayResponseWrapper',
  full_name='instance.AddStrToArrayResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='instance.AddStrToArrayResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='instance.AddStrToArrayResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='instance.AddStrToArrayResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='instance.AddStrToArrayResponseWrapper.data', index=3,
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
  serialized_start=242,
  serialized_end=369,
)

_ADDSTRTOARRAYREQUEST.fields_by_name['query'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_ADDSTRTOARRAYRESPONSEWRAPPER.fields_by_name['data'].message_type = _ADDSTRTOARRAYRESPONSE
DESCRIPTOR.message_types_by_name['AddStrToArrayRequest'] = _ADDSTRTOARRAYREQUEST
DESCRIPTOR.message_types_by_name['AddStrToArrayResponse'] = _ADDSTRTOARRAYRESPONSE
DESCRIPTOR.message_types_by_name['AddStrToArrayResponseWrapper'] = _ADDSTRTOARRAYRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AddStrToArrayRequest = _reflection.GeneratedProtocolMessageType('AddStrToArrayRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDSTRTOARRAYREQUEST,
  '__module__' : 'add_str_to_array_pb2'
  # @@protoc_insertion_point(class_scope:instance.AddStrToArrayRequest)
  })
_sym_db.RegisterMessage(AddStrToArrayRequest)

AddStrToArrayResponse = _reflection.GeneratedProtocolMessageType('AddStrToArrayResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDSTRTOARRAYRESPONSE,
  '__module__' : 'add_str_to_array_pb2'
  # @@protoc_insertion_point(class_scope:instance.AddStrToArrayResponse)
  })
_sym_db.RegisterMessage(AddStrToArrayResponse)

AddStrToArrayResponseWrapper = _reflection.GeneratedProtocolMessageType('AddStrToArrayResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _ADDSTRTOARRAYRESPONSEWRAPPER,
  '__module__' : 'add_str_to_array_pb2'
  # @@protoc_insertion_point(class_scope:instance.AddStrToArrayResponseWrapper)
  })
_sym_db.RegisterMessage(AddStrToArrayResponseWrapper)


# @@protoc_insertion_point(module_scope)
