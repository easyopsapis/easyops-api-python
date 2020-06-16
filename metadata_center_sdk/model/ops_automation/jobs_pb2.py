# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: jobs.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from metadata_center_sdk.model.ops_automation import bind_resource_pb2 as metadata__center__sdk_dot_model_dot_ops__automation_dot_bind__resource__pb2
from metadata_center_sdk.model.ops_automation import mail_info_pb2 as metadata__center__sdk_dot_model_dot_ops__automation_dot_mail__info__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='jobs.proto',
  package='ops_automation',
  syntax='proto3',
  serialized_options=_b('ZHgo.easyops.local/contracts/protorepo-models/easyops/model/ops_automation'),
  serialized_pb=_b('\n\njobs.proto\x12\x0eops_automation\x1a<metadata_center_sdk/model/ops_automation/bind_resource.proto\x1a\x38metadata_center_sdk/model/ops_automation/mail_info.proto\"\xc1\x01\n\x04Jobs\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\x12\x0e\n\x06menuId\x18\x03 \x01(\t\x12\x32\n\x0c\x62indResource\x18\x04 \x01(\x0b\x32\x1c.ops_automation.BindResource\x12\x0c\n\x04\x64\x65sc\x18\x05 \x01(\t\x12\x13\n\x0b\x61llowModify\x18\x06 \x01(\x08\x12&\n\x04mail\x18\x07 \x01(\x0b\x32\x18.ops_automation.MailInfo\x12\n\n\x02id\x18\x08 \x01(\tBJZHgo.easyops.local/contracts/protorepo-models/easyops/model/ops_automationb\x06proto3')
  ,
  dependencies=[metadata__center__sdk_dot_model_dot_ops__automation_dot_bind__resource__pb2.DESCRIPTOR,metadata__center__sdk_dot_model_dot_ops__automation_dot_mail__info__pb2.DESCRIPTOR,])




_JOBS = _descriptor.Descriptor(
  name='Jobs',
  full_name='ops_automation.Jobs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ops_automation.Jobs.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='ops_automation.Jobs.category', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='menuId', full_name='ops_automation.Jobs.menuId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bindResource', full_name='ops_automation.Jobs.bindResource', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='desc', full_name='ops_automation.Jobs.desc', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='allowModify', full_name='ops_automation.Jobs.allowModify', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mail', full_name='ops_automation.Jobs.mail', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='ops_automation.Jobs.id', index=7,
      number=8, type=9, cpp_type=9, label=1,
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
  serialized_start=151,
  serialized_end=344,
)

_JOBS.fields_by_name['bindResource'].message_type = metadata__center__sdk_dot_model_dot_ops__automation_dot_bind__resource__pb2._BINDRESOURCE
_JOBS.fields_by_name['mail'].message_type = metadata__center__sdk_dot_model_dot_ops__automation_dot_mail__info__pb2._MAILINFO
DESCRIPTOR.message_types_by_name['Jobs'] = _JOBS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Jobs = _reflection.GeneratedProtocolMessageType('Jobs', (_message.Message,), {
  'DESCRIPTOR' : _JOBS,
  '__module__' : 'jobs_pb2'
  # @@protoc_insertion_point(class_scope:ops_automation.Jobs)
  })
_sym_db.RegisterMessage(Jobs)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
