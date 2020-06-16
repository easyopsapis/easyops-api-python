# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from object_store_sdk.model.container.metadata_pb2 import (
    Metadata as object_store_sdk___model___container___metadata_pb2___Metadata,
)

from object_store_sdk.model.container.pod_status_pb2 import (
    PodStatus as object_store_sdk___model___container___pod_status_pb2___PodStatus,
)

from typing import (
    Optional as typing___Optional,
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


class PodDetail(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def metadata(self) -> object_store_sdk___model___container___metadata_pb2___Metadata: ...

    @property
    def status(self) -> object_store_sdk___model___container___pod_status_pb2___PodStatus: ...

    def __init__(self,
        *,
        metadata : typing___Optional[object_store_sdk___model___container___metadata_pb2___Metadata] = None,
        status : typing___Optional[object_store_sdk___model___container___pod_status_pb2___PodStatus] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> PodDetail: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> PodDetail: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"metadata",b"metadata",u"status",b"status"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"metadata",b"metadata",u"status",b"status"]) -> None: ...
