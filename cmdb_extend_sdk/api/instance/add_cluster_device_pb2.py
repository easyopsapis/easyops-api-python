# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: add_cluster_device.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='add_cluster_device.proto',
  package='instance',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x18\x61\x64\x64_cluster_device.proto\x12\x08instance\"@\n\x17\x41\x64\x64\x43lusterDeviceRequest\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x11\n\tdeviceIds\x18\x02 \x01(\t\"V\n\x18\x41\x64\x64\x43lusterDeviceResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\r\n\x05\x65rror\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\t\"\x85\x01\n\x1f\x41\x64\x64\x43lusterDeviceResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x30\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\".instance.AddClusterDeviceResponseb\x06proto3')
)




_ADDCLUSTERDEVICEREQUEST = _descriptor.Descriptor(
  name='AddClusterDeviceRequest',
  full_name='instance.AddClusterDeviceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='instance.AddClusterDeviceRequest.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deviceIds', full_name='instance.AddClusterDeviceRequest.deviceIds', index=1,
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
  serialized_start=38,
  serialized_end=102,
)


_ADDCLUSTERDEVICERESPONSE = _descriptor.Descriptor(
  name='AddClusterDeviceResponse',
  full_name='instance.AddClusterDeviceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='instance.AddClusterDeviceResponse.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='instance.AddClusterDeviceResponse.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='instance.AddClusterDeviceResponse.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='instance.AddClusterDeviceResponse.data', index=3,
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
  serialized_start=104,
  serialized_end=190,
)


_ADDCLUSTERDEVICERESPONSEWRAPPER = _descriptor.Descriptor(
  name='AddClusterDeviceResponseWrapper',
  full_name='instance.AddClusterDeviceResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='instance.AddClusterDeviceResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='instance.AddClusterDeviceResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='instance.AddClusterDeviceResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='instance.AddClusterDeviceResponseWrapper.data', index=3,
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
  serialized_start=193,
  serialized_end=326,
)

_ADDCLUSTERDEVICERESPONSEWRAPPER.fields_by_name['data'].message_type = _ADDCLUSTERDEVICERESPONSE
DESCRIPTOR.message_types_by_name['AddClusterDeviceRequest'] = _ADDCLUSTERDEVICEREQUEST
DESCRIPTOR.message_types_by_name['AddClusterDeviceResponse'] = _ADDCLUSTERDEVICERESPONSE
DESCRIPTOR.message_types_by_name['AddClusterDeviceResponseWrapper'] = _ADDCLUSTERDEVICERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AddClusterDeviceRequest = _reflection.GeneratedProtocolMessageType('AddClusterDeviceRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDCLUSTERDEVICEREQUEST,
  '__module__' : 'add_cluster_device_pb2'
  # @@protoc_insertion_point(class_scope:instance.AddClusterDeviceRequest)
  })
_sym_db.RegisterMessage(AddClusterDeviceRequest)

AddClusterDeviceResponse = _reflection.GeneratedProtocolMessageType('AddClusterDeviceResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDCLUSTERDEVICERESPONSE,
  '__module__' : 'add_cluster_device_pb2'
  # @@protoc_insertion_point(class_scope:instance.AddClusterDeviceResponse)
  })
_sym_db.RegisterMessage(AddClusterDeviceResponse)

AddClusterDeviceResponseWrapper = _reflection.GeneratedProtocolMessageType('AddClusterDeviceResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _ADDCLUSTERDEVICERESPONSEWRAPPER,
  '__module__' : 'add_cluster_device_pb2'
  # @@protoc_insertion_point(class_scope:instance.AddClusterDeviceResponseWrapper)
  })
_sym_db.RegisterMessage(AddClusterDeviceResponseWrapper)


# @@protoc_insertion_point(module_scope)
