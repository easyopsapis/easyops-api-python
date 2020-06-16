# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from agent_admin_sdk.model.topology.property_pb2 import (
    Property as agent_admin_sdk___model___topology___property_pb2___Property,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
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


class Container(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Style(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        x = ... # type: builtin___float
        y = ... # type: builtin___float
        width = ... # type: builtin___float
        height = ... # type: builtin___float
        className = ... # type: typing___Text

        def __init__(self,
            *,
            x : typing___Optional[builtin___float] = None,
            y : typing___Optional[builtin___float] = None,
            width : typing___Optional[builtin___float] = None,
            height : typing___Optional[builtin___float] = None,
            className : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Container.Style: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Container.Style: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"className",b"className",u"height",b"height",u"width",b"width",u"x",b"x",u"y",b"y"]) -> None: ...

    name = ... # type: typing___Text
    dataSource = ... # type: typing___Text
    id = ... # type: typing___Text
    collapse = ... # type: builtin___bool
    creator = ... # type: typing___Text
    modifier = ... # type: typing___Text
    ctime = ... # type: builtin___int
    mtime = ... # type: builtin___int

    @property
    def property(self) -> agent_admin_sdk___model___topology___property_pb2___Property: ...

    @property
    def style(self) -> Container.Style: ...

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        dataSource : typing___Optional[typing___Text] = None,
        id : typing___Optional[typing___Text] = None,
        property : typing___Optional[agent_admin_sdk___model___topology___property_pb2___Property] = None,
        collapse : typing___Optional[builtin___bool] = None,
        creator : typing___Optional[typing___Text] = None,
        modifier : typing___Optional[typing___Text] = None,
        ctime : typing___Optional[builtin___int] = None,
        mtime : typing___Optional[builtin___int] = None,
        style : typing___Optional[Container.Style] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Container: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Container: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"property",b"property",u"style",b"style"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"collapse",b"collapse",u"creator",b"creator",u"ctime",b"ctime",u"dataSource",b"dataSource",u"id",b"id",u"modifier",b"modifier",u"mtime",b"mtime",u"name",b"name",u"property",b"property",u"style",b"style"]) -> None: ...
