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

from google.protobuf.struct_pb2 import (
    Struct as google___protobuf___struct_pb2___Struct,
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


class TaskRet(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class TargetsLog(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class ActionsLog(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            name = ... # type: typing___Text
            type = ... # type: typing___Text
            action = ... # type: typing___Text
            status = ... # type: typing___Text
            code = ... # type: builtin___int
            msg = ... # type: typing___Text
            usedTime = ... # type: builtin___int
            startTime = ... # type: typing___Text
            endTime = ... # type: typing___Text

            @property
            def extInfo(self) -> google___protobuf___struct_pb2___Struct: ...

            @property
            def progress(self) -> google___protobuf___struct_pb2___Struct: ...

            def __init__(self,
                *,
                name : typing___Optional[typing___Text] = None,
                type : typing___Optional[typing___Text] = None,
                action : typing___Optional[typing___Text] = None,
                status : typing___Optional[typing___Text] = None,
                code : typing___Optional[builtin___int] = None,
                extInfo : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
                msg : typing___Optional[typing___Text] = None,
                progress : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
                usedTime : typing___Optional[builtin___int] = None,
                startTime : typing___Optional[typing___Text] = None,
                endTime : typing___Optional[typing___Text] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> TaskRet.TargetsLog.ActionsLog: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> TaskRet.TargetsLog.ActionsLog: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def HasField(self, field_name: typing_extensions___Literal[u"extInfo",b"extInfo",u"progress",b"progress"]) -> builtin___bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"action",b"action",u"code",b"code",u"endTime",b"endTime",u"extInfo",b"extInfo",u"msg",b"msg",u"name",b"name",u"progress",b"progress",u"startTime",b"startTime",u"status",b"status",u"type",b"type",u"usedTime",b"usedTime"]) -> None: ...

        targetId = ... # type: typing___Text
        targetName = ... # type: typing___Text
        status = ... # type: typing___Text
        sysStatus = ... # type: typing___Text
        code = ... # type: builtin___int
        msg = ... # type: typing___Text

        @property
        def progress(self) -> google___protobuf___struct_pb2___Struct: ...

        @property
        def actionsLog(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[TaskRet.TargetsLog.ActionsLog]: ...

        def __init__(self,
            *,
            targetId : typing___Optional[typing___Text] = None,
            targetName : typing___Optional[typing___Text] = None,
            status : typing___Optional[typing___Text] = None,
            sysStatus : typing___Optional[typing___Text] = None,
            code : typing___Optional[builtin___int] = None,
            msg : typing___Optional[typing___Text] = None,
            progress : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
            actionsLog : typing___Optional[typing___Iterable[TaskRet.TargetsLog.ActionsLog]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> TaskRet.TargetsLog: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> TaskRet.TargetsLog: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"progress",b"progress"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"actionsLog",b"actionsLog",u"code",b"code",u"msg",b"msg",u"progress",b"progress",u"status",b"status",u"sysStatus",b"sysStatus",u"targetId",b"targetId",u"targetName",b"targetName"]) -> None: ...

    taskId = ... # type: typing___Text
    name = ... # type: typing___Text
    groupId = ... # type: typing___Text
    appId = ... # type: typing___Text
    batchNum = ... # type: builtin___int
    batchInterval = ... # type: builtin___int
    failedStop = ... # type: builtin___bool
    packageId = ... # type: typing___Text
    type = ... # type: typing___Text
    operation = ... # type: typing___Text
    org = ... # type: builtin___int
    operator = ... # type: typing___Text
    status = ... # type: typing___Text
    code = ... # type: builtin___int
    usedTime = ... # type: builtin___int
    startTime = ... # type: typing___Text
    endTime = ... # type: typing___Text

    @property
    def extraInfo(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def targetsLog(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[TaskRet.TargetsLog]: ...

    def __init__(self,
        *,
        taskId : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        groupId : typing___Optional[typing___Text] = None,
        appId : typing___Optional[typing___Text] = None,
        batchNum : typing___Optional[builtin___int] = None,
        batchInterval : typing___Optional[builtin___int] = None,
        failedStop : typing___Optional[builtin___bool] = None,
        packageId : typing___Optional[typing___Text] = None,
        type : typing___Optional[typing___Text] = None,
        operation : typing___Optional[typing___Text] = None,
        org : typing___Optional[builtin___int] = None,
        operator : typing___Optional[typing___Text] = None,
        status : typing___Optional[typing___Text] = None,
        code : typing___Optional[builtin___int] = None,
        usedTime : typing___Optional[builtin___int] = None,
        startTime : typing___Optional[typing___Text] = None,
        endTime : typing___Optional[typing___Text] = None,
        extraInfo : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        targetsLog : typing___Optional[typing___Iterable[TaskRet.TargetsLog]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> TaskRet: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> TaskRet: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"extraInfo",b"extraInfo"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"appId",b"appId",u"batchInterval",b"batchInterval",u"batchNum",b"batchNum",u"code",b"code",u"endTime",b"endTime",u"extraInfo",b"extraInfo",u"failedStop",b"failedStop",u"groupId",b"groupId",u"name",b"name",u"operation",b"operation",u"operator",b"operator",u"org",b"org",u"packageId",b"packageId",u"startTime",b"startTime",u"status",b"status",u"targetsLog",b"targetsLog",u"taskId",b"taskId",u"type",b"type",u"usedTime",b"usedTime"]) -> None: ...
