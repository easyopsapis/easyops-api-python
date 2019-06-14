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


class CountRelationInstanceRequest(google___protobuf___message___Message):
    relationId = ... # type: typing___Text

    def __init__(self,
        relationId : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CountRelationInstanceRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"relationId"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"relationId"]) -> None: ...

class CountRelationInstanceResponse(google___protobuf___message___Message):
    code = ... # type: int
    error = ... # type: typing___Text
    message = ... # type: typing___Text
    data = ... # type: int

    def __init__(self,
        code : typing___Optional[int] = None,
        error : typing___Optional[typing___Text] = None,
        message : typing___Optional[typing___Text] = None,
        data : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CountRelationInstanceResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"code",u"data",u"error",u"message"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"code",b"data",b"error",b"message"]) -> None: ...

class CountRelationInstanceResponseWrapper(google___protobuf___message___Message):
    code = ... # type: int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> CountRelationInstanceResponse: ...

    def __init__(self,
        code : typing___Optional[int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[CountRelationInstanceResponse] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CountRelationInstanceResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"code",u"codeExplain",u"data",u"error"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"code",b"codeExplain",b"data",b"error"]) -> None: ...
