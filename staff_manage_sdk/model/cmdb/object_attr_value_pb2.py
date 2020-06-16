# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_attr_value.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from staff_manage_sdk.model.cmdb import object_attr_value_struct_pb2 as staff__manage__sdk_dot_model_dot_cmdb_dot_object__attr__value__struct__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='object_attr_value.proto',
  package='cmdb',
  syntax='proto3',
  serialized_options=_b('Z>go.easyops.local/contracts/protorepo-models/easyops/model/cmdb'),
  serialized_pb=_b('\n\x17object_attr_value.proto\x12\x04\x63mdb\x1a:staff_manage_sdk/model/cmdb/object_attr_value_struct.proto\x1a\x1cgoogle/protobuf/struct.proto\"\x8a\x02\n\x0fObjectAttrValue\x12\x0c\n\x04type\x18\x01 \x01(\t\x12%\n\x05regex\x18\x02 \x01(\x0b\x32\x16.google.protobuf.Value\x12\x14\n\x0c\x64\x65\x66\x61ult_type\x18\x03 \x01(\t\x12\'\n\x07\x64\x65\x66\x61ult\x18\x04 \x01(\x0b\x32\x16.google.protobuf.Value\x12\x32\n\rstruct_define\x18\x05 \x03(\x0b\x32\x1b.cmdb.ObjectAttrValueStruct\x12\x0c\n\x04mode\x18\x06 \x01(\t\x12\x0e\n\x06prefix\x18\x07 \x01(\t\x12\x13\n\x0bstart_value\x18\x08 \x01(\x05\x12\x1c\n\x14series_number_length\x18\t \x01(\x05\x42@Z>go.easyops.local/contracts/protorepo-models/easyops/model/cmdbb\x06proto3')
  ,
  dependencies=[staff__manage__sdk_dot_model_dot_cmdb_dot_object__attr__value__struct__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_OBJECTATTRVALUE = _descriptor.Descriptor(
  name='ObjectAttrValue',
  full_name='cmdb.ObjectAttrValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='cmdb.ObjectAttrValue.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='regex', full_name='cmdb.ObjectAttrValue.regex', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default_type', full_name='cmdb.ObjectAttrValue.default_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default', full_name='cmdb.ObjectAttrValue.default', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='struct_define', full_name='cmdb.ObjectAttrValue.struct_define', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mode', full_name='cmdb.ObjectAttrValue.mode', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prefix', full_name='cmdb.ObjectAttrValue.prefix', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_value', full_name='cmdb.ObjectAttrValue.start_value', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='series_number_length', full_name='cmdb.ObjectAttrValue.series_number_length', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=124,
  serialized_end=390,
)

_OBJECTATTRVALUE.fields_by_name['regex'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_OBJECTATTRVALUE.fields_by_name['default'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_OBJECTATTRVALUE.fields_by_name['struct_define'].message_type = staff__manage__sdk_dot_model_dot_cmdb_dot_object__attr__value__struct__pb2._OBJECTATTRVALUESTRUCT
DESCRIPTOR.message_types_by_name['ObjectAttrValue'] = _OBJECTATTRVALUE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ObjectAttrValue = _reflection.GeneratedProtocolMessageType('ObjectAttrValue', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTATTRVALUE,
  '__module__' : 'object_attr_value_pb2'
  # @@protoc_insertion_point(class_scope:cmdb.ObjectAttrValue)
  })
_sym_db.RegisterMessage(ObjectAttrValue)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
