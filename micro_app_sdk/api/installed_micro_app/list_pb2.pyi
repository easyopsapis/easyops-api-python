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

from google.protobuf.struct_pb2 import (
    Struct as google___protobuf___struct_pb2___Struct,
)

from micro_app_sdk.model.micro_app.micro_app_container_pb2 import (
    MicroAppContainer as micro_app_sdk___model___micro_app___micro_app_container_pb2___MicroAppContainer,
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


class ListMicroAppRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    page = ... # type: builtin___int
    page_size = ... # type: builtin___int

    def __init__(self,
        *,
        page : typing___Optional[builtin___int] = None,
        page_size : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListMicroAppRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListMicroAppRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"page",b"page",u"page_size",b"page_size"]) -> None: ...

class ListMicroAppResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class List(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class Icons(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            large = ... # type: typing___Text

            def __init__(self,
                *,
                large : typing___Optional[typing___Text] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> ListMicroAppResponse.List.Icons: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListMicroAppResponse.List.Icons: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"large",b"large"]) -> None: ...

        class ClonedFrom(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            appId = ... # type: typing___Text
            version = ... # type: typing___Text
            name = ... # type: typing___Text

            def __init__(self,
                *,
                appId : typing___Optional[typing___Text] = None,
                version : typing___Optional[typing___Text] = None,
                name : typing___Optional[typing___Text] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> ListMicroAppResponse.List.ClonedFrom: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListMicroAppResponse.List.ClonedFrom: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"appId",b"appId",u"name",b"name",u"version",b"version"]) -> None: ...

        class MenuIcon(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            lib = ... # type: typing___Text
            type = ... # type: typing___Text
            theme = ... # type: typing___Text
            icon = ... # type: typing___Text
            prefix = ... # type: typing___Text
            category = ... # type: typing___Text

            def __init__(self,
                *,
                lib : typing___Optional[typing___Text] = None,
                type : typing___Optional[typing___Text] = None,
                theme : typing___Optional[typing___Text] = None,
                icon : typing___Optional[typing___Text] = None,
                prefix : typing___Optional[typing___Text] = None,
                category : typing___Optional[typing___Text] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> ListMicroAppResponse.List.MenuIcon: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListMicroAppResponse.List.MenuIcon: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"category",b"category",u"icon",b"icon",u"lib",b"lib",u"prefix",b"prefix",u"theme",b"theme",u"type",b"type"]) -> None: ...

        instanceId = ... # type: typing___Text
        name = ... # type: typing___Text
        appId = ... # type: typing___Text
        storyboardJson = ... # type: typing___Text
        tags = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
        currentVersion = ... # type: typing___Text
        appVersion = ... # type: typing___Text
        installStatus = ... # type: typing___Text
        homepage = ... # type: typing___Text
        internal = ... # type: typing___Text
        private = ... # type: typing___Text
        owner = ... # type: typing___Text
        readme = ... # type: typing___Text
        status = ... # type: typing___Text
        ctime = ... # type: typing___Text
        mtime = ... # type: typing___Text
        pkgName = ... # type: typing___Text
        iconBackground = ... # type: typing___Text

        @property
        def container(self) -> micro_app_sdk___model___micro_app___micro_app_container_pb2___MicroAppContainer: ...

        @property
        def icons(self) -> ListMicroAppResponse.List.Icons: ...

        @property
        def clonedFrom(self) -> ListMicroAppResponse.List.ClonedFrom: ...

        @property
        def menuIcon(self) -> ListMicroAppResponse.List.MenuIcon: ...

        @property
        def defaultConfig(self) -> google___protobuf___struct_pb2___Struct: ...

        @property
        def userConfig(self) -> google___protobuf___struct_pb2___Struct: ...

        def __init__(self,
            *,
            container : typing___Optional[micro_app_sdk___model___micro_app___micro_app_container_pb2___MicroAppContainer] = None,
            instanceId : typing___Optional[typing___Text] = None,
            name : typing___Optional[typing___Text] = None,
            appId : typing___Optional[typing___Text] = None,
            icons : typing___Optional[ListMicroAppResponse.List.Icons] = None,
            storyboardJson : typing___Optional[typing___Text] = None,
            tags : typing___Optional[typing___Iterable[typing___Text]] = None,
            currentVersion : typing___Optional[typing___Text] = None,
            appVersion : typing___Optional[typing___Text] = None,
            installStatus : typing___Optional[typing___Text] = None,
            homepage : typing___Optional[typing___Text] = None,
            internal : typing___Optional[typing___Text] = None,
            private : typing___Optional[typing___Text] = None,
            clonedFrom : typing___Optional[ListMicroAppResponse.List.ClonedFrom] = None,
            owner : typing___Optional[typing___Text] = None,
            readme : typing___Optional[typing___Text] = None,
            status : typing___Optional[typing___Text] = None,
            ctime : typing___Optional[typing___Text] = None,
            mtime : typing___Optional[typing___Text] = None,
            pkgName : typing___Optional[typing___Text] = None,
            iconBackground : typing___Optional[typing___Text] = None,
            menuIcon : typing___Optional[ListMicroAppResponse.List.MenuIcon] = None,
            defaultConfig : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
            userConfig : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> ListMicroAppResponse.List: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListMicroAppResponse.List: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"clonedFrom",b"clonedFrom",u"container",b"container",u"defaultConfig",b"defaultConfig",u"icons",b"icons",u"menuIcon",b"menuIcon",u"userConfig",b"userConfig"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"appId",b"appId",u"appVersion",b"appVersion",u"clonedFrom",b"clonedFrom",u"container",b"container",u"ctime",b"ctime",u"currentVersion",b"currentVersion",u"defaultConfig",b"defaultConfig",u"homepage",b"homepage",u"iconBackground",b"iconBackground",u"icons",b"icons",u"installStatus",b"installStatus",u"instanceId",b"instanceId",u"internal",b"internal",u"menuIcon",b"menuIcon",u"mtime",b"mtime",u"name",b"name",u"owner",b"owner",u"pkgName",b"pkgName",u"private",b"private",u"readme",b"readme",u"status",b"status",u"storyboardJson",b"storyboardJson",u"tags",b"tags",u"userConfig",b"userConfig"]) -> None: ...

    page = ... # type: builtin___int
    page_size = ... # type: builtin___int
    total = ... # type: builtin___int

    @property
    def list(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ListMicroAppResponse.List]: ...

    def __init__(self,
        *,
        page : typing___Optional[builtin___int] = None,
        page_size : typing___Optional[builtin___int] = None,
        total : typing___Optional[builtin___int] = None,
        list : typing___Optional[typing___Iterable[ListMicroAppResponse.List]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListMicroAppResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListMicroAppResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"list",b"list",u"page",b"page",u"page_size",b"page_size",u"total",b"total"]) -> None: ...

class ListMicroAppResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> ListMicroAppResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[ListMicroAppResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListMicroAppResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListMicroAppResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
