# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_relation_group.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='object_relation_group.proto',
  package='cmdb',
  syntax='proto3',
  serialized_options=_b('Z>go.easyops.local/contracts/protorepo-models/easyops/model/cmdb'),
  serialized_pb=_b('\n\x1bobject_relation_group.proto\x12\x04\x63mdb\"B\n\x13ObjectRelationGroup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tprotected\x18\x03 \x01(\x08\x42@Z>go.easyops.local/contracts/protorepo-models/easyops/model/cmdbb\x06proto3')
)




_OBJECTRELATIONGROUP = _descriptor.Descriptor(
  name='ObjectRelationGroup',
  full_name='cmdb.ObjectRelationGroup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cmdb.ObjectRelationGroup.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='cmdb.ObjectRelationGroup.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='protected', full_name='cmdb.ObjectRelationGroup.protected', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=37,
  serialized_end=103,
)

DESCRIPTOR.message_types_by_name['ObjectRelationGroup'] = _OBJECTRELATIONGROUP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ObjectRelationGroup = _reflection.GeneratedProtocolMessageType('ObjectRelationGroup', (_message.Message,), dict(
  DESCRIPTOR = _OBJECTRELATIONGROUP,
  __module__ = 'object_relation_group_pb2'
  # @@protoc_insertion_point(class_scope:cmdb.ObjectRelationGroup)
  ))
_sym_db.RegisterMessage(ObjectRelationGroup)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
