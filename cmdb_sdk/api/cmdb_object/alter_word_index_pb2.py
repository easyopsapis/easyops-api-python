# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: alter_word_index.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cmdb_sdk.model.cmdb import object_attr_pb2 as cmdb__sdk_dot_model_dot_cmdb_dot_object__attr__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='alter_word_index.proto',
  package='cmdb_object',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16\x61lter_word_index.proto\x12\x0b\x63mdb_object\x1a%cmdb_sdk/model/cmdb/object_attr.proto\x1a\x1bgoogle/protobuf/empty.proto\"\xa6\x01\n\x15\x41lertWordIndexRequest\x12\x11\n\tobject_id\x18\x01 \x01(\t\x12\x35\n\x04\x62ody\x18\x02 \x01(\x0b\x32\'.cmdb_object.AlertWordIndexRequest.Body\x1a\x43\n\x04\x42ody\x12\x17\n\x0fwordIndexDenied\x18\x01 \x01(\x08\x12\"\n\x08\x61ttrList\x18\x02 \x03(\x0b\x32\x10.cmdb.ObjectAttr\"w\n\x1d\x41lertWordIndexResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12$\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x16.google.protobuf.Emptyb\x06proto3')
  ,
  dependencies=[cmdb__sdk_dot_model_dot_cmdb_dot_object__attr__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_ALERTWORDINDEXREQUEST_BODY = _descriptor.Descriptor(
  name='Body',
  full_name='cmdb_object.AlertWordIndexRequest.Body',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='wordIndexDenied', full_name='cmdb_object.AlertWordIndexRequest.Body.wordIndexDenied', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attrList', full_name='cmdb_object.AlertWordIndexRequest.Body.attrList', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=207,
  serialized_end=274,
)

_ALERTWORDINDEXREQUEST = _descriptor.Descriptor(
  name='AlertWordIndexRequest',
  full_name='cmdb_object.AlertWordIndexRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_id', full_name='cmdb_object.AlertWordIndexRequest.object_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='body', full_name='cmdb_object.AlertWordIndexRequest.body', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ALERTWORDINDEXREQUEST_BODY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=108,
  serialized_end=274,
)


_ALERTWORDINDEXRESPONSEWRAPPER = _descriptor.Descriptor(
  name='AlertWordIndexResponseWrapper',
  full_name='cmdb_object.AlertWordIndexResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='cmdb_object.AlertWordIndexResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='cmdb_object.AlertWordIndexResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='cmdb_object.AlertWordIndexResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='cmdb_object.AlertWordIndexResponseWrapper.data', index=3,
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
  serialized_start=276,
  serialized_end=395,
)

_ALERTWORDINDEXREQUEST_BODY.fields_by_name['attrList'].message_type = cmdb__sdk_dot_model_dot_cmdb_dot_object__attr__pb2._OBJECTATTR
_ALERTWORDINDEXREQUEST_BODY.containing_type = _ALERTWORDINDEXREQUEST
_ALERTWORDINDEXREQUEST.fields_by_name['body'].message_type = _ALERTWORDINDEXREQUEST_BODY
_ALERTWORDINDEXRESPONSEWRAPPER.fields_by_name['data'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
DESCRIPTOR.message_types_by_name['AlertWordIndexRequest'] = _ALERTWORDINDEXREQUEST
DESCRIPTOR.message_types_by_name['AlertWordIndexResponseWrapper'] = _ALERTWORDINDEXRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AlertWordIndexRequest = _reflection.GeneratedProtocolMessageType('AlertWordIndexRequest', (_message.Message,), {

  'Body' : _reflection.GeneratedProtocolMessageType('Body', (_message.Message,), {
    'DESCRIPTOR' : _ALERTWORDINDEXREQUEST_BODY,
    '__module__' : 'alter_word_index_pb2'
    # @@protoc_insertion_point(class_scope:cmdb_object.AlertWordIndexRequest.Body)
    })
  ,
  'DESCRIPTOR' : _ALERTWORDINDEXREQUEST,
  '__module__' : 'alter_word_index_pb2'
  # @@protoc_insertion_point(class_scope:cmdb_object.AlertWordIndexRequest)
  })
_sym_db.RegisterMessage(AlertWordIndexRequest)
_sym_db.RegisterMessage(AlertWordIndexRequest.Body)

AlertWordIndexResponseWrapper = _reflection.GeneratedProtocolMessageType('AlertWordIndexResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _ALERTWORDINDEXRESPONSEWRAPPER,
  '__module__' : 'alter_word_index_pb2'
  # @@protoc_insertion_point(class_scope:cmdb_object.AlertWordIndexResponseWrapper)
  })
_sym_db.RegisterMessage(AlertWordIndexResponseWrapper)


# @@protoc_insertion_point(module_scope)
