# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flow.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from app_store_sdk.model.flow import flow_step_pb2 as app__store__sdk_dot_model_dot_flow_dot_flow__step__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='flow.proto',
  package='flow',
  syntax='proto3',
  serialized_options=_b('Z>go.easyops.local/contracts/protorepo-models/easyops/model/flow'),
  serialized_pb=_b('\n\nflow.proto\x12\x04\x66low\x1a(app_store_sdk/model/flow/flow_step.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xb4\t\n\x04\x46low\x12\x0e\n\x06\x66lowId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x04 \x01(\t\x12\r\n\x05vName\x18\x05 \x01(\t\x12\x12\n\nenableLoop\x18\x06 \x01(\x08\x12\x10\n\x08readOnly\x18\x07 \x01(\x08\x12\x0b\n\x03org\x18\x08 \x01(\x05\x12\x12\n\ncreateTime\x18\t \x01(\t\x12\x0f\n\x07\x63reator\x18\n \x01(\t\x12\x10\n\x08vCreator\x18\x0b \x01(\t\x12\x12\n\nupdateTime\x18\x0c \x01(\t\x12\x0f\n\x07version\x18\r \x01(\x05\x12\r\n\x05vDesc\x18\x0e \x01(\t\x12\x17\n\x0freadAuthorizers\x18\x0f \x03(\t\x12\x19\n\x11updateAuthorizers\x18\x10 \x03(\t\x12\x19\n\x11\x64\x65leteAuthorizers\x18\x11 \x03(\t\x12\x1a\n\x12\x65xecuteAuthorizers\x18\x12 \x03(\t\x12\x0c\n\x04memo\x18\x13 \x01(\t\x12\x13\n\x0bsubscribers\x18\x14 \x03(\t\x12\x19\n\x11subscribedChannel\x18\x15 \x01(\t\x12\x15\n\ris_system_org\x18\x16 \x01(\x08\x12 \n\x08stepList\x18\x17 \x03(\x0b\x32\x0e.flow.FlowStep\x12\'\n\ttableDefs\x18\x18 \x03(\x0b\x32\x14.flow.Flow.TableDefs\x12\'\n\x07\x66lowEnv\x18\x19 \x01(\x0b\x32\x16.google.protobuf.Value\x12\x0c\n\x04tags\x18\x1a \x03(\t\x12%\n\x08metadata\x18\x1b \x01(\x0b\x32\x13.flow.Flow.Metadata\x12*\n\nflowInputs\x18\x1c \x01(\x0b\x32\x16.google.protobuf.Value\x12+\n\x0b\x66lowOutputs\x18\x1d \x03(\x0b\x32\x16.flow.Flow.FlowOutputs\x12)\n\noutputDefs\x18\x1e \x03(\x0b\x32\x15.flow.Flow.OutputDefs\x12*\n\thistories\x18\x1f \x03(\x0b\x32\x17.google.protobuf.Struct\x1a\xd6\x01\n\tTableDefs\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x33\n\ndimensions\x18\x03 \x03(\x0b\x32\x1f.flow.Flow.TableDefs.Dimensions\x12-\n\x07\x63olumns\x18\x04 \x03(\x0b\x32\x1c.flow.Flow.TableDefs.Columns\x1a&\n\nDimensions\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x1a#\n\x07\x43olumns\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x1a&\n\x08Metadata\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x02 \x01(\t\x1aq\n\x0b\x46lowOutputs\x12/\n\x07\x63olumns\x18\x01 \x03(\x0b\x32\x1e.flow.Flow.FlowOutputs.Columns\x1a\x31\n\x07\x43olumns\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x1a\x34\n\nOutputDefs\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\tB@Z>go.easyops.local/contracts/protorepo-models/easyops/model/flowb\x06proto3')
  ,
  dependencies=[app__store__sdk_dot_model_dot_flow_dot_flow__step__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_FLOW_TABLEDEFS_DIMENSIONS = _descriptor.Descriptor(
  name='Dimensions',
  full_name='flow.Flow.TableDefs.Dimensions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='flow.Flow.TableDefs.Dimensions.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='flow.Flow.TableDefs.Dimensions.name', index=1,
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
  serialized_start=1013,
  serialized_end=1051,
)

_FLOW_TABLEDEFS_COLUMNS = _descriptor.Descriptor(
  name='Columns',
  full_name='flow.Flow.TableDefs.Columns',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='flow.Flow.TableDefs.Columns.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='flow.Flow.TableDefs.Columns.name', index=1,
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
  serialized_start=1053,
  serialized_end=1088,
)

_FLOW_TABLEDEFS = _descriptor.Descriptor(
  name='TableDefs',
  full_name='flow.Flow.TableDefs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='flow.Flow.TableDefs.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='flow.Flow.TableDefs.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dimensions', full_name='flow.Flow.TableDefs.dimensions', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='columns', full_name='flow.Flow.TableDefs.columns', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FLOW_TABLEDEFS_DIMENSIONS, _FLOW_TABLEDEFS_COLUMNS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=874,
  serialized_end=1088,
)

_FLOW_METADATA = _descriptor.Descriptor(
  name='Metadata',
  full_name='flow.Flow.Metadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='flow.Flow.Metadata.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='desc', full_name='flow.Flow.Metadata.desc', index=1,
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
  serialized_start=1090,
  serialized_end=1128,
)

_FLOW_FLOWOUTPUTS_COLUMNS = _descriptor.Descriptor(
  name='Columns',
  full_name='flow.Flow.FlowOutputs.Columns',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='flow.Flow.FlowOutputs.Columns.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='flow.Flow.FlowOutputs.Columns.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='flow.Flow.FlowOutputs.Columns.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=1194,
  serialized_end=1243,
)

_FLOW_FLOWOUTPUTS = _descriptor.Descriptor(
  name='FlowOutputs',
  full_name='flow.Flow.FlowOutputs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='columns', full_name='flow.Flow.FlowOutputs.columns', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FLOW_FLOWOUTPUTS_COLUMNS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1130,
  serialized_end=1243,
)

_FLOW_OUTPUTDEFS = _descriptor.Descriptor(
  name='OutputDefs',
  full_name='flow.Flow.OutputDefs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='flow.Flow.OutputDefs.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='flow.Flow.OutputDefs.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='flow.Flow.OutputDefs.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=1245,
  serialized_end=1297,
)

_FLOW = _descriptor.Descriptor(
  name='Flow',
  full_name='flow.Flow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='flowId', full_name='flow.Flow.flowId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='flow.Flow.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='flow.Flow.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='flow.Flow.category', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vName', full_name='flow.Flow.vName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enableLoop', full_name='flow.Flow.enableLoop', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readOnly', full_name='flow.Flow.readOnly', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org', full_name='flow.Flow.org', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='createTime', full_name='flow.Flow.createTime', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='flow.Flow.creator', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vCreator', full_name='flow.Flow.vCreator', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updateTime', full_name='flow.Flow.updateTime', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='flow.Flow.version', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vDesc', full_name='flow.Flow.vDesc', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readAuthorizers', full_name='flow.Flow.readAuthorizers', index=14,
      number=15, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updateAuthorizers', full_name='flow.Flow.updateAuthorizers', index=15,
      number=16, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deleteAuthorizers', full_name='flow.Flow.deleteAuthorizers', index=16,
      number=17, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='executeAuthorizers', full_name='flow.Flow.executeAuthorizers', index=17,
      number=18, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='flow.Flow.memo', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subscribers', full_name='flow.Flow.subscribers', index=19,
      number=20, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subscribedChannel', full_name='flow.Flow.subscribedChannel', index=20,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_system_org', full_name='flow.Flow.is_system_org', index=21,
      number=22, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stepList', full_name='flow.Flow.stepList', index=22,
      number=23, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tableDefs', full_name='flow.Flow.tableDefs', index=23,
      number=24, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flowEnv', full_name='flow.Flow.flowEnv', index=24,
      number=25, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='flow.Flow.tags', index=25,
      number=26, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='flow.Flow.metadata', index=26,
      number=27, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flowInputs', full_name='flow.Flow.flowInputs', index=27,
      number=28, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flowOutputs', full_name='flow.Flow.flowOutputs', index=28,
      number=29, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outputDefs', full_name='flow.Flow.outputDefs', index=29,
      number=30, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='histories', full_name='flow.Flow.histories', index=30,
      number=31, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FLOW_TABLEDEFS, _FLOW_METADATA, _FLOW_FLOWOUTPUTS, _FLOW_OUTPUTDEFS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=93,
  serialized_end=1297,
)

_FLOW_TABLEDEFS_DIMENSIONS.containing_type = _FLOW_TABLEDEFS
_FLOW_TABLEDEFS_COLUMNS.containing_type = _FLOW_TABLEDEFS
_FLOW_TABLEDEFS.fields_by_name['dimensions'].message_type = _FLOW_TABLEDEFS_DIMENSIONS
_FLOW_TABLEDEFS.fields_by_name['columns'].message_type = _FLOW_TABLEDEFS_COLUMNS
_FLOW_TABLEDEFS.containing_type = _FLOW
_FLOW_METADATA.containing_type = _FLOW
_FLOW_FLOWOUTPUTS_COLUMNS.containing_type = _FLOW_FLOWOUTPUTS
_FLOW_FLOWOUTPUTS.fields_by_name['columns'].message_type = _FLOW_FLOWOUTPUTS_COLUMNS
_FLOW_FLOWOUTPUTS.containing_type = _FLOW
_FLOW_OUTPUTDEFS.containing_type = _FLOW
_FLOW.fields_by_name['stepList'].message_type = app__store__sdk_dot_model_dot_flow_dot_flow__step__pb2._FLOWSTEP
_FLOW.fields_by_name['tableDefs'].message_type = _FLOW_TABLEDEFS
_FLOW.fields_by_name['flowEnv'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_FLOW.fields_by_name['metadata'].message_type = _FLOW_METADATA
_FLOW.fields_by_name['flowInputs'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_FLOW.fields_by_name['flowOutputs'].message_type = _FLOW_FLOWOUTPUTS
_FLOW.fields_by_name['outputDefs'].message_type = _FLOW_OUTPUTDEFS
_FLOW.fields_by_name['histories'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['Flow'] = _FLOW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Flow = _reflection.GeneratedProtocolMessageType('Flow', (_message.Message,), {

  'TableDefs' : _reflection.GeneratedProtocolMessageType('TableDefs', (_message.Message,), {

    'Dimensions' : _reflection.GeneratedProtocolMessageType('Dimensions', (_message.Message,), {
      'DESCRIPTOR' : _FLOW_TABLEDEFS_DIMENSIONS,
      '__module__' : 'flow_pb2'
      # @@protoc_insertion_point(class_scope:flow.Flow.TableDefs.Dimensions)
      })
    ,

    'Columns' : _reflection.GeneratedProtocolMessageType('Columns', (_message.Message,), {
      'DESCRIPTOR' : _FLOW_TABLEDEFS_COLUMNS,
      '__module__' : 'flow_pb2'
      # @@protoc_insertion_point(class_scope:flow.Flow.TableDefs.Columns)
      })
    ,
    'DESCRIPTOR' : _FLOW_TABLEDEFS,
    '__module__' : 'flow_pb2'
    # @@protoc_insertion_point(class_scope:flow.Flow.TableDefs)
    })
  ,

  'Metadata' : _reflection.GeneratedProtocolMessageType('Metadata', (_message.Message,), {
    'DESCRIPTOR' : _FLOW_METADATA,
    '__module__' : 'flow_pb2'
    # @@protoc_insertion_point(class_scope:flow.Flow.Metadata)
    })
  ,

  'FlowOutputs' : _reflection.GeneratedProtocolMessageType('FlowOutputs', (_message.Message,), {

    'Columns' : _reflection.GeneratedProtocolMessageType('Columns', (_message.Message,), {
      'DESCRIPTOR' : _FLOW_FLOWOUTPUTS_COLUMNS,
      '__module__' : 'flow_pb2'
      # @@protoc_insertion_point(class_scope:flow.Flow.FlowOutputs.Columns)
      })
    ,
    'DESCRIPTOR' : _FLOW_FLOWOUTPUTS,
    '__module__' : 'flow_pb2'
    # @@protoc_insertion_point(class_scope:flow.Flow.FlowOutputs)
    })
  ,

  'OutputDefs' : _reflection.GeneratedProtocolMessageType('OutputDefs', (_message.Message,), {
    'DESCRIPTOR' : _FLOW_OUTPUTDEFS,
    '__module__' : 'flow_pb2'
    # @@protoc_insertion_point(class_scope:flow.Flow.OutputDefs)
    })
  ,
  'DESCRIPTOR' : _FLOW,
  '__module__' : 'flow_pb2'
  # @@protoc_insertion_point(class_scope:flow.Flow)
  })
_sym_db.RegisterMessage(Flow)
_sym_db.RegisterMessage(Flow.TableDefs)
_sym_db.RegisterMessage(Flow.TableDefs.Dimensions)
_sym_db.RegisterMessage(Flow.TableDefs.Columns)
_sym_db.RegisterMessage(Flow.Metadata)
_sym_db.RegisterMessage(Flow.FlowOutputs)
_sym_db.RegisterMessage(Flow.FlowOutputs.Columns)
_sym_db.RegisterMessage(Flow.OutputDefs)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
