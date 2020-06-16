# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
    Union as typing___Union,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class InspectionArg(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    key = ... # type: typing___Text
    alias = ... # type: typing___Text
    source = ... # type: typing___Text
    type = ... # type: typing___Text
    require = ... # type: builtin___bool
    default = ... # type: typing___Text
    memo = ... # type: typing___Text

    def __init__(self,
        *,
        key : typing___Optional[typing___Text] = None,
        alias : typing___Optional[typing___Text] = None,
        source : typing___Optional[typing___Text] = None,
        type : typing___Optional[typing___Text] = None,
        require : typing___Optional[builtin___bool] = None,
        default : typing___Optional[typing___Text] = None,
        memo : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> InspectionArg: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> InspectionArg: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"alias",b"alias",u"default",b"default",u"key",b"key",u"memo",b"memo",u"require",b"require",u"source",b"source",u"type",b"type"]) -> None: ...
