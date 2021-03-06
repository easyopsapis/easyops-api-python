# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list_agent_status_old.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='list_agent_status_old.proto',
  package='agent',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1blist_agent_status_old.proto\x12\x05\x61gent\"7\n\x19ListAgentStatusOldRequest\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0e\n\x06ip__in\x18\x02 \x01(\t\"\xe2\x03\n\x1aListAgentStatusOldResponse\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12\x34\n\x04list\x18\x04 \x03(\x0b\x32&.agent.ListAgentStatusOldResponse.List\x1a\xdd\x02\n\x04List\x12=\n\x06status\x18\x01 \x03(\x0b\x32-.agent.ListAgentStatusOldResponse.List.Status\x12\r\n\x05\x61live\x18\x02 \x01(\x08\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\x0c\n\x04uuid\x18\x04 \x01(\t\x12\x10\n\x08timezone\x18\x05 \x01(\x05\x12\x15\n\rhb_agent_time\x18\x06 \x01(\x05\x12\x16\n\x0ehb_server_time\x18\x07 \x01(\x05\x12\x12\n\nstart_time\x18\x08 \x01(\x05\x12\r\n\x05\x61gent\x18\t \x01(\t\x1a\x83\x01\n\x06Status\x12\x14\n\x0c\x63onnect_time\x18\x01 \x01(\x05\x12\x15\n\rhb_agent_time\x18\x02 \x01(\x05\x12\x16\n\x0ehb_server_time\x18\x03 \x01(\x05\x12\x12\n\nstart_time\x18\x04 \x01(\x05\x12\x0f\n\x07version\x18\x05 \x01(\t\x12\x0f\n\x07gateway\x18\x06 \x01(\t\"\x86\x01\n!ListAgentStatusOldResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12/\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32!.agent.ListAgentStatusOldResponseb\x06proto3')
)




_LISTAGENTSTATUSOLDREQUEST = _descriptor.Descriptor(
  name='ListAgentStatusOldRequest',
  full_name='agent.ListAgentStatusOldRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='agent.ListAgentStatusOldRequest.ip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip__in', full_name='agent.ListAgentStatusOldRequest.ip__in', index=1,
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
  serialized_end=93,
)


_LISTAGENTSTATUSOLDRESPONSE_LIST_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='agent.ListAgentStatusOldResponse.List.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='connect_time', full_name='agent.ListAgentStatusOldResponse.List.Status.connect_time', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hb_agent_time', full_name='agent.ListAgentStatusOldResponse.List.Status.hb_agent_time', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hb_server_time', full_name='agent.ListAgentStatusOldResponse.List.Status.hb_server_time', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='agent.ListAgentStatusOldResponse.List.Status.start_time', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='agent.ListAgentStatusOldResponse.List.Status.version', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gateway', full_name='agent.ListAgentStatusOldResponse.List.Status.gateway', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=447,
  serialized_end=578,
)

_LISTAGENTSTATUSOLDRESPONSE_LIST = _descriptor.Descriptor(
  name='List',
  full_name='agent.ListAgentStatusOldResponse.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='agent.ListAgentStatusOldResponse.List.status', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alive', full_name='agent.ListAgentStatusOldResponse.List.alive', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='agent.ListAgentStatusOldResponse.List.version', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='agent.ListAgentStatusOldResponse.List.uuid', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timezone', full_name='agent.ListAgentStatusOldResponse.List.timezone', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hb_agent_time', full_name='agent.ListAgentStatusOldResponse.List.hb_agent_time', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hb_server_time', full_name='agent.ListAgentStatusOldResponse.List.hb_server_time', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='agent.ListAgentStatusOldResponse.List.start_time', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agent', full_name='agent.ListAgentStatusOldResponse.List.agent', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTAGENTSTATUSOLDRESPONSE_LIST_STATUS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=229,
  serialized_end=578,
)

_LISTAGENTSTATUSOLDRESPONSE = _descriptor.Descriptor(
  name='ListAgentStatusOldResponse',
  full_name='agent.ListAgentStatusOldResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='agent.ListAgentStatusOldResponse.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='agent.ListAgentStatusOldResponse.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='agent.ListAgentStatusOldResponse.total', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='agent.ListAgentStatusOldResponse.list', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTAGENTSTATUSOLDRESPONSE_LIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=96,
  serialized_end=578,
)


_LISTAGENTSTATUSOLDRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListAgentStatusOldResponseWrapper',
  full_name='agent.ListAgentStatusOldResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='agent.ListAgentStatusOldResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='agent.ListAgentStatusOldResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='agent.ListAgentStatusOldResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='agent.ListAgentStatusOldResponseWrapper.data', index=3,
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
  serialized_start=581,
  serialized_end=715,
)

_LISTAGENTSTATUSOLDRESPONSE_LIST_STATUS.containing_type = _LISTAGENTSTATUSOLDRESPONSE_LIST
_LISTAGENTSTATUSOLDRESPONSE_LIST.fields_by_name['status'].message_type = _LISTAGENTSTATUSOLDRESPONSE_LIST_STATUS
_LISTAGENTSTATUSOLDRESPONSE_LIST.containing_type = _LISTAGENTSTATUSOLDRESPONSE
_LISTAGENTSTATUSOLDRESPONSE.fields_by_name['list'].message_type = _LISTAGENTSTATUSOLDRESPONSE_LIST
_LISTAGENTSTATUSOLDRESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTAGENTSTATUSOLDRESPONSE
DESCRIPTOR.message_types_by_name['ListAgentStatusOldRequest'] = _LISTAGENTSTATUSOLDREQUEST
DESCRIPTOR.message_types_by_name['ListAgentStatusOldResponse'] = _LISTAGENTSTATUSOLDRESPONSE
DESCRIPTOR.message_types_by_name['ListAgentStatusOldResponseWrapper'] = _LISTAGENTSTATUSOLDRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListAgentStatusOldRequest = _reflection.GeneratedProtocolMessageType('ListAgentStatusOldRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTAGENTSTATUSOLDREQUEST,
  '__module__' : 'list_agent_status_old_pb2'
  # @@protoc_insertion_point(class_scope:agent.ListAgentStatusOldRequest)
  })
_sym_db.RegisterMessage(ListAgentStatusOldRequest)

ListAgentStatusOldResponse = _reflection.GeneratedProtocolMessageType('ListAgentStatusOldResponse', (_message.Message,), {

  'List' : _reflection.GeneratedProtocolMessageType('List', (_message.Message,), {

    'Status' : _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
      'DESCRIPTOR' : _LISTAGENTSTATUSOLDRESPONSE_LIST_STATUS,
      '__module__' : 'list_agent_status_old_pb2'
      # @@protoc_insertion_point(class_scope:agent.ListAgentStatusOldResponse.List.Status)
      })
    ,
    'DESCRIPTOR' : _LISTAGENTSTATUSOLDRESPONSE_LIST,
    '__module__' : 'list_agent_status_old_pb2'
    # @@protoc_insertion_point(class_scope:agent.ListAgentStatusOldResponse.List)
    })
  ,
  'DESCRIPTOR' : _LISTAGENTSTATUSOLDRESPONSE,
  '__module__' : 'list_agent_status_old_pb2'
  # @@protoc_insertion_point(class_scope:agent.ListAgentStatusOldResponse)
  })
_sym_db.RegisterMessage(ListAgentStatusOldResponse)
_sym_db.RegisterMessage(ListAgentStatusOldResponse.List)
_sym_db.RegisterMessage(ListAgentStatusOldResponse.List.Status)

ListAgentStatusOldResponseWrapper = _reflection.GeneratedProtocolMessageType('ListAgentStatusOldResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _LISTAGENTSTATUSOLDRESPONSEWRAPPER,
  '__module__' : 'list_agent_status_old_pb2'
  # @@protoc_insertion_point(class_scope:agent.ListAgentStatusOldResponseWrapper)
  })
_sym_db.RegisterMessage(ListAgentStatusOldResponseWrapper)


# @@protoc_insertion_point(module_scope)
