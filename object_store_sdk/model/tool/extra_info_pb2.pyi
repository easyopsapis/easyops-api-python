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

from object_store_sdk.model.tool.callback_pb2 import (
    Callback as object_store_sdk___model___tool___callback_pb2___Callback,
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


class ExtraInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Detail(google___protobuf___message___Message):
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
                def FromString(cls, s: builtin___bytes) -> ExtraInfo.Detail.OutputDefs: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ExtraInfo.Detail.OutputDefs: ...
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
                    def FromString(cls, s: builtin___bytes) -> ExtraInfo.Detail.TableDefs.Dimensions: ...
                else:
                    @classmethod
                    def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ExtraInfo.Detail.TableDefs.Dimensions: ...
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
                    def FromString(cls, s: builtin___bytes) -> ExtraInfo.Detail.TableDefs.Columns: ...
                else:
                    @classmethod
                    def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ExtraInfo.Detail.TableDefs.Columns: ...
                def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
                def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
                def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id",u"name",b"name"]) -> None: ...

            id = ... # type: typing___Text
            name = ... # type: typing___Text

            @property
            def dimensions(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ExtraInfo.Detail.TableDefs.Dimensions]: ...

            @property
            def columns(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ExtraInfo.Detail.TableDefs.Columns]: ...

            def __init__(self,
                *,
                id : typing___Optional[typing___Text] = None,
                name : typing___Optional[typing___Text] = None,
                dimensions : typing___Optional[typing___Iterable[ExtraInfo.Detail.TableDefs.Dimensions]] = None,
                columns : typing___Optional[typing___Iterable[ExtraInfo.Detail.TableDefs.Columns]] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> ExtraInfo.Detail.TableDefs: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ExtraInfo.Detail.TableDefs: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"columns",b"columns",u"dimensions",b"dimensions",u"id",b"id",u"name",b"name"]) -> None: ...

        subscribers = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

        @property
        def callback(self) -> object_store_sdk___model___tool___callback_pb2___Callback: ...

        @property
        def toolOutputs(self) -> google___protobuf___struct_pb2___Value: ...

        @property
        def toolEnv(self) -> google___protobuf___struct_pb2___Struct: ...

        @property
        def outputDefs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ExtraInfo.Detail.OutputDefs]: ...

        @property
        def tableDefs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ExtraInfo.Detail.TableDefs]: ...

        def __init__(self,
            *,
            callback : typing___Optional[object_store_sdk___model___tool___callback_pb2___Callback] = None,
            toolOutputs : typing___Optional[google___protobuf___struct_pb2___Value] = None,
            toolEnv : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
            outputDefs : typing___Optional[typing___Iterable[ExtraInfo.Detail.OutputDefs]] = None,
            tableDefs : typing___Optional[typing___Iterable[ExtraInfo.Detail.TableDefs]] = None,
            subscribers : typing___Optional[typing___Iterable[typing___Text]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> ExtraInfo.Detail: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ExtraInfo.Detail: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"callback",b"callback",u"toolEnv",b"toolEnv",u"toolOutputs",b"toolOutputs"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"callback",b"callback",u"outputDefs",b"outputDefs",u"subscribers",b"subscribers",u"tableDefs",b"tableDefs",u"toolEnv",b"toolEnv",u"toolOutputs",b"toolOutputs"]) -> None: ...

    toolName = ... # type: typing___Text
    execMode = ... # type: typing___Text
    outputs = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    origin = ... # type: typing___Text
    trigger = ... # type: typing___Text
    toolId = ... # type: typing___Text
    execUser = ... # type: typing___Text

    @property
    def detail(self) -> ExtraInfo.Detail: ...

    @property
    def inputs(self) -> google___protobuf___struct_pb2___Struct: ...

    def __init__(self,
        *,
        toolName : typing___Optional[typing___Text] = None,
        execMode : typing___Optional[typing___Text] = None,
        outputs : typing___Optional[typing___Iterable[typing___Text]] = None,
        origin : typing___Optional[typing___Text] = None,
        trigger : typing___Optional[typing___Text] = None,
        detail : typing___Optional[ExtraInfo.Detail] = None,
        toolId : typing___Optional[typing___Text] = None,
        execUser : typing___Optional[typing___Text] = None,
        inputs : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ExtraInfo: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ExtraInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"detail",b"detail",u"inputs",b"inputs"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"detail",b"detail",u"execMode",b"execMode",u"execUser",b"execUser",u"inputs",b"inputs",u"origin",b"origin",u"outputs",b"outputs",u"toolId",b"toolId",u"toolName",b"toolName",u"trigger",b"trigger"]) -> None: ...
