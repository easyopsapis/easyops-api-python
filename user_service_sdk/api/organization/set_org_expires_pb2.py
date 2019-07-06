# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: set_org_expires.proto

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
  name='set_org_expires.proto',
  package='organization',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x15set_org_expires.proto\x12\x0corganization\x1a\x1bgoogle/protobuf/empty.proto\"<\n\x18SetOrgExpiredDateRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0c\x65xpired_date\x18\x02 \x01(\t\"z\n SetOrgExpiredDateResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12$\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x16.google.protobuf.Emptyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_SETORGEXPIREDDATEREQUEST = _descriptor.Descriptor(
  name='SetOrgExpiredDateRequest',
  full_name='organization.SetOrgExpiredDateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='organization.SetOrgExpiredDateRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expired_date', full_name='organization.SetOrgExpiredDateRequest.expired_date', index=1,
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
  serialized_start=68,
  serialized_end=128,
)


_SETORGEXPIREDDATERESPONSEWRAPPER = _descriptor.Descriptor(
  name='SetOrgExpiredDateResponseWrapper',
  full_name='organization.SetOrgExpiredDateResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='organization.SetOrgExpiredDateResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='organization.SetOrgExpiredDateResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='organization.SetOrgExpiredDateResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='organization.SetOrgExpiredDateResponseWrapper.data', index=3,
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
  serialized_start=130,
  serialized_end=252,
)

_SETORGEXPIREDDATERESPONSEWRAPPER.fields_by_name['data'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
DESCRIPTOR.message_types_by_name['SetOrgExpiredDateRequest'] = _SETORGEXPIREDDATEREQUEST
DESCRIPTOR.message_types_by_name['SetOrgExpiredDateResponseWrapper'] = _SETORGEXPIREDDATERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SetOrgExpiredDateRequest = _reflection.GeneratedProtocolMessageType('SetOrgExpiredDateRequest', (_message.Message,), dict(
  DESCRIPTOR = _SETORGEXPIREDDATEREQUEST,
  __module__ = 'set_org_expires_pb2'
  # @@protoc_insertion_point(class_scope:organization.SetOrgExpiredDateRequest)
  ))
_sym_db.RegisterMessage(SetOrgExpiredDateRequest)

SetOrgExpiredDateResponseWrapper = _reflection.GeneratedProtocolMessageType('SetOrgExpiredDateResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _SETORGEXPIREDDATERESPONSEWRAPPER,
  __module__ = 'set_org_expires_pb2'
  # @@protoc_insertion_point(class_scope:organization.SetOrgExpiredDateResponseWrapper)
  ))
_sym_db.RegisterMessage(SetOrgExpiredDateResponseWrapper)


# @@protoc_insertion_point(module_scope)
