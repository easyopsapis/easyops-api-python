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


class SendMessageResponse(google___protobuf___message___Message):
    msg = ... # type: typing___Text
    code = ... # type: int

    @property
    def data(self) -> google___protobuf___struct_pb2___Struct: ...

    def __init__(self,
        msg : typing___Optional[typing___Text] = None,
        code : typing___Optional[int] = None,
        data : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> SendMessageResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"code",u"data",u"msg"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"code",b"data",b"msg"]) -> None: ...