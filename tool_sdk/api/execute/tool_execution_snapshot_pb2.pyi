# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
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

from tool_sdk.model.tool.execution_snapshot_pb2 import (
    ExecutionSnapshot as tool_sdk___model___tool___execution_snapshot_pb2___ExecutionSnapshot,
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


class ToolExecutionSnapshotRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    toolId = ... # type: typing___Text
    vId = ... # type: typing___Text
    agents = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    execUser = ... # type: typing___Text
    timeout = ... # type: builtin___int
    name = ... # type: typing___Text
    needNotify = ... # type: typing___Text

    @property
    def callback(self) -> tool_sdk___model___tool___callback_pb2___Callback: ...

    @property
    def inputs(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def toolEnv(self) -> google___protobuf___struct_pb2___Struct: ...

    def __init__(self,
        *,
        callback : typing___Optional[tool_sdk___model___tool___callback_pb2___Callback] = None,
        toolId : typing___Optional[typing___Text] = None,
        vId : typing___Optional[typing___Text] = None,
        agents : typing___Optional[typing___Iterable[typing___Text]] = None,
        inputs : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        execUser : typing___Optional[typing___Text] = None,
        toolEnv : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        timeout : typing___Optional[builtin___int] = None,
        name : typing___Optional[typing___Text] = None,
        needNotify : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ToolExecutionSnapshotRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ToolExecutionSnapshotRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"callback",b"callback",u"inputs",b"inputs",u"toolEnv",b"toolEnv"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"agents",b"agents",u"callback",b"callback",u"execUser",b"execUser",u"inputs",b"inputs",u"name",b"name",u"needNotify",b"needNotify",u"timeout",b"timeout",u"toolEnv",b"toolEnv",u"toolId",b"toolId",u"vId",b"vId"]) -> None: ...

class ToolExecutionSnapshotResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> tool_sdk___model___tool___execution_snapshot_pb2___ExecutionSnapshot: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[tool_sdk___model___tool___execution_snapshot_pb2___ExecutionSnapshot] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ToolExecutionSnapshotResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ToolExecutionSnapshotResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
