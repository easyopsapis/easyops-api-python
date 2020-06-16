# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tool.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from easy_command_sdk.model.tool import tool_input_pb2 as easy__command__sdk_dot_model_dot_tool_dot_tool__input__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tool.proto',
  package='tool',
  syntax='proto3',
  serialized_options=_b('Z>go.easyops.local/contracts/protorepo-models/easyops/model/tool'),
  serialized_pb=_b('\n\ntool.proto\x12\x04tool\x1a,easy_command_sdk/model/tool/tool_input.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xf2\x0c\n\x04Tool\x12\x0e\n\x06toolId\x18\x01 \x01(\t\x12\x0b\n\x03vId\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07timeout\x18\x04 \x01(\x05\x12\x10\n\x08\x63\x61tegory\x18\x05 \x01(\t\x12\x0c\n\x04icon\x18\x06 \x01(\t\x12\r\n\x05style\x18\x07 \x01(\t\x12\x0c\n\x04memo\x18\x08 \x01(\t\x12\x13\n\x0blistVisible\x18\t \x01(\x08\x12\x0c\n\x04tags\x18\n \x03(\t\x12\x0f\n\x07\x64isable\x18\x0b \x01(\x08\x12\x12\n\ncreateTime\x18\x0c \x01(\t\x12\x12\n\nupdateTime\x18\r \x01(\t\x12\x0f\n\x07\x63reator\x18\x0e \x01(\t\x12\x0b\n\x03org\x18\x0f \x01(\x05\x12\x1f\n\x06inputs\x18\x10 \x03(\x0b\x32\x0f.tool.ToolInput\x12\x0f\n\x07outputs\x18\x11 \x01(\t\x12\x0c\n\x04type\x18\x12 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x13 \x01(\t\x12\x17\n\x0f\x64\x65\x66\x61ultExecUser\x18\x14 \x01(\t\x12\x10\n\x08\x65xecUser\x18\x15 \x01(\t\x12\x11\n\tauthUsers\x18\x16 \x03(\t\x12\x15\n\rdefaultAgents\x18\x17 \x03(\t\x12\x15\n\rsystem_plugin\x18\x18 \x01(\x08\x12\x13\n\x0bsystem_tool\x18\x19 \x01(\x08\x12\x12\n\nlockAgents\x18\x1a \x01(\t\x12\x12\n\nsandboxRun\x18\x1b \x01(\x08\x12\x11\n\twhiteList\x18\x1c \x03(\t\x12\x16\n\x0ewindowsSession\x18\x1d \x01(\x08\x12\x11\n\tblackList\x18\x1e \x03(\t\x12+\n\x0btoolOutputs\x18\x1f \x01(\x0b\x32\x16.google.protobuf.Value\x12)\n\noutputDefs\x18  \x03(\x0b\x32\x15.tool.Tool.OutputDefs\x12\'\n\ttableDefs\x18! \x03(\x0b\x32\x14.tool.Tool.TableDefs\x12\x13\n\x0bvCreateTime\x18\" \x01(\t\x12\x13\n\x0bvUpdateTime\x18# \x01(\t\x12\r\n\x05vName\x18$ \x01(\t\x12\x10\n\x08vCreator\x18% \x01(\t\x12\x17\n\x0freadAuthorizers\x18& \x03(\t\x12\x19\n\x11updateAuthorizers\x18\' \x03(\t\x12\x19\n\x11\x64\x65leteAuthorizers\x18( \x03(\t\x12\x1a\n\x12\x65xecuteAuthorizers\x18) \x03(\t\x12&\n\x1ereadExecutionResultAuthorizers\x18* \x03(\t\x12\x1e\n\x16rootExecuteAuthorizers\x18+ \x03(\t\x12\r\n\x05vDesc\x18, \x01(\t\x12\x12\n\nsourceFrom\x18- \x01(\t\x12\x0f\n\x07\x65nvType\x18. \x01(\t\x12\x11\n\tcheckType\x18/ \x01(\t\x12\x11\n\tcheckUser\x18\x30 \x01(\t\x12\x14\n\x0c\x63heckSponsor\x18\x31 \x01(\t\x12\x14\n\x0c\x63heckComment\x18\x32 \x01(\t\x12-\n\rbatchStrategy\x18\x33 \x01(\x0b\x32\x16.google.protobuf.Value\x12\x14\n\x0c\x66unctionType\x18\x34 \x01(\t\x12\x15\n\ris_system_org\x18\x35 \x01(\x08\x12\x13\n\x0bsubscribers\x18\x36 \x03(\t\x12\x19\n\x11subscribedChannel\x18\x37 \x01(\t\x12\x10\n\x08readOnly\x18\x38 \x01(\x08\x12\x14\n\x0ctemplateType\x18\x39 \x01(\t\x12\x11\n\tdelete_me\x18: \x01(\x08\x12\x11\n\tapprovers\x18; \x03(\t\x12\x1b\n\x13\x61nsibleNodeExecUser\x18< \x01(\t\x12\x1b\n\x03log\x18= \x01(\x0b\x32\x0e.tool.Tool.Log\x1a&\n\nOutputDefs\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x1a\xd6\x01\n\tTableDefs\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x33\n\ndimensions\x18\x03 \x03(\x0b\x32\x1f.tool.Tool.TableDefs.Dimensions\x12-\n\x07\x63olumns\x18\x04 \x03(\x0b\x32\x1c.tool.Tool.TableDefs.Columns\x1a&\n\nDimensions\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x1a#\n\x07\x43olumns\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x1a%\n\x03Log\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\r\n\x05level\x18\x02 \x01(\tB@Z>go.easyops.local/contracts/protorepo-models/easyops/model/toolb\x06proto3')
  ,
  dependencies=[easy__command__sdk_dot_model_dot_tool_dot_tool__input__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_TOOL_OUTPUTDEFS = _descriptor.Descriptor(
  name='OutputDefs',
  full_name='tool.Tool.OutputDefs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tool.Tool.OutputDefs.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='tool.Tool.OutputDefs.name', index=1,
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
  serialized_start=1453,
  serialized_end=1491,
)

_TOOL_TABLEDEFS_DIMENSIONS = _descriptor.Descriptor(
  name='Dimensions',
  full_name='tool.Tool.TableDefs.Dimensions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tool.Tool.TableDefs.Dimensions.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='tool.Tool.TableDefs.Dimensions.name', index=1,
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
  serialized_start=1633,
  serialized_end=1671,
)

_TOOL_TABLEDEFS_COLUMNS = _descriptor.Descriptor(
  name='Columns',
  full_name='tool.Tool.TableDefs.Columns',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tool.Tool.TableDefs.Columns.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='tool.Tool.TableDefs.Columns.name', index=1,
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
  serialized_start=1673,
  serialized_end=1708,
)

_TOOL_TABLEDEFS = _descriptor.Descriptor(
  name='TableDefs',
  full_name='tool.Tool.TableDefs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tool.Tool.TableDefs.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='tool.Tool.TableDefs.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dimensions', full_name='tool.Tool.TableDefs.dimensions', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='columns', full_name='tool.Tool.TableDefs.columns', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TOOL_TABLEDEFS_DIMENSIONS, _TOOL_TABLEDEFS_COLUMNS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1494,
  serialized_end=1708,
)

_TOOL_LOG = _descriptor.Descriptor(
  name='Log',
  full_name='tool.Tool.Log',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enabled', full_name='tool.Tool.Log.enabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level', full_name='tool.Tool.Log.level', index=1,
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
  serialized_start=1710,
  serialized_end=1747,
)

_TOOL = _descriptor.Descriptor(
  name='Tool',
  full_name='tool.Tool',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='toolId', full_name='tool.Tool.toolId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vId', full_name='tool.Tool.vId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='tool.Tool.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='tool.Tool.timeout', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='tool.Tool.category', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon', full_name='tool.Tool.icon', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='style', full_name='tool.Tool.style', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='tool.Tool.memo', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='listVisible', full_name='tool.Tool.listVisible', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='tool.Tool.tags', index=9,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disable', full_name='tool.Tool.disable', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='createTime', full_name='tool.Tool.createTime', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updateTime', full_name='tool.Tool.updateTime', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='tool.Tool.creator', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org', full_name='tool.Tool.org', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inputs', full_name='tool.Tool.inputs', index=15,
      number=16, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='tool.Tool.outputs', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='tool.Tool.type', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='tool.Tool.content', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='defaultExecUser', full_name='tool.Tool.defaultExecUser', index=19,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='execUser', full_name='tool.Tool.execUser', index=20,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='authUsers', full_name='tool.Tool.authUsers', index=21,
      number=22, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='defaultAgents', full_name='tool.Tool.defaultAgents', index=22,
      number=23, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='system_plugin', full_name='tool.Tool.system_plugin', index=23,
      number=24, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='system_tool', full_name='tool.Tool.system_tool', index=24,
      number=25, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lockAgents', full_name='tool.Tool.lockAgents', index=25,
      number=26, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sandboxRun', full_name='tool.Tool.sandboxRun', index=26,
      number=27, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='whiteList', full_name='tool.Tool.whiteList', index=27,
      number=28, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='windowsSession', full_name='tool.Tool.windowsSession', index=28,
      number=29, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blackList', full_name='tool.Tool.blackList', index=29,
      number=30, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='toolOutputs', full_name='tool.Tool.toolOutputs', index=30,
      number=31, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outputDefs', full_name='tool.Tool.outputDefs', index=31,
      number=32, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tableDefs', full_name='tool.Tool.tableDefs', index=32,
      number=33, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vCreateTime', full_name='tool.Tool.vCreateTime', index=33,
      number=34, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vUpdateTime', full_name='tool.Tool.vUpdateTime', index=34,
      number=35, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vName', full_name='tool.Tool.vName', index=35,
      number=36, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vCreator', full_name='tool.Tool.vCreator', index=36,
      number=37, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readAuthorizers', full_name='tool.Tool.readAuthorizers', index=37,
      number=38, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updateAuthorizers', full_name='tool.Tool.updateAuthorizers', index=38,
      number=39, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deleteAuthorizers', full_name='tool.Tool.deleteAuthorizers', index=39,
      number=40, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='executeAuthorizers', full_name='tool.Tool.executeAuthorizers', index=40,
      number=41, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readExecutionResultAuthorizers', full_name='tool.Tool.readExecutionResultAuthorizers', index=41,
      number=42, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rootExecuteAuthorizers', full_name='tool.Tool.rootExecuteAuthorizers', index=42,
      number=43, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vDesc', full_name='tool.Tool.vDesc', index=43,
      number=44, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sourceFrom', full_name='tool.Tool.sourceFrom', index=44,
      number=45, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='envType', full_name='tool.Tool.envType', index=45,
      number=46, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checkType', full_name='tool.Tool.checkType', index=46,
      number=47, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checkUser', full_name='tool.Tool.checkUser', index=47,
      number=48, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checkSponsor', full_name='tool.Tool.checkSponsor', index=48,
      number=49, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checkComment', full_name='tool.Tool.checkComment', index=49,
      number=50, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batchStrategy', full_name='tool.Tool.batchStrategy', index=50,
      number=51, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='functionType', full_name='tool.Tool.functionType', index=51,
      number=52, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_system_org', full_name='tool.Tool.is_system_org', index=52,
      number=53, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subscribers', full_name='tool.Tool.subscribers', index=53,
      number=54, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subscribedChannel', full_name='tool.Tool.subscribedChannel', index=54,
      number=55, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readOnly', full_name='tool.Tool.readOnly', index=55,
      number=56, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='templateType', full_name='tool.Tool.templateType', index=56,
      number=57, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delete_me', full_name='tool.Tool.delete_me', index=57,
      number=58, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='approvers', full_name='tool.Tool.approvers', index=58,
      number=59, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ansibleNodeExecUser', full_name='tool.Tool.ansibleNodeExecUser', index=59,
      number=60, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log', full_name='tool.Tool.log', index=60,
      number=61, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TOOL_OUTPUTDEFS, _TOOL_TABLEDEFS, _TOOL_LOG, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=97,
  serialized_end=1747,
)

_TOOL_OUTPUTDEFS.containing_type = _TOOL
_TOOL_TABLEDEFS_DIMENSIONS.containing_type = _TOOL_TABLEDEFS
_TOOL_TABLEDEFS_COLUMNS.containing_type = _TOOL_TABLEDEFS
_TOOL_TABLEDEFS.fields_by_name['dimensions'].message_type = _TOOL_TABLEDEFS_DIMENSIONS
_TOOL_TABLEDEFS.fields_by_name['columns'].message_type = _TOOL_TABLEDEFS_COLUMNS
_TOOL_TABLEDEFS.containing_type = _TOOL
_TOOL_LOG.containing_type = _TOOL
_TOOL.fields_by_name['inputs'].message_type = easy__command__sdk_dot_model_dot_tool_dot_tool__input__pb2._TOOLINPUT
_TOOL.fields_by_name['toolOutputs'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_TOOL.fields_by_name['outputDefs'].message_type = _TOOL_OUTPUTDEFS
_TOOL.fields_by_name['tableDefs'].message_type = _TOOL_TABLEDEFS
_TOOL.fields_by_name['batchStrategy'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_TOOL.fields_by_name['log'].message_type = _TOOL_LOG
DESCRIPTOR.message_types_by_name['Tool'] = _TOOL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Tool = _reflection.GeneratedProtocolMessageType('Tool', (_message.Message,), {

  'OutputDefs' : _reflection.GeneratedProtocolMessageType('OutputDefs', (_message.Message,), {
    'DESCRIPTOR' : _TOOL_OUTPUTDEFS,
    '__module__' : 'tool_pb2'
    # @@protoc_insertion_point(class_scope:tool.Tool.OutputDefs)
    })
  ,

  'TableDefs' : _reflection.GeneratedProtocolMessageType('TableDefs', (_message.Message,), {

    'Dimensions' : _reflection.GeneratedProtocolMessageType('Dimensions', (_message.Message,), {
      'DESCRIPTOR' : _TOOL_TABLEDEFS_DIMENSIONS,
      '__module__' : 'tool_pb2'
      # @@protoc_insertion_point(class_scope:tool.Tool.TableDefs.Dimensions)
      })
    ,

    'Columns' : _reflection.GeneratedProtocolMessageType('Columns', (_message.Message,), {
      'DESCRIPTOR' : _TOOL_TABLEDEFS_COLUMNS,
      '__module__' : 'tool_pb2'
      # @@protoc_insertion_point(class_scope:tool.Tool.TableDefs.Columns)
      })
    ,
    'DESCRIPTOR' : _TOOL_TABLEDEFS,
    '__module__' : 'tool_pb2'
    # @@protoc_insertion_point(class_scope:tool.Tool.TableDefs)
    })
  ,

  'Log' : _reflection.GeneratedProtocolMessageType('Log', (_message.Message,), {
    'DESCRIPTOR' : _TOOL_LOG,
    '__module__' : 'tool_pb2'
    # @@protoc_insertion_point(class_scope:tool.Tool.Log)
    })
  ,
  'DESCRIPTOR' : _TOOL,
  '__module__' : 'tool_pb2'
  # @@protoc_insertion_point(class_scope:tool.Tool)
  })
_sym_db.RegisterMessage(Tool)
_sym_db.RegisterMessage(Tool.OutputDefs)
_sym_db.RegisterMessage(Tool.TableDefs)
_sym_db.RegisterMessage(Tool.TableDefs.Dimensions)
_sym_db.RegisterMessage(Tool.TableDefs.Columns)
_sym_db.RegisterMessage(Tool.Log)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
