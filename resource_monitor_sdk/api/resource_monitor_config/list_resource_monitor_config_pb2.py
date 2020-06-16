# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list_resource_monitor_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='list_resource_monitor_config.proto',
  package='resource_monitor_config',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\"list_resource_monitor_config.proto\x12\x17resource_monitor_config\"B\n ListResourceMonitorConfigRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x10\n\x08pageSize\x18\x02 \x01(\x05\"\xed\x01\n!ListResourceMonitorConfigResponse\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12M\n\x04list\x18\x04 \x03(\x0b\x32?.resource_monitor_config.ListResourceMonitorConfigResponse.List\x1aI\n\x04List\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\x12\x10\n\x08objectId\x18\x03 \x01(\t\x12\x12\n\nobjectName\x18\x04 \x01(\t\"\xa6\x01\n(ListResourceMonitorConfigResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12H\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32:.resource_monitor_config.ListResourceMonitorConfigResponseb\x06proto3')
)




_LISTRESOURCEMONITORCONFIGREQUEST = _descriptor.Descriptor(
  name='ListResourceMonitorConfigRequest',
  full_name='resource_monitor_config.ListResourceMonitorConfigRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='resource_monitor_config.ListResourceMonitorConfigRequest.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='resource_monitor_config.ListResourceMonitorConfigRequest.pageSize', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=63,
  serialized_end=129,
)


_LISTRESOURCEMONITORCONFIGRESPONSE_LIST = _descriptor.Descriptor(
  name='List',
  full_name='resource_monitor_config.ListResourceMonitorConfigResponse.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='resource_monitor_config.ListResourceMonitorConfigResponse.List.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enabled', full_name='resource_monitor_config.ListResourceMonitorConfigResponse.List.enabled', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectId', full_name='resource_monitor_config.ListResourceMonitorConfigResponse.List.objectId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectName', full_name='resource_monitor_config.ListResourceMonitorConfigResponse.List.objectName', index=3,
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
  serialized_start=296,
  serialized_end=369,
)

_LISTRESOURCEMONITORCONFIGRESPONSE = _descriptor.Descriptor(
  name='ListResourceMonitorConfigResponse',
  full_name='resource_monitor_config.ListResourceMonitorConfigResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='resource_monitor_config.ListResourceMonitorConfigResponse.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='resource_monitor_config.ListResourceMonitorConfigResponse.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='resource_monitor_config.ListResourceMonitorConfigResponse.total', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='resource_monitor_config.ListResourceMonitorConfigResponse.list', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTRESOURCEMONITORCONFIGRESPONSE_LIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=132,
  serialized_end=369,
)


_LISTRESOURCEMONITORCONFIGRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListResourceMonitorConfigResponseWrapper',
  full_name='resource_monitor_config.ListResourceMonitorConfigResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='resource_monitor_config.ListResourceMonitorConfigResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='resource_monitor_config.ListResourceMonitorConfigResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='resource_monitor_config.ListResourceMonitorConfigResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='resource_monitor_config.ListResourceMonitorConfigResponseWrapper.data', index=3,
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
  serialized_start=372,
  serialized_end=538,
)

_LISTRESOURCEMONITORCONFIGRESPONSE_LIST.containing_type = _LISTRESOURCEMONITORCONFIGRESPONSE
_LISTRESOURCEMONITORCONFIGRESPONSE.fields_by_name['list'].message_type = _LISTRESOURCEMONITORCONFIGRESPONSE_LIST
_LISTRESOURCEMONITORCONFIGRESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTRESOURCEMONITORCONFIGRESPONSE
DESCRIPTOR.message_types_by_name['ListResourceMonitorConfigRequest'] = _LISTRESOURCEMONITORCONFIGREQUEST
DESCRIPTOR.message_types_by_name['ListResourceMonitorConfigResponse'] = _LISTRESOURCEMONITORCONFIGRESPONSE
DESCRIPTOR.message_types_by_name['ListResourceMonitorConfigResponseWrapper'] = _LISTRESOURCEMONITORCONFIGRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListResourceMonitorConfigRequest = _reflection.GeneratedProtocolMessageType('ListResourceMonitorConfigRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTRESOURCEMONITORCONFIGREQUEST,
  '__module__' : 'list_resource_monitor_config_pb2'
  # @@protoc_insertion_point(class_scope:resource_monitor_config.ListResourceMonitorConfigRequest)
  })
_sym_db.RegisterMessage(ListResourceMonitorConfigRequest)

ListResourceMonitorConfigResponse = _reflection.GeneratedProtocolMessageType('ListResourceMonitorConfigResponse', (_message.Message,), {

  'List' : _reflection.GeneratedProtocolMessageType('List', (_message.Message,), {
    'DESCRIPTOR' : _LISTRESOURCEMONITORCONFIGRESPONSE_LIST,
    '__module__' : 'list_resource_monitor_config_pb2'
    # @@protoc_insertion_point(class_scope:resource_monitor_config.ListResourceMonitorConfigResponse.List)
    })
  ,
  'DESCRIPTOR' : _LISTRESOURCEMONITORCONFIGRESPONSE,
  '__module__' : 'list_resource_monitor_config_pb2'
  # @@protoc_insertion_point(class_scope:resource_monitor_config.ListResourceMonitorConfigResponse)
  })
_sym_db.RegisterMessage(ListResourceMonitorConfigResponse)
_sym_db.RegisterMessage(ListResourceMonitorConfigResponse.List)

ListResourceMonitorConfigResponseWrapper = _reflection.GeneratedProtocolMessageType('ListResourceMonitorConfigResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _LISTRESOURCEMONITORCONFIGRESPONSEWRAPPER,
  '__module__' : 'list_resource_monitor_config_pb2'
  # @@protoc_insertion_point(class_scope:resource_monitor_config.ListResourceMonitorConfigResponseWrapper)
  })
_sym_db.RegisterMessage(ListResourceMonitorConfigResponseWrapper)


# @@protoc_insertion_point(module_scope)
