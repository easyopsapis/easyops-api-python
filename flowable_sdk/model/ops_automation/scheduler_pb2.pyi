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


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class Scheduler(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class RecentHistory(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        status = ... # type: typing___Text
        createTime = ... # type: typing___Text

        def __init__(self,
            *,
            status : typing___Optional[typing___Text] = None,
            createTime : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Scheduler.RecentHistory: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Scheduler.RecentHistory: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"createTime",b"createTime",u"status",b"status"]) -> None: ...

    isBound = ... # type: builtin___bool
    isActive = ... # type: builtin___bool

    @property
    def recentHistory(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Scheduler.RecentHistory]: ...

    def __init__(self,
        *,
        isBound : typing___Optional[builtin___bool] = None,
        isActive : typing___Optional[builtin___bool] = None,
        recentHistory : typing___Optional[typing___Iterable[Scheduler.RecentHistory]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Scheduler: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Scheduler: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"isActive",b"isActive",u"isBound",b"isBound",u"recentHistory",b"recentHistory"]) -> None: ...
