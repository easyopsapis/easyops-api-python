# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_attr_value_struct.proto

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
  name='object_attr_value_struct.proto',
  package='cmdb',
  syntax='proto3',
  serialized_options=_b('Z>go.easyops.local/contracts/protorepo-models/easyops/model/cmdb'),
  serialized_pb=_b('\n\x1eobject_attr_value_struct.proto\x12\x04\x63mdb\x1a\x1cgoogle/protobuf/struct.proto\"y\n\x15ObjectAttrValueStruct\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12%\n\x05regex\x18\x04 \x01(\x0b\x32\x16.google.protobuf.Value\x12\x11\n\tprotected\x18\x05 \x01(\x08\x42@Z>go.easyops.local/contracts/protorepo-models/easyops/model/cmdbb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_OBJECTATTRVALUESTRUCT = _descriptor.Descriptor(
  name='ObjectAttrValueStruct',
  full_name='cmdb.ObjectAttrValueStruct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cmdb.ObjectAttrValueStruct.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='cmdb.ObjectAttrValueStruct.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='cmdb.ObjectAttrValueStruct.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='regex', full_name='cmdb.ObjectAttrValueStruct.regex', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='protected', full_name='cmdb.ObjectAttrValueStruct.protected', index=4,
      number=5, type=8, cpp_type=7, label=1,
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
  serialized_start=70,
  serialized_end=191,
)

_OBJECTATTRVALUESTRUCT.fields_by_name['regex'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
DESCRIPTOR.message_types_by_name['ObjectAttrValueStruct'] = _OBJECTATTRVALUESTRUCT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ObjectAttrValueStruct = _reflection.GeneratedProtocolMessageType('ObjectAttrValueStruct', (_message.Message,), dict(
  DESCRIPTOR = _OBJECTATTRVALUESTRUCT,
  __module__ = 'object_attr_value_struct_pb2'
  # @@protoc_insertion_point(class_scope:cmdb.ObjectAttrValueStruct)
  ))
_sym_db.RegisterMessage(ObjectAttrValueStruct)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)