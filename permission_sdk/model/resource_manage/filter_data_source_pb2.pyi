# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.struct_pb2 import (
    Value as google___protobuf___struct_pb2___Value,
)

from typing import (
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


class FilterDataSource(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Const(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        type = ... # type: typing___Text

        @property
        def value(self) -> google___protobuf___struct_pb2___Value: ...

        def __init__(self,
            *,
            type : typing___Optional[typing___Text] = None,
            value : typing___Optional[google___protobuf___struct_pb2___Value] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> FilterDataSource.Const: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> FilterDataSource.Const: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"type",b"type",u"value",b"value"]) -> None: ...

    class Mapping(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key_path = ... # type: typing___Text

        def __init__(self,
            *,
            key_path : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> FilterDataSource.Mapping: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> FilterDataSource.Mapping: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key_path",b"key_path"]) -> None: ...

    class Expression(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        operator = ... # type: typing___Text

        @property
        def left(self) -> FilterDataSource: ...

        @property
        def right(self) -> FilterDataSource: ...

        def __init__(self,
            *,
            operator : typing___Optional[typing___Text] = None,
            left : typing___Optional[FilterDataSource] = None,
            right : typing___Optional[FilterDataSource] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> FilterDataSource.Expression: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> FilterDataSource.Expression: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"left",b"left",u"right",b"right"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"left",b"left",u"operator",b"operator",u"right",b"right"]) -> None: ...

    class Time(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        type = ... # type: typing___Text
        static = ... # type: typing___Text
        unit = ... # type: typing___Text
        offset = ... # type: builtin___int

        def __init__(self,
            *,
            type : typing___Optional[typing___Text] = None,
            static : typing___Optional[typing___Text] = None,
            unit : typing___Optional[typing___Text] = None,
            offset : typing___Optional[builtin___int] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> FilterDataSource.Time: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> FilterDataSource.Time: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"offset",b"offset",u"static",b"static",u"type",b"type",u"unit",b"unit"]) -> None: ...

    type = ... # type: typing___Text
    format = ... # type: typing___Text

    @property
    def const(self) -> FilterDataSource.Const: ...

    @property
    def mapping(self) -> FilterDataSource.Mapping: ...

    @property
    def expression(self) -> FilterDataSource.Expression: ...

    @property
    def time(self) -> FilterDataSource.Time: ...

    def __init__(self,
        *,
        type : typing___Optional[typing___Text] = None,
        const : typing___Optional[FilterDataSource.Const] = None,
        mapping : typing___Optional[FilterDataSource.Mapping] = None,
        expression : typing___Optional[FilterDataSource.Expression] = None,
        time : typing___Optional[FilterDataSource.Time] = None,
        format : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> FilterDataSource: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> FilterDataSource: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"const",b"const",u"expression",b"expression",u"mapping",b"mapping",u"time",b"time"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"const",b"const",u"expression",b"expression",u"format",b"format",u"mapping",b"mapping",u"time",b"time",u"type",b"type"]) -> None: ...
