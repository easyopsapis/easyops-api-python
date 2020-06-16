# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from anxin_service_sdk.model.container.metric_target_pb2 import (
    MetricTarget as anxin_service_sdk___model___container___metric_target_pb2___MetricTarget,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
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


class ResourceMetricSource(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name = ... # type: typing___Text

    @property
    def target(self) -> anxin_service_sdk___model___container___metric_target_pb2___MetricTarget: ...

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        target : typing___Optional[anxin_service_sdk___model___container___metric_target_pb2___MetricTarget] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ResourceMetricSource: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ResourceMetricSource: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"target",b"target"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"name",b"name",u"target",b"target"]) -> None: ...
