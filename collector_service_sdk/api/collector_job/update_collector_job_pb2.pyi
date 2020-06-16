# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
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


class UpdateCollectorJobRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class CollectTime(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        startTime = ... # type: typing___Text
        endTime = ... # type: typing___Text

        def __init__(self,
            *,
            startTime : typing___Optional[typing___Text] = None,
            endTime : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> UpdateCollectorJobRequest.CollectTime: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> UpdateCollectorJobRequest.CollectTime: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"endTime",b"endTime",u"startTime",b"startTime"]) -> None: ...

    collectorTemplateId = ... # type: typing___Text
    instanceId = ... # type: typing___Text
    objectId = ... # type: typing___Text
    jobName = ... # type: typing___Text
    filter = ... # type: typing___Text
    timeout = ... # type: builtin___int
    enabled = ... # type: builtin___bool
    interval = ... # type: builtin___int
    path = ... # type: typing___Text
    pathId = ... # type: typing___Text

    @property
    def collectTime(self) -> UpdateCollectorJobRequest.CollectTime: ...

    def __init__(self,
        *,
        collectorTemplateId : typing___Optional[typing___Text] = None,
        instanceId : typing___Optional[typing___Text] = None,
        objectId : typing___Optional[typing___Text] = None,
        jobName : typing___Optional[typing___Text] = None,
        filter : typing___Optional[typing___Text] = None,
        collectTime : typing___Optional[UpdateCollectorJobRequest.CollectTime] = None,
        timeout : typing___Optional[builtin___int] = None,
        enabled : typing___Optional[builtin___bool] = None,
        interval : typing___Optional[builtin___int] = None,
        path : typing___Optional[typing___Text] = None,
        pathId : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> UpdateCollectorJobRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> UpdateCollectorJobRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"collectTime",b"collectTime"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"collectTime",b"collectTime",u"collectorTemplateId",b"collectorTemplateId",u"enabled",b"enabled",u"filter",b"filter",u"instanceId",b"instanceId",u"interval",b"interval",u"jobName",b"jobName",u"objectId",b"objectId",u"path",b"path",u"pathId",b"pathId",u"timeout",b"timeout"]) -> None: ...

class UpdateCollectorJobResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    instanceId = ... # type: typing___Text

    def __init__(self,
        *,
        instanceId : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> UpdateCollectorJobResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> UpdateCollectorJobResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"instanceId",b"instanceId"]) -> None: ...

class UpdateCollectorJobResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> UpdateCollectorJobResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[UpdateCollectorJobResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> UpdateCollectorJobResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> UpdateCollectorJobResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
