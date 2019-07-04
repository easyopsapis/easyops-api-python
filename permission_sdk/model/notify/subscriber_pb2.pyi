# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from model.notify.subscribe_info_pb2 import (
    SubscribeInfo as model___notify___subscribe_info_pb2___SubscribeInfo,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class Subscriber(google___protobuf___message___Message):
    name = ... # type: typing___Text
    admin = ... # type: typing___Text
    callback = ... # type: typing___Text
    ensName = ... # type: typing___Text
    procNum = ... # type: int
    msgType = ... # type: int
    retry = ... # type: int

    @property
    def subscribeInfo(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[model___notify___subscribe_info_pb2___SubscribeInfo]: ...

    def __init__(self,
        name : typing___Optional[typing___Text] = None,
        admin : typing___Optional[typing___Text] = None,
        callback : typing___Optional[typing___Text] = None,
        ensName : typing___Optional[typing___Text] = None,
        procNum : typing___Optional[int] = None,
        msgType : typing___Optional[int] = None,
        retry : typing___Optional[int] = None,
        subscribeInfo : typing___Optional[typing___Iterable[model___notify___subscribe_info_pb2___SubscribeInfo]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Subscriber: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"admin",u"callback",u"ensName",u"msgType",u"name",u"procNum",u"retry",u"subscribeInfo"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"admin",b"callback",b"ensName",b"msgType",b"name",b"procNum",b"retry",b"subscribeInfo"]) -> None: ...