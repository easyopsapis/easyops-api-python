# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: safe_commit_workspace.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='safe_commit_workspace.proto',
  package='workspace',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1bsafe_commit_workspace.proto\x12\tworkspace\"\x83\x01\n\x1aSafeCommitWorkspaceRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x11\n\tpackageId\x18\x02 \x01(\t\x12\x11\n\tversionId\x18\x03 \x01(\t\x12\x10\n\x08\x65nv_type\x18\x04 \x01(\x05\x12\x0e\n\x06source\x18\x05 \x01(\t\x12\x0c\n\x04name\x18\x06 \x01(\t\"Y\n\x1bSafeCommitWorkspaceResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\r\n\x05\x65rror\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\t\"\x8c\x01\n\"SafeCommitWorkspaceResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x34\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32&.workspace.SafeCommitWorkspaceResponseb\x06proto3')
)




_SAFECOMMITWORKSPACEREQUEST = _descriptor.Descriptor(
  name='SafeCommitWorkspaceRequest',
  full_name='workspace.SafeCommitWorkspaceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='workspace.SafeCommitWorkspaceRequest.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageId', full_name='workspace.SafeCommitWorkspaceRequest.packageId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionId', full_name='workspace.SafeCommitWorkspaceRequest.versionId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='env_type', full_name='workspace.SafeCommitWorkspaceRequest.env_type', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='workspace.SafeCommitWorkspaceRequest.source', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='workspace.SafeCommitWorkspaceRequest.name', index=5,
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
  serialized_start=43,
  serialized_end=174,
)


_SAFECOMMITWORKSPACERESPONSE = _descriptor.Descriptor(
  name='SafeCommitWorkspaceResponse',
  full_name='workspace.SafeCommitWorkspaceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='workspace.SafeCommitWorkspaceResponse.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='workspace.SafeCommitWorkspaceResponse.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='workspace.SafeCommitWorkspaceResponse.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='workspace.SafeCommitWorkspaceResponse.data', index=3,
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
  serialized_start=176,
  serialized_end=265,
)


_SAFECOMMITWORKSPACERESPONSEWRAPPER = _descriptor.Descriptor(
  name='SafeCommitWorkspaceResponseWrapper',
  full_name='workspace.SafeCommitWorkspaceResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='workspace.SafeCommitWorkspaceResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='workspace.SafeCommitWorkspaceResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='workspace.SafeCommitWorkspaceResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='workspace.SafeCommitWorkspaceResponseWrapper.data', index=3,
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
  serialized_start=268,
  serialized_end=408,
)

_SAFECOMMITWORKSPACERESPONSEWRAPPER.fields_by_name['data'].message_type = _SAFECOMMITWORKSPACERESPONSE
DESCRIPTOR.message_types_by_name['SafeCommitWorkspaceRequest'] = _SAFECOMMITWORKSPACEREQUEST
DESCRIPTOR.message_types_by_name['SafeCommitWorkspaceResponse'] = _SAFECOMMITWORKSPACERESPONSE
DESCRIPTOR.message_types_by_name['SafeCommitWorkspaceResponseWrapper'] = _SAFECOMMITWORKSPACERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SafeCommitWorkspaceRequest = _reflection.GeneratedProtocolMessageType('SafeCommitWorkspaceRequest', (_message.Message,), dict(
  DESCRIPTOR = _SAFECOMMITWORKSPACEREQUEST,
  __module__ = 'safe_commit_workspace_pb2'
  # @@protoc_insertion_point(class_scope:workspace.SafeCommitWorkspaceRequest)
  ))
_sym_db.RegisterMessage(SafeCommitWorkspaceRequest)

SafeCommitWorkspaceResponse = _reflection.GeneratedProtocolMessageType('SafeCommitWorkspaceResponse', (_message.Message,), dict(
  DESCRIPTOR = _SAFECOMMITWORKSPACERESPONSE,
  __module__ = 'safe_commit_workspace_pb2'
  # @@protoc_insertion_point(class_scope:workspace.SafeCommitWorkspaceResponse)
  ))
_sym_db.RegisterMessage(SafeCommitWorkspaceResponse)

SafeCommitWorkspaceResponseWrapper = _reflection.GeneratedProtocolMessageType('SafeCommitWorkspaceResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _SAFECOMMITWORKSPACERESPONSEWRAPPER,
  __module__ = 'safe_commit_workspace_pb2'
  # @@protoc_insertion_point(class_scope:workspace.SafeCommitWorkspaceResponseWrapper)
  ))
_sym_db.RegisterMessage(SafeCommitWorkspaceResponseWrapper)


# @@protoc_insertion_point(module_scope)
