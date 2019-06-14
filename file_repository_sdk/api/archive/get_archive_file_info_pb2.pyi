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


class GetFileInfoRequest(google___protobuf___message___Message):
    path = ... # type: typing___Text
    encoding = ... # type: typing___Text
    packageId = ... # type: typing___Text
    versionId = ... # type: typing___Text

    def __init__(self,
        path : typing___Optional[typing___Text] = None,
        encoding : typing___Optional[typing___Text] = None,
        packageId : typing___Optional[typing___Text] = None,
        versionId : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetFileInfoRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"encoding",u"packageId",u"path",u"versionId"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"encoding",b"packageId",b"path",b"versionId"]) -> None: ...

class GetFileInfoResponse(google___protobuf___message___Message):
    name = ... # type: typing___Text
    type = ... # type: typing___Text
    size = ... # type: int
    perm = ... # type: typing___Text
    mtime = ... # type: typing___Text
    ctime = ... # type: typing___Text
    link = ... # type: typing___Text
    encoding = ... # type: typing___Text
    md5 = ... # type: typing___Text

    def __init__(self,
        name : typing___Optional[typing___Text] = None,
        type : typing___Optional[typing___Text] = None,
        size : typing___Optional[int] = None,
        perm : typing___Optional[typing___Text] = None,
        mtime : typing___Optional[typing___Text] = None,
        ctime : typing___Optional[typing___Text] = None,
        link : typing___Optional[typing___Text] = None,
        encoding : typing___Optional[typing___Text] = None,
        md5 : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetFileInfoResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"ctime",u"encoding",u"link",u"md5",u"mtime",u"name",u"perm",u"size",u"type"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"ctime",b"encoding",b"link",b"md5",b"mtime",b"name",b"perm",b"size",b"type"]) -> None: ...

class GetFileInfoResponseWrapper(google___protobuf___message___Message):
    code = ... # type: int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> GetFileInfoResponse: ...

    def __init__(self,
        code : typing___Optional[int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[GetFileInfoResponse] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetFileInfoResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"code",u"codeExplain",u"data",u"error"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"code",b"codeExplain",b"data",b"error"]) -> None: ...
