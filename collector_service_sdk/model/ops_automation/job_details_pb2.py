# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: job_details.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from collector_service_sdk.model.ops_automation import bind_resource_pb2 as collector__service__sdk_dot_model_dot_ops__automation_dot_bind__resource__pb2
from collector_service_sdk.model.ops_automation import mail_info_pb2 as collector__service__sdk_dot_model_dot_ops__automation_dot_mail__info__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='job_details.proto',
  package='ops_automation',
  syntax='proto3',
  serialized_options=_b('ZHgo.easyops.local/contracts/protorepo-models/easyops/model/ops_automation'),
  serialized_pb=_b('\n\x11job_details.proto\x12\x0eops_automation\x1a>collector_service_sdk/model/ops_automation/bind_resource.proto\x1a:collector_service_sdk/model/ops_automation/mail_info.proto\"\x87\x03\n\nJobDetails\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x12\n\ncreateTime\x18\x02 \x01(\t\x12\x12\n\nupdateTime\x18\x03 \x01(\t\x12\x0f\n\x07\x63reator\x18\x04 \x01(\t\x12\x0b\n\x03org\x18\x05 \x01(\x05\x12\x37\n\tscheduler\x18\x06 \x01(\x0b\x32$.ops_automation.JobDetails.Scheduler\x12\x0c\n\x04name\x18\x07 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x08 \x01(\t\x12\x0e\n\x06menuId\x18\t \x01(\t\x12\x32\n\x0c\x62indResource\x18\n \x01(\x0b\x32\x1c.ops_automation.BindResource\x12\x0c\n\x04\x64\x65sc\x18\x0b \x01(\t\x12\x13\n\x0b\x61llowModify\x18\x0c \x01(\x08\x12&\n\x04mail\x18\r \x01(\x0b\x32\x18.ops_automation.MailInfo\x12\n\n\x02id\x18\x0e \x01(\t\x1a.\n\tScheduler\x12\x0f\n\x07isBound\x18\x01 \x01(\x08\x12\x10\n\x08isActive\x18\x02 \x01(\x08\x42JZHgo.easyops.local/contracts/protorepo-models/easyops/model/ops_automationb\x06proto3')
  ,
  dependencies=[collector__service__sdk_dot_model_dot_ops__automation_dot_bind__resource__pb2.DESCRIPTOR,collector__service__sdk_dot_model_dot_ops__automation_dot_mail__info__pb2.DESCRIPTOR,])




_JOBDETAILS_SCHEDULER = _descriptor.Descriptor(
  name='Scheduler',
  full_name='ops_automation.JobDetails.Scheduler',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='isBound', full_name='ops_automation.JobDetails.Scheduler.isBound', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isActive', full_name='ops_automation.JobDetails.Scheduler.isActive', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=507,
  serialized_end=553,
)

_JOBDETAILS = _descriptor.Descriptor(
  name='JobDetails',
  full_name='ops_automation.JobDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='ops_automation.JobDetails.version', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='createTime', full_name='ops_automation.JobDetails.createTime', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updateTime', full_name='ops_automation.JobDetails.updateTime', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='ops_automation.JobDetails.creator', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org', full_name='ops_automation.JobDetails.org', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scheduler', full_name='ops_automation.JobDetails.scheduler', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='ops_automation.JobDetails.name', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='ops_automation.JobDetails.category', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='menuId', full_name='ops_automation.JobDetails.menuId', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bindResource', full_name='ops_automation.JobDetails.bindResource', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='desc', full_name='ops_automation.JobDetails.desc', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='allowModify', full_name='ops_automation.JobDetails.allowModify', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mail', full_name='ops_automation.JobDetails.mail', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='ops_automation.JobDetails.id', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_JOBDETAILS_SCHEDULER, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=162,
  serialized_end=553,
)

_JOBDETAILS_SCHEDULER.containing_type = _JOBDETAILS
_JOBDETAILS.fields_by_name['scheduler'].message_type = _JOBDETAILS_SCHEDULER
_JOBDETAILS.fields_by_name['bindResource'].message_type = collector__service__sdk_dot_model_dot_ops__automation_dot_bind__resource__pb2._BINDRESOURCE
_JOBDETAILS.fields_by_name['mail'].message_type = collector__service__sdk_dot_model_dot_ops__automation_dot_mail__info__pb2._MAILINFO
DESCRIPTOR.message_types_by_name['JobDetails'] = _JOBDETAILS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

JobDetails = _reflection.GeneratedProtocolMessageType('JobDetails', (_message.Message,), {

  'Scheduler' : _reflection.GeneratedProtocolMessageType('Scheduler', (_message.Message,), {
    'DESCRIPTOR' : _JOBDETAILS_SCHEDULER,
    '__module__' : 'job_details_pb2'
    # @@protoc_insertion_point(class_scope:ops_automation.JobDetails.Scheduler)
    })
  ,
  'DESCRIPTOR' : _JOBDETAILS,
  '__module__' : 'job_details_pb2'
  # @@protoc_insertion_point(class_scope:ops_automation.JobDetails)
  })
_sym_db.RegisterMessage(JobDetails)
_sym_db.RegisterMessage(JobDetails.Scheduler)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
