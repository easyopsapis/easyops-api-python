# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from easy_flow_sdk.model.file_repository.diff_pb2 import (
    Diff as easy_flow_sdk___model___file_repository___diff_pb2___Diff,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
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


class VersionInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class SourceDecode(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        ensName = ... # type: typing___Text
        host = ... # type: typing___Text
        type = ... # type: typing___Text
        ip = ... # type: typing___Text
        port = ... # type: builtin___int

        def __init__(self,
            *,
            ensName : typing___Optional[typing___Text] = None,
            host : typing___Optional[typing___Text] = None,
            type : typing___Optional[typing___Text] = None,
            ip : typing___Optional[typing___Text] = None,
            port : typing___Optional[builtin___int] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> VersionInfo.SourceDecode: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> VersionInfo.SourceDecode: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"ensName",b"ensName",u"host",b"host",u"ip",b"ip",u"port",b"port",u"type",b"type"]) -> None: ...

    repoVersion = ... # type: typing___Text
    source = ... # type: typing___Text
    packageId = ... # type: typing___Text
    versionId = ... # type: typing___Text
    name = ... # type: typing___Text
    creator = ... # type: typing___Text
    org = ... # type: builtin___int
    memo = ... # type: typing___Text
    ctime = ... # type: typing___Text
    mtime = ... # type: typing___Text
    sign = ... # type: typing___Text
    sourceType = ... # type: typing___Text
    conf = ... # type: typing___Text
    env_type = ... # type: builtin___int

    @property
    def sourceDecode(self) -> VersionInfo.SourceDecode: ...

    @property
    def diff(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[easy_flow_sdk___model___file_repository___diff_pb2___Diff]: ...

    def __init__(self,
        *,
        repoVersion : typing___Optional[typing___Text] = None,
        source : typing___Optional[typing___Text] = None,
        sourceDecode : typing___Optional[VersionInfo.SourceDecode] = None,
        diff : typing___Optional[typing___Iterable[easy_flow_sdk___model___file_repository___diff_pb2___Diff]] = None,
        packageId : typing___Optional[typing___Text] = None,
        versionId : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        org : typing___Optional[builtin___int] = None,
        memo : typing___Optional[typing___Text] = None,
        ctime : typing___Optional[typing___Text] = None,
        mtime : typing___Optional[typing___Text] = None,
        sign : typing___Optional[typing___Text] = None,
        sourceType : typing___Optional[typing___Text] = None,
        conf : typing___Optional[typing___Text] = None,
        env_type : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> VersionInfo: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> VersionInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"sourceDecode",b"sourceDecode"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"conf",b"conf",u"creator",b"creator",u"ctime",b"ctime",u"diff",b"diff",u"env_type",b"env_type",u"memo",b"memo",u"mtime",b"mtime",u"name",b"name",u"org",b"org",u"packageId",b"packageId",u"repoVersion",b"repoVersion",u"sign",b"sign",u"source",b"source",u"sourceDecode",b"sourceDecode",u"sourceType",b"sourceType",u"versionId",b"versionId"]) -> None: ...
