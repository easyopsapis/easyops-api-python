# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_custom_dbtask_detail.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_custom_dbtask_detail.proto',
  package='dbtask',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1eget_custom_dbtask_detail.proto\x12\x06\x64\x62task\"0\n\x1cGetCustomDBTaskDetailRequest\x12\x10\n\x08\x64\x62TaskId\x18\x01 \x01(\t\"\xd6\x04\n\x1dGetCustomDBTaskDetailResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05state\x18\x02 \x01(\t\x12\x0f\n\x07\x63reator\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x62ServiceId\x18\x04 \x01(\t\x12\x15\n\rdbServiceName\x18\x05 \x01(\t\x12\x44\n\nchangeTask\x18\x06 \x03(\x0b\x32\x30.dbtask.GetCustomDBTaskDetailResponse.ChangeTask\x12\x0e\n\x06status\x18\x07 \x01(\t\x12\r\n\x05\x63time\x18\x08 \x01(\x03\x12\r\n\x05\x65time\x18\t \x01(\x03\x1a\xe8\x02\n\nChangeTask\x12\x14\n\x0c\x65ntityTaskId\x18\x01 \x01(\t\x12\x14\n\x0c\x64\x62InstanceId\x18\x02 \x01(\t\x12\x16\n\x0e\x64\x62InstanceName\x18\x03 \x01(\t\x12G\n\x06result\x18\x04 \x03(\x0b\x32\x37.dbtask.GetCustomDBTaskDetailResponse.ChangeTask.Result\x1a\xcc\x01\n\x06Result\x12\x0e\n\x06isSkip\x18\x01 \x01(\x05\x12\x12\n\nisRollback\x18\x02 \x01(\x05\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x05 \x01(\t\x12\x11\n\totherAttr\x18\x06 \x01(\t\x12\x11\n\tupdateSql\x18\x07 \x01(\t\x12\x13\n\x0brollbackSql\x18\x08 \x01(\t\x12\x0e\n\x06status\x18\t \x01(\t\x12\x0b\n\x03msg\x18\n \x01(\t\x12\r\n\x05\x63time\x18\x0b \x01(\x03\x12\r\n\x05\x65time\x18\x0c \x01(\x03\"\x8d\x01\n$GetCustomDBTaskDetailResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x33\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32%.dbtask.GetCustomDBTaskDetailResponseb\x06proto3')
)




_GETCUSTOMDBTASKDETAILREQUEST = _descriptor.Descriptor(
  name='GetCustomDBTaskDetailRequest',
  full_name='dbtask.GetCustomDBTaskDetailRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dbTaskId', full_name='dbtask.GetCustomDBTaskDetailRequest.dbTaskId', index=0,
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
  serialized_start=42,
  serialized_end=90,
)


_GETCUSTOMDBTASKDETAILRESPONSE_CHANGETASK_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='dbtask.GetCustomDBTaskDetailResponse.ChangeTask.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='isSkip', full_name='dbtask.GetCustomDBTaskDetailResponse.ChangeTask.Result.isSkip', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isRollback', full_name='dbtask.GetCustomDBTaskDetailResponse.ChangeTask.Result.isRollback', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='dbtask.GetCustomDBTaskDetailResponse.ChangeTask.Result.id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='dbtask.GetCustomDBTaskDetailResponse.ChangeTask.Result.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='author', full_name='dbtask.GetCustomDBTaskDetailResponse.ChangeTask.Result.author', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='otherAttr', full_name='dbtask.GetCustomDBTaskDetailResponse.ChangeTask.Result.otherAttr', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updateSql', full_name='dbtask.GetCustomDBTaskDetailResponse.ChangeTask.Result.updateSql', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rollbackSql', full_name='dbtask.GetCustomDBTaskDetailResponse.ChangeTask.Result.rollbackSql', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='dbtask.GetCustomDBTaskDetailResponse.ChangeTask.Result.status', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='dbtask.GetCustomDBTaskDetailResponse.ChangeTask.Result.msg', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='dbtask.GetCustomDBTaskDetailResponse.ChangeTask.Result.ctime', index=10,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='etime', full_name='dbtask.GetCustomDBTaskDetailResponse.ChangeTask.Result.etime', index=11,
      number=12, type=3, cpp_type=2, label=1,
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
  serialized_start=487,
  serialized_end=691,
)

_GETCUSTOMDBTASKDETAILRESPONSE_CHANGETASK = _descriptor.Descriptor(
  name='ChangeTask',
  full_name='dbtask.GetCustomDBTaskDetailResponse.ChangeTask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entityTaskId', full_name='dbtask.GetCustomDBTaskDetailResponse.ChangeTask.entityTaskId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dbInstanceId', full_name='dbtask.GetCustomDBTaskDetailResponse.ChangeTask.dbInstanceId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dbInstanceName', full_name='dbtask.GetCustomDBTaskDetailResponse.ChangeTask.dbInstanceName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result', full_name='dbtask.GetCustomDBTaskDetailResponse.ChangeTask.result', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETCUSTOMDBTASKDETAILRESPONSE_CHANGETASK_RESULT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=331,
  serialized_end=691,
)

_GETCUSTOMDBTASKDETAILRESPONSE = _descriptor.Descriptor(
  name='GetCustomDBTaskDetailResponse',
  full_name='dbtask.GetCustomDBTaskDetailResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='dbtask.GetCustomDBTaskDetailResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='dbtask.GetCustomDBTaskDetailResponse.state', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='dbtask.GetCustomDBTaskDetailResponse.creator', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dbServiceId', full_name='dbtask.GetCustomDBTaskDetailResponse.dbServiceId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dbServiceName', full_name='dbtask.GetCustomDBTaskDetailResponse.dbServiceName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='changeTask', full_name='dbtask.GetCustomDBTaskDetailResponse.changeTask', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='dbtask.GetCustomDBTaskDetailResponse.status', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='dbtask.GetCustomDBTaskDetailResponse.ctime', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='etime', full_name='dbtask.GetCustomDBTaskDetailResponse.etime', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETCUSTOMDBTASKDETAILRESPONSE_CHANGETASK, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=93,
  serialized_end=691,
)


_GETCUSTOMDBTASKDETAILRESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetCustomDBTaskDetailResponseWrapper',
  full_name='dbtask.GetCustomDBTaskDetailResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='dbtask.GetCustomDBTaskDetailResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='dbtask.GetCustomDBTaskDetailResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dbtask.GetCustomDBTaskDetailResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='dbtask.GetCustomDBTaskDetailResponseWrapper.data', index=3,
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
  serialized_start=694,
  serialized_end=835,
)

_GETCUSTOMDBTASKDETAILRESPONSE_CHANGETASK_RESULT.containing_type = _GETCUSTOMDBTASKDETAILRESPONSE_CHANGETASK
_GETCUSTOMDBTASKDETAILRESPONSE_CHANGETASK.fields_by_name['result'].message_type = _GETCUSTOMDBTASKDETAILRESPONSE_CHANGETASK_RESULT
_GETCUSTOMDBTASKDETAILRESPONSE_CHANGETASK.containing_type = _GETCUSTOMDBTASKDETAILRESPONSE
_GETCUSTOMDBTASKDETAILRESPONSE.fields_by_name['changeTask'].message_type = _GETCUSTOMDBTASKDETAILRESPONSE_CHANGETASK
_GETCUSTOMDBTASKDETAILRESPONSEWRAPPER.fields_by_name['data'].message_type = _GETCUSTOMDBTASKDETAILRESPONSE
DESCRIPTOR.message_types_by_name['GetCustomDBTaskDetailRequest'] = _GETCUSTOMDBTASKDETAILREQUEST
DESCRIPTOR.message_types_by_name['GetCustomDBTaskDetailResponse'] = _GETCUSTOMDBTASKDETAILRESPONSE
DESCRIPTOR.message_types_by_name['GetCustomDBTaskDetailResponseWrapper'] = _GETCUSTOMDBTASKDETAILRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetCustomDBTaskDetailRequest = _reflection.GeneratedProtocolMessageType('GetCustomDBTaskDetailRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCUSTOMDBTASKDETAILREQUEST,
  '__module__' : 'get_custom_dbtask_detail_pb2'
  # @@protoc_insertion_point(class_scope:dbtask.GetCustomDBTaskDetailRequest)
  })
_sym_db.RegisterMessage(GetCustomDBTaskDetailRequest)

GetCustomDBTaskDetailResponse = _reflection.GeneratedProtocolMessageType('GetCustomDBTaskDetailResponse', (_message.Message,), {

  'ChangeTask' : _reflection.GeneratedProtocolMessageType('ChangeTask', (_message.Message,), {

    'Result' : _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), {
      'DESCRIPTOR' : _GETCUSTOMDBTASKDETAILRESPONSE_CHANGETASK_RESULT,
      '__module__' : 'get_custom_dbtask_detail_pb2'
      # @@protoc_insertion_point(class_scope:dbtask.GetCustomDBTaskDetailResponse.ChangeTask.Result)
      })
    ,
    'DESCRIPTOR' : _GETCUSTOMDBTASKDETAILRESPONSE_CHANGETASK,
    '__module__' : 'get_custom_dbtask_detail_pb2'
    # @@protoc_insertion_point(class_scope:dbtask.GetCustomDBTaskDetailResponse.ChangeTask)
    })
  ,
  'DESCRIPTOR' : _GETCUSTOMDBTASKDETAILRESPONSE,
  '__module__' : 'get_custom_dbtask_detail_pb2'
  # @@protoc_insertion_point(class_scope:dbtask.GetCustomDBTaskDetailResponse)
  })
_sym_db.RegisterMessage(GetCustomDBTaskDetailResponse)
_sym_db.RegisterMessage(GetCustomDBTaskDetailResponse.ChangeTask)
_sym_db.RegisterMessage(GetCustomDBTaskDetailResponse.ChangeTask.Result)

GetCustomDBTaskDetailResponseWrapper = _reflection.GeneratedProtocolMessageType('GetCustomDBTaskDetailResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _GETCUSTOMDBTASKDETAILRESPONSEWRAPPER,
  '__module__' : 'get_custom_dbtask_detail_pb2'
  # @@protoc_insertion_point(class_scope:dbtask.GetCustomDBTaskDetailResponseWrapper)
  })
_sym_db.RegisterMessage(GetCustomDBTaskDetailResponseWrapper)


# @@protoc_insertion_point(module_scope)
