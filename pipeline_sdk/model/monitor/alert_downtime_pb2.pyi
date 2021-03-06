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

from pipeline_sdk.model.monitor.alert_dims_pb2 import (
    AlertDims as pipeline_sdk___model___monitor___alert_dims_pb2___AlertDims,
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


class AlertDowntime(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Schedule(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        type = ... # type: typing___Text
        start_time = ... # type: typing___Text
        end_time = ... # type: typing___Text
        start_date = ... # type: typing___Text
        end_date = ... # type: typing___Text
        repeat_on = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

        def __init__(self,
            *,
            type : typing___Optional[typing___Text] = None,
            start_time : typing___Optional[typing___Text] = None,
            end_time : typing___Optional[typing___Text] = None,
            start_date : typing___Optional[typing___Text] = None,
            end_date : typing___Optional[typing___Text] = None,
            repeat_on : typing___Optional[typing___Iterable[typing___Text]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> AlertDowntime.Schedule: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> AlertDowntime.Schedule: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"end_date",b"end_date",u"end_time",b"end_time",u"repeat_on",b"repeat_on",u"start_date",b"start_date",u"start_time",b"start_time",u"type",b"type"]) -> None: ...

    id = ... # type: typing___Text
    alert_rule_id = ... # type: typing___Text
    reason = ... # type: typing___Text
    creator = ... # type: typing___Text
    ctime = ... # type: builtin___int
    mtime = ... # type: builtin___int
    org = ... # type: builtin___int

    @property
    def alert_dims(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[pipeline_sdk___model___monitor___alert_dims_pb2___AlertDims]: ...

    @property
    def schedule(self) -> AlertDowntime.Schedule: ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        alert_rule_id : typing___Optional[typing___Text] = None,
        alert_dims : typing___Optional[typing___Iterable[pipeline_sdk___model___monitor___alert_dims_pb2___AlertDims]] = None,
        schedule : typing___Optional[AlertDowntime.Schedule] = None,
        reason : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        ctime : typing___Optional[builtin___int] = None,
        mtime : typing___Optional[builtin___int] = None,
        org : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> AlertDowntime: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> AlertDowntime: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"schedule",b"schedule"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"alert_dims",b"alert_dims",u"alert_rule_id",b"alert_rule_id",u"creator",b"creator",u"ctime",b"ctime",u"id",b"id",u"mtime",b"mtime",u"org",b"org",u"reason",b"reason",u"schedule",b"schedule"]) -> None: ...
