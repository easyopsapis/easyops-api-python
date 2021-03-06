# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
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


class GetPatchTaskDetailRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    taskId = ... # type: typing___Text

    def __init__(self,
        *,
        taskId : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetPatchTaskDetailRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetPatchTaskDetailRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"taskId",b"taskId"]) -> None: ...

class GetPatchTaskDetailResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class TaskResult(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class Result(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            patchId = ... # type: typing___Text
            wuec = ... # type: builtin___int
            message = ... # type: typing___Text
            articleId = ... # type: typing___Text
            releaseTime = ... # type: typing___Text
            size = ... # type: builtin___int
            memo = ... # type: typing___Text
            requireReboot = ... # type: builtin___bool
            status = ... # type: typing___Text
            ctime = ... # type: builtin___int
            etime = ... # type: builtin___int

            def __init__(self,
                *,
                patchId : typing___Optional[typing___Text] = None,
                wuec : typing___Optional[builtin___int] = None,
                message : typing___Optional[typing___Text] = None,
                articleId : typing___Optional[typing___Text] = None,
                releaseTime : typing___Optional[typing___Text] = None,
                size : typing___Optional[builtin___int] = None,
                memo : typing___Optional[typing___Text] = None,
                requireReboot : typing___Optional[builtin___bool] = None,
                status : typing___Optional[typing___Text] = None,
                ctime : typing___Optional[builtin___int] = None,
                etime : typing___Optional[builtin___int] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> GetPatchTaskDetailResponse.TaskResult.Result: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetPatchTaskDetailResponse.TaskResult.Result: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"articleId",b"articleId",u"ctime",b"ctime",u"etime",b"etime",u"memo",b"memo",u"message",b"message",u"patchId",b"patchId",u"releaseTime",b"releaseTime",u"requireReboot",b"requireReboot",u"size",b"size",u"status",b"status",u"wuec",b"wuec"]) -> None: ...

        hostId = ... # type: typing___Text
        hostIp = ... # type: typing___Text
        patchIdList = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
        status = ... # type: typing___Text
        ctime = ... # type: builtin___int
        etime = ... # type: builtin___int
        hostname = ... # type: typing___Text
        osVersion = ... # type: typing___Text
        osArchitecture = ... # type: typing___Text
        requireReboot = ... # type: builtin___bool

        @property
        def result(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[GetPatchTaskDetailResponse.TaskResult.Result]: ...

        def __init__(self,
            *,
            result : typing___Optional[typing___Iterable[GetPatchTaskDetailResponse.TaskResult.Result]] = None,
            hostId : typing___Optional[typing___Text] = None,
            hostIp : typing___Optional[typing___Text] = None,
            patchIdList : typing___Optional[typing___Iterable[typing___Text]] = None,
            status : typing___Optional[typing___Text] = None,
            ctime : typing___Optional[builtin___int] = None,
            etime : typing___Optional[builtin___int] = None,
            hostname : typing___Optional[typing___Text] = None,
            osVersion : typing___Optional[typing___Text] = None,
            osArchitecture : typing___Optional[typing___Text] = None,
            requireReboot : typing___Optional[builtin___bool] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> GetPatchTaskDetailResponse.TaskResult: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetPatchTaskDetailResponse.TaskResult: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"ctime",b"ctime",u"etime",b"etime",u"hostId",b"hostId",u"hostIp",b"hostIp",u"hostname",b"hostname",u"osArchitecture",b"osArchitecture",u"osVersion",b"osVersion",u"patchIdList",b"patchIdList",u"requireReboot",b"requireReboot",u"result",b"result",u"status",b"status"]) -> None: ...

    class Request(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        hostId = ... # type: typing___Text
        hostIp = ... # type: typing___Text
        patchIdList = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

        def __init__(self,
            *,
            hostId : typing___Optional[typing___Text] = None,
            hostIp : typing___Optional[typing___Text] = None,
            patchIdList : typing___Optional[typing___Iterable[typing___Text]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> GetPatchTaskDetailResponse.Request: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetPatchTaskDetailResponse.Request: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"hostId",b"hostId",u"hostIp",b"hostIp",u"patchIdList",b"patchIdList"]) -> None: ...

    taskId = ... # type: typing___Text
    creator = ... # type: typing___Text
    ctime = ... # type: builtin___int
    etime = ... # type: builtin___int
    status = ... # type: typing___Text

    @property
    def taskResult(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[GetPatchTaskDetailResponse.TaskResult]: ...

    @property
    def request(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[GetPatchTaskDetailResponse.Request]: ...

    def __init__(self,
        *,
        taskResult : typing___Optional[typing___Iterable[GetPatchTaskDetailResponse.TaskResult]] = None,
        taskId : typing___Optional[typing___Text] = None,
        request : typing___Optional[typing___Iterable[GetPatchTaskDetailResponse.Request]] = None,
        creator : typing___Optional[typing___Text] = None,
        ctime : typing___Optional[builtin___int] = None,
        etime : typing___Optional[builtin___int] = None,
        status : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetPatchTaskDetailResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetPatchTaskDetailResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"creator",b"creator",u"ctime",b"ctime",u"etime",b"etime",u"request",b"request",u"status",b"status",u"taskId",b"taskId",u"taskResult",b"taskResult"]) -> None: ...

class GetPatchTaskDetailResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> GetPatchTaskDetailResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[GetPatchTaskDetailResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetPatchTaskDetailResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetPatchTaskDetailResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
