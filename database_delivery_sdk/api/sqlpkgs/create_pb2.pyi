# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from model.database_delivery.sql_package_version_pb2 import (
    SQLPackageVersion as model___database_delivery___sql_package_version_pb2___SQLPackageVersion,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class CreateSQLPackageRequest(google___protobuf___message___Message):
    class CreateSqlpkg(google___protobuf___message___Message):
        name = ... # type: typing___Text
        dbType = ... # type: typing___Text
        memo = ... # type: typing___Text
        appPackageId = ... # type: typing___Text

        def __init__(self,
            name : typing___Optional[typing___Text] = None,
            dbType : typing___Optional[typing___Text] = None,
            memo : typing___Optional[typing___Text] = None,
            appPackageId : typing___Optional[typing___Text] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> CreateSQLPackageRequest.CreateSqlpkg: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"appPackageId",u"dbType",u"memo",u"name"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[b"appPackageId",b"dbType",b"memo",b"name"]) -> None: ...


    @property
    def createSqlpkg(self) -> CreateSQLPackageRequest.CreateSqlpkg: ...

    def __init__(self,
        createSqlpkg : typing___Optional[CreateSQLPackageRequest.CreateSqlpkg] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CreateSQLPackageRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"createSqlpkg"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"createSqlpkg"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"createSqlpkg",b"createSqlpkg"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"createSqlpkg"]) -> None: ...

class CreateSQLPackageResponse(google___protobuf___message___Message):
    id = ... # type: typing___Text
    name = ... # type: typing___Text
    dbType = ... # type: typing___Text
    memo = ... # type: typing___Text
    creator = ... # type: typing___Text
    ctime = ... # type: int
    mtime = ... # type: int
    appPackageId = ... # type: typing___Text
    repoPackageId = ... # type: typing___Text

    @property
    def versionList(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[model___database_delivery___sql_package_version_pb2___SQLPackageVersion]: ...

    def __init__(self,
        versionList : typing___Optional[typing___Iterable[model___database_delivery___sql_package_version_pb2___SQLPackageVersion]] = None,
        id : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        dbType : typing___Optional[typing___Text] = None,
        memo : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        ctime : typing___Optional[int] = None,
        mtime : typing___Optional[int] = None,
        appPackageId : typing___Optional[typing___Text] = None,
        repoPackageId : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CreateSQLPackageResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"appPackageId",u"creator",u"ctime",u"dbType",u"id",u"memo",u"mtime",u"name",u"repoPackageId",u"versionList"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"appPackageId",b"creator",b"ctime",b"dbType",b"id",b"memo",b"mtime",b"name",b"repoPackageId",b"versionList"]) -> None: ...

class CreateSQLPackageResponseWrapper(google___protobuf___message___Message):
    code = ... # type: int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> CreateSQLPackageResponse: ...

    def __init__(self,
        code : typing___Optional[int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[CreateSQLPackageResponse] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CreateSQLPackageResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"code",u"codeExplain",u"data",u"error"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"code",b"codeExplain",b"data",b"error"]) -> None: ...
