# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: save.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flowable_service_sdk.model.flowable_service import form_schema_version_pb2 as flowable__service__sdk_dot_model_dot_flowable__service_dot_form__schema__version__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='save.proto',
  package='form_schema',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\nsave.proto\x12\x0b\x66orm_schema\x1a\x45\x66lowable_service_sdk/model/flowable_service/form_schema_version.proto\"\x90\x01\n\x15SaveFormSchemaRequest\x12\r\n\x05state\x18\x01 \x01(\t\x12\r\n\x05vMemo\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x04 \x01(\t\x12\x0c\n\x04memo\x18\x05 \x01(\t\x12\x16\n\x0e\x66ormDefinition\x18\x06 \x01(\t\x12\x13\n\x0bversionName\x18\x07 \x01(\t\"\xb7\x01\n\x16SaveFormSchemaResponse\x12;\n\x0elastestVersion\x18\x01 \x01(\x0b\x32#.flowable_service.FormSchemaVersion\x12\x12\n\ninstanceId\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x04 \x01(\t\x12\x0c\n\x04memo\x18\x05 \x01(\t\x12\x0f\n\x07\x63reator\x18\x06 \x01(\t\x12\r\n\x05\x63time\x18\x07 \x01(\t\"\x84\x01\n\x1dSaveFormSchemaResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x31\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32#.form_schema.SaveFormSchemaResponseb\x06proto3')
  ,
  dependencies=[flowable__service__sdk_dot_model_dot_flowable__service_dot_form__schema__version__pb2.DESCRIPTOR,])




_SAVEFORMSCHEMAREQUEST = _descriptor.Descriptor(
  name='SaveFormSchemaRequest',
  full_name='form_schema.SaveFormSchemaRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='form_schema.SaveFormSchemaRequest.state', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vMemo', full_name='form_schema.SaveFormSchemaRequest.vMemo', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='form_schema.SaveFormSchemaRequest.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='form_schema.SaveFormSchemaRequest.category', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='form_schema.SaveFormSchemaRequest.memo', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='formDefinition', full_name='form_schema.SaveFormSchemaRequest.formDefinition', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionName', full_name='form_schema.SaveFormSchemaRequest.versionName', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=99,
  serialized_end=243,
)


_SAVEFORMSCHEMARESPONSE = _descriptor.Descriptor(
  name='SaveFormSchemaResponse',
  full_name='form_schema.SaveFormSchemaResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lastestVersion', full_name='form_schema.SaveFormSchemaResponse.lastestVersion', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='form_schema.SaveFormSchemaResponse.instanceId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='form_schema.SaveFormSchemaResponse.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='form_schema.SaveFormSchemaResponse.category', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='form_schema.SaveFormSchemaResponse.memo', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='form_schema.SaveFormSchemaResponse.creator', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='form_schema.SaveFormSchemaResponse.ctime', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=246,
  serialized_end=429,
)


_SAVEFORMSCHEMARESPONSEWRAPPER = _descriptor.Descriptor(
  name='SaveFormSchemaResponseWrapper',
  full_name='form_schema.SaveFormSchemaResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='form_schema.SaveFormSchemaResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='form_schema.SaveFormSchemaResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='form_schema.SaveFormSchemaResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='form_schema.SaveFormSchemaResponseWrapper.data', index=3,
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
  serialized_start=432,
  serialized_end=564,
)

_SAVEFORMSCHEMARESPONSE.fields_by_name['lastestVersion'].message_type = flowable__service__sdk_dot_model_dot_flowable__service_dot_form__schema__version__pb2._FORMSCHEMAVERSION
_SAVEFORMSCHEMARESPONSEWRAPPER.fields_by_name['data'].message_type = _SAVEFORMSCHEMARESPONSE
DESCRIPTOR.message_types_by_name['SaveFormSchemaRequest'] = _SAVEFORMSCHEMAREQUEST
DESCRIPTOR.message_types_by_name['SaveFormSchemaResponse'] = _SAVEFORMSCHEMARESPONSE
DESCRIPTOR.message_types_by_name['SaveFormSchemaResponseWrapper'] = _SAVEFORMSCHEMARESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SaveFormSchemaRequest = _reflection.GeneratedProtocolMessageType('SaveFormSchemaRequest', (_message.Message,), {
  'DESCRIPTOR' : _SAVEFORMSCHEMAREQUEST,
  '__module__' : 'save_pb2'
  # @@protoc_insertion_point(class_scope:form_schema.SaveFormSchemaRequest)
  })
_sym_db.RegisterMessage(SaveFormSchemaRequest)

SaveFormSchemaResponse = _reflection.GeneratedProtocolMessageType('SaveFormSchemaResponse', (_message.Message,), {
  'DESCRIPTOR' : _SAVEFORMSCHEMARESPONSE,
  '__module__' : 'save_pb2'
  # @@protoc_insertion_point(class_scope:form_schema.SaveFormSchemaResponse)
  })
_sym_db.RegisterMessage(SaveFormSchemaResponse)

SaveFormSchemaResponseWrapper = _reflection.GeneratedProtocolMessageType('SaveFormSchemaResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _SAVEFORMSCHEMARESPONSEWRAPPER,
  '__module__' : 'save_pb2'
  # @@protoc_insertion_point(class_scope:form_schema.SaveFormSchemaResponseWrapper)
  })
_sym_db.RegisterMessage(SaveFormSchemaResponseWrapper)


# @@protoc_insertion_point(module_scope)
