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


class FileInfo(google___protobuf___message___Message):
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
    def FromString(cls, s: bytes) -> FileInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"ctime",u"encoding",u"link",u"md5",u"mtime",u"name",u"perm",u"size",u"type"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"ctime",b"encoding",b"link",b"md5",b"mtime",b"name",b"perm",b"size",b"type"]) -> None: ...
