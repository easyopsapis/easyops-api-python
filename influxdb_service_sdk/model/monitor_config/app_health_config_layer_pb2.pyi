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

from influxdb_service_sdk.model.monitor_config.app_health_config_metrics_pb2 import (
    AppHealthConfigMetrics as influxdb_service_sdk___model___monitor_config___app_health_config_metrics_pb2___AppHealthConfigMetrics,
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


class AppHealthConfigLayer(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    id = ... # type: typing___Text
    name = ... # type: typing___Text
    weight = ... # type: builtin___int

    @property
    def metrics(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[influxdb_service_sdk___model___monitor_config___app_health_config_metrics_pb2___AppHealthConfigMetrics]: ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        weight : typing___Optional[builtin___int] = None,
        metrics : typing___Optional[typing___Iterable[influxdb_service_sdk___model___monitor_config___app_health_config_metrics_pb2___AppHealthConfigMetrics]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> AppHealthConfigLayer: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> AppHealthConfigLayer: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id",u"metrics",b"metrics",u"name",b"name",u"weight",b"weight"]) -> None: ...
