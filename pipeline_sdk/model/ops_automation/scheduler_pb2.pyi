# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.struct_pb2 import (
    Struct as google___protobuf___struct_pb2___Struct,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class Scheduler(google___protobuf___message___Message):
    isBound = ... # type: bool
    isActive = ... # type: bool

    @property
    def recentHistory(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___protobuf___struct_pb2___Struct]: ...

    def __init__(self,
        isBound : typing___Optional[bool] = None,
        isActive : typing___Optional[bool] = None,
        recentHistory : typing___Optional[typing___Iterable[google___protobuf___struct_pb2___Struct]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Scheduler: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"isActive",u"isBound",u"recentHistory"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"isActive",b"isBound",b"recentHistory"]) -> None: ...
