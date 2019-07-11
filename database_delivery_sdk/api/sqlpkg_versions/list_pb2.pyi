# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
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
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class ListSQLPackageVersionRequest(google___protobuf___message___Message):
    pkgId = ... # type: typing___Text
    page = ... # type: int
    pageSize = ... # type: int

    def __init__(self,
        pkgId : typing___Optional[typing___Text] = None,
        page : typing___Optional[int] = None,
        pageSize : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ListSQLPackageVersionRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"page",u"pageSize",u"pkgId"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"page",b"pageSize",b"pkgId"]) -> None: ...

class ListSQLPackageVersionResponse(google___protobuf___message___Message):
    class List(google___protobuf___message___Message):
        class SqlPackage(google___protobuf___message___Message):
            id = ... # type: typing___Text
            name = ... # type: typing___Text
            memo = ... # type: typing___Text
            repoPackageId = ... # type: typing___Text
            creator = ... # type: typing___Text
            mtime = ... # type: int

            def __init__(self,
                id : typing___Optional[typing___Text] = None,
                name : typing___Optional[typing___Text] = None,
                memo : typing___Optional[typing___Text] = None,
                repoPackageId : typing___Optional[typing___Text] = None,
                creator : typing___Optional[typing___Text] = None,
                mtime : typing___Optional[int] = None,
                ) -> None: ...
            @classmethod
            def FromString(cls, s: bytes) -> ListSQLPackageVersionResponse.List.SqlPackage: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            if sys.version_info >= (3,):
                def ClearField(self, field_name: typing_extensions___Literal[u"creator",u"id",u"memo",u"mtime",u"name",u"repoPackageId"]) -> None: ...
            else:
                def ClearField(self, field_name: typing_extensions___Literal[b"creator",b"id",b"memo",b"mtime",b"name",b"repoPackageId"]) -> None: ...

        id = ... # type: typing___Text
        name = ... # type: typing___Text
        repoVersionId = ... # type: typing___Text
        appVersionId = ... # type: typing___Text
        versionName = ... # type: typing___Text
        memo = ... # type: typing___Text
        creator = ... # type: typing___Text
        ctime = ... # type: int
        mtime = ... # type: int

        @property
        def sqlPackage(self) -> ListSQLPackageVersionResponse.List.SqlPackage: ...

        def __init__(self,
            sqlPackage : typing___Optional[ListSQLPackageVersionResponse.List.SqlPackage] = None,
            id : typing___Optional[typing___Text] = None,
            name : typing___Optional[typing___Text] = None,
            repoVersionId : typing___Optional[typing___Text] = None,
            appVersionId : typing___Optional[typing___Text] = None,
            versionName : typing___Optional[typing___Text] = None,
            memo : typing___Optional[typing___Text] = None,
            creator : typing___Optional[typing___Text] = None,
            ctime : typing___Optional[int] = None,
            mtime : typing___Optional[int] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> ListSQLPackageVersionResponse.List: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def HasField(self, field_name: typing_extensions___Literal[u"sqlPackage"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"appVersionId",u"creator",u"ctime",u"id",u"memo",u"mtime",u"name",u"repoVersionId",u"sqlPackage",u"versionName"]) -> None: ...
        else:
            def HasField(self, field_name: typing_extensions___Literal[u"sqlPackage",b"sqlPackage"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[b"appVersionId",b"creator",b"ctime",b"id",b"memo",b"mtime",b"name",b"repoVersionId",b"sqlPackage",b"versionName"]) -> None: ...

    page = ... # type: int
    page_size = ... # type: int
    total = ... # type: int

    @property
    def list(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ListSQLPackageVersionResponse.List]: ...

    def __init__(self,
        page : typing___Optional[int] = None,
        page_size : typing___Optional[int] = None,
        total : typing___Optional[int] = None,
        list : typing___Optional[typing___Iterable[ListSQLPackageVersionResponse.List]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ListSQLPackageVersionResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"list",u"page",u"page_size",u"total"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"list",b"page",b"page_size",b"total"]) -> None: ...

class ListSQLPackageVersionResponseWrapper(google___protobuf___message___Message):
    code = ... # type: int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> ListSQLPackageVersionResponse: ...

    def __init__(self,
        code : typing___Optional[int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[ListSQLPackageVersionResponse] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ListSQLPackageVersionResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"code",u"codeExplain",u"data",u"error"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"code",b"codeExplain",b"data",b"error"]) -> None: ...
