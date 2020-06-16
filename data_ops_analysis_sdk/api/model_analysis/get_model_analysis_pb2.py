# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_model_analysis.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_model_analysis.proto',
  package='model_analysis',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x18get_model_analysis.proto\x12\x0emodel_analysis\x1a\x1cgoogle/protobuf/struct.proto\"\xd7\x01\n\x18GetModelAnalysisResponse\x12;\n\x04list\x18\x01 \x03(\x0b\x32-.model_analysis.GetModelAnalysisResponse.List\x1a~\n\x04List\x12\x10\n\x08objectId\x18\x01 \x01(\t\x12\x12\n\nobjectName\x18\x02 \x01(\t\x12\r\n\x05\x61ttrs\x18\x03 \x03(\t\x12\x15\n\rinstanceTotal\x18\x04 \x01(\x05\x12*\n\tfailCount\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\"\x8b\x01\n\x1fGetModelAnalysisResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x36\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32(.model_analysis.GetModelAnalysisResponseb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_GETMODELANALYSISRESPONSE_LIST = _descriptor.Descriptor(
  name='List',
  full_name='model_analysis.GetModelAnalysisResponse.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='objectId', full_name='model_analysis.GetModelAnalysisResponse.List.objectId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectName', full_name='model_analysis.GetModelAnalysisResponse.List.objectName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attrs', full_name='model_analysis.GetModelAnalysisResponse.List.attrs', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceTotal', full_name='model_analysis.GetModelAnalysisResponse.List.instanceTotal', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='failCount', full_name='model_analysis.GetModelAnalysisResponse.List.failCount', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=164,
  serialized_end=290,
)

_GETMODELANALYSISRESPONSE = _descriptor.Descriptor(
  name='GetModelAnalysisResponse',
  full_name='model_analysis.GetModelAnalysisResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='list', full_name='model_analysis.GetModelAnalysisResponse.list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETMODELANALYSISRESPONSE_LIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=75,
  serialized_end=290,
)


_GETMODELANALYSISRESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetModelAnalysisResponseWrapper',
  full_name='model_analysis.GetModelAnalysisResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='model_analysis.GetModelAnalysisResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='model_analysis.GetModelAnalysisResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='model_analysis.GetModelAnalysisResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='model_analysis.GetModelAnalysisResponseWrapper.data', index=3,
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
  serialized_start=293,
  serialized_end=432,
)

_GETMODELANALYSISRESPONSE_LIST.fields_by_name['failCount'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_GETMODELANALYSISRESPONSE_LIST.containing_type = _GETMODELANALYSISRESPONSE
_GETMODELANALYSISRESPONSE.fields_by_name['list'].message_type = _GETMODELANALYSISRESPONSE_LIST
_GETMODELANALYSISRESPONSEWRAPPER.fields_by_name['data'].message_type = _GETMODELANALYSISRESPONSE
DESCRIPTOR.message_types_by_name['GetModelAnalysisResponse'] = _GETMODELANALYSISRESPONSE
DESCRIPTOR.message_types_by_name['GetModelAnalysisResponseWrapper'] = _GETMODELANALYSISRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetModelAnalysisResponse = _reflection.GeneratedProtocolMessageType('GetModelAnalysisResponse', (_message.Message,), {

  'List' : _reflection.GeneratedProtocolMessageType('List', (_message.Message,), {
    'DESCRIPTOR' : _GETMODELANALYSISRESPONSE_LIST,
    '__module__' : 'get_model_analysis_pb2'
    # @@protoc_insertion_point(class_scope:model_analysis.GetModelAnalysisResponse.List)
    })
  ,
  'DESCRIPTOR' : _GETMODELANALYSISRESPONSE,
  '__module__' : 'get_model_analysis_pb2'
  # @@protoc_insertion_point(class_scope:model_analysis.GetModelAnalysisResponse)
  })
_sym_db.RegisterMessage(GetModelAnalysisResponse)
_sym_db.RegisterMessage(GetModelAnalysisResponse.List)

GetModelAnalysisResponseWrapper = _reflection.GeneratedProtocolMessageType('GetModelAnalysisResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _GETMODELANALYSISRESPONSEWRAPPER,
  '__module__' : 'get_model_analysis_pb2'
  # @@protoc_insertion_point(class_scope:model_analysis.GetModelAnalysisResponseWrapper)
  })
_sym_db.RegisterMessage(GetModelAnalysisResponseWrapper)


# @@protoc_insertion_point(module_scope)
