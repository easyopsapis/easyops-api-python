# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flow_instance.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from collector_service_sdk.model.flow import flow_execute_step_pb2 as collector__service__sdk_dot_model_dot_flow_dot_flow__execute__step__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='flow_instance.proto',
  package='flow',
  syntax='proto3',
  serialized_options=_b('Z>go.easyops.local/contracts/protorepo-models/easyops/model/flow'),
  serialized_pb=_b('\n\x13\x66low_instance.proto\x12\x04\x66low\x1a\x38\x63ollector_service_sdk/model/flow/flow_execute_step.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xf2\n\n\x0c\x46lowInstance\x12\'\n\x08stepList\x18\x01 \x03(\x0b\x32\x15.flow.FlowExecuteStep\x12\x0e\n\x06taskId\x18\x02 \x01(\t\x12,\n\x0binstanceMap\x18\x03 \x03(\x0b\x32\x17.google.protobuf.Struct\x12\'\n\x07outputs\x18\x04 \x01(\x0b\x32\x16.google.protobuf.Value\x12,\n\x0crunningSteps\x18\x05 \x01(\x0b\x32\x16.google.protobuf.Value\x12\x12\n\nneedNotify\x18\x06 \x01(\x08\x12\x11\n\tstartTime\x18\x07 \x01(\x03\x12\x0f\n\x07\x65ndTime\x18\x08 \x01(\x03\x12\x13\n\x0b\x63urrentTime\x18\t \x01(\x03\x12\x13\n\x0btotalStatus\x18\n \x01(\t\x12\x0f\n\x07message\x18\x0b \x01(\t\x12\x13\n\x0btaskCounter\x18\x0c \x01(\x05\x12/\n\x0f\x66lowOutputsData\x18\r \x01(\x0b\x32\x16.google.protobuf.Value\x12)\n\ttableData\x18\x0e \x01(\x0b\x32\x16.google.protobuf.Value\x12/\n\x0fstandardOutputs\x18\x0f \x01(\x0b\x32\x16.google.protobuf.Value\x12)\n\tagentData\x18\x10 \x01(\x0b\x32\x16.google.protobuf.Value\x12\x0e\n\x06\x66lowId\x18\x11 \x01(\t\x12\x0f\n\x07version\x18\x12 \x01(\x05\x12*\n\nflowInputs\x18\x13 \x01(\x0b\x32\x16.google.protobuf.Value\x12\'\n\x07\x66lowEnv\x18\x14 \x01(\x0b\x32\x16.google.protobuf.Value\x12-\n\x08metadata\x18\x15 \x01(\x0b\x32\x1b.flow.FlowInstance.Metadata\x12\x0c\n\x04name\x18\x16 \x01(\t\x12\x0b\n\x03org\x18\x17 \x01(\x05\x12\x33\n\x0b\x66lowOutputs\x18\x18 \x03(\x0b\x32\x1e.flow.FlowInstance.FlowOutputs\x12\x31\n\noutputDefs\x18\x19 \x03(\x0b\x32\x1d.flow.FlowInstance.OutputDefs\x12/\n\ttableDefs\x18\x1a \x03(\x0b\x32\x1c.flow.FlowInstance.TableDefs\x12\x0f\n\x07\x63reator\x18\x1b \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x1c \x01(\t\x12\x12\n\nupdateTime\x18\x1d \x01(\t\x12\x12\n\ncreateTime\x18\x1e \x01(\t\x1a&\n\x08Metadata\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x02 \x01(\t\x1ay\n\x0b\x46lowOutputs\x12\x37\n\x07\x63olumns\x18\x01 \x03(\x0b\x32&.flow.FlowInstance.FlowOutputs.Columns\x1a\x31\n\x07\x43olumns\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x1a\x34\n\nOutputDefs\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x1a\xe6\x01\n\tTableDefs\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12;\n\ndimensions\x18\x03 \x03(\x0b\x32\'.flow.FlowInstance.TableDefs.Dimensions\x12\x35\n\x07\x63olumns\x18\x04 \x03(\x0b\x32$.flow.FlowInstance.TableDefs.Columns\x1a&\n\nDimensions\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x1a#\n\x07\x43olumns\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\tB@Z>go.easyops.local/contracts/protorepo-models/easyops/model/flowb\x06proto3')
  ,
  dependencies=[collector__service__sdk_dot_model_dot_flow_dot_flow__execute__step__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_FLOWINSTANCE_METADATA = _descriptor.Descriptor(
  name='Metadata',
  full_name='flow.FlowInstance.Metadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='flow.FlowInstance.Metadata.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='desc', full_name='flow.FlowInstance.Metadata.desc', index=1,
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
  serialized_start=1064,
  serialized_end=1102,
)

_FLOWINSTANCE_FLOWOUTPUTS_COLUMNS = _descriptor.Descriptor(
  name='Columns',
  full_name='flow.FlowInstance.FlowOutputs.Columns',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='flow.FlowInstance.FlowOutputs.Columns.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='flow.FlowInstance.FlowOutputs.Columns.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='flow.FlowInstance.FlowOutputs.Columns.name', index=2,
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
  serialized_start=1176,
  serialized_end=1225,
)

_FLOWINSTANCE_FLOWOUTPUTS = _descriptor.Descriptor(
  name='FlowOutputs',
  full_name='flow.FlowInstance.FlowOutputs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='columns', full_name='flow.FlowInstance.FlowOutputs.columns', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FLOWINSTANCE_FLOWOUTPUTS_COLUMNS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1104,
  serialized_end=1225,
)

_FLOWINSTANCE_OUTPUTDEFS = _descriptor.Descriptor(
  name='OutputDefs',
  full_name='flow.FlowInstance.OutputDefs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='flow.FlowInstance.OutputDefs.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='flow.FlowInstance.OutputDefs.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='flow.FlowInstance.OutputDefs.name', index=2,
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
  serialized_start=1227,
  serialized_end=1279,
)

_FLOWINSTANCE_TABLEDEFS_DIMENSIONS = _descriptor.Descriptor(
  name='Dimensions',
  full_name='flow.FlowInstance.TableDefs.Dimensions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='flow.FlowInstance.TableDefs.Dimensions.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='flow.FlowInstance.TableDefs.Dimensions.name', index=1,
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
  serialized_start=1437,
  serialized_end=1475,
)

_FLOWINSTANCE_TABLEDEFS_COLUMNS = _descriptor.Descriptor(
  name='Columns',
  full_name='flow.FlowInstance.TableDefs.Columns',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='flow.FlowInstance.TableDefs.Columns.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='flow.FlowInstance.TableDefs.Columns.name', index=1,
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
  serialized_start=1477,
  serialized_end=1512,
)

_FLOWINSTANCE_TABLEDEFS = _descriptor.Descriptor(
  name='TableDefs',
  full_name='flow.FlowInstance.TableDefs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='flow.FlowInstance.TableDefs.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='flow.FlowInstance.TableDefs.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dimensions', full_name='flow.FlowInstance.TableDefs.dimensions', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='columns', full_name='flow.FlowInstance.TableDefs.columns', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FLOWINSTANCE_TABLEDEFS_DIMENSIONS, _FLOWINSTANCE_TABLEDEFS_COLUMNS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1282,
  serialized_end=1512,
)

_FLOWINSTANCE = _descriptor.Descriptor(
  name='FlowInstance',
  full_name='flow.FlowInstance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stepList', full_name='flow.FlowInstance.stepList', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='taskId', full_name='flow.FlowInstance.taskId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceMap', full_name='flow.FlowInstance.instanceMap', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='flow.FlowInstance.outputs', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='runningSteps', full_name='flow.FlowInstance.runningSteps', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='needNotify', full_name='flow.FlowInstance.needNotify', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='flow.FlowInstance.startTime', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endTime', full_name='flow.FlowInstance.endTime', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currentTime', full_name='flow.FlowInstance.currentTime', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='totalStatus', full_name='flow.FlowInstance.totalStatus', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='flow.FlowInstance.message', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='taskCounter', full_name='flow.FlowInstance.taskCounter', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flowOutputsData', full_name='flow.FlowInstance.flowOutputsData', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tableData', full_name='flow.FlowInstance.tableData', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='standardOutputs', full_name='flow.FlowInstance.standardOutputs', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agentData', full_name='flow.FlowInstance.agentData', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flowId', full_name='flow.FlowInstance.flowId', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='flow.FlowInstance.version', index=17,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flowInputs', full_name='flow.FlowInstance.flowInputs', index=18,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flowEnv', full_name='flow.FlowInstance.flowEnv', index=19,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='flow.FlowInstance.metadata', index=20,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='flow.FlowInstance.name', index=21,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org', full_name='flow.FlowInstance.org', index=22,
      number=23, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flowOutputs', full_name='flow.FlowInstance.flowOutputs', index=23,
      number=24, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outputDefs', full_name='flow.FlowInstance.outputDefs', index=24,
      number=25, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tableDefs', full_name='flow.FlowInstance.tableDefs', index=25,
      number=26, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='flow.FlowInstance.creator', index=26,
      number=27, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='flow.FlowInstance.category', index=27,
      number=28, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updateTime', full_name='flow.FlowInstance.updateTime', index=28,
      number=29, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='createTime', full_name='flow.FlowInstance.createTime', index=29,
      number=30, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FLOWINSTANCE_METADATA, _FLOWINSTANCE_FLOWOUTPUTS, _FLOWINSTANCE_OUTPUTDEFS, _FLOWINSTANCE_TABLEDEFS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=118,
  serialized_end=1512,
)

_FLOWINSTANCE_METADATA.containing_type = _FLOWINSTANCE
_FLOWINSTANCE_FLOWOUTPUTS_COLUMNS.containing_type = _FLOWINSTANCE_FLOWOUTPUTS
_FLOWINSTANCE_FLOWOUTPUTS.fields_by_name['columns'].message_type = _FLOWINSTANCE_FLOWOUTPUTS_COLUMNS
_FLOWINSTANCE_FLOWOUTPUTS.containing_type = _FLOWINSTANCE
_FLOWINSTANCE_OUTPUTDEFS.containing_type = _FLOWINSTANCE
_FLOWINSTANCE_TABLEDEFS_DIMENSIONS.containing_type = _FLOWINSTANCE_TABLEDEFS
_FLOWINSTANCE_TABLEDEFS_COLUMNS.containing_type = _FLOWINSTANCE_TABLEDEFS
_FLOWINSTANCE_TABLEDEFS.fields_by_name['dimensions'].message_type = _FLOWINSTANCE_TABLEDEFS_DIMENSIONS
_FLOWINSTANCE_TABLEDEFS.fields_by_name['columns'].message_type = _FLOWINSTANCE_TABLEDEFS_COLUMNS
_FLOWINSTANCE_TABLEDEFS.containing_type = _FLOWINSTANCE
_FLOWINSTANCE.fields_by_name['stepList'].message_type = collector__service__sdk_dot_model_dot_flow_dot_flow__execute__step__pb2._FLOWEXECUTESTEP
_FLOWINSTANCE.fields_by_name['instanceMap'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_FLOWINSTANCE.fields_by_name['outputs'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_FLOWINSTANCE.fields_by_name['runningSteps'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_FLOWINSTANCE.fields_by_name['flowOutputsData'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_FLOWINSTANCE.fields_by_name['tableData'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_FLOWINSTANCE.fields_by_name['standardOutputs'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_FLOWINSTANCE.fields_by_name['agentData'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_FLOWINSTANCE.fields_by_name['flowInputs'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_FLOWINSTANCE.fields_by_name['flowEnv'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_FLOWINSTANCE.fields_by_name['metadata'].message_type = _FLOWINSTANCE_METADATA
_FLOWINSTANCE.fields_by_name['flowOutputs'].message_type = _FLOWINSTANCE_FLOWOUTPUTS
_FLOWINSTANCE.fields_by_name['outputDefs'].message_type = _FLOWINSTANCE_OUTPUTDEFS
_FLOWINSTANCE.fields_by_name['tableDefs'].message_type = _FLOWINSTANCE_TABLEDEFS
DESCRIPTOR.message_types_by_name['FlowInstance'] = _FLOWINSTANCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FlowInstance = _reflection.GeneratedProtocolMessageType('FlowInstance', (_message.Message,), {

  'Metadata' : _reflection.GeneratedProtocolMessageType('Metadata', (_message.Message,), {
    'DESCRIPTOR' : _FLOWINSTANCE_METADATA,
    '__module__' : 'flow_instance_pb2'
    # @@protoc_insertion_point(class_scope:flow.FlowInstance.Metadata)
    })
  ,

  'FlowOutputs' : _reflection.GeneratedProtocolMessageType('FlowOutputs', (_message.Message,), {

    'Columns' : _reflection.GeneratedProtocolMessageType('Columns', (_message.Message,), {
      'DESCRIPTOR' : _FLOWINSTANCE_FLOWOUTPUTS_COLUMNS,
      '__module__' : 'flow_instance_pb2'
      # @@protoc_insertion_point(class_scope:flow.FlowInstance.FlowOutputs.Columns)
      })
    ,
    'DESCRIPTOR' : _FLOWINSTANCE_FLOWOUTPUTS,
    '__module__' : 'flow_instance_pb2'
    # @@protoc_insertion_point(class_scope:flow.FlowInstance.FlowOutputs)
    })
  ,

  'OutputDefs' : _reflection.GeneratedProtocolMessageType('OutputDefs', (_message.Message,), {
    'DESCRIPTOR' : _FLOWINSTANCE_OUTPUTDEFS,
    '__module__' : 'flow_instance_pb2'
    # @@protoc_insertion_point(class_scope:flow.FlowInstance.OutputDefs)
    })
  ,

  'TableDefs' : _reflection.GeneratedProtocolMessageType('TableDefs', (_message.Message,), {

    'Dimensions' : _reflection.GeneratedProtocolMessageType('Dimensions', (_message.Message,), {
      'DESCRIPTOR' : _FLOWINSTANCE_TABLEDEFS_DIMENSIONS,
      '__module__' : 'flow_instance_pb2'
      # @@protoc_insertion_point(class_scope:flow.FlowInstance.TableDefs.Dimensions)
      })
    ,

    'Columns' : _reflection.GeneratedProtocolMessageType('Columns', (_message.Message,), {
      'DESCRIPTOR' : _FLOWINSTANCE_TABLEDEFS_COLUMNS,
      '__module__' : 'flow_instance_pb2'
      # @@protoc_insertion_point(class_scope:flow.FlowInstance.TableDefs.Columns)
      })
    ,
    'DESCRIPTOR' : _FLOWINSTANCE_TABLEDEFS,
    '__module__' : 'flow_instance_pb2'
    # @@protoc_insertion_point(class_scope:flow.FlowInstance.TableDefs)
    })
  ,
  'DESCRIPTOR' : _FLOWINSTANCE,
  '__module__' : 'flow_instance_pb2'
  # @@protoc_insertion_point(class_scope:flow.FlowInstance)
  })
_sym_db.RegisterMessage(FlowInstance)
_sym_db.RegisterMessage(FlowInstance.Metadata)
_sym_db.RegisterMessage(FlowInstance.FlowOutputs)
_sym_db.RegisterMessage(FlowInstance.FlowOutputs.Columns)
_sym_db.RegisterMessage(FlowInstance.OutputDefs)
_sym_db.RegisterMessage(FlowInstance.TableDefs)
_sym_db.RegisterMessage(FlowInstance.TableDefs.Dimensions)
_sym_db.RegisterMessage(FlowInstance.TableDefs.Columns)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
