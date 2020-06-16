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

from permission_sdk.model.easy_command.action_pb2 import (
    Action as permission_sdk___model___easy_command___action_pb2___Action,
)

from permission_sdk.model.easy_command.target_pb2 import (
    Target as permission_sdk___model___easy_command___target_pb2___Target,
)

from permission_sdk.model.easy_command.task_callback_pb2 import (
    TaskCallback as permission_sdk___model___easy_command___task_callback_pb2___TaskCallback,
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


class TaskSpec(google___protobuf___message___Message):
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

    @property
    def actions(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[permission_sdk___model___easy_command___action_pb2___Action]: ...

    @property
    def targets(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[permission_sdk___model___easy_command___target_pb2___Target]: ...

    @property
    def callback(self) -> permission_sdk___model___easy_command___task_callback_pb2___TaskCallback: ...

    def __init__(self,
        *,
        taskId : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        type : typing___Optional[typing___Text] = None,
        operation : typing___Optional[typing___Text] = None,
        groupId : typing___Optional[typing___Text] = None,
        actions : typing___Optional[typing___Iterable[permission_sdk___model___easy_command___action_pb2___Action]] = None,
        targets : typing___Optional[typing___Iterable[permission_sdk___model___easy_command___target_pb2___Target]] = None,
        appId : typing___Optional[typing___Text] = None,
        clusterId : typing___Optional[typing___Text] = None,
        packageId : typing___Optional[typing___Text] = None,
        versionId : typing___Optional[typing___Text] = None,
        needNotify : typing___Optional[builtin___bool] = None,
        callback : typing___Optional[permission_sdk___model___easy_command___task_callback_pb2___TaskCallback] = None,
        batchNum : typing___Optional[builtin___int] = None,
        batchInterval : typing___Optional[builtin___int] = None,
        failedStop : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> TaskSpec: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> TaskSpec: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"callback",b"callback"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"actions",b"actions",u"appId",b"appId",u"batchInterval",b"batchInterval",u"batchNum",b"batchNum",u"callback",b"callback",u"clusterId",b"clusterId",u"failedStop",b"failedStop",u"groupId",b"groupId",u"name",b"name",u"needNotify",b"needNotify",u"operation",b"operation",u"packageId",b"packageId",u"targets",b"targets",u"taskId",b"taskId",u"type",b"type",u"versionId",b"versionId"]) -> None: ...
