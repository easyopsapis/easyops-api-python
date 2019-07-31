# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_trigger.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from model.pipeline import trigger_pb2 as model_dot_pipeline_dot_trigger__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_trigger.proto',
  package='pipeline',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11get_trigger.proto\x12\x08pipeline\x1a\x1cmodel/pipeline/trigger.proto\"\x1f\n\x11GetTriggerRequest\x12\n\n\x02id\x18\x01 \x01(\t\"n\n\x19GetTriggerResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x1f\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x11.pipeline.Triggerb\x06proto3')
  ,
  dependencies=[model_dot_pipeline_dot_trigger__pb2.DESCRIPTOR,])




_GETTRIGGERREQUEST = _descriptor.Descriptor(
  name='GetTriggerRequest',
  full_name='pipeline.GetTriggerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='pipeline.GetTriggerRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=61,
  serialized_end=92,
)


_GETTRIGGERRESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetTriggerResponseWrapper',
  full_name='pipeline.GetTriggerResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='pipeline.GetTriggerResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='pipeline.GetTriggerResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='pipeline.GetTriggerResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='pipeline.GetTriggerResponseWrapper.data', index=3,
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
  serialized_start=94,
  serialized_end=204,
)

_GETTRIGGERRESPONSEWRAPPER.fields_by_name['data'].message_type = model_dot_pipeline_dot_trigger__pb2._TRIGGER
DESCRIPTOR.message_types_by_name['GetTriggerRequest'] = _GETTRIGGERREQUEST
DESCRIPTOR.message_types_by_name['GetTriggerResponseWrapper'] = _GETTRIGGERRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetTriggerRequest = _reflection.GeneratedProtocolMessageType('GetTriggerRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETTRIGGERREQUEST,
  __module__ = 'get_trigger_pb2'
  # @@protoc_insertion_point(class_scope:pipeline.GetTriggerRequest)
  ))
_sym_db.RegisterMessage(GetTriggerRequest)

GetTriggerResponseWrapper = _reflection.GeneratedProtocolMessageType('GetTriggerResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _GETTRIGGERRESPONSEWRAPPER,
  __module__ = 'get_trigger_pb2'
  # @@protoc_insertion_point(class_scope:pipeline.GetTriggerResponseWrapper)
  ))
_sym_db.RegisterMessage(GetTriggerResponseWrapper)


# @@protoc_insertion_point(module_scope)
