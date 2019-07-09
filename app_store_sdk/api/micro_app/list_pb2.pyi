# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from model.app_store.app_version_pb2 import (
    AppVersion as model___app_store___app_version_pb2___AppVersion,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class ListAppStoreMicroAppRequest(google___protobuf___message___Message):
    class Query(google___protobuf___message___Message):
        name = ... # type: typing___Text
        id = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

        def __init__(self,
            name : typing___Optional[typing___Text] = None,
            id : typing___Optional[typing___Iterable[typing___Text]] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> ListAppStoreMicroAppRequest.Query: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"id",u"name"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[b"id",b"name"]) -> None: ...

    class Sort(google___protobuf___message___Message):
        name = ... # type: int

        def __init__(self,
            name : typing___Optional[int] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> ListAppStoreMicroAppRequest.Sort: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"name"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[b"name"]) -> None: ...

    page = ... # type: int
    page_size = ... # type: int

    @property
    def query(self) -> ListAppStoreMicroAppRequest.Query: ...

    @property
    def sort(self) -> ListAppStoreMicroAppRequest.Sort: ...

    def __init__(self,
        page : typing___Optional[int] = None,
        page_size : typing___Optional[int] = None,
        query : typing___Optional[ListAppStoreMicroAppRequest.Query] = None,
        sort : typing___Optional[ListAppStoreMicroAppRequest.Sort] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ListAppStoreMicroAppRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"query",u"sort"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"page",u"page_size",u"query",u"sort"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"query",b"query",u"sort",b"sort"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"page",b"page_size",b"query",b"sort"]) -> None: ...

class ListAppStoreMicroAppResponse(google___protobuf___message___Message):
    class List(google___protobuf___message___Message):
        class Icons(google___protobuf___message___Message):
            large = ... # type: typing___Text

            def __init__(self,
                large : typing___Optional[typing___Text] = None,
                ) -> None: ...
            @classmethod
            def FromString(cls, s: bytes) -> ListAppStoreMicroAppResponse.List.Icons: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            if sys.version_info >= (3,):
                def ClearField(self, field_name: typing_extensions___Literal[u"large"]) -> None: ...
            else:
                def ClearField(self, field_name: typing_extensions___Literal[b"large"]) -> None: ...

        name = ... # type: typing___Text
        id = ... # type: typing___Text
        intro = ... # type: typing___Text
        preview = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
        description = ... # type: typing___Text
        homepage = ... # type: typing___Text

        @property
        def currentVersion(self) -> model___app_store___app_version_pb2___AppVersion: ...

        @property
        def icons(self) -> ListAppStoreMicroAppResponse.List.Icons: ...

        def __init__(self,
            currentVersion : typing___Optional[model___app_store___app_version_pb2___AppVersion] = None,
            name : typing___Optional[typing___Text] = None,
            id : typing___Optional[typing___Text] = None,
            icons : typing___Optional[ListAppStoreMicroAppResponse.List.Icons] = None,
            intro : typing___Optional[typing___Text] = None,
            preview : typing___Optional[typing___Iterable[typing___Text]] = None,
            description : typing___Optional[typing___Text] = None,
            homepage : typing___Optional[typing___Text] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> ListAppStoreMicroAppResponse.List: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def HasField(self, field_name: typing_extensions___Literal[u"currentVersion",u"icons"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"currentVersion",u"description",u"homepage",u"icons",u"id",u"intro",u"name",u"preview"]) -> None: ...
        else:
            def HasField(self, field_name: typing_extensions___Literal[u"currentVersion",b"currentVersion",u"icons",b"icons"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[b"currentVersion",b"description",b"homepage",b"icons",b"id",b"intro",b"name",b"preview"]) -> None: ...

    total = ... # type: int
    page = ... # type: int
    page_size = ... # type: int

    @property
    def list(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ListAppStoreMicroAppResponse.List]: ...

    def __init__(self,
        total : typing___Optional[int] = None,
        page : typing___Optional[int] = None,
        page_size : typing___Optional[int] = None,
        list : typing___Optional[typing___Iterable[ListAppStoreMicroAppResponse.List]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ListAppStoreMicroAppResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"list",u"page",u"page_size",u"total"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"list",b"page",b"page_size",b"total"]) -> None: ...

class ListAppStoreMicroAppResponseWrapper(google___protobuf___message___Message):
    code = ... # type: int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> ListAppStoreMicroAppResponse: ...

    def __init__(self,
        code : typing___Optional[int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[ListAppStoreMicroAppResponse] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ListAppStoreMicroAppResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"code",u"codeExplain",u"data",u"error"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"code",b"codeExplain",b"data",b"error"]) -> None: ...
