# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from model.agent_admin.plugin_version_pb2 import (
    PluginVersion as model___agent_admin___plugin_version_pb2___PluginVersion,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class UpdatePluginV1Request(google___protobuf___message___Message):
    id = ... # type: typing___Text
    name = ... # type: typing___Text
    memo = ... # type: typing___Text
    deployPath = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

    def __init__(self,
        id : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        memo : typing___Optional[typing___Text] = None,
        deployPath : typing___Optional[typing___Iterable[typing___Text]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> UpdatePluginV1Request: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"deployPath",u"id",u"memo",u"name"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"deployPath",b"id",b"memo",b"name"]) -> None: ...

class UpdatePluginV1Response(google___protobuf___message___Message):
    deployedCount = ... # type: int
    id = ... # type: typing___Text
    name = ... # type: typing___Text
    deployPath = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    memo = ... # type: typing___Text
    repoPackageId = ... # type: typing___Text
    creator = ... # type: typing___Text
    ctime = ... # type: int
    mtime = ... # type: int
    isLocked = ... # type: bool

    @property
    def lastestVersion(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[model___agent_admin___plugin_version_pb2___PluginVersion]: ...

    def __init__(self,
        lastestVersion : typing___Optional[typing___Iterable[model___agent_admin___plugin_version_pb2___PluginVersion]] = None,
        deployedCount : typing___Optional[int] = None,
        id : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        deployPath : typing___Optional[typing___Iterable[typing___Text]] = None,
        memo : typing___Optional[typing___Text] = None,
        repoPackageId : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        ctime : typing___Optional[int] = None,
        mtime : typing___Optional[int] = None,
        isLocked : typing___Optional[bool] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> UpdatePluginV1Response: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"creator",u"ctime",u"deployPath",u"deployedCount",u"id",u"isLocked",u"lastestVersion",u"memo",u"mtime",u"name",u"repoPackageId"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"creator",b"ctime",b"deployPath",b"deployedCount",b"id",b"isLocked",b"lastestVersion",b"memo",b"mtime",b"name",b"repoPackageId"]) -> None: ...

class UpdatePluginV1ResponseWrapper(google___protobuf___message___Message):
    code = ... # type: int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> UpdatePluginV1Response: ...

    def __init__(self,
        code : typing___Optional[int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[UpdatePluginV1Response] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> UpdatePluginV1ResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"code",u"codeExplain",u"data",u"error"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"code",b"codeExplain",b"data",b"error"]) -> None: ...
