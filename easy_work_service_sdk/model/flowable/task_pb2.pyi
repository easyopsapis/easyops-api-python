# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from easy_work_service_sdk.model.flowable.process_variable_pb2 import (
    FlowableProcessVariable as easy_work_service_sdk___model___flowable___process_variable_pb2___FlowableProcessVariable,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
    Union as typing___Union,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class FlowableTask(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    id = ... # type: typing___Text
    url = ... # type: typing___Text
    owner = ... # type: typing___Text
    assignee = ... # type: typing___Text
    delegationState = ... # type: typing___Text
    name = ... # type: typing___Text
    description = ... # type: typing___Text
    createTime = ... # type: typing___Text
    dueDate = ... # type: typing___Text
    priority = ... # type: builtin___int
    suspended = ... # type: builtin___bool
    claimTime = ... # type: typing___Text
    taskDefinitionKey = ... # type: typing___Text
    scopeDefinitionId = ... # type: typing___Text
    scopeId = ... # type: typing___Text
    scopeType = ... # type: typing___Text
    tenantId = ... # type: typing___Text
    category = ... # type: typing___Text
    formKey = ... # type: typing___Text
    parentTaskId = ... # type: typing___Text
    executionId = ... # type: typing___Text
    executionUrl = ... # type: typing___Text
    processInstanceId = ... # type: typing___Text
    processInstanceUrl = ... # type: typing___Text
    processDefinitionId = ... # type: typing___Text
    processDefinitionUrl = ... # type: typing___Text

    @property
    def variables(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[easy_work_service_sdk___model___flowable___process_variable_pb2___FlowableProcessVariable]: ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        url : typing___Optional[typing___Text] = None,
        owner : typing___Optional[typing___Text] = None,
        assignee : typing___Optional[typing___Text] = None,
        delegationState : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        description : typing___Optional[typing___Text] = None,
        createTime : typing___Optional[typing___Text] = None,
        dueDate : typing___Optional[typing___Text] = None,
        priority : typing___Optional[builtin___int] = None,
        suspended : typing___Optional[builtin___bool] = None,
        claimTime : typing___Optional[typing___Text] = None,
        taskDefinitionKey : typing___Optional[typing___Text] = None,
        scopeDefinitionId : typing___Optional[typing___Text] = None,
        scopeId : typing___Optional[typing___Text] = None,
        scopeType : typing___Optional[typing___Text] = None,
        tenantId : typing___Optional[typing___Text] = None,
        category : typing___Optional[typing___Text] = None,
        formKey : typing___Optional[typing___Text] = None,
        parentTaskId : typing___Optional[typing___Text] = None,
        executionId : typing___Optional[typing___Text] = None,
        executionUrl : typing___Optional[typing___Text] = None,
        processInstanceId : typing___Optional[typing___Text] = None,
        processInstanceUrl : typing___Optional[typing___Text] = None,
        processDefinitionId : typing___Optional[typing___Text] = None,
        processDefinitionUrl : typing___Optional[typing___Text] = None,
        variables : typing___Optional[typing___Iterable[easy_work_service_sdk___model___flowable___process_variable_pb2___FlowableProcessVariable]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> FlowableTask: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> FlowableTask: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"assignee",b"assignee",u"category",b"category",u"claimTime",b"claimTime",u"createTime",b"createTime",u"delegationState",b"delegationState",u"description",b"description",u"dueDate",b"dueDate",u"executionId",b"executionId",u"executionUrl",b"executionUrl",u"formKey",b"formKey",u"id",b"id",u"name",b"name",u"owner",b"owner",u"parentTaskId",b"parentTaskId",u"priority",b"priority",u"processDefinitionId",b"processDefinitionId",u"processDefinitionUrl",b"processDefinitionUrl",u"processInstanceId",b"processInstanceId",u"processInstanceUrl",b"processInstanceUrl",u"scopeDefinitionId",b"scopeDefinitionId",u"scopeId",b"scopeId",u"scopeType",b"scopeType",u"suspended",b"suspended",u"taskDefinitionKey",b"taskDefinitionKey",u"tenantId",b"tenantId",u"url",b"url",u"variables",b"variables"]) -> None: ...
