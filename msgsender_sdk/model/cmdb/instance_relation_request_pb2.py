# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: instance_relation_request.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='instance_relation_request.proto',
  package='cmdb',
  syntax='proto3',
  serialized_options=_b('Z>go.easyops.local/contracts/protorepo-models/easyops/model/cmdb'),
  serialized_pb=_b('\n\x1finstance_relation_request.proto\x12\x04\x63mdb\"M\n\x17InstanceRelationRequest\x12\x14\n\x0cinstance_ids\x18\x01 \x03(\t\x12\x1c\n\x14related_instance_ids\x18\x02 \x03(\tB@Z>go.easyops.local/contracts/protorepo-models/easyops/model/cmdbb\x06proto3')
)




_INSTANCERELATIONREQUEST = _descriptor.Descriptor(
  name='InstanceRelationRequest',
  full_name='cmdb.InstanceRelationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance_ids', full_name='cmdb.InstanceRelationRequest.instance_ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='related_instance_ids', full_name='cmdb.InstanceRelationRequest.related_instance_ids', index=1,
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
  serialized_start=41,
  serialized_end=118,
)

DESCRIPTOR.message_types_by_name['InstanceRelationRequest'] = _INSTANCERELATIONREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InstanceRelationRequest = _reflection.GeneratedProtocolMessageType('InstanceRelationRequest', (_message.Message,), dict(
  DESCRIPTOR = _INSTANCERELATIONREQUEST,
  __module__ = 'instance_relation_request_pb2'
  # @@protoc_insertion_point(class_scope:cmdb.InstanceRelationRequest)
  ))
_sym_db.RegisterMessage(InstanceRelationRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
