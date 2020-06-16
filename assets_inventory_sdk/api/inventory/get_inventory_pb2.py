# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_inventory.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from assets_inventory_sdk.model.assets_inventory import assets_inventory_summary_pb2 as assets__inventory__sdk_dot_model_dot_assets__inventory_dot_assets__inventory__summary__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_inventory.proto',
  package='inventory',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13get_inventory.proto\x12\tinventory\x1aJassets_inventory_sdk/model/assets_inventory/assets_inventory_summary.proto\"M\n\x13GetInventoryRequest\x12\x14\n\x0cinventoryIds\x18\x01 \x01(\t\x12\x0e\n\x06idcIds\x18\x02 \x01(\t\x12\x10\n\x08\x62\x61tchNos\x18\x03 \x01(\t\"V\n\x14GetInventoryResponse\x12>\n\rinventoryList\x18\x01 \x03(\x0b\x32\'.assets_inventory.AssetInventorySummary\"~\n\x1bGetInventoryResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12-\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1f.inventory.GetInventoryResponseb\x06proto3')
  ,
  dependencies=[assets__inventory__sdk_dot_model_dot_assets__inventory_dot_assets__inventory__summary__pb2.DESCRIPTOR,])




_GETINVENTORYREQUEST = _descriptor.Descriptor(
  name='GetInventoryRequest',
  full_name='inventory.GetInventoryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inventoryIds', full_name='inventory.GetInventoryRequest.inventoryIds', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='idcIds', full_name='inventory.GetInventoryRequest.idcIds', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batchNos', full_name='inventory.GetInventoryRequest.batchNos', index=2,
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
  serialized_start=110,
  serialized_end=187,
)


_GETINVENTORYRESPONSE = _descriptor.Descriptor(
  name='GetInventoryResponse',
  full_name='inventory.GetInventoryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inventoryList', full_name='inventory.GetInventoryResponse.inventoryList', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=189,
  serialized_end=275,
)


_GETINVENTORYRESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetInventoryResponseWrapper',
  full_name='inventory.GetInventoryResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='inventory.GetInventoryResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='inventory.GetInventoryResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='inventory.GetInventoryResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='inventory.GetInventoryResponseWrapper.data', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=277,
  serialized_end=403,
)

_GETINVENTORYRESPONSE.fields_by_name['inventoryList'].message_type = assets__inventory__sdk_dot_model_dot_assets__inventory_dot_assets__inventory__summary__pb2._ASSETINVENTORYSUMMARY
_GETINVENTORYRESPONSEWRAPPER.fields_by_name['data'].message_type = _GETINVENTORYRESPONSE
DESCRIPTOR.message_types_by_name['GetInventoryRequest'] = _GETINVENTORYREQUEST
DESCRIPTOR.message_types_by_name['GetInventoryResponse'] = _GETINVENTORYRESPONSE
DESCRIPTOR.message_types_by_name['GetInventoryResponseWrapper'] = _GETINVENTORYRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetInventoryRequest = _reflection.GeneratedProtocolMessageType('GetInventoryRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETINVENTORYREQUEST,
  '__module__' : 'get_inventory_pb2'
  # @@protoc_insertion_point(class_scope:inventory.GetInventoryRequest)
  })
_sym_db.RegisterMessage(GetInventoryRequest)

GetInventoryResponse = _reflection.GeneratedProtocolMessageType('GetInventoryResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETINVENTORYRESPONSE,
  '__module__' : 'get_inventory_pb2'
  # @@protoc_insertion_point(class_scope:inventory.GetInventoryResponse)
  })
_sym_db.RegisterMessage(GetInventoryResponse)

GetInventoryResponseWrapper = _reflection.GeneratedProtocolMessageType('GetInventoryResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _GETINVENTORYRESPONSEWRAPPER,
  '__module__' : 'get_inventory_pb2'
  # @@protoc_insertion_point(class_scope:inventory.GetInventoryResponseWrapper)
  })
_sym_db.RegisterMessage(GetInventoryResponseWrapper)


# @@protoc_insertion_point(module_scope)
