# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_version_permission_info.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from model.artifact import white_permission_user_pb2 as model_dot_artifact_dot_white__permission__user__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_version_permission_info.proto',
  package='version',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n!get_version_permission_info.proto\x12\x07version\x1a*model/artifact/white_permission_user.proto\"_\n\x1fGetVersionPermissionInfoRequest\x12\x16\n\x0epermissionType\x18\x01 \x01(\t\x12\x11\n\tpackageId\x18\x02 \x01(\t\x12\x11\n\tversionId\x18\x03 \x01(\t\"\x88\x01\n\'GetVersionPermissionInfoResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12+\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1d.artifact.WhitePermissionUserb\x06proto3')
  ,
  dependencies=[model_dot_artifact_dot_white__permission__user__pb2.DESCRIPTOR,])




_GETVERSIONPERMISSIONINFOREQUEST = _descriptor.Descriptor(
  name='GetVersionPermissionInfoRequest',
  full_name='version.GetVersionPermissionInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='permissionType', full_name='version.GetVersionPermissionInfoRequest.permissionType', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageId', full_name='version.GetVersionPermissionInfoRequest.packageId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionId', full_name='version.GetVersionPermissionInfoRequest.versionId', index=2,
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
  serialized_start=90,
  serialized_end=185,
)


_GETVERSIONPERMISSIONINFORESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetVersionPermissionInfoResponseWrapper',
  full_name='version.GetVersionPermissionInfoResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='version.GetVersionPermissionInfoResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='version.GetVersionPermissionInfoResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='version.GetVersionPermissionInfoResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='version.GetVersionPermissionInfoResponseWrapper.data', index=3,
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
  serialized_start=188,
  serialized_end=324,
)

_GETVERSIONPERMISSIONINFORESPONSEWRAPPER.fields_by_name['data'].message_type = model_dot_artifact_dot_white__permission__user__pb2._WHITEPERMISSIONUSER
DESCRIPTOR.message_types_by_name['GetVersionPermissionInfoRequest'] = _GETVERSIONPERMISSIONINFOREQUEST
DESCRIPTOR.message_types_by_name['GetVersionPermissionInfoResponseWrapper'] = _GETVERSIONPERMISSIONINFORESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetVersionPermissionInfoRequest = _reflection.GeneratedProtocolMessageType('GetVersionPermissionInfoRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETVERSIONPERMISSIONINFOREQUEST,
  __module__ = 'get_version_permission_info_pb2'
  # @@protoc_insertion_point(class_scope:version.GetVersionPermissionInfoRequest)
  ))
_sym_db.RegisterMessage(GetVersionPermissionInfoRequest)

GetVersionPermissionInfoResponseWrapper = _reflection.GeneratedProtocolMessageType('GetVersionPermissionInfoResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _GETVERSIONPERMISSIONINFORESPONSEWRAPPER,
  __module__ = 'get_version_permission_info_pb2'
  # @@protoc_insertion_point(class_scope:version.GetVersionPermissionInfoResponseWrapper)
  ))
_sym_db.RegisterMessage(GetVersionPermissionInfoResponseWrapper)


# @@protoc_insertion_point(module_scope)
