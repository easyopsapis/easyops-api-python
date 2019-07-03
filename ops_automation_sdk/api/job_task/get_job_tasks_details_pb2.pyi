# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.internal.containers import (
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from model.ops_automation.mail_info_pb2 import (
    MailInfo as model___ops_automation___mail_info_pb2___MailInfo,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class GetJobTasksDetailRequest(google___protobuf___message___Message):
    jobTaskId = ... # type: typing___Text

    def __init__(self,
        jobTaskId : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetJobTasksDetailRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"jobTaskId"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"jobTaskId"]) -> None: ...

class GetJobTasksDetailResponse(google___protobuf___message___Message):
    jobName = ... # type: typing___Text
    menuName = ... # type: typing___Text
    execId = ... # type: typing___Text
    resourceType = ... # type: typing___Text
    resourceId = ... # type: typing___Text
    resourceVId = ... # type: typing___Text
    resourceVName = ... # type: typing___Text
    hosts = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    createTime = ... # type: typing___Text
    updateTime = ... # type: typing___Text
    creator = ... # type: typing___Text
    org = ... # type: int
    id = ... # type: typing___Text
    jobId = ... # type: typing___Text
    trigger = ... # type: typing___Text
    execUser = ... # type: typing___Text
    status = ... # type: typing___Text
    successRate = ... # type: float
    error = ... # type: typing___Text

    @property
    def mail(self) -> model___ops_automation___mail_info_pb2___MailInfo: ...

    def __init__(self,
        jobName : typing___Optional[typing___Text] = None,
        menuName : typing___Optional[typing___Text] = None,
        execId : typing___Optional[typing___Text] = None,
        resourceType : typing___Optional[typing___Text] = None,
        resourceId : typing___Optional[typing___Text] = None,
        resourceVId : typing___Optional[typing___Text] = None,
        resourceVName : typing___Optional[typing___Text] = None,
        hosts : typing___Optional[typing___Iterable[typing___Text]] = None,
        mail : typing___Optional[model___ops_automation___mail_info_pb2___MailInfo] = None,
        createTime : typing___Optional[typing___Text] = None,
        updateTime : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        org : typing___Optional[int] = None,
        id : typing___Optional[typing___Text] = None,
        jobId : typing___Optional[typing___Text] = None,
        trigger : typing___Optional[typing___Text] = None,
        execUser : typing___Optional[typing___Text] = None,
        status : typing___Optional[typing___Text] = None,
        successRate : typing___Optional[float] = None,
        error : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetJobTasksDetailResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"mail"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"createTime",u"creator",u"error",u"execId",u"execUser",u"hosts",u"id",u"jobId",u"jobName",u"mail",u"menuName",u"org",u"resourceId",u"resourceType",u"resourceVId",u"resourceVName",u"status",u"successRate",u"trigger",u"updateTime"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"mail",b"mail"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"createTime",b"creator",b"error",b"execId",b"execUser",b"hosts",b"id",b"jobId",b"jobName",b"mail",b"menuName",b"org",b"resourceId",b"resourceType",b"resourceVId",b"resourceVName",b"status",b"successRate",b"trigger",b"updateTime"]) -> None: ...

class GetJobTasksDetailResponseWrapper(google___protobuf___message___Message):
    code = ... # type: int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> GetJobTasksDetailResponse: ...

    def __init__(self,
        code : typing___Optional[int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[GetJobTasksDetailResponse] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetJobTasksDetailResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"code",u"codeExplain",u"data",u"error"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"code",b"codeExplain",b"data",b"error"]) -> None: ...