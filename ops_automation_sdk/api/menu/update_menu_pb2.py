# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: update_menu.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='update_menu.proto',
  package='menu',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11update_menu.proto\x12\x04menu\"v\n\x11UpdateMenuRequest\x12\x0f\n\x07menusId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04icon\x18\x03 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x04 \x01(\t\x12\x10\n\x08visitors\x18\x05 \x03(\t\x12\x10\n\x08managers\x18\x06 \x03(\t\" \n\x12UpdateMenuResponse\x12\n\n\x02id\x18\x01 \x01(\t\"u\n\x19UpdateMenuResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12&\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x18.menu.UpdateMenuResponseb\x06proto3')
)




_UPDATEMENUREQUEST = _descriptor.Descriptor(
  name='UpdateMenuRequest',
  full_name='menu.UpdateMenuRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='menusId', full_name='menu.UpdateMenuRequest.menusId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='menu.UpdateMenuRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon', full_name='menu.UpdateMenuRequest.icon', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='menu.UpdateMenuRequest.category', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='visitors', full_name='menu.UpdateMenuRequest.visitors', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='managers', full_name='menu.UpdateMenuRequest.managers', index=5,
      number=6, type=9, cpp_type=9, label=3,
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
  serialized_start=27,
  serialized_end=145,
)


_UPDATEMENURESPONSE = _descriptor.Descriptor(
  name='UpdateMenuResponse',
  full_name='menu.UpdateMenuResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='menu.UpdateMenuResponse.id', index=0,
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
  serialized_start=147,
  serialized_end=179,
)


_UPDATEMENURESPONSEWRAPPER = _descriptor.Descriptor(
  name='UpdateMenuResponseWrapper',
  full_name='menu.UpdateMenuResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='menu.UpdateMenuResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='menu.UpdateMenuResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='menu.UpdateMenuResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='menu.UpdateMenuResponseWrapper.data', index=3,
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
  serialized_start=181,
  serialized_end=298,
)

_UPDATEMENURESPONSEWRAPPER.fields_by_name['data'].message_type = _UPDATEMENURESPONSE
DESCRIPTOR.message_types_by_name['UpdateMenuRequest'] = _UPDATEMENUREQUEST
DESCRIPTOR.message_types_by_name['UpdateMenuResponse'] = _UPDATEMENURESPONSE
DESCRIPTOR.message_types_by_name['UpdateMenuResponseWrapper'] = _UPDATEMENURESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateMenuRequest = _reflection.GeneratedProtocolMessageType('UpdateMenuRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEMENUREQUEST,
  __module__ = 'update_menu_pb2'
  # @@protoc_insertion_point(class_scope:menu.UpdateMenuRequest)
  ))
_sym_db.RegisterMessage(UpdateMenuRequest)

UpdateMenuResponse = _reflection.GeneratedProtocolMessageType('UpdateMenuResponse', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEMENURESPONSE,
  __module__ = 'update_menu_pb2'
  # @@protoc_insertion_point(class_scope:menu.UpdateMenuResponse)
  ))
_sym_db.RegisterMessage(UpdateMenuResponse)

UpdateMenuResponseWrapper = _reflection.GeneratedProtocolMessageType('UpdateMenuResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEMENURESPONSEWRAPPER,
  __module__ = 'update_menu_pb2'
  # @@protoc_insertion_point(class_scope:menu.UpdateMenuResponseWrapper)
  ))
_sym_db.RegisterMessage(UpdateMenuResponseWrapper)


# @@protoc_insertion_point(module_scope)
