# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
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


class Metrics(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Formats(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class Fields(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            field_type = ... # type: typing___Text
            description = ... # type: typing___Text
            field_name = ... # type: typing___Text
            field_value_type = ... # type: typing___Text
            stat_period = ... # type: builtin___int
            stat_type = ... # type: typing___Text
            unit = ... # type: typing___Text
            column_name = ... # type: typing___Text

            def __init__(self,
                *,
                field_type : typing___Optional[typing___Text] = None,
                description : typing___Optional[typing___Text] = None,
                field_name : typing___Optional[typing___Text] = None,
                field_value_type : typing___Optional[typing___Text] = None,
                stat_period : typing___Optional[builtin___int] = None,
                stat_type : typing___Optional[typing___Text] = None,
                unit : typing___Optional[typing___Text] = None,
                column_name : typing___Optional[typing___Text] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> Metrics.Formats.Fields: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Metrics.Formats.Fields: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"column_name",b"column_name",u"description",b"description",u"field_name",b"field_name",u"field_type",b"field_type",u"field_value_type",b"field_value_type",u"stat_period",b"stat_period",u"stat_type",b"stat_type",u"unit",b"unit"]) -> None: ...

        config_id = ... # type: typing___Text
        max_int_col = ... # type: builtin___int
        max_string_col = ... # type: builtin___int
        max_text_col = ... # type: builtin___int
        max_double_col = ... # type: builtin___int
        max_dim_col = ... # type: builtin___int
        table = ... # type: typing___Text
        aggregation = ... # type: builtin___bool

        @property
        def fields(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Metrics.Formats.Fields]: ...

        def __init__(self,
            *,
            config_id : typing___Optional[typing___Text] = None,
            max_int_col : typing___Optional[builtin___int] = None,
            max_string_col : typing___Optional[builtin___int] = None,
            max_text_col : typing___Optional[builtin___int] = None,
            max_double_col : typing___Optional[builtin___int] = None,
            max_dim_col : typing___Optional[builtin___int] = None,
            table : typing___Optional[typing___Text] = None,
            aggregation : typing___Optional[builtin___bool] = None,
            fields : typing___Optional[typing___Iterable[Metrics.Formats.Fields]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Metrics.Formats: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Metrics.Formats: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"aggregation",b"aggregation",u"config_id",b"config_id",u"fields",b"fields",u"max_dim_col",b"max_dim_col",u"max_double_col",b"max_double_col",u"max_int_col",b"max_int_col",u"max_string_col",b"max_string_col",u"max_text_col",b"max_text_col",u"table",b"table"]) -> None: ...

    retention_policy = ... # type: typing___Text
    description = ... # type: typing___Text
    data_type = ... # type: typing___Text
    data_name = ... # type: typing___Text
    custom = ... # type: builtin___bool
    version = ... # type: builtin___float
    org = ... # type: builtin___int
    _id = ... # type: typing___Text
    creator = ... # type: typing___Text
    modifier = ... # type: typing___Text
    ctime = ... # type: typing___Text
    mtime = ... # type: typing___Text

    @property
    def formats(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Metrics.Formats]: ...

    def __init__(self,
        *,
        retention_policy : typing___Optional[typing___Text] = None,
        description : typing___Optional[typing___Text] = None,
        data_type : typing___Optional[typing___Text] = None,
        data_name : typing___Optional[typing___Text] = None,
        custom : typing___Optional[builtin___bool] = None,
        version : typing___Optional[builtin___float] = None,
        formats : typing___Optional[typing___Iterable[Metrics.Formats]] = None,
        org : typing___Optional[builtin___int] = None,
        _id : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        modifier : typing___Optional[typing___Text] = None,
        ctime : typing___Optional[typing___Text] = None,
        mtime : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Metrics: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Metrics: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"_id",b"_id",u"creator",b"creator",u"ctime",b"ctime",u"custom",b"custom",u"data_name",b"data_name",u"data_type",b"data_type",u"description",b"description",u"formats",b"formats",u"modifier",b"modifier",u"mtime",b"mtime",u"org",b"org",u"retention_policy",b"retention_policy",u"version",b"version"]) -> None: ...