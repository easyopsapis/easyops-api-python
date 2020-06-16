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

from translate_sdk.model.monitor.translate_rule_pb2 import (
    TransalteRule as translate_sdk___model___monitor___translate_rule_pb2___TransalteRule,
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


class TranslateDataNameListHandlerRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    page = ... # type: builtin___int
    page_size = ... # type: builtin___int
    relate = ... # type: builtin___bool
    data_name = ... # type: typing___Text
    data_name__in = ... # type: typing___Text

    def __init__(self,
        *,
        page : typing___Optional[builtin___int] = None,
        page_size : typing___Optional[builtin___int] = None,
        relate : typing___Optional[builtin___bool] = None,
        data_name : typing___Optional[typing___Text] = None,
        data_name__in : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> TranslateDataNameListHandlerRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> TranslateDataNameListHandlerRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"data_name",b"data_name",u"data_name__in",b"data_name__in",u"page",b"page",u"page_size",b"page_size",u"relate",b"relate"]) -> None: ...

class TranslateDataNameListHandlerResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Data(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class Formats(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            class Fields(google___protobuf___message___Message):
                DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
                field_type = ... # type: typing___Text
                description = ... # type: typing___Text
                field_name = ... # type: typing___Text
                field_value_type = ... # type: typing___Text
                unit = ... # type: typing___Text

                def __init__(self,
                    *,
                    field_type : typing___Optional[typing___Text] = None,
                    description : typing___Optional[typing___Text] = None,
                    field_name : typing___Optional[typing___Text] = None,
                    field_value_type : typing___Optional[typing___Text] = None,
                    unit : typing___Optional[typing___Text] = None,
                    ) -> None: ...
                if sys.version_info >= (3,):
                    @classmethod
                    def FromString(cls, s: builtin___bytes) -> TranslateDataNameListHandlerResponse.Data.Formats.Fields: ...
                else:
                    @classmethod
                    def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> TranslateDataNameListHandlerResponse.Data.Formats.Fields: ...
                def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
                def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
                def ClearField(self, field_name: typing_extensions___Literal[u"description",b"description",u"field_name",b"field_name",u"field_type",b"field_type",u"field_value_type",b"field_value_type",u"unit",b"unit"]) -> None: ...

            config_id = ... # type: typing___Text
            table = ... # type: typing___Text

            @property
            def fields(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[TranslateDataNameListHandlerResponse.Data.Formats.Fields]: ...

            def __init__(self,
                *,
                config_id : typing___Optional[typing___Text] = None,
                fields : typing___Optional[typing___Iterable[TranslateDataNameListHandlerResponse.Data.Formats.Fields]] = None,
                table : typing___Optional[typing___Text] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> TranslateDataNameListHandlerResponse.Data.Formats: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> TranslateDataNameListHandlerResponse.Data.Formats: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"config_id",b"config_id",u"fields",b"fields",u"table",b"table"]) -> None: ...

        org = ... # type: builtin___int
        creator = ... # type: typing___Text
        modifier = ... # type: typing___Text
        description = ... # type: typing___Text
        retention_policy = ... # type: typing___Text
        data_type = ... # type: typing___Text
        data_name = ... # type: typing___Text
        custom = ... # type: builtin___bool
        version = ... # type: builtin___float

        @property
        def formats(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[TranslateDataNameListHandlerResponse.Data.Formats]: ...

        @property
        def translate_rules(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[translate_sdk___model___monitor___translate_rule_pb2___TransalteRule]: ...

        def __init__(self,
            *,
            org : typing___Optional[builtin___int] = None,
            creator : typing___Optional[typing___Text] = None,
            modifier : typing___Optional[typing___Text] = None,
            description : typing___Optional[typing___Text] = None,
            retention_policy : typing___Optional[typing___Text] = None,
            data_type : typing___Optional[typing___Text] = None,
            data_name : typing___Optional[typing___Text] = None,
            custom : typing___Optional[builtin___bool] = None,
            version : typing___Optional[builtin___float] = None,
            formats : typing___Optional[typing___Iterable[TranslateDataNameListHandlerResponse.Data.Formats]] = None,
            translate_rules : typing___Optional[typing___Iterable[translate_sdk___model___monitor___translate_rule_pb2___TransalteRule]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> TranslateDataNameListHandlerResponse.Data: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> TranslateDataNameListHandlerResponse.Data: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"creator",b"creator",u"custom",b"custom",u"data_name",b"data_name",u"data_type",b"data_type",u"description",b"description",u"formats",b"formats",u"modifier",b"modifier",u"org",b"org",u"retention_policy",b"retention_policy",u"translate_rules",b"translate_rules",u"version",b"version"]) -> None: ...

    code = ... # type: builtin___int
    page_size = ... # type: builtin___int
    msg = ... # type: typing___Text
    total = ... # type: builtin___int
    page = ... # type: builtin___int

    @property
    def data(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[TranslateDataNameListHandlerResponse.Data]: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        page_size : typing___Optional[builtin___int] = None,
        msg : typing___Optional[typing___Text] = None,
        total : typing___Optional[builtin___int] = None,
        page : typing___Optional[builtin___int] = None,
        data : typing___Optional[typing___Iterable[TranslateDataNameListHandlerResponse.Data]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> TranslateDataNameListHandlerResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> TranslateDataNameListHandlerResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"data",b"data",u"msg",b"msg",u"page",b"page",u"page_size",b"page_size",u"total",b"total"]) -> None: ...

class TranslateDataNameListHandlerResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> TranslateDataNameListHandlerResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[TranslateDataNameListHandlerResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> TranslateDataNameListHandlerResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> TranslateDataNameListHandlerResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
