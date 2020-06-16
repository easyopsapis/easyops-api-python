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


class GetVersionDetailRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    versionId = ... # type: typing___Text

    def __init__(self,
        *,
        versionId : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetVersionDetailRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetVersionDetailRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"versionId",b"versionId"]) -> None: ...

class GetVersionDetailResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Source(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        host = ... # type: typing___Text
        ensName = ... # type: typing___Text
        type = ... # type: typing___Text
        port = ... # type: builtin___int
        ip = ... # type: typing___Text

        def __init__(self,
            *,
            host : typing___Optional[typing___Text] = None,
            ensName : typing___Optional[typing___Text] = None,
            type : typing___Optional[typing___Text] = None,
            port : typing___Optional[builtin___int] = None,
            ip : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> GetVersionDetailResponse.Source: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetVersionDetailResponse.Source: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"ensName",b"ensName",u"host",b"host",u"ip",b"ip",u"port",b"port",u"type",b"type"]) -> None: ...

    name = ... # type: typing___Text
    versionId = ... # type: typing___Text
    packageId = ... # type: typing___Text
    org = ... # type: builtin___int
    baseImageId = ... # type: typing___Text
    baseVersionName = ... # type: typing___Text
    creator = ... # type: typing___Text
    env_type = ... # type: builtin___int
    memo = ... # type: typing___Text
    ctime = ... # type: typing___Text
    mtime = ... # type: typing___Text
    sign = ... # type: typing___Text
    repoVersion = ... # type: typing___Text
    sourceType = ... # type: typing___Text
    workspaceBaseId = ... # type: typing___Text
    conf = ... # type: typing___Text

    @property
    def source(self) -> GetVersionDetailResponse.Source: ...

    def __init__(self,
        *,
        source : typing___Optional[GetVersionDetailResponse.Source] = None,
        name : typing___Optional[typing___Text] = None,
        versionId : typing___Optional[typing___Text] = None,
        packageId : typing___Optional[typing___Text] = None,
        org : typing___Optional[builtin___int] = None,
        baseImageId : typing___Optional[typing___Text] = None,
        baseVersionName : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        env_type : typing___Optional[builtin___int] = None,
        memo : typing___Optional[typing___Text] = None,
        ctime : typing___Optional[typing___Text] = None,
        mtime : typing___Optional[typing___Text] = None,
        sign : typing___Optional[typing___Text] = None,
        repoVersion : typing___Optional[typing___Text] = None,
        sourceType : typing___Optional[typing___Text] = None,
        workspaceBaseId : typing___Optional[typing___Text] = None,
        conf : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetVersionDetailResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetVersionDetailResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"source",b"source"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"baseImageId",b"baseImageId",u"baseVersionName",b"baseVersionName",u"conf",b"conf",u"creator",b"creator",u"ctime",b"ctime",u"env_type",b"env_type",u"memo",b"memo",u"mtime",b"mtime",u"name",b"name",u"org",b"org",u"packageId",b"packageId",u"repoVersion",b"repoVersion",u"sign",b"sign",u"source",b"source",u"sourceType",b"sourceType",u"versionId",b"versionId",u"workspaceBaseId",b"workspaceBaseId"]) -> None: ...

class GetVersionDetailResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> GetVersionDetailResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[GetVersionDetailResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetVersionDetailResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetVersionDetailResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
