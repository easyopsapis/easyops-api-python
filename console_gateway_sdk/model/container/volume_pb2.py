# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: volume.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from console_gateway_sdk.model.container import key_to_path_pb2 as console__gateway__sdk_dot_model_dot_container_dot_key__to__path__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='volume.proto',
  package='container',
  syntax='proto3',
  serialized_options=_b('ZCgo.easyops.local/contracts/protorepo-models/easyops/model/container'),
  serialized_pb=_b('\n\x0cvolume.proto\x12\tcontainer\x1a\x35\x63onsole_gateway_sdk/model/container/key_to_path.proto\"\xfa\x04\n\x06Volume\x12\x0c\n\x04name\x18\x01 \x01(\t\x12,\n\x08hostPath\x18\x02 \x01(\x0b\x32\x1a.container.Volume.HostPath\x12,\n\x08\x65mptyDir\x18\x03 \x01(\x0b\x32\x1a.container.Volume.EmptyDir\x12(\n\x06secret\x18\x04 \x01(\x0b\x32\x18.container.Volume.Secret\x12.\n\tconfigMap\x18\x05 \x01(\x0b\x32\x1b.container.Volume.ConfigMap\x12\x46\n\x15persistentVolumeClaim\x18\x06 \x01(\x0b\x32\'.container.Volume.PersistentVolumeClaim\x1a&\n\x08HostPath\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x1a-\n\x08\x45mptyDir\x12\x0e\n\x06medium\x18\x01 \x01(\t\x12\x11\n\tsizeLimit\x18\x02 \x01(\t\x1ah\n\x06Secret\x12\x12\n\nsecretName\x18\x01 \x01(\t\x12#\n\x05items\x18\x02 \x03(\x0b\x32\x14.container.KeyToPath\x12\x13\n\x0b\x64\x65\x66\x61ultMode\x18\x03 \x01(\x05\x12\x10\n\x08optional\x18\x04 \x01(\x08\x1a\x65\n\tConfigMap\x12\x0c\n\x04name\x18\x01 \x01(\t\x12#\n\x05items\x18\x02 \x03(\x0b\x32\x14.container.KeyToPath\x12\x13\n\x0b\x64\x65\x66\x61ultMode\x18\x03 \x01(\x05\x12\x10\n\x08optional\x18\x04 \x01(\x08\x1a<\n\x15PersistentVolumeClaim\x12\x11\n\tclaimName\x18\x01 \x01(\t\x12\x10\n\x08readOnly\x18\x02 \x01(\x08\x42\x45ZCgo.easyops.local/contracts/protorepo-models/easyops/model/containerb\x06proto3')
  ,
  dependencies=[console__gateway__sdk_dot_model_dot_container_dot_key__to__path__pb2.DESCRIPTOR,])




_VOLUME_HOSTPATH = _descriptor.Descriptor(
  name='HostPath',
  full_name='container.Volume.HostPath',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='container.Volume.HostPath.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='container.Volume.HostPath.type', index=1,
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
  serialized_start=361,
  serialized_end=399,
)

_VOLUME_EMPTYDIR = _descriptor.Descriptor(
  name='EmptyDir',
  full_name='container.Volume.EmptyDir',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='medium', full_name='container.Volume.EmptyDir.medium', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sizeLimit', full_name='container.Volume.EmptyDir.sizeLimit', index=1,
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
  serialized_start=401,
  serialized_end=446,
)

_VOLUME_SECRET = _descriptor.Descriptor(
  name='Secret',
  full_name='container.Volume.Secret',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='secretName', full_name='container.Volume.Secret.secretName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='items', full_name='container.Volume.Secret.items', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='defaultMode', full_name='container.Volume.Secret.defaultMode', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='optional', full_name='container.Volume.Secret.optional', index=3,
      number=4, type=8, cpp_type=7, label=1,
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
  serialized_start=448,
  serialized_end=552,
)

_VOLUME_CONFIGMAP = _descriptor.Descriptor(
  name='ConfigMap',
  full_name='container.Volume.ConfigMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='container.Volume.ConfigMap.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='items', full_name='container.Volume.ConfigMap.items', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='defaultMode', full_name='container.Volume.ConfigMap.defaultMode', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='optional', full_name='container.Volume.ConfigMap.optional', index=3,
      number=4, type=8, cpp_type=7, label=1,
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
  serialized_start=554,
  serialized_end=655,
)

_VOLUME_PERSISTENTVOLUMECLAIM = _descriptor.Descriptor(
  name='PersistentVolumeClaim',
  full_name='container.Volume.PersistentVolumeClaim',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='claimName', full_name='container.Volume.PersistentVolumeClaim.claimName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readOnly', full_name='container.Volume.PersistentVolumeClaim.readOnly', index=1,
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
  serialized_start=657,
  serialized_end=717,
)

_VOLUME = _descriptor.Descriptor(
  name='Volume',
  full_name='container.Volume',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='container.Volume.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hostPath', full_name='container.Volume.hostPath', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='emptyDir', full_name='container.Volume.emptyDir', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secret', full_name='container.Volume.secret', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='configMap', full_name='container.Volume.configMap', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='persistentVolumeClaim', full_name='container.Volume.persistentVolumeClaim', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_VOLUME_HOSTPATH, _VOLUME_EMPTYDIR, _VOLUME_SECRET, _VOLUME_CONFIGMAP, _VOLUME_PERSISTENTVOLUMECLAIM, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=83,
  serialized_end=717,
)

_VOLUME_HOSTPATH.containing_type = _VOLUME
_VOLUME_EMPTYDIR.containing_type = _VOLUME
_VOLUME_SECRET.fields_by_name['items'].message_type = console__gateway__sdk_dot_model_dot_container_dot_key__to__path__pb2._KEYTOPATH
_VOLUME_SECRET.containing_type = _VOLUME
_VOLUME_CONFIGMAP.fields_by_name['items'].message_type = console__gateway__sdk_dot_model_dot_container_dot_key__to__path__pb2._KEYTOPATH
_VOLUME_CONFIGMAP.containing_type = _VOLUME
_VOLUME_PERSISTENTVOLUMECLAIM.containing_type = _VOLUME
_VOLUME.fields_by_name['hostPath'].message_type = _VOLUME_HOSTPATH
_VOLUME.fields_by_name['emptyDir'].message_type = _VOLUME_EMPTYDIR
_VOLUME.fields_by_name['secret'].message_type = _VOLUME_SECRET
_VOLUME.fields_by_name['configMap'].message_type = _VOLUME_CONFIGMAP
_VOLUME.fields_by_name['persistentVolumeClaim'].message_type = _VOLUME_PERSISTENTVOLUMECLAIM
DESCRIPTOR.message_types_by_name['Volume'] = _VOLUME
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Volume = _reflection.GeneratedProtocolMessageType('Volume', (_message.Message,), {

  'HostPath' : _reflection.GeneratedProtocolMessageType('HostPath', (_message.Message,), {
    'DESCRIPTOR' : _VOLUME_HOSTPATH,
    '__module__' : 'volume_pb2'
    # @@protoc_insertion_point(class_scope:container.Volume.HostPath)
    })
  ,

  'EmptyDir' : _reflection.GeneratedProtocolMessageType('EmptyDir', (_message.Message,), {
    'DESCRIPTOR' : _VOLUME_EMPTYDIR,
    '__module__' : 'volume_pb2'
    # @@protoc_insertion_point(class_scope:container.Volume.EmptyDir)
    })
  ,

  'Secret' : _reflection.GeneratedProtocolMessageType('Secret', (_message.Message,), {
    'DESCRIPTOR' : _VOLUME_SECRET,
    '__module__' : 'volume_pb2'
    # @@protoc_insertion_point(class_scope:container.Volume.Secret)
    })
  ,

  'ConfigMap' : _reflection.GeneratedProtocolMessageType('ConfigMap', (_message.Message,), {
    'DESCRIPTOR' : _VOLUME_CONFIGMAP,
    '__module__' : 'volume_pb2'
    # @@protoc_insertion_point(class_scope:container.Volume.ConfigMap)
    })
  ,

  'PersistentVolumeClaim' : _reflection.GeneratedProtocolMessageType('PersistentVolumeClaim', (_message.Message,), {
    'DESCRIPTOR' : _VOLUME_PERSISTENTVOLUMECLAIM,
    '__module__' : 'volume_pb2'
    # @@protoc_insertion_point(class_scope:container.Volume.PersistentVolumeClaim)
    })
  ,
  'DESCRIPTOR' : _VOLUME,
  '__module__' : 'volume_pb2'
  # @@protoc_insertion_point(class_scope:container.Volume)
  })
_sym_db.RegisterMessage(Volume)
_sym_db.RegisterMessage(Volume.HostPath)
_sym_db.RegisterMessage(Volume.EmptyDir)
_sym_db.RegisterMessage(Volume.Secret)
_sym_db.RegisterMessage(Volume.ConfigMap)
_sym_db.RegisterMessage(Volume.PersistentVolumeClaim)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
