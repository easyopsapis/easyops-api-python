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


class GetDiffSizeRequest(google___protobuf___message___Message):
    ver_from = ... # type: typing___Text
    ver_to = ... # type: typing___Text
    packageId = ... # type: typing___Text

    def __init__(self,
        ver_from : typing___Optional[typing___Text] = None,
        ver_to : typing___Optional[typing___Text] = None,
        packageId : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetDiffSizeRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"packageId",u"ver_from",u"ver_to"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"packageId",b"ver_from",b"ver_to"]) -> None: ...

class GetDiffSizeResponse(google___protobuf___message___Message):
    size = ... # type: int
    diffSize = ... # type: int

    def __init__(self,
        size : typing___Optional[int] = None,
        diffSize : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetDiffSizeResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"diffSize",u"size"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"diffSize",b"size"]) -> None: ...

class GetDiffSizeResponseWrapper(google___protobuf___message___Message):
    code = ... # type: int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> GetDiffSizeResponse: ...

    def __init__(self,
        code : typing___Optional[int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[GetDiffSizeResponse] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetDiffSizeResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"code",u"codeExplain",u"data",u"error"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"code",b"codeExplain",b"data",b"error"]) -> None: ...