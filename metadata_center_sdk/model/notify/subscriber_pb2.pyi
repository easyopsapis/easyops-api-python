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

from metadata_center_sdk.model.notify.subscribe_info_pb2 import (
    SubscribeInfo as metadata_center_sdk___model___notify___subscribe_info_pb2___SubscribeInfo,
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


class Subscriber(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name = ... # type: typing___Text
    admin = ... # type: typing___Text
    callback = ... # type: typing___Text
    ensName = ... # type: typing___Text
    procNum = ... # type: builtin___int
    msgType = ... # type: builtin___int
    retry = ... # type: builtin___int

    @property
    def subscribeInfo(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[metadata_center_sdk___model___notify___subscribe_info_pb2___SubscribeInfo]: ...

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        admin : typing___Optional[typing___Text] = None,
        callback : typing___Optional[typing___Text] = None,
        ensName : typing___Optional[typing___Text] = None,
        procNum : typing___Optional[builtin___int] = None,
        msgType : typing___Optional[builtin___int] = None,
        retry : typing___Optional[builtin___int] = None,
        subscribeInfo : typing___Optional[typing___Iterable[metadata_center_sdk___model___notify___subscribe_info_pb2___SubscribeInfo]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Subscriber: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Subscriber: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"admin",b"admin",u"callback",b"callback",u"ensName",b"ensName",u"msgType",b"msgType",u"name",b"name",u"procNum",b"procNum",u"retry",b"retry",u"subscribeInfo",b"subscribeInfo"]) -> None: ...
