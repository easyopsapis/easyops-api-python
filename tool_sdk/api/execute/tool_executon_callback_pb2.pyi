# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from tool_sdk.model.tool.extra_info_pb2 import (
    ExtraInfo as tool_sdk___model___tool___extra_info_pb2___ExtraInfo,
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


class ToolExecutionCallbackRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    taskId = ... # type: typing___Text
    status = ... # type: typing___Text

    @property
    def extraInfo(self) -> tool_sdk___model___tool___extra_info_pb2___ExtraInfo: ...

    def __init__(self,
        *,
        taskId : typing___Optional[typing___Text] = None,
        extraInfo : typing___Optional[tool_sdk___model___tool___extra_info_pb2___ExtraInfo] = None,
        status : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ToolExecutionCallbackRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ToolExecutionCallbackRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"extraInfo",b"extraInfo"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"extraInfo",b"extraInfo",u"status",b"status",u"taskId",b"taskId"]) -> None: ...

class ToolExecutionCallbackResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    taskId = ... # type: typing___Text
    status = ... # type: typing___Text

    @property
    def extraInfo(self) -> tool_sdk___model___tool___extra_info_pb2___ExtraInfo: ...

    def __init__(self,
        *,
        taskId : typing___Optional[typing___Text] = None,
        extraInfo : typing___Optional[tool_sdk___model___tool___extra_info_pb2___ExtraInfo] = None,
        status : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ToolExecutionCallbackResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ToolExecutionCallbackResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"extraInfo",b"extraInfo"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"extraInfo",b"extraInfo",u"status",b"status",u"taskId",b"taskId"]) -> None: ...

class ToolExecutionCallbackResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> ToolExecutionCallbackResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[ToolExecutionCallbackResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ToolExecutionCallbackResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ToolExecutionCallbackResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...