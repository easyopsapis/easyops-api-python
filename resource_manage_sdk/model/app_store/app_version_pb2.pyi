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


class AppVersion(google___protobuf___message___Message):
    versionId = ... # type: typing___Text
    name = ... # type: typing___Text
    versionName = ... # type: typing___Text
    changeLog = ... # type: typing___Text
    releaseTime = ... # type: typing___Text

    def __init__(self,
        versionId : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        versionName : typing___Optional[typing___Text] = None,
        changeLog : typing___Optional[typing___Text] = None,
        releaseTime : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> AppVersion: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"changeLog",u"name",u"releaseTime",u"versionId",u"versionName"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"changeLog",b"name",b"releaseTime",b"versionId",b"versionName"]) -> None: ...
