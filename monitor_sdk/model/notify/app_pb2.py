# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='app.proto',
  package='notify',
  syntax='proto3',
  serialized_options=_b('Z@go.easyops.local/contracts/protorepo-models/easyops/model/notify'),
  serialized_pb=_b('\n\tapp.proto\x12\x06notify\"\'\n\x03\x41pp\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ninstanceId\x18\x02 \x01(\tBBZ@go.easyops.local/contracts/protorepo-models/easyops/model/notifyb\x06proto3')
)




_APP = _descriptor.Descriptor(
  name='App',
  full_name='notify.App',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='notify.App.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceId', full_name='notify.App.instanceId', index=1,
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
  serialized_start=21,
  serialized_end=60,
)

DESCRIPTOR.message_types_by_name['App'] = _APP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

App = _reflection.GeneratedProtocolMessageType('App', (_message.Message,), dict(
  DESCRIPTOR = _APP,
  __module__ = 'app_pb2'
  # @@protoc_insertion_point(class_scope:notify.App)
  ))
_sym_db.RegisterMessage(App)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)