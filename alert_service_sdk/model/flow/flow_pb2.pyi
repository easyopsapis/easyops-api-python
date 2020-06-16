# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from alert_service_sdk.model.flow.flow_step_pb2 import (
    FlowStep as alert_service_sdk___model___flow___flow_step_pb2___FlowStep,
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


class Flow(google___protobuf___message___Message):
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
                def FromString(cls, s: builtin___bytes) -> Flow.TableDefs.Dimensions: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Flow.TableDefs.Dimensions: ...
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
                def FromString(cls, s: builtin___bytes) -> Flow.TableDefs.Columns: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Flow.TableDefs.Columns: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id",u"name",b"name"]) -> None: ...

        id = ... # type: typing___Text
        name = ... # type: typing___Text

        @property
        def dimensions(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Flow.TableDefs.Dimensions]: ...

        @property
        def columns(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Flow.TableDefs.Columns]: ...

        def __init__(self,
            *,
            id : typing___Optional[typing___Text] = None,
            name : typing___Optional[typing___Text] = None,
            dimensions : typing___Optional[typing___Iterable[Flow.TableDefs.Dimensions]] = None,
            columns : typing___Optional[typing___Iterable[Flow.TableDefs.Columns]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Flow.TableDefs: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Flow.TableDefs: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"columns",b"columns",u"dimensions",b"dimensions",u"id",b"id",u"name",b"name"]) -> None: ...

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
            def FromString(cls, s: builtin___bytes) -> Flow.Metadata: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Flow.Metadata: ...
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
                def FromString(cls, s: builtin___bytes) -> Flow.FlowOutputs.Columns: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Flow.FlowOutputs.Columns: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id",u"name",b"name",u"type",b"type"]) -> None: ...


        @property
        def columns(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Flow.FlowOutputs.Columns]: ...

        def __init__(self,
            *,
            columns : typing___Optional[typing___Iterable[Flow.FlowOutputs.Columns]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Flow.FlowOutputs: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Flow.FlowOutputs: ...
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
            def FromString(cls, s: builtin___bytes) -> Flow.OutputDefs: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Flow.OutputDefs: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id",u"name",b"name",u"type",b"type"]) -> None: ...

    flowId = ... # type: typing___Text
    name = ... # type: typing___Text
    type = ... # type: typing___Text
    category = ... # type: typing___Text
    vName = ... # type: typing___Text
    enableLoop = ... # type: builtin___bool
    readOnly = ... # type: builtin___bool
    org = ... # type: builtin___int
    createTime = ... # type: typing___Text
    creator = ... # type: typing___Text
    vCreator = ... # type: typing___Text
    updateTime = ... # type: typing___Text
    version = ... # type: builtin___int
    vDesc = ... # type: typing___Text
    readAuthorizers = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    updateAuthorizers = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    deleteAuthorizers = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    executeAuthorizers = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    memo = ... # type: typing___Text
    subscribers = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    subscribedChannel = ... # type: typing___Text
    is_system_org = ... # type: builtin___bool
    tags = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

    @property
    def stepList(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[alert_service_sdk___model___flow___flow_step_pb2___FlowStep]: ...

    @property
    def tableDefs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Flow.TableDefs]: ...

    @property
    def flowEnv(self) -> google___protobuf___struct_pb2___Value: ...

    @property
    def metadata(self) -> Flow.Metadata: ...

    @property
    def flowInputs(self) -> google___protobuf___struct_pb2___Value: ...

    @property
    def flowOutputs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Flow.FlowOutputs]: ...

    @property
    def outputDefs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Flow.OutputDefs]: ...

    @property
    def histories(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___protobuf___struct_pb2___Struct]: ...

    def __init__(self,
        *,
        flowId : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        type : typing___Optional[typing___Text] = None,
        category : typing___Optional[typing___Text] = None,
        vName : typing___Optional[typing___Text] = None,
        enableLoop : typing___Optional[builtin___bool] = None,
        readOnly : typing___Optional[builtin___bool] = None,
        org : typing___Optional[builtin___int] = None,
        createTime : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        vCreator : typing___Optional[typing___Text] = None,
        updateTime : typing___Optional[typing___Text] = None,
        version : typing___Optional[builtin___int] = None,
        vDesc : typing___Optional[typing___Text] = None,
        readAuthorizers : typing___Optional[typing___Iterable[typing___Text]] = None,
        updateAuthorizers : typing___Optional[typing___Iterable[typing___Text]] = None,
        deleteAuthorizers : typing___Optional[typing___Iterable[typing___Text]] = None,
        executeAuthorizers : typing___Optional[typing___Iterable[typing___Text]] = None,
        memo : typing___Optional[typing___Text] = None,
        subscribers : typing___Optional[typing___Iterable[typing___Text]] = None,
        subscribedChannel : typing___Optional[typing___Text] = None,
        is_system_org : typing___Optional[builtin___bool] = None,
        stepList : typing___Optional[typing___Iterable[alert_service_sdk___model___flow___flow_step_pb2___FlowStep]] = None,
        tableDefs : typing___Optional[typing___Iterable[Flow.TableDefs]] = None,
        flowEnv : typing___Optional[google___protobuf___struct_pb2___Value] = None,
        tags : typing___Optional[typing___Iterable[typing___Text]] = None,
        metadata : typing___Optional[Flow.Metadata] = None,
        flowInputs : typing___Optional[google___protobuf___struct_pb2___Value] = None,
        flowOutputs : typing___Optional[typing___Iterable[Flow.FlowOutputs]] = None,
        outputDefs : typing___Optional[typing___Iterable[Flow.OutputDefs]] = None,
        histories : typing___Optional[typing___Iterable[google___protobuf___struct_pb2___Struct]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Flow: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Flow: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"flowEnv",b"flowEnv",u"flowInputs",b"flowInputs",u"metadata",b"metadata"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"category",b"category",u"createTime",b"createTime",u"creator",b"creator",u"deleteAuthorizers",b"deleteAuthorizers",u"enableLoop",b"enableLoop",u"executeAuthorizers",b"executeAuthorizers",u"flowEnv",b"flowEnv",u"flowId",b"flowId",u"flowInputs",b"flowInputs",u"flowOutputs",b"flowOutputs",u"histories",b"histories",u"is_system_org",b"is_system_org",u"memo",b"memo",u"metadata",b"metadata",u"name",b"name",u"org",b"org",u"outputDefs",b"outputDefs",u"readAuthorizers",b"readAuthorizers",u"readOnly",b"readOnly",u"stepList",b"stepList",u"subscribedChannel",b"subscribedChannel",u"subscribers",b"subscribers",u"tableDefs",b"tableDefs",u"tags",b"tags",u"type",b"type",u"updateAuthorizers",b"updateAuthorizers",u"updateTime",b"updateTime",u"vCreator",b"vCreator",u"vDesc",b"vDesc",u"vName",b"vName",u"version",b"version"]) -> None: ...
