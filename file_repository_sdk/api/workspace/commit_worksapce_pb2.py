# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: commit_worksapce.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='commit_worksapce.proto',
  package='workspace',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16\x63ommit_worksapce.proto\x12\tworkspace\"O\n\x16\x43ommitWorkspaceRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x11\n\tpackageId\x18\x02 \x01(\t\x12\x11\n\tversionId\x18\x03 \x01(\t\"A\n\x17\x43ommitWorkspaceResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04\x63onf\x18\x02 \x01(\t\x12\x0c\n\x04sign\x18\x03 \x01(\t\"\x84\x01\n\x1e\x43ommitWorkspaceResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x30\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\".workspace.CommitWorkspaceResponseb\x06proto3')
)




_COMMITWORKSPACEREQUEST = _descriptor.Descriptor(
  name='CommitWorkspaceRequest',
  full_name='workspace.CommitWorkspaceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='workspace.CommitWorkspaceRequest.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageId', full_name='workspace.CommitWorkspaceRequest.packageId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionId', full_name='workspace.CommitWorkspaceRequest.versionId', index=2,
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
  serialized_start=37,
  serialized_end=116,
)


_COMMITWORKSPACERESPONSE = _descriptor.Descriptor(
  name='CommitWorkspaceResponse',
  full_name='workspace.CommitWorkspaceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='workspace.CommitWorkspaceResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conf', full_name='workspace.CommitWorkspaceResponse.conf', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sign', full_name='workspace.CommitWorkspaceResponse.sign', index=2,
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
  serialized_start=118,
  serialized_end=183,
)


_COMMITWORKSPACERESPONSEWRAPPER = _descriptor.Descriptor(
  name='CommitWorkspaceResponseWrapper',
  full_name='workspace.CommitWorkspaceResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='workspace.CommitWorkspaceResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='workspace.CommitWorkspaceResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='workspace.CommitWorkspaceResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='workspace.CommitWorkspaceResponseWrapper.data', index=3,
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
  serialized_start=186,
  serialized_end=318,
)

_COMMITWORKSPACERESPONSEWRAPPER.fields_by_name['data'].message_type = _COMMITWORKSPACERESPONSE
DESCRIPTOR.message_types_by_name['CommitWorkspaceRequest'] = _COMMITWORKSPACEREQUEST
DESCRIPTOR.message_types_by_name['CommitWorkspaceResponse'] = _COMMITWORKSPACERESPONSE
DESCRIPTOR.message_types_by_name['CommitWorkspaceResponseWrapper'] = _COMMITWORKSPACERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CommitWorkspaceRequest = _reflection.GeneratedProtocolMessageType('CommitWorkspaceRequest', (_message.Message,), dict(
  DESCRIPTOR = _COMMITWORKSPACEREQUEST,
  __module__ = 'commit_worksapce_pb2'
  # @@protoc_insertion_point(class_scope:workspace.CommitWorkspaceRequest)
  ))
_sym_db.RegisterMessage(CommitWorkspaceRequest)

CommitWorkspaceResponse = _reflection.GeneratedProtocolMessageType('CommitWorkspaceResponse', (_message.Message,), dict(
  DESCRIPTOR = _COMMITWORKSPACERESPONSE,
  __module__ = 'commit_worksapce_pb2'
  # @@protoc_insertion_point(class_scope:workspace.CommitWorkspaceResponse)
  ))
_sym_db.RegisterMessage(CommitWorkspaceResponse)

CommitWorkspaceResponseWrapper = _reflection.GeneratedProtocolMessageType('CommitWorkspaceResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _COMMITWORKSPACERESPONSEWRAPPER,
  __module__ = 'commit_worksapce_pb2'
  # @@protoc_insertion_point(class_scope:workspace.CommitWorkspaceResponseWrapper)
  ))
_sym_db.RegisterMessage(CommitWorkspaceResponseWrapper)


# @@protoc_insertion_point(module_scope)
