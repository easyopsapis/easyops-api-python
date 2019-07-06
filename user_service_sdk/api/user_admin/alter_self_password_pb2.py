# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: alter_self_password.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='alter_self_password.proto',
  package='user_admin',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x19\x61lter_self_password.proto\x12\nuser_admin\x1a\x1bgoogle/protobuf/empty.proto\"A\n\x18\x41lterSelfPasswordRequest\x12\x10\n\x08password\x18\x01 \x01(\t\x12\x13\n\x0boldPassword\x18\x02 \x01(\t\"z\n AlterSelfPasswordResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12$\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x16.google.protobuf.Emptyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_ALTERSELFPASSWORDREQUEST = _descriptor.Descriptor(
  name='AlterSelfPasswordRequest',
  full_name='user_admin.AlterSelfPasswordRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='password', full_name='user_admin.AlterSelfPasswordRequest.password', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='oldPassword', full_name='user_admin.AlterSelfPasswordRequest.oldPassword', index=1,
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
  serialized_start=70,
  serialized_end=135,
)


_ALTERSELFPASSWORDRESPONSEWRAPPER = _descriptor.Descriptor(
  name='AlterSelfPasswordResponseWrapper',
  full_name='user_admin.AlterSelfPasswordResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='user_admin.AlterSelfPasswordResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='user_admin.AlterSelfPasswordResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='user_admin.AlterSelfPasswordResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='user_admin.AlterSelfPasswordResponseWrapper.data', index=3,
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
  serialized_start=137,
  serialized_end=259,
)

_ALTERSELFPASSWORDRESPONSEWRAPPER.fields_by_name['data'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
DESCRIPTOR.message_types_by_name['AlterSelfPasswordRequest'] = _ALTERSELFPASSWORDREQUEST
DESCRIPTOR.message_types_by_name['AlterSelfPasswordResponseWrapper'] = _ALTERSELFPASSWORDRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AlterSelfPasswordRequest = _reflection.GeneratedProtocolMessageType('AlterSelfPasswordRequest', (_message.Message,), dict(
  DESCRIPTOR = _ALTERSELFPASSWORDREQUEST,
  __module__ = 'alter_self_password_pb2'
  # @@protoc_insertion_point(class_scope:user_admin.AlterSelfPasswordRequest)
  ))
_sym_db.RegisterMessage(AlterSelfPasswordRequest)

AlterSelfPasswordResponseWrapper = _reflection.GeneratedProtocolMessageType('AlterSelfPasswordResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _ALTERSELFPASSWORDRESPONSEWRAPPER,
  __module__ = 'alter_self_password_pb2'
  # @@protoc_insertion_point(class_scope:user_admin.AlterSelfPasswordResponseWrapper)
  ))
_sym_db.RegisterMessage(AlterSelfPasswordResponseWrapper)


# @@protoc_insertion_point(module_scope)
