# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tool_task.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from architecture_view_sdk.model.tool import callback_pb2 as architecture__view__sdk_dot_model_dot_tool_dot_callback__pb2
from architecture_view_sdk.model.tool import tool_pb2 as architecture__view__sdk_dot_model_dot_tool_dot_tool__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tool_task.proto',
  package='tool',
  syntax='proto3',
  serialized_options=_b('Z>go.easyops.local/contracts/protorepo-models/easyops/model/tool'),
  serialized_pb=_b('\n\x0ftool_task.proto\x12\x04tool\x1a/architecture_view_sdk/model/tool/callback.proto\x1a+architecture_view_sdk/model/tool/tool.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xd8\x0e\n\x08ToolTask\x12\x10\n\x08username\x18\x01 \x01(\t\x12\'\n\x06inputs\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12/\n\x0b\x65xtraDetail\x18\x03 \x01(\x0b\x32\x1a.tool.ToolTask.ExtraDetail\x12\x13\n\x0btotalStatus\x18\x04 \x01(\t\x12\r\n\x05\x65rror\x18\x05 \x01(\t\x12\x0e\n\x06\x65xecId\x18\x06 \x01(\t\x12(\n\x07toolEnv\x18\x07 \x01(\x0b\x32\x17.google.protobuf.Struct\x12(\n\x07outputs\x18\x08 \x01(\x0b\x32\x17.google.protobuf.Struct\x12,\n\x0boutViewData\x18\t \x01(\x0b\x32\x17.google.protobuf.Struct\x12*\n\tagentData\x18\n \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0e\n\x06\x61gents\x18\x0b \x03(\t\x12*\n\tstartTime\x18\x0c \x01(\x0b\x32\x17.google.protobuf.Struct\x12\'\n\x06status\x18\r \x01(\x0b\x32\x17.google.protobuf.Struct\x12$\n\x03msg\x18\x0e \x01(\x0b\x32\x17.google.protobuf.Struct\x12(\n\x07\x65ndTime\x18\x0f \x01(\x0b\x32\x17.google.protobuf.Struct\x12+\n\nexitStatus\x18\x10 \x01(\x0b\x32\x17.google.protobuf.Struct\x12*\n\tsysStatus\x18\x11 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x30\n\x0ftoolOutputsData\x18\x12 \x03(\x0b\x32\x17.google.protobuf.Struct\x12*\n\ttableData\x18\x13 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x1c\n\x08toolData\x18\x14 \x01(\x0b\x32\n.tool.Tool\x12\x33\n\rbatchStrategy\x18\x15 \x01(\x0b\x32\x1c.tool.ToolTask.BatchStrategy\x12\x12\n\nneedNotify\x18\x16 \x01(\t\x12\x10\n\x08\x65xecUser\x18\x17 \x01(\t\x12\x0b\n\x03vId\x18\x18 \x01(\t\x12\x0e\n\x06toolId\x18\x19 \x01(\t\x12-\n\noutputDefs\x18\x1a \x03(\x0b\x32\x19.tool.ToolTask.OutputDefs\x12+\n\ttableDefs\x18\x1b \x03(\x0b\x32\x18.tool.ToolTask.TableDefs\x12+\n\x0btoolOutputs\x18\x1c \x01(\x0b\x32\x16.google.protobuf.Value\x1a\x9b\x04\n\x0b\x45xtraDetail\x12 \n\x08\x63\x61llback\x18\x01 \x01(\x0b\x32\x0e.tool.Callback\x12(\n\x07toolEnv\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12+\n\x0btoolOutputs\x18\x03 \x01(\x0b\x32\x16.google.protobuf.Value\x12\x37\n\ttableDefs\x18\x04 \x03(\x0b\x32$.tool.ToolTask.ExtraDetail.TableDefs\x12\x39\n\noutputDefs\x18\x05 \x03(\x0b\x32%.tool.ToolTask.ExtraDetail.OutputDefs\x1a\xf6\x01\n\tTableDefs\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x43\n\ndimensions\x18\x03 \x03(\x0b\x32/.tool.ToolTask.ExtraDetail.TableDefs.Dimensions\x12=\n\x07\x63olumns\x18\x04 \x03(\x0b\x32,.tool.ToolTask.ExtraDetail.TableDefs.Columns\x1a&\n\nDimensions\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x1a#\n\x07\x43olumns\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x1a&\n\nOutputDefs\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x1aL\n\rBatchStrategy\x12\x10\n\x08\x62\x61tchNum\x18\x01 \x01(\x05\x12\x15\n\rbatchInterval\x18\x02 \x01(\x05\x12\x12\n\nfailedStop\x18\x03 \x01(\x08\x1a&\n\nOutputDefs\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x1a\xde\x01\n\tTableDefs\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x37\n\ndimensions\x18\x03 \x03(\x0b\x32#.tool.ToolTask.TableDefs.Dimensions\x12\x31\n\x07\x63olumns\x18\x04 \x03(\x0b\x32 .tool.ToolTask.TableDefs.Columns\x1a&\n\nDimensions\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x1a#\n\x07\x43olumns\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\tB@Z>go.easyops.local/contracts/protorepo-models/easyops/model/toolb\x06proto3')
  ,
  dependencies=[architecture__view__sdk_dot_model_dot_tool_dot_callback__pb2.DESCRIPTOR,architecture__view__sdk_dot_model_dot_tool_dot_tool__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_TOOLTASK_EXTRADETAIL_TABLEDEFS_DIMENSIONS = _descriptor.Descriptor(
  name='Dimensions',
  full_name='tool.ToolTask.ExtraDetail.TableDefs.Dimensions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tool.ToolTask.ExtraDetail.TableDefs.Dimensions.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='tool.ToolTask.ExtraDetail.TableDefs.Dimensions.name', index=1,
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
  serialized_start=1572,
  serialized_end=1610,
)

_TOOLTASK_EXTRADETAIL_TABLEDEFS_COLUMNS = _descriptor.Descriptor(
  name='Columns',
  full_name='tool.ToolTask.ExtraDetail.TableDefs.Columns',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tool.ToolTask.ExtraDetail.TableDefs.Columns.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='tool.ToolTask.ExtraDetail.TableDefs.Columns.name', index=1,
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
  serialized_start=1612,
  serialized_end=1647,
)

_TOOLTASK_EXTRADETAIL_TABLEDEFS = _descriptor.Descriptor(
  name='TableDefs',
  full_name='tool.ToolTask.ExtraDetail.TableDefs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tool.ToolTask.ExtraDetail.TableDefs.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='tool.ToolTask.ExtraDetail.TableDefs.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dimensions', full_name='tool.ToolTask.ExtraDetail.TableDefs.dimensions', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='columns', full_name='tool.ToolTask.ExtraDetail.TableDefs.columns', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TOOLTASK_EXTRADETAIL_TABLEDEFS_DIMENSIONS, _TOOLTASK_EXTRADETAIL_TABLEDEFS_COLUMNS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1401,
  serialized_end=1647,
)

_TOOLTASK_EXTRADETAIL_OUTPUTDEFS = _descriptor.Descriptor(
  name='OutputDefs',
  full_name='tool.ToolTask.ExtraDetail.OutputDefs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tool.ToolTask.ExtraDetail.OutputDefs.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='tool.ToolTask.ExtraDetail.OutputDefs.name', index=1,
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
  serialized_start=1649,
  serialized_end=1687,
)

_TOOLTASK_EXTRADETAIL = _descriptor.Descriptor(
  name='ExtraDetail',
  full_name='tool.ToolTask.ExtraDetail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='callback', full_name='tool.ToolTask.ExtraDetail.callback', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='toolEnv', full_name='tool.ToolTask.ExtraDetail.toolEnv', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='toolOutputs', full_name='tool.ToolTask.ExtraDetail.toolOutputs', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tableDefs', full_name='tool.ToolTask.ExtraDetail.tableDefs', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outputDefs', full_name='tool.ToolTask.ExtraDetail.outputDefs', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TOOLTASK_EXTRADETAIL_TABLEDEFS, _TOOLTASK_EXTRADETAIL_OUTPUTDEFS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1148,
  serialized_end=1687,
)

_TOOLTASK_BATCHSTRATEGY = _descriptor.Descriptor(
  name='BatchStrategy',
  full_name='tool.ToolTask.BatchStrategy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='batchNum', full_name='tool.ToolTask.BatchStrategy.batchNum', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batchInterval', full_name='tool.ToolTask.BatchStrategy.batchInterval', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='failedStop', full_name='tool.ToolTask.BatchStrategy.failedStop', index=2,
      number=3, type=8, cpp_type=7, label=1,
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
  serialized_start=1689,
  serialized_end=1765,
)

_TOOLTASK_OUTPUTDEFS = _descriptor.Descriptor(
  name='OutputDefs',
  full_name='tool.ToolTask.OutputDefs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tool.ToolTask.OutputDefs.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='tool.ToolTask.OutputDefs.name', index=1,
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
  serialized_start=1649,
  serialized_end=1687,
)

_TOOLTASK_TABLEDEFS_DIMENSIONS = _descriptor.Descriptor(
  name='Dimensions',
  full_name='tool.ToolTask.TableDefs.Dimensions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tool.ToolTask.TableDefs.Dimensions.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='tool.ToolTask.TableDefs.Dimensions.name', index=1,
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
  serialized_start=1572,
  serialized_end=1610,
)

_TOOLTASK_TABLEDEFS_COLUMNS = _descriptor.Descriptor(
  name='Columns',
  full_name='tool.ToolTask.TableDefs.Columns',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tool.ToolTask.TableDefs.Columns.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='tool.ToolTask.TableDefs.Columns.name', index=1,
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
  serialized_start=1612,
  serialized_end=1647,
)

_TOOLTASK_TABLEDEFS = _descriptor.Descriptor(
  name='TableDefs',
  full_name='tool.ToolTask.TableDefs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tool.ToolTask.TableDefs.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='tool.ToolTask.TableDefs.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dimensions', full_name='tool.ToolTask.TableDefs.dimensions', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='columns', full_name='tool.ToolTask.TableDefs.columns', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TOOLTASK_TABLEDEFS_DIMENSIONS, _TOOLTASK_TABLEDEFS_COLUMNS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1808,
  serialized_end=2030,
)

_TOOLTASK = _descriptor.Descriptor(
  name='ToolTask',
  full_name='tool.ToolTask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='tool.ToolTask.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inputs', full_name='tool.ToolTask.inputs', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extraDetail', full_name='tool.ToolTask.extraDetail', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='totalStatus', full_name='tool.ToolTask.totalStatus', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='tool.ToolTask.error', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='execId', full_name='tool.ToolTask.execId', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='toolEnv', full_name='tool.ToolTask.toolEnv', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='tool.ToolTask.outputs', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outViewData', full_name='tool.ToolTask.outViewData', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agentData', full_name='tool.ToolTask.agentData', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agents', full_name='tool.ToolTask.agents', index=10,
      number=11, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='tool.ToolTask.startTime', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='tool.ToolTask.status', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='tool.ToolTask.msg', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endTime', full_name='tool.ToolTask.endTime', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exitStatus', full_name='tool.ToolTask.exitStatus', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sysStatus', full_name='tool.ToolTask.sysStatus', index=16,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='toolOutputsData', full_name='tool.ToolTask.toolOutputsData', index=17,
      number=18, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tableData', full_name='tool.ToolTask.tableData', index=18,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='toolData', full_name='tool.ToolTask.toolData', index=19,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batchStrategy', full_name='tool.ToolTask.batchStrategy', index=20,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='needNotify', full_name='tool.ToolTask.needNotify', index=21,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='execUser', full_name='tool.ToolTask.execUser', index=22,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vId', full_name='tool.ToolTask.vId', index=23,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='toolId', full_name='tool.ToolTask.toolId', index=24,
      number=25, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outputDefs', full_name='tool.ToolTask.outputDefs', index=25,
      number=26, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tableDefs', full_name='tool.ToolTask.tableDefs', index=26,
      number=27, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='toolOutputs', full_name='tool.ToolTask.toolOutputs', index=27,
      number=28, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TOOLTASK_EXTRADETAIL, _TOOLTASK_BATCHSTRATEGY, _TOOLTASK_OUTPUTDEFS, _TOOLTASK_TABLEDEFS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=150,
  serialized_end=2030,
)

_TOOLTASK_EXTRADETAIL_TABLEDEFS_DIMENSIONS.containing_type = _TOOLTASK_EXTRADETAIL_TABLEDEFS
_TOOLTASK_EXTRADETAIL_TABLEDEFS_COLUMNS.containing_type = _TOOLTASK_EXTRADETAIL_TABLEDEFS
_TOOLTASK_EXTRADETAIL_TABLEDEFS.fields_by_name['dimensions'].message_type = _TOOLTASK_EXTRADETAIL_TABLEDEFS_DIMENSIONS
_TOOLTASK_EXTRADETAIL_TABLEDEFS.fields_by_name['columns'].message_type = _TOOLTASK_EXTRADETAIL_TABLEDEFS_COLUMNS
_TOOLTASK_EXTRADETAIL_TABLEDEFS.containing_type = _TOOLTASK_EXTRADETAIL
_TOOLTASK_EXTRADETAIL_OUTPUTDEFS.containing_type = _TOOLTASK_EXTRADETAIL
_TOOLTASK_EXTRADETAIL.fields_by_name['callback'].message_type = architecture__view__sdk_dot_model_dot_tool_dot_callback__pb2._CALLBACK
_TOOLTASK_EXTRADETAIL.fields_by_name['toolEnv'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_TOOLTASK_EXTRADETAIL.fields_by_name['toolOutputs'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_TOOLTASK_EXTRADETAIL.fields_by_name['tableDefs'].message_type = _TOOLTASK_EXTRADETAIL_TABLEDEFS
_TOOLTASK_EXTRADETAIL.fields_by_name['outputDefs'].message_type = _TOOLTASK_EXTRADETAIL_OUTPUTDEFS
_TOOLTASK_EXTRADETAIL.containing_type = _TOOLTASK
_TOOLTASK_BATCHSTRATEGY.containing_type = _TOOLTASK
_TOOLTASK_OUTPUTDEFS.containing_type = _TOOLTASK
_TOOLTASK_TABLEDEFS_DIMENSIONS.containing_type = _TOOLTASK_TABLEDEFS
_TOOLTASK_TABLEDEFS_COLUMNS.containing_type = _TOOLTASK_TABLEDEFS
_TOOLTASK_TABLEDEFS.fields_by_name['dimensions'].message_type = _TOOLTASK_TABLEDEFS_DIMENSIONS
_TOOLTASK_TABLEDEFS.fields_by_name['columns'].message_type = _TOOLTASK_TABLEDEFS_COLUMNS
_TOOLTASK_TABLEDEFS.containing_type = _TOOLTASK
_TOOLTASK.fields_by_name['inputs'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_TOOLTASK.fields_by_name['extraDetail'].message_type = _TOOLTASK_EXTRADETAIL
_TOOLTASK.fields_by_name['toolEnv'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_TOOLTASK.fields_by_name['outputs'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_TOOLTASK.fields_by_name['outViewData'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_TOOLTASK.fields_by_name['agentData'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_TOOLTASK.fields_by_name['startTime'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_TOOLTASK.fields_by_name['status'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_TOOLTASK.fields_by_name['msg'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_TOOLTASK.fields_by_name['endTime'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_TOOLTASK.fields_by_name['exitStatus'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_TOOLTASK.fields_by_name['sysStatus'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_TOOLTASK.fields_by_name['toolOutputsData'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_TOOLTASK.fields_by_name['tableData'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_TOOLTASK.fields_by_name['toolData'].message_type = architecture__view__sdk_dot_model_dot_tool_dot_tool__pb2._TOOL
_TOOLTASK.fields_by_name['batchStrategy'].message_type = _TOOLTASK_BATCHSTRATEGY
_TOOLTASK.fields_by_name['outputDefs'].message_type = _TOOLTASK_OUTPUTDEFS
_TOOLTASK.fields_by_name['tableDefs'].message_type = _TOOLTASK_TABLEDEFS
_TOOLTASK.fields_by_name['toolOutputs'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
DESCRIPTOR.message_types_by_name['ToolTask'] = _TOOLTASK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ToolTask = _reflection.GeneratedProtocolMessageType('ToolTask', (_message.Message,), {

  'ExtraDetail' : _reflection.GeneratedProtocolMessageType('ExtraDetail', (_message.Message,), {

    'TableDefs' : _reflection.GeneratedProtocolMessageType('TableDefs', (_message.Message,), {

      'Dimensions' : _reflection.GeneratedProtocolMessageType('Dimensions', (_message.Message,), {
        'DESCRIPTOR' : _TOOLTASK_EXTRADETAIL_TABLEDEFS_DIMENSIONS,
        '__module__' : 'tool_task_pb2'
        # @@protoc_insertion_point(class_scope:tool.ToolTask.ExtraDetail.TableDefs.Dimensions)
        })
      ,

      'Columns' : _reflection.GeneratedProtocolMessageType('Columns', (_message.Message,), {
        'DESCRIPTOR' : _TOOLTASK_EXTRADETAIL_TABLEDEFS_COLUMNS,
        '__module__' : 'tool_task_pb2'
        # @@protoc_insertion_point(class_scope:tool.ToolTask.ExtraDetail.TableDefs.Columns)
        })
      ,
      'DESCRIPTOR' : _TOOLTASK_EXTRADETAIL_TABLEDEFS,
      '__module__' : 'tool_task_pb2'
      # @@protoc_insertion_point(class_scope:tool.ToolTask.ExtraDetail.TableDefs)
      })
    ,

    'OutputDefs' : _reflection.GeneratedProtocolMessageType('OutputDefs', (_message.Message,), {
      'DESCRIPTOR' : _TOOLTASK_EXTRADETAIL_OUTPUTDEFS,
      '__module__' : 'tool_task_pb2'
      # @@protoc_insertion_point(class_scope:tool.ToolTask.ExtraDetail.OutputDefs)
      })
    ,
    'DESCRIPTOR' : _TOOLTASK_EXTRADETAIL,
    '__module__' : 'tool_task_pb2'
    # @@protoc_insertion_point(class_scope:tool.ToolTask.ExtraDetail)
    })
  ,

  'BatchStrategy' : _reflection.GeneratedProtocolMessageType('BatchStrategy', (_message.Message,), {
    'DESCRIPTOR' : _TOOLTASK_BATCHSTRATEGY,
    '__module__' : 'tool_task_pb2'
    # @@protoc_insertion_point(class_scope:tool.ToolTask.BatchStrategy)
    })
  ,

  'OutputDefs' : _reflection.GeneratedProtocolMessageType('OutputDefs', (_message.Message,), {
    'DESCRIPTOR' : _TOOLTASK_OUTPUTDEFS,
    '__module__' : 'tool_task_pb2'
    # @@protoc_insertion_point(class_scope:tool.ToolTask.OutputDefs)
    })
  ,

  'TableDefs' : _reflection.GeneratedProtocolMessageType('TableDefs', (_message.Message,), {

    'Dimensions' : _reflection.GeneratedProtocolMessageType('Dimensions', (_message.Message,), {
      'DESCRIPTOR' : _TOOLTASK_TABLEDEFS_DIMENSIONS,
      '__module__' : 'tool_task_pb2'
      # @@protoc_insertion_point(class_scope:tool.ToolTask.TableDefs.Dimensions)
      })
    ,

    'Columns' : _reflection.GeneratedProtocolMessageType('Columns', (_message.Message,), {
      'DESCRIPTOR' : _TOOLTASK_TABLEDEFS_COLUMNS,
      '__module__' : 'tool_task_pb2'
      # @@protoc_insertion_point(class_scope:tool.ToolTask.TableDefs.Columns)
      })
    ,
    'DESCRIPTOR' : _TOOLTASK_TABLEDEFS,
    '__module__' : 'tool_task_pb2'
    # @@protoc_insertion_point(class_scope:tool.ToolTask.TableDefs)
    })
  ,
  'DESCRIPTOR' : _TOOLTASK,
  '__module__' : 'tool_task_pb2'
  # @@protoc_insertion_point(class_scope:tool.ToolTask)
  })
_sym_db.RegisterMessage(ToolTask)
_sym_db.RegisterMessage(ToolTask.ExtraDetail)
_sym_db.RegisterMessage(ToolTask.ExtraDetail.TableDefs)
_sym_db.RegisterMessage(ToolTask.ExtraDetail.TableDefs.Dimensions)
_sym_db.RegisterMessage(ToolTask.ExtraDetail.TableDefs.Columns)
_sym_db.RegisterMessage(ToolTask.ExtraDetail.OutputDefs)
_sym_db.RegisterMessage(ToolTask.BatchStrategy)
_sym_db.RegisterMessage(ToolTask.OutputDefs)
_sym_db.RegisterMessage(ToolTask.TableDefs)
_sym_db.RegisterMessage(ToolTask.TableDefs.Dimensions)
_sym_db.RegisterMessage(ToolTask.TableDefs.Columns)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
