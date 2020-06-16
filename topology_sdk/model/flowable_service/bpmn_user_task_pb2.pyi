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

from topology_sdk.model.flowable_service.bpmn_links_pb2 import (
    BPMNLinks as topology_sdk___model___flowable_service___bpmn_links_pb2___BPMNLinks,
)

from topology_sdk.model.flowable_service.process_variable_pb2 import (
    ProcessVariable as topology_sdk___model___flowable_service___process_variable_pb2___ProcessVariable,
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


class BPMNUserTask(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class ProcessOp(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        name = ... # type: typing___Text
        targetTaskId = ... # type: typing___Text

        @property
        def conditionExpression(self) -> topology_sdk___model___flowable_service___process_variable_pb2___ProcessVariable: ...

        def __init__(self,
            *,
            name : typing___Optional[typing___Text] = None,
            conditionExpression : typing___Optional[topology_sdk___model___flowable_service___process_variable_pb2___ProcessVariable] = None,
            targetTaskId : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> BPMNUserTask.ProcessOp: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> BPMNUserTask.ProcessOp: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"conditionExpression",b"conditionExpression"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"conditionExpression",b"conditionExpression",u"name",b"name",u"targetTaskId",b"targetTaskId"]) -> None: ...

    id = ... # type: typing___Text
    name = ... # type: typing___Text
    isFormDecision = ... # type: typing___Text
    assignType = ... # type: typing___Text
    assignStrategy = ... # type: typing___Text
    userType = ... # type: typing___Text
    assigneeListUser = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    taskWorkingTime = ... # type: builtin___float

    @property
    def links(self) -> topology_sdk___model___flowable_service___bpmn_links_pb2___BPMNLinks: ...

    @property
    def processOp(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[BPMNUserTask.ProcessOp]: ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        links : typing___Optional[topology_sdk___model___flowable_service___bpmn_links_pb2___BPMNLinks] = None,
        isFormDecision : typing___Optional[typing___Text] = None,
        assignType : typing___Optional[typing___Text] = None,
        assignStrategy : typing___Optional[typing___Text] = None,
        userType : typing___Optional[typing___Text] = None,
        assigneeListUser : typing___Optional[typing___Iterable[typing___Text]] = None,
        taskWorkingTime : typing___Optional[builtin___float] = None,
        processOp : typing___Optional[typing___Iterable[BPMNUserTask.ProcessOp]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> BPMNUserTask: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> BPMNUserTask: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"links",b"links"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"assignStrategy",b"assignStrategy",u"assignType",b"assignType",u"assigneeListUser",b"assigneeListUser",u"id",b"id",u"isFormDecision",b"isFormDecision",u"links",b"links",u"name",b"name",u"processOp",b"processOp",u"taskWorkingTime",b"taskWorkingTime",u"userType",b"userType"]) -> None: ...
