# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: agent_install_progress.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='agent_install_progress.proto',
  package='agent',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1c\x61gent_install_progress.proto\x12\x05\x61gent\"[\n\x1b\x41gentInstallProgressRequest\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\x12\x10\n\x08username\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\"O\n\x1c\x41gentInstallProgressResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0f\n\x07retCode\x18\x02 \x01(\x05\x12\x0e\n\x06\x64\x65tail\x18\x03 \x01(\t\"\x8a\x01\n#AgentInstallProgressResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x31\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32#.agent.AgentInstallProgressResponseb\x06proto3')
)




_AGENTINSTALLPROGRESSREQUEST = _descriptor.Descriptor(
  name='AgentInstallProgressRequest',
  full_name='agent.AgentInstallProgressRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='agent.AgentInstallProgressRequest.ip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='agent.AgentInstallProgressRequest.port', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='username', full_name='agent.AgentInstallProgressRequest.username', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='agent.AgentInstallProgressRequest.password', index=3,
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
  serialized_start=39,
  serialized_end=130,
)


_AGENTINSTALLPROGRESSRESPONSE = _descriptor.Descriptor(
  name='AgentInstallProgressResponse',
  full_name='agent.AgentInstallProgressResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='agent.AgentInstallProgressResponse.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='retCode', full_name='agent.AgentInstallProgressResponse.retCode', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='detail', full_name='agent.AgentInstallProgressResponse.detail', index=2,
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
  serialized_start=132,
  serialized_end=211,
)


_AGENTINSTALLPROGRESSRESPONSEWRAPPER = _descriptor.Descriptor(
  name='AgentInstallProgressResponseWrapper',
  full_name='agent.AgentInstallProgressResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='agent.AgentInstallProgressResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='agent.AgentInstallProgressResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='agent.AgentInstallProgressResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='agent.AgentInstallProgressResponseWrapper.data', index=3,
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
  serialized_start=214,
  serialized_end=352,
)

_AGENTINSTALLPROGRESSRESPONSEWRAPPER.fields_by_name['data'].message_type = _AGENTINSTALLPROGRESSRESPONSE
DESCRIPTOR.message_types_by_name['AgentInstallProgressRequest'] = _AGENTINSTALLPROGRESSREQUEST
DESCRIPTOR.message_types_by_name['AgentInstallProgressResponse'] = _AGENTINSTALLPROGRESSRESPONSE
DESCRIPTOR.message_types_by_name['AgentInstallProgressResponseWrapper'] = _AGENTINSTALLPROGRESSRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AgentInstallProgressRequest = _reflection.GeneratedProtocolMessageType('AgentInstallProgressRequest', (_message.Message,), {
  'DESCRIPTOR' : _AGENTINSTALLPROGRESSREQUEST,
  '__module__' : 'agent_install_progress_pb2'
  # @@protoc_insertion_point(class_scope:agent.AgentInstallProgressRequest)
  })
_sym_db.RegisterMessage(AgentInstallProgressRequest)

AgentInstallProgressResponse = _reflection.GeneratedProtocolMessageType('AgentInstallProgressResponse', (_message.Message,), {
  'DESCRIPTOR' : _AGENTINSTALLPROGRESSRESPONSE,
  '__module__' : 'agent_install_progress_pb2'
  # @@protoc_insertion_point(class_scope:agent.AgentInstallProgressResponse)
  })
_sym_db.RegisterMessage(AgentInstallProgressResponse)

AgentInstallProgressResponseWrapper = _reflection.GeneratedProtocolMessageType('AgentInstallProgressResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _AGENTINSTALLPROGRESSRESPONSEWRAPPER,
  '__module__' : 'agent_install_progress_pb2'
  # @@protoc_insertion_point(class_scope:agent.AgentInstallProgressResponseWrapper)
  })
_sym_db.RegisterMessage(AgentInstallProgressResponseWrapper)


# @@protoc_insertion_point(module_scope)