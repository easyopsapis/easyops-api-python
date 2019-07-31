# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from model.topology.property_pb2 import (
    Property as model___topology___property_pb2___Property,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class Container(google___protobuf___message___Message):
    class Style(google___protobuf___message___Message):
        x = ... # type: float
        y = ... # type: float
        width = ... # type: float
        height = ... # type: float
        className = ... # type: typing___Text

        def __init__(self,
            x : typing___Optional[float] = None,
            y : typing___Optional[float] = None,
            width : typing___Optional[float] = None,
            height : typing___Optional[float] = None,
            className : typing___Optional[typing___Text] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> Container.Style: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"className",u"height",u"width",u"x",u"y"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[b"className",b"height",b"width",b"x",b"y"]) -> None: ...

    name = ... # type: typing___Text
    dataSource = ... # type: typing___Text
    id = ... # type: typing___Text
    collapse = ... # type: bool
    creator = ... # type: typing___Text
    modifier = ... # type: typing___Text
    ctime = ... # type: int
    mtime = ... # type: int

    @property
    def property(self) -> model___topology___property_pb2___Property: ...

    @property
    def style(self) -> Container.Style: ...

    def __init__(self,
        name : typing___Optional[typing___Text] = None,
        dataSource : typing___Optional[typing___Text] = None,
        id : typing___Optional[typing___Text] = None,
        property : typing___Optional[model___topology___property_pb2___Property] = None,
        collapse : typing___Optional[bool] = None,
        creator : typing___Optional[typing___Text] = None,
        modifier : typing___Optional[typing___Text] = None,
        ctime : typing___Optional[int] = None,
        mtime : typing___Optional[int] = None,
        style : typing___Optional[Container.Style] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Container: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"property",u"style"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"collapse",u"creator",u"ctime",u"dataSource",u"id",u"modifier",u"mtime",u"name",u"property",u"style"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"property",b"property",u"style",b"style"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"collapse",b"creator",b"ctime",b"dataSource",b"id",b"modifier",b"mtime",b"name",b"property",b"style"]) -> None: ...
