# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_instances.proto

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
  name='get_instances.proto',
  package='instance',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13get_instances.proto\x12\x08instance\x1a\x1cgoogle/protobuf/struct.proto\"\x84\x01\n\x13GetInstancesRequest\x12\x10\n\x08objectId\x18\x01 \x01(\t\x12\x13\n\x0binstanceIds\x18\x02 \x01(\t\x12\x0c\n\x04page\x18\x03 \x01(\x05\x12\x10\n\x08pageSize\x18\x04 \x01(\x05\x12&\n\x05query\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\"l\n\x14GetInstancesResponse\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x10\n\x08pageSize\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12%\n\x04list\x18\x04 \x03(\x0b\x32\x17.google.protobuf.Struct\"}\n\x1bGetInstancesResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12,\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1e.instance.GetInstancesResponseb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_GETINSTANCESREQUEST = _descriptor.Descriptor(
  name='GetInstancesRequest',
  full_name='instance.GetInstancesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='objectId', full_name='instance.GetInstancesRequest.objectId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceIds', full_name='instance.GetInstancesRequest.instanceIds', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page', full_name='instance.GetInstancesRequest.page', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='instance.GetInstancesRequest.pageSize', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='query', full_name='instance.GetInstancesRequest.query', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=64,
  serialized_end=196,
)


_GETINSTANCESRESPONSE = _descriptor.Descriptor(
  name='GetInstancesResponse',
  full_name='instance.GetInstancesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='instance.GetInstancesResponse.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='instance.GetInstancesResponse.pageSize', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='instance.GetInstancesResponse.total', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='instance.GetInstancesResponse.list', index=3,
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
  serialized_start=198,
  serialized_end=306,
)


_GETINSTANCESRESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetInstancesResponseWrapper',
  full_name='instance.GetInstancesResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='instance.GetInstancesResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='instance.GetInstancesResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='instance.GetInstancesResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='instance.GetInstancesResponseWrapper.data', index=3,
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
  serialized_start=308,
  serialized_end=433,
)

_GETINSTANCESREQUEST.fields_by_name['query'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_GETINSTANCESRESPONSE.fields_by_name['list'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_GETINSTANCESRESPONSEWRAPPER.fields_by_name['data'].message_type = _GETINSTANCESRESPONSE
DESCRIPTOR.message_types_by_name['GetInstancesRequest'] = _GETINSTANCESREQUEST
DESCRIPTOR.message_types_by_name['GetInstancesResponse'] = _GETINSTANCESRESPONSE
DESCRIPTOR.message_types_by_name['GetInstancesResponseWrapper'] = _GETINSTANCESRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetInstancesRequest = _reflection.GeneratedProtocolMessageType('GetInstancesRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETINSTANCESREQUEST,
  __module__ = 'get_instances_pb2'
  # @@protoc_insertion_point(class_scope:instance.GetInstancesRequest)
  ))
_sym_db.RegisterMessage(GetInstancesRequest)

GetInstancesResponse = _reflection.GeneratedProtocolMessageType('GetInstancesResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETINSTANCESRESPONSE,
  __module__ = 'get_instances_pb2'
  # @@protoc_insertion_point(class_scope:instance.GetInstancesResponse)
  ))
_sym_db.RegisterMessage(GetInstancesResponse)

GetInstancesResponseWrapper = _reflection.GeneratedProtocolMessageType('GetInstancesResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _GETINSTANCESRESPONSEWRAPPER,
  __module__ = 'get_instances_pb2'
  # @@protoc_insertion_point(class_scope:instance.GetInstancesResponseWrapper)
  ))
_sym_db.RegisterMessage(GetInstancesResponseWrapper)


# @@protoc_insertion_point(module_scope)