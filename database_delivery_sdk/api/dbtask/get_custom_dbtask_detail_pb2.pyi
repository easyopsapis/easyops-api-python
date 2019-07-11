# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
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
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class GetCustomDBTaskDetailRequest(google___protobuf___message___Message):
    dbTaskId = ... # type: typing___Text

    def __init__(self,
        dbTaskId : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetCustomDBTaskDetailRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"dbTaskId"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"dbTaskId"]) -> None: ...

class GetCustomDBTaskDetailResponse(google___protobuf___message___Message):
    class ChangeTask(google___protobuf___message___Message):
        class Result(google___protobuf___message___Message):
            isSkip = ... # type: int
            isRollback = ... # type: int
            id = ... # type: typing___Text
            name = ... # type: typing___Text
            author = ... # type: typing___Text
            otherAttr = ... # type: typing___Text
            updateSql = ... # type: typing___Text
            rollbackSql = ... # type: typing___Text
            status = ... # type: typing___Text
            msg = ... # type: typing___Text
            ctime = ... # type: int
            etime = ... # type: int

            def __init__(self,
                isSkip : typing___Optional[int] = None,
                isRollback : typing___Optional[int] = None,
                id : typing___Optional[typing___Text] = None,
                name : typing___Optional[typing___Text] = None,
                author : typing___Optional[typing___Text] = None,
                otherAttr : typing___Optional[typing___Text] = None,
                updateSql : typing___Optional[typing___Text] = None,
                rollbackSql : typing___Optional[typing___Text] = None,
                status : typing___Optional[typing___Text] = None,
                msg : typing___Optional[typing___Text] = None,
                ctime : typing___Optional[int] = None,
                etime : typing___Optional[int] = None,
                ) -> None: ...
            @classmethod
            def FromString(cls, s: bytes) -> GetCustomDBTaskDetailResponse.ChangeTask.Result: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            if sys.version_info >= (3,):
                def ClearField(self, field_name: typing_extensions___Literal[u"author",u"ctime",u"etime",u"id",u"isRollback",u"isSkip",u"msg",u"name",u"otherAttr",u"rollbackSql",u"status",u"updateSql"]) -> None: ...
            else:
                def ClearField(self, field_name: typing_extensions___Literal[b"author",b"ctime",b"etime",b"id",b"isRollback",b"isSkip",b"msg",b"name",b"otherAttr",b"rollbackSql",b"status",b"updateSql"]) -> None: ...

        entityTaskId = ... # type: typing___Text
        dbInstanceId = ... # type: typing___Text
        dbInstanceName = ... # type: typing___Text

        @property
        def result(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[GetCustomDBTaskDetailResponse.ChangeTask.Result]: ...

        def __init__(self,
            entityTaskId : typing___Optional[typing___Text] = None,
            dbInstanceId : typing___Optional[typing___Text] = None,
            dbInstanceName : typing___Optional[typing___Text] = None,
            result : typing___Optional[typing___Iterable[GetCustomDBTaskDetailResponse.ChangeTask.Result]] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> GetCustomDBTaskDetailResponse.ChangeTask: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"dbInstanceId",u"dbInstanceName",u"entityTaskId",u"result"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[b"dbInstanceId",b"dbInstanceName",b"entityTaskId",b"result"]) -> None: ...

    id = ... # type: typing___Text
    state = ... # type: typing___Text
    creator = ... # type: typing___Text
    dbServiceId = ... # type: typing___Text
    dbServiceName = ... # type: typing___Text
    status = ... # type: typing___Text
    ctime = ... # type: int
    etime = ... # type: int

    @property
    def changeTask(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[GetCustomDBTaskDetailResponse.ChangeTask]: ...

    def __init__(self,
        id : typing___Optional[typing___Text] = None,
        state : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        dbServiceId : typing___Optional[typing___Text] = None,
        dbServiceName : typing___Optional[typing___Text] = None,
        changeTask : typing___Optional[typing___Iterable[GetCustomDBTaskDetailResponse.ChangeTask]] = None,
        status : typing___Optional[typing___Text] = None,
        ctime : typing___Optional[int] = None,
        etime : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetCustomDBTaskDetailResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"changeTask",u"creator",u"ctime",u"dbServiceId",u"dbServiceName",u"etime",u"id",u"state",u"status"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"changeTask",b"creator",b"ctime",b"dbServiceId",b"dbServiceName",b"etime",b"id",b"state",b"status"]) -> None: ...

class GetCustomDBTaskDetailResponseWrapper(google___protobuf___message___Message):
    code = ... # type: int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> GetCustomDBTaskDetailResponse: ...

    def __init__(self,
        code : typing___Optional[int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[GetCustomDBTaskDetailResponse] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetCustomDBTaskDetailResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"code",u"codeExplain",u"data",u"error"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"code",b"codeExplain",b"data",b"error"]) -> None: ...