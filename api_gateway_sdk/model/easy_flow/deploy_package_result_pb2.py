# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: deploy_package_result.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api_gateway_sdk.model.easy_flow import package_info_pb2 as api__gateway__sdk_dot_model_dot_easy__flow_dot_package__info__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='deploy_package_result.proto',
  package='easy_flow',
  syntax='proto3',
  serialized_options=_b('ZCgo.easyops.local/contracts/protorepo-models/easyops/model/easy_flow'),
  serialized_pb=_b('\n\x1b\x64\x65ploy_package_result.proto\x12\teasy_flow\x1a\x32\x61pi_gateway_sdk/model/easy_flow/package_info.proto\"\xfa\x02\n\x13\x44\x65ployPackageResult\x12\x11\n\tpackageId\x18\x01 \x01(\t\x12\x11\n\tversionId\x18\x02 \x01(\t\x12\x13\n\x0binstallPath\x18\x03 \x01(\t\x12\x10\n\x08usedTime\x18\x04 \x01(\x05\x12\x11\n\tstartTime\x18\x05 \x01(\t\x12\x0f\n\x07\x65ndTime\x18\x06 \x01(\t\x12\x39\n\x08progress\x18\x07 \x03(\x0b\x32\'.easy_flow.DeployPackageResult.Progress\x12\x0b\n\x03msg\x18\x08 \x01(\t\x12\x0e\n\x06status\x18\t \x01(\t\x12\x0c\n\x04\x63ode\x18\n \x01(\x05\x12%\n\x05param\x18\x0b \x01(\x0b\x32\x16.easy_flow.PackageInfo\x1a\x65\n\x08Progress\x12\x0b\n\x03msg\x18\x01 \x01(\t\x12\r\n\x05mtime\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07percent\x18\x04 \x01(\t\x12\x0e\n\x06status\x18\x05 \x01(\t\x12\x0e\n\x06values\x18\x06 \x01(\tBEZCgo.easyops.local/contracts/protorepo-models/easyops/model/easy_flowb\x06proto3')
  ,
  dependencies=[api__gateway__sdk_dot_model_dot_easy__flow_dot_package__info__pb2.DESCRIPTOR,])




_DEPLOYPACKAGERESULT_PROGRESS = _descriptor.Descriptor(
  name='Progress',
  full_name='easy_flow.DeployPackageResult.Progress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='easy_flow.DeployPackageResult.Progress.msg', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='easy_flow.DeployPackageResult.Progress.mtime', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='easy_flow.DeployPackageResult.Progress.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='percent', full_name='easy_flow.DeployPackageResult.Progress.percent', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='easy_flow.DeployPackageResult.Progress.status', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='values', full_name='easy_flow.DeployPackageResult.Progress.values', index=5,
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
  serialized_start=372,
  serialized_end=473,
)

_DEPLOYPACKAGERESULT = _descriptor.Descriptor(
  name='DeployPackageResult',
  full_name='easy_flow.DeployPackageResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='packageId', full_name='easy_flow.DeployPackageResult.packageId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionId', full_name='easy_flow.DeployPackageResult.versionId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='installPath', full_name='easy_flow.DeployPackageResult.installPath', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='usedTime', full_name='easy_flow.DeployPackageResult.usedTime', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='easy_flow.DeployPackageResult.startTime', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endTime', full_name='easy_flow.DeployPackageResult.endTime', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='progress', full_name='easy_flow.DeployPackageResult.progress', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='easy_flow.DeployPackageResult.msg', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='easy_flow.DeployPackageResult.status', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='easy_flow.DeployPackageResult.code', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='param', full_name='easy_flow.DeployPackageResult.param', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DEPLOYPACKAGERESULT_PROGRESS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=95,
  serialized_end=473,
)

_DEPLOYPACKAGERESULT_PROGRESS.containing_type = _DEPLOYPACKAGERESULT
_DEPLOYPACKAGERESULT.fields_by_name['progress'].message_type = _DEPLOYPACKAGERESULT_PROGRESS
_DEPLOYPACKAGERESULT.fields_by_name['param'].message_type = api__gateway__sdk_dot_model_dot_easy__flow_dot_package__info__pb2._PACKAGEINFO
DESCRIPTOR.message_types_by_name['DeployPackageResult'] = _DEPLOYPACKAGERESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeployPackageResult = _reflection.GeneratedProtocolMessageType('DeployPackageResult', (_message.Message,), {

  'Progress' : _reflection.GeneratedProtocolMessageType('Progress', (_message.Message,), {
    'DESCRIPTOR' : _DEPLOYPACKAGERESULT_PROGRESS,
    '__module__' : 'deploy_package_result_pb2'
    # @@protoc_insertion_point(class_scope:easy_flow.DeployPackageResult.Progress)
    })
  ,
  'DESCRIPTOR' : _DEPLOYPACKAGERESULT,
  '__module__' : 'deploy_package_result_pb2'
  # @@protoc_insertion_point(class_scope:easy_flow.DeployPackageResult)
  })
_sym_db.RegisterMessage(DeployPackageResult)
_sym_db.RegisterMessage(DeployPackageResult.Progress)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)