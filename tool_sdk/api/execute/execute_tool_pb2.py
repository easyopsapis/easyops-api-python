# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: execute_tool.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from model.tool import callback_pb2 as model_dot_tool_dot_callback__pb2
from model.tool import input_param_pb2 as model_dot_tool_dot_input__param__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='execute_tool.proto',
  package='execute',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x12\x65xecute_tool.proto\x12\x07\x65xecute\x1a\x19model/tool/callback.proto\x1a\x1cmodel/tool/input_param.proto\"\x9f\x02\n\x12\x45xecuteToolRequest\x12\x0e\n\x06\x61gents\x18\x01 \x03(\t\x12 \n\x08\x63\x61llback\x18\x02 \x01(\x0b\x32\x0e.tool.Callback\x12\x12\n\nneedNotify\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x36\n\x08metadata\x18\x05 \x01(\x0b\x32$.execute.ExecuteToolRequest.Metadata\x12\x0e\n\x06toolId\x18\x06 \x01(\t\x12\x0b\n\x03vId\x18\x07 \x01(\t\x12!\n\x06inputs\x18\x08 \x03(\x0b\x32\x11.tool.input_param\x12\x10\n\x08\x65xecUser\x18\t \x01(\t\x12\x0f\n\x07timeout\x18\n \x01(\x05\x1a\x1a\n\x08Metadata\x12\x0e\n\x06origin\x18\x01 \x01(\t\"%\n\x13\x45xecuteToolResponse\x12\x0e\n\x06\x65xecId\x18\x01 \x01(\t\"z\n\x1a\x45xecuteToolResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12*\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1c.execute.ExecuteToolResponseb\x06proto3')
  ,
  dependencies=[model_dot_tool_dot_callback__pb2.DESCRIPTOR,model_dot_tool_dot_input__param__pb2.DESCRIPTOR,])




_EXECUTETOOLREQUEST_METADATA = _descriptor.Descriptor(
  name='Metadata',
  full_name='execute.ExecuteToolRequest.Metadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='origin', full_name='execute.ExecuteToolRequest.Metadata.origin', index=0,
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
  serialized_start=350,
  serialized_end=376,
)

_EXECUTETOOLREQUEST = _descriptor.Descriptor(
  name='ExecuteToolRequest',
  full_name='execute.ExecuteToolRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agents', full_name='execute.ExecuteToolRequest.agents', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='callback', full_name='execute.ExecuteToolRequest.callback', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='needNotify', full_name='execute.ExecuteToolRequest.needNotify', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='execute.ExecuteToolRequest.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='execute.ExecuteToolRequest.metadata', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='toolId', full_name='execute.ExecuteToolRequest.toolId', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vId', full_name='execute.ExecuteToolRequest.vId', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inputs', full_name='execute.ExecuteToolRequest.inputs', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='execUser', full_name='execute.ExecuteToolRequest.execUser', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='execute.ExecuteToolRequest.timeout', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_EXECUTETOOLREQUEST_METADATA, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=89,
  serialized_end=376,
)


_EXECUTETOOLRESPONSE = _descriptor.Descriptor(
  name='ExecuteToolResponse',
  full_name='execute.ExecuteToolResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='execId', full_name='execute.ExecuteToolResponse.execId', index=0,
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
  serialized_start=378,
  serialized_end=415,
)


_EXECUTETOOLRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ExecuteToolResponseWrapper',
  full_name='execute.ExecuteToolResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='execute.ExecuteToolResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='execute.ExecuteToolResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='execute.ExecuteToolResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='execute.ExecuteToolResponseWrapper.data', index=3,
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
  serialized_start=417,
  serialized_end=539,
)

_EXECUTETOOLREQUEST_METADATA.containing_type = _EXECUTETOOLREQUEST
_EXECUTETOOLREQUEST.fields_by_name['callback'].message_type = model_dot_tool_dot_callback__pb2._CALLBACK
_EXECUTETOOLREQUEST.fields_by_name['metadata'].message_type = _EXECUTETOOLREQUEST_METADATA
_EXECUTETOOLREQUEST.fields_by_name['inputs'].message_type = model_dot_tool_dot_input__param__pb2._INPUT_PARAM
_EXECUTETOOLRESPONSEWRAPPER.fields_by_name['data'].message_type = _EXECUTETOOLRESPONSE
DESCRIPTOR.message_types_by_name['ExecuteToolRequest'] = _EXECUTETOOLREQUEST
DESCRIPTOR.message_types_by_name['ExecuteToolResponse'] = _EXECUTETOOLRESPONSE
DESCRIPTOR.message_types_by_name['ExecuteToolResponseWrapper'] = _EXECUTETOOLRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExecuteToolRequest = _reflection.GeneratedProtocolMessageType('ExecuteToolRequest', (_message.Message,), dict(

  Metadata = _reflection.GeneratedProtocolMessageType('Metadata', (_message.Message,), dict(
    DESCRIPTOR = _EXECUTETOOLREQUEST_METADATA,
    __module__ = 'execute_tool_pb2'
    # @@protoc_insertion_point(class_scope:execute.ExecuteToolRequest.Metadata)
    ))
  ,
  DESCRIPTOR = _EXECUTETOOLREQUEST,
  __module__ = 'execute_tool_pb2'
  # @@protoc_insertion_point(class_scope:execute.ExecuteToolRequest)
  ))
_sym_db.RegisterMessage(ExecuteToolRequest)
_sym_db.RegisterMessage(ExecuteToolRequest.Metadata)

ExecuteToolResponse = _reflection.GeneratedProtocolMessageType('ExecuteToolResponse', (_message.Message,), dict(
  DESCRIPTOR = _EXECUTETOOLRESPONSE,
  __module__ = 'execute_tool_pb2'
  # @@protoc_insertion_point(class_scope:execute.ExecuteToolResponse)
  ))
_sym_db.RegisterMessage(ExecuteToolResponse)

ExecuteToolResponseWrapper = _reflection.GeneratedProtocolMessageType('ExecuteToolResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _EXECUTETOOLRESPONSEWRAPPER,
  __module__ = 'execute_tool_pb2'
  # @@protoc_insertion_point(class_scope:execute.ExecuteToolResponseWrapper)
  ))
_sym_db.RegisterMessage(ExecuteToolResponseWrapper)


# @@protoc_insertion_point(module_scope)
