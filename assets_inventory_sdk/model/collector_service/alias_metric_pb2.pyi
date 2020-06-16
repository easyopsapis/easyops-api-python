# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from assets_inventory_sdk.model.collector_service.metric_pb2 import (
    CollectorMetric as assets_inventory_sdk___model___collector_service___metric_pb2___CollectorMetric,
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


class CollectorAliasMetric(google___protobuf___message___Message):
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
            def FromString(cls, s: builtin___bytes) -> CollectorAliasMetric.Dims: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CollectorAliasMetric.Dims: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"dimName",b"dimName",u"originDimName",b"originDimName"]) -> None: ...

    instanceId = ... # type: typing___Text
    name = ... # type: typing___Text
    version = ... # type: builtin___int
    isKeyMetric = ... # type: builtin___bool
    description = ... # type: typing___Text
    objectId = ... # type: typing___Text
    isCalculated = ... # type: builtin___bool
    expression = ... # type: typing___Text

    @property
    def dims(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[CollectorAliasMetric.Dims]: ...

    @property
    def originalMetrics(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[assets_inventory_sdk___model___collector_service___metric_pb2___CollectorMetric]: ...

    @property
    def dependMetrics(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[CollectorAliasMetric]: ...

    def __init__(self,
        *,
        instanceId : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        dims : typing___Optional[typing___Iterable[CollectorAliasMetric.Dims]] = None,
        version : typing___Optional[builtin___int] = None,
        isKeyMetric : typing___Optional[builtin___bool] = None,
        description : typing___Optional[typing___Text] = None,
        objectId : typing___Optional[typing___Text] = None,
        originalMetrics : typing___Optional[typing___Iterable[assets_inventory_sdk___model___collector_service___metric_pb2___CollectorMetric]] = None,
        dependMetrics : typing___Optional[typing___Iterable[CollectorAliasMetric]] = None,
        isCalculated : typing___Optional[builtin___bool] = None,
        expression : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CollectorAliasMetric: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CollectorAliasMetric: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"dependMetrics",b"dependMetrics",u"description",b"description",u"dims",b"dims",u"expression",b"expression",u"instanceId",b"instanceId",u"isCalculated",b"isCalculated",u"isKeyMetric",b"isKeyMetric",u"name",b"name",u"objectId",b"objectId",u"originalMetrics",b"originalMetrics",u"version",b"version"]) -> None: ...
