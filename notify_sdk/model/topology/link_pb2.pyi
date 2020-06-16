# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from notify_sdk.model.topology.linkStyle_pb2 import (
    LinkStyle as notify_sdk___model___topology___linkStyle_pb2___LinkStyle,
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


class Link(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    source = ... # type: typing___Text
    target = ... # type: typing___Text

    @property
    def style(self) -> notify_sdk___model___topology___linkStyle_pb2___LinkStyle: ...

    def __init__(self,
        *,
        source : typing___Optional[typing___Text] = None,
        target : typing___Optional[typing___Text] = None,
        style : typing___Optional[notify_sdk___model___topology___linkStyle_pb2___LinkStyle] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Link: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Link: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"style",b"style"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"source",b"source",u"style",b"style",u"target",b"target"]) -> None: ...
