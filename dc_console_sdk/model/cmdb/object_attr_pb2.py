# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_attr.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from dc_console_sdk.model.cmdb import object_attr_value_pb2 as dc__console__sdk_dot_model_dot_cmdb_dot_object__attr__value__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='object_attr.proto',
  package='cmdb',
  syntax='proto3',
  serialized_options=_b('Z>go.easyops.local/contracts/protorepo-models/easyops/model/cmdb'),
  serialized_pb=_b('\n\x11object_attr.proto\x12\x04\x63mdb\x1a\x31\x64\x63_console_sdk/model/cmdb/object_attr_value.proto\"\xff\x01\n\nObjectAttr\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tprotected\x18\x03 \x01(\x08\x12\x0e\n\x06\x63ustom\x18\x04 \x01(\t\x12\x10\n\x08readonly\x18\x05 \x01(\t\x12\x10\n\x08required\x18\x06 \x01(\t\x12\x0e\n\x06unique\x18\x07 \x01(\t\x12\x0b\n\x03tag\x18\x08 \x03(\t\x12$\n\x05value\x18\t \x01(\x0b\x32\x15.cmdb.ObjectAttrValue\x12\x17\n\x0fwordIndexDenied\x18\n \x01(\x08\x12\x13\n\x0b\x64\x65scription\x18\x0b \x01(\t\x12\x0c\n\x04tips\x18\x0c \x01(\t\x12\x11\n\tisInherit\x18\r \x01(\x08\x42@Z>go.easyops.local/contracts/protorepo-models/easyops/model/cmdbb\x06proto3')
  ,
  dependencies=[dc__console__sdk_dot_model_dot_cmdb_dot_object__attr__value__pb2.DESCRIPTOR,])




_OBJECTATTR = _descriptor.Descriptor(
  name='ObjectAttr',
  full_name='cmdb.ObjectAttr',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cmdb.ObjectAttr.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='cmdb.ObjectAttr.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='protected', full_name='cmdb.ObjectAttr.protected', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='custom', full_name='cmdb.ObjectAttr.custom', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readonly', full_name='cmdb.ObjectAttr.readonly', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='required', full_name='cmdb.ObjectAttr.required', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unique', full_name='cmdb.ObjectAttr.unique', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tag', full_name='cmdb.ObjectAttr.tag', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='cmdb.ObjectAttr.value', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wordIndexDenied', full_name='cmdb.ObjectAttr.wordIndexDenied', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='cmdb.ObjectAttr.description', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tips', full_name='cmdb.ObjectAttr.tips', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isInherit', full_name='cmdb.ObjectAttr.isInherit', index=12,
      number=13, type=8, cpp_type=7, label=1,
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
  serialized_start=79,
  serialized_end=334,
)

_OBJECTATTR.fields_by_name['value'].message_type = dc__console__sdk_dot_model_dot_cmdb_dot_object__attr__value__pb2._OBJECTATTRVALUE
DESCRIPTOR.message_types_by_name['ObjectAttr'] = _OBJECTATTR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ObjectAttr = _reflection.GeneratedProtocolMessageType('ObjectAttr', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTATTR,
  '__module__' : 'object_attr_pb2'
  # @@protoc_insertion_point(class_scope:cmdb.ObjectAttr)
  })
_sym_db.RegisterMessage(ObjectAttr)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
