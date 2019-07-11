# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app_pipeline.proto

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
  name='app_pipeline.proto',
  package='cmdb_extend',
  syntax='proto3',
  serialized_options=_b('ZEgo.easyops.local/contracts/protorepo-models/easyops/model/cmdb_extend'),
  serialized_pb=_b('\n\x12\x61pp_pipeline.proto\x12\x0b\x63mdb_extend\x1a\x1cgoogle/protobuf/struct.proto\"\x82\x02\n\x0b\x41ppPipeline\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\x12\x0e\n\x06\x66lowId\x18\x03 \x01(\t\x12\x13\n\x0b\x66lowVersion\x18\x04 \x01(\x05\x12\x12\n\ntemplateId\x18\x05 \x01(\t\x12\x17\n\x0ftemplateVersion\x18\x06 \x01(\x05\x12\x13\n\x0bsubscribers\x18\x07 \x03(\t\x12\x19\n\x11subscribedChannel\x18\x08 \x01(\t\x12&\n\x05rules\x18\t \x01(\x0b\x32\x17.google.protobuf.Struct\x12)\n\x08metadata\x18\n \x01(\x0b\x32\x17.google.protobuf.StructBGZEgo.easyops.local/contracts/protorepo-models/easyops/model/cmdb_extendb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_APPPIPELINE = _descriptor.Descriptor(
  name='AppPipeline',
  full_name='cmdb_extend.AppPipeline',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cmdb_extend.AppPipeline.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='cmdb_extend.AppPipeline.category', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flowId', full_name='cmdb_extend.AppPipeline.flowId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flowVersion', full_name='cmdb_extend.AppPipeline.flowVersion', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='templateId', full_name='cmdb_extend.AppPipeline.templateId', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='templateVersion', full_name='cmdb_extend.AppPipeline.templateVersion', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subscribers', full_name='cmdb_extend.AppPipeline.subscribers', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subscribedChannel', full_name='cmdb_extend.AppPipeline.subscribedChannel', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rules', full_name='cmdb_extend.AppPipeline.rules', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='cmdb_extend.AppPipeline.metadata', index=9,
      number=10, type=11, cpp_type=10, label=1,
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
  serialized_start=66,
  serialized_end=324,
)

_APPPIPELINE.fields_by_name['rules'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_APPPIPELINE.fields_by_name['metadata'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['AppPipeline'] = _APPPIPELINE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AppPipeline = _reflection.GeneratedProtocolMessageType('AppPipeline', (_message.Message,), dict(
  DESCRIPTOR = _APPPIPELINE,
  __module__ = 'app_pipeline_pb2'
  # @@protoc_insertion_point(class_scope:cmdb_extend.AppPipeline)
  ))
_sym_db.RegisterMessage(AppPipeline)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)