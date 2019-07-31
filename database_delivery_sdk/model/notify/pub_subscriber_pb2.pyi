# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class PubSubscriber(google___protobuf___message___Message):
    instanceId = ... # type: typing___Text
    name = ... # type: typing___Text
    org = ... # type: int
    admin = ... # type: typing___Text
    callback = ... # type: typing___Text
    ensName = ... # type: typing___Text
    retry = ... # type: int
    mtime = ... # type: int
    _version = ... # type: int

    def __init__(self,
        instanceId : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        org : typing___Optional[int] = None,
        admin : typing___Optional[typing___Text] = None,
        callback : typing___Optional[typing___Text] = None,
        ensName : typing___Optional[typing___Text] = None,
        retry : typing___Optional[int] = None,
        mtime : typing___Optional[int] = None,
        _version : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PubSubscriber: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"_version",u"admin",u"callback",u"ensName",u"instanceId",u"mtime",u"name",u"org",u"retry"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"_version",b"admin",b"callback",b"ensName",b"instanceId",b"mtime",b"name",b"org",b"retry"]) -> None: ...
