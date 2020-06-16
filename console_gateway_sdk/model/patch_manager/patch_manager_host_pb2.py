# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: patch_manager_host.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='patch_manager_host.proto',
  package='patch_manager',
  syntax='proto3',
  serialized_options=_b('ZGgo.easyops.local/contracts/protorepo-models/easyops/model/patch_manager'),
  serialized_pb=_b('\n\x18patch_manager_host.proto\x12\rpatch_manager\"\x90\x03\n\x10PatchManagerHost\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x10\n\x08hostname\x18\x02 \x01(\t\x12\n\n\x02ip\x18\x03 \x01(\t\x12\x14\n\x0c_agentStatus\x18\x04 \x01(\t\x12\x14\n\x0c_environment\x18\x05 \x01(\t\x12\x10\n\x08osSystem\x18\x06 \x01(\t\x12\x16\n\x0eosArchitecture\x18\x07 \x01(\t\x12\x11\n\tosVersion\x18\x08 \x01(\t\x12\x11\n\tosRelease\x18\t \x01(\t\x12\x15\n\rrequireReboot\x18\n \x01(\x08\x12\x15\n\rlastStartTime\x18\x0b \x01(\x05\x12\x1c\n\x14lastInstallPatchTime\x18\x0c \x01(\x05\x12\x46\n\x0einstalledPatch\x18\r \x03(\x0b\x32..patch_manager.PatchManagerHost.InstalledPatch\x1a:\n\x0eInstalledPatch\x12\x11\n\tarticleId\x18\x01 \x01(\t\x12\x15\n\rinstalledTime\x18\x02 \x01(\tBIZGgo.easyops.local/contracts/protorepo-models/easyops/model/patch_managerb\x06proto3')
)




_PATCHMANAGERHOST_INSTALLEDPATCH = _descriptor.Descriptor(
  name='InstalledPatch',
  full_name='patch_manager.PatchManagerHost.InstalledPatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='articleId', full_name='patch_manager.PatchManagerHost.InstalledPatch.articleId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='installedTime', full_name='patch_manager.PatchManagerHost.InstalledPatch.installedTime', index=1,
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
  serialized_start=386,
  serialized_end=444,
)

_PATCHMANAGERHOST = _descriptor.Descriptor(
  name='PatchManagerHost',
  full_name='patch_manager.PatchManagerHost',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='patch_manager.PatchManagerHost.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hostname', full_name='patch_manager.PatchManagerHost.hostname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip', full_name='patch_manager.PatchManagerHost.ip', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='_agentStatus', full_name='patch_manager.PatchManagerHost._agentStatus', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='_environment', full_name='patch_manager.PatchManagerHost._environment', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='osSystem', full_name='patch_manager.PatchManagerHost.osSystem', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='osArchitecture', full_name='patch_manager.PatchManagerHost.osArchitecture', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='osVersion', full_name='patch_manager.PatchManagerHost.osVersion', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='osRelease', full_name='patch_manager.PatchManagerHost.osRelease', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requireReboot', full_name='patch_manager.PatchManagerHost.requireReboot', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastStartTime', full_name='patch_manager.PatchManagerHost.lastStartTime', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastInstallPatchTime', full_name='patch_manager.PatchManagerHost.lastInstallPatchTime', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='installedPatch', full_name='patch_manager.PatchManagerHost.installedPatch', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PATCHMANAGERHOST_INSTALLEDPATCH, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=44,
  serialized_end=444,
)

_PATCHMANAGERHOST_INSTALLEDPATCH.containing_type = _PATCHMANAGERHOST
_PATCHMANAGERHOST.fields_by_name['installedPatch'].message_type = _PATCHMANAGERHOST_INSTALLEDPATCH
DESCRIPTOR.message_types_by_name['PatchManagerHost'] = _PATCHMANAGERHOST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PatchManagerHost = _reflection.GeneratedProtocolMessageType('PatchManagerHost', (_message.Message,), {

  'InstalledPatch' : _reflection.GeneratedProtocolMessageType('InstalledPatch', (_message.Message,), {
    'DESCRIPTOR' : _PATCHMANAGERHOST_INSTALLEDPATCH,
    '__module__' : 'patch_manager_host_pb2'
    # @@protoc_insertion_point(class_scope:patch_manager.PatchManagerHost.InstalledPatch)
    })
  ,
  'DESCRIPTOR' : _PATCHMANAGERHOST,
  '__module__' : 'patch_manager_host_pb2'
  # @@protoc_insertion_point(class_scope:patch_manager.PatchManagerHost)
  })
_sym_db.RegisterMessage(PatchManagerHost)
_sym_db.RegisterMessage(PatchManagerHost.InstalledPatch)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)