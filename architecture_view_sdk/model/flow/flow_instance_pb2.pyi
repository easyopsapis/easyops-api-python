# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from architecture_view_sdk.model.flow.flow_execute_step_pb2 import (
    FlowExecuteStep as architecture_view_sdk___model___flow___flow_execute_step_pb2___FlowExecuteStep,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
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


class FlowInstance(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Metadata(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        type = ... # type: typing___Text
        desc = ... # type: typing___Text

        def __init__(self,
            *,
            type : typing___Optional[typing___Text] = None,
            desc : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> FlowInstance.Metadata: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> FlowInstance.Metadata: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"desc",b"desc",u"type",b"type"]) -> None: ...

    class FlowOutputs(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class Columns(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            type = ... # type: typing___Text
            id = ... # type: typing___Text
            name = ... # type: typing___Text

            def __init__(self,
                *,
                type : typing___Optional[typing___Text] = None,
                id : typing___Optional[typing___Text] = None,
                name : typing___Optional[typing___Text] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> FlowInstance.FlowOutputs.Columns: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> FlowInstance.FlowOutputs.Columns: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id",u"name",b"name",u"type",b"type"]) -> None: ...


        @property
        def columns(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[FlowInstance.FlowOutputs.Columns]: ...

        def __init__(self,
            *,
            columns : typing___Optional[typing___Iterable[FlowInstance.FlowOutputs.Columns]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> FlowInstance.FlowOutputs: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> FlowInstance.FlowOutputs: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"columns",b"columns"]) -> None: ...

    class OutputDefs(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        type = ... # type: typing___Text
        id = ... # type: typing___Text
        name = ... # type: typing___Text

        def __init__(self,
            *,
            type : typing___Optional[typing___Text] = None,
            id : typing___Optional[typing___Text] = None,
            name : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> FlowInstance.OutputDefs: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> FlowInstance.OutputDefs: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id",u"name",b"name",u"type",b"type"]) -> None: ...

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
                def FromString(cls, s: builtin___bytes) -> FlowInstance.TableDefs.Dimensions: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> FlowInstance.TableDefs.Dimensions: ...
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
                def FromString(cls, s: builtin___bytes) -> FlowInstance.TableDefs.Columns: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> FlowInstance.TableDefs.Columns: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id",u"name",b"name"]) -> None: ...

        id = ... # type: typing___Text
        name = ... # type: typing___Text

        @property
        def dimensions(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[FlowInstance.TableDefs.Dimensions]: ...

        @property
        def columns(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[FlowInstance.TableDefs.Columns]: ...

        def __init__(self,
            *,
            id : typing___Optional[typing___Text] = None,
            name : typing___Optional[typing___Text] = None,
            dimensions : typing___Optional[typing___Iterable[FlowInstance.TableDefs.Dimensions]] = None,
            columns : typing___Optional[typing___Iterable[FlowInstance.TableDefs.Columns]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> FlowInstance.TableDefs: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> FlowInstance.TableDefs: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"columns",b"columns",u"dimensions",b"dimensions",u"id",b"id",u"name",b"name"]) -> None: ...

    taskId = ... # type: typing___Text
    needNotify = ... # type: builtin___bool
    startTime = ... # type: builtin___int
    endTime = ... # type: builtin___int
    currentTime = ... # type: builtin___int
    totalStatus = ... # type: typing___Text
    message = ... # type: typing___Text
    taskCounter = ... # type: builtin___int
    flowId = ... # type: typing___Text
    version = ... # type: builtin___int
    name = ... # type: typing___Text
    org = ... # type: builtin___int
    creator = ... # type: typing___Text
    category = ... # type: typing___Text
    updateTime = ... # type: typing___Text
    createTime = ... # type: typing___Text

    @property
    def stepList(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[architecture_view_sdk___model___flow___flow_execute_step_pb2___FlowExecuteStep]: ...

    @property
    def instanceMap(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___protobuf___struct_pb2___Struct]: ...

    @property
    def outputs(self) -> google___protobuf___struct_pb2___Value: ...

    @property
    def runningSteps(self) -> google___protobuf___struct_pb2___Value: ...

    @property
    def flowOutputsData(self) -> google___protobuf___struct_pb2___Value: ...

    @property
    def tableData(self) -> google___protobuf___struct_pb2___Value: ...

    @property
    def standardOutputs(self) -> google___protobuf___struct_pb2___Value: ...

    @property
    def agentData(self) -> google___protobuf___struct_pb2___Value: ...

    @property
    def flowInputs(self) -> google___protobuf___struct_pb2___Value: ...

    @property
    def flowEnv(self) -> google___protobuf___struct_pb2___Value: ...

    @property
    def metadata(self) -> FlowInstance.Metadata: ...

    @property
    def flowOutputs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[FlowInstance.FlowOutputs]: ...

    @property
    def outputDefs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[FlowInstance.OutputDefs]: ...

    @property
    def tableDefs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[FlowInstance.TableDefs]: ...

    def __init__(self,
        *,
        stepList : typing___Optional[typing___Iterable[architecture_view_sdk___model___flow___flow_execute_step_pb2___FlowExecuteStep]] = None,
        taskId : typing___Optional[typing___Text] = None,
        instanceMap : typing___Optional[typing___Iterable[google___protobuf___struct_pb2___Struct]] = None,
        outputs : typing___Optional[google___protobuf___struct_pb2___Value] = None,
        runningSteps : typing___Optional[google___protobuf___struct_pb2___Value] = None,
        needNotify : typing___Optional[builtin___bool] = None,
        startTime : typing___Optional[builtin___int] = None,
        endTime : typing___Optional[builtin___int] = None,
        currentTime : typing___Optional[builtin___int] = None,
        totalStatus : typing___Optional[typing___Text] = None,
        message : typing___Optional[typing___Text] = None,
        taskCounter : typing___Optional[builtin___int] = None,
        flowOutputsData : typing___Optional[google___protobuf___struct_pb2___Value] = None,
        tableData : typing___Optional[google___protobuf___struct_pb2___Value] = None,
        standardOutputs : typing___Optional[google___protobuf___struct_pb2___Value] = None,
        agentData : typing___Optional[google___protobuf___struct_pb2___Value] = None,
        flowId : typing___Optional[typing___Text] = None,
        version : typing___Optional[builtin___int] = None,
        flowInputs : typing___Optional[google___protobuf___struct_pb2___Value] = None,
        flowEnv : typing___Optional[google___protobuf___struct_pb2___Value] = None,
        metadata : typing___Optional[FlowInstance.Metadata] = None,
        name : typing___Optional[typing___Text] = None,
        org : typing___Optional[builtin___int] = None,
        flowOutputs : typing___Optional[typing___Iterable[FlowInstance.FlowOutputs]] = None,
        outputDefs : typing___Optional[typing___Iterable[FlowInstance.OutputDefs]] = None,
        tableDefs : typing___Optional[typing___Iterable[FlowInstance.TableDefs]] = None,
        creator : typing___Optional[typing___Text] = None,
        category : typing___Optional[typing___Text] = None,
        updateTime : typing___Optional[typing___Text] = None,
        createTime : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> FlowInstance: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> FlowInstance: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"agentData",b"agentData",u"flowEnv",b"flowEnv",u"flowInputs",b"flowInputs",u"flowOutputsData",b"flowOutputsData",u"metadata",b"metadata",u"outputs",b"outputs",u"runningSteps",b"runningSteps",u"standardOutputs",b"standardOutputs",u"tableData",b"tableData"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"agentData",b"agentData",u"category",b"category",u"createTime",b"createTime",u"creator",b"creator",u"currentTime",b"currentTime",u"endTime",b"endTime",u"flowEnv",b"flowEnv",u"flowId",b"flowId",u"flowInputs",b"flowInputs",u"flowOutputs",b"flowOutputs",u"flowOutputsData",b"flowOutputsData",u"instanceMap",b"instanceMap",u"message",b"message",u"metadata",b"metadata",u"name",b"name",u"needNotify",b"needNotify",u"org",b"org",u"outputDefs",b"outputDefs",u"outputs",b"outputs",u"runningSteps",b"runningSteps",u"standardOutputs",b"standardOutputs",u"startTime",b"startTime",u"stepList",b"stepList",u"tableData",b"tableData",u"tableDefs",b"tableDefs",u"taskCounter",b"taskCounter",u"taskId",b"taskId",u"totalStatus",b"totalStatus",u"updateTime",b"updateTime",u"version",b"version"]) -> None: ...
