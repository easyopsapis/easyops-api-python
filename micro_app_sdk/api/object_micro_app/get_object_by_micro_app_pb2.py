# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_object_by_micro_app.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from micro_app_sdk.model.micro_app import object_micro_app_pb2 as micro__app__sdk_dot_model_dot_micro__app_dot_object__micro__app__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_object_by_micro_app.proto',
  package='object_micro_app',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1dget_object_by_micro_app.proto\x12\x10object_micro_app\x1a\x34micro_app_sdk/model/micro_app/object_micro_app.proto\"+\n\x1aGetObjectByMicroAppRequest\x12\r\n\x05\x61ppId\x18\x01 \x01(\t\"\x7f\n\"GetObjectByMicroAppResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\'\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x19.micro_app.ObjectMicroAppb\x06proto3')
  ,
  dependencies=[micro__app__sdk_dot_model_dot_micro__app_dot_object__micro__app__pb2.DESCRIPTOR,])




_GETOBJECTBYMICROAPPREQUEST = _descriptor.Descriptor(
  name='GetObjectByMicroAppRequest',
  full_name='object_micro_app.GetObjectByMicroAppRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appId', full_name='object_micro_app.GetObjectByMicroAppRequest.appId', index=0,
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
  serialized_start=105,
  serialized_end=148,
)


_GETOBJECTBYMICROAPPRESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetObjectByMicroAppResponseWrapper',
  full_name='object_micro_app.GetObjectByMicroAppResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='object_micro_app.GetObjectByMicroAppResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='object_micro_app.GetObjectByMicroAppResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='object_micro_app.GetObjectByMicroAppResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='object_micro_app.GetObjectByMicroAppResponseWrapper.data', index=3,
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
  serialized_start=150,
  serialized_end=277,
)

_GETOBJECTBYMICROAPPRESPONSEWRAPPER.fields_by_name['data'].message_type = micro__app__sdk_dot_model_dot_micro__app_dot_object__micro__app__pb2._OBJECTMICROAPP
DESCRIPTOR.message_types_by_name['GetObjectByMicroAppRequest'] = _GETOBJECTBYMICROAPPREQUEST
DESCRIPTOR.message_types_by_name['GetObjectByMicroAppResponseWrapper'] = _GETOBJECTBYMICROAPPRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetObjectByMicroAppRequest = _reflection.GeneratedProtocolMessageType('GetObjectByMicroAppRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETOBJECTBYMICROAPPREQUEST,
  '__module__' : 'get_object_by_micro_app_pb2'
  # @@protoc_insertion_point(class_scope:object_micro_app.GetObjectByMicroAppRequest)
  })
_sym_db.RegisterMessage(GetObjectByMicroAppRequest)

GetObjectByMicroAppResponseWrapper = _reflection.GeneratedProtocolMessageType('GetObjectByMicroAppResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _GETOBJECTBYMICROAPPRESPONSEWRAPPER,
  '__module__' : 'get_object_by_micro_app_pb2'
  # @@protoc_insertion_point(class_scope:object_micro_app.GetObjectByMicroAppResponseWrapper)
  })
_sym_db.RegisterMessage(GetObjectByMicroAppResponseWrapper)


# @@protoc_insertion_point(module_scope)