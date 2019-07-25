# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.struct_pb2 import (
    Struct as google___protobuf___struct_pb2___Struct,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class FlowExecuteStep(google___protobuf___message___Message):
    class Times(google___protobuf___message___Message):
        stepStartTime = ... # type: int
        toolStartTime = ... # type: int
        toolEndTime = ... # type: int
        stepEndTime = ... # type: int

        def __init__(self,
            stepStartTime : typing___Optional[int] = None,
            toolStartTime : typing___Optional[int] = None,
            toolEndTime : typing___Optional[int] = None,
            stepEndTime : typing___Optional[int] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> FlowExecuteStep.Times: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"stepEndTime",u"stepStartTime",u"toolEndTime",u"toolStartTime"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[b"stepEndTime",b"stepStartTime",b"toolEndTime",b"toolStartTime"]) -> None: ...

    class Agents(google___protobuf___message___Message):
        ip = ... # type: typing___Text
        instanceId = ... # type: typing___Text

        def __init__(self,
            ip : typing___Optional[typing___Text] = None,
            instanceId : typing___Optional[typing___Text] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> FlowExecuteStep.Agents: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"instanceId",u"ip"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[b"instanceId",b"ip"]) -> None: ...

    class Styles(google___protobuf___message___Message):
        width = ... # type: float

        def __init__(self,
            width : typing___Optional[float] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> FlowExecuteStep.Styles: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"width"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[b"width"]) -> None: ...

    class Parents(google___protobuf___message___Message):
        stepName = ... # type: typing___Text
        stepId = ... # type: int
        sourcePoint = ... # type: typing___Text
        targetPoint = ... # type: typing___Text

        def __init__(self,
            stepName : typing___Optional[typing___Text] = None,
            stepId : typing___Optional[int] = None,
            sourcePoint : typing___Optional[typing___Text] = None,
            targetPoint : typing___Optional[typing___Text] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> FlowExecuteStep.Parents: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"sourcePoint",u"stepId",u"stepName",u"targetPoint"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[b"sourcePoint",b"stepId",b"stepName",b"targetPoint"]) -> None: ...

    taskId = ... # type: typing___Text
    flowId = ... # type: typing___Text
    status = ... # type: typing___Text
    org = ... # type: int
    execId = ... # type: typing___Text
    exitStatus = ... # type: int
    stepId = ... # type: int
    toolId = ... # type: typing___Text
    stepName = ... # type: typing___Text
    vId = ... # type: typing___Text
    execUser = ... # type: typing___Text
    failureExit = ... # type: typing___Text
    subType = ... # type: typing___Text
    type = ... # type: typing___Text
    _x = ... # type: float
    _y = ... # type: float
    root = ... # type: typing___Text
    _dx = ... # type: float
    _dy = ... # type: float
    informCondition = ... # type: typing___Text

    @property
    def times(self) -> FlowExecuteStep.Times: ...

    @property
    def inputsDefinition(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def outputsDefinition(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def agents(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[FlowExecuteStep.Agents]: ...

    @property
    def agentStatus(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def agentOutputs(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def agentData(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def styles(self) -> FlowExecuteStep.Styles: ...

    @property
    def outputs(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def inputs(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def parents(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[FlowExecuteStep.Parents]: ...

    def __init__(self,
        taskId : typing___Optional[typing___Text] = None,
        flowId : typing___Optional[typing___Text] = None,
        times : typing___Optional[FlowExecuteStep.Times] = None,
        status : typing___Optional[typing___Text] = None,
        org : typing___Optional[int] = None,
        inputsDefinition : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        outputsDefinition : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        agents : typing___Optional[typing___Iterable[FlowExecuteStep.Agents]] = None,
        execId : typing___Optional[typing___Text] = None,
        exitStatus : typing___Optional[int] = None,
        agentStatus : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        agentOutputs : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        agentData : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        stepId : typing___Optional[int] = None,
        toolId : typing___Optional[typing___Text] = None,
        stepName : typing___Optional[typing___Text] = None,
        vId : typing___Optional[typing___Text] = None,
        execUser : typing___Optional[typing___Text] = None,
        failureExit : typing___Optional[typing___Text] = None,
        subType : typing___Optional[typing___Text] = None,
        type : typing___Optional[typing___Text] = None,
        _x : typing___Optional[float] = None,
        _y : typing___Optional[float] = None,
        root : typing___Optional[typing___Text] = None,
        _dx : typing___Optional[float] = None,
        _dy : typing___Optional[float] = None,
        styles : typing___Optional[FlowExecuteStep.Styles] = None,
        outputs : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        inputs : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        informCondition : typing___Optional[typing___Text] = None,
        parents : typing___Optional[typing___Iterable[FlowExecuteStep.Parents]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> FlowExecuteStep: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"agentData",u"agentOutputs",u"agentStatus",u"inputs",u"inputsDefinition",u"outputs",u"outputsDefinition",u"styles",u"times"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"_dx",u"_dy",u"_x",u"_y",u"agentData",u"agentOutputs",u"agentStatus",u"agents",u"execId",u"execUser",u"exitStatus",u"failureExit",u"flowId",u"informCondition",u"inputs",u"inputsDefinition",u"org",u"outputs",u"outputsDefinition",u"parents",u"root",u"status",u"stepId",u"stepName",u"styles",u"subType",u"taskId",u"times",u"toolId",u"type",u"vId"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"agentData",b"agentData",u"agentOutputs",b"agentOutputs",u"agentStatus",b"agentStatus",u"inputs",b"inputs",u"inputsDefinition",b"inputsDefinition",u"outputs",b"outputs",u"outputsDefinition",b"outputsDefinition",u"styles",b"styles",u"times",b"times"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"_dx",b"_dy",b"_x",b"_y",b"agentData",b"agentOutputs",b"agentStatus",b"agents",b"execId",b"execUser",b"exitStatus",b"failureExit",b"flowId",b"informCondition",b"inputs",b"inputsDefinition",b"org",b"outputs",b"outputsDefinition",b"parents",b"root",b"status",b"stepId",b"stepName",b"styles",b"subType",b"taskId",b"times",b"toolId",b"type",b"vId"]) -> None: ...
