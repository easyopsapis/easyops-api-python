# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from model.agent_admin.plugin_pb2 import (
    Plugin as model___agent_admin___plugin_pb2___Plugin,
)

from model.agent_admin.plugin_version_pb2 import (
    PluginVersion as model___agent_admin___plugin_version_pb2___PluginVersion,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class UpdatePluginVersionV1Request(google___protobuf___message___Message):
    id = ... # type: typing___Text
    verId = ... # type: typing___Text
    name = ... # type: typing___Text
    memo = ... # type: typing___Text

    def __init__(self,
        id : typing___Optional[typing___Text] = None,
        verId : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        memo : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> UpdatePluginVersionV1Request: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"id",u"memo",u"name",u"verId"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"id",b"memo",b"name",b"verId"]) -> None: ...

class UpdatePluginVersionV1Response(google___protobuf___message___Message):
    versionName = ... # type: typing___Text
    id = ... # type: typing___Text
    repoVersionId = ... # type: typing___Text
    name = ... # type: typing___Text
    memo = ... # type: typing___Text
    pluginId = ... # type: typing___Text
    creator = ... # type: typing___Text
    ctime = ... # type: int
    mtime = ... # type: int

    @property
    def agentPlugin(self) -> model___agent_admin___plugin_pb2___Plugin: ...

    @property
    def baseVersion(self) -> model___agent_admin___plugin_version_pb2___PluginVersion: ...

    def __init__(self,
        versionName : typing___Optional[typing___Text] = None,
        agentPlugin : typing___Optional[model___agent_admin___plugin_pb2___Plugin] = None,
        baseVersion : typing___Optional[model___agent_admin___plugin_version_pb2___PluginVersion] = None,
        id : typing___Optional[typing___Text] = None,
        repoVersionId : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        memo : typing___Optional[typing___Text] = None,
        pluginId : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        ctime : typing___Optional[int] = None,
        mtime : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> UpdatePluginVersionV1Response: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"agentPlugin",u"baseVersion"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"agentPlugin",u"baseVersion",u"creator",u"ctime",u"id",u"memo",u"mtime",u"name",u"pluginId",u"repoVersionId",u"versionName"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"agentPlugin",b"agentPlugin",u"baseVersion",b"baseVersion"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"agentPlugin",b"baseVersion",b"creator",b"ctime",b"id",b"memo",b"mtime",b"name",b"pluginId",b"repoVersionId",b"versionName"]) -> None: ...

class UpdatePluginVersionV1ResponseWrapper(google___protobuf___message___Message):
    code = ... # type: int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> UpdatePluginVersionV1Response: ...

    def __init__(self,
        code : typing___Optional[int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[UpdatePluginVersionV1Response] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> UpdatePluginVersionV1ResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"code",u"codeExplain",u"data",u"error"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"code",b"codeExplain",b"data",b"error"]) -> None: ...