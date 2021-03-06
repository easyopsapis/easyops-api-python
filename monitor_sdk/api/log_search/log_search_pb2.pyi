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

from monitor_sdk.model.log_search.log_search_data_pb2 import (
    LogSearchData as monitor_sdk___model___log_search___log_search_data_pb2___LogSearchData,
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


class LogSearchRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    log_file_name = ... # type: typing___Text
    enabled_file_pattern = ... # type: builtin___bool
    keywords = ... # type: typing___Text
    max_return_lines = ... # type: typing___Text
    before_lines = ... # type: builtin___int
    after_lines = ... # type: builtin___int
    agents = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

    def __init__(self,
        *,
        log_file_name : typing___Optional[typing___Text] = None,
        enabled_file_pattern : typing___Optional[builtin___bool] = None,
        keywords : typing___Optional[typing___Text] = None,
        max_return_lines : typing___Optional[typing___Text] = None,
        before_lines : typing___Optional[builtin___int] = None,
        after_lines : typing___Optional[builtin___int] = None,
        agents : typing___Optional[typing___Iterable[typing___Text]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> LogSearchRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> LogSearchRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"after_lines",b"after_lines",u"agents",b"agents",u"before_lines",b"before_lines",u"enabled_file_pattern",b"enabled_file_pattern",u"keywords",b"keywords",u"log_file_name",b"log_file_name",u"max_return_lines",b"max_return_lines"]) -> None: ...

class LogSearchResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    message = ... # type: typing___Text

    @property
    def data(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[monitor_sdk___model___log_search___log_search_data_pb2___LogSearchData]: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        message : typing___Optional[typing___Text] = None,
        data : typing___Optional[typing___Iterable[monitor_sdk___model___log_search___log_search_data_pb2___LogSearchData]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> LogSearchResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> LogSearchResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"data",b"data",u"message",b"message"]) -> None: ...

class LogSearchResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> LogSearchResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[LogSearchResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> LogSearchResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> LogSearchResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
