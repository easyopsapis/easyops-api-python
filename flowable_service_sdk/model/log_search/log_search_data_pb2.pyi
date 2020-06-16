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


class LogSearchData(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Data(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class Content(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            code = ... # type: builtin___int
            file_path = ... # type: typing___Text
            text = ... # type: typing___Text

            def __init__(self,
                *,
                code : typing___Optional[builtin___int] = None,
                file_path : typing___Optional[typing___Text] = None,
                text : typing___Optional[typing___Text] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> LogSearchData.Data.Content: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> LogSearchData.Data.Content: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"file_path",b"file_path",u"text",b"text"]) -> None: ...

        max_query_lines = ... # type: builtin___int
        max_return_lines = ... # type: builtin___int

        @property
        def content(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[LogSearchData.Data.Content]: ...

        def __init__(self,
            *,
            max_query_lines : typing___Optional[builtin___int] = None,
            max_return_lines : typing___Optional[builtin___int] = None,
            content : typing___Optional[typing___Iterable[LogSearchData.Data.Content]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> LogSearchData.Data: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> LogSearchData.Data: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"content",b"content",u"max_query_lines",b"max_query_lines",u"max_return_lines",b"max_return_lines"]) -> None: ...

    code = ... # type: builtin___int
    ip = ... # type: typing___Text
    msg = ... # type: typing___Text

    @property
    def data(self) -> LogSearchData.Data: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        ip : typing___Optional[typing___Text] = None,
        msg : typing___Optional[typing___Text] = None,
        data : typing___Optional[LogSearchData.Data] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> LogSearchData: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> LogSearchData: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"data",b"data",u"ip",b"ip",u"msg",b"msg"]) -> None: ...