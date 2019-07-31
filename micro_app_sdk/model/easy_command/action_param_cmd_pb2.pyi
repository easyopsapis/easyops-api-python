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


class CmdActionParam(google___protobuf___message___Message):
    cmd = ... # type: typing___Text
    execUser = ... # type: typing___Text
    scriptType = ... # type: typing___Text
    parser = ... # type: typing___Text
    timeout = ... # type: int

    def __init__(self,
        cmd : typing___Optional[typing___Text] = None,
        execUser : typing___Optional[typing___Text] = None,
        scriptType : typing___Optional[typing___Text] = None,
        parser : typing___Optional[typing___Text] = None,
        timeout : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CmdActionParam: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"cmd",u"execUser",u"parser",u"scriptType",u"timeout"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"cmd",b"execUser",b"parser",b"scriptType",b"timeout"]) -> None: ...
