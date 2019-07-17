# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: install_plugin.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='install_plugin.proto',
  package='admin_task',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14install_plugin.proto\x12\nadmin_task\"\xab\x02\n\x18InstallPluginTaskRequest\x12=\n\x07targets\x18\x01 \x03(\x0b\x32,.admin_task.InstallPluginTaskRequest.Targets\x12\x10\n\x08taskType\x18\x02 \x01(\t\x12\x10\n\x08\x62\x61tchNum\x18\x03 \x01(\x05\x12\x15\n\rbatchInterval\x18\x04 \x01(\x05\x1a\x94\x01\n\x07Targets\x12\x0f\n\x07\x61gentId\x18\x01 \x01(\t\x12\n\n\x02ip\x18\x02 \x01(\t\x12\x12\n\ndeployPath\x18\x03 \x03(\t\x12\x10\n\x08pluginId\x18\x04 \x01(\t\x12\x12\n\npluginName\x18\x05 \x01(\t\x12\x19\n\x11pluginVersionName\x18\x06 \x01(\t\x12\x17\n\x0fpluginVersionId\x18\x07 \x01(\t\"\'\n\x19InstallPluginTaskResponse\x12\n\n\x02id\x18\x01 \x01(\t\"\x89\x01\n InstallPluginTaskResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x33\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32%.admin_task.InstallPluginTaskResponseb\x06proto3')
)




_INSTALLPLUGINTASKREQUEST_TARGETS = _descriptor.Descriptor(
  name='Targets',
  full_name='admin_task.InstallPluginTaskRequest.Targets',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agentId', full_name='admin_task.InstallPluginTaskRequest.Targets.agentId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip', full_name='admin_task.InstallPluginTaskRequest.Targets.ip', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deployPath', full_name='admin_task.InstallPluginTaskRequest.Targets.deployPath', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pluginId', full_name='admin_task.InstallPluginTaskRequest.Targets.pluginId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pluginName', full_name='admin_task.InstallPluginTaskRequest.Targets.pluginName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pluginVersionName', full_name='admin_task.InstallPluginTaskRequest.Targets.pluginVersionName', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pluginVersionId', full_name='admin_task.InstallPluginTaskRequest.Targets.pluginVersionId', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=188,
  serialized_end=336,
)

_INSTALLPLUGINTASKREQUEST = _descriptor.Descriptor(
  name='InstallPluginTaskRequest',
  full_name='admin_task.InstallPluginTaskRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='targets', full_name='admin_task.InstallPluginTaskRequest.targets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='taskType', full_name='admin_task.InstallPluginTaskRequest.taskType', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batchNum', full_name='admin_task.InstallPluginTaskRequest.batchNum', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batchInterval', full_name='admin_task.InstallPluginTaskRequest.batchInterval', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_INSTALLPLUGINTASKREQUEST_TARGETS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=336,
)


_INSTALLPLUGINTASKRESPONSE = _descriptor.Descriptor(
  name='InstallPluginTaskResponse',
  full_name='admin_task.InstallPluginTaskResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='admin_task.InstallPluginTaskResponse.id', index=0,
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
  serialized_start=338,
  serialized_end=377,
)


_INSTALLPLUGINTASKRESPONSEWRAPPER = _descriptor.Descriptor(
  name='InstallPluginTaskResponseWrapper',
  full_name='admin_task.InstallPluginTaskResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='admin_task.InstallPluginTaskResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='admin_task.InstallPluginTaskResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='admin_task.InstallPluginTaskResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='admin_task.InstallPluginTaskResponseWrapper.data', index=3,
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
  serialized_start=380,
  serialized_end=517,
)

_INSTALLPLUGINTASKREQUEST_TARGETS.containing_type = _INSTALLPLUGINTASKREQUEST
_INSTALLPLUGINTASKREQUEST.fields_by_name['targets'].message_type = _INSTALLPLUGINTASKREQUEST_TARGETS
_INSTALLPLUGINTASKRESPONSEWRAPPER.fields_by_name['data'].message_type = _INSTALLPLUGINTASKRESPONSE
DESCRIPTOR.message_types_by_name['InstallPluginTaskRequest'] = _INSTALLPLUGINTASKREQUEST
DESCRIPTOR.message_types_by_name['InstallPluginTaskResponse'] = _INSTALLPLUGINTASKRESPONSE
DESCRIPTOR.message_types_by_name['InstallPluginTaskResponseWrapper'] = _INSTALLPLUGINTASKRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InstallPluginTaskRequest = _reflection.GeneratedProtocolMessageType('InstallPluginTaskRequest', (_message.Message,), dict(

  Targets = _reflection.GeneratedProtocolMessageType('Targets', (_message.Message,), dict(
    DESCRIPTOR = _INSTALLPLUGINTASKREQUEST_TARGETS,
    __module__ = 'install_plugin_pb2'
    # @@protoc_insertion_point(class_scope:admin_task.InstallPluginTaskRequest.Targets)
    ))
  ,
  DESCRIPTOR = _INSTALLPLUGINTASKREQUEST,
  __module__ = 'install_plugin_pb2'
  # @@protoc_insertion_point(class_scope:admin_task.InstallPluginTaskRequest)
  ))
_sym_db.RegisterMessage(InstallPluginTaskRequest)
_sym_db.RegisterMessage(InstallPluginTaskRequest.Targets)

InstallPluginTaskResponse = _reflection.GeneratedProtocolMessageType('InstallPluginTaskResponse', (_message.Message,), dict(
  DESCRIPTOR = _INSTALLPLUGINTASKRESPONSE,
  __module__ = 'install_plugin_pb2'
  # @@protoc_insertion_point(class_scope:admin_task.InstallPluginTaskResponse)
  ))
_sym_db.RegisterMessage(InstallPluginTaskResponse)

InstallPluginTaskResponseWrapper = _reflection.GeneratedProtocolMessageType('InstallPluginTaskResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _INSTALLPLUGINTASKRESPONSEWRAPPER,
  __module__ = 'install_plugin_pb2'
  # @@protoc_insertion_point(class_scope:admin_task.InstallPluginTaskResponseWrapper)
  ))
_sym_db.RegisterMessage(InstallPluginTaskResponseWrapper)


# @@protoc_insertion_point(module_scope)