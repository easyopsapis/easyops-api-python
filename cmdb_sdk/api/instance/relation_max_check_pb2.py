# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: relation_max_check.proto

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
  name='relation_max_check.proto',
  package='instance',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x18relation_max_check.proto\x12\x08instance\x1a\x1cgoogle/protobuf/struct.proto\"\xde\x01\n\x17RelationMaxCheckRequest\x12\x10\n\x08objectId\x18\x01 \x01(\t\x12\x13\n\x0brelation_id\x18\x02 \x01(\t\x12\x18\n\x10relation_side_id\x18\x03 \x01(\t\x12&\n\x05query\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12%\n\x04sort\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x12\n\npermission\x18\x06 \x03(\t\x12\x0c\n\x04page\x18\x07 \x01(\x05\x12\x11\n\tpage_size\x18\x08 \x01(\x05\"\xb7\x01\n\x18RelationMaxCheckResponse\x12\r\n\x05total\x18\x01 \x01(\x05\x12\x0c\n\x04page\x18\x02 \x01(\x05\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x35\n\x04list\x18\x04 \x03(\x0b\x32\'.instance.RelationMaxCheckResponse.List\x1a\x34\n\x04List\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x18\n\x10_relation_is_max\x18\x02 \x01(\x08\"\x85\x01\n\x1fRelationMaxCheckResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x30\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\".instance.RelationMaxCheckResponseb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_RELATIONMAXCHECKREQUEST = _descriptor.Descriptor(
  name='RelationMaxCheckRequest',
  full_name='instance.RelationMaxCheckRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='objectId', full_name='instance.RelationMaxCheckRequest.objectId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relation_id', full_name='instance.RelationMaxCheckRequest.relation_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relation_side_id', full_name='instance.RelationMaxCheckRequest.relation_side_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='query', full_name='instance.RelationMaxCheckRequest.query', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sort', full_name='instance.RelationMaxCheckRequest.sort', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='permission', full_name='instance.RelationMaxCheckRequest.permission', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page', full_name='instance.RelationMaxCheckRequest.page', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='instance.RelationMaxCheckRequest.page_size', index=7,
      number=8, type=5, cpp_type=1, label=1,
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
  serialized_start=69,
  serialized_end=291,
)


_RELATIONMAXCHECKRESPONSE_LIST = _descriptor.Descriptor(
  name='List',
  full_name='instance.RelationMaxCheckResponse.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='instance.RelationMaxCheckResponse.List.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='_relation_is_max', full_name='instance.RelationMaxCheckResponse.List._relation_is_max', index=1,
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
  serialized_start=425,
  serialized_end=477,
)

_RELATIONMAXCHECKRESPONSE = _descriptor.Descriptor(
  name='RelationMaxCheckResponse',
  full_name='instance.RelationMaxCheckResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='total', full_name='instance.RelationMaxCheckResponse.total', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page', full_name='instance.RelationMaxCheckResponse.page', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='instance.RelationMaxCheckResponse.page_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='instance.RelationMaxCheckResponse.list', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_RELATIONMAXCHECKRESPONSE_LIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=294,
  serialized_end=477,
)


_RELATIONMAXCHECKRESPONSEWRAPPER = _descriptor.Descriptor(
  name='RelationMaxCheckResponseWrapper',
  full_name='instance.RelationMaxCheckResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='instance.RelationMaxCheckResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='instance.RelationMaxCheckResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='instance.RelationMaxCheckResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='instance.RelationMaxCheckResponseWrapper.data', index=3,
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
  serialized_start=480,
  serialized_end=613,
)

_RELATIONMAXCHECKREQUEST.fields_by_name['query'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_RELATIONMAXCHECKREQUEST.fields_by_name['sort'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_RELATIONMAXCHECKRESPONSE_LIST.containing_type = _RELATIONMAXCHECKRESPONSE
_RELATIONMAXCHECKRESPONSE.fields_by_name['list'].message_type = _RELATIONMAXCHECKRESPONSE_LIST
_RELATIONMAXCHECKRESPONSEWRAPPER.fields_by_name['data'].message_type = _RELATIONMAXCHECKRESPONSE
DESCRIPTOR.message_types_by_name['RelationMaxCheckRequest'] = _RELATIONMAXCHECKREQUEST
DESCRIPTOR.message_types_by_name['RelationMaxCheckResponse'] = _RELATIONMAXCHECKRESPONSE
DESCRIPTOR.message_types_by_name['RelationMaxCheckResponseWrapper'] = _RELATIONMAXCHECKRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RelationMaxCheckRequest = _reflection.GeneratedProtocolMessageType('RelationMaxCheckRequest', (_message.Message,), {
  'DESCRIPTOR' : _RELATIONMAXCHECKREQUEST,
  '__module__' : 'relation_max_check_pb2'
  # @@protoc_insertion_point(class_scope:instance.RelationMaxCheckRequest)
  })
_sym_db.RegisterMessage(RelationMaxCheckRequest)

RelationMaxCheckResponse = _reflection.GeneratedProtocolMessageType('RelationMaxCheckResponse', (_message.Message,), {

  'List' : _reflection.GeneratedProtocolMessageType('List', (_message.Message,), {
    'DESCRIPTOR' : _RELATIONMAXCHECKRESPONSE_LIST,
    '__module__' : 'relation_max_check_pb2'
    # @@protoc_insertion_point(class_scope:instance.RelationMaxCheckResponse.List)
    })
  ,
  'DESCRIPTOR' : _RELATIONMAXCHECKRESPONSE,
  '__module__' : 'relation_max_check_pb2'
  # @@protoc_insertion_point(class_scope:instance.RelationMaxCheckResponse)
  })
_sym_db.RegisterMessage(RelationMaxCheckResponse)
_sym_db.RegisterMessage(RelationMaxCheckResponse.List)

RelationMaxCheckResponseWrapper = _reflection.GeneratedProtocolMessageType('RelationMaxCheckResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _RELATIONMAXCHECKRESPONSEWRAPPER,
  '__module__' : 'relation_max_check_pb2'
  # @@protoc_insertion_point(class_scope:instance.RelationMaxCheckResponseWrapper)
  })
_sym_db.RegisterMessage(RelationMaxCheckResponseWrapper)


# @@protoc_insertion_point(module_scope)
