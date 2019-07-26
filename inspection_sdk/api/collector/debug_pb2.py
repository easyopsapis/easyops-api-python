# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: debug.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='debug.proto',
  package='collector',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0b\x64\x65\x62ug.proto\x12\tcollector\"\xb3\x01\n\x15\x44\x65\x62ugCollectorRequest\x12\x10\n\x08pluginId\x18\x01 \x01(\t\x12\x0e\n\x06target\x18\x02 \x01(\t\x12\x33\n\x04\x61rgs\x18\x03 \x03(\x0b\x32%.collector.DebugCollectorRequest.Args\x12\x0e\n\x06script\x18\x04 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x05 \x01(\t\x1a\"\n\x04\x41rgs\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x9e\x06\n\x16\x44\x65\x62ugCollectorResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x45\n\rmetric_groups\x18\x03 \x03(\x0b\x32..collector.DebugCollectorResponse.MetricGroups\x1a\x9f\x05\n\x0cMetricGroups\x12\x1b\n\x13metric_group_status\x18\x01 \x01(\t\x12L\n\ndim_status\x18\x02 \x03(\x0b\x32\x38.collector.DebugCollectorResponse.MetricGroups.DimStatus\x12L\n\nval_status\x18\x03 \x03(\x0b\x32\x38.collector.DebugCollectorResponse.MetricGroups.ValStatus\x12\x41\n\x04list\x18\x04 \x03(\x0b\x32\x33.collector.DebugCollectorResponse.MetricGroups.List\x12\n\n\x02id\x18\x05 \x01(\t\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x07 \x01(\t\x1a\x35\n\tDimStatus\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x1aQ\n\tValStatus\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x0c\n\x04unit\x18\x05 \x01(\t\x1a\xdc\x01\n\x04List\x12\x46\n\x04\x64ims\x18\x01 \x03(\x0b\x32\x38.collector.DebugCollectorResponse.MetricGroups.List.Dims\x12\x46\n\x04vals\x18\x02 \x03(\x0b\x32\x38.collector.DebugCollectorResponse.MetricGroups.List.Vals\x1a!\n\x04\x44ims\x12\r\n\x05value\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x1a!\n\x04Vals\x12\r\n\x05value\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\"\x82\x01\n\x1d\x44\x65\x62ugCollectorResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12/\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32!.collector.DebugCollectorResponseb\x06proto3')
)




_DEBUGCOLLECTORREQUEST_ARGS = _descriptor.Descriptor(
  name='Args',
  full_name='collector.DebugCollectorRequest.Args',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='collector.DebugCollectorRequest.Args.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='collector.DebugCollectorRequest.Args.value', index=1,
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
  serialized_start=172,
  serialized_end=206,
)

_DEBUGCOLLECTORREQUEST = _descriptor.Descriptor(
  name='DebugCollectorRequest',
  full_name='collector.DebugCollectorRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pluginId', full_name='collector.DebugCollectorRequest.pluginId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target', full_name='collector.DebugCollectorRequest.target', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='args', full_name='collector.DebugCollectorRequest.args', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='script', full_name='collector.DebugCollectorRequest.script', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='collector.DebugCollectorRequest.content', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DEBUGCOLLECTORREQUEST_ARGS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=206,
)


_DEBUGCOLLECTORRESPONSE_METRICGROUPS_DIMSTATUS = _descriptor.Descriptor(
  name='DimStatus',
  full_name='collector.DebugCollectorResponse.MetricGroups.DimStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='collector.DebugCollectorResponse.MetricGroups.DimStatus.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='collector.DebugCollectorResponse.MetricGroups.DimStatus.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='collector.DebugCollectorResponse.MetricGroups.DimStatus.name', index=2,
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
  serialized_start=648,
  serialized_end=701,
)

_DEBUGCOLLECTORRESPONSE_METRICGROUPS_VALSTATUS = _descriptor.Descriptor(
  name='ValStatus',
  full_name='collector.DebugCollectorResponse.MetricGroups.ValStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='collector.DebugCollectorResponse.MetricGroups.ValStatus.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='collector.DebugCollectorResponse.MetricGroups.ValStatus.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='collector.DebugCollectorResponse.MetricGroups.ValStatus.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='collector.DebugCollectorResponse.MetricGroups.ValStatus.type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unit', full_name='collector.DebugCollectorResponse.MetricGroups.ValStatus.unit', index=4,
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
  serialized_start=703,
  serialized_end=784,
)

_DEBUGCOLLECTORRESPONSE_METRICGROUPS_LIST_DIMS = _descriptor.Descriptor(
  name='Dims',
  full_name='collector.DebugCollectorResponse.MetricGroups.List.Dims',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='collector.DebugCollectorResponse.MetricGroups.List.Dims.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='collector.DebugCollectorResponse.MetricGroups.List.Dims.id', index=1,
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
  serialized_start=939,
  serialized_end=972,
)

_DEBUGCOLLECTORRESPONSE_METRICGROUPS_LIST_VALS = _descriptor.Descriptor(
  name='Vals',
  full_name='collector.DebugCollectorResponse.MetricGroups.List.Vals',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='collector.DebugCollectorResponse.MetricGroups.List.Vals.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='collector.DebugCollectorResponse.MetricGroups.List.Vals.id', index=1,
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
  serialized_start=974,
  serialized_end=1007,
)

_DEBUGCOLLECTORRESPONSE_METRICGROUPS_LIST = _descriptor.Descriptor(
  name='List',
  full_name='collector.DebugCollectorResponse.MetricGroups.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dims', full_name='collector.DebugCollectorResponse.MetricGroups.List.dims', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vals', full_name='collector.DebugCollectorResponse.MetricGroups.List.vals', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DEBUGCOLLECTORRESPONSE_METRICGROUPS_LIST_DIMS, _DEBUGCOLLECTORRESPONSE_METRICGROUPS_LIST_VALS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=787,
  serialized_end=1007,
)

_DEBUGCOLLECTORRESPONSE_METRICGROUPS = _descriptor.Descriptor(
  name='MetricGroups',
  full_name='collector.DebugCollectorResponse.MetricGroups',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metric_group_status', full_name='collector.DebugCollectorResponse.MetricGroups.metric_group_status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dim_status', full_name='collector.DebugCollectorResponse.MetricGroups.dim_status', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='val_status', full_name='collector.DebugCollectorResponse.MetricGroups.val_status', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='collector.DebugCollectorResponse.MetricGroups.list', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='collector.DebugCollectorResponse.MetricGroups.id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='collector.DebugCollectorResponse.MetricGroups.name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='collector.DebugCollectorResponse.MetricGroups.category', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DEBUGCOLLECTORRESPONSE_METRICGROUPS_DIMSTATUS, _DEBUGCOLLECTORRESPONSE_METRICGROUPS_VALSTATUS, _DEBUGCOLLECTORRESPONSE_METRICGROUPS_LIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=336,
  serialized_end=1007,
)

_DEBUGCOLLECTORRESPONSE = _descriptor.Descriptor(
  name='DebugCollectorResponse',
  full_name='collector.DebugCollectorResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='collector.DebugCollectorResponse.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='collector.DebugCollectorResponse.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metric_groups', full_name='collector.DebugCollectorResponse.metric_groups', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DEBUGCOLLECTORRESPONSE_METRICGROUPS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=209,
  serialized_end=1007,
)


_DEBUGCOLLECTORRESPONSEWRAPPER = _descriptor.Descriptor(
  name='DebugCollectorResponseWrapper',
  full_name='collector.DebugCollectorResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='collector.DebugCollectorResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='collector.DebugCollectorResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='collector.DebugCollectorResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='collector.DebugCollectorResponseWrapper.data', index=3,
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
  serialized_start=1010,
  serialized_end=1140,
)

_DEBUGCOLLECTORREQUEST_ARGS.containing_type = _DEBUGCOLLECTORREQUEST
_DEBUGCOLLECTORREQUEST.fields_by_name['args'].message_type = _DEBUGCOLLECTORREQUEST_ARGS
_DEBUGCOLLECTORRESPONSE_METRICGROUPS_DIMSTATUS.containing_type = _DEBUGCOLLECTORRESPONSE_METRICGROUPS
_DEBUGCOLLECTORRESPONSE_METRICGROUPS_VALSTATUS.containing_type = _DEBUGCOLLECTORRESPONSE_METRICGROUPS
_DEBUGCOLLECTORRESPONSE_METRICGROUPS_LIST_DIMS.containing_type = _DEBUGCOLLECTORRESPONSE_METRICGROUPS_LIST
_DEBUGCOLLECTORRESPONSE_METRICGROUPS_LIST_VALS.containing_type = _DEBUGCOLLECTORRESPONSE_METRICGROUPS_LIST
_DEBUGCOLLECTORRESPONSE_METRICGROUPS_LIST.fields_by_name['dims'].message_type = _DEBUGCOLLECTORRESPONSE_METRICGROUPS_LIST_DIMS
_DEBUGCOLLECTORRESPONSE_METRICGROUPS_LIST.fields_by_name['vals'].message_type = _DEBUGCOLLECTORRESPONSE_METRICGROUPS_LIST_VALS
_DEBUGCOLLECTORRESPONSE_METRICGROUPS_LIST.containing_type = _DEBUGCOLLECTORRESPONSE_METRICGROUPS
_DEBUGCOLLECTORRESPONSE_METRICGROUPS.fields_by_name['dim_status'].message_type = _DEBUGCOLLECTORRESPONSE_METRICGROUPS_DIMSTATUS
_DEBUGCOLLECTORRESPONSE_METRICGROUPS.fields_by_name['val_status'].message_type = _DEBUGCOLLECTORRESPONSE_METRICGROUPS_VALSTATUS
_DEBUGCOLLECTORRESPONSE_METRICGROUPS.fields_by_name['list'].message_type = _DEBUGCOLLECTORRESPONSE_METRICGROUPS_LIST
_DEBUGCOLLECTORRESPONSE_METRICGROUPS.containing_type = _DEBUGCOLLECTORRESPONSE
_DEBUGCOLLECTORRESPONSE.fields_by_name['metric_groups'].message_type = _DEBUGCOLLECTORRESPONSE_METRICGROUPS
_DEBUGCOLLECTORRESPONSEWRAPPER.fields_by_name['data'].message_type = _DEBUGCOLLECTORRESPONSE
DESCRIPTOR.message_types_by_name['DebugCollectorRequest'] = _DEBUGCOLLECTORREQUEST
DESCRIPTOR.message_types_by_name['DebugCollectorResponse'] = _DEBUGCOLLECTORRESPONSE
DESCRIPTOR.message_types_by_name['DebugCollectorResponseWrapper'] = _DEBUGCOLLECTORRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DebugCollectorRequest = _reflection.GeneratedProtocolMessageType('DebugCollectorRequest', (_message.Message,), dict(

  Args = _reflection.GeneratedProtocolMessageType('Args', (_message.Message,), dict(
    DESCRIPTOR = _DEBUGCOLLECTORREQUEST_ARGS,
    __module__ = 'debug_pb2'
    # @@protoc_insertion_point(class_scope:collector.DebugCollectorRequest.Args)
    ))
  ,
  DESCRIPTOR = _DEBUGCOLLECTORREQUEST,
  __module__ = 'debug_pb2'
  # @@protoc_insertion_point(class_scope:collector.DebugCollectorRequest)
  ))
_sym_db.RegisterMessage(DebugCollectorRequest)
_sym_db.RegisterMessage(DebugCollectorRequest.Args)

DebugCollectorResponse = _reflection.GeneratedProtocolMessageType('DebugCollectorResponse', (_message.Message,), dict(

  MetricGroups = _reflection.GeneratedProtocolMessageType('MetricGroups', (_message.Message,), dict(

    DimStatus = _reflection.GeneratedProtocolMessageType('DimStatus', (_message.Message,), dict(
      DESCRIPTOR = _DEBUGCOLLECTORRESPONSE_METRICGROUPS_DIMSTATUS,
      __module__ = 'debug_pb2'
      # @@protoc_insertion_point(class_scope:collector.DebugCollectorResponse.MetricGroups.DimStatus)
      ))
    ,

    ValStatus = _reflection.GeneratedProtocolMessageType('ValStatus', (_message.Message,), dict(
      DESCRIPTOR = _DEBUGCOLLECTORRESPONSE_METRICGROUPS_VALSTATUS,
      __module__ = 'debug_pb2'
      # @@protoc_insertion_point(class_scope:collector.DebugCollectorResponse.MetricGroups.ValStatus)
      ))
    ,

    List = _reflection.GeneratedProtocolMessageType('List', (_message.Message,), dict(

      Dims = _reflection.GeneratedProtocolMessageType('Dims', (_message.Message,), dict(
        DESCRIPTOR = _DEBUGCOLLECTORRESPONSE_METRICGROUPS_LIST_DIMS,
        __module__ = 'debug_pb2'
        # @@protoc_insertion_point(class_scope:collector.DebugCollectorResponse.MetricGroups.List.Dims)
        ))
      ,

      Vals = _reflection.GeneratedProtocolMessageType('Vals', (_message.Message,), dict(
        DESCRIPTOR = _DEBUGCOLLECTORRESPONSE_METRICGROUPS_LIST_VALS,
        __module__ = 'debug_pb2'
        # @@protoc_insertion_point(class_scope:collector.DebugCollectorResponse.MetricGroups.List.Vals)
        ))
      ,
      DESCRIPTOR = _DEBUGCOLLECTORRESPONSE_METRICGROUPS_LIST,
      __module__ = 'debug_pb2'
      # @@protoc_insertion_point(class_scope:collector.DebugCollectorResponse.MetricGroups.List)
      ))
    ,
    DESCRIPTOR = _DEBUGCOLLECTORRESPONSE_METRICGROUPS,
    __module__ = 'debug_pb2'
    # @@protoc_insertion_point(class_scope:collector.DebugCollectorResponse.MetricGroups)
    ))
  ,
  DESCRIPTOR = _DEBUGCOLLECTORRESPONSE,
  __module__ = 'debug_pb2'
  # @@protoc_insertion_point(class_scope:collector.DebugCollectorResponse)
  ))
_sym_db.RegisterMessage(DebugCollectorResponse)
_sym_db.RegisterMessage(DebugCollectorResponse.MetricGroups)
_sym_db.RegisterMessage(DebugCollectorResponse.MetricGroups.DimStatus)
_sym_db.RegisterMessage(DebugCollectorResponse.MetricGroups.ValStatus)
_sym_db.RegisterMessage(DebugCollectorResponse.MetricGroups.List)
_sym_db.RegisterMessage(DebugCollectorResponse.MetricGroups.List.Dims)
_sym_db.RegisterMessage(DebugCollectorResponse.MetricGroups.List.Vals)

DebugCollectorResponseWrapper = _reflection.GeneratedProtocolMessageType('DebugCollectorResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _DEBUGCOLLECTORRESPONSEWRAPPER,
  __module__ = 'debug_pb2'
  # @@protoc_insertion_point(class_scope:collector.DebugCollectorResponseWrapper)
  ))
_sym_db.RegisterMessage(DebugCollectorResponseWrapper)


# @@protoc_insertion_point(module_scope)
