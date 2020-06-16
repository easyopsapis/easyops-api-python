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


class RelationMaxCheckRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    objectId = ... # type: typing___Text
    relation_id = ... # type: typing___Text
    relation_side_id = ... # type: typing___Text
    permission = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    page = ... # type: builtin___int
    page_size = ... # type: builtin___int

    @property
    def query(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def sort(self) -> google___protobuf___struct_pb2___Struct: ...

    def __init__(self,
        *,
        objectId : typing___Optional[typing___Text] = None,
        relation_id : typing___Optional[typing___Text] = None,
        relation_side_id : typing___Optional[typing___Text] = None,
        query : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        sort : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        permission : typing___Optional[typing___Iterable[typing___Text]] = None,
        page : typing___Optional[builtin___int] = None,
        page_size : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> RelationMaxCheckRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> RelationMaxCheckRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"query",b"query",u"sort",b"sort"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"objectId",b"objectId",u"page",b"page",u"page_size",b"page_size",u"permission",b"permission",u"query",b"query",u"relation_id",b"relation_id",u"relation_side_id",b"relation_side_id",u"sort",b"sort"]) -> None: ...

class RelationMaxCheckResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class List(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        instanceId = ... # type: typing___Text
        _relation_is_max = ... # type: builtin___bool

        def __init__(self,
            *,
            instanceId : typing___Optional[typing___Text] = None,
            _relation_is_max : typing___Optional[builtin___bool] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> RelationMaxCheckResponse.List: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> RelationMaxCheckResponse.List: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"_relation_is_max",b"_relation_is_max",u"instanceId",b"instanceId"]) -> None: ...

    total = ... # type: builtin___int
    page = ... # type: builtin___int
    page_size = ... # type: builtin___int

    @property
    def list(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[RelationMaxCheckResponse.List]: ...

    def __init__(self,
        *,
        total : typing___Optional[builtin___int] = None,
        page : typing___Optional[builtin___int] = None,
        page_size : typing___Optional[builtin___int] = None,
        list : typing___Optional[typing___Iterable[RelationMaxCheckResponse.List]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> RelationMaxCheckResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> RelationMaxCheckResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"list",b"list",u"page",b"page",u"page_size",b"page_size",u"total",b"total"]) -> None: ...

class RelationMaxCheckResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> RelationMaxCheckResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[RelationMaxCheckResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> RelationMaxCheckResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> RelationMaxCheckResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
