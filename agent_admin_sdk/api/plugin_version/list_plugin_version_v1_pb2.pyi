# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from agent_admin_sdk.model.agent_admin.plugin_pb2 import (
    Plugin as agent_admin_sdk___model___agent_admin___plugin_pb2___Plugin,
)

from agent_admin_sdk.model.agent_admin.plugin_version_pb2 import (
    PluginVersion as agent_admin_sdk___model___agent_admin___plugin_version_pb2___PluginVersion,
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


class ListPluginVersionV1Request(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    id = ... # type: typing___Text
    page = ... # type: builtin___int
    pageSize = ... # type: builtin___int

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        page : typing___Optional[builtin___int] = None,
        pageSize : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListPluginVersionV1Request: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListPluginVersionV1Request: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id",u"page",b"page",u"pageSize",b"pageSize"]) -> None: ...

class ListPluginVersionV1Response(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class List(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        versionName = ... # type: typing___Text
        deployedCount = ... # type: builtin___int
        id = ... # type: typing___Text
        repoVersionId = ... # type: typing___Text
        name = ... # type: typing___Text
        memo = ... # type: typing___Text
        pluginId = ... # type: typing___Text
        creator = ... # type: typing___Text
        ctime = ... # type: builtin___int
        mtime = ... # type: builtin___int

        @property
        def agentPlugin(self) -> agent_admin_sdk___model___agent_admin___plugin_pb2___Plugin: ...

        @property
        def baseVersion(self) -> agent_admin_sdk___model___agent_admin___plugin_version_pb2___PluginVersion: ...

        def __init__(self,
            *,
            versionName : typing___Optional[typing___Text] = None,
            agentPlugin : typing___Optional[agent_admin_sdk___model___agent_admin___plugin_pb2___Plugin] = None,
            baseVersion : typing___Optional[agent_admin_sdk___model___agent_admin___plugin_version_pb2___PluginVersion] = None,
            deployedCount : typing___Optional[builtin___int] = None,
            id : typing___Optional[typing___Text] = None,
            repoVersionId : typing___Optional[typing___Text] = None,
            name : typing___Optional[typing___Text] = None,
            memo : typing___Optional[typing___Text] = None,
            pluginId : typing___Optional[typing___Text] = None,
            creator : typing___Optional[typing___Text] = None,
            ctime : typing___Optional[builtin___int] = None,
            mtime : typing___Optional[builtin___int] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> ListPluginVersionV1Response.List: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListPluginVersionV1Response.List: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"agentPlugin",b"agentPlugin",u"baseVersion",b"baseVersion"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"agentPlugin",b"agentPlugin",u"baseVersion",b"baseVersion",u"creator",b"creator",u"ctime",b"ctime",u"deployedCount",b"deployedCount",u"id",b"id",u"memo",b"memo",u"mtime",b"mtime",u"name",b"name",u"pluginId",b"pluginId",u"repoVersionId",b"repoVersionId",u"versionName",b"versionName"]) -> None: ...

    page = ... # type: builtin___int
    page_size = ... # type: builtin___int
    total = ... # type: builtin___int

    @property
    def list(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ListPluginVersionV1Response.List]: ...

    def __init__(self,
        *,
        page : typing___Optional[builtin___int] = None,
        page_size : typing___Optional[builtin___int] = None,
        total : typing___Optional[builtin___int] = None,
        list : typing___Optional[typing___Iterable[ListPluginVersionV1Response.List]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListPluginVersionV1Response: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListPluginVersionV1Response: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"list",b"list",u"page",b"page",u"page_size",b"page_size",u"total",b"total"]) -> None: ...

class ListPluginVersionV1ResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> ListPluginVersionV1Response: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[ListPluginVersionV1Response] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListPluginVersionV1ResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListPluginVersionV1ResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
