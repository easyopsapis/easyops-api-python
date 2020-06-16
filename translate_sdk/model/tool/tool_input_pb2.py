# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tool_input.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tool_input.proto',
  package='tool',
  syntax='proto3',
  serialized_options=_b('Z>go.easyops.local/contracts/protorepo-models/easyops/model/tool'),
  serialized_pb=_b('\n\x10tool_input.proto\x12\x04tool\"\xe2\x02\n\tToolInput\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ncmdbAttrId\x18\x02 \x01(\t\x12\x14\n\x0c\x63mdbObjectId\x18\x03 \x01(\t\x12\x14\n\x0c\x63mdbAttrType\x18\x04 \x01(\t\x12\x0f\n\x07\x63\x61scade\x18\x05 \x01(\x08\x12\r\n\x05label\x18\x06 \x01(\t\x12\x10\n\x08multiple\x18\x07 \x01(\x08\x12\x10\n\x08required\x18\x08 \x01(\x08\x12\x0c\n\x04type\x18\t \x01(\t\x12\x0c\n\x04\x65num\x18\n \x03(\t\x12\x11\n\tprimitive\x18\x0b \x01(\x08\x12\x0c\n\x04memo\x18\x0c \x01(\t\x12\"\n\x04path\x18\r \x03(\x0b\x32\x14.tool.ToolInput.Path\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x0e \x01(\t\x12\x0e\n\x06source\x18\x0f \x01(\t\x12\x10\n\x08selector\x18\x10 \x01(\t\x12\r\n\x05value\x18\x11 \x01(\t\x1a \n\x04Path\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\tB@Z>go.easyops.local/contracts/protorepo-models/easyops/model/toolb\x06proto3')
)




_TOOLINPUT_PATH = _descriptor.Descriptor(
  name='Path',
  full_name='tool.ToolInput.Path',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tool.ToolInput.Path.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='tool.ToolInput.Path.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=349,
  serialized_end=381,
)

_TOOLINPUT = _descriptor.Descriptor(
  name='ToolInput',
  full_name='tool.ToolInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tool.ToolInput.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cmdbAttrId', full_name='tool.ToolInput.cmdbAttrId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cmdbObjectId', full_name='tool.ToolInput.cmdbObjectId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cmdbAttrType', full_name='tool.ToolInput.cmdbAttrType', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cascade', full_name='tool.ToolInput.cascade', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='label', full_name='tool.ToolInput.label', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='multiple', full_name='tool.ToolInput.multiple', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='required', full_name='tool.ToolInput.required', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='tool.ToolInput.type', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enum', full_name='tool.ToolInput.enum', index=9,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='primitive', full_name='tool.ToolInput.primitive', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='tool.ToolInput.memo', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='tool.ToolInput.path', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default', full_name='tool.ToolInput.default', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='tool.ToolInput.source', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='selector', full_name='tool.ToolInput.selector', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='tool.ToolInput.value', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TOOLINPUT_PATH, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=381,
)

_TOOLINPUT_PATH.containing_type = _TOOLINPUT
_TOOLINPUT.fields_by_name['path'].message_type = _TOOLINPUT_PATH
DESCRIPTOR.message_types_by_name['ToolInput'] = _TOOLINPUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ToolInput = _reflection.GeneratedProtocolMessageType('ToolInput', (_message.Message,), {

  'Path' : _reflection.GeneratedProtocolMessageType('Path', (_message.Message,), {
    'DESCRIPTOR' : _TOOLINPUT_PATH,
    '__module__' : 'tool_input_pb2'
    # @@protoc_insertion_point(class_scope:tool.ToolInput.Path)
    })
  ,
  'DESCRIPTOR' : _TOOLINPUT,
  '__module__' : 'tool_input_pb2'
  # @@protoc_insertion_point(class_scope:tool.ToolInput)
  })
_sym_db.RegisterMessage(ToolInput)
_sym_db.RegisterMessage(ToolInput.Path)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
