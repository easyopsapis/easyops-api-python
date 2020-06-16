# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from alert_service_sdk.model.tool.callback_pb2 import (
    Callback as alert_service_sdk___model___tool___callback_pb2___Callback,
)

from alert_service_sdk.model.tool.tool_pb2 import (
    Tool as alert_service_sdk___model___tool___tool_pb2___Tool,
)

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


class ToolTask(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class ExtraDetail(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
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
                    def FromString(cls, s: builtin___bytes) -> ToolTask.ExtraDetail.TableDefs.Dimensions: ...
                else:
                    @classmethod
                    def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ToolTask.ExtraDetail.TableDefs.Dimensions: ...
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
                    def FromString(cls, s: builtin___bytes) -> ToolTask.ExtraDetail.TableDefs.Columns: ...
                else:
                    @classmethod
                    def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ToolTask.ExtraDetail.TableDefs.Columns: ...
                def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
                def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
                def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id",u"name",b"name"]) -> None: ...

            id = ... # type: typing___Text
            name = ... # type: typing___Text

            @property
            def dimensions(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ToolTask.ExtraDetail.TableDefs.Dimensions]: ...

            @property
            def columns(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ToolTask.ExtraDetail.TableDefs.Columns]: ...

            def __init__(self,
                *,
                id : typing___Optional[typing___Text] = None,
                name : typing___Optional[typing___Text] = None,
                dimensions : typing___Optional[typing___Iterable[ToolTask.ExtraDetail.TableDefs.Dimensions]] = None,
                columns : typing___Optional[typing___Iterable[ToolTask.ExtraDetail.TableDefs.Columns]] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> ToolTask.ExtraDetail.TableDefs: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ToolTask.ExtraDetail.TableDefs: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"columns",b"columns",u"dimensions",b"dimensions",u"id",b"id",u"name",b"name"]) -> None: ...

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
                def FromString(cls, s: builtin___bytes) -> ToolTask.ExtraDetail.OutputDefs: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ToolTask.ExtraDetail.OutputDefs: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id",u"name",b"name"]) -> None: ...


        @property
        def callback(self) -> alert_service_sdk___model___tool___callback_pb2___Callback: ...

        @property
        def toolEnv(self) -> google___protobuf___struct_pb2___Struct: ...

        @property
        def toolOutputs(self) -> google___protobuf___struct_pb2___Value: ...

        @property
        def tableDefs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ToolTask.ExtraDetail.TableDefs]: ...

        @property
        def outputDefs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ToolTask.ExtraDetail.OutputDefs]: ...

        def __init__(self,
            *,
            callback : typing___Optional[alert_service_sdk___model___tool___callback_pb2___Callback] = None,
            toolEnv : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
            toolOutputs : typing___Optional[google___protobuf___struct_pb2___Value] = None,
            tableDefs : typing___Optional[typing___Iterable[ToolTask.ExtraDetail.TableDefs]] = None,
            outputDefs : typing___Optional[typing___Iterable[ToolTask.ExtraDetail.OutputDefs]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> ToolTask.ExtraDetail: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ToolTask.ExtraDetail: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"callback",b"callback",u"toolEnv",b"toolEnv",u"toolOutputs",b"toolOutputs"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"callback",b"callback",u"outputDefs",b"outputDefs",u"tableDefs",b"tableDefs",u"toolEnv",b"toolEnv",u"toolOutputs",b"toolOutputs"]) -> None: ...

    class BatchStrategy(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        batchNum = ... # type: builtin___int
        batchInterval = ... # type: builtin___int
        failedStop = ... # type: builtin___bool

        def __init__(self,
            *,
            batchNum : typing___Optional[builtin___int] = None,
            batchInterval : typing___Optional[builtin___int] = None,
            failedStop : typing___Optional[builtin___bool] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> ToolTask.BatchStrategy: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ToolTask.BatchStrategy: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"batchInterval",b"batchInterval",u"batchNum",b"batchNum",u"failedStop",b"failedStop"]) -> None: ...

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
            def FromString(cls, s: builtin___bytes) -> ToolTask.OutputDefs: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ToolTask.OutputDefs: ...
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
                def FromString(cls, s: builtin___bytes) -> ToolTask.TableDefs.Dimensions: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ToolTask.TableDefs.Dimensions: ...
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
                def FromString(cls, s: builtin___bytes) -> ToolTask.TableDefs.Columns: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ToolTask.TableDefs.Columns: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id",u"name",b"name"]) -> None: ...

        id = ... # type: typing___Text
        name = ... # type: typing___Text

        @property
        def dimensions(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ToolTask.TableDefs.Dimensions]: ...

        @property
        def columns(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ToolTask.TableDefs.Columns]: ...

        def __init__(self,
            *,
            id : typing___Optional[typing___Text] = None,
            name : typing___Optional[typing___Text] = None,
            dimensions : typing___Optional[typing___Iterable[ToolTask.TableDefs.Dimensions]] = None,
            columns : typing___Optional[typing___Iterable[ToolTask.TableDefs.Columns]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> ToolTask.TableDefs: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ToolTask.TableDefs: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"columns",b"columns",u"dimensions",b"dimensions",u"id",b"id",u"name",b"name"]) -> None: ...

    username = ... # type: typing___Text
    totalStatus = ... # type: typing___Text
    error = ... # type: typing___Text
    execId = ... # type: typing___Text
    agents = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    needNotify = ... # type: typing___Text
    execUser = ... # type: typing___Text
    vId = ... # type: typing___Text
    toolId = ... # type: typing___Text

    @property
    def inputs(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def extraDetail(self) -> ToolTask.ExtraDetail: ...

    @property
    def toolEnv(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def outputs(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def outViewData(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def agentData(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def startTime(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def status(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def msg(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def endTime(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def exitStatus(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def sysStatus(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def toolOutputsData(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___protobuf___struct_pb2___Struct]: ...

    @property
    def tableData(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def toolData(self) -> alert_service_sdk___model___tool___tool_pb2___Tool: ...

    @property
    def batchStrategy(self) -> ToolTask.BatchStrategy: ...

    @property
    def outputDefs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ToolTask.OutputDefs]: ...

    @property
    def tableDefs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ToolTask.TableDefs]: ...

    @property
    def toolOutputs(self) -> google___protobuf___struct_pb2___Value: ...

    def __init__(self,
        *,
        username : typing___Optional[typing___Text] = None,
        inputs : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        extraDetail : typing___Optional[ToolTask.ExtraDetail] = None,
        totalStatus : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        execId : typing___Optional[typing___Text] = None,
        toolEnv : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        outputs : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        outViewData : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        agentData : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        agents : typing___Optional[typing___Iterable[typing___Text]] = None,
        startTime : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        status : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        msg : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        endTime : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        exitStatus : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        sysStatus : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        toolOutputsData : typing___Optional[typing___Iterable[google___protobuf___struct_pb2___Struct]] = None,
        tableData : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        toolData : typing___Optional[alert_service_sdk___model___tool___tool_pb2___Tool] = None,
        batchStrategy : typing___Optional[ToolTask.BatchStrategy] = None,
        needNotify : typing___Optional[typing___Text] = None,
        execUser : typing___Optional[typing___Text] = None,
        vId : typing___Optional[typing___Text] = None,
        toolId : typing___Optional[typing___Text] = None,
        outputDefs : typing___Optional[typing___Iterable[ToolTask.OutputDefs]] = None,
        tableDefs : typing___Optional[typing___Iterable[ToolTask.TableDefs]] = None,
        toolOutputs : typing___Optional[google___protobuf___struct_pb2___Value] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ToolTask: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ToolTask: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"agentData",b"agentData",u"batchStrategy",b"batchStrategy",u"endTime",b"endTime",u"exitStatus",b"exitStatus",u"extraDetail",b"extraDetail",u"inputs",b"inputs",u"msg",b"msg",u"outViewData",b"outViewData",u"outputs",b"outputs",u"startTime",b"startTime",u"status",b"status",u"sysStatus",b"sysStatus",u"tableData",b"tableData",u"toolData",b"toolData",u"toolEnv",b"toolEnv",u"toolOutputs",b"toolOutputs"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"agentData",b"agentData",u"agents",b"agents",u"batchStrategy",b"batchStrategy",u"endTime",b"endTime",u"error",b"error",u"execId",b"execId",u"execUser",b"execUser",u"exitStatus",b"exitStatus",u"extraDetail",b"extraDetail",u"inputs",b"inputs",u"msg",b"msg",u"needNotify",b"needNotify",u"outViewData",b"outViewData",u"outputDefs",b"outputDefs",u"outputs",b"outputs",u"startTime",b"startTime",u"status",b"status",u"sysStatus",b"sysStatus",u"tableData",b"tableData",u"tableDefs",b"tableDefs",u"toolData",b"toolData",u"toolEnv",b"toolEnv",u"toolId",b"toolId",u"toolOutputs",b"toolOutputs",u"toolOutputsData",b"toolOutputsData",u"totalStatus",b"totalStatus",u"username",b"username",u"vId",b"vId"]) -> None: ...
