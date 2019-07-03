# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: search_one.proto

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
  name='search_one.proto',
  package='mongo',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10search_one.proto\x12\x05mongo\x1a\x1cgoogle/protobuf/struct.proto\"l\n\x10SearchOneRequest\x12\x12\n\ncollection\x18\x01 \x01(\t\x12&\n\x05query\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0e\n\x06\x66ields\x18\x03 \x03(\t\x12\x0c\n\x04sort\x18\x04 \x03(\t\"9\n\x11SearchOneResponse\x12$\n\x03\x64oc\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\"t\n\x18SearchOneResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12&\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x18.mongo.SearchOneResponseb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_SEARCHONEREQUEST = _descriptor.Descriptor(
  name='SearchOneRequest',
  full_name='mongo.SearchOneRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='collection', full_name='mongo.SearchOneRequest.collection', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='query', full_name='mongo.SearchOneRequest.query', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fields', full_name='mongo.SearchOneRequest.fields', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sort', full_name='mongo.SearchOneRequest.sort', index=3,
      number=4, type=9, cpp_type=9, label=3,
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
  serialized_start=57,
  serialized_end=165,
)


_SEARCHONERESPONSE = _descriptor.Descriptor(
  name='SearchOneResponse',
  full_name='mongo.SearchOneResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='doc', full_name='mongo.SearchOneResponse.doc', index=0,
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
  serialized_start=167,
  serialized_end=224,
)


_SEARCHONERESPONSEWRAPPER = _descriptor.Descriptor(
  name='SearchOneResponseWrapper',
  full_name='mongo.SearchOneResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='mongo.SearchOneResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='mongo.SearchOneResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='mongo.SearchOneResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='mongo.SearchOneResponseWrapper.data', index=3,
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
  serialized_start=226,
  serialized_end=342,
)

_SEARCHONEREQUEST.fields_by_name['query'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SEARCHONERESPONSE.fields_by_name['doc'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SEARCHONERESPONSEWRAPPER.fields_by_name['data'].message_type = _SEARCHONERESPONSE
DESCRIPTOR.message_types_by_name['SearchOneRequest'] = _SEARCHONEREQUEST
DESCRIPTOR.message_types_by_name['SearchOneResponse'] = _SEARCHONERESPONSE
DESCRIPTOR.message_types_by_name['SearchOneResponseWrapper'] = _SEARCHONERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SearchOneRequest = _reflection.GeneratedProtocolMessageType('SearchOneRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHONEREQUEST,
  __module__ = 'search_one_pb2'
  # @@protoc_insertion_point(class_scope:mongo.SearchOneRequest)
  ))
_sym_db.RegisterMessage(SearchOneRequest)

SearchOneResponse = _reflection.GeneratedProtocolMessageType('SearchOneResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHONERESPONSE,
  __module__ = 'search_one_pb2'
  # @@protoc_insertion_point(class_scope:mongo.SearchOneResponse)
  ))
_sym_db.RegisterMessage(SearchOneResponse)

SearchOneResponseWrapper = _reflection.GeneratedProtocolMessageType('SearchOneResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHONERESPONSEWRAPPER,
  __module__ = 'search_one_pb2'
  # @@protoc_insertion_point(class_scope:mongo.SearchOneResponseWrapper)
  ))
_sym_db.RegisterMessage(SearchOneResponseWrapper)


# @@protoc_insertion_point(module_scope)