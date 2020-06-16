# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from database_delivery_sdk.model.database_delivery import dbinstance_pb2 as database__delivery__sdk_dot_model_dot_database__delivery_dot_dbinstance__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='list.proto',
  package='dbservice',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\nlist.proto\x12\tdbservice\x1a>database_delivery_sdk/model/database_delivery/dbinstance.proto\"6\n\x14ListDBServiceRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x10\n\x08pageSize\x18\x02 \x01(\x05\"\xb1\x03\n\x15ListDBServiceResponse\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12\x33\n\x04list\x18\x04 \x03(\x0b\x32%.dbservice.ListDBServiceResponse.List\x1a\xb2\x02\n\x04List\x12\x31\n\ndbInstance\x18\x01 \x03(\x0b\x32\x1d.database_delivery.DBInstance\x12:\n\x05owner\x18\x02 \x03(\x0b\x32+.dbservice.ListDBServiceResponse.List.Owner\x12\x12\n\ninstanceId\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0e\n\x06\x64\x62Type\x18\x05 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x06 \x01(\t\x12\x13\n\x0bupdatedTime\x18\x07 \x01(\x03\x1a\x66\n\x05Owner\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x12\n\nuser_email\x18\x02 \x01(\t\x12\x10\n\x08user_tel\x18\x03 \x01(\t\x12\x11\n\tuser_type\x18\x04 \x01(\t\x12\x10\n\x08nickname\x18\x05 \x01(\t\"\x80\x01\n\x1cListDBServiceResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12.\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32 .dbservice.ListDBServiceResponseb\x06proto3')
  ,
  dependencies=[database__delivery__sdk_dot_model_dot_database__delivery_dot_dbinstance__pb2.DESCRIPTOR,])




_LISTDBSERVICEREQUEST = _descriptor.Descriptor(
  name='ListDBServiceRequest',
  full_name='dbservice.ListDBServiceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='dbservice.ListDBServiceRequest.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='dbservice.ListDBServiceRequest.pageSize', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=89,
  serialized_end=143,
)


_LISTDBSERVICERESPONSE_LIST_OWNER = _descriptor.Descriptor(
  name='Owner',
  full_name='dbservice.ListDBServiceResponse.List.Owner',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='dbservice.ListDBServiceResponse.List.Owner.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_email', full_name='dbservice.ListDBServiceResponse.List.Owner.user_email', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_tel', full_name='dbservice.ListDBServiceResponse.List.Owner.user_tel', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_type', full_name='dbservice.ListDBServiceResponse.List.Owner.user_type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nickname', full_name='dbservice.ListDBServiceResponse.List.Owner.nickname', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=477,
  serialized_end=579,
)

_LISTDBSERVICERESPONSE_LIST = _descriptor.Descriptor(
  name='List',
  full_name='dbservice.ListDBServiceResponse.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dbInstance', full_name='dbservice.ListDBServiceResponse.List.dbInstance', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='owner', full_name='dbservice.ListDBServiceResponse.List.owner', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='dbservice.ListDBServiceResponse.List.instanceId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='dbservice.ListDBServiceResponse.List.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dbType', full_name='dbservice.ListDBServiceResponse.List.dbType', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='desc', full_name='dbservice.ListDBServiceResponse.List.desc', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updatedTime', full_name='dbservice.ListDBServiceResponse.List.updatedTime', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTDBSERVICERESPONSE_LIST_OWNER, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=273,
  serialized_end=579,
)

_LISTDBSERVICERESPONSE = _descriptor.Descriptor(
  name='ListDBServiceResponse',
  full_name='dbservice.ListDBServiceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='dbservice.ListDBServiceResponse.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='dbservice.ListDBServiceResponse.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='dbservice.ListDBServiceResponse.total', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='dbservice.ListDBServiceResponse.list', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTDBSERVICERESPONSE_LIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=146,
  serialized_end=579,
)


_LISTDBSERVICERESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListDBServiceResponseWrapper',
  full_name='dbservice.ListDBServiceResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='dbservice.ListDBServiceResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='dbservice.ListDBServiceResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dbservice.ListDBServiceResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='dbservice.ListDBServiceResponseWrapper.data', index=3,
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
  serialized_start=582,
  serialized_end=710,
)

_LISTDBSERVICERESPONSE_LIST_OWNER.containing_type = _LISTDBSERVICERESPONSE_LIST
_LISTDBSERVICERESPONSE_LIST.fields_by_name['dbInstance'].message_type = database__delivery__sdk_dot_model_dot_database__delivery_dot_dbinstance__pb2._DBINSTANCE
_LISTDBSERVICERESPONSE_LIST.fields_by_name['owner'].message_type = _LISTDBSERVICERESPONSE_LIST_OWNER
_LISTDBSERVICERESPONSE_LIST.containing_type = _LISTDBSERVICERESPONSE
_LISTDBSERVICERESPONSE.fields_by_name['list'].message_type = _LISTDBSERVICERESPONSE_LIST
_LISTDBSERVICERESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTDBSERVICERESPONSE
DESCRIPTOR.message_types_by_name['ListDBServiceRequest'] = _LISTDBSERVICEREQUEST
DESCRIPTOR.message_types_by_name['ListDBServiceResponse'] = _LISTDBSERVICERESPONSE
DESCRIPTOR.message_types_by_name['ListDBServiceResponseWrapper'] = _LISTDBSERVICERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListDBServiceRequest = _reflection.GeneratedProtocolMessageType('ListDBServiceRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTDBSERVICEREQUEST,
  '__module__' : 'list_pb2'
  # @@protoc_insertion_point(class_scope:dbservice.ListDBServiceRequest)
  })
_sym_db.RegisterMessage(ListDBServiceRequest)

ListDBServiceResponse = _reflection.GeneratedProtocolMessageType('ListDBServiceResponse', (_message.Message,), {

  'List' : _reflection.GeneratedProtocolMessageType('List', (_message.Message,), {

    'Owner' : _reflection.GeneratedProtocolMessageType('Owner', (_message.Message,), {
      'DESCRIPTOR' : _LISTDBSERVICERESPONSE_LIST_OWNER,
      '__module__' : 'list_pb2'
      # @@protoc_insertion_point(class_scope:dbservice.ListDBServiceResponse.List.Owner)
      })
    ,
    'DESCRIPTOR' : _LISTDBSERVICERESPONSE_LIST,
    '__module__' : 'list_pb2'
    # @@protoc_insertion_point(class_scope:dbservice.ListDBServiceResponse.List)
    })
  ,
  'DESCRIPTOR' : _LISTDBSERVICERESPONSE,
  '__module__' : 'list_pb2'
  # @@protoc_insertion_point(class_scope:dbservice.ListDBServiceResponse)
  })
_sym_db.RegisterMessage(ListDBServiceResponse)
_sym_db.RegisterMessage(ListDBServiceResponse.List)
_sym_db.RegisterMessage(ListDBServiceResponse.List.Owner)

ListDBServiceResponseWrapper = _reflection.GeneratedProtocolMessageType('ListDBServiceResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _LISTDBSERVICERESPONSEWRAPPER,
  '__module__' : 'list_pb2'
  # @@protoc_insertion_point(class_scope:dbservice.ListDBServiceResponseWrapper)
  })
_sym_db.RegisterMessage(ListDBServiceResponseWrapper)


# @@protoc_insertion_point(module_scope)
