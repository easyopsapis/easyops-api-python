# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: execution_snapshot.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from idcmanager_sdk.model.tool import callback_pb2 as idcmanager__sdk_dot_model_dot_tool_dot_callback__pb2
from idcmanager_sdk.model.tool import extra_info_pb2 as idcmanager__sdk_dot_model_dot_tool_dot_extra__info__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='execution_snapshot.proto',
  package='tool',
  syntax='proto3',
  serialized_options=_b('Z>go.easyops.local/contracts/protorepo-models/easyops/model/tool'),
  serialized_pb=_b('\n\x18\x65xecution_snapshot.proto\x12\x04tool\x1a(idcmanager_sdk/model/tool/callback.proto\x1a*idcmanager_sdk/model/tool/extra_info.proto\"\x9d\x04\n\x11\x45xecutionSnapshot\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x11\n\toperation\x18\x03 \x01(\t\x12\x11\n\tpackageId\x18\x04 \x01(\t\x12\x11\n\tversionId\x18\x05 \x01(\t\x12\x30\n\x07targets\x18\x06 \x03(\x0b\x32\x1f.tool.ExecutionSnapshot.Targets\x12\x30\n\x07\x61\x63tions\x18\x07 \x03(\x0b\x32\x1f.tool.ExecutionSnapshot.Actions\x12 \n\x08\x63\x61llback\x18\x08 \x01(\x0b\x32\x0e.tool.Callback\x12\"\n\textraInfo\x18\t \x01(\x0b\x32\x0f.tool.ExtraInfo\x12\x12\n\nneedNotify\x18\n \x01(\t\x1a\x1b\n\x07Targets\x12\x10\n\x08targetId\x18\x01 \x01(\t\x1a\xd7\x01\n\x07\x41\x63tions\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x03 \x01(\t\x12\x34\n\x05param\x18\x04 \x01(\x0b\x32%.tool.ExecutionSnapshot.Actions.Param\x1aj\n\x05Param\x12\x0b\n\x03\x63md\x18\x01 \x01(\t\x12\x12\n\nscriptType\x18\x02 \x01(\t\x12\x0e\n\x06parser\x18\x03 \x01(\t\x12\r\n\x05param\x18\x04 \x01(\t\x12\x10\n\x08\x65xecUser\x18\x05 \x01(\t\x12\x0f\n\x07timeout\x18\x06 \x01(\x05\x42@Z>go.easyops.local/contracts/protorepo-models/easyops/model/toolb\x06proto3')
  ,
  dependencies=[idcmanager__sdk_dot_model_dot_tool_dot_callback__pb2.DESCRIPTOR,idcmanager__sdk_dot_model_dot_tool_dot_extra__info__pb2.DESCRIPTOR,])




_EXECUTIONSNAPSHOT_TARGETS = _descriptor.Descriptor(
  name='Targets',
  full_name='tool.ExecutionSnapshot.Targets',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='targetId', full_name='tool.ExecutionSnapshot.Targets.targetId', index=0,
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
  serialized_start=417,
  serialized_end=444,
)

_EXECUTIONSNAPSHOT_ACTIONS_PARAM = _descriptor.Descriptor(
  name='Param',
  full_name='tool.ExecutionSnapshot.Actions.Param',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='tool.ExecutionSnapshot.Actions.Param.cmd', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scriptType', full_name='tool.ExecutionSnapshot.Actions.Param.scriptType', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parser', full_name='tool.ExecutionSnapshot.Actions.Param.parser', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='param', full_name='tool.ExecutionSnapshot.Actions.Param.param', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='execUser', full_name='tool.ExecutionSnapshot.Actions.Param.execUser', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='tool.ExecutionSnapshot.Actions.Param.timeout', index=5,
      number=6, type=5, cpp_type=1, label=1,
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
  serialized_start=556,
  serialized_end=662,
)

_EXECUTIONSNAPSHOT_ACTIONS = _descriptor.Descriptor(
  name='Actions',
  full_name='tool.ExecutionSnapshot.Actions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tool.ExecutionSnapshot.Actions.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='tool.ExecutionSnapshot.Actions.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='tool.ExecutionSnapshot.Actions.action', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='param', full_name='tool.ExecutionSnapshot.Actions.param', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_EXECUTIONSNAPSHOT_ACTIONS_PARAM, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=447,
  serialized_end=662,
)

_EXECUTIONSNAPSHOT = _descriptor.Descriptor(
  name='ExecutionSnapshot',
  full_name='tool.ExecutionSnapshot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tool.ExecutionSnapshot.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='tool.ExecutionSnapshot.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operation', full_name='tool.ExecutionSnapshot.operation', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='packageId', full_name='tool.ExecutionSnapshot.packageId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versionId', full_name='tool.ExecutionSnapshot.versionId', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targets', full_name='tool.ExecutionSnapshot.targets', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actions', full_name='tool.ExecutionSnapshot.actions', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='callback', full_name='tool.ExecutionSnapshot.callback', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extraInfo', full_name='tool.ExecutionSnapshot.extraInfo', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='needNotify', full_name='tool.ExecutionSnapshot.needNotify', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_EXECUTIONSNAPSHOT_TARGETS, _EXECUTIONSNAPSHOT_ACTIONS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=662,
)

_EXECUTIONSNAPSHOT_TARGETS.containing_type = _EXECUTIONSNAPSHOT
_EXECUTIONSNAPSHOT_ACTIONS_PARAM.containing_type = _EXECUTIONSNAPSHOT_ACTIONS
_EXECUTIONSNAPSHOT_ACTIONS.fields_by_name['param'].message_type = _EXECUTIONSNAPSHOT_ACTIONS_PARAM
_EXECUTIONSNAPSHOT_ACTIONS.containing_type = _EXECUTIONSNAPSHOT
_EXECUTIONSNAPSHOT.fields_by_name['targets'].message_type = _EXECUTIONSNAPSHOT_TARGETS
_EXECUTIONSNAPSHOT.fields_by_name['actions'].message_type = _EXECUTIONSNAPSHOT_ACTIONS
_EXECUTIONSNAPSHOT.fields_by_name['callback'].message_type = idcmanager__sdk_dot_model_dot_tool_dot_callback__pb2._CALLBACK
_EXECUTIONSNAPSHOT.fields_by_name['extraInfo'].message_type = idcmanager__sdk_dot_model_dot_tool_dot_extra__info__pb2._EXTRAINFO
DESCRIPTOR.message_types_by_name['ExecutionSnapshot'] = _EXECUTIONSNAPSHOT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExecutionSnapshot = _reflection.GeneratedProtocolMessageType('ExecutionSnapshot', (_message.Message,), {

  'Targets' : _reflection.GeneratedProtocolMessageType('Targets', (_message.Message,), {
    'DESCRIPTOR' : _EXECUTIONSNAPSHOT_TARGETS,
    '__module__' : 'execution_snapshot_pb2'
    # @@protoc_insertion_point(class_scope:tool.ExecutionSnapshot.Targets)
    })
  ,

  'Actions' : _reflection.GeneratedProtocolMessageType('Actions', (_message.Message,), {

    'Param' : _reflection.GeneratedProtocolMessageType('Param', (_message.Message,), {
      'DESCRIPTOR' : _EXECUTIONSNAPSHOT_ACTIONS_PARAM,
      '__module__' : 'execution_snapshot_pb2'
      # @@protoc_insertion_point(class_scope:tool.ExecutionSnapshot.Actions.Param)
      })
    ,
    'DESCRIPTOR' : _EXECUTIONSNAPSHOT_ACTIONS,
    '__module__' : 'execution_snapshot_pb2'
    # @@protoc_insertion_point(class_scope:tool.ExecutionSnapshot.Actions)
    })
  ,
  'DESCRIPTOR' : _EXECUTIONSNAPSHOT,
  '__module__' : 'execution_snapshot_pb2'
  # @@protoc_insertion_point(class_scope:tool.ExecutionSnapshot)
  })
_sym_db.RegisterMessage(ExecutionSnapshot)
_sym_db.RegisterMessage(ExecutionSnapshot.Targets)
_sym_db.RegisterMessage(ExecutionSnapshot.Actions)
_sym_db.RegisterMessage(ExecutionSnapshot.Actions.Param)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)