# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from flowable_service_sdk.model.flowable_service.form_schema_version_pb2 import (
    FormSchemaVersion as flowable_service_sdk___model___flowable_service___form_schema_version_pb2___FormSchemaVersion,
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


class ListFormSchemaRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    page = ... # type: builtin___int
    pageSize = ... # type: builtin___int
    category = ... # type: typing___Text
    creator = ... # type: typing___Text
    isMain = ... # type: builtin___bool
    Q = ... # type: typing___Text
    name = ... # type: typing___Text
    state = ... # type: typing___Text

    def __init__(self,
        *,
        page : typing___Optional[builtin___int] = None,
        pageSize : typing___Optional[builtin___int] = None,
        category : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        isMain : typing___Optional[builtin___bool] = None,
        Q : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        state : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListFormSchemaRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListFormSchemaRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"Q",b"Q",u"category",b"category",u"creator",b"creator",u"isMain",b"isMain",u"name",b"name",u"page",b"page",u"pageSize",b"pageSize",u"state",b"state"]) -> None: ...

class ListFormSchemaResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class List(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        instanceId = ... # type: typing___Text
        name = ... # type: typing___Text
        category = ... # type: typing___Text
        memo = ... # type: typing___Text
        creator = ... # type: typing___Text
        ctime = ... # type: typing___Text

        @property
        def lastestMainVersion(self) -> flowable_service_sdk___model___flowable_service___form_schema_version_pb2___FormSchemaVersion: ...

        def __init__(self,
            *,
            lastestMainVersion : typing___Optional[flowable_service_sdk___model___flowable_service___form_schema_version_pb2___FormSchemaVersion] = None,
            instanceId : typing___Optional[typing___Text] = None,
            name : typing___Optional[typing___Text] = None,
            category : typing___Optional[typing___Text] = None,
            memo : typing___Optional[typing___Text] = None,
            creator : typing___Optional[typing___Text] = None,
            ctime : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> ListFormSchemaResponse.List: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListFormSchemaResponse.List: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"lastestMainVersion",b"lastestMainVersion"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"category",b"category",u"creator",b"creator",u"ctime",b"ctime",u"instanceId",b"instanceId",u"lastestMainVersion",b"lastestMainVersion",u"memo",b"memo",u"name",b"name"]) -> None: ...

    page = ... # type: builtin___int
    page_size = ... # type: builtin___int
    total = ... # type: builtin___int

    @property
    def list(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ListFormSchemaResponse.List]: ...

    def __init__(self,
        *,
        page : typing___Optional[builtin___int] = None,
        page_size : typing___Optional[builtin___int] = None,
        total : typing___Optional[builtin___int] = None,
        list : typing___Optional[typing___Iterable[ListFormSchemaResponse.List]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListFormSchemaResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListFormSchemaResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"list",b"list",u"page",b"page",u"page_size",b"page_size",u"total",b"total"]) -> None: ...

class ListFormSchemaResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> ListFormSchemaResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[ListFormSchemaResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListFormSchemaResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListFormSchemaResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...