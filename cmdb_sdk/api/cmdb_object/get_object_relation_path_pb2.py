# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_object_relation_path.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cmdb_sdk.model.cmdb import strategy_path_node_basic_pb2 as cmdb__sdk_dot_model_dot_cmdb_dot_strategy__path__node__basic__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_object_relation_path.proto',
  package='cmdb_object',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1eget_object_relation_path.proto\x12\x0b\x63mdb_object\x1a\x32\x63mdb_sdk/model/cmdb/strategy_path_node_basic.proto\"\xb1\x01\n\x1cGetObjectRelationPathRequest\x12\x15\n\rsrc_object_id\x18\x01 \x01(\t\x12\x15\n\rdst_object_id\x18\x02 \x01(\t\x12\x11\n\tmax_depth\x18\x03 \x01(\x05\x12\x14\n\x0cmax_sub_node\x18\x04 \x01(\x05\x12\x12\n\nwith_cycle\x18\x05 \x01(\x08\x12\x12\n\nwhite_list\x18\x06 \x01(\t\x12\x12\n\nblack_list\x18\x07 \x01(\t\"\xda\x01\n\x1dGetObjectRelationPathResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\r\n\x05\x65rror\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\x12=\n\x04\x64\x61ta\x18\x04 \x03(\x0b\x32/.cmdb_object.GetObjectRelationPathResponse.Data\x1aL\n\x04\x44\x61ta\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12)\n\x04path\x18\x03 \x03(\x0b\x32\x1b.cmdb.StrategyPathNodeBasic\"\x92\x01\n$GetObjectRelationPathResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x38\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32*.cmdb_object.GetObjectRelationPathResponseb\x06proto3')
  ,
  dependencies=[cmdb__sdk_dot_model_dot_cmdb_dot_strategy__path__node__basic__pb2.DESCRIPTOR,])




_GETOBJECTRELATIONPATHREQUEST = _descriptor.Descriptor(
  name='GetObjectRelationPathRequest',
  full_name='cmdb_object.GetObjectRelationPathRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='src_object_id', full_name='cmdb_object.GetObjectRelationPathRequest.src_object_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dst_object_id', full_name='cmdb_object.GetObjectRelationPathRequest.dst_object_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_depth', full_name='cmdb_object.GetObjectRelationPathRequest.max_depth', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_sub_node', full_name='cmdb_object.GetObjectRelationPathRequest.max_sub_node', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='with_cycle', full_name='cmdb_object.GetObjectRelationPathRequest.with_cycle', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='white_list', full_name='cmdb_object.GetObjectRelationPathRequest.white_list', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='black_list', full_name='cmdb_object.GetObjectRelationPathRequest.black_list', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=100,
  serialized_end=277,
)


_GETOBJECTRELATIONPATHRESPONSE_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='cmdb_object.GetObjectRelationPathResponse.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cmdb_object.GetObjectRelationPathResponse.Data.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='label', full_name='cmdb_object.GetObjectRelationPathResponse.Data.label', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='cmdb_object.GetObjectRelationPathResponse.Data.path', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=422,
  serialized_end=498,
)

_GETOBJECTRELATIONPATHRESPONSE = _descriptor.Descriptor(
  name='GetObjectRelationPathResponse',
  full_name='cmdb_object.GetObjectRelationPathResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='cmdb_object.GetObjectRelationPathResponse.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='cmdb_object.GetObjectRelationPathResponse.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='cmdb_object.GetObjectRelationPathResponse.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='cmdb_object.GetObjectRelationPathResponse.data', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETOBJECTRELATIONPATHRESPONSE_DATA, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=280,
  serialized_end=498,
)


_GETOBJECTRELATIONPATHRESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetObjectRelationPathResponseWrapper',
  full_name='cmdb_object.GetObjectRelationPathResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='cmdb_object.GetObjectRelationPathResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='cmdb_object.GetObjectRelationPathResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='cmdb_object.GetObjectRelationPathResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='cmdb_object.GetObjectRelationPathResponseWrapper.data', index=3,
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
  serialized_start=501,
  serialized_end=647,
)

_GETOBJECTRELATIONPATHRESPONSE_DATA.fields_by_name['path'].message_type = cmdb__sdk_dot_model_dot_cmdb_dot_strategy__path__node__basic__pb2._STRATEGYPATHNODEBASIC
_GETOBJECTRELATIONPATHRESPONSE_DATA.containing_type = _GETOBJECTRELATIONPATHRESPONSE
_GETOBJECTRELATIONPATHRESPONSE.fields_by_name['data'].message_type = _GETOBJECTRELATIONPATHRESPONSE_DATA
_GETOBJECTRELATIONPATHRESPONSEWRAPPER.fields_by_name['data'].message_type = _GETOBJECTRELATIONPATHRESPONSE
DESCRIPTOR.message_types_by_name['GetObjectRelationPathRequest'] = _GETOBJECTRELATIONPATHREQUEST
DESCRIPTOR.message_types_by_name['GetObjectRelationPathResponse'] = _GETOBJECTRELATIONPATHRESPONSE
DESCRIPTOR.message_types_by_name['GetObjectRelationPathResponseWrapper'] = _GETOBJECTRELATIONPATHRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetObjectRelationPathRequest = _reflection.GeneratedProtocolMessageType('GetObjectRelationPathRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETOBJECTRELATIONPATHREQUEST,
  '__module__' : 'get_object_relation_path_pb2'
  # @@protoc_insertion_point(class_scope:cmdb_object.GetObjectRelationPathRequest)
  })
_sym_db.RegisterMessage(GetObjectRelationPathRequest)

GetObjectRelationPathResponse = _reflection.GeneratedProtocolMessageType('GetObjectRelationPathResponse', (_message.Message,), {

  'Data' : _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), {
    'DESCRIPTOR' : _GETOBJECTRELATIONPATHRESPONSE_DATA,
    '__module__' : 'get_object_relation_path_pb2'
    # @@protoc_insertion_point(class_scope:cmdb_object.GetObjectRelationPathResponse.Data)
    })
  ,
  'DESCRIPTOR' : _GETOBJECTRELATIONPATHRESPONSE,
  '__module__' : 'get_object_relation_path_pb2'
  # @@protoc_insertion_point(class_scope:cmdb_object.GetObjectRelationPathResponse)
  })
_sym_db.RegisterMessage(GetObjectRelationPathResponse)
_sym_db.RegisterMessage(GetObjectRelationPathResponse.Data)

GetObjectRelationPathResponseWrapper = _reflection.GeneratedProtocolMessageType('GetObjectRelationPathResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _GETOBJECTRELATIONPATHRESPONSEWRAPPER,
  '__module__' : 'get_object_relation_path_pb2'
  # @@protoc_insertion_point(class_scope:cmdb_object.GetObjectRelationPathResponseWrapper)
  })
_sym_db.RegisterMessage(GetObjectRelationPathResponseWrapper)


# @@protoc_insertion_point(module_scope)
