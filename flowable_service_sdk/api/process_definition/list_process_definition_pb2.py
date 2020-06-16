# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list_process_definition.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='list_process_definition.proto',
  package='process_definition',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1dlist_process_definition.proto\x12\x12process_definition\"\x8a\x01\n\x1cListProcessDefinitionRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x10\n\x08pageSize\x18\x02 \x01(\x05\x12\x10\n\x08\x63\x61tegory\x18\x03 \x01(\t\x12\x0e\n\x06isMain\x18\x04 \x01(\x08\x12\t\n\x01Q\x18\x05 \x01(\t\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x0f\n\x07\x63reator\x18\x07 \x01(\t\"\xf1\x03\n\x1dListProcessDefinitionResponse\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12\x44\n\x04list\x18\x04 \x03(\x0b\x32\x36.process_definition.ListProcessDefinitionResponse.List\x1a\xd9\x02\n\x04List\x12\x13\n\x0bvInstanceId\x18\x01 \x01(\t\x12\x10\n\x08vCreator\x18\x02 \x01(\t\x12\r\n\x05vMemo\x18\x03 \x01(\t\x12\x12\n\ninstanceId\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x06 \x01(\t\x12\x0f\n\x07\x63reator\x18\x07 \x01(\t\x12\x0c\n\x04memo\x18\x08 \x01(\t\x12\r\n\x05\x63time\x18\t \x01(\t\x12\x13\n\x0bversionName\x18\n \x01(\t\x12\x14\n\x0c\x64\x65ploymentId\x18\x0b \x01(\t\x12\x1c\n\x14\x66lowableDefinitionId\x18\x0c \x01(\t\x12\x1d\n\x15\x66lowableDefinitionKey\x18\r \x01(\t\x12\x0e\n\x06isMain\x18\x0e \x01(\x08\x12\r\n\x05state\x18\x0f \x01(\t\x12\x16\n\x0e\x64\x65ploymentTime\x18\x10 \x01(\t\x12\x1a\n\x12parentDeploymentId\x18\x11 \x01(\t\"\x99\x01\n$ListProcessDefinitionResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12?\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x31.process_definition.ListProcessDefinitionResponseb\x06proto3')
)




_LISTPROCESSDEFINITIONREQUEST = _descriptor.Descriptor(
  name='ListProcessDefinitionRequest',
  full_name='process_definition.ListProcessDefinitionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='process_definition.ListProcessDefinitionRequest.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='process_definition.ListProcessDefinitionRequest.pageSize', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='process_definition.ListProcessDefinitionRequest.category', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isMain', full_name='process_definition.ListProcessDefinitionRequest.isMain', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Q', full_name='process_definition.ListProcessDefinitionRequest.Q', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='process_definition.ListProcessDefinitionRequest.name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='process_definition.ListProcessDefinitionRequest.creator', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=54,
  serialized_end=192,
)


_LISTPROCESSDEFINITIONRESPONSE_LIST = _descriptor.Descriptor(
  name='List',
  full_name='process_definition.ListProcessDefinitionResponse.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vInstanceId', full_name='process_definition.ListProcessDefinitionResponse.List.vInstanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vCreator', full_name='process_definition.ListProcessDefinitionResponse.List.vCreator', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vMemo', full_name='process_definition.ListProcessDefinitionResponse.List.vMemo', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='process_definition.ListProcessDefinitionResponse.List.instanceId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='process_definition.ListProcessDefinitionResponse.List.name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='process_definition.ListProcessDefinitionResponse.List.category', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='process_definition.ListProcessDefinitionResponse.List.creator', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='process_definition.ListProcessDefinitionResponse.List.memo', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='process_definition.ListProcessDefinitionResponse.List.ctime', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionName', full_name='process_definition.ListProcessDefinitionResponse.List.versionName', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deploymentId', full_name='process_definition.ListProcessDefinitionResponse.List.deploymentId', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flowableDefinitionId', full_name='process_definition.ListProcessDefinitionResponse.List.flowableDefinitionId', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flowableDefinitionKey', full_name='process_definition.ListProcessDefinitionResponse.List.flowableDefinitionKey', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isMain', full_name='process_definition.ListProcessDefinitionResponse.List.isMain', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='process_definition.ListProcessDefinitionResponse.List.state', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deploymentTime', full_name='process_definition.ListProcessDefinitionResponse.List.deploymentTime', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parentDeploymentId', full_name='process_definition.ListProcessDefinitionResponse.List.parentDeploymentId', index=16,
      number=17, type=9, cpp_type=9, label=1,
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
  serialized_start=347,
  serialized_end=692,
)

_LISTPROCESSDEFINITIONRESPONSE = _descriptor.Descriptor(
  name='ListProcessDefinitionResponse',
  full_name='process_definition.ListProcessDefinitionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='process_definition.ListProcessDefinitionResponse.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='process_definition.ListProcessDefinitionResponse.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='process_definition.ListProcessDefinitionResponse.total', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='process_definition.ListProcessDefinitionResponse.list', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTPROCESSDEFINITIONRESPONSE_LIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=195,
  serialized_end=692,
)


_LISTPROCESSDEFINITIONRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListProcessDefinitionResponseWrapper',
  full_name='process_definition.ListProcessDefinitionResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='process_definition.ListProcessDefinitionResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='process_definition.ListProcessDefinitionResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='process_definition.ListProcessDefinitionResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='process_definition.ListProcessDefinitionResponseWrapper.data', index=3,
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
  serialized_start=695,
  serialized_end=848,
)

_LISTPROCESSDEFINITIONRESPONSE_LIST.containing_type = _LISTPROCESSDEFINITIONRESPONSE
_LISTPROCESSDEFINITIONRESPONSE.fields_by_name['list'].message_type = _LISTPROCESSDEFINITIONRESPONSE_LIST
_LISTPROCESSDEFINITIONRESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTPROCESSDEFINITIONRESPONSE
DESCRIPTOR.message_types_by_name['ListProcessDefinitionRequest'] = _LISTPROCESSDEFINITIONREQUEST
DESCRIPTOR.message_types_by_name['ListProcessDefinitionResponse'] = _LISTPROCESSDEFINITIONRESPONSE
DESCRIPTOR.message_types_by_name['ListProcessDefinitionResponseWrapper'] = _LISTPROCESSDEFINITIONRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListProcessDefinitionRequest = _reflection.GeneratedProtocolMessageType('ListProcessDefinitionRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTPROCESSDEFINITIONREQUEST,
  '__module__' : 'list_process_definition_pb2'
  # @@protoc_insertion_point(class_scope:process_definition.ListProcessDefinitionRequest)
  })
_sym_db.RegisterMessage(ListProcessDefinitionRequest)

ListProcessDefinitionResponse = _reflection.GeneratedProtocolMessageType('ListProcessDefinitionResponse', (_message.Message,), {

  'List' : _reflection.GeneratedProtocolMessageType('List', (_message.Message,), {
    'DESCRIPTOR' : _LISTPROCESSDEFINITIONRESPONSE_LIST,
    '__module__' : 'list_process_definition_pb2'
    # @@protoc_insertion_point(class_scope:process_definition.ListProcessDefinitionResponse.List)
    })
  ,
  'DESCRIPTOR' : _LISTPROCESSDEFINITIONRESPONSE,
  '__module__' : 'list_process_definition_pb2'
  # @@protoc_insertion_point(class_scope:process_definition.ListProcessDefinitionResponse)
  })
_sym_db.RegisterMessage(ListProcessDefinitionResponse)
_sym_db.RegisterMessage(ListProcessDefinitionResponse.List)

ListProcessDefinitionResponseWrapper = _reflection.GeneratedProtocolMessageType('ListProcessDefinitionResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _LISTPROCESSDEFINITIONRESPONSEWRAPPER,
  '__module__' : 'list_process_definition_pb2'
  # @@protoc_insertion_point(class_scope:process_definition.ListProcessDefinitionResponseWrapper)
  })
_sym_db.RegisterMessage(ListProcessDefinitionResponseWrapper)


# @@protoc_insertion_point(module_scope)
