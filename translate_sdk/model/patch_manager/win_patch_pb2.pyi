# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
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


class WinPatch(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    instanceId = ... # type: typing___Text
    name = ... # type: typing___Text
    articleId = ... # type: typing___Text
    releaseTime = ... # type: typing___Text
    osSystem = ... # type: typing___Text
    osVersion = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    osArchitecture = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    requireReboot = ... # type: builtin___bool
    msrc = ... # type: typing___Text
    size = ... # type: builtin___int
    memo = ... # type: typing___Text
    url = ... # type: typing___Text

    def __init__(self,
        *,
        instanceId : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        articleId : typing___Optional[typing___Text] = None,
        releaseTime : typing___Optional[typing___Text] = None,
        osSystem : typing___Optional[typing___Text] = None,
        osVersion : typing___Optional[typing___Iterable[typing___Text]] = None,
        osArchitecture : typing___Optional[typing___Iterable[typing___Text]] = None,
        requireReboot : typing___Optional[builtin___bool] = None,
        msrc : typing___Optional[typing___Text] = None,
        size : typing___Optional[builtin___int] = None,
        memo : typing___Optional[typing___Text] = None,
        url : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> WinPatch: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> WinPatch: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"articleId",b"articleId",u"instanceId",b"instanceId",u"memo",b"memo",u"msrc",b"msrc",u"name",b"name",u"osArchitecture",b"osArchitecture",u"osSystem",b"osSystem",u"osVersion",b"osVersion",u"releaseTime",b"releaseTime",u"requireReboot",b"requireReboot",u"size",b"size",u"url",b"url"]) -> None: ...
