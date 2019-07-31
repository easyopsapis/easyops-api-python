# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.struct_pb2 import (
    Struct as google___protobuf___struct_pb2___Struct,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class JobTasksToolCallbackRequest(google___protobuf___message___Message):
    execId = ... # type: typing___Text
    totalStatus = ... # type: typing___Text

    @property
    def status(self) -> google___protobuf___struct_pb2___Struct: ...

    def __init__(self,
        execId : typing___Optional[typing___Text] = None,
        status : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        totalStatus : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> JobTasksToolCallbackRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"status"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"execId",u"status",u"totalStatus"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"status",b"status"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"execId",b"status",b"totalStatus"]) -> None: ...

class JobTasksToolCallbackResponse(google___protobuf___message___Message):
    jobTasksId = ... # type: typing___Text

    def __init__(self,
        jobTasksId : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> JobTasksToolCallbackResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"jobTasksId"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"jobTasksId"]) -> None: ...

class JobTasksToolCallbackResponseWrapper(google___protobuf___message___Message):
    code = ... # type: int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> JobTasksToolCallbackResponse: ...

    def __init__(self,
        code : typing___Optional[int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[JobTasksToolCallbackResponse] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> JobTasksToolCallbackResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"code",u"codeExplain",u"data",u"error"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"code",b"codeExplain",b"data",b"error"]) -> None: ...
