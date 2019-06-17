# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from model.artifact.version_pb2 import (
    Version as model___artifact___version_pb2___Version,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class UpdateRequest(google___protobuf___message___Message):
    versionId = ... # type: typing___Text
    name = ... # type: typing___Text
    memo = ... # type: typing___Text
    baseImageId = ... # type: typing___Text

    def __init__(self,
        versionId : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        memo : typing___Optional[typing___Text] = None,
        baseImageId : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> UpdateRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"baseImageId",u"memo",u"name",u"versionId"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"baseImageId",b"memo",b"name",b"versionId"]) -> None: ...

class UpdateResponseWrapper(google___protobuf___message___Message):
    code = ... # type: int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> model___artifact___version_pb2___Version: ...

    def __init__(self,
        code : typing___Optional[int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[model___artifact___version_pb2___Version] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> UpdateResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"code",u"codeExplain",u"data",u"error"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"code",b"codeExplain",b"data",b"error"]) -> None: ...