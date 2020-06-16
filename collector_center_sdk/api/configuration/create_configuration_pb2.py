# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: create_configuration.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from collector_center_sdk.model.collector_center import script_pb2 as collector__center__sdk_dot_model_dot_collector__center_dot_script__pb2
from collector_center_sdk.model.collector_center import target_range_pb2 as collector__center__sdk_dot_model_dot_collector__center_dot_target__range__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='create_configuration.proto',
  package='configuration',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1a\x63reate_configuration.proto\x12\rconfiguration\x1a\x38\x63ollector_center_sdk/model/collector_center/script.proto\x1a>collector_center_sdk/model/collector_center/target_range.proto\x1a\x1cgoogle/protobuf/struct.proto\"\x94\x03\n\x1a\x43reateConfigurationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12&\n\x06kwargs\x18\x02 \x01(\x0b\x32\x16.google.protobuf.Value\x12\x0f\n\x07timeout\x18\x03 \x01(\x05\x12#\n\x03\x65nv\x18\x04 \x01(\x0b\x32\x16.google.protobuf.Value\x12\x10\n\x08\x64isabled\x18\x05 \x01(\x08\x12\x0e\n\x06labels\x18\x06 \x03(\t\x12(\n\x06script\x18\x07 \x01(\x0b\x32\x18.collector_center.Script\x12\x15\n\rignoreInvalid\x18\x08 \x01(\x08\x12\x32\n\x0btargetRange\x18\t \x01(\x0b\x32\x1d.collector_center.TargetRange\x12\x10\n\x08interval\x18\n \x01(\x05\x12\x10\n\x08\x63\x61\x63heTtl\x18\x0b \x01(\x05\x12\x11\n\ttimeRange\x18\x0c \x01(\t\x12\x11\n\tclazzName\x18\r \x01(\t\x12\x10\n\x08objectId\x18\x0e \x01(\t\x12\x17\n\x0finstanceIdMacro\x18\x0f \x01(\t\")\n\x1b\x43reateConfigurationResponse\x12\n\n\x02id\x18\x01 \x01(\t\"\x90\x01\n\"CreateConfigurationResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x38\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32*.configuration.CreateConfigurationResponseb\x06proto3')
  ,
  dependencies=[collector__center__sdk_dot_model_dot_collector__center_dot_script__pb2.DESCRIPTOR,collector__center__sdk_dot_model_dot_collector__center_dot_target__range__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_CREATECONFIGURATIONREQUEST = _descriptor.Descriptor(
  name='CreateConfigurationRequest',
  full_name='configuration.CreateConfigurationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='configuration.CreateConfigurationRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kwargs', full_name='configuration.CreateConfigurationRequest.kwargs', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='configuration.CreateConfigurationRequest.timeout', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='env', full_name='configuration.CreateConfigurationRequest.env', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disabled', full_name='configuration.CreateConfigurationRequest.disabled', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='configuration.CreateConfigurationRequest.labels', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='script', full_name='configuration.CreateConfigurationRequest.script', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ignoreInvalid', full_name='configuration.CreateConfigurationRequest.ignoreInvalid', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targetRange', full_name='configuration.CreateConfigurationRequest.targetRange', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interval', full_name='configuration.CreateConfigurationRequest.interval', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cacheTtl', full_name='configuration.CreateConfigurationRequest.cacheTtl', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeRange', full_name='configuration.CreateConfigurationRequest.timeRange', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clazzName', full_name='configuration.CreateConfigurationRequest.clazzName', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectId', full_name='configuration.CreateConfigurationRequest.objectId', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceIdMacro', full_name='configuration.CreateConfigurationRequest.instanceIdMacro', index=14,
      number=15, type=9, cpp_type=9, label=1,
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
  serialized_start=198,
  serialized_end=602,
)


_CREATECONFIGURATIONRESPONSE = _descriptor.Descriptor(
  name='CreateConfigurationResponse',
  full_name='configuration.CreateConfigurationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='configuration.CreateConfigurationResponse.id', index=0,
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
  serialized_start=604,
  serialized_end=645,
)


_CREATECONFIGURATIONRESPONSEWRAPPER = _descriptor.Descriptor(
  name='CreateConfigurationResponseWrapper',
  full_name='configuration.CreateConfigurationResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='configuration.CreateConfigurationResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='configuration.CreateConfigurationResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='configuration.CreateConfigurationResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='configuration.CreateConfigurationResponseWrapper.data', index=3,
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
  serialized_start=648,
  serialized_end=792,
)

_CREATECONFIGURATIONREQUEST.fields_by_name['kwargs'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_CREATECONFIGURATIONREQUEST.fields_by_name['env'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_CREATECONFIGURATIONREQUEST.fields_by_name['script'].message_type = collector__center__sdk_dot_model_dot_collector__center_dot_script__pb2._SCRIPT
_CREATECONFIGURATIONREQUEST.fields_by_name['targetRange'].message_type = collector__center__sdk_dot_model_dot_collector__center_dot_target__range__pb2._TARGETRANGE
_CREATECONFIGURATIONRESPONSEWRAPPER.fields_by_name['data'].message_type = _CREATECONFIGURATIONRESPONSE
DESCRIPTOR.message_types_by_name['CreateConfigurationRequest'] = _CREATECONFIGURATIONREQUEST
DESCRIPTOR.message_types_by_name['CreateConfigurationResponse'] = _CREATECONFIGURATIONRESPONSE
DESCRIPTOR.message_types_by_name['CreateConfigurationResponseWrapper'] = _CREATECONFIGURATIONRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateConfigurationRequest = _reflection.GeneratedProtocolMessageType('CreateConfigurationRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATECONFIGURATIONREQUEST,
  '__module__' : 'create_configuration_pb2'
  # @@protoc_insertion_point(class_scope:configuration.CreateConfigurationRequest)
  })
_sym_db.RegisterMessage(CreateConfigurationRequest)

CreateConfigurationResponse = _reflection.GeneratedProtocolMessageType('CreateConfigurationResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATECONFIGURATIONRESPONSE,
  '__module__' : 'create_configuration_pb2'
  # @@protoc_insertion_point(class_scope:configuration.CreateConfigurationResponse)
  })
_sym_db.RegisterMessage(CreateConfigurationResponse)

CreateConfigurationResponseWrapper = _reflection.GeneratedProtocolMessageType('CreateConfigurationResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _CREATECONFIGURATIONRESPONSEWRAPPER,
  '__module__' : 'create_configuration_pb2'
  # @@protoc_insertion_point(class_scope:configuration.CreateConfigurationResponseWrapper)
  })
_sym_db.RegisterMessage(CreateConfigurationResponseWrapper)


# @@protoc_insertion_point(module_scope)