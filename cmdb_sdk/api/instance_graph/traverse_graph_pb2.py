# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: traverse_graph.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from model.cmdb import traverse_child_node_pb2 as model_dot_cmdb_dot_traverse__child__node__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='traverse_graph.proto',
  package='instance_graph',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14traverse_graph.proto\x12\x0einstance_graph\x1a$model/cmdb/traverse_child_node.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xa2\x01\n\x14TraverseGraphRequest\x12\x11\n\tobject_id\x18\x01 \x01(\t\x12&\n\x05query\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\'\n\x06\x66ields\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12&\n\x05\x63hild\x18\x04 \x03(\x0b\x32\x17.cmdb.TraverseChildNode\"\xe6\x01\n\x15TraverseGraphResponse\x12/\n\x0etopic_vertices\x18\x01 \x03(\x0b\x32\x17.google.protobuf.Struct\x12)\n\x08vertices\x18\x02 \x03(\x0b\x32\x17.google.protobuf.Struct\x12:\n\x05\x65\x64ges\x18\x03 \x03(\x0b\x32+.instance_graph.TraverseGraphResponse.Edges\x1a\x35\n\x05\x45\x64ges\x12\x13\n\x0brelation_id\x18\x01 \x01(\t\x12\x0b\n\x03out\x18\x02 \x01(\t\x12\n\n\x02in\x18\x03 \x01(\t\"\x85\x01\n\x1cTraverseGraphResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x33\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32%.instance_graph.TraverseGraphResponseb\x06proto3')
  ,
  dependencies=[model_dot_cmdb_dot_traverse__child__node__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_TRAVERSEGRAPHREQUEST = _descriptor.Descriptor(
  name='TraverseGraphRequest',
  full_name='instance_graph.TraverseGraphRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_id', full_name='instance_graph.TraverseGraphRequest.object_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='query', full_name='instance_graph.TraverseGraphRequest.query', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fields', full_name='instance_graph.TraverseGraphRequest.fields', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='child', full_name='instance_graph.TraverseGraphRequest.child', index=3,
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
  serialized_start=109,
  serialized_end=271,
)


_TRAVERSEGRAPHRESPONSE_EDGES = _descriptor.Descriptor(
  name='Edges',
  full_name='instance_graph.TraverseGraphResponse.Edges',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='relation_id', full_name='instance_graph.TraverseGraphResponse.Edges.relation_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='out', full_name='instance_graph.TraverseGraphResponse.Edges.out', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='in', full_name='instance_graph.TraverseGraphResponse.Edges.in', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=451,
  serialized_end=504,
)

_TRAVERSEGRAPHRESPONSE = _descriptor.Descriptor(
  name='TraverseGraphResponse',
  full_name='instance_graph.TraverseGraphResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='topic_vertices', full_name='instance_graph.TraverseGraphResponse.topic_vertices', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vertices', full_name='instance_graph.TraverseGraphResponse.vertices', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='edges', full_name='instance_graph.TraverseGraphResponse.edges', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TRAVERSEGRAPHRESPONSE_EDGES, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=274,
  serialized_end=504,
)


_TRAVERSEGRAPHRESPONSEWRAPPER = _descriptor.Descriptor(
  name='TraverseGraphResponseWrapper',
  full_name='instance_graph.TraverseGraphResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='instance_graph.TraverseGraphResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='instance_graph.TraverseGraphResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='instance_graph.TraverseGraphResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='instance_graph.TraverseGraphResponseWrapper.data', index=3,
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
  serialized_start=507,
  serialized_end=640,
)

_TRAVERSEGRAPHREQUEST.fields_by_name['query'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_TRAVERSEGRAPHREQUEST.fields_by_name['fields'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_TRAVERSEGRAPHREQUEST.fields_by_name['child'].message_type = model_dot_cmdb_dot_traverse__child__node__pb2._TRAVERSECHILDNODE
_TRAVERSEGRAPHRESPONSE_EDGES.containing_type = _TRAVERSEGRAPHRESPONSE
_TRAVERSEGRAPHRESPONSE.fields_by_name['topic_vertices'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_TRAVERSEGRAPHRESPONSE.fields_by_name['vertices'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_TRAVERSEGRAPHRESPONSE.fields_by_name['edges'].message_type = _TRAVERSEGRAPHRESPONSE_EDGES
_TRAVERSEGRAPHRESPONSEWRAPPER.fields_by_name['data'].message_type = _TRAVERSEGRAPHRESPONSE
DESCRIPTOR.message_types_by_name['TraverseGraphRequest'] = _TRAVERSEGRAPHREQUEST
DESCRIPTOR.message_types_by_name['TraverseGraphResponse'] = _TRAVERSEGRAPHRESPONSE
DESCRIPTOR.message_types_by_name['TraverseGraphResponseWrapper'] = _TRAVERSEGRAPHRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TraverseGraphRequest = _reflection.GeneratedProtocolMessageType('TraverseGraphRequest', (_message.Message,), dict(
  DESCRIPTOR = _TRAVERSEGRAPHREQUEST,
  __module__ = 'traverse_graph_pb2'
  # @@protoc_insertion_point(class_scope:instance_graph.TraverseGraphRequest)
  ))
_sym_db.RegisterMessage(TraverseGraphRequest)

TraverseGraphResponse = _reflection.GeneratedProtocolMessageType('TraverseGraphResponse', (_message.Message,), dict(

  Edges = _reflection.GeneratedProtocolMessageType('Edges', (_message.Message,), dict(
    DESCRIPTOR = _TRAVERSEGRAPHRESPONSE_EDGES,
    __module__ = 'traverse_graph_pb2'
    # @@protoc_insertion_point(class_scope:instance_graph.TraverseGraphResponse.Edges)
    ))
  ,
  DESCRIPTOR = _TRAVERSEGRAPHRESPONSE,
  __module__ = 'traverse_graph_pb2'
  # @@protoc_insertion_point(class_scope:instance_graph.TraverseGraphResponse)
  ))
_sym_db.RegisterMessage(TraverseGraphResponse)
_sym_db.RegisterMessage(TraverseGraphResponse.Edges)

TraverseGraphResponseWrapper = _reflection.GeneratedProtocolMessageType('TraverseGraphResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _TRAVERSEGRAPHRESPONSEWRAPPER,
  __module__ = 'traverse_graph_pb2'
  # @@protoc_insertion_point(class_scope:instance_graph.TraverseGraphResponseWrapper)
  ))
_sym_db.RegisterMessage(TraverseGraphResponseWrapper)


# @@protoc_insertion_point(module_scope)