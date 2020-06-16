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

from google.protobuf.struct_pb2 import (
    Struct as google___protobuf___struct_pb2___Struct,
    Value as google___protobuf___struct_pb2___Value,
)

from tool_sdk.model.tool.tool_input_pb2 import (
    ToolInput as tool_sdk___model___tool___tool_input_pb2___ToolInput,
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


class ExecuteDebugToolRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class OutputDefs(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        id = ... # type: typing___Text
        name = ... # type: typing___Text

        def __init__(self,
            *,
            id : typing___Optional[typing___Text] = None,
            name : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> ExecuteDebugToolRequest.OutputDefs: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ExecuteDebugToolRequest.OutputDefs: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id",u"name",b"name"]) -> None: ...

    class TableDefs(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class Dimensions(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            id = ... # type: typing___Text
            name = ... # type: typing___Text

            def __init__(self,
                *,
                id : typing___Optional[typing___Text] = None,
                name : typing___Optional[typing___Text] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> ExecuteDebugToolRequest.TableDefs.Dimensions: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ExecuteDebugToolRequest.TableDefs.Dimensions: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id",u"name",b"name"]) -> None: ...

        class Columns(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            id = ... # type: typing___Text
            name = ... # type: typing___Text

            def __init__(self,
                *,
                id : typing___Optional[typing___Text] = None,
                name : typing___Optional[typing___Text] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> ExecuteDebugToolRequest.TableDefs.Columns: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ExecuteDebugToolRequest.TableDefs.Columns: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id",u"name",b"name"]) -> None: ...

        id = ... # type: typing___Text
        name = ... # type: typing___Text

        @property
        def dimensions(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ExecuteDebugToolRequest.TableDefs.Dimensions]: ...

        @property
        def columns(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ExecuteDebugToolRequest.TableDefs.Columns]: ...

        def __init__(self,
            *,
            id : typing___Optional[typing___Text] = None,
            name : typing___Optional[typing___Text] = None,
            dimensions : typing___Optional[typing___Iterable[ExecuteDebugToolRequest.TableDefs.Dimensions]] = None,
            columns : typing___Optional[typing___Iterable[ExecuteDebugToolRequest.TableDefs.Columns]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> ExecuteDebugToolRequest.TableDefs: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ExecuteDebugToolRequest.TableDefs: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"columns",b"columns",u"dimensions",b"dimensions",u"id",b"id",u"name",b"name"]) -> None: ...

    content = ... # type: typing___Text
    type = ... # type: typing___Text
    execUser = ... # type: typing___Text
    whiteList = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    blackList = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    sandboxRun = ... # type: builtin___bool
    windowsSession = ... # type: builtin___bool
    subscribers = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    needNotify = ... # type: typing___Text

    @property
    def inputs_info(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[tool_sdk___model___tool___tool_input_pb2___ToolInput]: ...

    @property
    def inputs(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def outputs(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def toolOutputs(self) -> google___protobuf___struct_pb2___Value: ...

    @property
    def outputDefs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ExecuteDebugToolRequest.OutputDefs]: ...

    @property
    def tableDefs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ExecuteDebugToolRequest.TableDefs]: ...

    @property
    def toolEnv(self) -> google___protobuf___struct_pb2___Struct: ...

    def __init__(self,
        *,
        inputs_info : typing___Optional[typing___Iterable[tool_sdk___model___tool___tool_input_pb2___ToolInput]] = None,
        content : typing___Optional[typing___Text] = None,
        type : typing___Optional[typing___Text] = None,
        inputs : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        outputs : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        execUser : typing___Optional[typing___Text] = None,
        whiteList : typing___Optional[typing___Iterable[typing___Text]] = None,
        blackList : typing___Optional[typing___Iterable[typing___Text]] = None,
        toolOutputs : typing___Optional[google___protobuf___struct_pb2___Value] = None,
        outputDefs : typing___Optional[typing___Iterable[ExecuteDebugToolRequest.OutputDefs]] = None,
        tableDefs : typing___Optional[typing___Iterable[ExecuteDebugToolRequest.TableDefs]] = None,
        sandboxRun : typing___Optional[builtin___bool] = None,
        windowsSession : typing___Optional[builtin___bool] = None,
        subscribers : typing___Optional[typing___Iterable[typing___Text]] = None,
        needNotify : typing___Optional[typing___Text] = None,
        toolEnv : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ExecuteDebugToolRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ExecuteDebugToolRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"inputs",b"inputs",u"outputs",b"outputs",u"toolEnv",b"toolEnv",u"toolOutputs",b"toolOutputs"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"blackList",b"blackList",u"content",b"content",u"execUser",b"execUser",u"inputs",b"inputs",u"inputs_info",b"inputs_info",u"needNotify",b"needNotify",u"outputDefs",b"outputDefs",u"outputs",b"outputs",u"sandboxRun",b"sandboxRun",u"subscribers",b"subscribers",u"tableDefs",b"tableDefs",u"toolEnv",b"toolEnv",u"toolOutputs",b"toolOutputs",u"type",b"type",u"whiteList",b"whiteList",u"windowsSession",b"windowsSession"]) -> None: ...

class ExecuteDebugToolResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    execId = ... # type: typing___Text

    def __init__(self,
        *,
        execId : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ExecuteDebugToolResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ExecuteDebugToolResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"execId",b"execId"]) -> None: ...

class ExecuteDebugToolResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> ExecuteDebugToolResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[ExecuteDebugToolResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ExecuteDebugToolResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ExecuteDebugToolResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...