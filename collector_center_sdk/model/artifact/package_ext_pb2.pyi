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


class PackageExt(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class LastVersionInfo(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        ctime = ... # type: typing___Text
        env_type = ... # type: builtin___int
        name = ... # type: typing___Text
        memo = ... # type: typing___Text
        versionId = ... # type: typing___Text

        def __init__(self,
            *,
            ctime : typing___Optional[typing___Text] = None,
            env_type : typing___Optional[builtin___int] = None,
            name : typing___Optional[typing___Text] = None,
            memo : typing___Optional[typing___Text] = None,
            versionId : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> PackageExt.LastVersionInfo: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> PackageExt.LastVersionInfo: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"ctime",b"ctime",u"env_type",b"env_type",u"memo",b"memo",u"name",b"name",u"versionId",b"versionId"]) -> None: ...

    instanceCount = ... # type: builtin___int

    @property
    def lastVersionInfo(self) -> PackageExt.LastVersionInfo: ...

    def __init__(self,
        *,
        lastVersionInfo : typing___Optional[PackageExt.LastVersionInfo] = None,
        instanceCount : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> PackageExt: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> PackageExt: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"lastVersionInfo",b"lastVersionInfo"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"instanceCount",b"instanceCount",u"lastVersionInfo",b"lastVersionInfo"]) -> None: ...