# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: update.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='update.proto',
  package='dbinstance',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0cupdate.proto\x12\ndbinstance\"\x85\x03\n\x17UpdateDBInstanceRequest\x12\x13\n\x0b\x64\x62ServiceId\x18\x01 \x01(\t\x12\x14\n\x0c\x64\x62InstanceId\x18\x02 \x01(\t\x12N\n\x10updateDbinstance\x18\x03 \x01(\x0b\x32\x34.dbinstance.UpdateDBInstanceRequest.UpdateDbinstance\x1a\xee\x01\n\x10UpdateDbinstance\x12K\n\x06\x63lient\x18\x01 \x01(\x0b\x32;.dbinstance.UpdateDBInstanceRequest.UpdateDbinstance.Client\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06\x64\x62Name\x18\x03 \x01(\t\x12\n\n\x02ip\x18\x04 \x01(\t\x12\x0c\n\x04port\x18\x05 \x01(\x05\x12\x0f\n\x07\x63onnURL\x18\x06 \x01(\t\x12\x10\n\x08userName\x18\x07 \x01(\t\x12\x10\n\x08password\x18\x08 \x01(\t\x1a \n\x06\x43lient\x12\n\n\x02ip\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\"\x9b\x03\n\x18UpdateDBInstanceResponse\x12\x41\n\tdbService\x18\x01 \x03(\x0b\x32..dbinstance.UpdateDBInstanceResponse.DbService\x12;\n\x06\x63lient\x18\x02 \x01(\x0b\x32+.dbinstance.UpdateDBInstanceResponse.Client\x12\x12\n\ninstanceId\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0e\n\x06\x64\x62Name\x18\x05 \x01(\t\x12\n\n\x02ip\x18\x06 \x01(\t\x12\x0c\n\x04port\x18\x07 \x01(\x05\x12\x0f\n\x07\x63onnURL\x18\x08 \x01(\t\x12\x10\n\x08userName\x18\t \x01(\t\x12\x10\n\x08password\x18\n \x01(\t\x12\x0f\n\x07isValid\x18\x0b \x01(\t\x1aK\n\tDbService\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06\x64\x62Type\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x04 \x01(\t\x1a \n\x06\x43lient\x12\n\n\x02id\x18\x01 \x01(\t\x12\n\n\x02ip\x18\x02 \x01(\t\"\x87\x01\n\x1fUpdateDBInstanceResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x32\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32$.dbinstance.UpdateDBInstanceResponseb\x06proto3')
)




_UPDATEDBINSTANCEREQUEST_UPDATEDBINSTANCE_CLIENT = _descriptor.Descriptor(
  name='Client',
  full_name='dbinstance.UpdateDBInstanceRequest.UpdateDbinstance.Client',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='dbinstance.UpdateDBInstanceRequest.UpdateDbinstance.Client.ip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='dbinstance.UpdateDBInstanceRequest.UpdateDbinstance.Client.id', index=1,
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
  serialized_start=386,
  serialized_end=418,
)

_UPDATEDBINSTANCEREQUEST_UPDATEDBINSTANCE = _descriptor.Descriptor(
  name='UpdateDbinstance',
  full_name='dbinstance.UpdateDBInstanceRequest.UpdateDbinstance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client', full_name='dbinstance.UpdateDBInstanceRequest.UpdateDbinstance.client', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='dbinstance.UpdateDBInstanceRequest.UpdateDbinstance.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dbName', full_name='dbinstance.UpdateDBInstanceRequest.UpdateDbinstance.dbName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip', full_name='dbinstance.UpdateDBInstanceRequest.UpdateDbinstance.ip', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='dbinstance.UpdateDBInstanceRequest.UpdateDbinstance.port', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connURL', full_name='dbinstance.UpdateDBInstanceRequest.UpdateDbinstance.connURL', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userName', full_name='dbinstance.UpdateDBInstanceRequest.UpdateDbinstance.userName', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='dbinstance.UpdateDBInstanceRequest.UpdateDbinstance.password', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_UPDATEDBINSTANCEREQUEST_UPDATEDBINSTANCE_CLIENT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=180,
  serialized_end=418,
)

_UPDATEDBINSTANCEREQUEST = _descriptor.Descriptor(
  name='UpdateDBInstanceRequest',
  full_name='dbinstance.UpdateDBInstanceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dbServiceId', full_name='dbinstance.UpdateDBInstanceRequest.dbServiceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dbInstanceId', full_name='dbinstance.UpdateDBInstanceRequest.dbInstanceId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updateDbinstance', full_name='dbinstance.UpdateDBInstanceRequest.updateDbinstance', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_UPDATEDBINSTANCEREQUEST_UPDATEDBINSTANCE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=418,
)


_UPDATEDBINSTANCERESPONSE_DBSERVICE = _descriptor.Descriptor(
  name='DbService',
  full_name='dbinstance.UpdateDBInstanceResponse.DbService',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='dbinstance.UpdateDBInstanceResponse.DbService.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='dbinstance.UpdateDBInstanceResponse.DbService.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dbType', full_name='dbinstance.UpdateDBInstanceResponse.DbService.dbType', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='desc', full_name='dbinstance.UpdateDBInstanceResponse.DbService.desc', index=3,
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
  serialized_start=723,
  serialized_end=798,
)

_UPDATEDBINSTANCERESPONSE_CLIENT = _descriptor.Descriptor(
  name='Client',
  full_name='dbinstance.UpdateDBInstanceResponse.Client',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='dbinstance.UpdateDBInstanceResponse.Client.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip', full_name='dbinstance.UpdateDBInstanceResponse.Client.ip', index=1,
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
  serialized_start=800,
  serialized_end=832,
)

_UPDATEDBINSTANCERESPONSE = _descriptor.Descriptor(
  name='UpdateDBInstanceResponse',
  full_name='dbinstance.UpdateDBInstanceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dbService', full_name='dbinstance.UpdateDBInstanceResponse.dbService', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client', full_name='dbinstance.UpdateDBInstanceResponse.client', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='dbinstance.UpdateDBInstanceResponse.instanceId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='dbinstance.UpdateDBInstanceResponse.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dbName', full_name='dbinstance.UpdateDBInstanceResponse.dbName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip', full_name='dbinstance.UpdateDBInstanceResponse.ip', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='dbinstance.UpdateDBInstanceResponse.port', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connURL', full_name='dbinstance.UpdateDBInstanceResponse.connURL', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userName', full_name='dbinstance.UpdateDBInstanceResponse.userName', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='dbinstance.UpdateDBInstanceResponse.password', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isValid', full_name='dbinstance.UpdateDBInstanceResponse.isValid', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_UPDATEDBINSTANCERESPONSE_DBSERVICE, _UPDATEDBINSTANCERESPONSE_CLIENT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=421,
  serialized_end=832,
)


_UPDATEDBINSTANCERESPONSEWRAPPER = _descriptor.Descriptor(
  name='UpdateDBInstanceResponseWrapper',
  full_name='dbinstance.UpdateDBInstanceResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='dbinstance.UpdateDBInstanceResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='dbinstance.UpdateDBInstanceResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dbinstance.UpdateDBInstanceResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='dbinstance.UpdateDBInstanceResponseWrapper.data', index=3,
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
  serialized_start=835,
  serialized_end=970,
)

_UPDATEDBINSTANCEREQUEST_UPDATEDBINSTANCE_CLIENT.containing_type = _UPDATEDBINSTANCEREQUEST_UPDATEDBINSTANCE
_UPDATEDBINSTANCEREQUEST_UPDATEDBINSTANCE.fields_by_name['client'].message_type = _UPDATEDBINSTANCEREQUEST_UPDATEDBINSTANCE_CLIENT
_UPDATEDBINSTANCEREQUEST_UPDATEDBINSTANCE.containing_type = _UPDATEDBINSTANCEREQUEST
_UPDATEDBINSTANCEREQUEST.fields_by_name['updateDbinstance'].message_type = _UPDATEDBINSTANCEREQUEST_UPDATEDBINSTANCE
_UPDATEDBINSTANCERESPONSE_DBSERVICE.containing_type = _UPDATEDBINSTANCERESPONSE
_UPDATEDBINSTANCERESPONSE_CLIENT.containing_type = _UPDATEDBINSTANCERESPONSE
_UPDATEDBINSTANCERESPONSE.fields_by_name['dbService'].message_type = _UPDATEDBINSTANCERESPONSE_DBSERVICE
_UPDATEDBINSTANCERESPONSE.fields_by_name['client'].message_type = _UPDATEDBINSTANCERESPONSE_CLIENT
_UPDATEDBINSTANCERESPONSEWRAPPER.fields_by_name['data'].message_type = _UPDATEDBINSTANCERESPONSE
DESCRIPTOR.message_types_by_name['UpdateDBInstanceRequest'] = _UPDATEDBINSTANCEREQUEST
DESCRIPTOR.message_types_by_name['UpdateDBInstanceResponse'] = _UPDATEDBINSTANCERESPONSE
DESCRIPTOR.message_types_by_name['UpdateDBInstanceResponseWrapper'] = _UPDATEDBINSTANCERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateDBInstanceRequest = _reflection.GeneratedProtocolMessageType('UpdateDBInstanceRequest', (_message.Message,), dict(

  UpdateDbinstance = _reflection.GeneratedProtocolMessageType('UpdateDbinstance', (_message.Message,), dict(

    Client = _reflection.GeneratedProtocolMessageType('Client', (_message.Message,), dict(
      DESCRIPTOR = _UPDATEDBINSTANCEREQUEST_UPDATEDBINSTANCE_CLIENT,
      __module__ = 'update_pb2'
      # @@protoc_insertion_point(class_scope:dbinstance.UpdateDBInstanceRequest.UpdateDbinstance.Client)
      ))
    ,
    DESCRIPTOR = _UPDATEDBINSTANCEREQUEST_UPDATEDBINSTANCE,
    __module__ = 'update_pb2'
    # @@protoc_insertion_point(class_scope:dbinstance.UpdateDBInstanceRequest.UpdateDbinstance)
    ))
  ,
  DESCRIPTOR = _UPDATEDBINSTANCEREQUEST,
  __module__ = 'update_pb2'
  # @@protoc_insertion_point(class_scope:dbinstance.UpdateDBInstanceRequest)
  ))
_sym_db.RegisterMessage(UpdateDBInstanceRequest)
_sym_db.RegisterMessage(UpdateDBInstanceRequest.UpdateDbinstance)
_sym_db.RegisterMessage(UpdateDBInstanceRequest.UpdateDbinstance.Client)

UpdateDBInstanceResponse = _reflection.GeneratedProtocolMessageType('UpdateDBInstanceResponse', (_message.Message,), dict(

  DbService = _reflection.GeneratedProtocolMessageType('DbService', (_message.Message,), dict(
    DESCRIPTOR = _UPDATEDBINSTANCERESPONSE_DBSERVICE,
    __module__ = 'update_pb2'
    # @@protoc_insertion_point(class_scope:dbinstance.UpdateDBInstanceResponse.DbService)
    ))
  ,

  Client = _reflection.GeneratedProtocolMessageType('Client', (_message.Message,), dict(
    DESCRIPTOR = _UPDATEDBINSTANCERESPONSE_CLIENT,
    __module__ = 'update_pb2'
    # @@protoc_insertion_point(class_scope:dbinstance.UpdateDBInstanceResponse.Client)
    ))
  ,
  DESCRIPTOR = _UPDATEDBINSTANCERESPONSE,
  __module__ = 'update_pb2'
  # @@protoc_insertion_point(class_scope:dbinstance.UpdateDBInstanceResponse)
  ))
_sym_db.RegisterMessage(UpdateDBInstanceResponse)
_sym_db.RegisterMessage(UpdateDBInstanceResponse.DbService)
_sym_db.RegisterMessage(UpdateDBInstanceResponse.Client)

UpdateDBInstanceResponseWrapper = _reflection.GeneratedProtocolMessageType('UpdateDBInstanceResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEDBINSTANCERESPONSEWRAPPER,
  __module__ = 'update_pb2'
  # @@protoc_insertion_point(class_scope:dbinstance.UpdateDBInstanceResponseWrapper)
  ))
_sym_db.RegisterMessage(UpdateDBInstanceResponseWrapper)


# @@protoc_insertion_point(module_scope)