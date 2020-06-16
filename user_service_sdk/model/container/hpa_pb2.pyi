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

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
    Union as typing___Union,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)

from user_service_sdk.model.container.resource_metric_source_pb2 import (
    ResourceMetricSource as user_service_sdk___model___container___resource_metric_source_pb2___ResourceMetricSource,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class HorizontalPodAutoscaler(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class ScaleTargetRef(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        kind = ... # type: typing___Text
        name = ... # type: typing___Text
        apiVersion = ... # type: typing___Text

        def __init__(self,
            *,
            kind : typing___Optional[typing___Text] = None,
            name : typing___Optional[typing___Text] = None,
            apiVersion : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> HorizontalPodAutoscaler.ScaleTargetRef: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> HorizontalPodAutoscaler.ScaleTargetRef: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"apiVersion",b"apiVersion",u"kind",b"kind",u"name",b"name"]) -> None: ...

    class Metrics(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        type = ... # type: typing___Text

        @property
        def resource(self) -> user_service_sdk___model___container___resource_metric_source_pb2___ResourceMetricSource: ...

        def __init__(self,
            *,
            type : typing___Optional[typing___Text] = None,
            resource : typing___Optional[user_service_sdk___model___container___resource_metric_source_pb2___ResourceMetricSource] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> HorizontalPodAutoscaler.Metrics: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> HorizontalPodAutoscaler.Metrics: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"resource",b"resource"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"resource",b"resource",u"type",b"type"]) -> None: ...

    instanceId = ... # type: typing___Text
    resourceName = ... # type: typing___Text
    namespace = ... # type: typing___Text
    minReplicas = ... # type: builtin___int
    maxReplicas = ... # type: builtin___int

    @property
    def scaleTargetRef(self) -> HorizontalPodAutoscaler.ScaleTargetRef: ...

    @property
    def metrics(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[HorizontalPodAutoscaler.Metrics]: ...

    def __init__(self,
        *,
        instanceId : typing___Optional[typing___Text] = None,
        resourceName : typing___Optional[typing___Text] = None,
        namespace : typing___Optional[typing___Text] = None,
        scaleTargetRef : typing___Optional[HorizontalPodAutoscaler.ScaleTargetRef] = None,
        minReplicas : typing___Optional[builtin___int] = None,
        maxReplicas : typing___Optional[builtin___int] = None,
        metrics : typing___Optional[typing___Iterable[HorizontalPodAutoscaler.Metrics]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> HorizontalPodAutoscaler: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> HorizontalPodAutoscaler: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"scaleTargetRef",b"scaleTargetRef"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"instanceId",b"instanceId",u"maxReplicas",b"maxReplicas",u"metrics",b"metrics",u"minReplicas",b"minReplicas",u"namespace",b"namespace",u"resourceName",b"resourceName",u"scaleTargetRef",b"scaleTargetRef"]) -> None: ...
