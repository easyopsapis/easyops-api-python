# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: create_analysis_setting.proto

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
  name='create_analysis_setting.proto',
  package='model_analysis',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1d\x63reate_analysis_setting.proto\x12\x0emodel_analysis\x1a\x1bgoogle/protobuf/empty.proto\"\xa8\x01\n\x1c\x43reateAnalysisSettingRequest\x12G\n\x08settings\x18\x01 \x03(\x0b\x32\x35.model_analysis.CreateAnalysisSettingRequest.Settings\x1a?\n\x08Settings\x12\x10\n\x08objectId\x18\x01 \x01(\t\x12\x12\n\nobjectName\x18\x02 \x01(\t\x12\r\n\x05\x61ttrs\x18\x03 \x03(\t\"~\n$CreateAnalysisSettingResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12$\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x16.google.protobuf.Emptyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_CREATEANALYSISSETTINGREQUEST_SETTINGS = _descriptor.Descriptor(
  name='Settings',
  full_name='model_analysis.CreateAnalysisSettingRequest.Settings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='objectId', full_name='model_analysis.CreateAnalysisSettingRequest.Settings.objectId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectName', full_name='model_analysis.CreateAnalysisSettingRequest.Settings.objectName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attrs', full_name='model_analysis.CreateAnalysisSettingRequest.Settings.attrs', index=2,
      number=3, type=9, cpp_type=9, label=3,
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
  serialized_start=184,
  serialized_end=247,
)

_CREATEANALYSISSETTINGREQUEST = _descriptor.Descriptor(
  name='CreateAnalysisSettingRequest',
  full_name='model_analysis.CreateAnalysisSettingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='settings', full_name='model_analysis.CreateAnalysisSettingRequest.settings', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CREATEANALYSISSETTINGREQUEST_SETTINGS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=79,
  serialized_end=247,
)


_CREATEANALYSISSETTINGRESPONSEWRAPPER = _descriptor.Descriptor(
  name='CreateAnalysisSettingResponseWrapper',
  full_name='model_analysis.CreateAnalysisSettingResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='model_analysis.CreateAnalysisSettingResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='model_analysis.CreateAnalysisSettingResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='model_analysis.CreateAnalysisSettingResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='model_analysis.CreateAnalysisSettingResponseWrapper.data', index=3,
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
  serialized_start=249,
  serialized_end=375,
)

_CREATEANALYSISSETTINGREQUEST_SETTINGS.containing_type = _CREATEANALYSISSETTINGREQUEST
_CREATEANALYSISSETTINGREQUEST.fields_by_name['settings'].message_type = _CREATEANALYSISSETTINGREQUEST_SETTINGS
_CREATEANALYSISSETTINGRESPONSEWRAPPER.fields_by_name['data'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
DESCRIPTOR.message_types_by_name['CreateAnalysisSettingRequest'] = _CREATEANALYSISSETTINGREQUEST
DESCRIPTOR.message_types_by_name['CreateAnalysisSettingResponseWrapper'] = _CREATEANALYSISSETTINGRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateAnalysisSettingRequest = _reflection.GeneratedProtocolMessageType('CreateAnalysisSettingRequest', (_message.Message,), {

  'Settings' : _reflection.GeneratedProtocolMessageType('Settings', (_message.Message,), {
    'DESCRIPTOR' : _CREATEANALYSISSETTINGREQUEST_SETTINGS,
    '__module__' : 'create_analysis_setting_pb2'
    # @@protoc_insertion_point(class_scope:model_analysis.CreateAnalysisSettingRequest.Settings)
    })
  ,
  'DESCRIPTOR' : _CREATEANALYSISSETTINGREQUEST,
  '__module__' : 'create_analysis_setting_pb2'
  # @@protoc_insertion_point(class_scope:model_analysis.CreateAnalysisSettingRequest)
  })
_sym_db.RegisterMessage(CreateAnalysisSettingRequest)
_sym_db.RegisterMessage(CreateAnalysisSettingRequest.Settings)

CreateAnalysisSettingResponseWrapper = _reflection.GeneratedProtocolMessageType('CreateAnalysisSettingResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _CREATEANALYSISSETTINGRESPONSEWRAPPER,
  '__module__' : 'create_analysis_setting_pb2'
  # @@protoc_insertion_point(class_scope:model_analysis.CreateAnalysisSettingResponseWrapper)
  })
_sym_db.RegisterMessage(CreateAnalysisSettingResponseWrapper)


# @@protoc_insertion_point(module_scope)