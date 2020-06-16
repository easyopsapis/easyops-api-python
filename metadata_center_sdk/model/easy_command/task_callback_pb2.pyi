# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
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


class TaskCallback(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    url = ... # type: typing___Text
    ensName = ... # type: typing___Text
    ip = ... # type: typing___Text
    port = ... # type: builtin___int
    host = ... # type: typing___Text

    def __init__(self,
        *,
        url : typing___Optional[typing___Text] = None,
        ensName : typing___Optional[typing___Text] = None,
        ip : typing___Optional[typing___Text] = None,
        port : typing___Optional[builtin___int] = None,
        host : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> TaskCallback: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> TaskCallback: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"ensName",b"ensName",u"host",b"host",u"ip",b"ip",u"port",b"port",u"url",b"url"]) -> None: ...
