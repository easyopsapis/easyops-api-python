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


class StreamAggregateRule(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class AggregateVars(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        name = ... # type: typing___Text
        metric = ... # type: typing___Text
        objectId = ... # type: typing___Text
        instances = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

        def __init__(self,
            *,
            name : typing___Optional[typing___Text] = None,
            metric : typing___Optional[typing___Text] = None,
            objectId : typing___Optional[typing___Text] = None,
            instances : typing___Optional[typing___Iterable[typing___Text]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> StreamAggregateRule.AggregateVars: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> StreamAggregateRule.AggregateVars: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"instances",b"instances",u"metric",b"metric",u"name",b"name",u"objectId",b"objectId"]) -> None: ...

    org = ... # type: builtin___int
    id = ... # type: typing___Text
    ruleId = ... # type: typing___Text
    version = ... # type: builtin___int
    objectId = ... # type: typing___Text
    instanceId = ... # type: typing___Text
    metricName = ... # type: typing___Text
    aggregateFunc = ... # type: typing___Text
    aggregateExpr = ... # type: typing___Text
    granularity = ... # type: builtin___int
    groupBy = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

    @property
    def aggregateVars(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[StreamAggregateRule.AggregateVars]: ...

    def __init__(self,
        *,
        org : typing___Optional[builtin___int] = None,
        id : typing___Optional[typing___Text] = None,
        ruleId : typing___Optional[typing___Text] = None,
        version : typing___Optional[builtin___int] = None,
        objectId : typing___Optional[typing___Text] = None,
        instanceId : typing___Optional[typing___Text] = None,
        metricName : typing___Optional[typing___Text] = None,
        aggregateFunc : typing___Optional[typing___Text] = None,
        aggregateExpr : typing___Optional[typing___Text] = None,
        aggregateVars : typing___Optional[typing___Iterable[StreamAggregateRule.AggregateVars]] = None,
        granularity : typing___Optional[builtin___int] = None,
        groupBy : typing___Optional[typing___Iterable[typing___Text]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> StreamAggregateRule: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> StreamAggregateRule: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"aggregateExpr",b"aggregateExpr",u"aggregateFunc",b"aggregateFunc",u"aggregateVars",b"aggregateVars",u"granularity",b"granularity",u"groupBy",b"groupBy",u"id",b"id",u"instanceId",b"instanceId",u"metricName",b"metricName",u"objectId",b"objectId",u"org",b"org",u"ruleId",b"ruleId",u"version",b"version"]) -> None: ...
