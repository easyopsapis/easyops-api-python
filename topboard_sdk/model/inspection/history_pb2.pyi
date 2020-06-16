# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from topboard_sdk.model.inspection.target_pb2 import (
    InspectionTarget as topboard_sdk___model___inspection___target_pb2___InspectionTarget,
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


class InspectionHistory(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    jobId = ... # type: typing___Text
    taskId = ... # type: typing___Text
    taskName = ... # type: typing___Text
    startTime = ... # type: builtin___int
    endTime = ... # type: builtin___int
    usedTime = ... # type: builtin___int
    status = ... # type: typing___Text
    passingRate = ... # type: builtin___float
    score = ... # type: builtin___float

    @property
    def targets(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[topboard_sdk___model___inspection___target_pb2___InspectionTarget]: ...

    def __init__(self,
        *,
        jobId : typing___Optional[typing___Text] = None,
        taskId : typing___Optional[typing___Text] = None,
        taskName : typing___Optional[typing___Text] = None,
        startTime : typing___Optional[builtin___int] = None,
        endTime : typing___Optional[builtin___int] = None,
        usedTime : typing___Optional[builtin___int] = None,
        status : typing___Optional[typing___Text] = None,
        passingRate : typing___Optional[builtin___float] = None,
        score : typing___Optional[builtin___float] = None,
        targets : typing___Optional[typing___Iterable[topboard_sdk___model___inspection___target_pb2___InspectionTarget]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> InspectionHistory: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> InspectionHistory: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"endTime",b"endTime",u"jobId",b"jobId",u"passingRate",b"passingRate",u"score",b"score",u"startTime",b"startTime",u"status",b"status",u"targets",b"targets",u"taskId",b"taskId",u"taskName",b"taskName",u"usedTime",b"usedTime"]) -> None: ...
