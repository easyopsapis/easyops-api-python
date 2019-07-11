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


class NodeStyle(google___protobuf___message___Message):
    x = ... # type: float
    y = ... # type: float
    shape = ... # type: typing___Text
    className = ... # type: typing___Text

    def __init__(self,
        x : typing___Optional[float] = None,
        y : typing___Optional[float] = None,
        shape : typing___Optional[typing___Text] = None,
        className : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> NodeStyle: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"className",u"shape",u"x",u"y"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"className",b"shape",b"x",b"y"]) -> None: ...
