# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list_collection_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='list_collection_config.proto',
  package='collection_config',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1clist_collection_config.proto\x12\x11\x63ollection_config\x1a\x1cgoogle/protobuf/struct.proto\"^\n\x1bListCollectionConfigRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x10\n\x08pageSize\x18\x02 \x01(\x05\x12\x10\n\x08\x64isabled\x18\x03 \x01(\x05\x12\r\n\x05isAll\x18\x04 \x01(\x05\"\xd5\t\n\x1cListCollectionConfigResponse\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12\x42\n\x04list\x18\x04 \x03(\x0b\x32\x34.collection_config.ListCollectionConfigResponse.List\x1a\xc0\x08\n\x04List\x12\x0b\n\x03org\x18\x01 \x01(\x05\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12K\n\x06kwargs\x18\x04 \x03(\x0b\x32;.collection_config.ListCollectionConfigResponse.List.Kwargs\x12\x0f\n\x07timeout\x18\x05 \x01(\x05\x12\x45\n\x03\x65nv\x18\x06 \x03(\x0b\x32\x38.collection_config.ListCollectionConfigResponse.List.Env\x12\x10\n\x08\x64isabled\x18\x07 \x01(\x08\x12\x0e\n\x06labels\x18\x08 \x03(\t\x12K\n\x06script\x18\t \x01(\x0b\x32;.collection_config.ListCollectionConfigResponse.List.Script\x12\x15\n\rignoreInvalid\x18\n \x01(\x08\x12Q\n\thostRange\x18\x0b \x01(\x0b\x32>.collection_config.ListCollectionConfigResponse.List.HostRange\x12\x10\n\x08interval\x18\x0c \x01(\x05\x12\x10\n\x08\x63\x61\x63heTtl\x18\r \x01(\x05\x12\x11\n\ttimeRange\x18\x0e \x01(\t\x12\x0f\n\x07\x63lazzId\x18\x0f \x01(\t\x12\x0f\n\x07\x63reator\x18\x10 \x01(\t\x12\x10\n\x08modifier\x18\x11 \x01(\t\x12\r\n\x05\x63time\x18\x12 \x01(\x05\x12\r\n\x05mtime\x18\x13 \x01(\x05\x12\x10\n\x08objectId\x18\x14 \x01(\t\x12\x17\n\x0finstanceIdMacro\x18\x15 \x01(\t\x1a<\n\x06Kwargs\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.Value\x1a\x39\n\x03\x45nv\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.Value\x1aR\n\x06Script\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x1a\x91\x02\n\tHostRange\x12\x10\n\x08objectId\x18\x01 \x01(\t\x12\x0f\n\x07hostKey\x18\x02 \x01(\t\x12\x0f\n\x07querier\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x13\n\x0bqueryString\x18\x05 \x01(\t\x12\x0f\n\x07queryId\x18\x06 \x01(\t\x12S\n\x05query\x18\x07 \x03(\x0b\x32\x44.collection_config.ListCollectionConfigResponse.List.HostRange.Query\x1aG\n\x05Query\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\n\n\x02op\x18\x02 \x01(\t\x12%\n\x05value\x18\x03 \x01(\x0b\x32\x16.google.protobuf.Value\"\x96\x01\n#ListCollectionConfigResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12=\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32/.collection_config.ListCollectionConfigResponseb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_LISTCOLLECTIONCONFIGREQUEST = _descriptor.Descriptor(
  name='ListCollectionConfigRequest',
  full_name='collection_config.ListCollectionConfigRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='collection_config.ListCollectionConfigRequest.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='collection_config.ListCollectionConfigRequest.pageSize', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disabled', full_name='collection_config.ListCollectionConfigRequest.disabled', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isAll', full_name='collection_config.ListCollectionConfigRequest.isAll', index=3,
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
  serialized_start=81,
  serialized_end=175,
)


_LISTCOLLECTIONCONFIGRESPONSE_LIST_KWARGS = _descriptor.Descriptor(
  name='Kwargs',
  full_name='collection_config.ListCollectionConfigResponse.List.Kwargs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='collection_config.ListCollectionConfigResponse.List.Kwargs.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='collection_config.ListCollectionConfigResponse.List.Kwargs.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=936,
  serialized_end=996,
)

_LISTCOLLECTIONCONFIGRESPONSE_LIST_ENV = _descriptor.Descriptor(
  name='Env',
  full_name='collection_config.ListCollectionConfigResponse.List.Env',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='collection_config.ListCollectionConfigResponse.List.Env.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='collection_config.ListCollectionConfigResponse.List.Env.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=998,
  serialized_end=1055,
)

_LISTCOLLECTIONCONFIGRESPONSE_LIST_SCRIPT = _descriptor.Descriptor(
  name='Script',
  full_name='collection_config.ListCollectionConfigResponse.List.Script',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='collection_config.ListCollectionConfigResponse.List.Script.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='collection_config.ListCollectionConfigResponse.List.Script.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='collection_config.ListCollectionConfigResponse.List.Script.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='collection_config.ListCollectionConfigResponse.List.Script.content', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='collection_config.ListCollectionConfigResponse.List.Script.name', index=4,
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
  serialized_start=1057,
  serialized_end=1139,
)

_LISTCOLLECTIONCONFIGRESPONSE_LIST_HOSTRANGE_QUERY = _descriptor.Descriptor(
  name='Query',
  full_name='collection_config.ListCollectionConfigResponse.List.HostRange.Query',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='collection_config.ListCollectionConfigResponse.List.HostRange.Query.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='op', full_name='collection_config.ListCollectionConfigResponse.List.HostRange.Query.op', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='collection_config.ListCollectionConfigResponse.List.HostRange.Query.value', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=1344,
  serialized_end=1415,
)

_LISTCOLLECTIONCONFIGRESPONSE_LIST_HOSTRANGE = _descriptor.Descriptor(
  name='HostRange',
  full_name='collection_config.ListCollectionConfigResponse.List.HostRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='objectId', full_name='collection_config.ListCollectionConfigResponse.List.HostRange.objectId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hostKey', full_name='collection_config.ListCollectionConfigResponse.List.HostRange.hostKey', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='querier', full_name='collection_config.ListCollectionConfigResponse.List.HostRange.querier', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='collection_config.ListCollectionConfigResponse.List.HostRange.type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='queryString', full_name='collection_config.ListCollectionConfigResponse.List.HostRange.queryString', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='queryId', full_name='collection_config.ListCollectionConfigResponse.List.HostRange.queryId', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='query', full_name='collection_config.ListCollectionConfigResponse.List.HostRange.query', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTCOLLECTIONCONFIGRESPONSE_LIST_HOSTRANGE_QUERY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1142,
  serialized_end=1415,
)

_LISTCOLLECTIONCONFIGRESPONSE_LIST = _descriptor.Descriptor(
  name='List',
  full_name='collection_config.ListCollectionConfigResponse.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='org', full_name='collection_config.ListCollectionConfigResponse.List.org', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='collection_config.ListCollectionConfigResponse.List.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='collection_config.ListCollectionConfigResponse.List.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kwargs', full_name='collection_config.ListCollectionConfigResponse.List.kwargs', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='collection_config.ListCollectionConfigResponse.List.timeout', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='env', full_name='collection_config.ListCollectionConfigResponse.List.env', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disabled', full_name='collection_config.ListCollectionConfigResponse.List.disabled', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='collection_config.ListCollectionConfigResponse.List.labels', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='script', full_name='collection_config.ListCollectionConfigResponse.List.script', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ignoreInvalid', full_name='collection_config.ListCollectionConfigResponse.List.ignoreInvalid', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hostRange', full_name='collection_config.ListCollectionConfigResponse.List.hostRange', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interval', full_name='collection_config.ListCollectionConfigResponse.List.interval', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cacheTtl', full_name='collection_config.ListCollectionConfigResponse.List.cacheTtl', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeRange', full_name='collection_config.ListCollectionConfigResponse.List.timeRange', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clazzId', full_name='collection_config.ListCollectionConfigResponse.List.clazzId', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='collection_config.ListCollectionConfigResponse.List.creator', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='modifier', full_name='collection_config.ListCollectionConfigResponse.List.modifier', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='collection_config.ListCollectionConfigResponse.List.ctime', index=17,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='collection_config.ListCollectionConfigResponse.List.mtime', index=18,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectId', full_name='collection_config.ListCollectionConfigResponse.List.objectId', index=19,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceIdMacro', full_name='collection_config.ListCollectionConfigResponse.List.instanceIdMacro', index=20,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTCOLLECTIONCONFIGRESPONSE_LIST_KWARGS, _LISTCOLLECTIONCONFIGRESPONSE_LIST_ENV, _LISTCOLLECTIONCONFIGRESPONSE_LIST_SCRIPT, _LISTCOLLECTIONCONFIGRESPONSE_LIST_HOSTRANGE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=327,
  serialized_end=1415,
)

_LISTCOLLECTIONCONFIGRESPONSE = _descriptor.Descriptor(
  name='ListCollectionConfigResponse',
  full_name='collection_config.ListCollectionConfigResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='collection_config.ListCollectionConfigResponse.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='collection_config.ListCollectionConfigResponse.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='collection_config.ListCollectionConfigResponse.total', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='collection_config.ListCollectionConfigResponse.list', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTCOLLECTIONCONFIGRESPONSE_LIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=178,
  serialized_end=1415,
)


_LISTCOLLECTIONCONFIGRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListCollectionConfigResponseWrapper',
  full_name='collection_config.ListCollectionConfigResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='collection_config.ListCollectionConfigResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='collection_config.ListCollectionConfigResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='collection_config.ListCollectionConfigResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='collection_config.ListCollectionConfigResponseWrapper.data', index=3,
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
  serialized_start=1418,
  serialized_end=1568,
)

_LISTCOLLECTIONCONFIGRESPONSE_LIST_KWARGS.fields_by_name['value'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_LISTCOLLECTIONCONFIGRESPONSE_LIST_KWARGS.containing_type = _LISTCOLLECTIONCONFIGRESPONSE_LIST
_LISTCOLLECTIONCONFIGRESPONSE_LIST_ENV.fields_by_name['value'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_LISTCOLLECTIONCONFIGRESPONSE_LIST_ENV.containing_type = _LISTCOLLECTIONCONFIGRESPONSE_LIST
_LISTCOLLECTIONCONFIGRESPONSE_LIST_SCRIPT.containing_type = _LISTCOLLECTIONCONFIGRESPONSE_LIST
_LISTCOLLECTIONCONFIGRESPONSE_LIST_HOSTRANGE_QUERY.fields_by_name['value'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_LISTCOLLECTIONCONFIGRESPONSE_LIST_HOSTRANGE_QUERY.containing_type = _LISTCOLLECTIONCONFIGRESPONSE_LIST_HOSTRANGE
_LISTCOLLECTIONCONFIGRESPONSE_LIST_HOSTRANGE.fields_by_name['query'].message_type = _LISTCOLLECTIONCONFIGRESPONSE_LIST_HOSTRANGE_QUERY
_LISTCOLLECTIONCONFIGRESPONSE_LIST_HOSTRANGE.containing_type = _LISTCOLLECTIONCONFIGRESPONSE_LIST
_LISTCOLLECTIONCONFIGRESPONSE_LIST.fields_by_name['kwargs'].message_type = _LISTCOLLECTIONCONFIGRESPONSE_LIST_KWARGS
_LISTCOLLECTIONCONFIGRESPONSE_LIST.fields_by_name['env'].message_type = _LISTCOLLECTIONCONFIGRESPONSE_LIST_ENV
_LISTCOLLECTIONCONFIGRESPONSE_LIST.fields_by_name['script'].message_type = _LISTCOLLECTIONCONFIGRESPONSE_LIST_SCRIPT
_LISTCOLLECTIONCONFIGRESPONSE_LIST.fields_by_name['hostRange'].message_type = _LISTCOLLECTIONCONFIGRESPONSE_LIST_HOSTRANGE
_LISTCOLLECTIONCONFIGRESPONSE_LIST.containing_type = _LISTCOLLECTIONCONFIGRESPONSE
_LISTCOLLECTIONCONFIGRESPONSE.fields_by_name['list'].message_type = _LISTCOLLECTIONCONFIGRESPONSE_LIST
_LISTCOLLECTIONCONFIGRESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTCOLLECTIONCONFIGRESPONSE
DESCRIPTOR.message_types_by_name['ListCollectionConfigRequest'] = _LISTCOLLECTIONCONFIGREQUEST
DESCRIPTOR.message_types_by_name['ListCollectionConfigResponse'] = _LISTCOLLECTIONCONFIGRESPONSE
DESCRIPTOR.message_types_by_name['ListCollectionConfigResponseWrapper'] = _LISTCOLLECTIONCONFIGRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListCollectionConfigRequest = _reflection.GeneratedProtocolMessageType('ListCollectionConfigRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTCOLLECTIONCONFIGREQUEST,
  '__module__' : 'list_collection_config_pb2'
  # @@protoc_insertion_point(class_scope:collection_config.ListCollectionConfigRequest)
  })
_sym_db.RegisterMessage(ListCollectionConfigRequest)

ListCollectionConfigResponse = _reflection.GeneratedProtocolMessageType('ListCollectionConfigResponse', (_message.Message,), {

  'List' : _reflection.GeneratedProtocolMessageType('List', (_message.Message,), {

    'Kwargs' : _reflection.GeneratedProtocolMessageType('Kwargs', (_message.Message,), {
      'DESCRIPTOR' : _LISTCOLLECTIONCONFIGRESPONSE_LIST_KWARGS,
      '__module__' : 'list_collection_config_pb2'
      # @@protoc_insertion_point(class_scope:collection_config.ListCollectionConfigResponse.List.Kwargs)
      })
    ,

    'Env' : _reflection.GeneratedProtocolMessageType('Env', (_message.Message,), {
      'DESCRIPTOR' : _LISTCOLLECTIONCONFIGRESPONSE_LIST_ENV,
      '__module__' : 'list_collection_config_pb2'
      # @@protoc_insertion_point(class_scope:collection_config.ListCollectionConfigResponse.List.Env)
      })
    ,

    'Script' : _reflection.GeneratedProtocolMessageType('Script', (_message.Message,), {
      'DESCRIPTOR' : _LISTCOLLECTIONCONFIGRESPONSE_LIST_SCRIPT,
      '__module__' : 'list_collection_config_pb2'
      # @@protoc_insertion_point(class_scope:collection_config.ListCollectionConfigResponse.List.Script)
      })
    ,

    'HostRange' : _reflection.GeneratedProtocolMessageType('HostRange', (_message.Message,), {

      'Query' : _reflection.GeneratedProtocolMessageType('Query', (_message.Message,), {
        'DESCRIPTOR' : _LISTCOLLECTIONCONFIGRESPONSE_LIST_HOSTRANGE_QUERY,
        '__module__' : 'list_collection_config_pb2'
        # @@protoc_insertion_point(class_scope:collection_config.ListCollectionConfigResponse.List.HostRange.Query)
        })
      ,
      'DESCRIPTOR' : _LISTCOLLECTIONCONFIGRESPONSE_LIST_HOSTRANGE,
      '__module__' : 'list_collection_config_pb2'
      # @@protoc_insertion_point(class_scope:collection_config.ListCollectionConfigResponse.List.HostRange)
      })
    ,
    'DESCRIPTOR' : _LISTCOLLECTIONCONFIGRESPONSE_LIST,
    '__module__' : 'list_collection_config_pb2'
    # @@protoc_insertion_point(class_scope:collection_config.ListCollectionConfigResponse.List)
    })
  ,
  'DESCRIPTOR' : _LISTCOLLECTIONCONFIGRESPONSE,
  '__module__' : 'list_collection_config_pb2'
  # @@protoc_insertion_point(class_scope:collection_config.ListCollectionConfigResponse)
  })
_sym_db.RegisterMessage(ListCollectionConfigResponse)
_sym_db.RegisterMessage(ListCollectionConfigResponse.List)
_sym_db.RegisterMessage(ListCollectionConfigResponse.List.Kwargs)
_sym_db.RegisterMessage(ListCollectionConfigResponse.List.Env)
_sym_db.RegisterMessage(ListCollectionConfigResponse.List.Script)
_sym_db.RegisterMessage(ListCollectionConfigResponse.List.HostRange)
_sym_db.RegisterMessage(ListCollectionConfigResponse.List.HostRange.Query)

ListCollectionConfigResponseWrapper = _reflection.GeneratedProtocolMessageType('ListCollectionConfigResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _LISTCOLLECTIONCONFIGRESPONSEWRAPPER,
  '__module__' : 'list_collection_config_pb2'
  # @@protoc_insertion_point(class_scope:collection_config.ListCollectionConfigResponseWrapper)
  })
_sym_db.RegisterMessage(ListCollectionConfigResponseWrapper)


# @@protoc_insertion_point(module_scope)