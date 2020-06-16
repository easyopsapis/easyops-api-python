# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: detail_configuration_template.proto

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
from collector_center_sdk.model.collector_center import configuration_template_pb2 as collector__center__sdk_dot_model_dot_collector__center_dot_configuration__template__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='detail_configuration_template.proto',
  package='template',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n#detail_configuration_template.proto\x12\x08template\x1a\x38\x63ollector_center_sdk/model/collector_center/script.proto\x1a>collector_center_sdk/model/collector_center/target_range.proto\x1aHcollector_center_sdk/model/collector_center/configuration_template.proto\x1a\x1cgoogle/protobuf/struct.proto\"0\n\"DetailConfigurationTemplateRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x95\x01\n*DetailConfigurationTemplateResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x35\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\'.collector_center.ConfigurationTemplateb\x06proto3')
  ,
  dependencies=[collector__center__sdk_dot_model_dot_collector__center_dot_script__pb2.DESCRIPTOR,collector__center__sdk_dot_model_dot_collector__center_dot_target__range__pb2.DESCRIPTOR,collector__center__sdk_dot_model_dot_collector__center_dot_configuration__template__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_DETAILCONFIGURATIONTEMPLATEREQUEST = _descriptor.Descriptor(
  name='DetailConfigurationTemplateRequest',
  full_name='template.DetailConfigurationTemplateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='template.DetailConfigurationTemplateRequest.id', index=0,
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
  serialized_start=275,
  serialized_end=323,
)


_DETAILCONFIGURATIONTEMPLATERESPONSEWRAPPER = _descriptor.Descriptor(
  name='DetailConfigurationTemplateResponseWrapper',
  full_name='template.DetailConfigurationTemplateResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='template.DetailConfigurationTemplateResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='template.DetailConfigurationTemplateResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='template.DetailConfigurationTemplateResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='template.DetailConfigurationTemplateResponseWrapper.data', index=3,
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
  serialized_start=326,
  serialized_end=475,
)

_DETAILCONFIGURATIONTEMPLATERESPONSEWRAPPER.fields_by_name['data'].message_type = collector__center__sdk_dot_model_dot_collector__center_dot_configuration__template__pb2._CONFIGURATIONTEMPLATE
DESCRIPTOR.message_types_by_name['DetailConfigurationTemplateRequest'] = _DETAILCONFIGURATIONTEMPLATEREQUEST
DESCRIPTOR.message_types_by_name['DetailConfigurationTemplateResponseWrapper'] = _DETAILCONFIGURATIONTEMPLATERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DetailConfigurationTemplateRequest = _reflection.GeneratedProtocolMessageType('DetailConfigurationTemplateRequest', (_message.Message,), {
  'DESCRIPTOR' : _DETAILCONFIGURATIONTEMPLATEREQUEST,
  '__module__' : 'detail_configuration_template_pb2'
  # @@protoc_insertion_point(class_scope:template.DetailConfigurationTemplateRequest)
  })
_sym_db.RegisterMessage(DetailConfigurationTemplateRequest)

DetailConfigurationTemplateResponseWrapper = _reflection.GeneratedProtocolMessageType('DetailConfigurationTemplateResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _DETAILCONFIGURATIONTEMPLATERESPONSEWRAPPER,
  '__module__' : 'detail_configuration_template_pb2'
  # @@protoc_insertion_point(class_scope:template.DetailConfigurationTemplateResponseWrapper)
  })
_sym_db.RegisterMessage(DetailConfigurationTemplateResponseWrapper)


# @@protoc_insertion_point(module_scope)