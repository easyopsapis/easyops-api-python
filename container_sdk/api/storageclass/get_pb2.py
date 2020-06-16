# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from container_sdk.model.container import cluster_pb2 as container__sdk_dot_model_dot_container_dot_cluster__pb2
from container_sdk.model.container import storage_class_pb2 as container__sdk_dot_model_dot_container_dot_storage__class__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='get.proto',
  package='storageclass',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\tget.proto\x12\x0cstorageclass\x1a+container_sdk/model/container/cluster.proto\x1a\x31\x63ontainer_sdk/model/container/storage_class.proto\" \n\nGetRequest\x12\x12\n\ninstanceId\x18\x01 \x01(\t\"a\n\x0bGetResponse\x12#\n\x07\x63luster\x18\x01 \x01(\x0b\x32\x12.container.Cluster\x12-\n\x0cstorageClass\x18\x02 \x01(\x0b\x32\x17.container.StorageClass\"o\n\x12GetResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\'\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x19.storageclass.GetResponseb\x06proto3')
  ,
  dependencies=[container__sdk_dot_model_dot_container_dot_cluster__pb2.DESCRIPTOR,container__sdk_dot_model_dot_container_dot_storage__class__pb2.DESCRIPTOR,])




_GETREQUEST = _descriptor.Descriptor(
  name='GetRequest',
  full_name='storageclass.GetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='storageclass.GetRequest.instanceId', index=0,
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
  serialized_start=123,
  serialized_end=155,
)


_GETRESPONSE = _descriptor.Descriptor(
  name='GetResponse',
  full_name='storageclass.GetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster', full_name='storageclass.GetResponse.cluster', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='storageClass', full_name='storageclass.GetResponse.storageClass', index=1,
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
  serialized_start=157,
  serialized_end=254,
)


_GETRESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetResponseWrapper',
  full_name='storageclass.GetResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='storageclass.GetResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='storageclass.GetResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='storageclass.GetResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='storageclass.GetResponseWrapper.data', index=3,
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
  serialized_start=256,
  serialized_end=367,
)

_GETRESPONSE.fields_by_name['cluster'].message_type = container__sdk_dot_model_dot_container_dot_cluster__pb2._CLUSTER
_GETRESPONSE.fields_by_name['storageClass'].message_type = container__sdk_dot_model_dot_container_dot_storage__class__pb2._STORAGECLASS
_GETRESPONSEWRAPPER.fields_by_name['data'].message_type = _GETRESPONSE
DESCRIPTOR.message_types_by_name['GetRequest'] = _GETREQUEST
DESCRIPTOR.message_types_by_name['GetResponse'] = _GETRESPONSE
DESCRIPTOR.message_types_by_name['GetResponseWrapper'] = _GETRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetRequest = _reflection.GeneratedProtocolMessageType('GetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETREQUEST,
  '__module__' : 'get_pb2'
  # @@protoc_insertion_point(class_scope:storageclass.GetRequest)
  })
_sym_db.RegisterMessage(GetRequest)

GetResponse = _reflection.GeneratedProtocolMessageType('GetResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETRESPONSE,
  '__module__' : 'get_pb2'
  # @@protoc_insertion_point(class_scope:storageclass.GetResponse)
  })
_sym_db.RegisterMessage(GetResponse)

GetResponseWrapper = _reflection.GeneratedProtocolMessageType('GetResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _GETRESPONSEWRAPPER,
  '__module__' : 'get_pb2'
  # @@protoc_insertion_point(class_scope:storageclass.GetResponseWrapper)
  })
_sym_db.RegisterMessage(GetResponseWrapper)


# @@protoc_insertion_point(module_scope)
