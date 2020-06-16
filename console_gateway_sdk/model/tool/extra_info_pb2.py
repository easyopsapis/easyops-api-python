# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: extra_info.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from console_gateway_sdk.model.tool import callback_pb2 as console__gateway__sdk_dot_model_dot_tool_dot_callback__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='extra_info.proto',
  package='tool',
  syntax='proto3',
  serialized_options=_b('Z>go.easyops.local/contracts/protorepo-models/easyops/model/tool'),
  serialized_pb=_b('\n\x10\x65xtra_info.proto\x12\x04tool\x1a-console_gateway_sdk/model/tool/callback.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xf2\x05\n\tExtraInfo\x12\x10\n\x08toolName\x18\x01 \x01(\t\x12\x10\n\x08\x65xecMode\x18\x02 \x01(\t\x12\x0f\n\x07outputs\x18\x03 \x03(\t\x12\x0e\n\x06origin\x18\x04 \x01(\t\x12\x0f\n\x07trigger\x18\x05 \x01(\t\x12&\n\x06\x64\x65tail\x18\x06 \x01(\x0b\x32\x16.tool.ExtraInfo.Detail\x12\x0e\n\x06toolId\x18\x07 \x01(\t\x12\x10\n\x08\x65xecUser\x18\x08 \x01(\t\x12\'\n\x06inputs\x18\t \x01(\x0b\x32\x17.google.protobuf.Struct\x1a\x9b\x04\n\x06\x44\x65tail\x12 \n\x08\x63\x61llback\x18\x01 \x01(\x0b\x32\x0e.tool.Callback\x12+\n\x0btoolOutputs\x18\x02 \x01(\x0b\x32\x16.google.protobuf.Value\x12(\n\x07toolEnv\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x35\n\noutputDefs\x18\x04 \x03(\x0b\x32!.tool.ExtraInfo.Detail.OutputDefs\x12\x33\n\ttableDefs\x18\x05 \x03(\x0b\x32 .tool.ExtraInfo.Detail.TableDefs\x12\x13\n\x0bsubscribers\x18\x06 \x03(\t\x1a&\n\nOutputDefs\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x1a\xee\x01\n\tTableDefs\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12?\n\ndimensions\x18\x03 \x03(\x0b\x32+.tool.ExtraInfo.Detail.TableDefs.Dimensions\x12\x39\n\x07\x63olumns\x18\x04 \x03(\x0b\x32(.tool.ExtraInfo.Detail.TableDefs.Columns\x1a&\n\nDimensions\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x1a#\n\x07\x43olumns\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\tB@Z>go.easyops.local/contracts/protorepo-models/easyops/model/toolb\x06proto3')
  ,
  dependencies=[console__gateway__sdk_dot_model_dot_tool_dot_callback__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_EXTRAINFO_DETAIL_OUTPUTDEFS = _descriptor.Descriptor(
  name='OutputDefs',
  full_name='tool.ExtraInfo.Detail.OutputDefs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tool.ExtraInfo.Detail.OutputDefs.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='tool.ExtraInfo.Detail.OutputDefs.name', index=1,
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
  serialized_start=579,
  serialized_end=617,
)

_EXTRAINFO_DETAIL_TABLEDEFS_DIMENSIONS = _descriptor.Descriptor(
  name='Dimensions',
  full_name='tool.ExtraInfo.Detail.TableDefs.Dimensions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tool.ExtraInfo.Detail.TableDefs.Dimensions.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='tool.ExtraInfo.Detail.TableDefs.Dimensions.name', index=1,
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
  serialized_start=783,
  serialized_end=821,
)

_EXTRAINFO_DETAIL_TABLEDEFS_COLUMNS = _descriptor.Descriptor(
  name='Columns',
  full_name='tool.ExtraInfo.Detail.TableDefs.Columns',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tool.ExtraInfo.Detail.TableDefs.Columns.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='tool.ExtraInfo.Detail.TableDefs.Columns.name', index=1,
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
  serialized_start=823,
  serialized_end=858,
)

_EXTRAINFO_DETAIL_TABLEDEFS = _descriptor.Descriptor(
  name='TableDefs',
  full_name='tool.ExtraInfo.Detail.TableDefs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tool.ExtraInfo.Detail.TableDefs.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='tool.ExtraInfo.Detail.TableDefs.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dimensions', full_name='tool.ExtraInfo.Detail.TableDefs.dimensions', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='columns', full_name='tool.ExtraInfo.Detail.TableDefs.columns', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_EXTRAINFO_DETAIL_TABLEDEFS_DIMENSIONS, _EXTRAINFO_DETAIL_TABLEDEFS_COLUMNS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=620,
  serialized_end=858,
)

_EXTRAINFO_DETAIL = _descriptor.Descriptor(
  name='Detail',
  full_name='tool.ExtraInfo.Detail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='callback', full_name='tool.ExtraInfo.Detail.callback', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='toolOutputs', full_name='tool.ExtraInfo.Detail.toolOutputs', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='toolEnv', full_name='tool.ExtraInfo.Detail.toolEnv', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outputDefs', full_name='tool.ExtraInfo.Detail.outputDefs', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tableDefs', full_name='tool.ExtraInfo.Detail.tableDefs', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subscribers', full_name='tool.ExtraInfo.Detail.subscribers', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_EXTRAINFO_DETAIL_OUTPUTDEFS, _EXTRAINFO_DETAIL_TABLEDEFS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=319,
  serialized_end=858,
)

_EXTRAINFO = _descriptor.Descriptor(
  name='ExtraInfo',
  full_name='tool.ExtraInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='toolName', full_name='tool.ExtraInfo.toolName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='execMode', full_name='tool.ExtraInfo.execMode', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='tool.ExtraInfo.outputs', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='origin', full_name='tool.ExtraInfo.origin', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trigger', full_name='tool.ExtraInfo.trigger', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='detail', full_name='tool.ExtraInfo.detail', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='toolId', full_name='tool.ExtraInfo.toolId', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='execUser', full_name='tool.ExtraInfo.execUser', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inputs', full_name='tool.ExtraInfo.inputs', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_EXTRAINFO_DETAIL, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=104,
  serialized_end=858,
)

_EXTRAINFO_DETAIL_OUTPUTDEFS.containing_type = _EXTRAINFO_DETAIL
_EXTRAINFO_DETAIL_TABLEDEFS_DIMENSIONS.containing_type = _EXTRAINFO_DETAIL_TABLEDEFS
_EXTRAINFO_DETAIL_TABLEDEFS_COLUMNS.containing_type = _EXTRAINFO_DETAIL_TABLEDEFS
_EXTRAINFO_DETAIL_TABLEDEFS.fields_by_name['dimensions'].message_type = _EXTRAINFO_DETAIL_TABLEDEFS_DIMENSIONS
_EXTRAINFO_DETAIL_TABLEDEFS.fields_by_name['columns'].message_type = _EXTRAINFO_DETAIL_TABLEDEFS_COLUMNS
_EXTRAINFO_DETAIL_TABLEDEFS.containing_type = _EXTRAINFO_DETAIL
_EXTRAINFO_DETAIL.fields_by_name['callback'].message_type = console__gateway__sdk_dot_model_dot_tool_dot_callback__pb2._CALLBACK
_EXTRAINFO_DETAIL.fields_by_name['toolOutputs'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_EXTRAINFO_DETAIL.fields_by_name['toolEnv'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_EXTRAINFO_DETAIL.fields_by_name['outputDefs'].message_type = _EXTRAINFO_DETAIL_OUTPUTDEFS
_EXTRAINFO_DETAIL.fields_by_name['tableDefs'].message_type = _EXTRAINFO_DETAIL_TABLEDEFS
_EXTRAINFO_DETAIL.containing_type = _EXTRAINFO
_EXTRAINFO.fields_by_name['detail'].message_type = _EXTRAINFO_DETAIL
_EXTRAINFO.fields_by_name['inputs'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['ExtraInfo'] = _EXTRAINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExtraInfo = _reflection.GeneratedProtocolMessageType('ExtraInfo', (_message.Message,), {

  'Detail' : _reflection.GeneratedProtocolMessageType('Detail', (_message.Message,), {

    'OutputDefs' : _reflection.GeneratedProtocolMessageType('OutputDefs', (_message.Message,), {
      'DESCRIPTOR' : _EXTRAINFO_DETAIL_OUTPUTDEFS,
      '__module__' : 'extra_info_pb2'
      # @@protoc_insertion_point(class_scope:tool.ExtraInfo.Detail.OutputDefs)
      })
    ,

    'TableDefs' : _reflection.GeneratedProtocolMessageType('TableDefs', (_message.Message,), {

      'Dimensions' : _reflection.GeneratedProtocolMessageType('Dimensions', (_message.Message,), {
        'DESCRIPTOR' : _EXTRAINFO_DETAIL_TABLEDEFS_DIMENSIONS,
        '__module__' : 'extra_info_pb2'
        # @@protoc_insertion_point(class_scope:tool.ExtraInfo.Detail.TableDefs.Dimensions)
        })
      ,

      'Columns' : _reflection.GeneratedProtocolMessageType('Columns', (_message.Message,), {
        'DESCRIPTOR' : _EXTRAINFO_DETAIL_TABLEDEFS_COLUMNS,
        '__module__' : 'extra_info_pb2'
        # @@protoc_insertion_point(class_scope:tool.ExtraInfo.Detail.TableDefs.Columns)
        })
      ,
      'DESCRIPTOR' : _EXTRAINFO_DETAIL_TABLEDEFS,
      '__module__' : 'extra_info_pb2'
      # @@protoc_insertion_point(class_scope:tool.ExtraInfo.Detail.TableDefs)
      })
    ,
    'DESCRIPTOR' : _EXTRAINFO_DETAIL,
    '__module__' : 'extra_info_pb2'
    # @@protoc_insertion_point(class_scope:tool.ExtraInfo.Detail)
    })
  ,
  'DESCRIPTOR' : _EXTRAINFO,
  '__module__' : 'extra_info_pb2'
  # @@protoc_insertion_point(class_scope:tool.ExtraInfo)
  })
_sym_db.RegisterMessage(ExtraInfo)
_sym_db.RegisterMessage(ExtraInfo.Detail)
_sym_db.RegisterMessage(ExtraInfo.Detail.OutputDefs)
_sym_db.RegisterMessage(ExtraInfo.Detail.TableDefs)
_sym_db.RegisterMessage(ExtraInfo.Detail.TableDefs.Dimensions)
_sym_db.RegisterMessage(ExtraInfo.Detail.TableDefs.Columns)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
