# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list_collection_config_job.proto

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
  name='list_collection_config_job.proto',
  package='collection_config',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n list_collection_config_job.proto\x12\x11\x63ollection_config\x1a\x1cgoogle/protobuf/struct.proto\"1\n\x1fListCollectionConfigJobsRequest\x12\x0e\n\x06\x63onfId\x18\x01 \x01(\t\"\x84\t\n ListCollectionConfigJobsResponse\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12\x46\n\x04list\x18\x04 \x03(\x0b\x32\x38.collection_config.ListCollectionConfigJobsResponse.List\x1a\xe7\x07\n\x04List\x12\x10\n\x08interval\x18\x01 \x01(\x05\x12\x0f\n\x07timeout\x18\x02 \x01(\x05\x12\x11\n\ttimeRange\x18\x03 \x01(\t\x12K\n\x04host\x18\x04 \x01(\x0b\x32=.collection_config.ListCollectionConfigJobsResponse.List.Host\x12\x13\n\x0bmetricTable\x18\x05 \x01(\t\x12\x10\n\x08pluginId\x18\x06 \x01(\t\x12\x0c\n\x04name\x18\x07 \x01(\t\x12O\n\x06script\x18\x08 \x01(\x0b\x32?.collection_config.ListCollectionConfigJobsResponse.List.Script\x12\x0e\n\x06\x64\x61taId\x18\t \x01(\x05\x12I\n\x03\x65nv\x18\n \x03(\x0b\x32<.collection_config.ListCollectionConfigJobsResponse.List.Env\x12O\n\x06kwargs\x18\x0b \x03(\x0b\x32?.collection_config.ListCollectionConfigJobsResponse.List.Kwargs\x12\x0b\n\x03\x66un\x18\x0c \x01(\t\x12\x0f\n\x07\x63lazzId\x18\r \x01(\t\x12\x11\n\tclazzName\x18\x0e \x01(\t\x12\x13\n\x0bjobConfigId\x18\x0f \x01(\t\x12\x16\n\x0erequiredFields\x18\x10 \x03(\t\x12\x10\n\x08\x63\x61\x63heTtl\x18\x11 \x01(\x05\x12\x15\n\rignoreInvalid\x18\x12 \x01(\x08\x12\x0e\n\x06labels\x18\x13 \x03(\t\x12\x10\n\x08\x64isabled\x18\x14 \x01(\x08\x12\x0b\n\x03org\x18\x15 \x01(\x05\x12\n\n\x02id\x18\x16 \x01(\t\x12\x0f\n\x07\x63reator\x18\x17 \x01(\t\x12\x10\n\x08modifier\x18\x18 \x01(\t\x12\r\n\x05\x63time\x18\x19 \x01(\x05\x12\r\n\x05mtime\x18\x1a \x01(\x05\x12\x10\n\x08objectId\x18\x1b \x01(\t\x12\x12\n\ninstanceId\x18\x1c \x01(\t\x1a\x34\n\x04Host\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\n\n\x02ip\x18\x02 \x01(\t\x12\x0c\n\x04uuid\x18\x03 \x01(\t\x1aR\n\x06Script\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x1a\x39\n\x03\x45nv\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.Value\x1a<\n\x06Kwargs\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.Value\"\x9e\x01\n\'ListCollectionConfigJobsResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x41\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x33.collection_config.ListCollectionConfigJobsResponseb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_LISTCOLLECTIONCONFIGJOBSREQUEST = _descriptor.Descriptor(
  name='ListCollectionConfigJobsRequest',
  full_name='collection_config.ListCollectionConfigJobsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='confId', full_name='collection_config.ListCollectionConfigJobsRequest.confId', index=0,
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
  serialized_start=85,
  serialized_end=134,
)


_LISTCOLLECTIONCONFIGJOBSRESPONSE_LIST_HOST = _descriptor.Descriptor(
  name='Host',
  full_name='collection_config.ListCollectionConfigJobsResponse.List.Host',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='collection_config.ListCollectionConfigJobsResponse.List.Host.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip', full_name='collection_config.ListCollectionConfigJobsResponse.List.Host.ip', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='collection_config.ListCollectionConfigJobsResponse.List.Host.uuid', index=2,
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
  serialized_start=1036,
  serialized_end=1088,
)

_LISTCOLLECTIONCONFIGJOBSRESPONSE_LIST_SCRIPT = _descriptor.Descriptor(
  name='Script',
  full_name='collection_config.ListCollectionConfigJobsResponse.List.Script',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='collection_config.ListCollectionConfigJobsResponse.List.Script.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='collection_config.ListCollectionConfigJobsResponse.List.Script.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='collection_config.ListCollectionConfigJobsResponse.List.Script.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='collection_config.ListCollectionConfigJobsResponse.List.Script.content', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='collection_config.ListCollectionConfigJobsResponse.List.Script.name', index=4,
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
  serialized_start=1090,
  serialized_end=1172,
)

_LISTCOLLECTIONCONFIGJOBSRESPONSE_LIST_ENV = _descriptor.Descriptor(
  name='Env',
  full_name='collection_config.ListCollectionConfigJobsResponse.List.Env',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='collection_config.ListCollectionConfigJobsResponse.List.Env.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='collection_config.ListCollectionConfigJobsResponse.List.Env.value', index=1,
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
  serialized_start=1174,
  serialized_end=1231,
)

_LISTCOLLECTIONCONFIGJOBSRESPONSE_LIST_KWARGS = _descriptor.Descriptor(
  name='Kwargs',
  full_name='collection_config.ListCollectionConfigJobsResponse.List.Kwargs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='collection_config.ListCollectionConfigJobsResponse.List.Kwargs.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='collection_config.ListCollectionConfigJobsResponse.List.Kwargs.value', index=1,
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
  serialized_start=1233,
  serialized_end=1293,
)

_LISTCOLLECTIONCONFIGJOBSRESPONSE_LIST = _descriptor.Descriptor(
  name='List',
  full_name='collection_config.ListCollectionConfigJobsResponse.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='interval', full_name='collection_config.ListCollectionConfigJobsResponse.List.interval', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='collection_config.ListCollectionConfigJobsResponse.List.timeout', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeRange', full_name='collection_config.ListCollectionConfigJobsResponse.List.timeRange', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host', full_name='collection_config.ListCollectionConfigJobsResponse.List.host', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metricTable', full_name='collection_config.ListCollectionConfigJobsResponse.List.metricTable', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pluginId', full_name='collection_config.ListCollectionConfigJobsResponse.List.pluginId', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='collection_config.ListCollectionConfigJobsResponse.List.name', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='script', full_name='collection_config.ListCollectionConfigJobsResponse.List.script', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataId', full_name='collection_config.ListCollectionConfigJobsResponse.List.dataId', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='env', full_name='collection_config.ListCollectionConfigJobsResponse.List.env', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kwargs', full_name='collection_config.ListCollectionConfigJobsResponse.List.kwargs', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fun', full_name='collection_config.ListCollectionConfigJobsResponse.List.fun', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clazzId', full_name='collection_config.ListCollectionConfigJobsResponse.List.clazzId', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clazzName', full_name='collection_config.ListCollectionConfigJobsResponse.List.clazzName', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='jobConfigId', full_name='collection_config.ListCollectionConfigJobsResponse.List.jobConfigId', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requiredFields', full_name='collection_config.ListCollectionConfigJobsResponse.List.requiredFields', index=15,
      number=16, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cacheTtl', full_name='collection_config.ListCollectionConfigJobsResponse.List.cacheTtl', index=16,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ignoreInvalid', full_name='collection_config.ListCollectionConfigJobsResponse.List.ignoreInvalid', index=17,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='collection_config.ListCollectionConfigJobsResponse.List.labels', index=18,
      number=19, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disabled', full_name='collection_config.ListCollectionConfigJobsResponse.List.disabled', index=19,
      number=20, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org', full_name='collection_config.ListCollectionConfigJobsResponse.List.org', index=20,
      number=21, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='collection_config.ListCollectionConfigJobsResponse.List.id', index=21,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='collection_config.ListCollectionConfigJobsResponse.List.creator', index=22,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='modifier', full_name='collection_config.ListCollectionConfigJobsResponse.List.modifier', index=23,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='collection_config.ListCollectionConfigJobsResponse.List.ctime', index=24,
      number=25, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='collection_config.ListCollectionConfigJobsResponse.List.mtime', index=25,
      number=26, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectId', full_name='collection_config.ListCollectionConfigJobsResponse.List.objectId', index=26,
      number=27, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='collection_config.ListCollectionConfigJobsResponse.List.instanceId', index=27,
      number=28, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTCOLLECTIONCONFIGJOBSRESPONSE_LIST_HOST, _LISTCOLLECTIONCONFIGJOBSRESPONSE_LIST_SCRIPT, _LISTCOLLECTIONCONFIGJOBSRESPONSE_LIST_ENV, _LISTCOLLECTIONCONFIGJOBSRESPONSE_LIST_KWARGS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=294,
  serialized_end=1293,
)

_LISTCOLLECTIONCONFIGJOBSRESPONSE = _descriptor.Descriptor(
  name='ListCollectionConfigJobsResponse',
  full_name='collection_config.ListCollectionConfigJobsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='collection_config.ListCollectionConfigJobsResponse.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='collection_config.ListCollectionConfigJobsResponse.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='collection_config.ListCollectionConfigJobsResponse.total', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='collection_config.ListCollectionConfigJobsResponse.list', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTCOLLECTIONCONFIGJOBSRESPONSE_LIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=137,
  serialized_end=1293,
)


_LISTCOLLECTIONCONFIGJOBSRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListCollectionConfigJobsResponseWrapper',
  full_name='collection_config.ListCollectionConfigJobsResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='collection_config.ListCollectionConfigJobsResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='collection_config.ListCollectionConfigJobsResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='collection_config.ListCollectionConfigJobsResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='collection_config.ListCollectionConfigJobsResponseWrapper.data', index=3,
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
  serialized_start=1296,
  serialized_end=1454,
)

_LISTCOLLECTIONCONFIGJOBSRESPONSE_LIST_HOST.containing_type = _LISTCOLLECTIONCONFIGJOBSRESPONSE_LIST
_LISTCOLLECTIONCONFIGJOBSRESPONSE_LIST_SCRIPT.containing_type = _LISTCOLLECTIONCONFIGJOBSRESPONSE_LIST
_LISTCOLLECTIONCONFIGJOBSRESPONSE_LIST_ENV.fields_by_name['value'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_LISTCOLLECTIONCONFIGJOBSRESPONSE_LIST_ENV.containing_type = _LISTCOLLECTIONCONFIGJOBSRESPONSE_LIST
_LISTCOLLECTIONCONFIGJOBSRESPONSE_LIST_KWARGS.fields_by_name['value'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_LISTCOLLECTIONCONFIGJOBSRESPONSE_LIST_KWARGS.containing_type = _LISTCOLLECTIONCONFIGJOBSRESPONSE_LIST
_LISTCOLLECTIONCONFIGJOBSRESPONSE_LIST.fields_by_name['host'].message_type = _LISTCOLLECTIONCONFIGJOBSRESPONSE_LIST_HOST
_LISTCOLLECTIONCONFIGJOBSRESPONSE_LIST.fields_by_name['script'].message_type = _LISTCOLLECTIONCONFIGJOBSRESPONSE_LIST_SCRIPT
_LISTCOLLECTIONCONFIGJOBSRESPONSE_LIST.fields_by_name['env'].message_type = _LISTCOLLECTIONCONFIGJOBSRESPONSE_LIST_ENV
_LISTCOLLECTIONCONFIGJOBSRESPONSE_LIST.fields_by_name['kwargs'].message_type = _LISTCOLLECTIONCONFIGJOBSRESPONSE_LIST_KWARGS
_LISTCOLLECTIONCONFIGJOBSRESPONSE_LIST.containing_type = _LISTCOLLECTIONCONFIGJOBSRESPONSE
_LISTCOLLECTIONCONFIGJOBSRESPONSE.fields_by_name['list'].message_type = _LISTCOLLECTIONCONFIGJOBSRESPONSE_LIST
_LISTCOLLECTIONCONFIGJOBSRESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTCOLLECTIONCONFIGJOBSRESPONSE
DESCRIPTOR.message_types_by_name['ListCollectionConfigJobsRequest'] = _LISTCOLLECTIONCONFIGJOBSREQUEST
DESCRIPTOR.message_types_by_name['ListCollectionConfigJobsResponse'] = _LISTCOLLECTIONCONFIGJOBSRESPONSE
DESCRIPTOR.message_types_by_name['ListCollectionConfigJobsResponseWrapper'] = _LISTCOLLECTIONCONFIGJOBSRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListCollectionConfigJobsRequest = _reflection.GeneratedProtocolMessageType('ListCollectionConfigJobsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTCOLLECTIONCONFIGJOBSREQUEST,
  '__module__' : 'list_collection_config_job_pb2'
  # @@protoc_insertion_point(class_scope:collection_config.ListCollectionConfigJobsRequest)
  })
_sym_db.RegisterMessage(ListCollectionConfigJobsRequest)

ListCollectionConfigJobsResponse = _reflection.GeneratedProtocolMessageType('ListCollectionConfigJobsResponse', (_message.Message,), {

  'List' : _reflection.GeneratedProtocolMessageType('List', (_message.Message,), {

    'Host' : _reflection.GeneratedProtocolMessageType('Host', (_message.Message,), {
      'DESCRIPTOR' : _LISTCOLLECTIONCONFIGJOBSRESPONSE_LIST_HOST,
      '__module__' : 'list_collection_config_job_pb2'
      # @@protoc_insertion_point(class_scope:collection_config.ListCollectionConfigJobsResponse.List.Host)
      })
    ,

    'Script' : _reflection.GeneratedProtocolMessageType('Script', (_message.Message,), {
      'DESCRIPTOR' : _LISTCOLLECTIONCONFIGJOBSRESPONSE_LIST_SCRIPT,
      '__module__' : 'list_collection_config_job_pb2'
      # @@protoc_insertion_point(class_scope:collection_config.ListCollectionConfigJobsResponse.List.Script)
      })
    ,

    'Env' : _reflection.GeneratedProtocolMessageType('Env', (_message.Message,), {
      'DESCRIPTOR' : _LISTCOLLECTIONCONFIGJOBSRESPONSE_LIST_ENV,
      '__module__' : 'list_collection_config_job_pb2'
      # @@protoc_insertion_point(class_scope:collection_config.ListCollectionConfigJobsResponse.List.Env)
      })
    ,

    'Kwargs' : _reflection.GeneratedProtocolMessageType('Kwargs', (_message.Message,), {
      'DESCRIPTOR' : _LISTCOLLECTIONCONFIGJOBSRESPONSE_LIST_KWARGS,
      '__module__' : 'list_collection_config_job_pb2'
      # @@protoc_insertion_point(class_scope:collection_config.ListCollectionConfigJobsResponse.List.Kwargs)
      })
    ,
    'DESCRIPTOR' : _LISTCOLLECTIONCONFIGJOBSRESPONSE_LIST,
    '__module__' : 'list_collection_config_job_pb2'
    # @@protoc_insertion_point(class_scope:collection_config.ListCollectionConfigJobsResponse.List)
    })
  ,
  'DESCRIPTOR' : _LISTCOLLECTIONCONFIGJOBSRESPONSE,
  '__module__' : 'list_collection_config_job_pb2'
  # @@protoc_insertion_point(class_scope:collection_config.ListCollectionConfigJobsResponse)
  })
_sym_db.RegisterMessage(ListCollectionConfigJobsResponse)
_sym_db.RegisterMessage(ListCollectionConfigJobsResponse.List)
_sym_db.RegisterMessage(ListCollectionConfigJobsResponse.List.Host)
_sym_db.RegisterMessage(ListCollectionConfigJobsResponse.List.Script)
_sym_db.RegisterMessage(ListCollectionConfigJobsResponse.List.Env)
_sym_db.RegisterMessage(ListCollectionConfigJobsResponse.List.Kwargs)

ListCollectionConfigJobsResponseWrapper = _reflection.GeneratedProtocolMessageType('ListCollectionConfigJobsResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _LISTCOLLECTIONCONFIGJOBSRESPONSEWRAPPER,
  '__module__' : 'list_collection_config_job_pb2'
  # @@protoc_insertion_point(class_scope:collection_config.ListCollectionConfigJobsResponseWrapper)
  })
_sym_db.RegisterMessage(ListCollectionConfigJobsResponseWrapper)


# @@protoc_insertion_point(module_scope)