# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: commit_worksapce_v2.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='commit_worksapce_v2.proto',
  package='workspace',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x19\x63ommit_worksapce_v2.proto\x12\tworkspace\"\x81\x01\n\x18\x43ommitWorkspaceV2Request\x12\x11\n\tversionId\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0e\n\x06source\x18\x04 \x01(\t\x12\x10\n\x08\x65nv_type\x18\x05 \x01(\t\x12\x11\n\tpackageId\x18\x06 \x01(\t\"W\n\x19\x43ommitWorkspaceV2Response\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\r\n\x05\x65rror\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\t\"\x88\x01\n CommitWorkspaceV2ResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x32\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32$.workspace.CommitWorkspaceV2Responseb\x06proto3')
)




_COMMITWORKSPACEV2REQUEST = _descriptor.Descriptor(
  name='CommitWorkspaceV2Request',
  full_name='workspace.CommitWorkspaceV2Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='versionId', full_name='workspace.CommitWorkspaceV2Request.versionId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='workspace.CommitWorkspaceV2Request.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='workspace.CommitWorkspaceV2Request.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='workspace.CommitWorkspaceV2Request.source', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='env_type', full_name='workspace.CommitWorkspaceV2Request.env_type', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageId', full_name='workspace.CommitWorkspaceV2Request.packageId', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=41,
  serialized_end=170,
)


_COMMITWORKSPACEV2RESPONSE = _descriptor.Descriptor(
  name='CommitWorkspaceV2Response',
  full_name='workspace.CommitWorkspaceV2Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='workspace.CommitWorkspaceV2Response.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='workspace.CommitWorkspaceV2Response.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='workspace.CommitWorkspaceV2Response.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='workspace.CommitWorkspaceV2Response.data', index=3,
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
  serialized_start=172,
  serialized_end=259,
)


_COMMITWORKSPACEV2RESPONSEWRAPPER = _descriptor.Descriptor(
  name='CommitWorkspaceV2ResponseWrapper',
  full_name='workspace.CommitWorkspaceV2ResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='workspace.CommitWorkspaceV2ResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='workspace.CommitWorkspaceV2ResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='workspace.CommitWorkspaceV2ResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='workspace.CommitWorkspaceV2ResponseWrapper.data', index=3,
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
  serialized_start=262,
  serialized_end=398,
)

_COMMITWORKSPACEV2RESPONSEWRAPPER.fields_by_name['data'].message_type = _COMMITWORKSPACEV2RESPONSE
DESCRIPTOR.message_types_by_name['CommitWorkspaceV2Request'] = _COMMITWORKSPACEV2REQUEST
DESCRIPTOR.message_types_by_name['CommitWorkspaceV2Response'] = _COMMITWORKSPACEV2RESPONSE
DESCRIPTOR.message_types_by_name['CommitWorkspaceV2ResponseWrapper'] = _COMMITWORKSPACEV2RESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CommitWorkspaceV2Request = _reflection.GeneratedProtocolMessageType('CommitWorkspaceV2Request', (_message.Message,), {
  'DESCRIPTOR' : _COMMITWORKSPACEV2REQUEST,
  '__module__' : 'commit_worksapce_v2_pb2'
  # @@protoc_insertion_point(class_scope:workspace.CommitWorkspaceV2Request)
  })
_sym_db.RegisterMessage(CommitWorkspaceV2Request)

CommitWorkspaceV2Response = _reflection.GeneratedProtocolMessageType('CommitWorkspaceV2Response', (_message.Message,), {
  'DESCRIPTOR' : _COMMITWORKSPACEV2RESPONSE,
  '__module__' : 'commit_worksapce_v2_pb2'
  # @@protoc_insertion_point(class_scope:workspace.CommitWorkspaceV2Response)
  })
_sym_db.RegisterMessage(CommitWorkspaceV2Response)

CommitWorkspaceV2ResponseWrapper = _reflection.GeneratedProtocolMessageType('CommitWorkspaceV2ResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _COMMITWORKSPACEV2RESPONSEWRAPPER,
  '__module__' : 'commit_worksapce_v2_pb2'
  # @@protoc_insertion_point(class_scope:workspace.CommitWorkspaceV2ResponseWrapper)
  })
_sym_db.RegisterMessage(CommitWorkspaceV2ResponseWrapper)


# @@protoc_insertion_point(module_scope)
