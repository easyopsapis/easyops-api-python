# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: business_tree_list.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='business_tree_list.proto',
  package='business_instance',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x18\x62usiness_tree_list.proto\x12\x11\x62usiness_instance\")\n\x1aGetBusinessTreeListRequest\x12\x0b\n\x03ids\x18\x01 \x01(\t\"\xb5\x01\n\x1bGetBusinessTreeListResponse\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12G\n\x07parents\x18\x03 \x03(\x0b\x32\x36.business_instance.GetBusinessTreeListResponse.Parents\x1a+\n\x07Parents\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x94\x01\n\"GetBusinessTreeListResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12<\n\x04\x64\x61ta\x18\x04 \x03(\x0b\x32..business_instance.GetBusinessTreeListResponseb\x06proto3')
)




_GETBUSINESSTREELISTREQUEST = _descriptor.Descriptor(
  name='GetBusinessTreeListRequest',
  full_name='business_instance.GetBusinessTreeListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='business_instance.GetBusinessTreeListRequest.ids', index=0,
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
  serialized_start=47,
  serialized_end=88,
)


_GETBUSINESSTREELISTRESPONSE_PARENTS = _descriptor.Descriptor(
  name='Parents',
  full_name='business_instance.GetBusinessTreeListResponse.Parents',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='business_instance.GetBusinessTreeListResponse.Parents.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='business_instance.GetBusinessTreeListResponse.Parents.name', index=1,
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
  serialized_start=229,
  serialized_end=272,
)

_GETBUSINESSTREELISTRESPONSE = _descriptor.Descriptor(
  name='GetBusinessTreeListResponse',
  full_name='business_instance.GetBusinessTreeListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='business_instance.GetBusinessTreeListResponse.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='business_instance.GetBusinessTreeListResponse.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parents', full_name='business_instance.GetBusinessTreeListResponse.parents', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETBUSINESSTREELISTRESPONSE_PARENTS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=91,
  serialized_end=272,
)


_GETBUSINESSTREELISTRESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetBusinessTreeListResponseWrapper',
  full_name='business_instance.GetBusinessTreeListResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='business_instance.GetBusinessTreeListResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='business_instance.GetBusinessTreeListResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='business_instance.GetBusinessTreeListResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='business_instance.GetBusinessTreeListResponseWrapper.data', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=275,
  serialized_end=423,
)

_GETBUSINESSTREELISTRESPONSE_PARENTS.containing_type = _GETBUSINESSTREELISTRESPONSE
_GETBUSINESSTREELISTRESPONSE.fields_by_name['parents'].message_type = _GETBUSINESSTREELISTRESPONSE_PARENTS
_GETBUSINESSTREELISTRESPONSEWRAPPER.fields_by_name['data'].message_type = _GETBUSINESSTREELISTRESPONSE
DESCRIPTOR.message_types_by_name['GetBusinessTreeListRequest'] = _GETBUSINESSTREELISTREQUEST
DESCRIPTOR.message_types_by_name['GetBusinessTreeListResponse'] = _GETBUSINESSTREELISTRESPONSE
DESCRIPTOR.message_types_by_name['GetBusinessTreeListResponseWrapper'] = _GETBUSINESSTREELISTRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetBusinessTreeListRequest = _reflection.GeneratedProtocolMessageType('GetBusinessTreeListRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBUSINESSTREELISTREQUEST,
  '__module__' : 'business_tree_list_pb2'
  # @@protoc_insertion_point(class_scope:business_instance.GetBusinessTreeListRequest)
  })
_sym_db.RegisterMessage(GetBusinessTreeListRequest)

GetBusinessTreeListResponse = _reflection.GeneratedProtocolMessageType('GetBusinessTreeListResponse', (_message.Message,), {

  'Parents' : _reflection.GeneratedProtocolMessageType('Parents', (_message.Message,), {
    'DESCRIPTOR' : _GETBUSINESSTREELISTRESPONSE_PARENTS,
    '__module__' : 'business_tree_list_pb2'
    # @@protoc_insertion_point(class_scope:business_instance.GetBusinessTreeListResponse.Parents)
    })
  ,
  'DESCRIPTOR' : _GETBUSINESSTREELISTRESPONSE,
  '__module__' : 'business_tree_list_pb2'
  # @@protoc_insertion_point(class_scope:business_instance.GetBusinessTreeListResponse)
  })
_sym_db.RegisterMessage(GetBusinessTreeListResponse)
_sym_db.RegisterMessage(GetBusinessTreeListResponse.Parents)

GetBusinessTreeListResponseWrapper = _reflection.GeneratedProtocolMessageType('GetBusinessTreeListResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _GETBUSINESSTREELISTRESPONSEWRAPPER,
  '__module__' : 'business_tree_list_pb2'
  # @@protoc_insertion_point(class_scope:business_instance.GetBusinessTreeListResponseWrapper)
  })
_sym_db.RegisterMessage(GetBusinessTreeListResponseWrapper)


# @@protoc_insertion_point(module_scope)
