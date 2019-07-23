# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: job_task_flow_callback.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from model.easy_flow import target_result_pb2 as model_dot_easy__flow_dot_target__result__pb2
from model.easy_flow import deploy_label_pb2 as model_dot_easy__flow_dot_deploy__label__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='job_task_flow_callback.proto',
  package='job_task',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1cjob_task_flow_callback.proto\x12\x08job_task\x1a#model/easy_flow/target_result.proto\x1a\"model/easy_flow/deploy_label.proto\x1a\x1bgoogle/protobuf/empty.proto\"}\n#JobTasksFlowCallbackResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12$\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x16.google.protobuf.Emptyb\x06proto3')
  ,
  dependencies=[model_dot_easy__flow_dot_target__result__pb2.DESCRIPTOR,model_dot_easy__flow_dot_deploy__label__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_JOBTASKSFLOWCALLBACKRESPONSEWRAPPER = _descriptor.Descriptor(
  name='JobTasksFlowCallbackResponseWrapper',
  full_name='job_task.JobTasksFlowCallbackResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='job_task.JobTasksFlowCallbackResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='job_task.JobTasksFlowCallbackResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='job_task.JobTasksFlowCallbackResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='job_task.JobTasksFlowCallbackResponseWrapper.data', index=3,
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
  serialized_start=144,
  serialized_end=269,
)

_JOBTASKSFLOWCALLBACKRESPONSEWRAPPER.fields_by_name['data'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
DESCRIPTOR.message_types_by_name['JobTasksFlowCallbackResponseWrapper'] = _JOBTASKSFLOWCALLBACKRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

JobTasksFlowCallbackResponseWrapper = _reflection.GeneratedProtocolMessageType('JobTasksFlowCallbackResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _JOBTASKSFLOWCALLBACKRESPONSEWRAPPER,
  __module__ = 'job_task_flow_callback_pb2'
  # @@protoc_insertion_point(class_scope:job_task.JobTasksFlowCallbackResponseWrapper)
  ))
_sym_db.RegisterMessage(JobTasksFlowCallbackResponseWrapper)


# @@protoc_insertion_point(module_scope)
