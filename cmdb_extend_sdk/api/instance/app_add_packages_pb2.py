# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app_add_packages.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cmdb_extend_sdk.model.cmdb_extend import app_package_pb2 as cmdb__extend__sdk_dot_model_dot_cmdb__extend_dot_app__package__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='app_add_packages.proto',
  package='instance',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16\x61pp_add_packages.proto\x12\x08instance\x1a\x33\x63mdb_extend_sdk/model/cmdb_extend/app_package.proto\x1a\x1bgoogle/protobuf/empty.proto\"V\n\x15\x41ppAddPackagesRequest\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12)\n\x08packages\x18\x02 \x03(\x0b\x32\x17.cmdb_extend.AppPackage\"w\n\x1d\x41ppAddPackagesResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12$\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x16.google.protobuf.Emptyb\x06proto3')
  ,
  dependencies=[cmdb__extend__sdk_dot_model_dot_cmdb__extend_dot_app__package__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_APPADDPACKAGESREQUEST = _descriptor.Descriptor(
  name='AppAddPackagesRequest',
  full_name='instance.AppAddPackagesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='instance.AppAddPackagesRequest.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packages', full_name='instance.AppAddPackagesRequest.packages', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=118,
  serialized_end=204,
)


_APPADDPACKAGESRESPONSEWRAPPER = _descriptor.Descriptor(
  name='AppAddPackagesResponseWrapper',
  full_name='instance.AppAddPackagesResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='instance.AppAddPackagesResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='instance.AppAddPackagesResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='instance.AppAddPackagesResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='instance.AppAddPackagesResponseWrapper.data', index=3,
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
  serialized_start=206,
  serialized_end=325,
)

_APPADDPACKAGESREQUEST.fields_by_name['packages'].message_type = cmdb__extend__sdk_dot_model_dot_cmdb__extend_dot_app__package__pb2._APPPACKAGE
_APPADDPACKAGESRESPONSEWRAPPER.fields_by_name['data'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
DESCRIPTOR.message_types_by_name['AppAddPackagesRequest'] = _APPADDPACKAGESREQUEST
DESCRIPTOR.message_types_by_name['AppAddPackagesResponseWrapper'] = _APPADDPACKAGESRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AppAddPackagesRequest = _reflection.GeneratedProtocolMessageType('AppAddPackagesRequest', (_message.Message,), {
  'DESCRIPTOR' : _APPADDPACKAGESREQUEST,
  '__module__' : 'app_add_packages_pb2'
  # @@protoc_insertion_point(class_scope:instance.AppAddPackagesRequest)
  })
_sym_db.RegisterMessage(AppAddPackagesRequest)

AppAddPackagesResponseWrapper = _reflection.GeneratedProtocolMessageType('AppAddPackagesResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _APPADDPACKAGESRESPONSEWRAPPER,
  '__module__' : 'app_add_packages_pb2'
  # @@protoc_insertion_point(class_scope:instance.AppAddPackagesResponseWrapper)
  })
_sym_db.RegisterMessage(AppAddPackagesResponseWrapper)


# @@protoc_insertion_point(module_scope)
