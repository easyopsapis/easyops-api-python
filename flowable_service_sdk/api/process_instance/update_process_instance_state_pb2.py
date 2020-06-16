# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: update_process_instance_state.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='update_process_instance_state.proto',
  package='process_instance',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n#update_process_instance_state.proto\x12\x10process_instance\x1a\x1bgoogle/protobuf/empty.proto\"G\n!UpdateProcessInstanceStateRequest\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x02 \x01(\t\"\x83\x01\n)UpdateProcessInstanceStateResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12$\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x16.google.protobuf.Emptyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_UPDATEPROCESSINSTANCESTATEREQUEST = _descriptor.Descriptor(
  name='UpdateProcessInstanceStateRequest',
  full_name='process_instance.UpdateProcessInstanceStateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='process_instance.UpdateProcessInstanceStateRequest.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='process_instance.UpdateProcessInstanceStateRequest.action', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=86,
  serialized_end=157,
)


_UPDATEPROCESSINSTANCESTATERESPONSEWRAPPER = _descriptor.Descriptor(
  name='UpdateProcessInstanceStateResponseWrapper',
  full_name='process_instance.UpdateProcessInstanceStateResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='process_instance.UpdateProcessInstanceStateResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='process_instance.UpdateProcessInstanceStateResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='process_instance.UpdateProcessInstanceStateResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='process_instance.UpdateProcessInstanceStateResponseWrapper.data', index=3,
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
  serialized_start=160,
  serialized_end=291,
)

_UPDATEPROCESSINSTANCESTATERESPONSEWRAPPER.fields_by_name['data'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
DESCRIPTOR.message_types_by_name['UpdateProcessInstanceStateRequest'] = _UPDATEPROCESSINSTANCESTATEREQUEST
DESCRIPTOR.message_types_by_name['UpdateProcessInstanceStateResponseWrapper'] = _UPDATEPROCESSINSTANCESTATERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateProcessInstanceStateRequest = _reflection.GeneratedProtocolMessageType('UpdateProcessInstanceStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPROCESSINSTANCESTATEREQUEST,
  '__module__' : 'update_process_instance_state_pb2'
  # @@protoc_insertion_point(class_scope:process_instance.UpdateProcessInstanceStateRequest)
  })
_sym_db.RegisterMessage(UpdateProcessInstanceStateRequest)

UpdateProcessInstanceStateResponseWrapper = _reflection.GeneratedProtocolMessageType('UpdateProcessInstanceStateResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPROCESSINSTANCESTATERESPONSEWRAPPER,
  '__module__' : 'update_process_instance_state_pb2'
  # @@protoc_insertion_point(class_scope:process_instance.UpdateProcessInstanceStateResponseWrapper)
  })
_sym_db.RegisterMessage(UpdateProcessInstanceStateResponseWrapper)


# @@protoc_insertion_point(module_scope)
