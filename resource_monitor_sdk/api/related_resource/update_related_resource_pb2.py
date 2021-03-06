# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: update_related_resource.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='update_related_resource.proto',
  package='related_resource',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1dupdate_related_resource.proto\x12\x10related_resource\"\xfc\x01\n\x1cUpdateRelatedResourceRequest\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x17\n\x0frelatedObjectId\x18\x03 \x01(\t\x12\r\n\x05query\x18\x04 \x01(\t\x12O\n\x0brelatedInfo\x18\x05 \x01(\x0b\x32:.related_resource.UpdateRelatedResourceRequest.RelatedInfo\x1a\x41\n\x0bRelatedInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12\x17\n\x0freverseQueryKey\x18\x03 \x01(\t\"3\n\x1dUpdateRelatedResourceResponse\x12\x12\n\ninstanceId\x18\x01 \x01(\t\"\x97\x01\n$UpdateRelatedResourceResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12=\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32/.related_resource.UpdateRelatedResourceResponseb\x06proto3')
)




_UPDATERELATEDRESOURCEREQUEST_RELATEDINFO = _descriptor.Descriptor(
  name='RelatedInfo',
  full_name='related_resource.UpdateRelatedResourceRequest.RelatedInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='related_resource.UpdateRelatedResourceRequest.RelatedInfo.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='label', full_name='related_resource.UpdateRelatedResourceRequest.RelatedInfo.label', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reverseQueryKey', full_name='related_resource.UpdateRelatedResourceRequest.RelatedInfo.reverseQueryKey', index=2,
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
  serialized_start=239,
  serialized_end=304,
)

_UPDATERELATEDRESOURCEREQUEST = _descriptor.Descriptor(
  name='UpdateRelatedResourceRequest',
  full_name='related_resource.UpdateRelatedResourceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='related_resource.UpdateRelatedResourceRequest.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='related_resource.UpdateRelatedResourceRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relatedObjectId', full_name='related_resource.UpdateRelatedResourceRequest.relatedObjectId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='query', full_name='related_resource.UpdateRelatedResourceRequest.query', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relatedInfo', full_name='related_resource.UpdateRelatedResourceRequest.relatedInfo', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_UPDATERELATEDRESOURCEREQUEST_RELATEDINFO, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=52,
  serialized_end=304,
)


_UPDATERELATEDRESOURCERESPONSE = _descriptor.Descriptor(
  name='UpdateRelatedResourceResponse',
  full_name='related_resource.UpdateRelatedResourceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='related_resource.UpdateRelatedResourceResponse.instanceId', index=0,
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
  serialized_start=306,
  serialized_end=357,
)


_UPDATERELATEDRESOURCERESPONSEWRAPPER = _descriptor.Descriptor(
  name='UpdateRelatedResourceResponseWrapper',
  full_name='related_resource.UpdateRelatedResourceResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='related_resource.UpdateRelatedResourceResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='related_resource.UpdateRelatedResourceResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='related_resource.UpdateRelatedResourceResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='related_resource.UpdateRelatedResourceResponseWrapper.data', index=3,
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
  serialized_start=360,
  serialized_end=511,
)

_UPDATERELATEDRESOURCEREQUEST_RELATEDINFO.containing_type = _UPDATERELATEDRESOURCEREQUEST
_UPDATERELATEDRESOURCEREQUEST.fields_by_name['relatedInfo'].message_type = _UPDATERELATEDRESOURCEREQUEST_RELATEDINFO
_UPDATERELATEDRESOURCERESPONSEWRAPPER.fields_by_name['data'].message_type = _UPDATERELATEDRESOURCERESPONSE
DESCRIPTOR.message_types_by_name['UpdateRelatedResourceRequest'] = _UPDATERELATEDRESOURCEREQUEST
DESCRIPTOR.message_types_by_name['UpdateRelatedResourceResponse'] = _UPDATERELATEDRESOURCERESPONSE
DESCRIPTOR.message_types_by_name['UpdateRelatedResourceResponseWrapper'] = _UPDATERELATEDRESOURCERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateRelatedResourceRequest = _reflection.GeneratedProtocolMessageType('UpdateRelatedResourceRequest', (_message.Message,), {

  'RelatedInfo' : _reflection.GeneratedProtocolMessageType('RelatedInfo', (_message.Message,), {
    'DESCRIPTOR' : _UPDATERELATEDRESOURCEREQUEST_RELATEDINFO,
    '__module__' : 'update_related_resource_pb2'
    # @@protoc_insertion_point(class_scope:related_resource.UpdateRelatedResourceRequest.RelatedInfo)
    })
  ,
  'DESCRIPTOR' : _UPDATERELATEDRESOURCEREQUEST,
  '__module__' : 'update_related_resource_pb2'
  # @@protoc_insertion_point(class_scope:related_resource.UpdateRelatedResourceRequest)
  })
_sym_db.RegisterMessage(UpdateRelatedResourceRequest)
_sym_db.RegisterMessage(UpdateRelatedResourceRequest.RelatedInfo)

UpdateRelatedResourceResponse = _reflection.GeneratedProtocolMessageType('UpdateRelatedResourceResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATERELATEDRESOURCERESPONSE,
  '__module__' : 'update_related_resource_pb2'
  # @@protoc_insertion_point(class_scope:related_resource.UpdateRelatedResourceResponse)
  })
_sym_db.RegisterMessage(UpdateRelatedResourceResponse)

UpdateRelatedResourceResponseWrapper = _reflection.GeneratedProtocolMessageType('UpdateRelatedResourceResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _UPDATERELATEDRESOURCERESPONSEWRAPPER,
  '__module__' : 'update_related_resource_pb2'
  # @@protoc_insertion_point(class_scope:related_resource.UpdateRelatedResourceResponseWrapper)
  })
_sym_db.RegisterMessage(UpdateRelatedResourceResponseWrapper)


# @@protoc_insertion_point(module_scope)
