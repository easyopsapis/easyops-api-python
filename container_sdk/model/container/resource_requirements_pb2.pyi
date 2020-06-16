# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from container_sdk.model.container.resource_list_pb2 import (
    ResourceList as container_sdk___model___container___resource_list_pb2___ResourceList,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
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


class ResourceRequirements(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def limits(self) -> container_sdk___model___container___resource_list_pb2___ResourceList: ...

    @property
    def requests(self) -> container_sdk___model___container___resource_list_pb2___ResourceList: ...

    def __init__(self,
        *,
        limits : typing___Optional[container_sdk___model___container___resource_list_pb2___ResourceList] = None,
        requests : typing___Optional[container_sdk___model___container___resource_list_pb2___ResourceList] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ResourceRequirements: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ResourceRequirements: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"limits",b"limits",u"requests",b"requests"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"limits",b"limits",u"requests",b"requests"]) -> None: ...
