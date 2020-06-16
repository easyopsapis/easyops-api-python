# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from pipeline_sdk.model.flowable.process_variable_pb2 import (
    FlowableProcessVariable as pipeline_sdk___model___flowable___process_variable_pb2___FlowableProcessVariable,
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


class FlowableProcessInstance(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    id = ... # type: typing___Text
    name = ... # type: typing___Text
    businessKey = ... # type: typing___Text
    suspended = ... # type: builtin___bool
    ended = ... # type: builtin___bool
    processDefinitionId = ... # type: typing___Text
    processDefinitionName = ... # type: typing___Text
    processDefinitionDescription = ... # type: typing___Text
    activityId = ... # type: typing___Text
    startUserId = ... # type: typing___Text
    callbackId = ... # type: typing___Text
    callbackType = ... # type: typing___Text
    referenceId = ... # type: typing___Text
    referenceType = ... # type: typing___Text
    tenantId = ... # type: typing___Text
    completed = ... # type: builtin___bool
    startTime = ... # type: typing___Text

    @property
    def variables(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[pipeline_sdk___model___flowable___process_variable_pb2___FlowableProcessVariable]: ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        businessKey : typing___Optional[typing___Text] = None,
        suspended : typing___Optional[builtin___bool] = None,
        ended : typing___Optional[builtin___bool] = None,
        processDefinitionId : typing___Optional[typing___Text] = None,
        processDefinitionName : typing___Optional[typing___Text] = None,
        processDefinitionDescription : typing___Optional[typing___Text] = None,
        activityId : typing___Optional[typing___Text] = None,
        startUserId : typing___Optional[typing___Text] = None,
        callbackId : typing___Optional[typing___Text] = None,
        callbackType : typing___Optional[typing___Text] = None,
        referenceId : typing___Optional[typing___Text] = None,
        referenceType : typing___Optional[typing___Text] = None,
        tenantId : typing___Optional[typing___Text] = None,
        completed : typing___Optional[builtin___bool] = None,
        startTime : typing___Optional[typing___Text] = None,
        variables : typing___Optional[typing___Iterable[pipeline_sdk___model___flowable___process_variable_pb2___FlowableProcessVariable]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> FlowableProcessInstance: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> FlowableProcessInstance: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"activityId",b"activityId",u"businessKey",b"businessKey",u"callbackId",b"callbackId",u"callbackType",b"callbackType",u"completed",b"completed",u"ended",b"ended",u"id",b"id",u"name",b"name",u"processDefinitionDescription",b"processDefinitionDescription",u"processDefinitionId",b"processDefinitionId",u"processDefinitionName",b"processDefinitionName",u"referenceId",b"referenceId",u"referenceType",b"referenceType",u"startTime",b"startTime",u"startUserId",b"startUserId",u"suspended",b"suspended",u"tenantId",b"tenantId",u"variables",b"variables"]) -> None: ...
