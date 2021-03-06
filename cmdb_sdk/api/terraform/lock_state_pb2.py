# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lock_state.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cmdb_sdk.model.cmdb import tf_lock_info_pb2 as cmdb__sdk_dot_model_dot_cmdb_dot_tf__lock__info__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='lock_state.proto',
  package='terraform',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10lock_state.proto\x12\tterraform\x1a&cmdb_sdk/model/cmdb/tf_lock_info.proto\x1a\x1bgoogle/protobuf/empty.proto\"s\n\x10LockStateRequest\x12\x10\n\x08objectId\x18\x01 \x01(\t\x12\x12\n\ninstanceId\x18\x02 \x01(\t\x12\x0b\n\x03org\x18\x03 \x01(\x05\x12\x0c\n\x04user\x18\x04 \x01(\t\x12\x1e\n\x04\x62ody\x18\x05 \x01(\x0b\x32\x10.cmdb.TFLockInfo\"r\n\x18LockStateResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12$\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x16.google.protobuf.Emptyb\x06proto3')
  ,
  dependencies=[cmdb__sdk_dot_model_dot_cmdb_dot_tf__lock__info__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_LOCKSTATEREQUEST = _descriptor.Descriptor(
  name='LockStateRequest',
  full_name='terraform.LockStateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='objectId', full_name='terraform.LockStateRequest.objectId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='terraform.LockStateRequest.instanceId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org', full_name='terraform.LockStateRequest.org', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='terraform.LockStateRequest.user', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='body', full_name='terraform.LockStateRequest.body', index=4,
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
  serialized_start=100,
  serialized_end=215,
)


_LOCKSTATERESPONSEWRAPPER = _descriptor.Descriptor(
  name='LockStateResponseWrapper',
  full_name='terraform.LockStateResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='terraform.LockStateResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='terraform.LockStateResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='terraform.LockStateResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='terraform.LockStateResponseWrapper.data', index=3,
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
  serialized_start=217,
  serialized_end=331,
)

_LOCKSTATEREQUEST.fields_by_name['body'].message_type = cmdb__sdk_dot_model_dot_cmdb_dot_tf__lock__info__pb2._TFLOCKINFO
_LOCKSTATERESPONSEWRAPPER.fields_by_name['data'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
DESCRIPTOR.message_types_by_name['LockStateRequest'] = _LOCKSTATEREQUEST
DESCRIPTOR.message_types_by_name['LockStateResponseWrapper'] = _LOCKSTATERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LockStateRequest = _reflection.GeneratedProtocolMessageType('LockStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOCKSTATEREQUEST,
  '__module__' : 'lock_state_pb2'
  # @@protoc_insertion_point(class_scope:terraform.LockStateRequest)
  })
_sym_db.RegisterMessage(LockStateRequest)

LockStateResponseWrapper = _reflection.GeneratedProtocolMessageType('LockStateResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _LOCKSTATERESPONSEWRAPPER,
  '__module__' : 'lock_state_pb2'
  # @@protoc_insertion_point(class_scope:terraform.LockStateResponseWrapper)
  })
_sym_db.RegisterMessage(LockStateResponseWrapper)


# @@protoc_insertion_point(module_scope)
