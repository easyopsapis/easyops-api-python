# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app_delete_package.proto

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
  name='app_delete_package.proto',
  package='instance',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x18\x61pp_delete_package.proto\x12\x08instance\x1a\x1bgoogle/protobuf/empty.proto\"U\n\x17\x41ppDeletePackageRequest\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x11\n\tpackageId\x18\x02 \x01(\t\x12\x13\n\x0binstallPath\x18\x03 \x01(\t\"y\n\x1f\x41ppDeletePackageResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12$\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x16.google.protobuf.Emptyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_APPDELETEPACKAGEREQUEST = _descriptor.Descriptor(
  name='AppDeletePackageRequest',
  full_name='instance.AppDeletePackageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='instance.AppDeletePackageRequest.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageId', full_name='instance.AppDeletePackageRequest.packageId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='installPath', full_name='instance.AppDeletePackageRequest.installPath', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=67,
  serialized_end=152,
)


_APPDELETEPACKAGERESPONSEWRAPPER = _descriptor.Descriptor(
  name='AppDeletePackageResponseWrapper',
  full_name='instance.AppDeletePackageResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='instance.AppDeletePackageResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='instance.AppDeletePackageResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='instance.AppDeletePackageResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='instance.AppDeletePackageResponseWrapper.data', index=3,
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
  serialized_start=154,
  serialized_end=275,
)

_APPDELETEPACKAGERESPONSEWRAPPER.fields_by_name['data'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
DESCRIPTOR.message_types_by_name['AppDeletePackageRequest'] = _APPDELETEPACKAGEREQUEST
DESCRIPTOR.message_types_by_name['AppDeletePackageResponseWrapper'] = _APPDELETEPACKAGERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AppDeletePackageRequest = _reflection.GeneratedProtocolMessageType('AppDeletePackageRequest', (_message.Message,), {
  'DESCRIPTOR' : _APPDELETEPACKAGEREQUEST,
  '__module__' : 'app_delete_package_pb2'
  # @@protoc_insertion_point(class_scope:instance.AppDeletePackageRequest)
  })
_sym_db.RegisterMessage(AppDeletePackageRequest)

AppDeletePackageResponseWrapper = _reflection.GeneratedProtocolMessageType('AppDeletePackageResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _APPDELETEPACKAGERESPONSEWRAPPER,
  '__module__' : 'app_delete_package_pb2'
  # @@protoc_insertion_point(class_scope:instance.AppDeletePackageResponseWrapper)
  })
_sym_db.RegisterMessage(AppDeletePackageResponseWrapper)


# @@protoc_insertion_point(module_scope)
