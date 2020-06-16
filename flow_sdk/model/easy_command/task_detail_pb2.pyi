# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from flow_sdk.model.easy_command.target_log_pb2 import (
    TargetLog as flow_sdk___model___easy_command___target_log_pb2___TargetLog,
)

from flow_sdk.model.easy_command.task_callback_pb2 import (
    TaskCallback as flow_sdk___model___easy_command___task_callback_pb2___TaskCallback,
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


class TaskDetail(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    taskId = ... # type: typing___Text
    name = ... # type: typing___Text
    type = ... # type: typing___Text
    operation = ... # type: typing___Text
    groupId = ... # type: typing___Text
    appId = ... # type: typing___Text
    clusterId = ... # type: typing___Text
    packageId = ... # type: typing___Text
    versionId = ... # type: typing___Text
    needNotify = ... # type: builtin___bool
    batchNum = ... # type: builtin___int
    batchInterval = ... # type: builtin___int
    failedStop = ... # type: builtin___bool
    org = ... # type: builtin___int
    operator = ... # type: typing___Text
    status = ... # type: typing___Text
    code = ... # type: builtin___int
    usedTime = ... # type: builtin___int
    startTime = ... # type: typing___Text
    updateTime = ... # type: typing___Text
    endTime = ... # type: typing___Text

    @property
    def callback(self) -> flow_sdk___model___easy_command___task_callback_pb2___TaskCallback: ...

    @property
    def targetsLog(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[flow_sdk___model___easy_command___target_log_pb2___TargetLog]: ...

    def __init__(self,
        *,
        taskId : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        type : typing___Optional[typing___Text] = None,
        operation : typing___Optional[typing___Text] = None,
        groupId : typing___Optional[typing___Text] = None,
        appId : typing___Optional[typing___Text] = None,
        clusterId : typing___Optional[typing___Text] = None,
        packageId : typing___Optional[typing___Text] = None,
        versionId : typing___Optional[typing___Text] = None,
        needNotify : typing___Optional[builtin___bool] = None,
        callback : typing___Optional[flow_sdk___model___easy_command___task_callback_pb2___TaskCallback] = None,
        batchNum : typing___Optional[builtin___int] = None,
        batchInterval : typing___Optional[builtin___int] = None,
        failedStop : typing___Optional[builtin___bool] = None,
        org : typing___Optional[builtin___int] = None,
        operator : typing___Optional[typing___Text] = None,
        status : typing___Optional[typing___Text] = None,
        code : typing___Optional[builtin___int] = None,
        usedTime : typing___Optional[builtin___int] = None,
        startTime : typing___Optional[typing___Text] = None,
        updateTime : typing___Optional[typing___Text] = None,
        endTime : typing___Optional[typing___Text] = None,
        targetsLog : typing___Optional[typing___Iterable[flow_sdk___model___easy_command___target_log_pb2___TargetLog]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> TaskDetail: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> TaskDetail: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"callback",b"callback"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"appId",b"appId",u"batchInterval",b"batchInterval",u"batchNum",b"batchNum",u"callback",b"callback",u"clusterId",b"clusterId",u"code",b"code",u"endTime",b"endTime",u"failedStop",b"failedStop",u"groupId",b"groupId",u"name",b"name",u"needNotify",b"needNotify",u"operation",b"operation",u"operator",b"operator",u"org",b"org",u"packageId",b"packageId",u"startTime",b"startTime",u"status",b"status",u"targetsLog",b"targetsLog",u"taskId",b"taskId",u"type",b"type",u"updateTime",b"updateTime",u"usedTime",b"usedTime",u"versionId",b"versionId"]) -> None: ...
