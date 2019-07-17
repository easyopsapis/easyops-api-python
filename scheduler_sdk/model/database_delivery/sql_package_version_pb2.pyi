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


class SQLPackageVersion(google___protobuf___message___Message):
    id = ... # type: typing___Text
    name = ... # type: typing___Text
    repoVersionId = ... # type: typing___Text
    appVersionId = ... # type: typing___Text
    versionName = ... # type: typing___Text
    memo = ... # type: typing___Text
    creator = ... # type: typing___Text
    ctime = ... # type: int
    mtime = ... # type: int

    def __init__(self,
        id : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        repoVersionId : typing___Optional[typing___Text] = None,
        appVersionId : typing___Optional[typing___Text] = None,
        versionName : typing___Optional[typing___Text] = None,
        memo : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        ctime : typing___Optional[int] = None,
        mtime : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> SQLPackageVersion: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"appVersionId",u"creator",u"ctime",u"id",u"memo",u"mtime",u"name",u"repoVersionId",u"versionName"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"appVersionId",b"creator",b"ctime",b"id",b"memo",b"mtime",b"name",b"repoVersionId",b"versionName"]) -> None: ...
