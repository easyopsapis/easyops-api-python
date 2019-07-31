# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: delete.proto

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
  name='delete.proto',
  package='dbinstance',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0c\x64\x65lete.proto\x12\ndbinstance\x1a\x1bgoogle/protobuf/empty.proto\"D\n\x17\x44\x65leteDBInstanceRequest\x12\x14\n\x0c\x64\x62InstanceId\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x62ServiceId\x18\x02 \x01(\t\"y\n\x1f\x44\x65leteDBInstanceResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12$\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x16.google.protobuf.Emptyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_DELETEDBINSTANCEREQUEST = _descriptor.Descriptor(
  name='DeleteDBInstanceRequest',
  full_name='dbinstance.DeleteDBInstanceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dbInstanceId', full_name='dbinstance.DeleteDBInstanceRequest.dbInstanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dbServiceId', full_name='dbinstance.DeleteDBInstanceRequest.dbServiceId', index=1,
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
  serialized_start=57,
  serialized_end=125,
)


_DELETEDBINSTANCERESPONSEWRAPPER = _descriptor.Descriptor(
  name='DeleteDBInstanceResponseWrapper',
  full_name='dbinstance.DeleteDBInstanceResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='dbinstance.DeleteDBInstanceResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='dbinstance.DeleteDBInstanceResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dbinstance.DeleteDBInstanceResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='dbinstance.DeleteDBInstanceResponseWrapper.data', index=3,
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
  serialized_start=127,
  serialized_end=248,
)

_DELETEDBINSTANCERESPONSEWRAPPER.fields_by_name['data'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
DESCRIPTOR.message_types_by_name['DeleteDBInstanceRequest'] = _DELETEDBINSTANCEREQUEST
DESCRIPTOR.message_types_by_name['DeleteDBInstanceResponseWrapper'] = _DELETEDBINSTANCERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeleteDBInstanceRequest = _reflection.GeneratedProtocolMessageType('DeleteDBInstanceRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETEDBINSTANCEREQUEST,
  __module__ = 'delete_pb2'
  # @@protoc_insertion_point(class_scope:dbinstance.DeleteDBInstanceRequest)
  ))
_sym_db.RegisterMessage(DeleteDBInstanceRequest)

DeleteDBInstanceResponseWrapper = _reflection.GeneratedProtocolMessageType('DeleteDBInstanceResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _DELETEDBINSTANCERESPONSEWRAPPER,
  __module__ = 'delete_pb2'
  # @@protoc_insertion_point(class_scope:dbinstance.DeleteDBInstanceResponseWrapper)
  ))
_sym_db.RegisterMessage(DeleteDBInstanceResponseWrapper)


# @@protoc_insertion_point(module_scope)
