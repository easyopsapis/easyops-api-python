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

from resource_manage_sdk.model.collector_service.metric_pb2 import (
    CollectorMetric as resource_manage_sdk___model___collector_service___metric_pb2___CollectorMetric,
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


class CollectorAliasMetricWithOneOiriginalMetric(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Dims(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        dimName = ... # type: typing___Text
        originDimName = ... # type: typing___Text

        def __init__(self,
            *,
            dimName : typing___Optional[typing___Text] = None,
            originDimName : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> CollectorAliasMetricWithOneOiriginalMetric.Dims: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CollectorAliasMetricWithOneOiriginalMetric.Dims: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"dimName",b"dimName",u"originDimName",b"originDimName"]) -> None: ...

    calculateOnly = ... # type: builtin___bool
    instanceId = ... # type: typing___Text
    name = ... # type: typing___Text
    version = ... # type: builtin___int
    isCalculated = ... # type: builtin___bool
    expression = ... # type: typing___Text

    @property
    def collectorMetric(self) -> resource_manage_sdk___model___collector_service___metric_pb2___CollectorMetric: ...

    @property
    def dependMetrics(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[CollectorAliasMetricWithOneOiriginalMetric]: ...

    @property
    def dims(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[CollectorAliasMetricWithOneOiriginalMetric.Dims]: ...

    def __init__(self,
        *,
        calculateOnly : typing___Optional[builtin___bool] = None,
        collectorMetric : typing___Optional[resource_manage_sdk___model___collector_service___metric_pb2___CollectorMetric] = None,
        dependMetrics : typing___Optional[typing___Iterable[CollectorAliasMetricWithOneOiriginalMetric]] = None,
        instanceId : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        dims : typing___Optional[typing___Iterable[CollectorAliasMetricWithOneOiriginalMetric.Dims]] = None,
        version : typing___Optional[builtin___int] = None,
        isCalculated : typing___Optional[builtin___bool] = None,
        expression : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CollectorAliasMetricWithOneOiriginalMetric: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CollectorAliasMetricWithOneOiriginalMetric: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"collectorMetric",b"collectorMetric"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"calculateOnly",b"calculateOnly",u"collectorMetric",b"collectorMetric",u"dependMetrics",b"dependMetrics",u"dims",b"dims",u"expression",b"expression",u"instanceId",b"instanceId",u"isCalculated",b"isCalculated",u"name",b"name",u"version",b"version"]) -> None: ...
