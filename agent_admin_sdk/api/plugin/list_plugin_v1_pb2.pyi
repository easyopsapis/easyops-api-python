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


class ListPluginV1Request(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    page = ... # type: builtin___int
    pageSize = ... # type: builtin___int

    def __init__(self,
        *,
        page : typing___Optional[builtin___int] = None,
        pageSize : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListPluginV1Request: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListPluginV1Request: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"page",b"page",u"pageSize",b"pageSize"]) -> None: ...

class ListPluginV1Response(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class List(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class LastestVersion(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            id = ... # type: typing___Text
            repoVersionId = ... # type: typing___Text
            versionName = ... # type: typing___Text
            memo = ... # type: typing___Text
            pluginId = ... # type: typing___Text
            creator = ... # type: typing___Text
            ctime = ... # type: builtin___int
            mtime = ... # type: builtin___int

            def __init__(self,
                *,
                id : typing___Optional[typing___Text] = None,
                repoVersionId : typing___Optional[typing___Text] = None,
                versionName : typing___Optional[typing___Text] = None,
                memo : typing___Optional[typing___Text] = None,
                pluginId : typing___Optional[typing___Text] = None,
                creator : typing___Optional[typing___Text] = None,
                ctime : typing___Optional[builtin___int] = None,
                mtime : typing___Optional[builtin___int] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> ListPluginV1Response.List.LastestVersion: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListPluginV1Response.List.LastestVersion: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"creator",b"creator",u"ctime",b"ctime",u"id",b"id",u"memo",b"memo",u"mtime",b"mtime",u"pluginId",b"pluginId",u"repoVersionId",b"repoVersionId",u"versionName",b"versionName"]) -> None: ...

        deployedCount = ... # type: builtin___int
        id = ... # type: typing___Text
        name = ... # type: typing___Text
        deployPath = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
        memo = ... # type: typing___Text
        repoPackageId = ... # type: typing___Text
        creator = ... # type: typing___Text
        ctime = ... # type: builtin___int
        mtime = ... # type: builtin___int
        isLocked = ... # type: builtin___bool

        @property
        def lastestVersion(self) -> ListPluginV1Response.List.LastestVersion: ...

        def __init__(self,
            *,
            lastestVersion : typing___Optional[ListPluginV1Response.List.LastestVersion] = None,
            deployedCount : typing___Optional[builtin___int] = None,
            id : typing___Optional[typing___Text] = None,
            name : typing___Optional[typing___Text] = None,
            deployPath : typing___Optional[typing___Iterable[typing___Text]] = None,
            memo : typing___Optional[typing___Text] = None,
            repoPackageId : typing___Optional[typing___Text] = None,
            creator : typing___Optional[typing___Text] = None,
            ctime : typing___Optional[builtin___int] = None,
            mtime : typing___Optional[builtin___int] = None,
            isLocked : typing___Optional[builtin___bool] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> ListPluginV1Response.List: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListPluginV1Response.List: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"lastestVersion",b"lastestVersion"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"creator",b"creator",u"ctime",b"ctime",u"deployPath",b"deployPath",u"deployedCount",b"deployedCount",u"id",b"id",u"isLocked",b"isLocked",u"lastestVersion",b"lastestVersion",u"memo",b"memo",u"mtime",b"mtime",u"name",b"name",u"repoPackageId",b"repoPackageId"]) -> None: ...

    page = ... # type: builtin___int
    page_size = ... # type: builtin___int
    total = ... # type: builtin___int

    @property
    def list(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ListPluginV1Response.List]: ...

    def __init__(self,
        *,
        page : typing___Optional[builtin___int] = None,
        page_size : typing___Optional[builtin___int] = None,
        total : typing___Optional[builtin___int] = None,
        list : typing___Optional[typing___Iterable[ListPluginV1Response.List]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListPluginV1Response: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListPluginV1Response: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"list",b"list",u"page",b"page",u"page_size",b"page_size",u"total",b"total"]) -> None: ...

class ListPluginV1ResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> ListPluginV1Response: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[ListPluginV1Response] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListPluginV1ResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListPluginV1ResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
