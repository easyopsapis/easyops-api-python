# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: idc.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='idc.proto',
  package='assets_inventory',
  syntax='proto3',
  serialized_options=_b('ZJgo.easyops.local/contracts/protorepo-models/easyops/model/assets_inventory'),
  serialized_pb=_b('\n\tidc.proto\x12\x10\x61ssets_inventory\"\xc7\x01\n\x0cInventoryIDC\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08\x62uilding\x18\x03 \x01(\t\x12\x12\n\nshort_name\x18\x04 \x01(\t\x12\x10\n\x08telphone\x18\x05 \x01(\t\x12\x0c\n\x04\x61rea\x18\x06 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x07 \x01(\t\x12\x0e\n\x06status\x18\x08 \x01(\t\x12\x0e\n\x06layout\x18\t \x01(\t\x12\r\n\x05\x63time\x18\n \x01(\t\x12\x0f\n\x07\x63reator\x18\x0b \x01(\tBLZJgo.easyops.local/contracts/protorepo-models/easyops/model/assets_inventoryb\x06proto3')
)




_INVENTORYIDC = _descriptor.Descriptor(
  name='InventoryIDC',
  full_name='assets_inventory.InventoryIDC',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='assets_inventory.InventoryIDC.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='assets_inventory.InventoryIDC.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='building', full_name='assets_inventory.InventoryIDC.building', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='short_name', full_name='assets_inventory.InventoryIDC.short_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='telphone', full_name='assets_inventory.InventoryIDC.telphone', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='area', full_name='assets_inventory.InventoryIDC.area', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='assets_inventory.InventoryIDC.address', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='assets_inventory.InventoryIDC.status', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='layout', full_name='assets_inventory.InventoryIDC.layout', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='assets_inventory.InventoryIDC.ctime', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='assets_inventory.InventoryIDC.creator', index=10,
      number=11, type=9, cpp_type=9, label=1,
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
  serialized_start=32,
  serialized_end=231,
)

DESCRIPTOR.message_types_by_name['InventoryIDC'] = _INVENTORYIDC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InventoryIDC = _reflection.GeneratedProtocolMessageType('InventoryIDC', (_message.Message,), {
  'DESCRIPTOR' : _INVENTORYIDC,
  '__module__' : 'idc_pb2'
  # @@protoc_insertion_point(class_scope:assets_inventory.InventoryIDC)
  })
_sym_db.RegisterMessage(InventoryIDC)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
