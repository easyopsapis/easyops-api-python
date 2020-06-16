# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: alert_rule.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from patch_manager_sdk.model.monitor import alert_dims_pb2 as patch__manager__sdk_dot_model_dot_monitor_dot_alert__dims__pb2
from patch_manager_sdk.model.monitor import alert_conditions_pb2 as patch__manager__sdk_dot_model_dot_monitor_dot_alert__conditions__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='alert_rule.proto',
  package='monitor',
  syntax='proto3',
  serialized_options=_b('ZAgo.easyops.local/contracts/protorepo-models/easyops/model/monitor'),
  serialized_pb=_b('\n\x10\x61lert_rule.proto\x12\x07monitor\x1a\x30patch_manager_sdk/model/monitor/alert_dims.proto\x1a\x36patch_manager_sdk/model/monitor/alert_conditions.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xc2\x08\n\tAlertRule\x12\x0b\n\x03org\x18\x01 \x01(\x05\x12\n\n\x02id\x18\x02 \x01(\t\x12\x11\n\trule_name\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\x05\x12\x12\n\nversion_id\x18\x05 \x01(\t\x12&\n\nalert_dims\x18\x06 \x03(\x0b\x32\x12.monitor.AlertDims\x12\x15\n\rrule_priority\x18\x07 \x01(\x05\x12\x32\n\x10\x61lert_conditions\x18\x08 \x01(\x0b\x32\x18.monitor.AlertConditions\x12\x15\n\rdetect_window\x18\t \x01(\x05\x12\x13\n\x0b\x61lert_count\x18\n \x01(\x05\x12\x16\n\x0e\x61lert_interval\x18\x0b \x01(\x05\x12\x15\n\rrecover_count\x18\x0c \x01(\x05\x12+\n\x07\x61\x63tions\x18\r \x03(\x0b\x32\x1a.monitor.AlertRule.Actions\x12/\n\ttemplates\x18\x0e \x01(\x0b\x32\x1c.monitor.AlertRule.Templates\x12\x0f\n\x07\x63reator\x18\x0f \x01(\t\x12\r\n\x05\x63time\x18\x10 \x01(\x05\x12\r\n\x05mtime\x18\x11 \x01(\x05\x12/\n\tinstances\x18\x12 \x01(\x0b\x32\x1c.monitor.AlertRule.Instances\x12\x10\n\x08objectId\x18\x13 \x01(\t\x12\x10\n\x08\x64isabled\x18\x14 \x01(\x08\x12\x0e\n\x06source\x18\x15 \x01(\t\x1a\xe8\x02\n\x07\x41\x63tions\x12\x37\n\tcondition\x18\x01 \x01(\x0b\x32$.monitor.AlertRule.Actions.Condition\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0f\n\x07upgrade\x18\x03 \x01(\x08\x12\x0f\n\x07methods\x18\x04 \x03(\t\x12\x11\n\treceivers\x18\x05 \x03(\t\x12\x1c\n\x14receiver_user_groups\x18\x06 \x03(\t\x12\x42\n\x0freceiver_owners\x18\x07 \x03(\x0b\x32).monitor.AlertRule.Actions.ReceiverOwners\x1a/\n\tCondition\x12\x13\n\x0blasting_for\x18\x01 \x01(\x05\x12\r\n\x05level\x18\x02 \x01(\x05\x1aN\n\x0eReceiverOwners\x12\x11\n\tobject_id\x18\x01 \x01(\t\x12\x16\n\x0eobject_attr_id\x18\x02 \x01(\t\x12\x11\n\ttranslate\x18\x03 \x01(\t\x1a\x61\n\tTemplates\x12\x18\n\x10\x63ontent_template\x18\x01 \x01(\t\x12\x17\n\x0ftarget_template\x18\x02 \x01(\t\x12!\n\x19recovery_content_template\x18\x03 \x01(\t\x1aV\n\tInstances\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x13\n\x0binstanceIds\x18\x02 \x03(\t\x12&\n\x05query\x18\x03 \x01(\x0b\x32\x17.google.protobuf.StructBCZAgo.easyops.local/contracts/protorepo-models/easyops/model/monitorb\x06proto3')
  ,
  dependencies=[patch__manager__sdk_dot_model_dot_monitor_dot_alert__dims__pb2.DESCRIPTOR,patch__manager__sdk_dot_model_dot_monitor_dot_alert__conditions__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_ALERTRULE_ACTIONS_CONDITION = _descriptor.Descriptor(
  name='Condition',
  full_name='monitor.AlertRule.Actions.Condition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lasting_for', full_name='monitor.AlertRule.Actions.Condition.lasting_for', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level', full_name='monitor.AlertRule.Actions.Condition.level', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=942,
  serialized_end=989,
)

_ALERTRULE_ACTIONS_RECEIVEROWNERS = _descriptor.Descriptor(
  name='ReceiverOwners',
  full_name='monitor.AlertRule.Actions.ReceiverOwners',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_id', full_name='monitor.AlertRule.Actions.ReceiverOwners.object_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='object_attr_id', full_name='monitor.AlertRule.Actions.ReceiverOwners.object_attr_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='translate', full_name='monitor.AlertRule.Actions.ReceiverOwners.translate', index=2,
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
  serialized_start=991,
  serialized_end=1069,
)

_ALERTRULE_ACTIONS = _descriptor.Descriptor(
  name='Actions',
  full_name='monitor.AlertRule.Actions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='condition', full_name='monitor.AlertRule.Actions.condition', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='monitor.AlertRule.Actions.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='upgrade', full_name='monitor.AlertRule.Actions.upgrade', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='methods', full_name='monitor.AlertRule.Actions.methods', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='receivers', full_name='monitor.AlertRule.Actions.receivers', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='receiver_user_groups', full_name='monitor.AlertRule.Actions.receiver_user_groups', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='receiver_owners', full_name='monitor.AlertRule.Actions.receiver_owners', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ALERTRULE_ACTIONS_CONDITION, _ALERTRULE_ACTIONS_RECEIVEROWNERS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=709,
  serialized_end=1069,
)

_ALERTRULE_TEMPLATES = _descriptor.Descriptor(
  name='Templates',
  full_name='monitor.AlertRule.Templates',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='content_template', full_name='monitor.AlertRule.Templates.content_template', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_template', full_name='monitor.AlertRule.Templates.target_template', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='recovery_content_template', full_name='monitor.AlertRule.Templates.recovery_content_template', index=2,
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
  serialized_start=1071,
  serialized_end=1168,
)

_ALERTRULE_INSTANCES = _descriptor.Descriptor(
  name='Instances',
  full_name='monitor.AlertRule.Instances',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='monitor.AlertRule.Instances.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceIds', full_name='monitor.AlertRule.Instances.instanceIds', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='query', full_name='monitor.AlertRule.Instances.query', index=2,
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
  serialized_start=1170,
  serialized_end=1256,
)

_ALERTRULE = _descriptor.Descriptor(
  name='AlertRule',
  full_name='monitor.AlertRule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='org', full_name='monitor.AlertRule.org', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='monitor.AlertRule.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rule_name', full_name='monitor.AlertRule.rule_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='monitor.AlertRule.version', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version_id', full_name='monitor.AlertRule.version_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alert_dims', full_name='monitor.AlertRule.alert_dims', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rule_priority', full_name='monitor.AlertRule.rule_priority', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alert_conditions', full_name='monitor.AlertRule.alert_conditions', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='detect_window', full_name='monitor.AlertRule.detect_window', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alert_count', full_name='monitor.AlertRule.alert_count', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alert_interval', full_name='monitor.AlertRule.alert_interval', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='recover_count', full_name='monitor.AlertRule.recover_count', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actions', full_name='monitor.AlertRule.actions', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='templates', full_name='monitor.AlertRule.templates', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='monitor.AlertRule.creator', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='monitor.AlertRule.ctime', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='monitor.AlertRule.mtime', index=16,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instances', full_name='monitor.AlertRule.instances', index=17,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectId', full_name='monitor.AlertRule.objectId', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disabled', full_name='monitor.AlertRule.disabled', index=19,
      number=20, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='monitor.AlertRule.source', index=20,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ALERTRULE_ACTIONS, _ALERTRULE_TEMPLATES, _ALERTRULE_INSTANCES, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=166,
  serialized_end=1256,
)

_ALERTRULE_ACTIONS_CONDITION.containing_type = _ALERTRULE_ACTIONS
_ALERTRULE_ACTIONS_RECEIVEROWNERS.containing_type = _ALERTRULE_ACTIONS
_ALERTRULE_ACTIONS.fields_by_name['condition'].message_type = _ALERTRULE_ACTIONS_CONDITION
_ALERTRULE_ACTIONS.fields_by_name['receiver_owners'].message_type = _ALERTRULE_ACTIONS_RECEIVEROWNERS
_ALERTRULE_ACTIONS.containing_type = _ALERTRULE
_ALERTRULE_TEMPLATES.containing_type = _ALERTRULE
_ALERTRULE_INSTANCES.fields_by_name['query'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_ALERTRULE_INSTANCES.containing_type = _ALERTRULE
_ALERTRULE.fields_by_name['alert_dims'].message_type = patch__manager__sdk_dot_model_dot_monitor_dot_alert__dims__pb2._ALERTDIMS
_ALERTRULE.fields_by_name['alert_conditions'].message_type = patch__manager__sdk_dot_model_dot_monitor_dot_alert__conditions__pb2._ALERTCONDITIONS
_ALERTRULE.fields_by_name['actions'].message_type = _ALERTRULE_ACTIONS
_ALERTRULE.fields_by_name['templates'].message_type = _ALERTRULE_TEMPLATES
_ALERTRULE.fields_by_name['instances'].message_type = _ALERTRULE_INSTANCES
DESCRIPTOR.message_types_by_name['AlertRule'] = _ALERTRULE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AlertRule = _reflection.GeneratedProtocolMessageType('AlertRule', (_message.Message,), {

  'Actions' : _reflection.GeneratedProtocolMessageType('Actions', (_message.Message,), {

    'Condition' : _reflection.GeneratedProtocolMessageType('Condition', (_message.Message,), {
      'DESCRIPTOR' : _ALERTRULE_ACTIONS_CONDITION,
      '__module__' : 'alert_rule_pb2'
      # @@protoc_insertion_point(class_scope:monitor.AlertRule.Actions.Condition)
      })
    ,

    'ReceiverOwners' : _reflection.GeneratedProtocolMessageType('ReceiverOwners', (_message.Message,), {
      'DESCRIPTOR' : _ALERTRULE_ACTIONS_RECEIVEROWNERS,
      '__module__' : 'alert_rule_pb2'
      # @@protoc_insertion_point(class_scope:monitor.AlertRule.Actions.ReceiverOwners)
      })
    ,
    'DESCRIPTOR' : _ALERTRULE_ACTIONS,
    '__module__' : 'alert_rule_pb2'
    # @@protoc_insertion_point(class_scope:monitor.AlertRule.Actions)
    })
  ,

  'Templates' : _reflection.GeneratedProtocolMessageType('Templates', (_message.Message,), {
    'DESCRIPTOR' : _ALERTRULE_TEMPLATES,
    '__module__' : 'alert_rule_pb2'
    # @@protoc_insertion_point(class_scope:monitor.AlertRule.Templates)
    })
  ,

  'Instances' : _reflection.GeneratedProtocolMessageType('Instances', (_message.Message,), {
    'DESCRIPTOR' : _ALERTRULE_INSTANCES,
    '__module__' : 'alert_rule_pb2'
    # @@protoc_insertion_point(class_scope:monitor.AlertRule.Instances)
    })
  ,
  'DESCRIPTOR' : _ALERTRULE,
  '__module__' : 'alert_rule_pb2'
  # @@protoc_insertion_point(class_scope:monitor.AlertRule)
  })
_sym_db.RegisterMessage(AlertRule)
_sym_db.RegisterMessage(AlertRule.Actions)
_sym_db.RegisterMessage(AlertRule.Actions.Condition)
_sym_db.RegisterMessage(AlertRule.Actions.ReceiverOwners)
_sym_db.RegisterMessage(AlertRule.Templates)
_sym_db.RegisterMessage(AlertRule.Instances)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
