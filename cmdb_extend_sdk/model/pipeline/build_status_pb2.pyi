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


class BuildStatus(google___protobuf___message___Message):
    state = ... # type: typing___Text
    nodeName = ... # type: typing___Text
    started = ... # type: int
    updated = ... # type: int
    finished = ... # type: int

    def __init__(self,
        state : typing___Optional[typing___Text] = None,
        nodeName : typing___Optional[typing___Text] = None,
        started : typing___Optional[int] = None,
        updated : typing___Optional[int] = None,
        finished : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BuildStatus: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"finished",u"nodeName",u"started",u"state",u"updated"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"finished",b"nodeName",b"started",b"state",b"updated"]) -> None: ...
