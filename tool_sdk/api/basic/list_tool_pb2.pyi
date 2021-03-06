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

from tool_sdk.model.tool.tool_pb2 import (
    Tool as tool_sdk___model___tool___tool_pb2___Tool,
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


class ListToolRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    detail = ... # type: builtin___bool
    plugin = ... # type: builtin___bool
    category = ... # type: typing___Text
    permissions = ... # type: typing___Text
    onlyProduction = ... # type: builtin___bool
    showInvisible = ... # type: builtin___bool
    tags = ... # type: typing___Text

    def __init__(self,
        *,
        detail : typing___Optional[builtin___bool] = None,
        plugin : typing___Optional[builtin___bool] = None,
        category : typing___Optional[typing___Text] = None,
        permissions : typing___Optional[typing___Text] = None,
        onlyProduction : typing___Optional[builtin___bool] = None,
        showInvisible : typing___Optional[builtin___bool] = None,
        tags : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListToolRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListToolRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"category",b"category",u"detail",b"detail",u"onlyProduction",b"onlyProduction",u"permissions",b"permissions",u"plugin",b"plugin",u"showInvisible",b"showInvisible",u"tags",b"tags"]) -> None: ...

class ListToolResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    page = ... # type: builtin___int
    page_size = ... # type: builtin___int
    total = ... # type: builtin___int

    @property
    def list(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[tool_sdk___model___tool___tool_pb2___Tool]: ...

    def __init__(self,
        *,
        page : typing___Optional[builtin___int] = None,
        page_size : typing___Optional[builtin___int] = None,
        total : typing___Optional[builtin___int] = None,
        list : typing___Optional[typing___Iterable[tool_sdk___model___tool___tool_pb2___Tool]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListToolResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListToolResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"list",b"list",u"page",b"page",u"page_size",b"page_size",u"total",b"total"]) -> None: ...

class ListToolResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> ListToolResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[ListToolResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListToolResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListToolResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
