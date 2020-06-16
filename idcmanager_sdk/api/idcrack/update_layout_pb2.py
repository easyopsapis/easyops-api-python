# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: update_layout.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='update_layout.proto',
  package='idcrack',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13update_layout.proto\x12\x07idcrack\"\xba\x01\n\x1aUpdateIDCRackLayoutRequest\x12\x11\n\tidcrackId\x18\x01 \x01(\t\x12:\n\x06layout\x18\x02 \x03(\x0b\x32*.idcrack.UpdateIDCRackLayoutRequest.Layout\x1aM\n\x06Layout\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0e\n\x06startU\x18\x03 \x01(\x05\x12\x11\n\toccupiedU\x18\x04 \x01(\x05\"1\n\x1bUpdateIDCRackLayoutResponse\x12\x12\n\ninstanceId\x18\x01 \x01(\t\"\x8a\x01\n\"UpdateIDCRackLayoutResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x32\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32$.idcrack.UpdateIDCRackLayoutResponseb\x06proto3')
)




_UPDATEIDCRACKLAYOUTREQUEST_LAYOUT = _descriptor.Descriptor(
  name='Layout',
  full_name='idcrack.UpdateIDCRackLayoutRequest.Layout',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='idcrack.UpdateIDCRackLayoutRequest.Layout.instanceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='idcrack.UpdateIDCRackLayoutRequest.Layout.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startU', full_name='idcrack.UpdateIDCRackLayoutRequest.Layout.startU', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='occupiedU', full_name='idcrack.UpdateIDCRackLayoutRequest.Layout.occupiedU', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=142,
  serialized_end=219,
)

_UPDATEIDCRACKLAYOUTREQUEST = _descriptor.Descriptor(
  name='UpdateIDCRackLayoutRequest',
  full_name='idcrack.UpdateIDCRackLayoutRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='idcrackId', full_name='idcrack.UpdateIDCRackLayoutRequest.idcrackId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='layout', full_name='idcrack.UpdateIDCRackLayoutRequest.layout', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_UPDATEIDCRACKLAYOUTREQUEST_LAYOUT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=219,
)


_UPDATEIDCRACKLAYOUTRESPONSE = _descriptor.Descriptor(
  name='UpdateIDCRackLayoutResponse',
  full_name='idcrack.UpdateIDCRackLayoutResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='idcrack.UpdateIDCRackLayoutResponse.instanceId', index=0,
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
  serialized_start=221,
  serialized_end=270,
)


_UPDATEIDCRACKLAYOUTRESPONSEWRAPPER = _descriptor.Descriptor(
  name='UpdateIDCRackLayoutResponseWrapper',
  full_name='idcrack.UpdateIDCRackLayoutResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='idcrack.UpdateIDCRackLayoutResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='idcrack.UpdateIDCRackLayoutResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='idcrack.UpdateIDCRackLayoutResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='idcrack.UpdateIDCRackLayoutResponseWrapper.data', index=3,
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
  serialized_start=273,
  serialized_end=411,
)

_UPDATEIDCRACKLAYOUTREQUEST_LAYOUT.containing_type = _UPDATEIDCRACKLAYOUTREQUEST
_UPDATEIDCRACKLAYOUTREQUEST.fields_by_name['layout'].message_type = _UPDATEIDCRACKLAYOUTREQUEST_LAYOUT
_UPDATEIDCRACKLAYOUTRESPONSEWRAPPER.fields_by_name['data'].message_type = _UPDATEIDCRACKLAYOUTRESPONSE
DESCRIPTOR.message_types_by_name['UpdateIDCRackLayoutRequest'] = _UPDATEIDCRACKLAYOUTREQUEST
DESCRIPTOR.message_types_by_name['UpdateIDCRackLayoutResponse'] = _UPDATEIDCRACKLAYOUTRESPONSE
DESCRIPTOR.message_types_by_name['UpdateIDCRackLayoutResponseWrapper'] = _UPDATEIDCRACKLAYOUTRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateIDCRackLayoutRequest = _reflection.GeneratedProtocolMessageType('UpdateIDCRackLayoutRequest', (_message.Message,), {

  'Layout' : _reflection.GeneratedProtocolMessageType('Layout', (_message.Message,), {
    'DESCRIPTOR' : _UPDATEIDCRACKLAYOUTREQUEST_LAYOUT,
    '__module__' : 'update_layout_pb2'
    # @@protoc_insertion_point(class_scope:idcrack.UpdateIDCRackLayoutRequest.Layout)
    })
  ,
  'DESCRIPTOR' : _UPDATEIDCRACKLAYOUTREQUEST,
  '__module__' : 'update_layout_pb2'
  # @@protoc_insertion_point(class_scope:idcrack.UpdateIDCRackLayoutRequest)
  })
_sym_db.RegisterMessage(UpdateIDCRackLayoutRequest)
_sym_db.RegisterMessage(UpdateIDCRackLayoutRequest.Layout)

UpdateIDCRackLayoutResponse = _reflection.GeneratedProtocolMessageType('UpdateIDCRackLayoutResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEIDCRACKLAYOUTRESPONSE,
  '__module__' : 'update_layout_pb2'
  # @@protoc_insertion_point(class_scope:idcrack.UpdateIDCRackLayoutResponse)
  })
_sym_db.RegisterMessage(UpdateIDCRackLayoutResponse)

UpdateIDCRackLayoutResponseWrapper = _reflection.GeneratedProtocolMessageType('UpdateIDCRackLayoutResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEIDCRACKLAYOUTRESPONSEWRAPPER,
  '__module__' : 'update_layout_pb2'
  # @@protoc_insertion_point(class_scope:idcrack.UpdateIDCRackLayoutResponseWrapper)
  })
_sym_db.RegisterMessage(UpdateIDCRackLayoutResponseWrapper)


# @@protoc_insertion_point(module_scope)
