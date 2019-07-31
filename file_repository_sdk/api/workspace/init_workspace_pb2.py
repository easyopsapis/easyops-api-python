# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: init_workspace.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='init_workspace.proto',
  package='workspace',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14init_workspace.proto\x12\tworkspace\"3\n\x0bInitRequest\x12\x11\n\tpackageId\x18\x01 \x01(\t\x12\x11\n\tversionId\x18\x02 \x01(\t\"J\n\x0cInitResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\r\n\x05\x65rror\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\t\"n\n\x13InitResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12%\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x17.workspace.InitResponseb\x06proto3')
)




_INITREQUEST = _descriptor.Descriptor(
  name='InitRequest',
  full_name='workspace.InitRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='packageId', full_name='workspace.InitRequest.packageId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionId', full_name='workspace.InitRequest.versionId', index=1,
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
  serialized_start=35,
  serialized_end=86,
)


_INITRESPONSE = _descriptor.Descriptor(
  name='InitResponse',
  full_name='workspace.InitResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='workspace.InitResponse.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='workspace.InitResponse.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='workspace.InitResponse.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='workspace.InitResponse.data', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=88,
  serialized_end=162,
)


_INITRESPONSEWRAPPER = _descriptor.Descriptor(
  name='InitResponseWrapper',
  full_name='workspace.InitResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='workspace.InitResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='workspace.InitResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='workspace.InitResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='workspace.InitResponseWrapper.data', index=3,
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
  serialized_start=164,
  serialized_end=274,
)

_INITRESPONSEWRAPPER.fields_by_name['data'].message_type = _INITRESPONSE
DESCRIPTOR.message_types_by_name['InitRequest'] = _INITREQUEST
DESCRIPTOR.message_types_by_name['InitResponse'] = _INITRESPONSE
DESCRIPTOR.message_types_by_name['InitResponseWrapper'] = _INITRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InitRequest = _reflection.GeneratedProtocolMessageType('InitRequest', (_message.Message,), dict(
  DESCRIPTOR = _INITREQUEST,
  __module__ = 'init_workspace_pb2'
  # @@protoc_insertion_point(class_scope:workspace.InitRequest)
  ))
_sym_db.RegisterMessage(InitRequest)

InitResponse = _reflection.GeneratedProtocolMessageType('InitResponse', (_message.Message,), dict(
  DESCRIPTOR = _INITRESPONSE,
  __module__ = 'init_workspace_pb2'
  # @@protoc_insertion_point(class_scope:workspace.InitResponse)
  ))
_sym_db.RegisterMessage(InitResponse)

InitResponseWrapper = _reflection.GeneratedProtocolMessageType('InitResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _INITRESPONSEWRAPPER,
  __module__ = 'init_workspace_pb2'
  # @@protoc_insertion_point(class_scope:workspace.InitResponseWrapper)
  ))
_sym_db.RegisterMessage(InitResponseWrapper)


# @@protoc_insertion_point(module_scope)
