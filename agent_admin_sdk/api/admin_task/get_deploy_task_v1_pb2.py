# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_deploy_task_v1.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_deploy_task_v1.proto',
  package='admin_task',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x18get_deploy_task_v1.proto\x12\nadmin_task\"+\n\x16GetDeployTaskV1Request\x12\x11\n\tcmdTaskId\x18\x01 \x01(\t\"\xf5\x02\n\x17GetDeployTaskV1Response\x12\x10\n\x08targetId\x18\x01 \x01(\t\x12\x12\n\ntargetName\x18\x02 \x01(\t\x12\x0f\n\x07\x63reator\x18\x03 \x01(\t\x12\x0e\n\x06status\x18\x04 \x01(\t\x12\r\n\x05\x63time\x18\x05 \x01(\x05\x12\r\n\x05\x65time\x18\x06 \x01(\x05\x12\x42\n\ndeployList\x18\x07 \x03(\x0b\x32..admin_task.GetDeployTaskV1Response.DeployList\x1a\xb0\x01\n\nDeployList\x12\x0f\n\x07\x61gentId\x18\x01 \x01(\t\x12\n\n\x02ip\x18\x02 \x01(\t\x12\x12\n\ndeployPath\x18\x03 \x03(\t\x12\x15\n\ragentPluginId\x18\x04 \x01(\t\x12\x17\n\x0f\x61gentPluginName\x18\x05 \x01(\t\x12\x16\n\x0epreVersionName\x18\x06 \x01(\t\x12\x19\n\x11pluginVersionName\x18\x07 \x01(\t\x12\x0e\n\x06status\x18\x08 \x01(\t\"\x85\x01\n\x1eGetDeployTaskV1ResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x31\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32#.admin_task.GetDeployTaskV1Responseb\x06proto3')
)




_GETDEPLOYTASKV1REQUEST = _descriptor.Descriptor(
  name='GetDeployTaskV1Request',
  full_name='admin_task.GetDeployTaskV1Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmdTaskId', full_name='admin_task.GetDeployTaskV1Request.cmdTaskId', index=0,
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
  serialized_start=40,
  serialized_end=83,
)


_GETDEPLOYTASKV1RESPONSE_DEPLOYLIST = _descriptor.Descriptor(
  name='DeployList',
  full_name='admin_task.GetDeployTaskV1Response.DeployList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agentId', full_name='admin_task.GetDeployTaskV1Response.DeployList.agentId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip', full_name='admin_task.GetDeployTaskV1Response.DeployList.ip', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deployPath', full_name='admin_task.GetDeployTaskV1Response.DeployList.deployPath', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agentPluginId', full_name='admin_task.GetDeployTaskV1Response.DeployList.agentPluginId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agentPluginName', full_name='admin_task.GetDeployTaskV1Response.DeployList.agentPluginName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preVersionName', full_name='admin_task.GetDeployTaskV1Response.DeployList.preVersionName', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pluginVersionName', full_name='admin_task.GetDeployTaskV1Response.DeployList.pluginVersionName', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='admin_task.GetDeployTaskV1Response.DeployList.status', index=7,
      number=8, type=9, cpp_type=9, label=1,
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
  serialized_start=283,
  serialized_end=459,
)

_GETDEPLOYTASKV1RESPONSE = _descriptor.Descriptor(
  name='GetDeployTaskV1Response',
  full_name='admin_task.GetDeployTaskV1Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='targetId', full_name='admin_task.GetDeployTaskV1Response.targetId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targetName', full_name='admin_task.GetDeployTaskV1Response.targetName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='admin_task.GetDeployTaskV1Response.creator', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='admin_task.GetDeployTaskV1Response.status', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='admin_task.GetDeployTaskV1Response.ctime', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='etime', full_name='admin_task.GetDeployTaskV1Response.etime', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deployList', full_name='admin_task.GetDeployTaskV1Response.deployList', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETDEPLOYTASKV1RESPONSE_DEPLOYLIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=86,
  serialized_end=459,
)


_GETDEPLOYTASKV1RESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetDeployTaskV1ResponseWrapper',
  full_name='admin_task.GetDeployTaskV1ResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='admin_task.GetDeployTaskV1ResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='admin_task.GetDeployTaskV1ResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='admin_task.GetDeployTaskV1ResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='admin_task.GetDeployTaskV1ResponseWrapper.data', index=3,
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
  serialized_start=462,
  serialized_end=595,
)

_GETDEPLOYTASKV1RESPONSE_DEPLOYLIST.containing_type = _GETDEPLOYTASKV1RESPONSE
_GETDEPLOYTASKV1RESPONSE.fields_by_name['deployList'].message_type = _GETDEPLOYTASKV1RESPONSE_DEPLOYLIST
_GETDEPLOYTASKV1RESPONSEWRAPPER.fields_by_name['data'].message_type = _GETDEPLOYTASKV1RESPONSE
DESCRIPTOR.message_types_by_name['GetDeployTaskV1Request'] = _GETDEPLOYTASKV1REQUEST
DESCRIPTOR.message_types_by_name['GetDeployTaskV1Response'] = _GETDEPLOYTASKV1RESPONSE
DESCRIPTOR.message_types_by_name['GetDeployTaskV1ResponseWrapper'] = _GETDEPLOYTASKV1RESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetDeployTaskV1Request = _reflection.GeneratedProtocolMessageType('GetDeployTaskV1Request', (_message.Message,), {
  'DESCRIPTOR' : _GETDEPLOYTASKV1REQUEST,
  '__module__' : 'get_deploy_task_v1_pb2'
  # @@protoc_insertion_point(class_scope:admin_task.GetDeployTaskV1Request)
  })
_sym_db.RegisterMessage(GetDeployTaskV1Request)

GetDeployTaskV1Response = _reflection.GeneratedProtocolMessageType('GetDeployTaskV1Response', (_message.Message,), {

  'DeployList' : _reflection.GeneratedProtocolMessageType('DeployList', (_message.Message,), {
    'DESCRIPTOR' : _GETDEPLOYTASKV1RESPONSE_DEPLOYLIST,
    '__module__' : 'get_deploy_task_v1_pb2'
    # @@protoc_insertion_point(class_scope:admin_task.GetDeployTaskV1Response.DeployList)
    })
  ,
  'DESCRIPTOR' : _GETDEPLOYTASKV1RESPONSE,
  '__module__' : 'get_deploy_task_v1_pb2'
  # @@protoc_insertion_point(class_scope:admin_task.GetDeployTaskV1Response)
  })
_sym_db.RegisterMessage(GetDeployTaskV1Response)
_sym_db.RegisterMessage(GetDeployTaskV1Response.DeployList)

GetDeployTaskV1ResponseWrapper = _reflection.GeneratedProtocolMessageType('GetDeployTaskV1ResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _GETDEPLOYTASKV1RESPONSEWRAPPER,
  '__module__' : 'get_deploy_task_v1_pb2'
  # @@protoc_insertion_point(class_scope:admin_task.GetDeployTaskV1ResponseWrapper)
  })
_sym_db.RegisterMessage(GetDeployTaskV1ResponseWrapper)


# @@protoc_insertion_point(module_scope)
