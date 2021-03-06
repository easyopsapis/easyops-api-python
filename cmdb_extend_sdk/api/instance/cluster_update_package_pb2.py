# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cluster_update_package.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cluster_update_package.proto',
  package='instance',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1c\x63luster_update_package.proto\x12\x08instance\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1bgoogle/protobuf/empty.proto\"[\n\x1b\x43lusterUpdatePackageRequest\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12(\n\x07package\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\"}\n#ClusterUpdatePackageResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12$\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x16.google.protobuf.Emptyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_CLUSTERUPDATEPACKAGEREQUEST = _descriptor.Descriptor(
  name='ClusterUpdatePackageRequest',
  full_name='instance.ClusterUpdatePackageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='instance.ClusterUpdatePackageRequest.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='package', full_name='instance.ClusterUpdatePackageRequest.package', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=101,
  serialized_end=192,
)


_CLUSTERUPDATEPACKAGERESPONSEWRAPPER = _descriptor.Descriptor(
  name='ClusterUpdatePackageResponseWrapper',
  full_name='instance.ClusterUpdatePackageResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='instance.ClusterUpdatePackageResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='instance.ClusterUpdatePackageResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='instance.ClusterUpdatePackageResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='instance.ClusterUpdatePackageResponseWrapper.data', index=3,
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
  serialized_start=194,
  serialized_end=319,
)

_CLUSTERUPDATEPACKAGEREQUEST.fields_by_name['package'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_CLUSTERUPDATEPACKAGERESPONSEWRAPPER.fields_by_name['data'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
DESCRIPTOR.message_types_by_name['ClusterUpdatePackageRequest'] = _CLUSTERUPDATEPACKAGEREQUEST
DESCRIPTOR.message_types_by_name['ClusterUpdatePackageResponseWrapper'] = _CLUSTERUPDATEPACKAGERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClusterUpdatePackageRequest = _reflection.GeneratedProtocolMessageType('ClusterUpdatePackageRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLUSTERUPDATEPACKAGEREQUEST,
  '__module__' : 'cluster_update_package_pb2'
  # @@protoc_insertion_point(class_scope:instance.ClusterUpdatePackageRequest)
  })
_sym_db.RegisterMessage(ClusterUpdatePackageRequest)

ClusterUpdatePackageResponseWrapper = _reflection.GeneratedProtocolMessageType('ClusterUpdatePackageResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _CLUSTERUPDATEPACKAGERESPONSEWRAPPER,
  '__module__' : 'cluster_update_package_pb2'
  # @@protoc_insertion_point(class_scope:instance.ClusterUpdatePackageResponseWrapper)
  })
_sym_db.RegisterMessage(ClusterUpdatePackageResponseWrapper)


# @@protoc_insertion_point(module_scope)
