# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: create_tool.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from model.tool import input_param_pb2 as model_dot_tool_dot_input__param__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='create_tool.proto',
  package='basic',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11\x63reate_tool.proto\x12\x05\x62\x61sic\x1a\x1cmodel/tool/input_param.proto\"B\n\x12\x43reateToolResponse\x12\x0e\n\x06toolId\x18\x01 \x01(\t\x12\x0b\n\x03vId\x18\x02 \x01(\t\x12\x0f\n\x07\x64isable\x18\x03 \x01(\t\"v\n\x19\x43reateToolResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\'\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x19.basic.CreateToolResponseb\x06proto3')
  ,
  dependencies=[model_dot_tool_dot_input__param__pb2.DESCRIPTOR,])




_CREATETOOLRESPONSE = _descriptor.Descriptor(
  name='CreateToolResponse',
  full_name='basic.CreateToolResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='toolId', full_name='basic.CreateToolResponse.toolId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vId', full_name='basic.CreateToolResponse.vId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disable', full_name='basic.CreateToolResponse.disable', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=58,
  serialized_end=124,
)


_CREATETOOLRESPONSEWRAPPER = _descriptor.Descriptor(
  name='CreateToolResponseWrapper',
  full_name='basic.CreateToolResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='basic.CreateToolResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='basic.CreateToolResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='basic.CreateToolResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='basic.CreateToolResponseWrapper.data', index=3,
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
  serialized_start=126,
  serialized_end=244,
)

_CREATETOOLRESPONSEWRAPPER.fields_by_name['data'].message_type = _CREATETOOLRESPONSE
DESCRIPTOR.message_types_by_name['CreateToolResponse'] = _CREATETOOLRESPONSE
DESCRIPTOR.message_types_by_name['CreateToolResponseWrapper'] = _CREATETOOLRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateToolResponse = _reflection.GeneratedProtocolMessageType('CreateToolResponse', (_message.Message,), dict(
  DESCRIPTOR = _CREATETOOLRESPONSE,
  __module__ = 'create_tool_pb2'
  # @@protoc_insertion_point(class_scope:basic.CreateToolResponse)
  ))
_sym_db.RegisterMessage(CreateToolResponse)

CreateToolResponseWrapper = _reflection.GeneratedProtocolMessageType('CreateToolResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _CREATETOOLRESPONSEWRAPPER,
  __module__ = 'create_tool_pb2'
  # @@protoc_insertion_point(class_scope:basic.CreateToolResponseWrapper)
  ))
_sym_db.RegisterMessage(CreateToolResponseWrapper)


# @@protoc_insertion_point(module_scope)
