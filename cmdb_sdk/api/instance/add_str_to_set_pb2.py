# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: add_str_to_set.proto

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
  name='add_str_to_set.proto',
  package='instance',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14\x61\x64\x64_str_to_set.proto\x12\x08instance\x1a\x1cgoogle/protobuf/struct.proto\"o\n\x12\x41\x64\x64StrToSetRequest\x12\x10\n\x08objectId\x18\x01 \x01(\t\x12\x0f\n\x07\x61ttr_id\x18\x02 \x01(\t\x12&\n\x05query\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0e\n\x06values\x18\x04 \x03(\t\"9\n\x13\x41\x64\x64StrToSetResponse\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0e\n\x06values\x18\x02 \x03(\t\"{\n\x1a\x41\x64\x64StrToSetResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12+\n\x04\x64\x61ta\x18\x04 \x03(\x0b\x32\x1d.instance.AddStrToSetResponseb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_ADDSTRTOSETREQUEST = _descriptor.Descriptor(
  name='AddStrToSetRequest',
  full_name='instance.AddStrToSetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='objectId', full_name='instance.AddStrToSetRequest.objectId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attr_id', full_name='instance.AddStrToSetRequest.attr_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='query', full_name='instance.AddStrToSetRequest.query', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='values', full_name='instance.AddStrToSetRequest.values', index=3,
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
  serialized_start=64,
  serialized_end=175,
)


_ADDSTRTOSETRESPONSE = _descriptor.Descriptor(
  name='AddStrToSetResponse',
  full_name='instance.AddStrToSetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='instance.AddStrToSetResponse.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='values', full_name='instance.AddStrToSetResponse.values', index=1,
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
  serialized_start=177,
  serialized_end=234,
)


_ADDSTRTOSETRESPONSEWRAPPER = _descriptor.Descriptor(
  name='AddStrToSetResponseWrapper',
  full_name='instance.AddStrToSetResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='instance.AddStrToSetResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='instance.AddStrToSetResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='instance.AddStrToSetResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='instance.AddStrToSetResponseWrapper.data', index=3,
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
  serialized_start=236,
  serialized_end=359,
)

_ADDSTRTOSETREQUEST.fields_by_name['query'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_ADDSTRTOSETRESPONSEWRAPPER.fields_by_name['data'].message_type = _ADDSTRTOSETRESPONSE
DESCRIPTOR.message_types_by_name['AddStrToSetRequest'] = _ADDSTRTOSETREQUEST
DESCRIPTOR.message_types_by_name['AddStrToSetResponse'] = _ADDSTRTOSETRESPONSE
DESCRIPTOR.message_types_by_name['AddStrToSetResponseWrapper'] = _ADDSTRTOSETRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AddStrToSetRequest = _reflection.GeneratedProtocolMessageType('AddStrToSetRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDSTRTOSETREQUEST,
  '__module__' : 'add_str_to_set_pb2'
  # @@protoc_insertion_point(class_scope:instance.AddStrToSetRequest)
  })
_sym_db.RegisterMessage(AddStrToSetRequest)

AddStrToSetResponse = _reflection.GeneratedProtocolMessageType('AddStrToSetResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDSTRTOSETRESPONSE,
  '__module__' : 'add_str_to_set_pb2'
  # @@protoc_insertion_point(class_scope:instance.AddStrToSetResponse)
  })
_sym_db.RegisterMessage(AddStrToSetResponse)

AddStrToSetResponseWrapper = _reflection.GeneratedProtocolMessageType('AddStrToSetResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _ADDSTRTOSETRESPONSEWRAPPER,
  '__module__' : 'add_str_to_set_pb2'
  # @@protoc_insertion_point(class_scope:instance.AddStrToSetResponseWrapper)
  })
_sym_db.RegisterMessage(AddStrToSetResponseWrapper)


# @@protoc_insertion_point(module_scope)
