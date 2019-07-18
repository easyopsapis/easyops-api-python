# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.struct_pb2 import (
    Struct as google___protobuf___struct_pb2___Struct,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class Callback(google___protobuf___message___Message):
    url = ... # type: typing___Text
    host = ... # type: typing___Text
    ensName = ... # type: typing___Text
    method = ... # type: typing___Text

    @property
    def headers(self) -> google___protobuf___struct_pb2___Struct: ...

    def __init__(self,
        url : typing___Optional[typing___Text] = None,
        host : typing___Optional[typing___Text] = None,
        ensName : typing___Optional[typing___Text] = None,
        method : typing___Optional[typing___Text] = None,
        headers : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Callback: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"headers"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"ensName",u"headers",u"host",u"method",u"url"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"headers",b"headers"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"ensName",b"headers",b"host",b"method",b"url"]) -> None: ...