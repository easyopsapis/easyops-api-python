# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list_support_infom.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='list_support_infom.proto',
  package='custom_sender',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x18list_support_infom.proto\x12\rcustom_sender\"\x9b\x02\n\x19ListSupportInformResponse\x12;\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32-.custom_sender.ListSupportInformResponse.Data\x12\x0c\n\x04page\x18\x02 \x01(\x05\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\r\n\x05tatal\x18\x04 \x01(\x05\x12\x0b\n\x03msg\x18\x05 \x01(\t\x12\x0c\n\x04\x63ode\x18\x06 \x01(\x05\x1av\n\x04\x44\x61ta\x12\x1f\n\x17\x63ol_of_cmdb_user_object\x18\x01 \x01(\t\x12\x0e\n\x06\x65nable\x18\x02 \x01(\x08\x12\x13\n\x0bplugin_name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x13\n\x0binform_type\x18\x05 \x01(\t\"\x8c\x01\n ListSupportInformResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x36\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32(.custom_sender.ListSupportInformResponseb\x06proto3')
)




_LISTSUPPORTINFORMRESPONSE_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='custom_sender.ListSupportInformResponse.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='col_of_cmdb_user_object', full_name='custom_sender.ListSupportInformResponse.Data.col_of_cmdb_user_object', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable', full_name='custom_sender.ListSupportInformResponse.Data.enable', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='plugin_name', full_name='custom_sender.ListSupportInformResponse.Data.plugin_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='custom_sender.ListSupportInformResponse.Data.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inform_type', full_name='custom_sender.ListSupportInformResponse.Data.inform_type', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=209,
  serialized_end=327,
)

_LISTSUPPORTINFORMRESPONSE = _descriptor.Descriptor(
  name='ListSupportInformResponse',
  full_name='custom_sender.ListSupportInformResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='custom_sender.ListSupportInformResponse.data', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page', full_name='custom_sender.ListSupportInformResponse.page', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='custom_sender.ListSupportInformResponse.page_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tatal', full_name='custom_sender.ListSupportInformResponse.tatal', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='custom_sender.ListSupportInformResponse.msg', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='custom_sender.ListSupportInformResponse.code', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTSUPPORTINFORMRESPONSE_DATA, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=44,
  serialized_end=327,
)


_LISTSUPPORTINFORMRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListSupportInformResponseWrapper',
  full_name='custom_sender.ListSupportInformResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='custom_sender.ListSupportInformResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='custom_sender.ListSupportInformResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='custom_sender.ListSupportInformResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='custom_sender.ListSupportInformResponseWrapper.data', index=3,
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
  serialized_start=330,
  serialized_end=470,
)

_LISTSUPPORTINFORMRESPONSE_DATA.containing_type = _LISTSUPPORTINFORMRESPONSE
_LISTSUPPORTINFORMRESPONSE.fields_by_name['data'].message_type = _LISTSUPPORTINFORMRESPONSE_DATA
_LISTSUPPORTINFORMRESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTSUPPORTINFORMRESPONSE
DESCRIPTOR.message_types_by_name['ListSupportInformResponse'] = _LISTSUPPORTINFORMRESPONSE
DESCRIPTOR.message_types_by_name['ListSupportInformResponseWrapper'] = _LISTSUPPORTINFORMRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListSupportInformResponse = _reflection.GeneratedProtocolMessageType('ListSupportInformResponse', (_message.Message,), {

  'Data' : _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), {
    'DESCRIPTOR' : _LISTSUPPORTINFORMRESPONSE_DATA,
    '__module__' : 'list_support_infom_pb2'
    # @@protoc_insertion_point(class_scope:custom_sender.ListSupportInformResponse.Data)
    })
  ,
  'DESCRIPTOR' : _LISTSUPPORTINFORMRESPONSE,
  '__module__' : 'list_support_infom_pb2'
  # @@protoc_insertion_point(class_scope:custom_sender.ListSupportInformResponse)
  })
_sym_db.RegisterMessage(ListSupportInformResponse)
_sym_db.RegisterMessage(ListSupportInformResponse.Data)

ListSupportInformResponseWrapper = _reflection.GeneratedProtocolMessageType('ListSupportInformResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _LISTSUPPORTINFORMRESPONSEWRAPPER,
  '__module__' : 'list_support_infom_pb2'
  # @@protoc_insertion_point(class_scope:custom_sender.ListSupportInformResponseWrapper)
  })
_sym_db.RegisterMessage(ListSupportInformResponseWrapper)


# @@protoc_insertion_point(module_scope)
