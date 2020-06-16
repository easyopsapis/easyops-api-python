# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from api_gateway_sdk.model.ops_automation.mail_info_pb2 import (
    MailInfo as api_gateway_sdk___model___ops_automation___mail_info_pb2___MailInfo,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
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


class JobTasks(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    id = ... # type: typing___Text
    jobId = ... # type: typing___Text
    jobName = ... # type: typing___Text
    menuName = ... # type: typing___Text
    execId = ... # type: typing___Text
    resourceType = ... # type: typing___Text
    resourceId = ... # type: typing___Text
    resourceVId = ... # type: typing___Text
    resourceVName = ... # type: typing___Text
    trigger = ... # type: typing___Text
    execUser = ... # type: typing___Text
    hosts = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    status = ... # type: typing___Text
    successRate = ... # type: builtin___float
    error = ... # type: typing___Text
    createTime = ... # type: typing___Text
    updateTime = ... # type: typing___Text
    creator = ... # type: typing___Text
    org = ... # type: builtin___int

    @property
    def mail(self) -> api_gateway_sdk___model___ops_automation___mail_info_pb2___MailInfo: ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        jobId : typing___Optional[typing___Text] = None,
        jobName : typing___Optional[typing___Text] = None,
        menuName : typing___Optional[typing___Text] = None,
        execId : typing___Optional[typing___Text] = None,
        resourceType : typing___Optional[typing___Text] = None,
        resourceId : typing___Optional[typing___Text] = None,
        resourceVId : typing___Optional[typing___Text] = None,
        resourceVName : typing___Optional[typing___Text] = None,
        trigger : typing___Optional[typing___Text] = None,
        execUser : typing___Optional[typing___Text] = None,
        hosts : typing___Optional[typing___Iterable[typing___Text]] = None,
        status : typing___Optional[typing___Text] = None,
        mail : typing___Optional[api_gateway_sdk___model___ops_automation___mail_info_pb2___MailInfo] = None,
        successRate : typing___Optional[builtin___float] = None,
        error : typing___Optional[typing___Text] = None,
        createTime : typing___Optional[typing___Text] = None,
        updateTime : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        org : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> JobTasks: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> JobTasks: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"mail",b"mail"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"createTime",b"createTime",u"creator",b"creator",u"error",b"error",u"execId",b"execId",u"execUser",b"execUser",u"hosts",b"hosts",u"id",b"id",u"jobId",b"jobId",u"jobName",b"jobName",u"mail",b"mail",u"menuName",b"menuName",u"org",b"org",u"resourceId",b"resourceId",u"resourceType",b"resourceType",u"resourceVId",b"resourceVId",u"resourceVName",b"resourceVName",u"status",b"status",u"successRate",b"successRate",u"trigger",b"trigger",u"updateTime",b"updateTime"]) -> None: ...
