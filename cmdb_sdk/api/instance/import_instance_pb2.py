# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: import_instance.proto

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
  name='import_instance.proto',
  package='instance',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x15import_instance.proto\x12\x08instance\x1a\x1cgoogle/protobuf/struct.proto\"_\n\x15ImportInstanceRequest\x12\x10\n\x08objectId\x18\x01 \x01(\t\x12\x0c\n\x04keys\x18\x02 \x03(\t\x12&\n\x05\x64\x61tas\x18\x03 \x03(\x0b\x32\x17.google.protobuf.Struct\"\xdb\x01\n\x16ImportInstanceResponse\x12\x14\n\x0cinsert_count\x18\x01 \x01(\x05\x12\x14\n\x0cupdate_count\x18\x02 \x01(\x05\x12\x14\n\x0c\x66\x61iled_count\x18\x03 \x01(\x05\x12\x33\n\x04\x64\x61ta\x18\x04 \x03(\x0b\x32%.instance.ImportInstanceResponse.Data\x1aJ\n\x04\x44\x61ta\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\r\n\x05\x65rror\x18\x02 \x01(\t\x12%\n\x04\x64\x61ta\x18\x03 \x03(\x0b\x32\x17.google.protobuf.Struct\"\x81\x01\n\x1dImportInstanceResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12.\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32 .instance.ImportInstanceResponseb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_IMPORTINSTANCEREQUEST = _descriptor.Descriptor(
  name='ImportInstanceRequest',
  full_name='instance.ImportInstanceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='objectId', full_name='instance.ImportInstanceRequest.objectId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keys', full_name='instance.ImportInstanceRequest.keys', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='datas', full_name='instance.ImportInstanceRequest.datas', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=65,
  serialized_end=160,
)


_IMPORTINSTANCERESPONSE_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='instance.ImportInstanceResponse.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='instance.ImportInstanceResponse.Data.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='instance.ImportInstanceResponse.Data.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='instance.ImportInstanceResponse.Data.data', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=308,
  serialized_end=382,
)

_IMPORTINSTANCERESPONSE = _descriptor.Descriptor(
  name='ImportInstanceResponse',
  full_name='instance.ImportInstanceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='insert_count', full_name='instance.ImportInstanceResponse.insert_count', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_count', full_name='instance.ImportInstanceResponse.update_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='failed_count', full_name='instance.ImportInstanceResponse.failed_count', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='instance.ImportInstanceResponse.data', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_IMPORTINSTANCERESPONSE_DATA, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=163,
  serialized_end=382,
)


_IMPORTINSTANCERESPONSEWRAPPER = _descriptor.Descriptor(
  name='ImportInstanceResponseWrapper',
  full_name='instance.ImportInstanceResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='instance.ImportInstanceResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='instance.ImportInstanceResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='instance.ImportInstanceResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='instance.ImportInstanceResponseWrapper.data', index=3,
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
  serialized_start=385,
  serialized_end=514,
)

_IMPORTINSTANCEREQUEST.fields_by_name['datas'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_IMPORTINSTANCERESPONSE_DATA.fields_by_name['data'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_IMPORTINSTANCERESPONSE_DATA.containing_type = _IMPORTINSTANCERESPONSE
_IMPORTINSTANCERESPONSE.fields_by_name['data'].message_type = _IMPORTINSTANCERESPONSE_DATA
_IMPORTINSTANCERESPONSEWRAPPER.fields_by_name['data'].message_type = _IMPORTINSTANCERESPONSE
DESCRIPTOR.message_types_by_name['ImportInstanceRequest'] = _IMPORTINSTANCEREQUEST
DESCRIPTOR.message_types_by_name['ImportInstanceResponse'] = _IMPORTINSTANCERESPONSE
DESCRIPTOR.message_types_by_name['ImportInstanceResponseWrapper'] = _IMPORTINSTANCERESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImportInstanceRequest = _reflection.GeneratedProtocolMessageType('ImportInstanceRequest', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTINSTANCEREQUEST,
  '__module__' : 'import_instance_pb2'
  # @@protoc_insertion_point(class_scope:instance.ImportInstanceRequest)
  })
_sym_db.RegisterMessage(ImportInstanceRequest)

ImportInstanceResponse = _reflection.GeneratedProtocolMessageType('ImportInstanceResponse', (_message.Message,), {

  'Data' : _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), {
    'DESCRIPTOR' : _IMPORTINSTANCERESPONSE_DATA,
    '__module__' : 'import_instance_pb2'
    # @@protoc_insertion_point(class_scope:instance.ImportInstanceResponse.Data)
    })
  ,
  'DESCRIPTOR' : _IMPORTINSTANCERESPONSE,
  '__module__' : 'import_instance_pb2'
  # @@protoc_insertion_point(class_scope:instance.ImportInstanceResponse)
  })
_sym_db.RegisterMessage(ImportInstanceResponse)
_sym_db.RegisterMessage(ImportInstanceResponse.Data)

ImportInstanceResponseWrapper = _reflection.GeneratedProtocolMessageType('ImportInstanceResponseWrapper', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTINSTANCERESPONSEWRAPPER,
  '__module__' : 'import_instance_pb2'
  # @@protoc_insertion_point(class_scope:instance.ImportInstanceResponseWrapper)
  })
_sym_db.RegisterMessage(ImportInstanceResponseWrapper)


# @@protoc_insertion_point(module_scope)
