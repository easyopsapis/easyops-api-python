# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
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


class SearchRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    page = ... # type: builtin___int
    pageSize = ... # type: builtin___int
    order = ... # type: typing___Text
    exact = ... # type: typing___Text
    XXX_RestFieldMask = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    name = ... # type: typing___Text
    type = ... # type: builtin___int
    cId = ... # type: builtin___int
    category = ... # type: typing___Text

    def __init__(self,
        *,
        page : typing___Optional[builtin___int] = None,
        pageSize : typing___Optional[builtin___int] = None,
        order : typing___Optional[typing___Text] = None,
        exact : typing___Optional[typing___Text] = None,
        XXX_RestFieldMask : typing___Optional[typing___Iterable[typing___Text]] = None,
        name : typing___Optional[typing___Text] = None,
        type : typing___Optional[builtin___int] = None,
        cId : typing___Optional[builtin___int] = None,
        category : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> SearchRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> SearchRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"XXX_RestFieldMask",b"XXX_RestFieldMask",u"cId",b"cId",u"category",b"category",u"exact",b"exact",u"name",b"name",u"order",b"order",u"page",b"page",u"pageSize",b"pageSize",u"type",b"type"]) -> None: ...

class SearchResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class List(google___protobuf___message___Message):
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
                def FromString(cls, s: builtin___bytes) -> SearchResponse.List.LastVersionInfo: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> SearchResponse.List.LastVersionInfo: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"ctime",b"ctime",u"env_type",b"env_type",u"memo",b"memo",u"name",b"name",u"versionId",b"versionId"]) -> None: ...

        packageId = ... # type: typing___Text
        name = ... # type: typing___Text
        type = ... # type: builtin___int
        cId = ... # type: builtin___int
        source = ... # type: typing___Text
        repoId = ... # type: typing___Text
        repoPath = ... # type: typing___Text
        memo = ... # type: typing___Text
        creator = ... # type: typing___Text
        org = ... # type: builtin___int
        category = ... # type: typing___Text
        icon = ... # type: typing___Text
        style = ... # type: typing___Text
        ctime = ... # type: typing___Text
        mtime = ... # type: typing___Text
        authUsers = ... # type: typing___Text
        installPath = ... # type: typing___Text
        platform = ... # type: typing___Text
        instanceCount = ... # type: builtin___int

        @property
        def lastVersionInfo(self) -> SearchResponse.List.LastVersionInfo: ...

        def __init__(self,
            *,
            packageId : typing___Optional[typing___Text] = None,
            name : typing___Optional[typing___Text] = None,
            type : typing___Optional[builtin___int] = None,
            cId : typing___Optional[builtin___int] = None,
            source : typing___Optional[typing___Text] = None,
            repoId : typing___Optional[typing___Text] = None,
            repoPath : typing___Optional[typing___Text] = None,
            memo : typing___Optional[typing___Text] = None,
            creator : typing___Optional[typing___Text] = None,
            org : typing___Optional[builtin___int] = None,
            category : typing___Optional[typing___Text] = None,
            icon : typing___Optional[typing___Text] = None,
            style : typing___Optional[typing___Text] = None,
            ctime : typing___Optional[typing___Text] = None,
            mtime : typing___Optional[typing___Text] = None,
            authUsers : typing___Optional[typing___Text] = None,
            installPath : typing___Optional[typing___Text] = None,
            platform : typing___Optional[typing___Text] = None,
            lastVersionInfo : typing___Optional[SearchResponse.List.LastVersionInfo] = None,
            instanceCount : typing___Optional[builtin___int] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> SearchResponse.List: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> SearchResponse.List: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"lastVersionInfo",b"lastVersionInfo"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"authUsers",b"authUsers",u"cId",b"cId",u"category",b"category",u"creator",b"creator",u"ctime",b"ctime",u"icon",b"icon",u"installPath",b"installPath",u"instanceCount",b"instanceCount",u"lastVersionInfo",b"lastVersionInfo",u"memo",b"memo",u"mtime",b"mtime",u"name",b"name",u"org",b"org",u"packageId",b"packageId",u"platform",b"platform",u"repoId",b"repoId",u"repoPath",b"repoPath",u"source",b"source",u"style",b"style",u"type",b"type"]) -> None: ...

    page = ... # type: builtin___int
    page_size = ... # type: builtin___int
    total = ... # type: builtin___int

    @property
    def list(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[SearchResponse.List]: ...

    def __init__(self,
        *,
        page : typing___Optional[builtin___int] = None,
        page_size : typing___Optional[builtin___int] = None,
        total : typing___Optional[builtin___int] = None,
        list : typing___Optional[typing___Iterable[SearchResponse.List]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> SearchResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> SearchResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"list",b"list",u"page",b"page",u"page_size",b"page_size",u"total",b"total"]) -> None: ...

class SearchResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> SearchResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[SearchResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> SearchResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> SearchResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
