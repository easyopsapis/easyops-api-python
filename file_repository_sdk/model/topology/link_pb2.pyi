# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from model.topology.linkStyle_pb2 import (
    LinkStyle as model___topology___linkStyle_pb2___LinkStyle,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class Link(google___protobuf___message___Message):
    source = ... # type: typing___Text
    target = ... # type: typing___Text

    @property
    def style(self) -> model___topology___linkStyle_pb2___LinkStyle: ...

    def __init__(self,
        source : typing___Optional[typing___Text] = None,
        target : typing___Optional[typing___Text] = None,
        style : typing___Optional[model___topology___linkStyle_pb2___LinkStyle] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Link: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"style"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"source",u"style",u"target"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"style",b"style"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"source",b"style",b"target"]) -> None: ...