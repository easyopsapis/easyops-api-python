# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list_abnormal_metrics.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from model.inspection import dim_pb2 as model_dot_inspection_dot_dim__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='list_abnormal_metrics.proto',
  package='history',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1blist_abnormal_metrics.proto\x12\x07history\x1a\x1amodel/inspection/dim.proto\"Q\n\x1aListAbnormalMetricsRequest\x12\x10\n\x08pluginId\x18\x01 \x01(\t\x12\r\n\x05jobId\x18\x02 \x01(\t\x12\x12\n\ninstanceId\x18\x03 \x01(\t\"\xd9\x04\n\x1bListAbnormalMetricsResponse\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\r\n\x05total\x18\x03 \x01(\x05\x12\x37\n\x04list\x18\x04 \x03(\x0b\x32).history.ListAbnormalMetricsResponse.List\x1a\xd0\x03\n\x04List\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x10\n\x08targetId\x18\x02 \x01(\t\x12\x0b\n\x03log\x18\x03 \x01(\t\x12\\\n\x14\x61\x62normalMetricGroups\x18\x04 \x01(\x0b\x32>.history.ListAbnormalMetricsResponse.List.AbnormalMetricGroups\x1a\xbe\x02\n\x14\x41\x62normalMetricGroups\x12\'\n\x04\x64ims\x18\x01 \x03(\x0b\x32\x19.inspection.InspectionDim\x12\x15\n\rmetricGroupId\x18\x02 \x01(\t\x12\x17\n\x0fmetricGroupName\x18\x03 \x01(\t\x12g\n\x0f\x61\x62normalMetrics\x18\x04 \x01(\x0b\x32N.history.ListAbnormalMetricsResponse.List.AbnormalMetricGroups.AbnormalMetrics\x1a\x64\n\x0f\x41\x62normalMetrics\x12\x0c\n\x04\x64ims\x18\x01 \x03(\t\x12\x18\n\x10\x61\x62normalMetricId\x18\x02 \x01(\t\x12\x1a\n\x12\x61\x62normalMetricName\x18\x03 \x01(\t\x12\r\n\x05level\x18\x04 \x01(\t\"\x8a\x01\n\"ListAbnormalMetricsResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x32\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32$.history.ListAbnormalMetricsResponseb\x06proto3')
  ,
  dependencies=[model_dot_inspection_dot_dim__pb2.DESCRIPTOR,])




_LISTABNORMALMETRICSREQUEST = _descriptor.Descriptor(
  name='ListAbnormalMetricsRequest',
  full_name='history.ListAbnormalMetricsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pluginId', full_name='history.ListAbnormalMetricsRequest.pluginId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='jobId', full_name='history.ListAbnormalMetricsRequest.jobId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='history.ListAbnormalMetricsRequest.instanceId', index=2,
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
  serialized_start=68,
  serialized_end=149,
)


_LISTABNORMALMETRICSRESPONSE_LIST_ABNORMALMETRICGROUPS_ABNORMALMETRICS = _descriptor.Descriptor(
  name='AbnormalMetrics',
  full_name='history.ListAbnormalMetricsResponse.List.AbnormalMetricGroups.AbnormalMetrics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dims', full_name='history.ListAbnormalMetricsResponse.List.AbnormalMetricGroups.AbnormalMetrics.dims', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='abnormalMetricId', full_name='history.ListAbnormalMetricsResponse.List.AbnormalMetricGroups.AbnormalMetrics.abnormalMetricId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='abnormalMetricName', full_name='history.ListAbnormalMetricsResponse.List.AbnormalMetricGroups.AbnormalMetrics.abnormalMetricName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level', full_name='history.ListAbnormalMetricsResponse.List.AbnormalMetricGroups.AbnormalMetrics.level', index=3,
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
  serialized_start=653,
  serialized_end=753,
)

_LISTABNORMALMETRICSRESPONSE_LIST_ABNORMALMETRICGROUPS = _descriptor.Descriptor(
  name='AbnormalMetricGroups',
  full_name='history.ListAbnormalMetricsResponse.List.AbnormalMetricGroups',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dims', full_name='history.ListAbnormalMetricsResponse.List.AbnormalMetricGroups.dims', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metricGroupId', full_name='history.ListAbnormalMetricsResponse.List.AbnormalMetricGroups.metricGroupId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metricGroupName', full_name='history.ListAbnormalMetricsResponse.List.AbnormalMetricGroups.metricGroupName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='abnormalMetrics', full_name='history.ListAbnormalMetricsResponse.List.AbnormalMetricGroups.abnormalMetrics', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTABNORMALMETRICSRESPONSE_LIST_ABNORMALMETRICGROUPS_ABNORMALMETRICS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=435,
  serialized_end=753,
)

_LISTABNORMALMETRICSRESPONSE_LIST = _descriptor.Descriptor(
  name='List',
  full_name='history.ListAbnormalMetricsResponse.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='history.ListAbnormalMetricsResponse.List.ip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targetId', full_name='history.ListAbnormalMetricsResponse.List.targetId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log', full_name='history.ListAbnormalMetricsResponse.List.log', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='abnormalMetricGroups', full_name='history.ListAbnormalMetricsResponse.List.abnormalMetricGroups', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTABNORMALMETRICSRESPONSE_LIST_ABNORMALMETRICGROUPS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=289,
  serialized_end=753,
)

_LISTABNORMALMETRICSRESPONSE = _descriptor.Descriptor(
  name='ListAbnormalMetricsResponse',
  full_name='history.ListAbnormalMetricsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='history.ListAbnormalMetricsResponse.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='history.ListAbnormalMetricsResponse.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='history.ListAbnormalMetricsResponse.total', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='history.ListAbnormalMetricsResponse.list', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTABNORMALMETRICSRESPONSE_LIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=152,
  serialized_end=753,
)


_LISTABNORMALMETRICSRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListAbnormalMetricsResponseWrapper',
  full_name='history.ListAbnormalMetricsResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='history.ListAbnormalMetricsResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='history.ListAbnormalMetricsResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='history.ListAbnormalMetricsResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='history.ListAbnormalMetricsResponseWrapper.data', index=3,
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
  serialized_start=756,
  serialized_end=894,
)

_LISTABNORMALMETRICSRESPONSE_LIST_ABNORMALMETRICGROUPS_ABNORMALMETRICS.containing_type = _LISTABNORMALMETRICSRESPONSE_LIST_ABNORMALMETRICGROUPS
_LISTABNORMALMETRICSRESPONSE_LIST_ABNORMALMETRICGROUPS.fields_by_name['dims'].message_type = model_dot_inspection_dot_dim__pb2._INSPECTIONDIM
_LISTABNORMALMETRICSRESPONSE_LIST_ABNORMALMETRICGROUPS.fields_by_name['abnormalMetrics'].message_type = _LISTABNORMALMETRICSRESPONSE_LIST_ABNORMALMETRICGROUPS_ABNORMALMETRICS
_LISTABNORMALMETRICSRESPONSE_LIST_ABNORMALMETRICGROUPS.containing_type = _LISTABNORMALMETRICSRESPONSE_LIST
_LISTABNORMALMETRICSRESPONSE_LIST.fields_by_name['abnormalMetricGroups'].message_type = _LISTABNORMALMETRICSRESPONSE_LIST_ABNORMALMETRICGROUPS
_LISTABNORMALMETRICSRESPONSE_LIST.containing_type = _LISTABNORMALMETRICSRESPONSE
_LISTABNORMALMETRICSRESPONSE.fields_by_name['list'].message_type = _LISTABNORMALMETRICSRESPONSE_LIST
_LISTABNORMALMETRICSRESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTABNORMALMETRICSRESPONSE
DESCRIPTOR.message_types_by_name['ListAbnormalMetricsRequest'] = _LISTABNORMALMETRICSREQUEST
DESCRIPTOR.message_types_by_name['ListAbnormalMetricsResponse'] = _LISTABNORMALMETRICSRESPONSE
DESCRIPTOR.message_types_by_name['ListAbnormalMetricsResponseWrapper'] = _LISTABNORMALMETRICSRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListAbnormalMetricsRequest = _reflection.GeneratedProtocolMessageType('ListAbnormalMetricsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTABNORMALMETRICSREQUEST,
  __module__ = 'list_abnormal_metrics_pb2'
  # @@protoc_insertion_point(class_scope:history.ListAbnormalMetricsRequest)
  ))
_sym_db.RegisterMessage(ListAbnormalMetricsRequest)

ListAbnormalMetricsResponse = _reflection.GeneratedProtocolMessageType('ListAbnormalMetricsResponse', (_message.Message,), dict(

  List = _reflection.GeneratedProtocolMessageType('List', (_message.Message,), dict(

    AbnormalMetricGroups = _reflection.GeneratedProtocolMessageType('AbnormalMetricGroups', (_message.Message,), dict(

      AbnormalMetrics = _reflection.GeneratedProtocolMessageType('AbnormalMetrics', (_message.Message,), dict(
        DESCRIPTOR = _LISTABNORMALMETRICSRESPONSE_LIST_ABNORMALMETRICGROUPS_ABNORMALMETRICS,
        __module__ = 'list_abnormal_metrics_pb2'
        # @@protoc_insertion_point(class_scope:history.ListAbnormalMetricsResponse.List.AbnormalMetricGroups.AbnormalMetrics)
        ))
      ,
      DESCRIPTOR = _LISTABNORMALMETRICSRESPONSE_LIST_ABNORMALMETRICGROUPS,
      __module__ = 'list_abnormal_metrics_pb2'
      # @@protoc_insertion_point(class_scope:history.ListAbnormalMetricsResponse.List.AbnormalMetricGroups)
      ))
    ,
    DESCRIPTOR = _LISTABNORMALMETRICSRESPONSE_LIST,
    __module__ = 'list_abnormal_metrics_pb2'
    # @@protoc_insertion_point(class_scope:history.ListAbnormalMetricsResponse.List)
    ))
  ,
  DESCRIPTOR = _LISTABNORMALMETRICSRESPONSE,
  __module__ = 'list_abnormal_metrics_pb2'
  # @@protoc_insertion_point(class_scope:history.ListAbnormalMetricsResponse)
  ))
_sym_db.RegisterMessage(ListAbnormalMetricsResponse)
_sym_db.RegisterMessage(ListAbnormalMetricsResponse.List)
_sym_db.RegisterMessage(ListAbnormalMetricsResponse.List.AbnormalMetricGroups)
_sym_db.RegisterMessage(ListAbnormalMetricsResponse.List.AbnormalMetricGroups.AbnormalMetrics)

ListAbnormalMetricsResponseWrapper = _reflection.GeneratedProtocolMessageType('ListAbnormalMetricsResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _LISTABNORMALMETRICSRESPONSEWRAPPER,
  __module__ = 'list_abnormal_metrics_pb2'
  # @@protoc_insertion_point(class_scope:history.ListAbnormalMetricsResponseWrapper)
  ))
_sym_db.RegisterMessage(ListAbnormalMetricsResponseWrapper)


# @@protoc_insertion_point(module_scope)
