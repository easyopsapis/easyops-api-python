# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
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
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class RelationCountAggregateRequest(google___protobuf___message___Message):
    objectId = ... # type: typing___Text
    relation_side_ids = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    only_my_instance = ... # type: bool

    @property
    def query(self) -> google___protobuf___struct_pb2___Struct: ...

    def __init__(self,
        objectId : typing___Optional[typing___Text] = None,
        query : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        relation_side_ids : typing___Optional[typing___Iterable[typing___Text]] = None,
        only_my_instance : typing___Optional[bool] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> RelationCountAggregateRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"query"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"objectId",u"only_my_instance",u"query",u"relation_side_ids"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"query",b"query"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"objectId",b"only_my_instance",b"query",b"relation_side_ids"]) -> None: ...

class RelationCountAggregateResponse(google___protobuf___message___Message):
    class Data(google___protobuf___message___Message):
        key = ... # type: typing___Text
        value = ... # type: int

        def __init__(self,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[int] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> RelationCountAggregateResponse.Data: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"key",u"value"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[b"key",b"value"]) -> None: ...

    code = ... # type: int
    error = ... # type: typing___Text
    message = ... # type: typing___Text

    @property
    def data(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[RelationCountAggregateResponse.Data]: ...

    def __init__(self,
        code : typing___Optional[int] = None,
        error : typing___Optional[typing___Text] = None,
        message : typing___Optional[typing___Text] = None,
        data : typing___Optional[typing___Iterable[RelationCountAggregateResponse.Data]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> RelationCountAggregateResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"code",u"data",u"error",u"message"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"code",b"data",b"error",b"message"]) -> None: ...

class RelationCountAggregateResponseWrapper(google___protobuf___message___Message):
    code = ... # type: int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> RelationCountAggregateResponse: ...

    def __init__(self,
        code : typing___Optional[int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[RelationCountAggregateResponse] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> RelationCountAggregateResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"code",u"codeExplain",u"data",u"error"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"code",b"codeExplain",b"data",b"error"]) -> None: ...
