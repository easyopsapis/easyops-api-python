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


class SearchAppInSystemRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    systemInstanceId = ... # type: typing___Text
    page = ... # type: builtin___int
    page_size = ... # type: builtin___int
    permission = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    only_relation_view = ... # type: builtin___bool
    only_my_instance = ... # type: builtin___bool
    include_sub_systems = ... # type: builtin___bool

    @property
    def query(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def fields(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def sort(self) -> google___protobuf___struct_pb2___Struct: ...

    def __init__(self,
        *,
        systemInstanceId : typing___Optional[typing___Text] = None,
        page : typing___Optional[builtin___int] = None,
        page_size : typing___Optional[builtin___int] = None,
        query : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        fields : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        sort : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        permission : typing___Optional[typing___Iterable[typing___Text]] = None,
        only_relation_view : typing___Optional[builtin___bool] = None,
        only_my_instance : typing___Optional[builtin___bool] = None,
        include_sub_systems : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> SearchAppInSystemRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> SearchAppInSystemRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"fields",b"fields",u"query",b"query",u"sort",b"sort"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"fields",b"fields",u"include_sub_systems",b"include_sub_systems",u"only_my_instance",b"only_my_instance",u"only_relation_view",b"only_relation_view",u"page",b"page",u"page_size",b"page_size",u"permission",b"permission",u"query",b"query",u"sort",b"sort",u"systemInstanceId",b"systemInstanceId"]) -> None: ...

class SearchAppInSystemResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    total = ... # type: builtin___int
    page = ... # type: builtin___int
    page_size = ... # type: builtin___int

    @property
    def list(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___protobuf___struct_pb2___Struct]: ...

    def __init__(self,
        *,
        total : typing___Optional[builtin___int] = None,
        page : typing___Optional[builtin___int] = None,
        page_size : typing___Optional[builtin___int] = None,
        list : typing___Optional[typing___Iterable[google___protobuf___struct_pb2___Struct]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> SearchAppInSystemResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> SearchAppInSystemResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"list",b"list",u"page",b"page",u"page_size",b"page_size",u"total",b"total"]) -> None: ...

class SearchAppInSystemResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> SearchAppInSystemResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[SearchAppInSystemResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> SearchAppInSystemResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> SearchAppInSystemResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
