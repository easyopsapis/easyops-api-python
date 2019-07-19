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


from model.inspection import info_pb2 as model_dot_inspection_dot_info__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='update.proto',
  package='info',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0cupdate.proto\x12\x04info\x1a\x1bmodel/inspection/info.proto\"L\n\x1bUpdateInspectionInfoRequest\x12\x10\n\x08pluginId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05index\x18\x03 \x01(\x05\"\x81\x01\n#UpdateInspectionInfoResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12(\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x1a.inspection.InspectionInfob\x06proto3')
  ,
  dependencies=[model_dot_inspection_dot_info__pb2.DESCRIPTOR,])




_UPDATEINSPECTIONINFOREQUEST = _descriptor.Descriptor(
  name='UpdateInspectionInfoRequest',
  full_name='info.UpdateInspectionInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pluginId', full_name='info.UpdateInspectionInfoRequest.pluginId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='info.UpdateInspectionInfoRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='index', full_name='info.UpdateInspectionInfoRequest.index', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=51,
  serialized_end=127,
)


_UPDATEINSPECTIONINFORESPONSEWRAPPER = _descriptor.Descriptor(
  name='UpdateInspectionInfoResponseWrapper',
  full_name='info.UpdateInspectionInfoResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='info.UpdateInspectionInfoResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='info.UpdateInspectionInfoResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='info.UpdateInspectionInfoResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='info.UpdateInspectionInfoResponseWrapper.data', index=3,
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
  serialized_start=130,
  serialized_end=259,
)

_UPDATEINSPECTIONINFORESPONSEWRAPPER.fields_by_name['data'].message_type = model_dot_inspection_dot_info__pb2._INSPECTIONINFO
DESCRIPTOR.message_types_by_name['UpdateInspectionInfoRequest'] = _UPDATEINSPECTIONINFOREQUEST
DESCRIPTOR.message_types_by_name['UpdateInspectionInfoResponseWrapper'] = _UPDATEINSPECTIONINFORESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateInspectionInfoRequest = _reflection.GeneratedProtocolMessageType('UpdateInspectionInfoRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEINSPECTIONINFOREQUEST,
  __module__ = 'update_pb2'
  # @@protoc_insertion_point(class_scope:info.UpdateInspectionInfoRequest)
  ))
_sym_db.RegisterMessage(UpdateInspectionInfoRequest)

UpdateInspectionInfoResponseWrapper = _reflection.GeneratedProtocolMessageType('UpdateInspectionInfoResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEINSPECTIONINFORESPONSEWRAPPER,
  __module__ = 'update_pb2'
  # @@protoc_insertion_point(class_scope:info.UpdateInspectionInfoResponseWrapper)
  ))
_sym_db.RegisterMessage(UpdateInspectionInfoResponseWrapper)


# @@protoc_insertion_point(module_scope)