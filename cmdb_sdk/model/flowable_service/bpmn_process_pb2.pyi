# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from cmdb_sdk.model.flowable_service.bpmn_end_event_pb2 import (
    BPMNEndEvent as cmdb_sdk___model___flowable_service___bpmn_end_event_pb2___BPMNEndEvent,
)

from cmdb_sdk.model.flowable_service.bpmn_exclusive_gateway_pb2 import (
    BPMNExclusiveGateway as cmdb_sdk___model___flowable_service___bpmn_exclusive_gateway_pb2___BPMNExclusiveGateway,
)

from cmdb_sdk.model.flowable_service.bpmn_sequence_flow_pb2 import (
    BPMNSequenceFlow as cmdb_sdk___model___flowable_service___bpmn_sequence_flow_pb2___BPMNSequenceFlow,
)

from cmdb_sdk.model.flowable_service.bpmn_start_event_pb2 import (
    BPMNStartEvent as cmdb_sdk___model___flowable_service___bpmn_start_event_pb2___BPMNStartEvent,
)

from cmdb_sdk.model.flowable_service.bpmn_user_task_pb2 import (
    BPMNUserTask as cmdb_sdk___model___flowable_service___bpmn_user_task_pb2___BPMNUserTask,
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


class BPMNProcess(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    id = ... # type: typing___Text
    name = ... # type: typing___Text
    isExecuteable = ... # type: typing___Text

    @property
    def sequenceFlow(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[cmdb_sdk___model___flowable_service___bpmn_sequence_flow_pb2___BPMNSequenceFlow]: ...

    @property
    def exclusiveGateway(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[cmdb_sdk___model___flowable_service___bpmn_exclusive_gateway_pb2___BPMNExclusiveGateway]: ...

    @property
    def startEvent(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[cmdb_sdk___model___flowable_service___bpmn_start_event_pb2___BPMNStartEvent]: ...

    @property
    def endEvent(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[cmdb_sdk___model___flowable_service___bpmn_end_event_pb2___BPMNEndEvent]: ...

    @property
    def userTask(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[cmdb_sdk___model___flowable_service___bpmn_user_task_pb2___BPMNUserTask]: ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        isExecuteable : typing___Optional[typing___Text] = None,
        sequenceFlow : typing___Optional[typing___Iterable[cmdb_sdk___model___flowable_service___bpmn_sequence_flow_pb2___BPMNSequenceFlow]] = None,
        exclusiveGateway : typing___Optional[typing___Iterable[cmdb_sdk___model___flowable_service___bpmn_exclusive_gateway_pb2___BPMNExclusiveGateway]] = None,
        startEvent : typing___Optional[typing___Iterable[cmdb_sdk___model___flowable_service___bpmn_start_event_pb2___BPMNStartEvent]] = None,
        endEvent : typing___Optional[typing___Iterable[cmdb_sdk___model___flowable_service___bpmn_end_event_pb2___BPMNEndEvent]] = None,
        userTask : typing___Optional[typing___Iterable[cmdb_sdk___model___flowable_service___bpmn_user_task_pb2___BPMNUserTask]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> BPMNProcess: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> BPMNProcess: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"endEvent",b"endEvent",u"exclusiveGateway",b"exclusiveGateway",u"id",b"id",u"isExecuteable",b"isExecuteable",u"name",b"name",u"sequenceFlow",b"sequenceFlow",u"startEvent",b"startEvent",u"userTask",b"userTask"]) -> None: ...
