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


class ListPluginTaskRequest(google___protobuf___message___Message):
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
        def FromString(cls, s: builtin___bytes) -> ListPluginTaskRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListPluginTaskRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id",u"page",b"page",u"pageSize",b"pageSize"]) -> None: ...

class ListPluginTaskResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class List(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class DeployList(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            agentId = ... # type: typing___Text
            ip = ... # type: typing___Text
            deployPath = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
            agentPluginId = ... # type: typing___Text
            agentPluginName = ... # type: typing___Text
            preVersionName = ... # type: typing___Text
            pluginVersionName = ... # type: typing___Text
            status = ... # type: typing___Text

            def __init__(self,
                *,
                agentId : typing___Optional[typing___Text] = None,
                ip : typing___Optional[typing___Text] = None,
                deployPath : typing___Optional[typing___Iterable[typing___Text]] = None,
                agentPluginId : typing___Optional[typing___Text] = None,
                agentPluginName : typing___Optional[typing___Text] = None,
                preVersionName : typing___Optional[typing___Text] = None,
                pluginVersionName : typing___Optional[typing___Text] = None,
                status : typing___Optional[typing___Text] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> ListPluginTaskResponse.List.DeployList: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListPluginTaskResponse.List.DeployList: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"agentId",b"agentId",u"agentPluginId",b"agentPluginId",u"agentPluginName",b"agentPluginName",u"deployPath",b"deployPath",u"ip",b"ip",u"pluginVersionName",b"pluginVersionName",u"preVersionName",b"preVersionName",u"status",b"status"]) -> None: ...

        targetId = ... # type: typing___Text
        targetName = ... # type: typing___Text
        creator = ... # type: typing___Text
        status = ... # type: typing___Text
        ctime = ... # type: builtin___int
        etime = ... # type: builtin___int

        @property
        def deployList(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ListPluginTaskResponse.List.DeployList]: ...

        def __init__(self,
            *,
            targetId : typing___Optional[typing___Text] = None,
            targetName : typing___Optional[typing___Text] = None,
            creator : typing___Optional[typing___Text] = None,
            status : typing___Optional[typing___Text] = None,
            ctime : typing___Optional[builtin___int] = None,
            etime : typing___Optional[builtin___int] = None,
            deployList : typing___Optional[typing___Iterable[ListPluginTaskResponse.List.DeployList]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> ListPluginTaskResponse.List: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListPluginTaskResponse.List: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"creator",b"creator",u"ctime",b"ctime",u"deployList",b"deployList",u"etime",b"etime",u"status",b"status",u"targetId",b"targetId",u"targetName",b"targetName"]) -> None: ...

    page = ... # type: builtin___int
    page_size = ... # type: builtin___int
    total = ... # type: builtin___int

    @property
    def list(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ListPluginTaskResponse.List]: ...

    def __init__(self,
        *,
        page : typing___Optional[builtin___int] = None,
        page_size : typing___Optional[builtin___int] = None,
        total : typing___Optional[builtin___int] = None,
        list : typing___Optional[typing___Iterable[ListPluginTaskResponse.List]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListPluginTaskResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListPluginTaskResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"list",b"list",u"page",b"page",u"page_size",b"page_size",u"total",b"total"]) -> None: ...

class ListPluginTaskResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> ListPluginTaskResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[ListPluginTaskResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListPluginTaskResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListPluginTaskResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...