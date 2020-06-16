# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_app_deploy_instance.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_app_deploy_instance.proto',
  package='business',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1dget_app_deploy_instance.proto\x12\x08\x62usiness\"-\n\x1bGetAppDeployInstanceRequest\x12\x0e\n\x06\x61ppIds\x18\x01 \x01(\t\"\xe4\x01\n\x1cGetAppDeployInstanceResponse\x12\x39\n\x04list\x18\x01 \x03(\x0b\x32+.business.GetAppDeployInstanceResponse.List\x1a\x88\x01\n\x04List\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x11\n\tpackageId\x18\x02 \x01(\t\x12\x11\n\tversionId\x18\x03 \x01(\t\x12\x10\n\x08\x64\x65viceId\x18\x04 \x01(\t\x12\x10\n\x08\x64\x65viceIp\x18\x05 \x01(\t\x12\x13\n\x0binstallPath\x18\x06 \x01(\t\x12\r\n\x05\x61ppId\x18\x07 \x01(\t\"\x8d\x01\n#GetAppDeployInstanceResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x34\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32&.business.GetAppDeployInstanceResponseb\x06proto3')
)




_GETAPPDEPLOYINSTANCEREQUEST = _descriptor.Descriptor(
  name='GetAppDeployInstanceRequest',
  full_name='business.GetAppDeployInstanceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appIds', full_name='business.GetAppDeployInstanceRequest.appIds', index=0,
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
  serialized_start=43,
  serialized_end=88,
)


_GETAPPDEPLOYINSTANCERESPONSE_LIST = _descriptor.Descriptor(
  name='List',
  full_name='business.GetAppDeployInstanceResponse.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='business.GetAppDeployInstanceResponse.List.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageId', full_name='business.GetAppDeployInstanceResponse.List.packageId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionId', full_name='business.GetAppDeployInstanceResponse.List.versionId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deviceId', full_name='business.GetAppDeployInstanceResponse.List.deviceId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deviceIp', full_name='business.GetAppDeployInstanceResponse.List.deviceIp', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='installPath', full_name='business.GetAppDeployInstanceResponse.List.installPath', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='appId', full_name='business.GetAppDeployInstanceResponse.List.appId', index=6,
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
  serialized_start=183,
  serialized_end=319,
)

_GETAPPDEPLOYINSTANCERESPONSE = _descriptor.Descriptor(
  name='GetAppDeployInstanceResponse',
  full_name='business.GetAppDeployInstanceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='list', full_name='business.GetAppDeployInstanceResponse.list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETAPPDEPLOYINSTANCERESPONSE_LIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=91,
  serialized_end=319,
)


_GETAPPDEPLOYINSTANCERESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetAppDeployInstanceResponseWrapper',
  full_name='business.GetAppDeployInstanceResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='business.GetAppDeployInstanceResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='business.GetAppDeployInstanceResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='business.GetAppDeployInstanceResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='business.GetAppDeployInstanceResponseWrapper.data', index=3,
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
  serialized_start=322,
  serialized_end=463,
)

_GETAPPDEPLOYINSTANCERESPONSE_LIST.containing_type = _GETAPPDEPLOYINSTANCERESPONSE
_GETAPPDEPLOYINSTANCERESPONSE.fields_by_name['list'].message_type = _GETAPPDEPLOYINSTANCERESPONSE_LIST
_GETAPPDEPLOYINSTANCERESPONSEWRAPPER.fields_by_name['data'].message_type = _GETAPPDEPLOYINSTANCERESPONSE
DESCRIPTOR.message_types_by_name['GetAppDeployInstanceRequest'] = _GETAPPDEPLOYINSTANCEREQUEST
DESCRIPTOR.message_types_by_name['GetAppDeployInstanceResponse'] = _GETAPPDEPLOYINSTANCERESPONSE
DESCRIPTOR.message_types_by_name['GetAppDeployInstanceResponseWrapper'] = _GETAPPDEPLOYINSTANCERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetAppDeployInstanceRequest = _reflection.GeneratedProtocolMessageType('GetAppDeployInstanceRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETAPPDEPLOYINSTANCEREQUEST,
  '__module__' : 'get_app_deploy_instance_pb2'
  # @@protoc_insertion_point(class_scope:business.GetAppDeployInstanceRequest)
  })
_sym_db.RegisterMessage(GetAppDeployInstanceRequest)

GetAppDeployInstanceResponse = _reflection.GeneratedProtocolMessageType('GetAppDeployInstanceResponse', (_message.Message,), {

  'List' : _reflection.GeneratedProtocolMessageType('List', (_message.Message,), {
    'DESCRIPTOR' : _GETAPPDEPLOYINSTANCERESPONSE_LIST,
    '__module__' : 'get_app_deploy_instance_pb2'
    # @@protoc_insertion_point(class_scope:business.GetAppDeployInstanceResponse.List)
    })
  ,
  'DESCRIPTOR' : _GETAPPDEPLOYINSTANCERESPONSE,
  '__module__' : 'get_app_deploy_instance_pb2'
  # @@protoc_insertion_point(class_scope:business.GetAppDeployInstanceResponse)
  })
_sym_db.RegisterMessage(GetAppDeployInstanceResponse)
_sym_db.RegisterMessage(GetAppDeployInstanceResponse.List)

GetAppDeployInstanceResponseWrapper = _reflection.GeneratedProtocolMessageType('GetAppDeployInstanceResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _GETAPPDEPLOYINSTANCERESPONSEWRAPPER,
  '__module__' : 'get_app_deploy_instance_pb2'
  # @@protoc_insertion_point(class_scope:business.GetAppDeployInstanceResponseWrapper)
  })
_sym_db.RegisterMessage(GetAppDeployInstanceResponseWrapper)


# @@protoc_insertion_point(module_scope)