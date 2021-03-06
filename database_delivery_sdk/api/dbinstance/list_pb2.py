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




DESCRIPTOR = _descriptor.FileDescriptor(
  name='list.proto',
  package='dbinstance',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\nlist.proto\x12\ndbinstance\"L\n\x15ListDBInstanceRequest\x12\x13\n\x0b\x64\x62ServiceId\x18\x01 \x01(\t\x12\x0c\n\x04page\x18\x02 \x01(\x05\x12\x10\n\x08pageSize\x18\x03 \x01(\x05\"\x8f\x04\n\x16ListDBInstanceResponse\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12\x35\n\x04list\x18\x04 \x03(\x0b\x32\'.dbinstance.ListDBInstanceResponse.List\x1a\x8d\x03\n\x04List\x12\x44\n\tdbService\x18\x01 \x03(\x0b\x32\x31.dbinstance.ListDBInstanceResponse.List.DbService\x12>\n\x06\x63lient\x18\x02 \x01(\x0b\x32..dbinstance.ListDBInstanceResponse.List.Client\x12\x12\n\ninstanceId\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0e\n\x06\x64\x62Name\x18\x05 \x01(\t\x12\n\n\x02ip\x18\x06 \x01(\t\x12\x0c\n\x04port\x18\x07 \x01(\x05\x12\x0f\n\x07\x63onnURL\x18\x08 \x01(\t\x12\x10\n\x08userName\x18\t \x01(\t\x12\x10\n\x08password\x18\n \x01(\t\x12\x0f\n\x07isValid\x18\x0b \x01(\t\x1aK\n\tDbService\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06\x64\x62Type\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x04 \x01(\t\x1a \n\x06\x43lient\x12\n\n\x02id\x18\x01 \x01(\t\x12\n\n\x02ip\x18\x02 \x01(\t\"\x83\x01\n\x1dListDBInstanceResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x30\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\".dbinstance.ListDBInstanceResponseb\x06proto3')
)




_LISTDBINSTANCEREQUEST = _descriptor.Descriptor(
  name='ListDBInstanceRequest',
  full_name='dbinstance.ListDBInstanceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dbServiceId', full_name='dbinstance.ListDBInstanceRequest.dbServiceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page', full_name='dbinstance.ListDBInstanceRequest.page', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='dbinstance.ListDBInstanceRequest.pageSize', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=26,
  serialized_end=102,
)


_LISTDBINSTANCERESPONSE_LIST_DBSERVICE = _descriptor.Descriptor(
  name='DbService',
  full_name='dbinstance.ListDBInstanceResponse.List.DbService',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='dbinstance.ListDBInstanceResponse.List.DbService.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='dbinstance.ListDBInstanceResponse.List.DbService.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dbType', full_name='dbinstance.ListDBInstanceResponse.List.DbService.dbType', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='desc', full_name='dbinstance.ListDBInstanceResponse.List.DbService.desc', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=523,
  serialized_end=598,
)

_LISTDBINSTANCERESPONSE_LIST_CLIENT = _descriptor.Descriptor(
  name='Client',
  full_name='dbinstance.ListDBInstanceResponse.List.Client',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='dbinstance.ListDBInstanceResponse.List.Client.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip', full_name='dbinstance.ListDBInstanceResponse.List.Client.ip', index=1,
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
  serialized_start=600,
  serialized_end=632,
)

_LISTDBINSTANCERESPONSE_LIST = _descriptor.Descriptor(
  name='List',
  full_name='dbinstance.ListDBInstanceResponse.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dbService', full_name='dbinstance.ListDBInstanceResponse.List.dbService', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client', full_name='dbinstance.ListDBInstanceResponse.List.client', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='dbinstance.ListDBInstanceResponse.List.instanceId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='dbinstance.ListDBInstanceResponse.List.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dbName', full_name='dbinstance.ListDBInstanceResponse.List.dbName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip', full_name='dbinstance.ListDBInstanceResponse.List.ip', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='dbinstance.ListDBInstanceResponse.List.port', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connURL', full_name='dbinstance.ListDBInstanceResponse.List.connURL', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userName', full_name='dbinstance.ListDBInstanceResponse.List.userName', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='dbinstance.ListDBInstanceResponse.List.password', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isValid', full_name='dbinstance.ListDBInstanceResponse.List.isValid', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTDBINSTANCERESPONSE_LIST_DBSERVICE, _LISTDBINSTANCERESPONSE_LIST_CLIENT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=235,
  serialized_end=632,
)

_LISTDBINSTANCERESPONSE = _descriptor.Descriptor(
  name='ListDBInstanceResponse',
  full_name='dbinstance.ListDBInstanceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='dbinstance.ListDBInstanceResponse.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='dbinstance.ListDBInstanceResponse.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='dbinstance.ListDBInstanceResponse.total', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='dbinstance.ListDBInstanceResponse.list', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTDBINSTANCERESPONSE_LIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=632,
)


_LISTDBINSTANCERESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListDBInstanceResponseWrapper',
  full_name='dbinstance.ListDBInstanceResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='dbinstance.ListDBInstanceResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='dbinstance.ListDBInstanceResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dbinstance.ListDBInstanceResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='dbinstance.ListDBInstanceResponseWrapper.data', index=3,
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
  serialized_start=635,
  serialized_end=766,
)

_LISTDBINSTANCERESPONSE_LIST_DBSERVICE.containing_type = _LISTDBINSTANCERESPONSE_LIST
_LISTDBINSTANCERESPONSE_LIST_CLIENT.containing_type = _LISTDBINSTANCERESPONSE_LIST
_LISTDBINSTANCERESPONSE_LIST.fields_by_name['dbService'].message_type = _LISTDBINSTANCERESPONSE_LIST_DBSERVICE
_LISTDBINSTANCERESPONSE_LIST.fields_by_name['client'].message_type = _LISTDBINSTANCERESPONSE_LIST_CLIENT
_LISTDBINSTANCERESPONSE_LIST.containing_type = _LISTDBINSTANCERESPONSE
_LISTDBINSTANCERESPONSE.fields_by_name['list'].message_type = _LISTDBINSTANCERESPONSE_LIST
_LISTDBINSTANCERESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTDBINSTANCERESPONSE
DESCRIPTOR.message_types_by_name['ListDBInstanceRequest'] = _LISTDBINSTANCEREQUEST
DESCRIPTOR.message_types_by_name['ListDBInstanceResponse'] = _LISTDBINSTANCERESPONSE
DESCRIPTOR.message_types_by_name['ListDBInstanceResponseWrapper'] = _LISTDBINSTANCERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListDBInstanceRequest = _reflection.GeneratedProtocolMessageType('ListDBInstanceRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTDBINSTANCEREQUEST,
  '__module__' : 'list_pb2'
  # @@protoc_insertion_point(class_scope:dbinstance.ListDBInstanceRequest)
  })
_sym_db.RegisterMessage(ListDBInstanceRequest)

ListDBInstanceResponse = _reflection.GeneratedProtocolMessageType('ListDBInstanceResponse', (_message.Message,), {

  'List' : _reflection.GeneratedProtocolMessageType('List', (_message.Message,), {

    'DbService' : _reflection.GeneratedProtocolMessageType('DbService', (_message.Message,), {
      'DESCRIPTOR' : _LISTDBINSTANCERESPONSE_LIST_DBSERVICE,
      '__module__' : 'list_pb2'
      # @@protoc_insertion_point(class_scope:dbinstance.ListDBInstanceResponse.List.DbService)
      })
    ,

    'Client' : _reflection.GeneratedProtocolMessageType('Client', (_message.Message,), {
      'DESCRIPTOR' : _LISTDBINSTANCERESPONSE_LIST_CLIENT,
      '__module__' : 'list_pb2'
      # @@protoc_insertion_point(class_scope:dbinstance.ListDBInstanceResponse.List.Client)
      })
    ,
    'DESCRIPTOR' : _LISTDBINSTANCERESPONSE_LIST,
    '__module__' : 'list_pb2'
    # @@protoc_insertion_point(class_scope:dbinstance.ListDBInstanceResponse.List)
    })
  ,
  'DESCRIPTOR' : _LISTDBINSTANCERESPONSE,
  '__module__' : 'list_pb2'
  # @@protoc_insertion_point(class_scope:dbinstance.ListDBInstanceResponse)
  })
_sym_db.RegisterMessage(ListDBInstanceResponse)
_sym_db.RegisterMessage(ListDBInstanceResponse.List)
_sym_db.RegisterMessage(ListDBInstanceResponse.List.DbService)
_sym_db.RegisterMessage(ListDBInstanceResponse.List.Client)

ListDBInstanceResponseWrapper = _reflection.GeneratedProtocolMessageType('ListDBInstanceResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _LISTDBINSTANCERESPONSEWRAPPER,
  '__module__' : 'list_pb2'
  # @@protoc_insertion_point(class_scope:dbinstance.ListDBInstanceResponseWrapper)
  })
_sym_db.RegisterMessage(ListDBInstanceResponseWrapper)


# @@protoc_insertion_point(module_scope)
