# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: running_install_app.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='running_install_app.proto',
  package='desktop',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x19running_install_app.proto\x12\x07\x64\x65sktop\":\n\x19RunningInstallAppResponse\x12\r\n\x05\x61ppId\x18\x01 \x01(\t\x12\x0e\n\x06taskId\x18\x02 \x01(\t\"\x86\x01\n RunningInstallAppResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x30\n\x04\x64\x61ta\x18\x04 \x03(\x0b\x32\".desktop.RunningInstallAppResponseb\x06proto3')
)




_RUNNINGINSTALLAPPRESPONSE = _descriptor.Descriptor(
  name='RunningInstallAppResponse',
  full_name='desktop.RunningInstallAppResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appId', full_name='desktop.RunningInstallAppResponse.appId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='taskId', full_name='desktop.RunningInstallAppResponse.taskId', index=1,
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
  serialized_start=38,
  serialized_end=96,
)


_RUNNINGINSTALLAPPRESPONSEWRAPPER = _descriptor.Descriptor(
  name='RunningInstallAppResponseWrapper',
  full_name='desktop.RunningInstallAppResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='desktop.RunningInstallAppResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='desktop.RunningInstallAppResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='desktop.RunningInstallAppResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='desktop.RunningInstallAppResponseWrapper.data', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=99,
  serialized_end=233,
)

_RUNNINGINSTALLAPPRESPONSEWRAPPER.fields_by_name['data'].message_type = _RUNNINGINSTALLAPPRESPONSE
DESCRIPTOR.message_types_by_name['RunningInstallAppResponse'] = _RUNNINGINSTALLAPPRESPONSE
DESCRIPTOR.message_types_by_name['RunningInstallAppResponseWrapper'] = _RUNNINGINSTALLAPPRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RunningInstallAppResponse = _reflection.GeneratedProtocolMessageType('RunningInstallAppResponse', (_message.Message,), dict(
  DESCRIPTOR = _RUNNINGINSTALLAPPRESPONSE,
  __module__ = 'running_install_app_pb2'
  # @@protoc_insertion_point(class_scope:desktop.RunningInstallAppResponse)
  ))
_sym_db.RegisterMessage(RunningInstallAppResponse)

RunningInstallAppResponseWrapper = _reflection.GeneratedProtocolMessageType('RunningInstallAppResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _RUNNINGINSTALLAPPRESPONSEWRAPPER,
  __module__ = 'running_install_app_pb2'
  # @@protoc_insertion_point(class_scope:desktop.RunningInstallAppResponseWrapper)
  ))
_sym_db.RegisterMessage(RunningInstallAppResponseWrapper)


# @@protoc_insertion_point(module_scope)