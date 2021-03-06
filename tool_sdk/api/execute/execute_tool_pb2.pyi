# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.struct_pb2 import (
    Struct as google___protobuf___struct_pb2___Struct,
)

from tool_sdk.model.tool.callback_pb2 import (
    Callback as tool_sdk___model___tool___callback_pb2___Callback,
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


class ExecuteToolRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Metadata(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        origin = ... # type: typing___Text

        def __init__(self,
            *,
            origin : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> ExecuteToolRequest.Metadata: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ExecuteToolRequest.Metadata: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"origin",b"origin"]) -> None: ...

    class Log(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        enabled = ... # type: builtin___bool
        level = ... # type: typing___Text

        def __init__(self,
            *,
            enabled : typing___Optional[builtin___bool] = None,
            level : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> ExecuteToolRequest.Log: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ExecuteToolRequest.Log: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"enabled",b"enabled",u"level",b"level"]) -> None: ...

    needNotify = ... # type: typing___Text
    name = ... # type: typing___Text
    toolId = ... # type: typing___Text
    vId = ... # type: typing___Text
    execUser = ... # type: typing___Text
    timeout = ... # type: builtin___int
    ansibleNodeExecUser = ... # type: typing___Text

    @property
    def inputs(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def callback(self) -> tool_sdk___model___tool___callback_pb2___Callback: ...

    @property
    def metadata(self) -> ExecuteToolRequest.Metadata: ...

    @property
    def log(self) -> ExecuteToolRequest.Log: ...

    def __init__(self,
        *,
        inputs : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        callback : typing___Optional[tool_sdk___model___tool___callback_pb2___Callback] = None,
        needNotify : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        metadata : typing___Optional[ExecuteToolRequest.Metadata] = None,
        toolId : typing___Optional[typing___Text] = None,
        vId : typing___Optional[typing___Text] = None,
        execUser : typing___Optional[typing___Text] = None,
        timeout : typing___Optional[builtin___int] = None,
        log : typing___Optional[ExecuteToolRequest.Log] = None,
        ansibleNodeExecUser : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ExecuteToolRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ExecuteToolRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"callback",b"callback",u"inputs",b"inputs",u"log",b"log",u"metadata",b"metadata"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"ansibleNodeExecUser",b"ansibleNodeExecUser",u"callback",b"callback",u"execUser",b"execUser",u"inputs",b"inputs",u"log",b"log",u"metadata",b"metadata",u"name",b"name",u"needNotify",b"needNotify",u"timeout",b"timeout",u"toolId",b"toolId",u"vId",b"vId"]) -> None: ...

class ExecuteToolResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    execId = ... # type: typing___Text

    def __init__(self,
        *,
        execId : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ExecuteToolResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ExecuteToolResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"execId",b"execId"]) -> None: ...

class ExecuteToolResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> ExecuteToolResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[ExecuteToolResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ExecuteToolResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ExecuteToolResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
