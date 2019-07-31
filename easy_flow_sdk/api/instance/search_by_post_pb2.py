# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: search_by_post.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from model.easy_flow import instance_info_pb2 as model_dot_easy__flow_dot_instance__info__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='search_by_post.proto',
  package='instance',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14search_by_post.proto\x12\x08instance\x1a#model/easy_flow/instance_info.proto\"\xd1\x01\n\x10GetSearchRequest\x12\x12\n\npackageIds\x18\x01 \x01(\t\x12\x11\n\tdeviceIds\x18\x02 \x01(\t\x12\x10\n\x08\x64\x65viceIp\x18\x03 \x01(\t\x12\x0e\n\x06\x61ppIds\x18\x04 \x01(\t\x12\x0c\n\x04page\x18\x05 \x01(\x05\x12\x10\n\x08pageSize\x18\x06 \x01(\x05\x12\r\n\x05order\x18\x07 \x01(\t\x12\x11\n\tpackageId\x18\x08 \x01(\t\x12\x11\n\tversionId\x18\t \x01(\t\x12\x10\n\x08\x64\x65viceId\x18\n \x01(\t\x12\r\n\x05\x61ppId\x18\x0b \x01(\t\"i\n\x11GetSearchResponse\x12\r\n\x05total\x18\x01 \x01(\x05\x12%\n\x04list\x18\x02 \x03(\x0b\x32\x17.easy_flow.InstanceInfo\x12\x0c\n\x04page\x18\x03 \x01(\x05\x12\x10\n\x08pageSize\x18\x04 \x01(\x05\"w\n\x18GetSearchResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12)\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1b.instance.GetSearchResponseb\x06proto3')
  ,
  dependencies=[model_dot_easy__flow_dot_instance__info__pb2.DESCRIPTOR,])




_GETSEARCHREQUEST = _descriptor.Descriptor(
  name='GetSearchRequest',
  full_name='instance.GetSearchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='packageIds', full_name='instance.GetSearchRequest.packageIds', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deviceIds', full_name='instance.GetSearchRequest.deviceIds', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deviceIp', full_name='instance.GetSearchRequest.deviceIp', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='appIds', full_name='instance.GetSearchRequest.appIds', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page', full_name='instance.GetSearchRequest.page', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='instance.GetSearchRequest.pageSize', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order', full_name='instance.GetSearchRequest.order', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageId', full_name='instance.GetSearchRequest.packageId', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionId', full_name='instance.GetSearchRequest.versionId', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deviceId', full_name='instance.GetSearchRequest.deviceId', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='appId', full_name='instance.GetSearchRequest.appId', index=10,
      number=11, type=9, cpp_type=9, label=1,
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
  serialized_start=72,
  serialized_end=281,
)


_GETSEARCHRESPONSE = _descriptor.Descriptor(
  name='GetSearchResponse',
  full_name='instance.GetSearchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='total', full_name='instance.GetSearchResponse.total', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='instance.GetSearchResponse.list', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page', full_name='instance.GetSearchResponse.page', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='instance.GetSearchResponse.pageSize', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=283,
  serialized_end=388,
)


_GETSEARCHRESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetSearchResponseWrapper',
  full_name='instance.GetSearchResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='instance.GetSearchResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='instance.GetSearchResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='instance.GetSearchResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='instance.GetSearchResponseWrapper.data', index=3,
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
  serialized_start=390,
  serialized_end=509,
)

_GETSEARCHRESPONSE.fields_by_name['list'].message_type = model_dot_easy__flow_dot_instance__info__pb2._INSTANCEINFO
_GETSEARCHRESPONSEWRAPPER.fields_by_name['data'].message_type = _GETSEARCHRESPONSE
DESCRIPTOR.message_types_by_name['GetSearchRequest'] = _GETSEARCHREQUEST
DESCRIPTOR.message_types_by_name['GetSearchResponse'] = _GETSEARCHRESPONSE
DESCRIPTOR.message_types_by_name['GetSearchResponseWrapper'] = _GETSEARCHRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetSearchRequest = _reflection.GeneratedProtocolMessageType('GetSearchRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETSEARCHREQUEST,
  __module__ = 'search_by_post_pb2'
  # @@protoc_insertion_point(class_scope:instance.GetSearchRequest)
  ))
_sym_db.RegisterMessage(GetSearchRequest)

GetSearchResponse = _reflection.GeneratedProtocolMessageType('GetSearchResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETSEARCHRESPONSE,
  __module__ = 'search_by_post_pb2'
  # @@protoc_insertion_point(class_scope:instance.GetSearchResponse)
  ))
_sym_db.RegisterMessage(GetSearchResponse)

GetSearchResponseWrapper = _reflection.GeneratedProtocolMessageType('GetSearchResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _GETSEARCHRESPONSEWRAPPER,
  __module__ = 'search_by_post_pb2'
  # @@protoc_insertion_point(class_scope:instance.GetSearchResponseWrapper)
  ))
_sym_db.RegisterMessage(GetSearchResponseWrapper)


# @@protoc_insertion_point(module_scope)
