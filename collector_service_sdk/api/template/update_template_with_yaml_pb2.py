# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: update_template_with_yaml.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from collector_service_sdk.model.collector_service import collector_template_pb2 as collector__service__sdk_dot_model_dot_collector__service_dot_collector__template__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='update_template_with_yaml.proto',
  package='template',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1fupdate_template_with_yaml.proto\x12\x08template\x1a\x46\x63ollector_service_sdk/model/collector_service/collector_template.proto\"p\n&UpdateCollectorTemplateWithYamlRequest\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08objectId\x18\x03 \x01(\t\x12\x12\n\nconfigYaml\x18\x04 \x01(\t\"\x96\x01\n.UpdateCollectorTemplateWithYamlResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x32\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32$.collector_service.CollectorTemplateb\x06proto3')
  ,
  dependencies=[collector__service__sdk_dot_model_dot_collector__service_dot_collector__template__pb2.DESCRIPTOR,])




_UPDATECOLLECTORTEMPLATEWITHYAMLREQUEST = _descriptor.Descriptor(
  name='UpdateCollectorTemplateWithYamlRequest',
  full_name='template.UpdateCollectorTemplateWithYamlRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='template.UpdateCollectorTemplateWithYamlRequest.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='template.UpdateCollectorTemplateWithYamlRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectId', full_name='template.UpdateCollectorTemplateWithYamlRequest.objectId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='configYaml', full_name='template.UpdateCollectorTemplateWithYamlRequest.configYaml', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=117,
  serialized_end=229,
)


_UPDATECOLLECTORTEMPLATEWITHYAMLRESPONSEWRAPPER = _descriptor.Descriptor(
  name='UpdateCollectorTemplateWithYamlResponseWrapper',
  full_name='template.UpdateCollectorTemplateWithYamlResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='template.UpdateCollectorTemplateWithYamlResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='template.UpdateCollectorTemplateWithYamlResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='template.UpdateCollectorTemplateWithYamlResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='template.UpdateCollectorTemplateWithYamlResponseWrapper.data', index=3,
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
  serialized_start=232,
  serialized_end=382,
)

_UPDATECOLLECTORTEMPLATEWITHYAMLRESPONSEWRAPPER.fields_by_name['data'].message_type = collector__service__sdk_dot_model_dot_collector__service_dot_collector__template__pb2._COLLECTORTEMPLATE
DESCRIPTOR.message_types_by_name['UpdateCollectorTemplateWithYamlRequest'] = _UPDATECOLLECTORTEMPLATEWITHYAMLREQUEST
DESCRIPTOR.message_types_by_name['UpdateCollectorTemplateWithYamlResponseWrapper'] = _UPDATECOLLECTORTEMPLATEWITHYAMLRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateCollectorTemplateWithYamlRequest = _reflection.GeneratedProtocolMessageType('UpdateCollectorTemplateWithYamlRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATECOLLECTORTEMPLATEWITHYAMLREQUEST,
  '__module__' : 'update_template_with_yaml_pb2'
  # @@protoc_insertion_point(class_scope:template.UpdateCollectorTemplateWithYamlRequest)
  })
_sym_db.RegisterMessage(UpdateCollectorTemplateWithYamlRequest)

UpdateCollectorTemplateWithYamlResponseWrapper = _reflection.GeneratedProtocolMessageType('UpdateCollectorTemplateWithYamlResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _UPDATECOLLECTORTEMPLATEWITHYAMLRESPONSEWRAPPER,
  '__module__' : 'update_template_with_yaml_pb2'
  # @@protoc_insertion_point(class_scope:template.UpdateCollectorTemplateWithYamlResponseWrapper)
  })
_sym_db.RegisterMessage(UpdateCollectorTemplateWithYamlResponseWrapper)


# @@protoc_insertion_point(module_scope)
