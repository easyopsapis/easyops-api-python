# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: job_tasks.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from msgsender_sdk.model.ops_automation import mail_info_pb2 as msgsender__sdk_dot_model_dot_ops__automation_dot_mail__info__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='job_tasks.proto',
  package='ops_automation',
  syntax='proto3',
  serialized_options=_b('ZHgo.easyops.local/contracts/protorepo-models/easyops/model/ops_automation'),
  serialized_pb=_b('\n\x0fjob_tasks.proto\x12\x0eops_automation\x1a\x32msgsender_sdk/model/ops_automation/mail_info.proto\"\x82\x03\n\x08JobTasks\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05jobId\x18\x02 \x01(\t\x12\x0f\n\x07jobName\x18\x03 \x01(\t\x12\x10\n\x08menuName\x18\x04 \x01(\t\x12\x0e\n\x06\x65xecId\x18\x05 \x01(\t\x12\x14\n\x0cresourceType\x18\x06 \x01(\t\x12\x12\n\nresourceId\x18\x07 \x01(\t\x12\x13\n\x0bresourceVId\x18\x08 \x01(\t\x12\x15\n\rresourceVName\x18\t \x01(\t\x12\x0f\n\x07trigger\x18\n \x01(\t\x12\x10\n\x08\x65xecUser\x18\x0b \x01(\t\x12\r\n\x05hosts\x18\x0c \x03(\t\x12\x0e\n\x06status\x18\r \x01(\t\x12&\n\x04mail\x18\x0e \x01(\x0b\x32\x18.ops_automation.MailInfo\x12\x13\n\x0bsuccessRate\x18\x0f \x01(\x02\x12\r\n\x05\x65rror\x18\x10 \x01(\t\x12\x12\n\ncreateTime\x18\x11 \x01(\t\x12\x12\n\nupdateTime\x18\x12 \x01(\t\x12\x0f\n\x07\x63reator\x18\x13 \x01(\t\x12\x0b\n\x03org\x18\x14 \x01(\x05\x42JZHgo.easyops.local/contracts/protorepo-models/easyops/model/ops_automationb\x06proto3')
  ,
  dependencies=[msgsender__sdk_dot_model_dot_ops__automation_dot_mail__info__pb2.DESCRIPTOR,])




_JOBTASKS = _descriptor.Descriptor(
  name='JobTasks',
  full_name='ops_automation.JobTasks',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ops_automation.JobTasks.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='jobId', full_name='ops_automation.JobTasks.jobId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='jobName', full_name='ops_automation.JobTasks.jobName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='menuName', full_name='ops_automation.JobTasks.menuName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='execId', full_name='ops_automation.JobTasks.execId', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resourceType', full_name='ops_automation.JobTasks.resourceType', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resourceId', full_name='ops_automation.JobTasks.resourceId', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resourceVId', full_name='ops_automation.JobTasks.resourceVId', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resourceVName', full_name='ops_automation.JobTasks.resourceVName', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trigger', full_name='ops_automation.JobTasks.trigger', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='execUser', full_name='ops_automation.JobTasks.execUser', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hosts', full_name='ops_automation.JobTasks.hosts', index=11,
      number=12, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='ops_automation.JobTasks.status', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mail', full_name='ops_automation.JobTasks.mail', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='successRate', full_name='ops_automation.JobTasks.successRate', index=14,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='ops_automation.JobTasks.error', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='createTime', full_name='ops_automation.JobTasks.createTime', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updateTime', full_name='ops_automation.JobTasks.updateTime', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='ops_automation.JobTasks.creator', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org', full_name='ops_automation.JobTasks.org', index=19,
      number=20, type=5, cpp_type=1, label=1,
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
  serialized_start=88,
  serialized_end=474,
)

_JOBTASKS.fields_by_name['mail'].message_type = msgsender__sdk_dot_model_dot_ops__automation_dot_mail__info__pb2._MAILINFO
DESCRIPTOR.message_types_by_name['JobTasks'] = _JOBTASKS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

JobTasks = _reflection.GeneratedProtocolMessageType('JobTasks', (_message.Message,), {
  'DESCRIPTOR' : _JOBTASKS,
  '__module__' : 'job_tasks_pb2'
  # @@protoc_insertion_point(class_scope:ops_automation.JobTasks)
  })
_sym_db.RegisterMessage(JobTasks)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
