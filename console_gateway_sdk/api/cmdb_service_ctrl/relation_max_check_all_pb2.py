# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: relation_max_check_all.proto

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
  name='relation_max_check_all.proto',
  package='cmdb_service_ctrl',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1crelation_max_check_all.proto\x12\x11\x63mdb_service_ctrl\x1a\x1cgoogle/protobuf/struct.proto\"\xc0\x01\n\x1aRelationMaxCheckAllRequest\x12\x10\n\x08objectId\x18\x01 \x01(\t\x12\x13\n\x0brelation_id\x18\x02 \x01(\t\x12\x18\n\x10relation_side_id\x18\x03 \x01(\t\x12&\n\x05query\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12%\n\x04sort\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x12\n\npermission\x18\x06 \x03(\t\"\xc4\x01\n\x1bRelationMaxCheckAllResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\r\n\x05\x65rror\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\x12\x41\n\x04\x64\x61ta\x18\x04 \x03(\x0b\x32\x33.cmdb_service_ctrl.RelationMaxCheckAllResponse.Data\x1a\x34\n\x04\x44\x61ta\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x18\n\x10_relation_is_max\x18\x02 \x01(\x08\"\x94\x01\n\"RelationMaxCheckAllResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12<\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32..cmdb_service_ctrl.RelationMaxCheckAllResponseb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_RELATIONMAXCHECKALLREQUEST = _descriptor.Descriptor(
  name='RelationMaxCheckAllRequest',
  full_name='cmdb_service_ctrl.RelationMaxCheckAllRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='objectId', full_name='cmdb_service_ctrl.RelationMaxCheckAllRequest.objectId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relation_id', full_name='cmdb_service_ctrl.RelationMaxCheckAllRequest.relation_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relation_side_id', full_name='cmdb_service_ctrl.RelationMaxCheckAllRequest.relation_side_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='query', full_name='cmdb_service_ctrl.RelationMaxCheckAllRequest.query', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sort', full_name='cmdb_service_ctrl.RelationMaxCheckAllRequest.sort', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='permission', full_name='cmdb_service_ctrl.RelationMaxCheckAllRequest.permission', index=5,
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
  serialized_start=82,
  serialized_end=274,
)


_RELATIONMAXCHECKALLRESPONSE_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='cmdb_service_ctrl.RelationMaxCheckAllResponse.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='cmdb_service_ctrl.RelationMaxCheckAllResponse.Data.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='_relation_is_max', full_name='cmdb_service_ctrl.RelationMaxCheckAllResponse.Data._relation_is_max', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=421,
  serialized_end=473,
)

_RELATIONMAXCHECKALLRESPONSE = _descriptor.Descriptor(
  name='RelationMaxCheckAllResponse',
  full_name='cmdb_service_ctrl.RelationMaxCheckAllResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='cmdb_service_ctrl.RelationMaxCheckAllResponse.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='cmdb_service_ctrl.RelationMaxCheckAllResponse.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='cmdb_service_ctrl.RelationMaxCheckAllResponse.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='cmdb_service_ctrl.RelationMaxCheckAllResponse.data', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_RELATIONMAXCHECKALLRESPONSE_DATA, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=277,
  serialized_end=473,
)


_RELATIONMAXCHECKALLRESPONSEWRAPPER = _descriptor.Descriptor(
  name='RelationMaxCheckAllResponseWrapper',
  full_name='cmdb_service_ctrl.RelationMaxCheckAllResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='cmdb_service_ctrl.RelationMaxCheckAllResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='cmdb_service_ctrl.RelationMaxCheckAllResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='cmdb_service_ctrl.RelationMaxCheckAllResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='cmdb_service_ctrl.RelationMaxCheckAllResponseWrapper.data', index=3,
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
  serialized_start=476,
  serialized_end=624,
)

_RELATIONMAXCHECKALLREQUEST.fields_by_name['query'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_RELATIONMAXCHECKALLREQUEST.fields_by_name['sort'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_RELATIONMAXCHECKALLRESPONSE_DATA.containing_type = _RELATIONMAXCHECKALLRESPONSE
_RELATIONMAXCHECKALLRESPONSE.fields_by_name['data'].message_type = _RELATIONMAXCHECKALLRESPONSE_DATA
_RELATIONMAXCHECKALLRESPONSEWRAPPER.fields_by_name['data'].message_type = _RELATIONMAXCHECKALLRESPONSE
DESCRIPTOR.message_types_by_name['RelationMaxCheckAllRequest'] = _RELATIONMAXCHECKALLREQUEST
DESCRIPTOR.message_types_by_name['RelationMaxCheckAllResponse'] = _RELATIONMAXCHECKALLRESPONSE
DESCRIPTOR.message_types_by_name['RelationMaxCheckAllResponseWrapper'] = _RELATIONMAXCHECKALLRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RelationMaxCheckAllRequest = _reflection.GeneratedProtocolMessageType('RelationMaxCheckAllRequest', (_message.Message,), {
  'DESCRIPTOR' : _RELATIONMAXCHECKALLREQUEST,
  '__module__' : 'relation_max_check_all_pb2'
  # @@protoc_insertion_point(class_scope:cmdb_service_ctrl.RelationMaxCheckAllRequest)
  })
_sym_db.RegisterMessage(RelationMaxCheckAllRequest)

RelationMaxCheckAllResponse = _reflection.GeneratedProtocolMessageType('RelationMaxCheckAllResponse', (_message.Message,), {

  'Data' : _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), {
    'DESCRIPTOR' : _RELATIONMAXCHECKALLRESPONSE_DATA,
    '__module__' : 'relation_max_check_all_pb2'
    # @@protoc_insertion_point(class_scope:cmdb_service_ctrl.RelationMaxCheckAllResponse.Data)
    })
  ,
  'DESCRIPTOR' : _RELATIONMAXCHECKALLRESPONSE,
  '__module__' : 'relation_max_check_all_pb2'
  # @@protoc_insertion_point(class_scope:cmdb_service_ctrl.RelationMaxCheckAllResponse)
  })
_sym_db.RegisterMessage(RelationMaxCheckAllResponse)
_sym_db.RegisterMessage(RelationMaxCheckAllResponse.Data)

RelationMaxCheckAllResponseWrapper = _reflection.GeneratedProtocolMessageType('RelationMaxCheckAllResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _RELATIONMAXCHECKALLRESPONSEWRAPPER,
  '__module__' : 'relation_max_check_all_pb2'
  # @@protoc_insertion_point(class_scope:cmdb_service_ctrl.RelationMaxCheckAllResponseWrapper)
  })
_sym_db.RegisterMessage(RelationMaxCheckAllResponseWrapper)


# @@protoc_insertion_point(module_scope)
