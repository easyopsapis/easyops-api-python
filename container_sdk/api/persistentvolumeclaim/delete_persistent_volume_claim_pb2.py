# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: delete_persistent_volume_claim.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='delete_persistent_volume_claim.proto',
  package='persistentvolumeclaim',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n$delete_persistent_volume_claim.proto\x12\x15persistentvolumeclaim\x1a\x1bgoogle/protobuf/empty.proto\"9\n#DeletePersistentVolumeClaimsRequest\x12\x12\n\ninstanceId\x18\x01 \x01(\t\"\x85\x01\n+DeletePersistentVolumeClaimsResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12$\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x16.google.protobuf.Emptyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_DELETEPERSISTENTVOLUMECLAIMSREQUEST = _descriptor.Descriptor(
  name='DeletePersistentVolumeClaimsRequest',
  full_name='persistentvolumeclaim.DeletePersistentVolumeClaimsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='persistentvolumeclaim.DeletePersistentVolumeClaimsRequest.instanceId', index=0,
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
  serialized_start=92,
  serialized_end=149,
)


_DELETEPERSISTENTVOLUMECLAIMSRESPONSEWRAPPER = _descriptor.Descriptor(
  name='DeletePersistentVolumeClaimsResponseWrapper',
  full_name='persistentvolumeclaim.DeletePersistentVolumeClaimsResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='persistentvolumeclaim.DeletePersistentVolumeClaimsResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='persistentvolumeclaim.DeletePersistentVolumeClaimsResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='persistentvolumeclaim.DeletePersistentVolumeClaimsResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='persistentvolumeclaim.DeletePersistentVolumeClaimsResponseWrapper.data', index=3,
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
  serialized_start=152,
  serialized_end=285,
)

_DELETEPERSISTENTVOLUMECLAIMSRESPONSEWRAPPER.fields_by_name['data'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
DESCRIPTOR.message_types_by_name['DeletePersistentVolumeClaimsRequest'] = _DELETEPERSISTENTVOLUMECLAIMSREQUEST
DESCRIPTOR.message_types_by_name['DeletePersistentVolumeClaimsResponseWrapper'] = _DELETEPERSISTENTVOLUMECLAIMSRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeletePersistentVolumeClaimsRequest = _reflection.GeneratedProtocolMessageType('DeletePersistentVolumeClaimsRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEPERSISTENTVOLUMECLAIMSREQUEST,
  '__module__' : 'delete_persistent_volume_claim_pb2'
  # @@protoc_insertion_point(class_scope:persistentvolumeclaim.DeletePersistentVolumeClaimsRequest)
  })
_sym_db.RegisterMessage(DeletePersistentVolumeClaimsRequest)

DeletePersistentVolumeClaimsResponseWrapper = _reflection.GeneratedProtocolMessageType('DeletePersistentVolumeClaimsResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _DELETEPERSISTENTVOLUMECLAIMSRESPONSEWRAPPER,
  '__module__' : 'delete_persistent_volume_claim_pb2'
  # @@protoc_insertion_point(class_scope:persistentvolumeclaim.DeletePersistentVolumeClaimsResponseWrapper)
  })
_sym_db.RegisterMessage(DeletePersistentVolumeClaimsResponseWrapper)


# @@protoc_insertion_point(module_scope)
