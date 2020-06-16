# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from container_sdk.model.metadata_center.stream_metrics_schema_field_pb2 import (
    StreamMetricsSchemaField as container_sdk___model___metadata_center___stream_metrics_schema_field_pb2___StreamMetricsSchemaField,
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


class StreamMetricsSchema(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    id = ... # type: typing___Text
    org = ... # type: builtin___int
    version = ... # type: builtin___int
    name = ... # type: typing___Text

    @property
    def dimensions(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[container_sdk___model___metadata_center___stream_metrics_schema_field_pb2___StreamMetricsSchemaField]: ...

    @property
    def metrics(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[container_sdk___model___metadata_center___stream_metrics_schema_field_pb2___StreamMetricsSchemaField]: ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        org : typing___Optional[builtin___int] = None,
        version : typing___Optional[builtin___int] = None,
        name : typing___Optional[typing___Text] = None,
        dimensions : typing___Optional[typing___Iterable[container_sdk___model___metadata_center___stream_metrics_schema_field_pb2___StreamMetricsSchemaField]] = None,
        metrics : typing___Optional[typing___Iterable[container_sdk___model___metadata_center___stream_metrics_schema_field_pb2___StreamMetricsSchemaField]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> StreamMetricsSchema: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> StreamMetricsSchema: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"dimensions",b"dimensions",u"id",b"id",u"metrics",b"metrics",u"name",b"name",u"org",b"org",u"version",b"version"]) -> None: ...
