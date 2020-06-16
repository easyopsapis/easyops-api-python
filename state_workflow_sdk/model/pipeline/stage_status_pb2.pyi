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

from state_workflow_sdk.model.pipeline.condition_pb2 import (
    Condition as state_workflow_sdk___model___pipeline___condition_pb2___Condition,
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


class StageStatus(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Steps(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        id = ... # type: typing___Text
        name = ... # type: typing___Text
        number = ... # type: builtin___int
        state = ... # type: typing___Text
        exit_code = ... # type: builtin___int
        log_id = ... # type: typing___Text
        started = ... # type: builtin___int
        finished = ... # type: builtin___int
        type = ... # type: typing___Text

        def __init__(self,
            *,
            id : typing___Optional[typing___Text] = None,
            name : typing___Optional[typing___Text] = None,
            number : typing___Optional[builtin___int] = None,
            state : typing___Optional[typing___Text] = None,
            exit_code : typing___Optional[builtin___int] = None,
            log_id : typing___Optional[typing___Text] = None,
            started : typing___Optional[builtin___int] = None,
            finished : typing___Optional[builtin___int] = None,
            type : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> StageStatus.Steps: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> StageStatus.Steps: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"exit_code",b"exit_code",u"finished",b"finished",u"id",b"id",u"log_id",b"log_id",u"name",b"name",u"number",b"number",u"started",b"started",u"state",b"state",u"type",b"type"]) -> None: ...

    id = ... # type: typing___Text
    stage_name = ... # type: typing___Text
    number = ... # type: builtin___int
    parallel = ... # type: builtin___bool
    state = ... # type: typing___Text
    created = ... # type: builtin___int
    updated = ... # type: builtin___int

    @property
    def conditions(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[state_workflow_sdk___model___pipeline___condition_pb2___Condition]: ...

    @property
    def steps(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[StageStatus.Steps]: ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        stage_name : typing___Optional[typing___Text] = None,
        number : typing___Optional[builtin___int] = None,
        parallel : typing___Optional[builtin___bool] = None,
        state : typing___Optional[typing___Text] = None,
        conditions : typing___Optional[typing___Iterable[state_workflow_sdk___model___pipeline___condition_pb2___Condition]] = None,
        steps : typing___Optional[typing___Iterable[StageStatus.Steps]] = None,
        created : typing___Optional[builtin___int] = None,
        updated : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> StageStatus: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> StageStatus: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"conditions",b"conditions",u"created",b"created",u"id",b"id",u"number",b"number",u"parallel",b"parallel",u"stage_name",b"stage_name",u"state",b"state",u"steps",b"steps",u"updated",b"updated"]) -> None: ...
