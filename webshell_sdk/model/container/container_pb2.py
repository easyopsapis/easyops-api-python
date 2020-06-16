# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: container.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from webshell_sdk.model.container import container_port_pb2 as webshell__sdk_dot_model_dot_container_dot_container__port__pb2
from webshell_sdk.model.container import volume_mount_pb2 as webshell__sdk_dot_model_dot_container_dot_volume__mount__pb2
from webshell_sdk.model.container import env_var_pb2 as webshell__sdk_dot_model_dot_container_dot_env__var__pb2
from webshell_sdk.model.container import resource_requirements_pb2 as webshell__sdk_dot_model_dot_container_dot_resource__requirements__pb2
from webshell_sdk.model.container import probe_pb2 as webshell__sdk_dot_model_dot_container_dot_probe__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='container.proto',
  package='container',
  syntax='proto3',
  serialized_options=_b('ZCgo.easyops.local/contracts/protorepo-models/easyops/model/container'),
  serialized_pb=_b('\n\x0f\x63ontainer.proto\x12\tcontainer\x1a\x31webshell_sdk/model/container/container_port.proto\x1a/webshell_sdk/model/container/volume_mount.proto\x1a*webshell_sdk/model/container/env_var.proto\x1a\x38webshell_sdk/model/container/resource_requirements.proto\x1a(webshell_sdk/model/container/probe.proto\"\x91\x03\n\x0f\x43ontainerConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05image\x18\x02 \x01(\t\x12\x12\n\nworkingDir\x18\x03 \x01(\t\x12\x17\n\x0fimagePullPolicy\x18\x04 \x01(\t\x12\x0f\n\x07\x63ommand\x18\x05 \x03(\t\x12\x0c\n\x04\x61rgs\x18\x06 \x03(\t\x12\'\n\x05ports\x18\x07 \x03(\x0b\x32\x18.container.ContainerPort\x12,\n\x0cvolumeMounts\x18\x08 \x03(\x0b\x32\x16.container.VolumeMount\x12\x1e\n\x03\x65nv\x18\t \x03(\x0b\x32\x11.container.EnvVar\x12\x32\n\tresources\x18\n \x01(\x0b\x32\x1f.container.ResourceRequirements\x12(\n\x0ereadinessProbe\x18\x0b \x01(\x0b\x32\x10.container.Probe\x12\'\n\rlivenessProbe\x18\x0c \x01(\x0b\x32\x10.container.Probe\x12\x17\n\x0f\x61rtifactVersion\x18\r \x01(\tBEZCgo.easyops.local/contracts/protorepo-models/easyops/model/containerb\x06proto3')
  ,
  dependencies=[webshell__sdk_dot_model_dot_container_dot_container__port__pb2.DESCRIPTOR,webshell__sdk_dot_model_dot_container_dot_volume__mount__pb2.DESCRIPTOR,webshell__sdk_dot_model_dot_container_dot_env__var__pb2.DESCRIPTOR,webshell__sdk_dot_model_dot_container_dot_resource__requirements__pb2.DESCRIPTOR,webshell__sdk_dot_model_dot_container_dot_probe__pb2.DESCRIPTOR,])




_CONTAINERCONFIG = _descriptor.Descriptor(
  name='ContainerConfig',
  full_name='container.ContainerConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='container.ContainerConfig.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image', full_name='container.ContainerConfig.image', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workingDir', full_name='container.ContainerConfig.workingDir', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='imagePullPolicy', full_name='container.ContainerConfig.imagePullPolicy', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='command', full_name='container.ContainerConfig.command', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='args', full_name='container.ContainerConfig.args', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ports', full_name='container.ContainerConfig.ports', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='volumeMounts', full_name='container.ContainerConfig.volumeMounts', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='env', full_name='container.ContainerConfig.env', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resources', full_name='container.ContainerConfig.resources', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readinessProbe', full_name='container.ContainerConfig.readinessProbe', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='livenessProbe', full_name='container.ContainerConfig.livenessProbe', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='artifactVersion', full_name='container.ContainerConfig.artifactVersion', index=12,
      number=13, type=9, cpp_type=9, label=1,
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
  serialized_start=275,
  serialized_end=676,
)

_CONTAINERCONFIG.fields_by_name['ports'].message_type = webshell__sdk_dot_model_dot_container_dot_container__port__pb2._CONTAINERPORT
_CONTAINERCONFIG.fields_by_name['volumeMounts'].message_type = webshell__sdk_dot_model_dot_container_dot_volume__mount__pb2._VOLUMEMOUNT
_CONTAINERCONFIG.fields_by_name['env'].message_type = webshell__sdk_dot_model_dot_container_dot_env__var__pb2._ENVVAR
_CONTAINERCONFIG.fields_by_name['resources'].message_type = webshell__sdk_dot_model_dot_container_dot_resource__requirements__pb2._RESOURCEREQUIREMENTS
_CONTAINERCONFIG.fields_by_name['readinessProbe'].message_type = webshell__sdk_dot_model_dot_container_dot_probe__pb2._PROBE
_CONTAINERCONFIG.fields_by_name['livenessProbe'].message_type = webshell__sdk_dot_model_dot_container_dot_probe__pb2._PROBE
DESCRIPTOR.message_types_by_name['ContainerConfig'] = _CONTAINERCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ContainerConfig = _reflection.GeneratedProtocolMessageType('ContainerConfig', (_message.Message,), {
  'DESCRIPTOR' : _CONTAINERCONFIG,
  '__module__' : 'container_pb2'
  # @@protoc_insertion_point(class_scope:container.ContainerConfig)
  })
_sym_db.RegisterMessage(ContainerConfig)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
