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


class AppStoreMicroApp(google___protobuf___message___Message):
    name = ... # type: typing___Text
    id = ... # type: typing___Text
    icon = ... # type: typing___Text
    intro = ... # type: typing___Text

    def __init__(self,
        name : typing___Optional[typing___Text] = None,
        id : typing___Optional[typing___Text] = None,
        icon : typing___Optional[typing___Text] = None,
        intro : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> AppStoreMicroApp: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"icon",u"id",u"intro",u"name"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"icon",b"id",b"intro",b"name"]) -> None: ...
