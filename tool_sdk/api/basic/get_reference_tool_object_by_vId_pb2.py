# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_reference_tool_object_by_vId.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_reference_tool_object_by_vId.proto',
  package='basic',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n&get_reference_tool_object_by_vId.proto\x12\x05\x62\x61sic\"A\n\"GetReferenceToolObjectByVidRequest\x12\x0e\n\x06toolId\x18\x01 \x01(\t\x12\x0b\n\x03vId\x18\x02 \x01(\t\"\xed\x02\n#GetReferenceToolObjectByVidResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\r\n\x05\x65rror\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\x12=\n\x04\x64\x61ta\x18\x04 \x03(\x0b\x32/.basic.GetReferenceToolObjectByVidResponse.Data\x1a\xd8\x01\n\x04\x44\x61ta\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x15\n\rtoolVersionId\x18\x04 \x01(\t\x12\x17\n\x0ftoolVersionName\x18\x05 \x01(\t\x12J\n\x08metadata\x18\x06 \x01(\x0b\x32\x38.basic.GetReferenceToolObjectByVidResponse.Data.Metadata\x1a,\n\x08Metadata\x12\x0e\n\x06stepId\x18\x01 \x01(\x05\x12\x10\n\x08stepName\x18\x02 \x01(\t\"\x98\x01\n*GetReferenceToolObjectByVidResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x38\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32*.basic.GetReferenceToolObjectByVidResponseb\x06proto3')
)




_GETREFERENCETOOLOBJECTBYVIDREQUEST = _descriptor.Descriptor(
  name='GetReferenceToolObjectByVidRequest',
  full_name='basic.GetReferenceToolObjectByVidRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='toolId', full_name='basic.GetReferenceToolObjectByVidRequest.toolId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vId', full_name='basic.GetReferenceToolObjectByVidRequest.vId', index=1,
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
  serialized_start=49,
  serialized_end=114,
)


_GETREFERENCETOOLOBJECTBYVIDRESPONSE_DATA_METADATA = _descriptor.Descriptor(
  name='Metadata',
  full_name='basic.GetReferenceToolObjectByVidResponse.Data.Metadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stepId', full_name='basic.GetReferenceToolObjectByVidResponse.Data.Metadata.stepId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stepName', full_name='basic.GetReferenceToolObjectByVidResponse.Data.Metadata.stepName', index=1,
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
  serialized_start=438,
  serialized_end=482,
)

_GETREFERENCETOOLOBJECTBYVIDRESPONSE_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='basic.GetReferenceToolObjectByVidResponse.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='basic.GetReferenceToolObjectByVidResponse.Data.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='basic.GetReferenceToolObjectByVidResponse.Data.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='basic.GetReferenceToolObjectByVidResponse.Data.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='toolVersionId', full_name='basic.GetReferenceToolObjectByVidResponse.Data.toolVersionId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='toolVersionName', full_name='basic.GetReferenceToolObjectByVidResponse.Data.toolVersionName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='basic.GetReferenceToolObjectByVidResponse.Data.metadata', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETREFERENCETOOLOBJECTBYVIDRESPONSE_DATA_METADATA, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=266,
  serialized_end=482,
)

_GETREFERENCETOOLOBJECTBYVIDRESPONSE = _descriptor.Descriptor(
  name='GetReferenceToolObjectByVidResponse',
  full_name='basic.GetReferenceToolObjectByVidResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='basic.GetReferenceToolObjectByVidResponse.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='basic.GetReferenceToolObjectByVidResponse.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='basic.GetReferenceToolObjectByVidResponse.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='basic.GetReferenceToolObjectByVidResponse.data', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETREFERENCETOOLOBJECTBYVIDRESPONSE_DATA, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=482,
)


_GETREFERENCETOOLOBJECTBYVIDRESPONSEWRAPPER = _descriptor.Descriptor(
  name='GetReferenceToolObjectByVidResponseWrapper',
  full_name='basic.GetReferenceToolObjectByVidResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='basic.GetReferenceToolObjectByVidResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='basic.GetReferenceToolObjectByVidResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='basic.GetReferenceToolObjectByVidResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='basic.GetReferenceToolObjectByVidResponseWrapper.data', index=3,
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
  serialized_start=485,
  serialized_end=637,
)

_GETREFERENCETOOLOBJECTBYVIDRESPONSE_DATA_METADATA.containing_type = _GETREFERENCETOOLOBJECTBYVIDRESPONSE_DATA
_GETREFERENCETOOLOBJECTBYVIDRESPONSE_DATA.fields_by_name['metadata'].message_type = _GETREFERENCETOOLOBJECTBYVIDRESPONSE_DATA_METADATA
_GETREFERENCETOOLOBJECTBYVIDRESPONSE_DATA.containing_type = _GETREFERENCETOOLOBJECTBYVIDRESPONSE
_GETREFERENCETOOLOBJECTBYVIDRESPONSE.fields_by_name['data'].message_type = _GETREFERENCETOOLOBJECTBYVIDRESPONSE_DATA
_GETREFERENCETOOLOBJECTBYVIDRESPONSEWRAPPER.fields_by_name['data'].message_type = _GETREFERENCETOOLOBJECTBYVIDRESPONSE
DESCRIPTOR.message_types_by_name['GetReferenceToolObjectByVidRequest'] = _GETREFERENCETOOLOBJECTBYVIDREQUEST
DESCRIPTOR.message_types_by_name['GetReferenceToolObjectByVidResponse'] = _GETREFERENCETOOLOBJECTBYVIDRESPONSE
DESCRIPTOR.message_types_by_name['GetReferenceToolObjectByVidResponseWrapper'] = _GETREFERENCETOOLOBJECTBYVIDRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetReferenceToolObjectByVidRequest = _reflection.GeneratedProtocolMessageType('GetReferenceToolObjectByVidRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETREFERENCETOOLOBJECTBYVIDREQUEST,
  '__module__' : 'get_reference_tool_object_by_vId_pb2'
  # @@protoc_insertion_point(class_scope:basic.GetReferenceToolObjectByVidRequest)
  })
_sym_db.RegisterMessage(GetReferenceToolObjectByVidRequest)

GetReferenceToolObjectByVidResponse = _reflection.GeneratedProtocolMessageType('GetReferenceToolObjectByVidResponse', (_message.Message,), {

  'Data' : _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), {

    'Metadata' : _reflection.GeneratedProtocolMessageType('Metadata', (_message.Message,), {
      'DESCRIPTOR' : _GETREFERENCETOOLOBJECTBYVIDRESPONSE_DATA_METADATA,
      '__module__' : 'get_reference_tool_object_by_vId_pb2'
      # @@protoc_insertion_point(class_scope:basic.GetReferenceToolObjectByVidResponse.Data.Metadata)
      })
    ,
    'DESCRIPTOR' : _GETREFERENCETOOLOBJECTBYVIDRESPONSE_DATA,
    '__module__' : 'get_reference_tool_object_by_vId_pb2'
    # @@protoc_insertion_point(class_scope:basic.GetReferenceToolObjectByVidResponse.Data)
    })
  ,
  'DESCRIPTOR' : _GETREFERENCETOOLOBJECTBYVIDRESPONSE,
  '__module__' : 'get_reference_tool_object_by_vId_pb2'
  # @@protoc_insertion_point(class_scope:basic.GetReferenceToolObjectByVidResponse)
  })
_sym_db.RegisterMessage(GetReferenceToolObjectByVidResponse)
_sym_db.RegisterMessage(GetReferenceToolObjectByVidResponse.Data)
_sym_db.RegisterMessage(GetReferenceToolObjectByVidResponse.Data.Metadata)

GetReferenceToolObjectByVidResponseWrapper = _reflection.GeneratedProtocolMessageType('GetReferenceToolObjectByVidResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _GETREFERENCETOOLOBJECTBYVIDRESPONSEWRAPPER,
  '__module__' : 'get_reference_tool_object_by_vId_pb2'
  # @@protoc_insertion_point(class_scope:basic.GetReferenceToolObjectByVidResponseWrapper)
  })
_sym_db.RegisterMessage(GetReferenceToolObjectByVidResponseWrapper)


# @@protoc_insertion_point(module_scope)
