# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
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
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class Scheduler(google___protobuf___message___Message):
    class RecentHistory(google___protobuf___message___Message):
        status = ... # type: typing___Text
        createTime = ... # type: typing___Text

        def __init__(self,
            status : typing___Optional[typing___Text] = None,
            createTime : typing___Optional[typing___Text] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> Scheduler.RecentHistory: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"createTime",u"status"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[b"createTime",b"status"]) -> None: ...

    isBound = ... # type: bool
    isActive = ... # type: bool

    @property
    def recentHistory(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Scheduler.RecentHistory]: ...

    def __init__(self,
        isBound : typing___Optional[bool] = None,
        isActive : typing___Optional[bool] = None,
        recentHistory : typing___Optional[typing___Iterable[Scheduler.RecentHistory]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Scheduler: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"isActive",u"isBound",u"recentHistory"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"isActive",b"isBound",b"recentHistory"]) -> None: ...
