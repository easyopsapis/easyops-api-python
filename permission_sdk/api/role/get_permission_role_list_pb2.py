# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_permission_role_list.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_permission_role_list.proto',
  package='role',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1eget_permission_role_list.proto\x12\x04role\"[\n\x1cGetPermissionRoleListRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x0c\n\x04role\x18\x02 \x01(\t\x12\x0c\n\x04page\x18\x03 \x01(\x05\x12\x11\n\tpage_size\x18\x04 \x01(\x05\"\x83\x02\n\x1dGetPermissionRoleListResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0c\n\x04page\x18\x02 \x01(\x05\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x36\n\x04\x64\x61ta\x18\x04 \x03(\x0b\x32(.role.GetPermissionRoleListResponse.Data\x1a{\n\x04\x44\x61ta\x12\x16\n\x0e\x66orbidden_menu\x18\x01 \x03(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0b\n\x03org\x18\x03 \x01(\x05\x12\x0c\n\x04role\x18\x04 \x01(\t\x12\x0c\n\x04user\x18\x05 \x03(\t\x12\x12\n\npermission\x18\x06 \x03(\t\x12\x12\n\nuser_group\x18\x07 \x03(\t\"\x8b\x01\n$GetPermissionRoleListResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x31\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32#.role.GetPermissionRoleListResponseb\x06proto3')
)




_GETPERMISSIONROLELISTREQUEST = _descriptor.Descriptor(
  name='GetPermissionRoleListRequest',
  full_name='role.GetPermissionRoleListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='role.GetPermissionRoleListRequest.user', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='role', full_name='role.GetPermissionRoleListRequest.role', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page', full_name='role.GetPermissionRoleListRequest.page', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='role.GetPermissionRoleListRequest.page_size', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_end=131,
)


_GETPERMISSIONROLELISTRESPONSE_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='role.GetPermissionRoleListResponse.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='forbidden_menu', full_name='role.GetPermissionRoleListResponse.Data.forbidden_menu', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='role.GetPermissionRoleListResponse.Data.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org', full_name='role.GetPermissionRoleListResponse.Data.org', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='role', full_name='role.GetPermissionRoleListResponse.Data.role', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='role.GetPermissionRoleListResponse.Data.user', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='permission', full_name='role.GetPermissionRoleListResponse.Data.permission', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_group', full_name='role.GetPermissionRoleListResponse.Data.user_group', index=6,
      number=7, type=9, cpp_type=9, label=3,
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
  serialized_start=270,
  serialized_end=393,
)

_GETPERMISSIONROLELISTRESPONSE = _descriptor.Descriptor(
  name='GetPermissionRoleListResponse',
  full_name='role.GetPermissionRoleListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='role.GetPermissionRoleListResponse.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page', full_name='role.GetPermissionRoleListResponse.page', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='role.GetPermissionRoleListResponse.page_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='role.GetPermissionRoleListResponse.data', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETPERMISSIONROLELISTRESPONSE_DATA, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=134,
  serialized_end=393,
)


_GETPERMISSIONROLELISTRESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetPermissionRoleListResponseWrapper',
  full_name='role.GetPermissionRoleListResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='role.GetPermissionRoleListResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='role.GetPermissionRoleListResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='role.GetPermissionRoleListResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='role.GetPermissionRoleListResponseWrapper.data', index=3,
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
  serialized_start=396,
  serialized_end=535,
)

_GETPERMISSIONROLELISTRESPONSE_DATA.containing_type = _GETPERMISSIONROLELISTRESPONSE
_GETPERMISSIONROLELISTRESPONSE.fields_by_name['data'].message_type = _GETPERMISSIONROLELISTRESPONSE_DATA
_GETPERMISSIONROLELISTRESPONSEWRAPPER.fields_by_name['data'].message_type = _GETPERMISSIONROLELISTRESPONSE
DESCRIPTOR.message_types_by_name['GetPermissionRoleListRequest'] = _GETPERMISSIONROLELISTREQUEST
DESCRIPTOR.message_types_by_name['GetPermissionRoleListResponse'] = _GETPERMISSIONROLELISTRESPONSE
DESCRIPTOR.message_types_by_name['GetPermissionRoleListResponseWrapper'] = _GETPERMISSIONROLELISTRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetPermissionRoleListRequest = _reflection.GeneratedProtocolMessageType('GetPermissionRoleListRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETPERMISSIONROLELISTREQUEST,
  __module__ = 'get_permission_role_list_pb2'
  # @@protoc_insertion_point(class_scope:role.GetPermissionRoleListRequest)
  ))
_sym_db.RegisterMessage(GetPermissionRoleListRequest)

GetPermissionRoleListResponse = _reflection.GeneratedProtocolMessageType('GetPermissionRoleListResponse', (_message.Message,), dict(

  Data = _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), dict(
    DESCRIPTOR = _GETPERMISSIONROLELISTRESPONSE_DATA,
    __module__ = 'get_permission_role_list_pb2'
    # @@protoc_insertion_point(class_scope:role.GetPermissionRoleListResponse.Data)
    ))
  ,
  DESCRIPTOR = _GETPERMISSIONROLELISTRESPONSE,
  __module__ = 'get_permission_role_list_pb2'
  # @@protoc_insertion_point(class_scope:role.GetPermissionRoleListResponse)
  ))
_sym_db.RegisterMessage(GetPermissionRoleListResponse)
_sym_db.RegisterMessage(GetPermissionRoleListResponse.Data)

GetPermissionRoleListResponseWrapper = _reflection.GeneratedProtocolMessageType('GetPermissionRoleListResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _GETPERMISSIONROLELISTRESPONSEWRAPPER,
  __module__ = 'get_permission_role_list_pb2'
  # @@protoc_insertion_point(class_scope:role.GetPermissionRoleListResponseWrapper)
  ))
_sym_db.RegisterMessage(GetPermissionRoleListResponseWrapper)


# @@protoc_insertion_point(module_scope)
