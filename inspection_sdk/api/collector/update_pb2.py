# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: update.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from model.inspection import collector_pb2 as model_dot_inspection_dot_collector__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='update.proto',
  package='collector',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0cupdate.proto\x12\tcollector\x1a model/inspection/collector.proto\"\xe1\x01\n\x16UpdateCollectorRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x63ollectorId\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x04 \x01(\t\x12\x0e\n\x06script\x18\x05 \x01(\t\x12\x34\n\x04\x61rgs\x18\x06 \x03(\x0b\x32&.collector.UpdateCollectorRequest.Args\x1a\x41\n\x04\x41rgs\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05\x61lias\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x0f\n\x07require\x18\x04 \x01(\x08\"\x81\x01\n\x1eUpdateCollectorResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12-\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1f.inspection.InspectionCollectorb\x06proto3')
  ,
  dependencies=[model_dot_inspection_dot_collector__pb2.DESCRIPTOR,])




_UPDATECOLLECTORREQUEST_ARGS = _descriptor.Descriptor(
  name='Args',
  full_name='collector.UpdateCollectorRequest.Args',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='collector.UpdateCollectorRequest.Args.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alias', full_name='collector.UpdateCollectorRequest.Args.alias', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='collector.UpdateCollectorRequest.Args.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='require', full_name='collector.UpdateCollectorRequest.Args.require', index=3,
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
  serialized_start=222,
  serialized_end=287,
)

_UPDATECOLLECTORREQUEST = _descriptor.Descriptor(
  name='UpdateCollectorRequest',
  full_name='collector.UpdateCollectorRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='collector.UpdateCollectorRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collectorId', full_name='collector.UpdateCollectorRequest.collectorId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='collector.UpdateCollectorRequest.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='collector.UpdateCollectorRequest.content', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='script', full_name='collector.UpdateCollectorRequest.script', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='args', full_name='collector.UpdateCollectorRequest.args', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_UPDATECOLLECTORREQUEST_ARGS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=287,
)


_UPDATECOLLECTORRESPONSEWRAPPER = _descriptor.Descriptor(
  name='UpdateCollectorResponseWrapper',
  full_name='collector.UpdateCollectorResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='collector.UpdateCollectorResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='collector.UpdateCollectorResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='collector.UpdateCollectorResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='collector.UpdateCollectorResponseWrapper.data', index=3,
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
  serialized_start=290,
  serialized_end=419,
)

_UPDATECOLLECTORREQUEST_ARGS.containing_type = _UPDATECOLLECTORREQUEST
_UPDATECOLLECTORREQUEST.fields_by_name['args'].message_type = _UPDATECOLLECTORREQUEST_ARGS
_UPDATECOLLECTORRESPONSEWRAPPER.fields_by_name['data'].message_type = model_dot_inspection_dot_collector__pb2._INSPECTIONCOLLECTOR
DESCRIPTOR.message_types_by_name['UpdateCollectorRequest'] = _UPDATECOLLECTORREQUEST
DESCRIPTOR.message_types_by_name['UpdateCollectorResponseWrapper'] = _UPDATECOLLECTORRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateCollectorRequest = _reflection.GeneratedProtocolMessageType('UpdateCollectorRequest', (_message.Message,), dict(

  Args = _reflection.GeneratedProtocolMessageType('Args', (_message.Message,), dict(
    DESCRIPTOR = _UPDATECOLLECTORREQUEST_ARGS,
    __module__ = 'update_pb2'
    # @@protoc_insertion_point(class_scope:collector.UpdateCollectorRequest.Args)
    ))
  ,
  DESCRIPTOR = _UPDATECOLLECTORREQUEST,
  __module__ = 'update_pb2'
  # @@protoc_insertion_point(class_scope:collector.UpdateCollectorRequest)
  ))
_sym_db.RegisterMessage(UpdateCollectorRequest)
_sym_db.RegisterMessage(UpdateCollectorRequest.Args)

UpdateCollectorResponseWrapper = _reflection.GeneratedProtocolMessageType('UpdateCollectorResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _UPDATECOLLECTORRESPONSEWRAPPER,
  __module__ = 'update_pb2'
  # @@protoc_insertion_point(class_scope:collector.UpdateCollectorResponseWrapper)
  ))
_sym_db.RegisterMessage(UpdateCollectorResponseWrapper)


# @@protoc_insertion_point(module_scope)