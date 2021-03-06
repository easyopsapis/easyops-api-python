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


class StoryboardBrick(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    brick = ... # type: typing___Text
    properties = ... # type: typing___Text
    injectDeep = ... # type: builtin___bool
    events = ... # type: typing___Text
    bg = ... # type: builtin___bool
    lifeCycle = ... # type: typing___Text
    params = ... # type: typing___Text

    def __init__(self,
        *,
        brick : typing___Optional[typing___Text] = None,
        properties : typing___Optional[typing___Text] = None,
        injectDeep : typing___Optional[builtin___bool] = None,
        events : typing___Optional[typing___Text] = None,
        bg : typing___Optional[builtin___bool] = None,
        lifeCycle : typing___Optional[typing___Text] = None,
        params : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> StoryboardBrick: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> StoryboardBrick: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"bg",b"bg",u"brick",b"brick",u"events",b"events",u"if",b"if",u"injectDeep",b"injectDeep",u"lifeCycle",b"lifeCycle",u"params",b"params",u"properties",b"properties"]) -> None: ...
