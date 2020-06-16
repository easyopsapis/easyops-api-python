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
    Value as google___protobuf___struct_pb2___Value,
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


class InfluxdbQueryRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    db = ... # type: typing___Text
    q = ... # type: typing___Text
    epoch = ... # type: typing___Text
    translate = ... # type: builtin___bool

    def __init__(self,
        *,
        db : typing___Optional[typing___Text] = None,
        q : typing___Optional[typing___Text] = None,
        epoch : typing___Optional[typing___Text] = None,
        translate : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> InfluxdbQueryRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> InfluxdbQueryRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"db",b"db",u"epoch",b"epoch",u"q",b"q",u"translate",b"translate"]) -> None: ...

class InfluxdbQueryResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Results(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class Series(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            name = ... # type: typing___Text
            columns = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

            @property
            def values(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___protobuf___struct_pb2___Value]: ...

            @property
            def tags(self) -> google___protobuf___struct_pb2___Struct: ...

            def __init__(self,
                *,
                values : typing___Optional[typing___Iterable[google___protobuf___struct_pb2___Value]] = None,
                name : typing___Optional[typing___Text] = None,
                columns : typing___Optional[typing___Iterable[typing___Text]] = None,
                tags : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> InfluxdbQueryResponse.Results.Series: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> InfluxdbQueryResponse.Results.Series: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def HasField(self, field_name: typing_extensions___Literal[u"tags",b"tags"]) -> builtin___bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"columns",b"columns",u"name",b"name",u"tags",b"tags",u"values",b"values"]) -> None: ...

        error = ... # type: typing___Text
        statement_id = ... # type: builtin___int

        @property
        def series(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[InfluxdbQueryResponse.Results.Series]: ...

        def __init__(self,
            *,
            series : typing___Optional[typing___Iterable[InfluxdbQueryResponse.Results.Series]] = None,
            error : typing___Optional[typing___Text] = None,
            statement_id : typing___Optional[builtin___int] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> InfluxdbQueryResponse.Results: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> InfluxdbQueryResponse.Results: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"error",b"error",u"series",b"series",u"statement_id",b"statement_id"]) -> None: ...


    @property
    def results(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[InfluxdbQueryResponse.Results]: ...

    def __init__(self,
        *,
        results : typing___Optional[typing___Iterable[InfluxdbQueryResponse.Results]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> InfluxdbQueryResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> InfluxdbQueryResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"results",b"results"]) -> None: ...

class InfluxdbQueryResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> InfluxdbQueryResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[InfluxdbQueryResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> InfluxdbQueryResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> InfluxdbQueryResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
