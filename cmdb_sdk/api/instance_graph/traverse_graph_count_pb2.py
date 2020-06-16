# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: traverse_graph_count.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cmdb_sdk.model.cmdb import traverse_child_node_pb2 as cmdb__sdk_dot_model_dot_cmdb_dot_traverse__child__node__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='traverse_graph_count.proto',
  package='instance_graph',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1atraverse_graph_count.proto\x12\x0einstance_graph\x1a-cmdb_sdk/model/cmdb/traverse_child_node.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xa7\x01\n\x19TraverseGraphCountRequest\x12\x11\n\tobject_id\x18\x01 \x01(\t\x12&\n\x05query\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\'\n\x06\x66ields\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12&\n\x05\x63hild\x18\x04 \x03(\x0b\x32\x17.cmdb.TraverseChildNode\"\xba\x01\n\x1aTraverseGraphCountResponse\x12\x11\n\tobject_id\x18\x01 \x01(\t\x12\x12\n\ninstanceId\x18\x02 \x01(\t\x12=\n\x04list\x18\x03 \x03(\x0b\x32/.instance_graph.TraverseGraphCountResponse.List\x1a\x36\n\x04List\x12\x11\n\tobject_id\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\r\n\x05\x63ount\x18\x03 \x01(\x05\"\x8f\x01\n!TraverseGraphCountResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x38\n\x04\x64\x61ta\x18\x04 \x03(\x0b\x32*.instance_graph.TraverseGraphCountResponseb\x06proto3')
  ,
  dependencies=[cmdb__sdk_dot_model_dot_cmdb_dot_traverse__child__node__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_TRAVERSEGRAPHCOUNTREQUEST = _descriptor.Descriptor(
  name='TraverseGraphCountRequest',
  full_name='instance_graph.TraverseGraphCountRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_id', full_name='instance_graph.TraverseGraphCountRequest.object_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='query', full_name='instance_graph.TraverseGraphCountRequest.query', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fields', full_name='instance_graph.TraverseGraphCountRequest.fields', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='child', full_name='instance_graph.TraverseGraphCountRequest.child', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=124,
  serialized_end=291,
)


_TRAVERSEGRAPHCOUNTRESPONSE_LIST = _descriptor.Descriptor(
  name='List',
  full_name='instance_graph.TraverseGraphCountResponse.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_id', full_name='instance_graph.TraverseGraphCountResponse.List.object_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='instance_graph.TraverseGraphCountResponse.List.path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='instance_graph.TraverseGraphCountResponse.List.count', index=2,
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
  serialized_start=426,
  serialized_end=480,
)

_TRAVERSEGRAPHCOUNTRESPONSE = _descriptor.Descriptor(
  name='TraverseGraphCountResponse',
  full_name='instance_graph.TraverseGraphCountResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_id', full_name='instance_graph.TraverseGraphCountResponse.object_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='instance_graph.TraverseGraphCountResponse.instanceId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='instance_graph.TraverseGraphCountResponse.list', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TRAVERSEGRAPHCOUNTRESPONSE_LIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=294,
  serialized_end=480,
)


_TRAVERSEGRAPHCOUNTRESPONSEWRAPPER = _descriptor.Descriptor(
  name='TraverseGraphCountResponseWrapper',
  full_name='instance_graph.TraverseGraphCountResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='instance_graph.TraverseGraphCountResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='instance_graph.TraverseGraphCountResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='instance_graph.TraverseGraphCountResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='instance_graph.TraverseGraphCountResponseWrapper.data', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=483,
  serialized_end=626,
)

_TRAVERSEGRAPHCOUNTREQUEST.fields_by_name['query'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_TRAVERSEGRAPHCOUNTREQUEST.fields_by_name['fields'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_TRAVERSEGRAPHCOUNTREQUEST.fields_by_name['child'].message_type = cmdb__sdk_dot_model_dot_cmdb_dot_traverse__child__node__pb2._TRAVERSECHILDNODE
_TRAVERSEGRAPHCOUNTRESPONSE_LIST.containing_type = _TRAVERSEGRAPHCOUNTRESPONSE
_TRAVERSEGRAPHCOUNTRESPONSE.fields_by_name['list'].message_type = _TRAVERSEGRAPHCOUNTRESPONSE_LIST
_TRAVERSEGRAPHCOUNTRESPONSEWRAPPER.fields_by_name['data'].message_type = _TRAVERSEGRAPHCOUNTRESPONSE
DESCRIPTOR.message_types_by_name['TraverseGraphCountRequest'] = _TRAVERSEGRAPHCOUNTREQUEST
DESCRIPTOR.message_types_by_name['TraverseGraphCountResponse'] = _TRAVERSEGRAPHCOUNTRESPONSE
DESCRIPTOR.message_types_by_name['TraverseGraphCountResponseWrapper'] = _TRAVERSEGRAPHCOUNTRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TraverseGraphCountRequest = _reflection.GeneratedProtocolMessageType('TraverseGraphCountRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRAVERSEGRAPHCOUNTREQUEST,
  '__module__' : 'traverse_graph_count_pb2'
  # @@protoc_insertion_point(class_scope:instance_graph.TraverseGraphCountRequest)
  })
_sym_db.RegisterMessage(TraverseGraphCountRequest)

TraverseGraphCountResponse = _reflection.GeneratedProtocolMessageType('TraverseGraphCountResponse', (_message.Message,), {

  'List' : _reflection.GeneratedProtocolMessageType('List', (_message.Message,), {
    'DESCRIPTOR' : _TRAVERSEGRAPHCOUNTRESPONSE_LIST,
    '__module__' : 'traverse_graph_count_pb2'
    # @@protoc_insertion_point(class_scope:instance_graph.TraverseGraphCountResponse.List)
    })
  ,
  'DESCRIPTOR' : _TRAVERSEGRAPHCOUNTRESPONSE,
  '__module__' : 'traverse_graph_count_pb2'
  # @@protoc_insertion_point(class_scope:instance_graph.TraverseGraphCountResponse)
  })
_sym_db.RegisterMessage(TraverseGraphCountResponse)
_sym_db.RegisterMessage(TraverseGraphCountResponse.List)

TraverseGraphCountResponseWrapper = _reflection.GeneratedProtocolMessageType('TraverseGraphCountResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _TRAVERSEGRAPHCOUNTRESPONSEWRAPPER,
  '__module__' : 'traverse_graph_count_pb2'
  # @@protoc_insertion_point(class_scope:instance_graph.TraverseGraphCountResponseWrapper)
  })
_sym_db.RegisterMessage(TraverseGraphCountResponseWrapper)


# @@protoc_insertion_point(module_scope)
