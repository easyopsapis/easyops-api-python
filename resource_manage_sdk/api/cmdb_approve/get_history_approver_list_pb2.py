# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_history_approver_list.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_history_approver_list.proto',
  package='cmdb_approve',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1fget_history_approver_list.proto\x12\x0c\x63mdb_approve\x1a\x1cgoogle/protobuf/struct.proto\"G\n\x1dGetHistoryApproverListRequest\x12&\n\x05query\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\"2\n\x1eGetHistoryApproverListResponse\x12\x10\n\x08userList\x18\x01 \x03(\t\"\x95\x01\n%GetHistoryApproverListResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12:\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32,.cmdb_approve.GetHistoryApproverListResponseb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_GETHISTORYAPPROVERLISTREQUEST = _descriptor.Descriptor(
  name='GetHistoryApproverListRequest',
  full_name='cmdb_approve.GetHistoryApproverListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='cmdb_approve.GetHistoryApproverListRequest.query', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=79,
  serialized_end=150,
)


_GETHISTORYAPPROVERLISTRESPONSE = _descriptor.Descriptor(
  name='GetHistoryApproverListResponse',
  full_name='cmdb_approve.GetHistoryApproverListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userList', full_name='cmdb_approve.GetHistoryApproverListResponse.userList', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=152,
  serialized_end=202,
)


_GETHISTORYAPPROVERLISTRESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetHistoryApproverListResponseWrapper',
  full_name='cmdb_approve.GetHistoryApproverListResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='cmdb_approve.GetHistoryApproverListResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='cmdb_approve.GetHistoryApproverListResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='cmdb_approve.GetHistoryApproverListResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='cmdb_approve.GetHistoryApproverListResponseWrapper.data', index=3,
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
  serialized_start=205,
  serialized_end=354,
)

_GETHISTORYAPPROVERLISTREQUEST.fields_by_name['query'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_GETHISTORYAPPROVERLISTRESPONSEWRAPPER.fields_by_name['data'].message_type = _GETHISTORYAPPROVERLISTRESPONSE
DESCRIPTOR.message_types_by_name['GetHistoryApproverListRequest'] = _GETHISTORYAPPROVERLISTREQUEST
DESCRIPTOR.message_types_by_name['GetHistoryApproverListResponse'] = _GETHISTORYAPPROVERLISTRESPONSE
DESCRIPTOR.message_types_by_name['GetHistoryApproverListResponseWrapper'] = _GETHISTORYAPPROVERLISTRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetHistoryApproverListRequest = _reflection.GeneratedProtocolMessageType('GetHistoryApproverListRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETHISTORYAPPROVERLISTREQUEST,
  __module__ = 'get_history_approver_list_pb2'
  # @@protoc_insertion_point(class_scope:cmdb_approve.GetHistoryApproverListRequest)
  ))
_sym_db.RegisterMessage(GetHistoryApproverListRequest)

GetHistoryApproverListResponse = _reflection.GeneratedProtocolMessageType('GetHistoryApproverListResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETHISTORYAPPROVERLISTRESPONSE,
  __module__ = 'get_history_approver_list_pb2'
  # @@protoc_insertion_point(class_scope:cmdb_approve.GetHistoryApproverListResponse)
  ))
_sym_db.RegisterMessage(GetHistoryApproverListResponse)

GetHistoryApproverListResponseWrapper = _reflection.GeneratedProtocolMessageType('GetHistoryApproverListResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _GETHISTORYAPPROVERLISTRESPONSEWRAPPER,
  __module__ = 'get_history_approver_list_pb2'
  # @@protoc_insertion_point(class_scope:cmdb_approve.GetHistoryApproverListResponseWrapper)
  ))
_sym_db.RegisterMessage(GetHistoryApproverListResponseWrapper)


# @@protoc_insertion_point(module_scope)