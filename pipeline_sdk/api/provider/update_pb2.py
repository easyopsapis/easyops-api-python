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


from model.pipeline import provider_pb2 as model_dot_pipeline_dot_provider__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='update.proto',
  package='provider',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0cupdate.proto\x12\x08provider\x1a\x1dmodel/pipeline/provider.proto\"k\n\x15UpdateResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12 \n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x12.pipeline.Providerb\x06proto3')
  ,
  dependencies=[model_dot_pipeline_dot_provider__pb2.DESCRIPTOR,])




_UPDATERESPONSEWRAPPER = _descriptor.Descriptor(
  name='UpdateResponseWrapper',
  full_name='provider.UpdateResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='provider.UpdateResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='provider.UpdateResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='provider.UpdateResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='provider.UpdateResponseWrapper.data', index=3,
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
  serialized_start=57,
  serialized_end=164,
)

_UPDATERESPONSEWRAPPER.fields_by_name['data'].message_type = model_dot_pipeline_dot_provider__pb2._PROVIDER
DESCRIPTOR.message_types_by_name['UpdateResponseWrapper'] = _UPDATERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateResponseWrapper = _reflection.GeneratedProtocolMessageType('UpdateResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _UPDATERESPONSEWRAPPER,
  __module__ = 'update_pb2'
  # @@protoc_insertion_point(class_scope:provider.UpdateResponseWrapper)
  ))
_sym_db.RegisterMessage(UpdateResponseWrapper)


# @@protoc_insertion_point(module_scope)
