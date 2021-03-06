# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: node_detail.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from idcmanager_sdk.model.container import metadata_pb2 as idcmanager__sdk_dot_model_dot_container_dot_metadata__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='node_detail.proto',
  package='container',
  syntax='proto3',
  serialized_options=_b('ZCgo.easyops.local/contracts/protorepo-models/easyops/model/container'),
  serialized_pb=_b('\n\x11node_detail.proto\x12\tcontainer\x1a-idcmanager_sdk/model/container/metadata.proto\"\xa3\x06\n\nNodeDetail\x12%\n\x08metadata\x18\x01 \x01(\x0b\x32\x13.container.Metadata\x12(\n\x04spec\x18\x02 \x01(\x0b\x32\x1a.container.NodeDetail.Spec\x12,\n\x06status\x18\x03 \x01(\x0b\x32\x1c.container.NodeDetail.Status\x12\x0e\n\x06worker\x18\x04 \x01(\x08\x1a\x42\n\x04Spec\x12\x0f\n\x07podCIDR\x18\x01 \x01(\t\x12\x12\n\nproviderID\x18\x02 \x01(\t\x12\x15\n\runschedulable\x18\x03 \x01(\x08\x1a\xc1\x04\n\x06Status\x12\x37\n\x08\x63\x61pacity\x18\x01 \x01(\x0b\x32%.container.NodeDetail.Status.Capacity\x12=\n\x0b\x61llocatable\x18\x02 \x01(\x0b\x32(.container.NodeDetail.Status.Allocatable\x12\r\n\x05phase\x18\x03 \x01(\t\x12\x37\n\x08nodeInfo\x18\x04 \x01(\x0b\x32%.container.NodeDetail.Status.NodeInfo\x1aO\n\x08\x43\x61pacity\x12\x0b\n\x03\x63pu\x18\x01 \x01(\t\x12\x0e\n\x06memory\x18\x02 \x01(\t\x12\x0c\n\x04pods\x18\x03 \x01(\t\x12\x18\n\x10\x65phemeralStorage\x18\x04 \x01(\t\x1a\x38\n\x0b\x41llocatable\x12\x0b\n\x03\x63pu\x18\x01 \x01(\t\x12\x0e\n\x06memory\x18\x02 \x01(\t\x12\x0c\n\x04pods\x18\x03 \x01(\t\x1a\xeb\x01\n\x08NodeInfo\x12\x11\n\tmachineID\x18\x01 \x01(\t\x12\x12\n\nsystemUUID\x18\x02 \x01(\t\x12\x0e\n\x06\x62ootID\x18\x03 \x01(\t\x12\x15\n\rkernelVersion\x18\x04 \x01(\t\x12\x0f\n\x07osImage\x18\x05 \x01(\t\x12\x1f\n\x17\x63ontainerRuntimeVersion\x18\x06 \x01(\t\x12\x16\n\x0ekubeletVersion\x18\x07 \x01(\t\x12\x18\n\x10kubeProxyVersion\x18\x08 \x01(\t\x12\x17\n\x0foperatingSystem\x18\t \x01(\t\x12\x14\n\x0c\x61rchitecture\x18\n \x01(\tBEZCgo.easyops.local/contracts/protorepo-models/easyops/model/containerb\x06proto3')
  ,
  dependencies=[idcmanager__sdk_dot_model_dot_container_dot_metadata__pb2.DESCRIPTOR,])




_NODEDETAIL_SPEC = _descriptor.Descriptor(
  name='Spec',
  full_name='container.NodeDetail.Spec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='podCIDR', full_name='container.NodeDetail.Spec.podCIDR', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='providerID', full_name='container.NodeDetail.Spec.providerID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unschedulable', full_name='container.NodeDetail.Spec.unschedulable', index=2,
      number=3, type=8, cpp_type=7, label=1,
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
  serialized_start=237,
  serialized_end=303,
)

_NODEDETAIL_STATUS_CAPACITY = _descriptor.Descriptor(
  name='Capacity',
  full_name='container.NodeDetail.Status.Capacity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cpu', full_name='container.NodeDetail.Status.Capacity.cpu', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memory', full_name='container.NodeDetail.Status.Capacity.memory', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pods', full_name='container.NodeDetail.Status.Capacity.pods', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ephemeralStorage', full_name='container.NodeDetail.Status.Capacity.ephemeralStorage', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=508,
  serialized_end=587,
)

_NODEDETAIL_STATUS_ALLOCATABLE = _descriptor.Descriptor(
  name='Allocatable',
  full_name='container.NodeDetail.Status.Allocatable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cpu', full_name='container.NodeDetail.Status.Allocatable.cpu', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memory', full_name='container.NodeDetail.Status.Allocatable.memory', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pods', full_name='container.NodeDetail.Status.Allocatable.pods', index=2,
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
  serialized_start=589,
  serialized_end=645,
)

_NODEDETAIL_STATUS_NODEINFO = _descriptor.Descriptor(
  name='NodeInfo',
  full_name='container.NodeDetail.Status.NodeInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='machineID', full_name='container.NodeDetail.Status.NodeInfo.machineID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='systemUUID', full_name='container.NodeDetail.Status.NodeInfo.systemUUID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bootID', full_name='container.NodeDetail.Status.NodeInfo.bootID', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kernelVersion', full_name='container.NodeDetail.Status.NodeInfo.kernelVersion', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='osImage', full_name='container.NodeDetail.Status.NodeInfo.osImage', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='containerRuntimeVersion', full_name='container.NodeDetail.Status.NodeInfo.containerRuntimeVersion', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kubeletVersion', full_name='container.NodeDetail.Status.NodeInfo.kubeletVersion', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kubeProxyVersion', full_name='container.NodeDetail.Status.NodeInfo.kubeProxyVersion', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operatingSystem', full_name='container.NodeDetail.Status.NodeInfo.operatingSystem', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='architecture', full_name='container.NodeDetail.Status.NodeInfo.architecture', index=9,
      number=10, type=9, cpp_type=9, label=1,
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
  serialized_start=648,
  serialized_end=883,
)

_NODEDETAIL_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='container.NodeDetail.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='capacity', full_name='container.NodeDetail.Status.capacity', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='allocatable', full_name='container.NodeDetail.Status.allocatable', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='phase', full_name='container.NodeDetail.Status.phase', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nodeInfo', full_name='container.NodeDetail.Status.nodeInfo', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_NODEDETAIL_STATUS_CAPACITY, _NODEDETAIL_STATUS_ALLOCATABLE, _NODEDETAIL_STATUS_NODEINFO, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=306,
  serialized_end=883,
)

_NODEDETAIL = _descriptor.Descriptor(
  name='NodeDetail',
  full_name='container.NodeDetail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadata', full_name='container.NodeDetail.metadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spec', full_name='container.NodeDetail.spec', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='container.NodeDetail.status', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='worker', full_name='container.NodeDetail.worker', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_NODEDETAIL_SPEC, _NODEDETAIL_STATUS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=883,
)

_NODEDETAIL_SPEC.containing_type = _NODEDETAIL
_NODEDETAIL_STATUS_CAPACITY.containing_type = _NODEDETAIL_STATUS
_NODEDETAIL_STATUS_ALLOCATABLE.containing_type = _NODEDETAIL_STATUS
_NODEDETAIL_STATUS_NODEINFO.containing_type = _NODEDETAIL_STATUS
_NODEDETAIL_STATUS.fields_by_name['capacity'].message_type = _NODEDETAIL_STATUS_CAPACITY
_NODEDETAIL_STATUS.fields_by_name['allocatable'].message_type = _NODEDETAIL_STATUS_ALLOCATABLE
_NODEDETAIL_STATUS.fields_by_name['nodeInfo'].message_type = _NODEDETAIL_STATUS_NODEINFO
_NODEDETAIL_STATUS.containing_type = _NODEDETAIL
_NODEDETAIL.fields_by_name['metadata'].message_type = idcmanager__sdk_dot_model_dot_container_dot_metadata__pb2._METADATA
_NODEDETAIL.fields_by_name['spec'].message_type = _NODEDETAIL_SPEC
_NODEDETAIL.fields_by_name['status'].message_type = _NODEDETAIL_STATUS
DESCRIPTOR.message_types_by_name['NodeDetail'] = _NODEDETAIL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NodeDetail = _reflection.GeneratedProtocolMessageType('NodeDetail', (_message.Message,), {

  'Spec' : _reflection.GeneratedProtocolMessageType('Spec', (_message.Message,), {
    'DESCRIPTOR' : _NODEDETAIL_SPEC,
    '__module__' : 'node_detail_pb2'
    # @@protoc_insertion_point(class_scope:container.NodeDetail.Spec)
    })
  ,

  'Status' : _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {

    'Capacity' : _reflection.GeneratedProtocolMessageType('Capacity', (_message.Message,), {
      'DESCRIPTOR' : _NODEDETAIL_STATUS_CAPACITY,
      '__module__' : 'node_detail_pb2'
      # @@protoc_insertion_point(class_scope:container.NodeDetail.Status.Capacity)
      })
    ,

    'Allocatable' : _reflection.GeneratedProtocolMessageType('Allocatable', (_message.Message,), {
      'DESCRIPTOR' : _NODEDETAIL_STATUS_ALLOCATABLE,
      '__module__' : 'node_detail_pb2'
      # @@protoc_insertion_point(class_scope:container.NodeDetail.Status.Allocatable)
      })
    ,

    'NodeInfo' : _reflection.GeneratedProtocolMessageType('NodeInfo', (_message.Message,), {
      'DESCRIPTOR' : _NODEDETAIL_STATUS_NODEINFO,
      '__module__' : 'node_detail_pb2'
      # @@protoc_insertion_point(class_scope:container.NodeDetail.Status.NodeInfo)
      })
    ,
    'DESCRIPTOR' : _NODEDETAIL_STATUS,
    '__module__' : 'node_detail_pb2'
    # @@protoc_insertion_point(class_scope:container.NodeDetail.Status)
    })
  ,
  'DESCRIPTOR' : _NODEDETAIL,
  '__module__' : 'node_detail_pb2'
  # @@protoc_insertion_point(class_scope:container.NodeDetail)
  })
_sym_db.RegisterMessage(NodeDetail)
_sym_db.RegisterMessage(NodeDetail.Spec)
_sym_db.RegisterMessage(NodeDetail.Status)
_sym_db.RegisterMessage(NodeDetail.Status.Capacity)
_sym_db.RegisterMessage(NodeDetail.Status.Allocatable)
_sym_db.RegisterMessage(NodeDetail.Status.NodeInfo)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
