# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from api_gateway_sdk.model.metadata_center.stream_metric_schema_pb2 import (
    StreamMetricSchema as api_gateway_sdk___model___metadata_center___stream_metric_schema_pb2___StreamMetricSchema,
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


class StreamMetricStates(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    org = ... # type: builtin___int
    command = ... # type: typing___Text

    @property
    def payload(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[api_gateway_sdk___model___metadata_center___stream_metric_schema_pb2___StreamMetricSchema]: ...

    def __init__(self,
        *,
        org : typing___Optional[builtin___int] = None,
        command : typing___Optional[typing___Text] = None,
        payload : typing___Optional[typing___Iterable[api_gateway_sdk___model___metadata_center___stream_metric_schema_pb2___StreamMetricSchema]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> StreamMetricStates: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> StreamMetricStates: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"command",b"command",u"org",b"org",u"payload",b"payload"]) -> None: ...
